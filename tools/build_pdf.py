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
import json
import re
import shutil
import struct
import subprocess
import sys
import time
import urllib.parse
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from functools import lru_cache
from pathlib import Path

import click
import markdown
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag
from PIL import Image

from tools.pdf_authors import load_imprint_names
from tools.pdf_normalize import ensure_profile, gray_path, gray_preview, normalize as normalize_pdf, normalized_path
from tools.pdf_preflight import print_report, run_preflight
from tools.print_geometry import COLUMN_INCHES, LOW_RESOLUTION_PPI, PRINT_PPI, TEXT_WIDTH_PT

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
SECTION_MODES = ("full", "list", "omit", "reference")
DEFAULT_COLUMNS = ("Page", "Summary")
# A `groups` table: the navigation titles under an overview page - the operator
# categories of the reference - and their pages, under the overview's title.
GROUP_COLUMNS = ("Category", "Pages")
# The class that leaves a part of a page out of the print edition, and the note
# that takes its place (tasks/spec.md, §10).
PRINT_EXCLUDE = "print-exclude"
EXCLUDED_NOTE = "print-excluded"
PART_NOTE = "This print edition leaves out a part of this page. The online edition has the full details:"
# The operator reference in `reference` mode (tasks/spec.md, §11): the plugin
# descriptions its pages are generated from (tools/update_di_reference.py), and
# how an entry names operator types and data types.
OPERATORS_JSON = Path("data/plugins.json")
OPERATOR_TYPES = {
    "aggregator": "Aggregator",
    "customtask": "Workflow task",
    "dataset": "Dataset",
    "distancemeasure": "Distance measure",
    "transformer": "Transformer",
}
DATA_TYPES = {
    "string": "text", "multiline string": "text", "boolean": "boolean", "int": "integer", "Long": "integer",
    "double": "number", "char": "character", "enumeration": "choice", "password": "password",
    "resource": "file", "scheme:string": "URI", "uri": "URI", "graph uri": "graph URI",
    "traversable[string]": "list of text", "stringmap": "map", "keyValuePairs": "key-value pairs",
    "objectParameter": "group", "duration": "duration", "template": "template", "task": "task",
    "project": "project", "SPARQL endpoint": "SPARQL endpoint", "identifier": "identifier", "locale": "locale",
}
CODE_LANGUAGES = {
    "sparql": "SPARQL", "sql": "SQL", "json": "JSON", "yaml": "YAML", "jinja2": "Jinja template",
    "python": "Python", "html": "HTML", "xml": "XML",
}
# The sections of an operator page an entry does not print: the examples, and
# what it sets from the plugin description instead.
OPERATOR_SECTIONS_LEFT_OUT = {"examples", "example", "parameter", "parameters", "advanced parameter", "related plugins"}
# The print edition's text column is 16 cm wide, and BoD asks for images at
# 300 dpi at their printed size (tasks/spec.md, §2).
# The column and the densities come from tools/print_geometry.py, which the
# image tools and the preflight share.
# Colour emoji in the print edition: rendered as images from the vendored font,
# for text the body font does not cover.
EMOJI_FONT = PDF_ASSETS / "fonts" / "noto-color-emoji" / "Noto-COLRv1.ttf"
TEXT_FONT = PDF_ASSETS / "fonts" / "roboto" / "Roboto-Light.ttf"
# What the print edition renders to PNG with Typst: colour emoji and SVGs that
# draw with transparency - opacity, masks, filters, translucent colours.
RENDER_PPI = 600
MAX_RENDER_WIDTH = round(COLUMN_INCHES * RENDER_PPI)
SVG_TRANSPARENCY = re.compile(r"opacity|<mask|<filter|rgba\(|hsla\(", re.IGNORECASE)
# A short line under one of the larger headings - the intended audience, say -
# is carried to the next page with it (print edition).
LEAD_HEADINGS = ("h1", "h2", "h3", "h4")
LEAD_MAX_CHARS = 200


