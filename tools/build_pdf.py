"""Build a single PDF of the whole documentation with pandoc and Typst.

The page order is `nav.yml` - the generated, `check:navigation` gated
navigation spine. Each page's article is taken from the built `site/`, so every
Markdown extension (admonitions, tabs, snippets, macros, icons) is already
resolved when this script sees it. The articles are merged into one HTML
document, normalized into plain elements pandoc's HTML reader understands,
converted to Typst by pandoc with `tools/pdf/filter.lua`, and typeset by Typst
with the eccenca house style in `tools/pdf/style.typ`.

`--edition print` builds the book block of a printed book instead of the screen
PDF: the same pipeline, shortened by the section modes in `tools/pdf/print.yml`,
with images copied at 300 ppi without transparency, and typeset by the print
branches of the style (tasks/spec.md).

Invoked by `task pdf` and `task pdf:print`. Every option falls back to an
environment variable, so BUILD_VERSION, PDF_EDITION, PDF_OUT, PANDOC and TYPST
keep working as tunables.
"""
from __future__ import annotations

import base64
import hashlib
import io
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import click
import yaml
from bs4 import BeautifulSoup, NavigableString
from PIL import Image

DEFAULT_OUT_STEM = "dist/documentation-eccenca-com"
SITE_DIR = Path("site")
NAV_YML = Path("nav.yml")
MKDOCS_YML = Path("mkdocs.yml")
# Style, pandoc template, filter, logo and vendored fonts.
PDF_ASSETS = Path("tools/pdf")
# Publisher and section modes of the print edition.
PRINT_YML = PDF_ASSETS / "print.yml"
# The merged HTML and the Typst source pandoc writes, kept for debugging.
WORK_DIR = Path("dist/pdf")
CONTENT_SELECTOR = "article.md-content__inner"
HEADING_TAGS = ("h1", "h2", "h3", "h4", "h5", "h6")
HEADING = re.compile(r"^h[1-6]$")
# Interactive widgets and web-only chrome that carry no meaning in a PDF.
NOISE_SELECTORS = (
    "#__comments", ".giscus", ".md-feedback", ".md-source-file", ".md-content__button",
    "a.headerlink", "script", "style", "input", "button", "noscript", "form", "nav",
)
# The raster and vector formats Typst embeds.
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
# html.parser lowercases attribute names; SVG is case-sensitive XML.
SVG_CAMEL_ATTRIBUTES = ("viewBox", "preserveAspectRatio")
# The Unicode box drawing block, which terminal tables are drawn with.
BOX_DRAWING = re.compile("[─-╿]")
# Typst is pre-1.0 and its minor releases change layout, so a PDF typeset with
# another one is a preview rather than the PDF this style was checked against.
TESTED_TYPST = "0.15"
BOOK_TITLE = "eccenca Corporate Memory"
BOOK_CONTEXT = "Documentation"
# The screen PDF, and the book block of the printed book (tasks/spec.md).
EDITIONS = ("screen", "print")
# How the print edition prints a navigation section (tools/pdf/print.yml).
SECTION_MODES = ("full", "list", "omit")
DEFAULT_COLUMNS = ("Page", "Summary")
# A `groups` table: the navigation titles under an overview page - the operator
# categories of the reference - and their pages, under the overview's title.
GROUP_COLUMNS = ("Category", "Pages")
# The print edition's text column is 16 cm wide, and BoD asks for images at
# 300 dpi at their printed size (tasks/spec.md, §2).
TEXT_WIDTH_PT = 16 / 2.54 * 72
PRINT_PPI = 300


@dataclass
class Generated:
    """Content the print edition sets in place of a section's pages.

    A `note` names the online edition for a section in `list` or `omit` mode; a
    `table` lists pages that no overview page of the section lists; `groups`
    lists the navigation titles whose pages an overview page lists, each with
    the names of its pages.
    """

    kind: str
    section: str
    mode: str
    pages: list[str] = field(default_factory=list)
    columns: tuple[str, str] = DEFAULT_COLUMNS
    # The section's name when no page of it carries one.
    name: str | None = None
    # The rows of a `groups` table: a navigation title and the page entries beneath it.
    groups: list[tuple[str, list[NavEntry]]] = field(default_factory=list)


@dataclass
class NavEntry:
    """One stop along the navigation: a page, the title of a section that has none, or generated content.

    A page carries the title the navigation gives it, when it gives one.
    """

    depth: int
    md: str | None = None
    title: str | None = None
    generated: Generated | None = None


@dataclass
class SectionRule:
    """How the print edition prints the pages under one docs/ directory."""

    prefix: str
    mode: str
    columns: tuple[str, str] = DEFAULT_COLUMNS


def load_site_config() -> dict:
    """Read mkdocs.yml, tolerating the `!!python/name:` handles it carries.

    Those tags resolve Material plugin callables and are meaningless here, so
    they are collapsed to None rather than imported.
    """

    class Loader(yaml.SafeLoader):
        pass

    Loader.add_multi_constructor(
        "tag:yaml.org,2002:python/name:", lambda l, s, n: None
    )
    Loader.add_multi_constructor("!!python/name:", lambda l, s, n: None)
    return yaml.load(MKDOCS_YML.read_text(encoding="utf-8"), Loader=Loader) or {}


def section_index(item: object) -> str | None:
    """The page a section's first child attaches to the section, if it is one.

    Mirrors `navigation.indexes`: an index.md that opens a section stands for
    the section - `build/index.md` is the Build page - rather than being listed
    beneath it.
    """
    path = item
    if isinstance(item, dict) and len(item) == 1:
        path = next(iter(item.values()))
    if isinstance(path, str) and (path == "index.md" or path.endswith("/index.md")):
        return path
    return None


