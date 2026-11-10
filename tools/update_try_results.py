"""Write the results of the "Try it" SPARQL boxes into the training pages.

A "Try it" box is a collapsible admonition with the class `try-sparql`. It holds
data (```` ```turtle { .try-data } ```` blocks or links with `{ .try-data }`) and
queries (```` ```sparql { .try-query } ````). `assets/training-sparql.js` runs
the queries in the browser, with Oxigraph compiled to WebAssembly.

This command runs the same queries with pyoxigraph, the Python build of the same
engine and version, and writes each result under its query:

    <div class="try-result" markdown>

    2 rows

    | name |
    | --- |
    | `"BARCO"` |

    </div>

So the result is part of the page without JavaScript, in the PDF and in search,
and the browser shows it before anything is run. The `try-result` blocks are
generated: they are replaced on every run and never edited by hand. `--check`
fails when a page states a result its data no longer gives.
"""

from __future__ import annotations

import difflib
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import click
from pyoxigraph import QueryBoolean, QuerySolutions, RdfFormat, Store

MAX_ROWS = 10
XSD_STRING = "http://www.w3.org/2001/XMLSchema#string"
DEFAULT_PREFIXES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}

BOX_START = re.compile(r'^(?P<indent>[ ]*)(?:\?\?\?\+?|!!!) [^\n"]*\btry-sparql\b[^\n"]*"[^"\n]*"[ ]*$')
FENCE = re.compile(r"^```(?P<info>.*)$")
DATA_LINK = re.compile(r"\]\((?P<href>[^)\s]+)\)\{ *\.try-data *\}")
RESULT_START = '<div class="try-result" markdown>'
RESULT_END = "</div>"
PREFIX_DECL = re.compile(r"(?:@prefix|PREFIX)\s+([A-Za-z][\w.-]*)?:\s*<([^>\s]*)>", re.IGNORECASE)
LOCAL_NAME = re.compile(r"^(?:[\w.-]|%[0-9A-Fa-f]{2})*$")
FORM = re.compile(
    r"\b(SELECT|ASK|CONSTRUCT|DESCRIBE|INSERT|DELETE|LOAD|CLEAR|DROP|CREATE|ADD|MOVE|COPY|WITH)\b",
    re.IGNORECASE,
)


# --- terms, the same rendering as assets/training-sparql.js ----------------


def prefixes_of(texts: list[str]) -> list[tuple[str, str]]:
    """Prefix declarations of the texts, longest namespace first."""
    prefixes = dict(DEFAULT_PREFIXES)
    for text in texts:
        for name, iri in PREFIX_DECL.findall(text):
            prefixes[name or ""] = iri
    return sorted(prefixes.items(), key=lambda p: -len(p[1]))


def compact(iri: str, prefixes: list[tuple[str, str]]) -> str:
    for name, namespace in prefixes:
        if iri.startswith(namespace):
            local = iri[len(namespace):]
            if LOCAL_NAME.match(local) and not re.search(r"^[.-]|\.$", local):
                return f"{name}:{local}"
    return f"<{iri}>"


def term_text(term, prefixes: list[tuple[str, str]]) -> str:
    if term is None:
        return ""
    kind = type(term).__name__
    if kind == "NamedNode":
        return compact(term.value, prefixes)
    if kind == "BlankNode":
        return f"_:{term.value}"
    text = f'"{term.value}"'
    if term.language:
        return f"{text}@{term.language}"
    if term.datatype.value != XSD_STRING:
        return f"{text}^^{compact(term.datatype.value, prefixes)}"
    return text


def cell(text: str) -> str:
    if not text:
        return ""
    ticks = "``" if "`" in text else "`"
    pad = " " if ticks == "``" else ""
    return f"{ticks}{pad}{text}{pad}{ticks}"


def count(n: int, what: str, shown: int = MAX_ROWS) -> str:
    text = f"{n} {what}{'' if n == 1 else 's'}"
    return text + (f", the first {shown} shown" if n > shown else "")