@dataclass
class Generated:
    """Content the print edition sets in place of a section's pages.

    A `note` names the online edition for a section in `list` mode; a `table`
    lists pages that no overview page of the section lists; `groups` lists the
    navigation titles whose pages an overview page lists, each with the names
    of its pages; `operators` sets the compact entries of an operator reference.
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
    # An `operators` entry: the plugin descriptions of its pages, in their order,
    # and the page and title of every operator of the reference by plugin ID.
    operators: list[dict] = field(default_factory=list)
    catalog: dict[str, tuple[str, str]] = field(default_factory=dict)


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
    """How the print edition prints the pages under one docs/ directory, or a single page."""

    prefix: str
    mode: str
    columns: tuple[str, str] = DEFAULT_COLUMNS

    @property
    def page(self) -> bool:
        """Whether the rule names a single page rather than a directory."""
        return self.prefix.endswith(".md")

    def matches(self, md: str) -> bool:
        return md == self.prefix if self.page else md.startswith(self.prefix)


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
# section or a single page without a trace (tasks/spec.md, §10).


def load_section_rules(path: Path = PRINT_YML) -> list[SectionRule]:
    """The section modes of the print edition.

    A key names a docs/ directory, or a single page by its `.md` path, which
    accepts only `omit`. A mode is given either as the value of a key, or as
    `mode` in a mapping that may also name the two `columns` of the section's
    tables. Keys do not nest.
    """
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    rules = []
    for key, value in (data.get("sections") or {}).items():
        spec = value if isinstance(value, dict) else {"mode": value}
        mode = spec.get("mode", "full")
        if mode not in SECTION_MODES:
            raise click.ClickException(
                f"{path}: section {key} has mode {mode!r}, not one of {', '.join(SECTION_MODES)}"
            )
        columns = tuple(spec.get("columns") or DEFAULT_COLUMNS)
        if len(columns) != 2:
            raise click.ClickException(f"{path}: section {key} needs two columns, not {len(columns)}")
        name = str(key)
        rule = SectionRule(name if name.endswith(".md") else name.rstrip("/") + "/", mode, columns)
        if rule.page and mode != "omit":
            raise click.ClickException(f"{path}: {rule.prefix} names a page, which accepts only `omit`, not {mode!r}")
        rules.append(rule)
    for rule in rules:
        outer = next((o for o in rules if o is not rule and not o.page and rule.prefix.startswith(o.prefix)), None)
        if outer is not None:
            raise click.ClickException(f"{path}: {rule.prefix} lies inside {outer.prefix} - section keys do not nest")
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
    """Drop a subtree or a single page, without a trace in the text (tasks/spec.md, §10).

    A dropped page with pages beneath it that stay - an index page omitted on its
    own - leaves the section's navigation title as a heading, so those pages keep
    their place.
    """
    result: list[NavEntry] = []
    dropped: set[str] = set()
    for i, entry in enumerate(entries):
        if not (entry.md and rule.matches(entry.md)):
            result.append(entry)
            continue
        dropped.add(entry.md)
        following = entries[i + 1] if i + 1 < len(entries) else None
        if following is not None and following.depth > entry.depth and not (following.md and rule.matches(following.md)):
            result.append(NavEntry(entry.depth, title=entry.title or section_name(entry.md.rsplit("/", 1)[0])))
    return drop_empty_headings(result), dropped


def load_operators(path: Path = OPERATORS_JSON) -> list[dict]:
    """The plugin descriptions of the operators the reference documents: all that are not deprecated."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return [record for record in data.values() if not record.get("is_deprecated")]


def operator_page(prefix: str, record: dict) -> str:
    """The docs/ path of an operator's page, as tools/update_di_reference.py writes it."""
    if record["pluginType"] == "transformer":
        return f"{prefix}transformer/{record['main_category']}/{record['pluginId']}.md"
    return f"{prefix}{record['pluginType']}/{record['pluginId']}.md"


def reference_overview(rule: SectionRule, md: str) -> str | None:
    """The operator type whose overview page `md` is, in a `reference` section."""
    match = re.fullmatch(re.escape(rule.prefix) + r"([^/]+)/index\.md", md)
    return match.group(1) if match else None


def reference_section(
    entries: list[NavEntry], rule: SectionRule, operators: list[dict]
) -> tuple[list[NavEntry], set[str]]:
    """Print the operators of a reference as compact entries after the overview page of their type (tasks/spec.md, §11).

    The section's own page is followed by a note on what an entry shows. Each
    type's overview page is followed by its operators in alphabetical order; the
    pages and navigation titles beneath it give way to them, so no page is
    dropped. The operator pages in the navigation and the plugin descriptions
    must agree.
    """
    root = rule.prefix + "index.md"
    catalog = {record["pluginId"]: (operator_page(rule.prefix, record), record["title"]) for record in operators}
    pages = {
        e.md for e in entries
        if e.md and e.md.startswith(rule.prefix) and e.md != root and reference_overview(rule, e.md) is None
    }
    expected = {page for page, _ in catalog.values()}
    if pages != expected:
        without_page = sorted(plugin for plugin, (page, _) in catalog.items() if page not in pages)
        raise click.ClickException(
            f"{rule.prefix}: operator pages without a description in {OPERATORS_JSON}: "
            f"{', '.join(sorted(pages - expected)) or 'none'}; descriptions without a page: "
            f"{', '.join(without_page) or 'none'}"
        )
    by_type: dict[str, list[dict]] = {}
    for record in operators:
        by_type.setdefault(record["pluginType"], []).append(record)
    result: list[NavEntry] = []
    beneath: int | None = None
    for entry in entries:
        if beneath is not None:
            if entry.depth > beneath:
                continue
            beneath = None
        result.append(entry)
        if entry.md == root:
            result.append(NavEntry(entry.depth, generated=Generated("note", rule.prefix, "reference", [root])))
        kind = reference_overview(rule, entry.md) if entry.md else None
        if kind is not None:
            records = sorted(by_type.get(kind, []), key=lambda record: record["title"].casefold())
            result.append(NavEntry(entry.depth + 1, generated=Generated(
                "operators", rule.prefix, "reference", [catalog[record["pluginId"]][0] for record in records],
                operators=records, catalog=catalog,
            )))
            beneath = entry.depth
    return result, set()