def nav_entries(nav: list) -> list[NavEntry]:
    """Flatten a nav list into the order and heading depth the PDF follows.

    A section attached to an index page opens with that page at the section's
    depth. A section without one - Release Notes and its years - gets its title
    as a heading of its own; otherwise its pages would read as part of whichever
    chapter came before. Everything else in a section sits one level below it.
    A page keeps the title the navigation gives it; an index page takes its
    section's.
    """
    entries: list[NavEntry] = []
    seen: set[str] = set()

    def add_page(md: str, depth: int, title: str | None = None) -> None:
        if md.endswith(".md") and md not in seen:
            seen.add(md)
            entries.append(NavEntry(depth=depth, md=md, title=title))

    def add_section(title: str, children: list, depth: int) -> None:
        index = section_index(children[0]) if children else None
        if index is None:
            entries.append(NavEntry(depth=depth, title=str(title)))
            add_items(children, depth + 1)
        else:
            add_page(index, depth, str(title))
            add_items(children[1:], depth + 1)

    def add_items(items: list, depth: int) -> None:
        for item in items:
            if isinstance(item, str):
                add_page(item, depth)
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        add_page(value, depth, str(title))
                    elif isinstance(value, list):
                        add_section(title, value, depth)

    add_items(nav, 0)
    return entries


def load_nav_entries(nav_yml: Path = NAV_YML) -> list[NavEntry]:
    """The navigation entries of nav.yml, in PDF order."""
    data = yaml.safe_load(nav_yml.read_text(encoding="utf-8")) or {}
    return nav_entries(data.get("nav") or [])


# -- print edition: section modes ------------------------------------------------
# The print edition fits the page limit of a printed book by shortening sections
# that are reference material online (tools/pdf/print.yml). `list` keeps a
# section's overview pages and drops the pages they list; pages no overview
# lists become a table of title and first paragraph, and navigation titles left
# without pages become one table of titles and page names. `omit` drops a
# section and leaves a note naming the online edition.


def load_section_rules(path: Path = PRINT_YML) -> list[SectionRule]:
    """The section modes of the print edition.

    A mode is given either as the value of a section, or as `mode` in a mapping
    that may also name the two `columns` of the section's tables.
    """
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rules = []
    for prefix, value in (data.get("sections") or {}).items():
        spec = value if isinstance(value, dict) else {"mode": value}
        mode = spec.get("mode", "full")
        if mode not in SECTION_MODES:
            raise click.ClickException(
                f"{path}: section {prefix} has mode {mode!r}, not one of {', '.join(SECTION_MODES)}"
            )
        columns = tuple(spec.get("columns") or DEFAULT_COLUMNS)
        if len(columns) != 2:
            raise click.ClickException(f"{path}: section {prefix} needs two columns, not {len(columns)}")
        rules.append(SectionRule(str(prefix).rstrip("/") + "/", mode, columns))
    return rules


def is_heading_entry(entry: NavEntry) -> bool:
    """A section title the navigation gives without a page."""
    return entry.md is None and entry.generated is None


def section_name(prefix: str) -> str:
    """A readable name for a section that has neither a page nor a navigation title."""
    return prefix.rstrip("/").rsplit("/", 1)[-1].replace("-", " ").replace("_", " ").title()


def list_section(entries: list[NavEntry], rule: SectionRule) -> tuple[list[NavEntry], set[str]]:
    """Keep a section's own page and its subsections' overview pages; table what no overview lists.

    The navigation titles left without pages are tabled too (`group_listed_titles`).
    """
    root = rule.prefix + "index.md"
    overview = re.compile(re.escape(rule.prefix) + r"[^/]+/index\.md$")
    kept = {e.md for e in entries if e.md and (e.md == root or overview.match(e.md))}
    # An overview page lists the pages in and below its own directory.
    listed_by = [md[: -len("index.md")] for md in kept]
    result: list[NavEntry] = []
    dropped: set[str] = set()
    listed: set[str] = set()
    table: Generated | None = None
    for entry in entries:
        if not (entry.md and entry.md.startswith(rule.prefix)):
            result.append(entry)
            table = None
            continue
        if entry.md in kept:
            result.append(entry)
            table = None
            if entry.md == root:
                result.append(NavEntry(entry.depth, generated=Generated("note", rule.prefix, "list", [root])))
            continue
        dropped.add(entry.md)
        if any(entry.md.startswith(directory) for directory in listed_by):
            listed.add(entry.md)
            continue
        if table is None:
            table = Generated("table", rule.prefix, "list", [], rule.columns)
            result.append(NavEntry(entry.depth, generated=table))
        table.pages.append(entry.md)
    result = group_listed_titles(entries, result, listed, rule)

    if root not in kept:
        first = next((i for i, e in enumerate(result) if e.generated and e.generated.section == rule.prefix), None)
        if first is not None:
            # The note opens the section: before the titles that lead into its
            # first table, after the part title they belong to.
            start = first
            while start > 0 and is_heading_entry(result[start - 1]) and result[start - 1].depth > 0:
                start -= 1
            before = result[start - 1] if start > 0 else None
            name = before.title if before is not None and is_heading_entry(before) else section_name(rule.prefix)
            pages = result[first].generated.pages[:1]
            note = Generated("note", rule.prefix, "list", pages, name=name)
            result.insert(start, NavEntry(result[start].depth, generated=note))
    return result, dropped


