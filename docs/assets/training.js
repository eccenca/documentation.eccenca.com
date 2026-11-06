/*
 * Training pages: a slide deck above the fold, the explanations below.
 *
 * A training page embeds its deck with
 *
 *   <div class="training-deck"><iframe src="slides.html" ...></iframe></div>
 *
 * and this script adds the control bar under the deck and ties slides to the
 * explanations: the bar links to the explanation of the current slide, and every
 * explained heading gets a button that shows its slide in the deck.
 * The deck side of the protocol is assets/revealjs/training-deck.js.
 */
(function () {
  "use strict";

  var decks = new Map(); // iframe contentWindow -> deck state

  function button(label, title, onClick) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "training-deck__button";
    b.textContent = label;
    b.title = title;
    b.setAttribute("aria-label", title);
    b.addEventListener("click", onClick);
    return b;
  }

  function send(state, message) {
    if (state.frame.contentWindow) {
      state.frame.contentWindow.postMessage(message, window.location.origin === "null" ? "*" : window.location.origin);
    }
  }

  function init(root) {
    if (root.dataset.trainingReady) return;
    root.dataset.trainingReady = "true";

    var frame = root.querySelector("iframe");
    if (!frame) return;

    var state = { root: root, frame: frame, slides: [], current: null };

    var bar = document.createElement("div");
    bar.className = "training-deck__bar";

    var nav = document.createElement("div");
    nav.className = "training-deck__nav";
    nav.appendChild(button("‹", "Previous slide", function () {
      send(state, { type: "training-deck:command", command: "prev" });
    }));
    var position = document.createElement("span");
    position.className = "training-deck__position";
    position.textContent = "Loading slides …";
    nav.appendChild(position);
    nav.appendChild(button("›", "Next slide", function () {
      send(state, { type: "training-deck:command", command: "next" });
    }));

    var explain = document.createElement("a");
    explain.className = "training-deck__explain";
    explain.hidden = true;

    var tools = document.createElement("div");
    tools.className = "training-deck__tools";
    tools.appendChild(button("Speaker notes", "Open the speaker view with the notes for each slide", function () {
      send(state, { type: "training-deck:command", command: "notes" });
    }));
    tools.appendChild(button("Fullscreen", "Show the slides in fullscreen", function () {
      if (frame.requestFullscreen) frame.requestFullscreen();
    }));
    var open = document.createElement("a");
    open.className = "training-deck__button";
    open.href = frame.getAttribute("src");
    open.target = "_blank";
    open.rel = "noopener";
    open.textContent = "Open in new tab";
    tools.appendChild(open);

    bar.appendChild(nav);
    bar.appendChild(explain);
    bar.appendChild(tools);
    root.appendChild(bar);

    state.position = position;
    state.explain = explain;

    // the WindowProxy of an iframe stays the same object across its loads
    decks.set(frame.contentWindow, state);
    send(state, { type: "training-deck:hello" });
  }

  function linkHeadings(state) {
    var seen = {};
    state.slides.forEach(function (slide) {
      if (!slide.explainer || !slide.id || seen[slide.explainer]) return;
      seen[slide.explainer] = true;
      var heading = document.getElementById(slide.explainer);
      if (!heading || heading.querySelector(".training-show-slide")) return;
      var b = button("Show slide", "Show the slide \"" + slide.title + "\" in the deck above", function () {
        send(state, { type: "training-deck:goto", id: slide.id });
        state.root.scrollIntoView({ behavior: "smooth", block: "start" });
      });
      b.classList.add("training-show-slide");
      heading.appendChild(b);
    });
  }

  function update(state, slide) {
    state.current = slide;
    state.position.textContent = slide.index + " / " + slide.total + (slide.title ? " · " + slide.title : "");

    document.querySelectorAll(".training-current").forEach(function (el) {
      el.classList.remove("training-current");
    });

    var heading = slide.explainer ? document.getElementById(slide.explainer) : null;
    if (heading) {
      heading.classList.add("training-current");
      state.explain.href = "#" + slide.explainer;
      state.explain.textContent = "Read the explanation ↓";
      state.explain.hidden = false;
    } else {
      state.explain.hidden = true;
    }
  }

  window.addEventListener("message", function (event) {
    var state = decks.get(event.source);
    if (!state || !event.data || typeof event.data !== "object") return;
    if (event.data.type === "training-deck:ready") {
      state.slides = event.data.slides || [];
      linkHeadings(state);
    } else if (event.data.type === "training-deck:slide") {
      update(state, event.data);
    }
  });

  function scan() {
    document.querySelectorAll(".training-deck").forEach(init);
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