def apply_section_rules(
    entries: list[NavEntry], rules: list[SectionRule], operators: list[dict] | None = None
) -> tuple[list[NavEntry], set[str]]:
    """Shorten the navigation by the section modes. Returns the entries and the pages dropped from them.

    A `reference` rule reads the plugin descriptions from data/plugins.json
    unless `operators` passes them.
    """
    dropped: set[str] = set()
    for rule in rules:
        if not any(e.md and rule.matches(e.md) for e in entries):
            where = f"{rule.prefix} is not a page" if rule.page else f"no page lies under {rule.prefix}"
            raise click.ClickException(f"{PRINT_YML}: {where} in {NAV_YML}")
        if rule.mode == "list":
            entries, gone = list_section(entries, rule)
        elif rule.mode == "omit":
            entries, gone = omit_section(entries, rule)
        elif rule.mode == "reference":
            if operators is None:
                operators = load_operators()
            entries, gone = reference_section(entries, rule, operators)
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
        # A part the print edition leaves out does not summarize the page either.
        for part in article.select(f".{PRINT_EXCLUDE}") if article is not None else ():
            if not part.decomposed:
                part.decompose()
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


def render_generated(
    doc: BeautifulSoup, entry: NavEntry, site_dir: Path, public_base: str, valid_ids: set | frozenset = frozenset()
) -> list:
    """The elements that stand in for a shortened section's pages."""
    generated = entry.generated
    if generated.kind == "table":
        return [summary_table(doc, generated, site_dir)]
    if generated.kind == "groups":
        return [groups_table(doc, generated, site_dir)]
    if generated.kind == "operators":
        return operator_entries(doc, entry, site_dir, public_base, valid_ids)
    name = generated.name or page_title(site_dir, generated.pages[0])
    url = section_url(generated, site_dir, public_base)
    note = doc.new_tag("div", attrs={"class": "admonition info"})
    paragraph = doc.new_tag("p")
    if generated.mode == "reference":
        paragraph.string = (
            f"This print edition lists every operator of the {name} with its description and parameters. "
            f"The examples are part of the online edition: {url}. An operator marked Python plugin belongs to a "
            "Python plugin package, which has to be installed first, for example with cmemc."
        )
    else:
        paragraph.string = (
            f"This print edition lists the {name} in short. The complete section is part of the online edition: {url}"
        )
    note.append(paragraph)
    return [note]


def data_type(parameter_type: str) -> str:
    """How an entry names a parameter's data type (tasks/spec.md, §11)."""
    if parameter_type.startswith("option[") and parameter_type.endswith("]"):
        return f"{data_type(parameter_type[len('option['):-1])}, optional"
    if parameter_type.startswith("code-"):
        language = parameter_type[len("code-"):]
        return CODE_LANGUAGES.get(language, language.upper())
    return DATA_TYPES.get(parameter_type, parameter_type)


def inline_markdown(text: str) -> list:
    """A parameter description, rendered from its Markdown, as inline nodes."""
    if not text.strip():
        return []
    fragment = BeautifulSoup(markdown.markdown(text), "html.parser")
    blocks = [node for node in fragment.contents if not (isinstance(node, NavigableString) and not node.strip())]
    root = blocks[0] if len(blocks) == 1 and getattr(blocks[0], "name", None) == "p" else fragment
    return [child.extract() for child in list(root.contents)]


def operator_fields(doc: BeautifulSoup, record: dict) -> Tag:
    """An entry's field line: type, transformer category, plugin ID, Python plugin and a distance measure's range."""
    fields: list = [OPERATOR_TYPES.get(record["pluginType"], record["pluginType"])]
    if record["pluginType"] == "transformer" and record.get("main_category"):
        fields.append(record["main_category"])
    plugin_id = doc.new_tag("code")
    plugin_id.string = record["pluginId"]
    fields.append(plugin_id)
    if record.get("backendType") == "python":
        fields.append("Python plugin")
    if record.get("distanceMeasureRange"):
        fields.append(f"range: {record['distanceMeasureRange']}")
    line = doc.new_tag("div", attrs={"class": "operator-fields"})
    for index, value in enumerate(fields):
        if index:
            line.append(" · ")
        line.append(value)
    return line


def operator_description(doc: BeautifulSoup, site_dir: Path, md: str) -> list:
    """The description of an operator's page, as its entry prints it.

    Without the page title, the Python plugin note and the sections the entry
    sets from the plugin description or leaves out; the page's own headings print
    as run-in labels.
    """
    article = page_article(site_dir, md)
    if article is None:
        return []
    title = article.find("h1")
    if title is not None:
        title.decompose()
    for note in article.select("div.admonition"):
        label = note.find(class_="admonition-title")
        if label is not None and plain_heading(label).casefold() == "python plugin":
            note.decompose()
    for heading in article.find_all("h2"):
        if heading.decomposed or plain_heading(heading).casefold() not in OPERATOR_SECTIONS_LEFT_OUT:
            continue
        for sibling in list(heading.find_next_siblings()):
            if sibling.name == "h2":
                break
            sibling.decompose()
        heading.decompose()
    for heading in article.find_all(HEADING):
        label = doc.new_tag("p")
        strong = doc.new_tag("strong")
        strong.string = plain_heading(heading)
        label.append(strong)
        heading.replace_with(label)
    return [child.extract() for child in list(article.contents)]