def table(columns: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows[:MAX_ROWS]:
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")
    return lines


# --- running ---------------------------------------------------------------


def form_of(query: str) -> str:
    """The query form or, for an update, its first operation."""
    stripped = re.sub(r"<[^>\s]*>", "<>", query)
    stripped = re.sub(r'"(?:[^"\\\n]|\\.)*"|\'(?:[^\'\\\n]|\\.)*\'', '""', stripped)
    stripped = re.sub(r"#.*$", "", stripped, flags=re.MULTILINE)
    match = FORM.search(stripped)
    return match.group(1).upper() if match else "SELECT"


def run_query(store: Store, query: str, prefix_texts: list[str]) -> list[str]:
    """Run one query or update and return the Markdown lines of its result."""
    prefixes = prefixes_of([query, *prefix_texts])
    form = form_of(query)
    if form in ("SELECT", "ASK", "CONSTRUCT", "DESCRIBE"):
        result = store.query(query, use_default_graph_as_union=True)
        if isinstance(result, QueryBoolean):
            return [f"Answer: {'true' if bool(result) else 'false'}"]
        if isinstance(result, QuerySolutions):
            variables = [v.value for v in result.variables]
            rows = [[term_text(s[v], prefixes) for v in variables] for s in result]
            return [count(len(rows), "row"), "", *table(variables, rows)]
        triples = [[term_text(t.subject, prefixes), term_text(t.predicate, prefixes),
                    term_text(t.object, prefixes)] for t in result]
        return [count(len(triples), "triple"), "", *table(["subject", "predicate", "object"], triples)]
    before = len(store)
    store.update(query)
    change = len(store) - before
    changed = f" ({change:+d})" if change else ""
    triples = "triple" if len(store) == 1 else "triples"
    return [f"Update done{changed}, the store holds {len(store)} {triples}."]


@dataclass
class Box:
    """One try-sparql admonition: where its body starts and its data."""

    indent: str
    data: list[str] = field(default_factory=list)
    files: list[Path] = field(default_factory=list)


def strip_results(lines: list[str]) -> list[str]:
    """Drop every generated try-result block and the blank line before it."""
    out: list[str] = []
    skipping = False
    for line in lines:
        if skipping:
            skipping = line.strip() != RESULT_END
            continue
        if line.strip() == RESULT_START:
            if out and not out[-1].strip():
                out.pop()
            skipping = True
            continue
        out.append(line)
    return out


def render_page(text: str, page: Path) -> str:
    """The page text with the result of every try-sparql query written under it."""
    lines = strip_results(text.split("\n"))
    out: list[str] = []
    box: Box | None = None
    store: Store | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        start = BOX_START.match(line)
        if start:
            box = Box(indent=start.group("indent") + "    ")
            store = None
            out.append(line)
            i += 1
            continue
        if box is not None and line.strip() and not line.startswith(box.indent):
            box = None
        if box is None:
            out.append(line)
            i += 1
            continue

        body = line[len(box.indent):]
        link = DATA_LINK.search(body)
        if link:
            box.files.append(page.parent / link.group("href"))
        fence = FENCE.match(body)
        if not fence:
            out.append(line)
            i += 1
            continue

        # a fenced block inside the box: copy it through to its closing fence
        info = fence.group("info")
        block: list[str] = []
        out.append(line)
        i += 1
        while i < len(lines) and lines[i][len(box.indent):] != "```":
            block.append(lines[i][len(box.indent):])
            out.append(lines[i])
            i += 1
        out.append(lines[i])
        i += 1
        code = "\n".join(block)
        if ".try-data" in info:
            box.data.append(code)
        elif ".try-query" in info:
            if store is None:
                store = load_store(box)
            prefix_texts = box.data + [f.read_text(encoding="utf-8") for f in box.files]
            try:
                result = run_query(store, code, prefix_texts)
            except (SyntaxError, OSError, ValueError) as error:
                raise click.ClickException(f"{page}: query fails: {error}\n{code}") from error
            out.append("")
            out.append(box.indent + RESULT_START)
            out.append("")
            out.extend((box.indent + r).rstrip() for r in result)
            out.append("")
            out.append(box.indent + RESULT_END)
    return "\n".join(out)


def load_store(box: Box) -> Store:
    store = Store()
    for data in box.data:
        store.load(data, format=RdfFormat.TURTLE)
    for file in box.files:
        fmt = RdfFormat.N_TRIPLES if file.suffix == ".nt" else RdfFormat.TURTLE
        store.load(path=str(file), format=fmt)
    return store


def pages_with_boxes(docs_dir: Path) -> list[Path]:
    return sorted(
        p for p in docs_dir.rglob("*.md")
        if "try-sparql" in p.read_text(encoding="utf-8")
    )


@click.command()
@click.option(
    "--docs-dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default="docs",
    help="Where to look for pages with try-sparql boxes?",
    show_default=True,
)
@click.option(
    "--check",
    is_flag=True,
    help="Compare the written results instead of writing them, exit 1 on drift.",
)
def update_try_results(docs_dir: str, check: bool) -> None:
    """Write the results of the try-sparql boxes under their queries."""
    drift = False
    for page in pages_with_boxes(Path(docs_dir)):
        current = page.read_text(encoding="utf-8")
        output = render_page(current, page)
        if current == output:
            click.echo(f"{page}: results are up to date.")
            continue
        if not check:
            click.echo(f"{page}: write the results.")
            page.write_text(output, encoding="utf-8")
            continue
        drift = True
        diff = difflib.unified_diff(
            current.splitlines(keepends=True),
            output.splitlines(keepends=True),
            fromfile=str(page),
            tofile=f"{page} (queries run)",
        )
        click.echo("".join(diff), nl=False)
        click.echo()
        click.echo(f"{page}: the written results differ from what the queries return.")
    if drift:
        click.echo("Run 'task update:try-results' and commit the result.")
        sys.exit(1)
