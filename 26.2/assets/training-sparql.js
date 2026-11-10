/*
 * Training pages: SPARQL queries that run in the browser.
 *
 * A "Try it" box is a collapsible admonition with the class try-sparql:
 *
 *   ??? example try-sparql "Try it"
 *
 *       ```turtle { .try-data }               data, shown and editable
 *       ```
 *
 *       Data: [product data](data/x.ttl){ .try-data }   or a data file
 *
 *       ```sparql { .try-query }              one or more queries, each with Run
 *       ```
 *
 * `task update:try-results` (tools/update_try_results.py) writes the result of
 * every query into the page, as a div.try-result under the query, so the box
 * reads as data, query and result without JavaScript and in the PDF.
 * With JavaScript, the code blocks become editable and every query gets a Run
 * button. The written result stays until the query or the data is edited, then
 * it is greyed out until the next Run replaces it.
 * The queries of one box share one in-memory store, built from the data on the
 * first Run, so an update changes what the next query of the box sees.
 * Reset restores the original text, data and results.
 *
 * The engine is Oxigraph 0.5.13 (npm package oxigraph, MIT OR Apache-2.0),
 * its web build copied to assets/oxigraph/. The WebAssembly file is loaded on
 * the first Run only.
 */
(function () {
  "use strict";

  var base = new URL(".", document.currentScript.src).href;
  var MAX_ROWS = 100;
  var XSD_STRING = "http://www.w3.org/2001/XMLSchema#string";

  var engine = null; // promise of the initialized oxigraph module
  var files = {}; // data file URL -> promise of its text

  function loadEngine() {
    if (!engine) {
      engine = import(base + "oxigraph/web.js").then(function (ox) {
        return ox.default({ module_or_path: base + "oxigraph/web_bg.wasm" }).then(function () {
          return ox;
        });
      });
      engine.catch(function () {
        engine = null;
      });
    }
    return engine;
  }

  function loadFile(url) {
    if (!files[url]) {
      files[url] = fetch(url).then(function (response) {
        if (!response.ok) throw new Error("Cannot load " + url + ": HTTP " + response.status);
        return response.text();
      });
      files[url].catch(function () {
        delete files[url];
      });
    }
    return files[url];
  }

  function el(tag, className, text) {
    var e = document.createElement(tag);
    if (className) e.className = className;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function button(label, title, onClick) {
    var b = el("button", "try-sparql__button", label);
    b.type = "button";
    b.title = title;
    b.addEventListener("click", onClick);
    return b;
  }

  function codeOf(block) {
    return block.querySelector("code");
  }

  function textOf(block) {
    return codeOf(block).innerText.replace(/\n$/, "");
  }

  // --- terms ------------------------------------------------------------

  function prefixesOf(texts) {
    var prefixes = [
      { name: "rdf", iri: "http://www.w3.org/1999/02/22-rdf-syntax-ns#" },
      { name: "rdfs", iri: "http://www.w3.org/2000/01/rdf-schema#" },
      { name: "xsd", iri: "http://www.w3.org/2001/XMLSchema#" }
    ];
    var re = /(?:@prefix|PREFIX)\s+([A-Za-z][\w.-]*)?:\s*<([^>\s]*)>/gi;
    texts.forEach(function (text) {
      var m;
      while ((m = re.exec(text))) prefixes.push({ name: m[1] || "", iri: m[2] });
    });
    // longest namespace first, so ex: does not shadow ex-sub:
    return prefixes.sort(function (a, b) {
      return b.iri.length - a.iri.length;
    });
  }

  function compact(iri, prefixes) {
    for (var i = 0; i < prefixes.length; i++) {
      var p = prefixes[i];
      if (iri.indexOf(p.iri) === 0) {
        var local = iri.slice(p.iri.length);
        // a Turtle local name: % only as an escape, no leading - or ., no trailing .
        if (/^(?:[\w.-]|%[0-9A-Fa-f]{2})*$/.test(local) && !/^[.-]|\.$/.test(local)) {
          return p.name + ":" + local;
        }
      }
    }
    return "<" + iri + ">";
  }

  // a term as JSON results give it, or an RDF/JS term from a graph result
  function termCell(term, prefixes) {
    var td = el("td");
    if (!term) return td;
    var type = term.type || term.termType;
    if (type === "uri" || type === "NamedNode") {
      td.textContent = compact(term.value, prefixes);
      td.title = term.value;
    } else if (type === "bnode" || type === "BlankNode") {
      td.textContent = "_:" + term.value;
    } else {
      var lang = term["xml:lang"] || term.language;
      var datatype = term.datatype && (term.datatype.value || term.datatype);
      td.textContent = "\"" + term.value + "\"";
      if (lang) {
        td.appendChild(el("span", "try-sparql__suffix", "@" + lang));
      } else if (datatype && datatype !== XSD_STRING) {
        td.appendChild(el("span", "try-sparql__suffix", "^^" + compact(datatype, prefixes)));
      }
    }
    return td;
  }

  function table(columns, rows, cellsOf, prefixes) {
    var t = el("table");
    var head = t.createTHead().insertRow();
    columns.forEach(function (c) {
      head.appendChild(el("th", null, c));
    });
    var body = t.createTBody();
    rows.slice(0, MAX_ROWS).forEach(function (row) {
      var tr = body.insertRow();
      cellsOf(row).forEach(function (term) {
        tr.appendChild(termCell(term, prefixes));
      });
    });
    return t;
  }

  function count(n, what) {
    return n + " " + what + (n === 1 ? "" : "s") + (n > MAX_ROWS ? ", the first " + MAX_ROWS + " shown" : "");
  }

  // --- running --------------------------------------------------------------

  // the first keyword after the prologue decides between query forms and update
  function formOf(query) {
    var stripped = query
      .replace(/<[^>\s]*>/g, "<>")
      .replace(/"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*'/g, "\"\"")
      .replace(/#.*$/gm, "");
    var m = /\b(SELECT|ASK|CONSTRUCT|DESCRIBE|INSERT|DELETE|LOAD|CLEAR|DROP|CREATE|ADD|MOVE|COPY|WITH)\b/i.exec(stripped);
    return m ? m[1].toUpperCase() : "SELECT";
  }

  function storeOf(box, ox) {
    if (box.store) return Promise.resolve(box.store);
    return Promise.all(box.sources.map(function (source) {
      if (source.block) return { text: textOf(source.block), format: "text/turtle", name: "the data" };
      return loadFile(source.url).then(function (text) {
        var format = /\.nt$/.test(source.url) ? "application/n-triples" : "text/turtle";
        return { text: text, format: format, name: source.url.split("/").pop() };
      });
    })).then(function (data) {
      var store = new ox.Store();
      data.forEach(function (d) {
        try {
          store.load(d.text, { format: d.format, base_iri: window.location.href });
        } catch (error) {
          throw new Error("Error in " + d.name + ": " + (error.message || error));
        }
      });
      box.prefixTexts = data.map(function (d) {
        return d.format === "text/turtle" ? d.text : "";
      });
      box.store = store;
      return store;
    });
  }

  function run(box, query) {
    var result = query.result;
    var status = query.status;
    status.textContent = box.store ? "Running …" : "Loading the query engine and the data …";
    status.classList.remove("try-sparql__status--error");
    result.classList.remove("try-sparql__result--stale");
    result.replaceChildren();

    loadEngine().then(function (ox) {
      return storeOf(box, ox).then(function (store) {
        var text = textOf(query.block);
        var prefixes = prefixesOf([text].concat(box.prefixTexts));
        var form = formOf(text);
        var options = { base_iri: window.location.href, use_default_graph_as_union: true };

        if (form === "SELECT") {
          options.results_format = "json";
          var json = JSON.parse(store.query(text, options));
          var vars = json.head.vars;
          var rows = json.results.bindings;
          status.textContent = count(rows.length, "row");
          result.appendChild(table(vars, rows, function (row) {
            return vars.map(function (v) { return row[v]; });
          }, prefixes));
        } else if (form === "ASK") {
          status.textContent = "Answer: " + store.query(text, options);
        } else if (form === "CONSTRUCT" || form === "DESCRIBE") {
          var quads = store.query(text, options);
          status.textContent = count(quads.length, "triple");
          result.appendChild(table(["subject", "predicate", "object"], quads, function (q) {
            return [q.subject, q.predicate, q.object];
          }, prefixes));
        } else {
          var before = store.size;
          store.update(text, { base_iri: window.location.href });
          var change = store.size - before;
          status.textContent = "Update done" +
            (change ? " (" + (change > 0 ? "+" : "") + change + ")" : "") +
            ", the store holds " + store.size + (store.size === 1 ? " triple." : " triples.");
        }
      });
    }).catch(function (error) {
      status.textContent = String(error && error.message || error);
      status.classList.add("try-sparql__status--error");
    });
  }

  // --- setup ----------------------------------------------------------------

  // the shown result no longer belongs to the text above it
  function stale(query) {
    if (query.result.classList.contains("try-sparql__result--stale")) return;
    query.result.classList.add("try-sparql__result--stale");
    query.status.classList.remove("try-sparql__status--error");
    query.status.textContent = "Edited, Run to update the result";
  }

  function editable(block, onEdit) {
    var code = codeOf(block);
    code.setAttribute("contenteditable", "plaintext-only");
    if (code.contentEditable !== "plaintext-only") code.setAttribute("contenteditable", "true");
    code.setAttribute("spellcheck", "false");
    code.setAttribute("autocapitalize", "off");
    code.setAttribute("aria-label", "Editable code");
    block.classList.add("try-sparql__editable");
    block.dataset.original = code.innerHTML;
    if (onEdit) code.addEventListener("input", onEdit);
  }

  function init(box) {
    if (box.dataset.tryReady) return;
    box.dataset.tryReady = "true";

    var dataBlocks = box.querySelectorAll("div.try-data");
    var dataLinks = box.querySelectorAll("a.try-data");
    var queryBlocks = box.querySelectorAll("div.try-query");
    if (!queryBlocks.length) return;

    var state = { store: null, sources: [], prefixTexts: [], queries: [] };
    var invalidate = function () {
      state.store = null;
      state.queries.forEach(stale);
    };

    dataBlocks.forEach(function (block) {
      editable(block, invalidate);
      state.sources.push({ block: block });
    });
    dataLinks.forEach(function (a) {
      state.sources.push({ url: a.href });
    });

    queryBlocks.forEach(function (block) {
      var bar = el("div", "try-sparql__bar");
      var status = el("span", "try-sparql__status");
      status.setAttribute("aria-live", "polite");

      // the result written into the page by `task update:try-results`:
      // its first paragraph is the status line, the rest stays as the result
      var next = block.nextElementSibling;
      var result = next && next.matches("div.try-result") ? next : el("div");
      result.classList.add("try-sparql__result");
      var written = result.querySelector(":scope > p");
      if (written) {
        status.textContent = written.textContent;
        written.remove();
      }

      var query = {
        block: block, status: status, result: result,
        writtenStatus: status.textContent, writtenResult: result.innerHTML
      };
      editable(block, function () { stale(query); });
      bar.appendChild(button("▶ Run", "Run the query (Ctrl+Enter)", function () {
        run(state, query);
      }));
      bar.appendChild(status);
      block.after(bar, result);
      codeOf(block).addEventListener("keydown", function (event) {
        if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
          event.preventDefault();
          run(state, query);
        }
      });
      state.queries.push(query);
    });

    var hint = el("p", "try-sparql__hint",
      "Edit the data or a query and run it in the browser. " +
      "The queries of this box share one store, so an update affects the queries after it.");
    var reset = button("Reset", "Restore the original data, queries and results", function () {
      box.querySelectorAll(".try-sparql__editable").forEach(function (block) {
        codeOf(block).innerHTML = block.dataset.original;
      });
      state.store = null;
      state.queries.forEach(function (q) {
        q.status.textContent = q.writtenStatus;
        q.status.classList.remove("try-sparql__status--error");
        q.result.innerHTML = q.writtenResult;
        q.result.classList.remove("try-sparql__result--stale");
      });
    });
    reset.classList.add("try-sparql__reset");
    hint.appendChild(reset);
    var summary = box.querySelector(":scope > summary, :scope > .admonition-title");
    if (summary) summary.after(hint);
    else box.prepend(hint);
  }

  function scan() {
    document.querySelectorAll(".try-sparql").forEach(init);
  }

  // navigation.instant swaps the page content without a reload: document$
  // emits on every page, the plain listener covers a build without it
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(scan);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scan);
  } else {
    scan();
  }
})();