def parameter_table(doc: BeautifulSoup, record: dict) -> list:
    """An entry's parameter table, and the defaults too long for a cell (tasks/spec.md, §11).

    Parameter with its ID, Type, Default and Description; advanced parameters
    after a row of their own, sub-parameters after their parameter. An operator
    without parameters has no table.
    """
    basic = list((record.get("properties") or {}).values())
    advanced = list((record.get("properties_advanced") or {}).values())
    if not basic and not advanced:
        return []
    table, body = list_table(doc, ("Parameter", "Type", "Default", "Description"))
    columns = doc.new_tag("colgroup")
    for width in ("27%", "13%", "13%", "47%"):
        columns.append(doc.new_tag("col", attrs={"style": f"width: {width}"}))
    table.insert(0, columns)
    blocks: list = []

    def code(text: str) -> Tag:
        element = doc.new_tag("code")
        element.string = text
        return element

    def add(parameter: dict, prefix: str = "") -> None:
        ident = prefix + parameter["name"]
        kind = parameter["parameterType"]
        value = parameter.get("value")
        name = list_cell(doc)
        name.append(parameter["title"])
        name.append(doc.new_tag("br"))
        name.append(code(ident))
        data = list_cell(doc)
        data.string = data_type(kind)
        default = list_cell(doc)
        if kind in ("password", "objectParameter") or value in (None, "") or isinstance(value, dict):
            default.string = "–"
        elif "\n" in str(value):
            default.string = "see below"
            label = doc.new_tag("p")
            label.append("Default of ")
            label.append(code(ident))
            label.append(":")
            block = doc.new_tag("pre")
            content = code(str(value))
            if kind.startswith("code-"):
                content["class"] = f"language-{kind[len('code-'):]}"
            block.append(content)
            blocks.extend([label, block])
        else:
            default.append(code(str(value)))
        description = list_cell(doc)
        for node in inline_markdown(parameter.get("description") or ""):
            description.append(node)
        row = doc.new_tag("tr")
        for cell in (name, data, default, description):
            row.append(cell)
        body.append(row)
        for sub in (parameter.get("properties") or {}).values():
            add(sub, f"{ident}.")

    for parameter in basic:
        add(parameter)
    if advanced:
        row = doc.new_tag("tr")
        cell = list_cell(doc)
        cell["colspan"] = "4"
        strong = doc.new_tag("strong")
        strong.string = "Advanced"
        cell.append(strong)
        row.append(cell)
        body.append(row)
        for parameter in advanced:
            add(parameter)
    return [table, *blocks]


def operator_related(doc: BeautifulSoup, record: dict, catalog: dict[str, tuple[str, str]]) -> Tag | None:
    """The line naming an entry's related operators, each linked to its entry."""
    related = [catalog[ref["id"]] for ref in record.get("relatedPlugins") or [] if ref.get("id") in catalog]
    if not related:
        return None
    line = doc.new_tag("p", attrs={"class": "operator-related"})
    line.append("Related: ")
    for index, (md, title) in enumerate(related):
        if index:
            line.append(", ")
        link = doc.new_tag("a", href=f"#{url_to_section_id(md_to_url_path(md))}")
        link.string = title
        line.append(link)
    return line


def operator_entries(
    doc: BeautifulSoup, entry: NavEntry, site_dir: Path, public_base: str, valid_ids: set | frozenset
) -> list:
    """The compact entries of a reference's operators: heading, field line, description, parameters, related."""
    generated = entry.generated
    level = min(6, entry.depth + 1)
    sections = []
    for md, record in zip(generated.pages, generated.operators):
        section_id = url_to_section_id(md_to_url_path(md))
        section = doc.new_tag("section", attrs={"class": "print-page", "id": section_id})
        for node in operator_description(doc, site_dir, md) + parameter_table(doc, record):
            section.append(node)
        namespace_ids(section, section_id)
        resolve_links(section, md_to_url_path(md), valid_ids, public_base)
        # Added after the ids and links are settled: namespacing would rewrite
        # the related operators' in-document links.
        heading = doc.new_tag(f"h{level}", attrs={"id": f"{section_id}-operator"})
        heading.string = record["title"]
        section.insert(0, heading)
        section.insert(1, operator_fields(doc, record))
        related = operator_related(doc, record, generated.catalog)
        if related is not None:
            section.append(related)
        sections.append(section)
    return sections


def exclude_parts(doc: BeautifulSoup, article, page_url: str) -> int:
    """Replace the parts of a page marked `print-exclude` with a note naming the page online (tasks/spec.md, §10).

    The note's address carries the anchor of the heading before the part, and
    consecutive parts share one note. A marked element inside another marked one
    goes with it. Returns the number of parts removed.
    """
    parts = [part for part in article.select(f".{PRINT_EXCLUDE}") if part.find_parent(class_=PRINT_EXCLUDE) is None]
    for part in parts:
        previous = next(
            (node for node in part.previous_siblings if not (isinstance(node, NavigableString) and not node.strip())),
            None,
        )
        if previous is not None and not isinstance(previous, NavigableString) and EXCLUDED_NOTE in previous.get("class", []):
            part.decompose()
            continue
        heading = part.find_previous(HEADING, id=True)
        note = doc.new_tag("div", attrs={"class": ["admonition", "info", EXCLUDED_NOTE]})
        paragraph = doc.new_tag("p")
        paragraph.string = f"{PART_NOTE} {page_url}" + (f"#{heading['id']}" if heading is not None else "")
        note.append(paragraph)
        part.replace_with(note)
    return len(parts)