def group_listed_titles(
    entries: list[NavEntry], result: list[NavEntry], listed: set[str], rule: SectionRule
) -> list[NavEntry]:
    """Replace each run of navigation titles whose pages an overview lists by one table.

    Without their pages such titles would print as empty headings - the
    operator categories after the Transformers overview do. The table has a row
    per title naming the pages beneath it; the overview before the run names the
    column of pages. Titles are told apart by identity, as two can read the same.
    """
    beneath: dict[int, list[NavEntry]] = {}
    for i, entry in enumerate(entries):
        if is_heading_entry(entry):
            pages: list[NavEntry] = []
            for below in entries[i + 1:]:
                if below.depth <= entry.depth:
                    break
                if below.md:
                    pages.append(below)
            beneath[id(entry)] = pages

    def emptied(index: int) -> bool:
        entry = result[index]
        pages = beneath.get(id(entry), []) if is_heading_entry(entry) else []
        following = result[index + 1] if index + 1 < len(result) else None
        return (
            bool(pages)
            and all(page.md in listed for page in pages)
            and (following is None or following.depth <= entry.depth)
        )

    grouped: list[NavEntry] = []
    i = 0
    while i < len(result):
        if not emptied(i):
            grouped.append(result[i])
            i += 1
            continue
        depth = result[i].depth
        rows = []
        while i < len(result) and result[i].depth == depth and emptied(i):
            rows.append((result[i].title, beneath[id(result[i])]))
            i += 1
        overview = next((e for e in reversed(grouped) if e.md and e.depth < depth), None)
        pages_column = overview.title if overview is not None and overview.title else GROUP_COLUMNS[1]
        table = Generated("groups", rule.prefix, "list", columns=(GROUP_COLUMNS[0], pages_column), groups=rows)
        grouped.append(NavEntry(depth, generated=table))
    return grouped


def drop_empty_headings(entries: list[NavEntry]) -> list[NavEntry]:
    """Remove section titles that no longer have anything beneath them."""
    result: list[NavEntry] = []
    for entry in reversed(entries):
        following = result[-1] if result else None
        if is_heading_entry(entry) and (following is None or following.depth <= entry.depth):
            continue
        result.append(entry)
    return list(reversed(result))


def omit_section(entries: list[NavEntry], rule: SectionRule) -> tuple[list[NavEntry], set[str]]:
    """Drop a section. A section with a page of its own leaves its title and a note in its place."""
    root = rule.prefix + "index.md"
    result: list[NavEntry] = []
    dropped: set[str] = set()
    for entry in entries:
        if entry.md and entry.md.startswith(rule.prefix):
            dropped.add(entry.md)
            if entry.md == root:
                result.append(NavEntry(entry.depth, generated=Generated("note", rule.prefix, "omit", [root])))
            continue
        result.append(entry)
    return drop_empty_headings(result), dropped


def apply_section_rules(entries: list[NavEntry], rules: list[SectionRule]) -> tuple[list[NavEntry], set[str]]:
    """Shorten the navigation by the section modes. Returns the entries and the pages dropped from them."""
    dropped: set[str] = set()
    for rule in rules:
        if not any(e.md and e.md.startswith(rule.prefix) for e in entries):
            raise click.ClickException(f"{PRINT_YML}: no page in {NAV_YML} lies under {rule.prefix}")
        if rule.mode == "list":
            entries, gone = list_section(entries, rule)
        elif rule.mode == "omit":
            entries, gone = omit_section(entries, rule)
        else:
            continue
        dropped |= gone
    return entries, dropped


# -- merging ---------------------------------------------------------------------


def md_to_built_html(src_md: str) -> str:
    """Map a docs/ markdown path to its built HTML (use_directory_urls=True)."""
    if src_md == "index.md":
        return "index.html"
    if src_md.endswith("/index.md"):
        return src_md[: -len("/index.md")] + "/index.html"
    if src_md.endswith(".md"):
        return src_md[: -len(".md")] + "/index.html"
    return src_md


def md_to_url_path(src_md: str) -> str:
    """Map a docs/ markdown path to its served URL path (use_directory_urls=True)."""
    if src_md == "index.md":
        return "/"
    if src_md.endswith("/index.md"):
        return "/" + src_md[: -len("index.md")]
    if src_md.endswith(".md"):
        return "/" + src_md[: -len(".md")] + "/"
    return "/" + src_md


def public_base_url(config: dict, version: str) -> str:
    """The published URL prefix that links leaving the PDF resolve against.

    The site is published per version with mike, so a 26.2 PDF points into the
    26.2 tree and the resources it links to stay the ones it describes; a build
    without a real version falls back to the `latest` alias.
    """
    site_url = str(config.get("site_url") or "/").rstrip("/") + "/"
    segment = "latest" if version in ("", "dev") else version
    return urllib.parse.urljoin(site_url, segment + "/")


def url_to_section_id(url_path: str) -> str:
    """Convert a URL path like /build/active-learning/ to its section id."""
    return url_path.strip("/").replace("/", "-")


def namespace_ids(section, section_id: str) -> None:
    """Prefix every element id in a merged page with its section id.

    Hundreds of pages share one document, so bare per-page ids such as
    `overview` collide. Same-page fragment links are rewritten to match, which
    is also what makes the cross-page rewriting below resolve.
    """
    for el in section.find_all(id=True):
        el["id"] = f"{section_id}-{el['id']}"
    for a in section.find_all("a", href=True):
        # A bare "#" is a placeholder link with no target; namespacing it would
        # manufacture a dangling anchor.
        if a["href"].startswith("#") and a["href"] != "#":
            a["href"] = f"#{section_id}-{a['href'][1:]}"


def resolve_links(
    section, base_url: str, valid_ids: set, public_base: str, unlink_ids: set | frozenset = frozenset()
) -> None:
    """Turn page-relative URLs into something valid inside the merged document.

    Links to other documented pages become in-PDF anchor jumps. Links to a page
    in `unlink_ids` - one the print edition drops from the section being merged
    - print as their text. Everything else relative - downloadable resources,
    screenshots opened at full size, pages outside the navigation - becomes an
    absolute link into the published site, which is the only address a reader of
    the PDF can follow.

    Image sources become root-absolute site paths; they are embedded, not linked.
    """
    for a in section.find_all("a", href=True):
        href = a["href"]
        if not href or href.startswith(
            ("http://", "https://", "mailto:", "tel:", "#")
        ):
            continue
        absolute = urllib.parse.urljoin(base_url, href)
        parsed = urllib.parse.urlparse(absolute)
        if parsed.scheme or parsed.netloc:
            continue
        section_id = url_to_section_id(parsed.path)
        if section_id and section_id in valid_ids:
            a["href"] = (
                f"#{section_id}-{parsed.fragment}"
                if parsed.fragment
                else f"#{section_id}"
            )
        elif section_id and section_id in unlink_ids:
            a.unwrap()
        else:
            a["href"] = urllib.parse.urljoin(public_base, absolute.lstrip("/"))

    for el in section.find_all(src=True):
        src = el["src"]
        if src and not src.startswith(("http://", "https://", "data:", "/")):
            el["src"] = urllib.parse.urljoin(base_url, src)


def demote_headings(section, depth: int) -> None:
    """Shift a page's headings down by its navigation depth.

    Every page renders its title as <h1>; shifting by depth makes the PDF
    outline and the contents mirror the navigation tree.
    """
    if depth <= 0:
        return
    for h in section.find_all(HEADING_TAGS):
        h.name = f"h{min(6, int(h.name[1]) + depth)}"


def part_cover(doc: BeautifulSoup, section) -> None:
    """Lay out a part page's cover: its title, then what the page shows above it, then the contents marker.

    The part pages show a "you are here" diagram beside their title, written
    before it in an admonition. On the cover it follows the title, without the
    admonition's box. `part-contents()` in style.typ starts a new page for the
    part's contents, and another after them.
    """
    marker = doc.new_tag("div", attrs={"class": "part-contents"})
    title = section.find("h1")
    if title is None:
        section.insert(0, marker)
        return
    above = list(reversed(list(title.previous_siblings)))
    anchor = title
    for node in above:
        anchor.insert_after(node)
        anchor = node
    anchor.insert_after(marker)
    for node in above:
        if node.name == "div" and "admonition" in node.get("class", []):
            node.unwrap()


def page_article(site_dir: Path, md: str):
    """A page's built article with its web chrome dropped, or None when the page is not built."""
    built = site_dir / md_to_built_html(md)
    if not built.exists():
        return None
    article = BeautifulSoup(built.read_text(encoding="utf-8"), "html.parser").select_one(CONTENT_SELECTOR)
    if article is not None:
        drop_noise(article)
    return article


def plain_heading(heading) -> str:
    """A heading's text without the icons some titles carry."""
    for icon in heading.select(".twemoji"):
        icon.decompose()
    return " ".join(heading.get_text(" ", strip=True).split())


def page_title(site_dir: Path, md: str) -> str:
    article = page_article(site_dir, md)
    heading = article.find("h1") if article is not None else None
    return plain_heading(heading) if heading is not None else md


def list_cell(doc: BeautifulSoup, name: str = "td"):
    """A cell of a print-list table, set left: pandoc centres a cell that has no alignment."""
    return doc.new_tag(name, attrs={"style": "text-align: left;"})


def list_table(doc: BeautifulSoup, columns: tuple[str, str]):
    """An empty print-list table under its two column labels, and the body to fill."""
    table = doc.new_tag("table", attrs={"class": "print-list"})
    head = doc.new_tag("thead")
    row = doc.new_tag("tr")
    for label in columns:
        cell = list_cell(doc, "th")
        cell.string = label
        row.append(cell)
    head.append(row)
    body = doc.new_tag("tbody")
    table.append(head)
    table.append(body)
    return table, body


def summary_table(doc: BeautifulSoup, generated: Generated, site_dir: Path):
    """A two-column table of pages: the title, and the paragraph that opens the page.

    A page that opens with something else is summarized by its second-level
    headings, which on a release page name the components released.
    """
    table, body = list_table(doc, generated.columns)
    for md in generated.pages:
        article = page_article(site_dir, md)
        heading = article.find("h1") if article is not None else None
        row = doc.new_tag("tr")
        title = list_cell(doc)
        title.string = plain_heading(heading) if heading is not None else md
        summary = list_cell(doc)
        opening = heading.find_next_sibling() if heading is not None else None
        if opening is not None and opening.name == "p":
            for link in opening.find_all("a"):
                link.unwrap()
            for image in opening.find_all("img"):
                image.decompose()
            for child in list(opening.contents):
                summary.append(child.extract())
        elif article is not None:
            summary.string = ", ".join(plain_heading(h) for h in article.find_all("h2"))
        row.append(title)
        row.append(summary)
        body.append(row)
    return table


def groups_table(doc: BeautifulSoup, generated: Generated, site_dir: Path):
    """A two-column table of navigation titles: the title, and the names of the pages beneath it.

    A page is named by its navigation title, or by its own title when the
    navigation gives it none.
    """
    table, body = list_table(doc, generated.columns)
    for title, pages in generated.groups:
        row = doc.new_tag("tr")
        for text in (title, ", ".join(page.title or page_title(site_dir, page.md) for page in pages)):
            cell = list_cell(doc)
            cell.string = text
            row.append(cell)
        body.append(row)
    return table