def merge_pages(
    entries: list[NavEntry],
    site_dir: Path,
    public_base: str,
    rules: list[SectionRule] | None = None,
    dropped: set[str] | None = None,
    print_edition: bool = False,
) -> tuple[BeautifulSoup, list[str], dict[str, int]]:
    """Merge the built articles along the navigation into one HTML document.

    Every top-level entry is a part. It is preceded by a chapter break, so a
    part starts on a new page, and its page opens with the part's cover (see
    `part_cover`); a part without a page gets its title and the contents marker.
    Generated entries of the print edition's section modes are rendered where
    they stand, and a shortened section's links to the pages it drops print as
    text. In the print edition, the parts of a page marked `print-exclude` give
    way to a note (`exclude_parts`). Returns the document, the navigation pages
    that had no built HTML, and the number of parts left out per page.
    """
    doc = BeautifulSoup('<html><head><meta charset="utf-8"></head><body></body></html>', "html.parser")
    valid_ids = {url_to_section_id(md_to_url_path(e.md)) for e in entries if e.md}
    # The operator pages of a reference print as entries, and links to them stay in the book.
    valid_ids |= {
        url_to_section_id(md_to_url_path(md))
        for e in entries if e.generated is not None and e.generated.kind == "operators"
        for md in e.generated.pages
    }
    dropped_ids = {url_to_section_id(md_to_url_path(md)) for md in dropped or ()}
    shortening = [rule for rule in rules or () if rule.mode != "full"]
    missing: list[str] = []
    excluded: dict[str, int] = {}

    part_count = 0
    for entry in entries:
        if entry.generated is not None:
            for element in render_generated(doc, entry, site_dir, public_base, valid_ids):
                doc.body.append(element)
            continue
        if entry.depth == 0:
            # The print edition closes a part with the web addresses it cites
            # (part-addresses in style.typ).
            if print_edition and part_count:
                doc.body.append(doc.new_tag("div", attrs={"class": "part-end"}))
            part_count += 1
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
        if print_edition:
            page_url = urllib.parse.urljoin(public_base, md_to_url_path(entry.md).lstrip("/"))
            parts = exclude_parts(doc, article, page_url)
            if parts:
                excluded[entry.md] = parts
        if any(rule.mode == "reference" and reference_overview(rule, entry.md) for rule in rules or ()):
            # The operator entries that follow replace the overview table.
            for table in article.find_all("table"):
                if not table.decomposed:
                    table.decompose()

        section_id = url_to_section_id(md_to_url_path(entry.md))
        section = doc.new_tag("section", attrs={"class": "print-page", "id": section_id})
        for child in list(article.children):
            section.append(child.extract())
        namespace_ids(section, section_id)
        unlink_ids = dropped_ids if any(rule.matches(entry.md) for rule in shortening) else frozenset()
        resolve_links(section, md_to_url_path(entry.md), valid_ids, public_base, unlink_ids)
        demote_headings(section, entry.depth)
        if entry.depth == 0:
            part_cover(doc, section)
        doc.body.append(section)

    if print_edition and part_count:
        doc.body.append(doc.new_tag("div", attrs={"class": "part-end"}))
    return doc, missing, excluded


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


def typst_density(source: Path, width: str | None) -> int:
    """An original image's pixel density at the width Typst prints it, in ppi.

    Typst sizes an image by the width the page declares, else by the density the
    file declares, capped at the column - `image_widths.printed_density` instead
    measures a share of the column, which is what a source may declare.
    """
    with Image.open(source) as image:
        return round(image.width / (printed_width_pt(image, width) / 72))


def load_accepted_low_resolution(path: Path = PRINT_YML) -> set[str]:
    """The low-resolution originals print.yml accepts as they are, by their path under docs/ (backlog P15)."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    accepted = data.get("accepted-low-resolution") or []
    if not isinstance(accepted, list) or not all(isinstance(image, str) for image in accepted):
        raise click.ClickException(f"{path}: accepted-low-resolution is a list of image paths under docs/")
    return set(accepted)


def unaccepted_low_resolution(
    low_resolution: dict[str, tuple[int, str]], accepted: set[str]
) -> list[tuple[str, int, str]]:
    """The low-resolution originals that are not accepted, lowest density first, each with the width its page declares."""
    return sorted(
        ((image, ppi, width) for image, (ppi, width) in low_resolution.items() if image not in accepted),
        key=lambda item: (item[1], item[0]),
    )


def resolve_images(
    doc: BeautifulSoup,
    site_dir: Path,
    stats: Counter,
    warnings: list[str],
    print_images: Path | None = None,
    low_resolution: dict[str, tuple[int, str]] | None = None,
) -> None:
    """Point images at the files Typst embeds, and replace what it cannot embed.

    Emoji that the site loads as Twemoji images become the emoji character,
    which the vendored emoji font draws. Other remote images - status badges -
    become their alt text: the build does not fetch from the network. An SVG
    that keeps its text in foreignObject elements, as Mermaid does by default,
    renders without that text in Typst, so it is reported. With `print_images`,
    raster images point at their print copies in that directory (`print_image`),
    and `low_resolution` collects the originals below 150 ppi at their printed
    size, by their path under docs/: their lowest density, and the width the
    page declares there - the `width="NN%"` of the Markdown source.
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
            if low_resolution is not None:
                width = img.get("width", "")
                density = typst_density(path, width or None)
                if density < LOW_RESOLUTION_PPI:
                    source = urllib.parse.unquote(src.split("#")[0].split("?")[0]).lstrip("/")
                    if source not in low_resolution or density < low_resolution[source][0]:
                        low_resolution[source] = (density, width)
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


def font_codepoints(path: Path) -> set[int]:
    """The code points a TrueType font maps to a glyph, read from its Windows cmap subtable (format 12 or 4)."""
    data = path.read_bytes()
    tables = {}
    for index in range(struct.unpack(">H", data[4:6])[0]):
        entry = 12 + 16 * index
        tables[data[entry:entry + 4]] = struct.unpack(">I", data[entry + 8:entry + 12])[0]
    cmap = tables[b"cmap"]
    subtables = {}
    for index in range(struct.unpack(">H", data[cmap + 2:cmap + 4])[0]):
        platform, encoding, offset = struct.unpack(">HHI", data[cmap + 4 + 8 * index:cmap + 12 + 8 * index])
        subtables[(platform, encoding)] = cmap + offset
    codepoints: set[int] = set()
    table = subtables.get((3, 10))
    if table is not None and struct.unpack(">H", data[table:table + 2])[0] == 12:
        for group in range(struct.unpack(">I", data[table + 12:table + 16])[0]):
            start, end, _ = struct.unpack(">III", data[table + 16 + 12 * group:table + 28 + 12 * group])
            codepoints.update(range(start, end + 1))
        return codepoints
    table = subtables[(3, 1)]
    segments = struct.unpack(">H", data[table + 6:table + 8])[0] // 2
    ends = struct.unpack(f">{segments}H", data[table + 14:table + 14 + 2 * segments])
    starts_at = table + 16 + 2 * segments
    starts = struct.unpack(f">{segments}H", data[starts_at:starts_at + 2 * segments])
    deltas = struct.unpack(f">{segments}h", data[starts_at + 2 * segments:starts_at + 4 * segments])
    offsets_at = starts_at + 4 * segments
    offsets = struct.unpack(f">{segments}H", data[offsets_at:offsets_at + 2 * segments])
    for segment, (start, end, delta, offset) in enumerate(zip(starts, ends, deltas, offsets)):
        for code in range(start, min(end, 0xFFFE) + 1):
            if offset == 0:
                glyph = (code + delta) & 0xFFFF
            else:
                position = offsets_at + 2 * segment + offset + 2 * (code - start)
                glyph = struct.unpack(">H", data[position:position + 2])[0]
                glyph = (glyph + delta) & 0xFFFF if glyph else 0
            if glyph:
                codepoints.add(code)
    return codepoints


@lru_cache(maxsize=None)
def emoji_pattern(emoji_font: Path = EMOJI_FONT, text_font: Path = TEXT_FONT) -> re.Pattern:
    """Emoji the text font leaves to the emoji font: a flag, or a base emoji with its variation selector,
    skin tone and zero-width joins."""
    modifiers = {0xFE0F, 0x200D, 0x20E3, *range(0x1F3FB, 0x1F400), *range(0xE0020, 0xE0080)}
    codes = sorted(font_codepoints(emoji_font) - font_codepoints(text_font) - modifiers)
    ranges: list[list[int]] = []
    for code in codes:
        if ranges and code == ranges[-1][1] + 1:
            ranges[-1][1] = code
        else:
            ranges.append([code, code])
    base = "[" + "".join(
        re.escape(chr(start)) if start == end else f"{re.escape(chr(start))}-{re.escape(chr(end))}"
        for start, end in ranges
    ) + "]"
    modifier = "[️\U0001F3FB-\U0001F3FF]*"
    return re.compile(f"[\U0001F1E6-\U0001F1FF]{{2}}|{base}{modifier}(?:‍{base}{modifier})*")


def typst_png(pages: list[str], targets: list[Path], typst: str, preamble: str, what: str) -> None:
    """Render Typst markup to PNG, a page each, on white at 600 ppi, and save each page without alpha.

    Each page is as large as its content. A copy that would be wider than the
    text column at 600 ppi is scaled down and declares a lower density, so it
    keeps the size Typst prints it at.
    """
    work = targets[0].parent
    work.mkdir(parents=True, exist_ok=True)
    source = work / "render.typ"
    source.write_text(
        "#set page(width: auto, height: auto, margin: 0pt, fill: white)\n" + preamble
        + "\n#pagebreak()\n".join(pages) + "\n",
        encoding="utf-8",
    )
    run(
        [
            # An unknown font is only a warning to Typst, so the fonts are found from this module, not the
            # working directory.
            typst, "compile", "--root", ".", "--ignore-system-fonts",
            "--font-path", str(Path(__file__).resolve().parent / "pdf" / "fonts"),
            "--format", "png", "--ppi", str(RENDER_PPI), str(source), str(work / "page-{p}.png"),
        ],
        what,
    )
    for number, target in enumerate(targets, 1):
        page = work / f"page-{number}.png"
        with Image.open(page) as image:
            flat = image.convert("RGB")
            density = RENDER_PPI
            if flat.width > MAX_RENDER_WIDTH:
                density = RENDER_PPI * MAX_RENDER_WIDTH / flat.width
                height = max(1, round(flat.height * MAX_RENDER_WIDTH / flat.width))
                flat = flat.resize((MAX_RENDER_WIDTH, height), Image.Resampling.LANCZOS)
            flat.save(target, "PNG", dpi=(density, density))
        page.unlink()