def section_url(generated: Generated, site_dir: Path, public_base: str) -> str:
    """Where a shortened section is complete: its own page online, else the first page it lists."""
    if (site_dir / generated.section / "index.html").is_file():
        path = generated.section
    else:
        path = md_to_url_path(generated.pages[0]).lstrip("/")
    return urllib.parse.urljoin(public_base, path)


def render_generated(doc: BeautifulSoup, entry: NavEntry, site_dir: Path, public_base: str) -> list:
    """The elements that stand in for a shortened section's pages."""
    generated = entry.generated
    if generated.kind == "table":
        return [summary_table(doc, generated, site_dir)]
    if generated.kind == "groups":
        return [groups_table(doc, generated, site_dir)]
    name = generated.name or page_title(site_dir, generated.pages[0])
    url = section_url(generated, site_dir, public_base)
    elements = []
    if generated.mode == "omit":
        heading = doc.new_tag(f"h{min(6, entry.depth + 1)}")
        heading.string = name
        elements.append(heading)
        text = f"The {name} is not part of this print edition. It is part of the online edition: {url}"
    else:
        text = f"This print edition lists the {name} in short. The complete section is part of the online edition: {url}"
    note = doc.new_tag("div", attrs={"class": "admonition info"})
    paragraph = doc.new_tag("p")
    paragraph.string = text
    note.append(paragraph)
    elements.append(note)
    return elements


def merge_pages(
    entries: list[NavEntry],
    site_dir: Path,
    public_base: str,
    rules: list[SectionRule] | None = None,
    dropped: set[str] | None = None,
) -> tuple[BeautifulSoup, list[str]]:
    """Merge the built articles along the navigation into one HTML document.

    Every top-level entry is a part. It is preceded by a chapter break, so a
    part starts on a new page, and its page opens with the part's cover (see
    `part_cover`); a part without a page gets its title and the contents marker.
    Generated entries of the print edition's section modes are rendered where
    they stand, and a shortened section's links to the pages it drops print as
    text. Returns the document and the navigation pages that had no built HTML.
    """
    doc = BeautifulSoup('<html><head><meta charset="utf-8"></head><body></body></html>', "html.parser")
    valid_ids = {url_to_section_id(md_to_url_path(e.md)) for e in entries if e.md}
    dropped_ids = {url_to_section_id(md_to_url_path(md)) for md in dropped or ()}
    shortened = [rule.prefix for rule in rules or () if rule.mode != "full"]
    missing: list[str] = []

    for entry in entries:
        if entry.generated is not None:
            for element in render_generated(doc, entry, site_dir, public_base):
                doc.body.append(element)
            continue
        if entry.depth == 0:
            doc.body.append(doc.new_tag("div", attrs={"class": "chapter-break"}))
        if entry.md is None:
            heading = doc.new_tag(f"h{min(6, entry.depth + 1)}")
            heading.string = entry.title or ""
            doc.body.append(heading)
            if entry.depth == 0:
                heading.insert_after(doc.new_tag("div", attrs={"class": "part-contents"}))
            continue

        # page_article drops the web chrome before the ids are namespaced:
        # selectors such as #__comments would no longer match afterwards.
        article = page_article(site_dir, entry.md)
        if article is None:
            missing.append(entry.md)
            continue

        section_id = url_to_section_id(md_to_url_path(entry.md))
        section = doc.new_tag("section", attrs={"class": "print-page", "id": section_id})
        for child in list(article.children):
            section.append(child.extract())
        namespace_ids(section, section_id)
        unlink_ids = dropped_ids if any(entry.md.startswith(prefix) for prefix in shortened) else frozenset()
        resolve_links(section, md_to_url_path(entry.md), valid_ids, public_base, unlink_ids)
        demote_headings(section, entry.depth)
        if entry.depth == 0:
            part_cover(doc, section)
        doc.body.append(section)

    return doc, missing


# -- normalization -------------------------------------------------------------
# Material's HTML is class-tagged but shaped for a browser: tab labels live apart
# from their panels, highlighted code is split into token spans and line anchors,
# icons are inline SVG. The steps below rewrite that into plain elements with one
# class each, which tools/pdf/filter.lua maps onto the functions in style.typ.


def drop_noise(root) -> None:
    """Remove interactive widgets and web-only chrome from a page's article."""
    for selector in NOISE_SELECTORS:
        for el in root.select(selector):
            if not el.decomposed:
                el.decompose()


def flatten_code_blocks(doc: BeautifulSoup, stats: Counter) -> None:
    """Highlighted code: one <pre><code>, keeping the language and the title.

    pandoc only reads a <pre> holding a bare <code> as a code block; with the
    highlighter's token spans and line anchors inside, it reads inline code.
    """
    for highlight in doc.select("div.highlight"):
        code = highlight.select_one("td.code code") or highlight.find("code")
        if code is None:
            continue
        pre = doc.new_tag("pre")
        flat = doc.new_tag("code")
        language = next(
            (c.removeprefix("language-") for c in highlight.get("class", []) if c.startswith("language-")),
            "",
        )
        if language:
            flat["class"] = f"language-{language}"
        text = code.get_text().rstrip("\n")
        flat.string = text
        pre.append(flat)
        attrs = {}
        title = highlight.find("span", class_="filename")
        if title is not None:
            attrs["data-title"] = title.get_text(strip=True)
        if BOX_DRAWING.search(text):
            # Terminal tables cannot wrap without falling apart; the style
            # shrinks such a block until its widest line fits.
            attrs["data-columns"] = str(max(len(line) for line in text.splitlines()))
        if attrs:
            wrapper = doc.new_tag("div", attrs={"class": "codeblock", **attrs})
            wrapper.append(pre)
            highlight.replace_with(wrapper)
        else:
            highlight.replace_with(pre)
        stats["code blocks"] += 1