def render_emoji(sequences: list[str], targets: list[Path], typst: str) -> None:
    """Render emoji with Typst, which draws the COLRv1 glyphs: 10 pt, from the font's ascender to its descender."""
    typst_png(
        sequences, targets, typst,
        '#set text(font: "Noto Color Emoji", size: 10pt, top-edge: "ascender", bottom-edge: "descender")\n',
        "typst (emoji)",
    )


def emoji_images(
    doc: BeautifulSoup, emoji_dir: Path, typst: str, stats: Counter, render=render_emoji
) -> list[list[str]]:
    """Render the colour emoji of the document as images, for the style to print instead (print edition).

    Typst writes colour emoji as a Type 3 font whose glyphs carry shadings and
    soft masks: transparency in the book block, and content Ghostscript 10.08
    drops or crashes on when it converts the book to CMYK (P13). The style swaps
    each sequence for its image with a show rule, so emoji in code and headings
    print as images too. Returns (sequence, image) pairs, the longest sequence
    first: the style gives the first pair precedence where sequences overlap.
    """
    pattern = emoji_pattern()
    sequences = {
        match.group(0)
        for node in doc.find_all(string=pattern)
        if type(node) is NavigableString and not any(parent.name in ("script", "style") for parent in node.parents)
        for match in pattern.finditer(node)
    }
    if not sequences:
        return []
    ordered = sorted(sequences, key=lambda sequence: (-len(sequence), sequence))
    targets = [emoji_dir / ("-".join(f"{ord(char):x}" for char in sequence) + ".png") for sequence in ordered]
    render(ordered, targets, typst)
    stats["emoji rendered as images"] += len(ordered)
    return [[sequence, typst_path(target)] for sequence, target in zip(ordered, targets)]


def keep_lead_with_heading(doc: BeautifulSoup, stats: Counter) -> None:
    """Keep a short lead paragraph with its heading and what follows it (print edition).

    A heading is sticky, so it is never the last thing on a page - but a one-line
    lead under it, such as the intended audience of a section, satisfies that and
    the break falls after the line, leaving heading and line alone at the foot of
    the page. A sticky lead carries both to where the section's content starts.
    """
    for paragraph in doc.find_all("p"):
        previous = paragraph.find_previous_sibling()
        if previous is None or previous.name not in LEAD_HEADINGS:
            continue
        if len(paragraph.get_text(" ", strip=True)) > LEAD_MAX_CHARS:
            continue
        paragraph.wrap(doc.new_tag("div", attrs={"class": "keep-with-next"}))
        stats["lead lines kept with their heading"] += 1


def rasterize_transparent_svgs(
    doc: BeautifulSoup, svg_dir: Path, typst: str, stats: Counter, render=typst_png
) -> None:
    """Render SVG images that draw with transparency as PNG on white, at their natural size (print edition).

    Typst embeds such an SVG with transparency groups and soft masks, which
    Ghostscript 10.08 draws incompletely when it writes PDF/X-4 (P13); telling it
    to ignore transparency instead strikes arrows through the labels of an
    Excalidraw diagram. Icons arrive as data URIs, other SVGs as files.
    """
    found: list[tuple[Tag, Path]] = []
    for img in doc.find_all("img"):
        src = img.get("src", "")
        if src.startswith("data:image/svg+xml;base64,"):
            markup = base64.b64decode(src.split(",", 1)[1])
            if not SVG_TRANSPARENCY.search(markup.decode("utf-8", errors="ignore")):
                continue
            source = svg_dir / f"{hashlib.sha256(markup).hexdigest()[:16]}.svg"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_bytes(markup)
        elif src.startswith("/") and src.lower().endswith(".svg"):
            source = Path(src.lstrip("/"))
            if not source.is_file() or not SVG_TRANSPARENCY.search(source.read_text(encoding="utf-8", errors="ignore")):
                continue
        else:
            continue
        found.append((img, source))
    if not found:
        return
    sources = sorted({source for _, source in found})
    targets = {
        source: svg_dir / f"{source.stem}-{hashlib.sha256(str(source).encode()).hexdigest()[:8]}.png"
        for source in sources
    }
    render(
        [f'#image("{typst_path(source)}")' for source in sources],
        [targets[source] for source in sources],
        typst, "", "typst (SVG)",
    )
    for img, source in found:
        img["src"] = typst_path(targets[source])
        stats["SVG images with transparency rendered as PNG"] += 1