def admonitions(doc: BeautifulSoup, stats: Counter) -> None:
    """Collapsible admonitions print expanded; every title becomes a div.

    pandoc drops the attributes of a <p>, which would lose the title class.
    """
    for details in doc.select("details"):
        kind = next(iter(details.get("class", [])), "note")
        div = doc.new_tag("div", attrs={"class": f"admonition {kind}"})
        summary = details.find("summary", recursive=False)
        if summary is not None:
            title = doc.new_tag("p", attrs={"class": "admonition-title"})
            for child in list(summary.contents):
                title.append(child.extract())
            summary.decompose()
            div.append(title)
        for child in list(details.contents):
            div.append(child.extract())
        details.replace_with(div)
    for title in doc.select("p.admonition-title"):
        title.name = "div"
        stats["admonitions"] += 1


def pair_tabs(doc: BeautifulSoup, stats: Counter) -> None:
    """Content tabs: each panel wrapped together with its label."""
    for tabbed in doc.select("div.tabbed-set"):
        labels = [label.get_text(" ", strip=True) for label in tabbed.select(":scope > div.tabbed-labels > label")]
        panels = tabbed.select(":scope > div.tabbed-content > div.tabbed-block")
        group = doc.new_tag("div", attrs={"class": "tabs"})
        for i, panel in enumerate(panels):
            label = labels[i] if i < len(labels) else f"Tab {i + 1}"
            tab = doc.new_tag("div", attrs={"class": "tab", "data-label": label})
            for child in list(panel.contents):
                tab.append(child.extract())
            group.append(tab)
        tabbed.replace_with(group)
        stats["tab sets"] += 1


def mark_cards(doc: BeautifulSoup, stats: Counter) -> None:
    """Grid cards keep their list; the class tells the filter to lay it out as cards."""
    for grid in doc.select("div.grid.cards"):
        grid["class"] = "cards"
        stats["card grids"] += 1


def inline_icons(doc: BeautifulSoup, stats: Counter) -> None:
    """Icons: an <img> carrying the SVG as a data URI, which pandoc sizes to the text.

    An icon in a heading is dropped instead. The title band, the contents, the
    running footer and the PDF outline all print the heading's title.
    """
    for icon in doc.select("span.twemoji"):
        heading = icon.find_parent(HEADING)
        if heading is not None:
            icon.decompose()
            for edge, strip in ((0, str.lstrip), (-1, str.rstrip)):
                if heading.contents and isinstance(heading.contents[edge], NavigableString):
                    heading.contents[edge].replace_with(strip(str(heading.contents[edge])))
            stats["icons dropped from headings"] += 1
            continue
        svg = icon.find("svg")
        if svg is None:
            icon.unwrap()
            continue
        # The style's slate; an icon without a fill would print black.
        svg["fill"] = "#2E3B45"
        markup = str(svg)
        for name in SVG_CAMEL_ATTRIBUTES:
            markup = markup.replace(f" {name.lower()}=", f" {name}=")
        data = base64.b64encode(markup.encode("utf-8")).decode("ascii")
        icon.replace_with(doc.new_tag(
            "img", attrs={"src": f"data:image/svg+xml;base64,{data}", "class": "icon", "alt": ""}
        ))
        stats["icons"] += 1


def typst_path(path: Path) -> str:
    """A file path as Typst resolves it: absolute from the project root, the working directory."""
    return "/" + path.resolve().relative_to(Path.cwd().resolve()).as_posix()


def printed_width_pt(image: Image.Image, width: str | None) -> float:
    """The width Typst prints an image at in the print edition's text column.

    A percentage is that share of the column. Without one, Typst sizes an image
    by the pixel density it declares - 72 dpi when it declares none - and never
    wider than the column.
    """
    if width and width.strip().endswith("%"):
        return TEXT_WIDTH_PT * float(width.strip()[:-1]) / 100
    dpi = image.info.get("dpi")
    density = float(dpi[0]) if dpi and dpi[0] else 72.0
    return min(image.width * 72 / density, TEXT_WIDTH_PT)


def print_image(source: Path, width: str | None, cache_dir: Path) -> Path:
    """A copy of an image for the print edition: flattened onto white, at 300 ppi at its printed width.

    BoD asks for 300 dpi and no transparency. The copy declares 300 dpi, so Typst
    prints it at the width the original printed at, resampled up or down with
    Lanczos. Copies are cached by the original's content and the pixel width.
    """
    data = source.read_bytes()
    with Image.open(io.BytesIO(data)) as image:
        pixels = max(1, round(printed_width_pt(image, width) / 72 * PRINT_PPI))
        target = cache_dir / f"{hashlib.sha256(data).hexdigest()[:16]}-{pixels}.png"
        if target.is_file():
            return target
        image.seek(0)
        frame = image.convert("RGBA")
        flat = Image.new("RGB", frame.size, "white")
        flat.paste(frame, mask=frame.getchannel("A"))
        height = max(1, round(frame.height * pixels / frame.width))
        cache_dir.mkdir(parents=True, exist_ok=True)
        flat.resize((pixels, height), Image.Resampling.LANCZOS).save(target, "PNG", dpi=(PRINT_PPI, PRINT_PPI))
    return target


def resolve_images(
    doc: BeautifulSoup, site_dir: Path, stats: Counter, warnings: list[str], print_images: Path | None = None
) -> None:
    """Point images at the files Typst embeds, and replace what it cannot embed.

    Emoji that the site loads as Twemoji images become the emoji character,
    which the vendored emoji font draws. Other remote images - status badges -
    become their alt text: the build does not fetch from the network. An SVG
    that keeps its text in foreignObject elements, as Mermaid does by default,
    renders without that text in Typst, so it is reported. With `print_images`,
    raster images point at their print copies in that directory (`print_image`).
    """
    for lightbox in doc.select("a.glightbox"):
        lightbox.unwrap()
    for img in doc.find_all("img"):
        src = img.get("src", "")
        alt = img.get("alt", "")
        classes = img.get("class", [])
        if src.startswith("data:"):
            continue
        if "twemoji" in classes or "emojione" in classes:
            img.replace_with(alt)
            stats["emoji images"] += 1
            continue
        path = site_dir / urllib.parse.unquote(src.split("#")[0].split("?")[0]).lstrip("/")
        remote = src.startswith(("http://", "https://"))
        if remote or not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
            if not remote:
                warnings.append(f"image cannot be embedded, printed as its alt text: {src}")
            if alt:
                img.replace_with(alt)
            else:
                img.decompose()
            stats["images printed as alt text"] += 1
            continue
        if path.suffix.lower() == ".svg" and "<foreignObject" in path.read_text(encoding="utf-8", errors="ignore"):
            warnings.append(f"SVG text in foreignObject elements does not render, embed a PNG instead: {src}")
        if print_images is not None and path.suffix.lower() != ".svg":
            img["src"] = typst_path(print_image(path, img.get("width"), print_images))
            stats["images normalized for print"] += 1
        else:
            img["src"] = typst_path(path)
        stats["images"] += 1


def embedded_media_to_links(doc: BeautifulSoup, stats: Counter) -> None:
    """Videos and iframes cannot play on paper; their address can be followed."""
    for media in doc.find_all(["iframe", "video"]):
        link = doc.new_tag("a", href=media.get("src", ""))
        link.string = f"[{media.name}: {media.get('src', '')}]"
        media.replace_with(link)
        stats["embedded media"] += 1


def settle_internal_links(doc: BeautifulSoup, stats: Counter) -> None:
    """Point in-document links at headings, and keep ids only on headings.

    pandoc turns ids into Typst labels, and a link to a label that does not
    exist fails the whole build. A link to a page therefore targets the page's
    first heading, a link to anything but a heading is unwrapped to its text,
    and ids on other elements are dropped.
    """
    first_heading = {}
    for section in doc.select("section.print-page"):
        heading = section.find(HEADING, id=True)
        if heading is not None:
            first_heading[section["id"]] = heading["id"]
    heading_ids = {h["id"] for h in doc.find_all(HEADING, id=True)}
    for a in doc.find_all("a"):
        href = a.get("href")
        if href is None:
            a.unwrap()
            continue
        if href.startswith("#"):
            target = first_heading.get(href[1:], href[1:])
            if target in heading_ids:
                a["href"] = f"#{target}"
                stats["internal links"] += 1
            else:
                a.unwrap()
                stats["internal links without a heading target"] += 1
    for el in doc.find_all(id=True):
        if not HEADING.match(el.name):
            del el["id"]
    for section in doc.select("section.print-page"):
        section.unwrap()


def normalize(doc: BeautifulSoup, site_dir: Path, print_images: Path | None = None) -> tuple[Counter, list[str]]:
    """Rewrite the merged document into elements pandoc's HTML reader understands.

    Returns counts of what was rewritten and warnings about content the PDF
    cannot show as the site does.
    """
    stats: Counter = Counter()
    warnings: list[str] = []
    flatten_code_blocks(doc, stats)
    admonitions(doc, stats)
    pair_tabs(doc, stats)
    mark_cards(doc, stats)
    inline_icons(doc, stats)
    resolve_images(doc, site_dir, stats, warnings, print_images)
    embedded_media_to_links(doc, stats)
    settle_internal_links(doc, stats)
    return stats, warnings


# -- typesetting ---------------------------------------------------------------


def source_commit() -> str:
    """The abbreviated commit the PDF is built from, or an empty string outside a git checkout.

    Tracked changes that are not committed append `-dirty`, so a PDF built from
    a working tree does not claim to be that commit.
    """
    try:
        result = subprocess.run(
            ["git", "describe", "--always", "--dirty", "--exclude=*"],
            capture_output=True, text=True, check=False,
        )
    except OSError:
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


def edition(config: dict, version: str, public_base: str, today: date, commit: str) -> dict[str, str]:
    """What the title page, header and PDF metadata print, as Typst --input values."""
    copyright_html = str(config.get("copyright") or "")
    copyright_text = " ".join(BeautifulSoup(copyright_html, "html.parser").get_text().split())
    return {
        "title": BOOK_TITLE,
        "subtitle": f"Version {version}",
        "context": BOOK_CONTEXT,
        "version": version,
        "generated": today.isoformat(),
        "commit": commit,
        "site-url": public_base,
        "copyright": copyright_text,
    }


def require_binary(binary: str, option: str) -> str:
    found = shutil.which(binary)
    if found is None:
        raise click.ClickException(f"{binary} not found - install it or name the binary with --{option}.")
    return found


def binary_version(binary: str) -> str:
    result = subprocess.run([binary, "--version"], capture_output=True, text=True, check=False)
    lines = result.stdout.strip().splitlines()
    return lines[0] if lines else f"{binary} (unknown version)"


def run(command: list[str], what: str) -> None:
    started = time.monotonic()
    if subprocess.run(command, check=False).returncode != 0:
        raise click.ClickException(f"{what} failed: {' '.join(command[:2])} ...")
    print(f"{what} took {time.monotonic() - started:.0f}s")