def normalize(
    doc: BeautifulSoup,
    site_dir: Path,
    print_images: Path | None = None,
    low_resolution: dict[str, tuple[int, str]] | None = None,
) -> tuple[Counter, list[str]]:
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
    resolve_images(doc, site_dir, stats, warnings, print_images, low_resolution)
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
@click.option(
    "--normalize", "normalize_output",
    is_flag=True,
    envvar="PDF_NORMALIZE",
    help="Also write a PDF/X-4 copy in CMYK with Ghostscript, and check that one? Print edition only.",
)
@click.option(
    "--gray", "gray_output",
    is_flag=True,
    envvar="PDF_GRAY",
    help="Also write a greyscale preview with Ghostscript, to see the black-and-white print on screen? "
    "Print edition only.",
)
@click.option(
    "--ghostscript",
    default="gs",
    envvar="GHOSTSCRIPT",
    show_default=True,
    help="Which Ghostscript converts the book block? A wrapper works, for one that runs in a container.",
)
def build_pdf(
    build_version: str,
    edition_name: str,
    output_file: str | None,
    pandoc_binary: str,
    typst_binary: str,
    normalize_output: bool,
    gray_output: bool,
    ghostscript: str,
) -> None:
    """Build a single PDF of the whole site with pandoc and Typst."""
    version = build_version.strip() or "dev"
    print_edition = edition_name == "print"
    if (normalize_output or gray_output) and not print_edition:
        raise click.ClickException("--normalize and --gray belong to the print edition - add --edition print")
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
        if rule.mode == "reference":
            count = sum(
                len(e.generated.pages) for e in entries
                if e.generated is not None and e.generated.kind == "operators" and e.generated.section == rule.prefix
            )
            print(f"Print edition: {rule.prefix} as {rule.mode}, {count} operator entries")
        elif rule.mode != "full":
            count = sum(1 for md in dropped if rule.matches(md))
            print(f"Print edition: {rule.prefix} as {rule.mode}, {count} pages dropped")
    config = load_site_config()
    public_base = public_base_url(config, version)
    doc, missing, excluded = merge_pages(entries, SITE_DIR, public_base, rules, dropped, print_edition)
    pages = sum(1 for e in entries if e.md) - len(missing)
    headings = sum(1 for e in entries if is_heading_entry(e))
    if missing:
        print(
            f"WARNING: {len(missing)} page(s) in {NAV_YML} had no built HTML: "
            + ", ".join(missing[:5])
            + (" ..." if len(missing) > 5 else ""),
            file=sys.stderr,
        )
    for md, count in sorted(excluded.items()):
        print(f"Print edition: {count} {'part' if count == 1 else 'parts'} of {md} left out")
    print(f"Merged {pages} pages and {headings} section headings along {NAV_YML}")

    low_resolution: dict[str, tuple[int, str]] = {}
    stats, warnings = normalize(doc, SITE_DIR, work_dir / "images" if print_edition else None, low_resolution)
    emoji: list[list[str]] = []
    if print_edition:
        keep_lead_with_heading(doc, stats)
        # Transparency Ghostscript cannot convert to PDF/X-4 becomes images (P13).
        rasterize_transparent_svgs(doc, work_dir / "svg", typst, stats)
        emoji = emoji_images(doc, work_dir / "emoji", typst, stats)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    print("Normalized " + ", ".join(f"{count} {what}" for what, count in sorted(stats.items())))

    work_dir.mkdir(parents=True, exist_ok=True)
    if print_edition:
        # The originals to replace or accept (backlog P15).
        unaccepted = unaccepted_low_resolution(low_resolution, load_accepted_low_resolution())
        report = work_dir / "low-resolution.tsv"
        # The width is the one the page declares, so the entry says whether the
        # image prints too large for its pixels or needs a fresh screenshot.
        report.write_text(
            "ppi\twidth\timage\n" + "".join(f"{ppi}\t{width}\t{image}\n" for image, ppi, width in unaccepted),
            encoding="utf-8",
        )
        if unaccepted:
            print(
                f"Print edition: {len(unaccepted)} images below {LOW_RESOLUTION_PPI} ppi at their printed size, "
                f"listed in {report} - replace them, or accept them in {PRINT_YML}"
            )
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
        # The imprint's authors: the committed list with the names and
        # exclusions of print.yml applied.
        names, unnamed = load_imprint_names()
        if unnamed:
            print(
                f"WARNING: the imprint prints {len(unnamed)} authors as their GitHub ID, for want of a name "
                f"in {PRINT_YML} (authors.names): {', '.join(unnamed)}",
                file=sys.stderr,
            )
        inputs["authors"] = ", ".join(names)
        inputs["emoji"] = json.dumps(emoji)
    for key, value in inputs.items():
        command += ["--input", f"{key}={value}"]
    if print_edition and unpadded_pages(command, typ_path) % 2:
        # A printed book has an even page count; the style adds a blank last page.
        command += ["--input", "pad=true"]
    run(command + [str(typ_path), str(out)], "typst")

    print(f"PDF written to {out} ({out.stat().st_size // 1024} KB)")

    # The book block is checked before Ghostscript runs for minutes on it, and the
    # PDF/X-4 copy again for what the conversion must deliver.
    if print_edition and not print_report(out, run_preflight(out)):
        raise click.ClickException(f"preflight found errors in {out} - it is written, but not ready for print")
    if normalize_output:
        final = normalize_pdf(
            out, normalized_path(out), ensure_profile(), ghostscript, title=f"{BOOK_TITLE} - {BOOK_CONTEXT}"
        )
        print(f"PDF/X-4 written to {final} ({final.stat().st_size // 1024} KB)")
        if not print_report(final, run_preflight(final, pdfx=True)):
            raise click.ClickException(f"preflight found errors in {final} - it is written, but not ready for print")
    if gray_output:
        preview = gray_preview(
            out, gray_path(out), ghostscript=ghostscript, title=f"{BOOK_TITLE} - {BOOK_CONTEXT}"
        )
        print(f"Greyscale preview written to {preview} ({preview.stat().st_size // 1024} KB)")