def unpadded_pages(compile_command: list[str], typ_path: Path) -> int:
    """How many pages the print edition has before it is padded to an even count.

    The style marks the book's last page with `<book-end>`. Typst cannot add the
    blank page itself: a page break that depends on the page count never lets the
    layout converge. So the build asks first and passes `pad=true` when needed.
    """
    started = time.monotonic()
    command = [compile_command[0], "eval", "query(<book-end>).first().value", "--in", str(typ_path)]
    command += compile_command[2:]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise click.ClickException(f"typst eval failed: {result.stderr.strip()[:500]}")
    pages = int(result.stdout.strip())
    print(f"typst eval took {time.monotonic() - started:.0f}s: {pages} pages before padding")
    return pages


@click.command()
@click.option(
    "--build-version",
    default="dev",
    envvar="BUILD_VERSION",
    help="Which version to stamp on the title page and fold into the file name?",
    show_default=True,
)
@click.option(
    "--edition", "edition_name",
    type=click.Choice(EDITIONS),
    default="screen",
    envvar="PDF_EDITION",
    help="Which edition: the screen PDF, or the book block for print on demand?",
    show_default=True,
)
@click.option(
    "--output-file", "-o",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default=None,
    envvar="PDF_OUT",
    help=f"Where to write the PDF?  [default: {DEFAULT_OUT_STEM}-<version>.pdf, -print.pdf for print]",
)
@click.option(
    "--pandoc", "pandoc_binary",
    default="pandoc",
    envvar="PANDOC",
    help="Which pandoc binary converts the merged HTML to Typst?",
    show_default=True,
)
@click.option(
    "--typst", "typst_binary",
    default="typst",
    envvar="TYPST",
    help="Which Typst binary typesets the PDF?",
    show_default=True,
)
def build_pdf(
    build_version: str, edition_name: str, output_file: str | None, pandoc_binary: str, typst_binary: str
) -> None:
    """Build a single PDF of the whole site with pandoc and Typst."""
    version = build_version.strip() or "dev"
    print_edition = edition_name == "print"
    suffix = "-print" if print_edition else ""
    out = Path(output_file or f"{DEFAULT_OUT_STEM}-{version.replace('.', '-')}{suffix}.pdf")
    # The print edition merges and normalizes differently, so its intermediate
    # files must not overwrite the screen edition's.
    work_dir = WORK_DIR / "print" if print_edition else WORK_DIR

    if not (SITE_DIR / "index.html").exists():
        raise click.ClickException(f"{SITE_DIR} is not built - run `task build` first.")
    pandoc = require_binary(pandoc_binary, "pandoc")
    typst = require_binary(typst_binary, "typst")
    typst_version = binary_version(typst)
    print(f"Using {binary_version(pandoc)} and {typst_version}")
    if not typst_version.startswith(f"typst {TESTED_TYPST}."):
        print(
            f"WARNING: the style is tested with typst {TESTED_TYPST}.x, and Typst "
            "minor releases change layout - treat this PDF as a preview.",
            file=sys.stderr,
        )

    entries = load_nav_entries()
    if not entries:
        raise click.ClickException(f"no pages found in {NAV_YML}")
    rules = load_section_rules() if print_edition else []
    entries, dropped = apply_section_rules(entries, rules)
    for rule in rules:
        if rule.mode != "full":
            count = sum(1 for md in dropped if md.startswith(rule.prefix))
            print(f"Print edition: {rule.prefix} as {rule.mode}, {count} pages dropped")
    config = load_site_config()
    public_base = public_base_url(config, version)
    doc, missing = merge_pages(entries, SITE_DIR, public_base, rules, dropped)
    pages = sum(1 for e in entries if e.md) - len(missing)
    headings = sum(1 for e in entries if is_heading_entry(e))
    if missing:
        print(
            f"WARNING: {len(missing)} page(s) in {NAV_YML} had no built HTML: "
            + ", ".join(missing[:5])
            + (" ..." if len(missing) > 5 else ""),
            file=sys.stderr,
        )
    print(f"Merged {pages} pages and {headings} section headings along {NAV_YML}")

    stats, warnings = normalize(doc, SITE_DIR, work_dir / "images" if print_edition else None)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    print("Normalized " + ", ".join(f"{count} {what}" for what, count in sorted(stats.items())))

    work_dir.mkdir(parents=True, exist_ok=True)
    html_path = work_dir / "book.html"
    typ_path = work_dir / "book.typ"
    html_path.write_text(str(doc), encoding="utf-8")

    run(
        [
            pandoc, "--from=html", "--to=typst", "--wrap=preserve",
            f"--lua-filter={PDF_ASSETS / 'filter.lua'}",
            f"--template={PDF_ASSETS / 'template.typ'}",
            f"--output={typ_path}", str(html_path),
        ],
        "pandoc",
    )

    out.parent.mkdir(parents=True, exist_ok=True)
    command = [
        typst, "compile", "--root", ".", "--ignore-system-fonts",
        "--font-path", str(PDF_ASSETS / "fonts"),
    ]
    inputs = edition(config, version, public_base, date.today(), source_commit())
    # Only the print edition passes the switch, so the screen edition's Typst
    # call is the one it always was.
    if print_edition:
        inputs["edition"] = "print"
    for key, value in inputs.items():
        command += ["--input", f"{key}={value}"]
    if print_edition and unpadded_pages(command, typ_path) % 2:
        # A printed book has an even page count; the style adds a blank last page.
        command += ["--input", "pad=true"]
    run(command + [str(typ_path), str(out)], "typst")

    print(f"PDF written to {out} ({out.stat().st_size // 1024} KB)")
