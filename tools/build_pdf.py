"""Build a single PDF of the whole documentation with pandoc and Typst.

The page order is `nav.yml` - the generated, `check:navigation` gated
navigation spine. Each page's article is taken from the built `site/`, so every
Markdown extension (admonitions, tabs, snippets, macros, icons) is already
resolved when this script sees it. The articles are merged into one HTML
document, normalized into plain elements pandoc's HTML reader understands,
converted to Typst by pandoc with `tools/pdf/filter.lua`, and typeset by Typst
with the eccenca house style in `tools/pdf/style.typ`.

Invoked by `task pdf`. Every option falls back to an environment variable, so
BUILD_VERSION, PDF_OUT, PANDOC and TYPST keep working as tunables.
"""
from __future__ import annotations

import base64
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import click
import yaml
from bs4 import BeautifulSoup

DEFAULT_OUT_STEM = "dist/documentation-eccenca-com"
SITE_DIR = Path("site")
NAV_YML = Path("nav.yml")
MKDOCS_YML = Path("mkdocs.yml")
# Style, pandoc template, filter, logo and vendored fonts.
PDF_ASSETS = Path("tools/pdf")
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


@dataclass
class NavEntry:
    """One stop along the navigation: a page, or the title of a section that has none."""

    depth: int
    md: str | None = None
    title: str | None = None


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
    """
    entries: list[NavEntry] = []
    seen: set[str] = set()

    def add_page(md: str, depth: int) -> None:
        if md.endswith(".md") and md not in seen:
            seen.add(md)
            entries.append(NavEntry(depth=depth, md=md))

    def add_section(title: str, children: list, depth: int) -> None:
        index = section_index(children[0]) if children else None
        if index is None:
            entries.append(NavEntry(depth=depth, title=str(title)))
            add_items(children, depth + 1)
        else:
            add_page(index, depth)
            add_items(children[1:], depth + 1)

    def add_items(items: list, depth: int) -> None:
        for item in items:
            if isinstance(item, str):
                add_page(item, depth)
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        add_page(value, depth)
                    elif isinstance(value, list):
                        add_section(title, value, depth)

    add_items(nav, 0)
    return entries


def load_nav_entries(nav_yml: Path = NAV_YML) -> list[NavEntry]:
    """The navigation entries of nav.yml, in PDF order."""
    data = yaml.safe_load(nav_yml.read_text(encoding="utf-8")) or {}
    return nav_entries(data.get("nav") or [])


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


def resolve_links(section, base_url: str, valid_ids: set, public_base: str) -> None:
    """Turn page-relative URLs into something valid inside the merged document.

    Links to other documented pages become in-PDF anchor jumps. Everything
    else relative - downloadable resources, screenshots opened at full size,
    pages outside the navigation - becomes an absolute link into the published
    site, which is the only address a reader of the PDF can follow.

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


def merge_pages(
    entries: list[NavEntry], site_dir: Path, public_base: str
) -> tuple[BeautifulSoup, list[str]]:
    """Merge the built articles along the navigation into one HTML document.

    Every top-level entry is preceded by a chapter break, so a chapter starts
    on a new page together with anything its page shows above its title.
    Returns the document and the navigation pages that had no built HTML.
    """
    doc = BeautifulSoup('<html><head><meta charset="utf-8"></head><body></body></html>', "html.parser")
    valid_ids = {url_to_section_id(md_to_url_path(e.md)) for e in entries if e.md}
    missing: list[str] = []

    for entry in entries:
        if entry.depth == 0:
            doc.body.append(doc.new_tag("div", attrs={"class": "chapter-break"}))
        if entry.md is None:
            heading = doc.new_tag(f"h{min(6, entry.depth + 1)}")
            heading.string = entry.title or ""
            doc.body.append(heading)
            continue

        built = site_dir / md_to_built_html(entry.md)
        article = None
        if built.exists():
            page = BeautifulSoup(built.read_text(encoding="utf-8"), "html.parser")
            article = page.select_one(CONTENT_SELECTOR)
        if article is None:
            missing.append(entry.md)
            continue
        # Before the ids are namespaced: selectors such as #__comments would no
        # longer match afterwards.
        drop_noise(article)

        section_id = url_to_section_id(md_to_url_path(entry.md))
        section = doc.new_tag("section", attrs={"class": "print-page", "id": section_id})
        for child in list(article.children):
            section.append(child.extract())
        namespace_ids(section, section_id)
        resolve_links(section, md_to_url_path(entry.md), valid_ids, public_base)
        demote_headings(section, entry.depth)
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
    """Icons: an <img> carrying the SVG as a data URI, which pandoc sizes to the text."""
    for icon in doc.select("span.twemoji"):
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


def resolve_images(doc: BeautifulSoup, site_dir: Path, stats: Counter, warnings: list[str]) -> None:
    """Point images at the built files Typst embeds, and replace what it cannot embed.

    Emoji that the site loads as Twemoji images become the emoji character,
    which the vendored emoji font draws. Other remote images - status badges -
    become their alt text: the build does not fetch from the network. An SVG
    that keeps its text in foreignObject elements, as Mermaid does by default,
    renders without that text in Typst, so it is reported.
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


def normalize(doc: BeautifulSoup, site_dir: Path) -> tuple[Counter, list[str]]:
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
    resolve_images(doc, site_dir, stats, warnings)
    embedded_media_to_links(doc, stats)
    settle_internal_links(doc, stats)
    return stats, warnings


# -- typesetting ---------------------------------------------------------------


def edition(config: dict, version: str, public_base: str, today: date) -> dict[str, str]:
    """What the title page, header and PDF metadata print, as Typst --input values."""
    copyright_html = str(config.get("copyright") or "")
    copyright_text = " ".join(BeautifulSoup(copyright_html, "html.parser").get_text().split())
    return {
        "title": BOOK_TITLE,
        "subtitle": f"Version {version}",
        "context": BOOK_CONTEXT,
        "version": version,
        "generated": today.isoformat(),
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


@click.command()
@click.option(
    "--build-version",
    default="dev",
    envvar="BUILD_VERSION",
    help="Which version to stamp on the title page and fold into the file name?",
    show_default=True,
)
@click.option(
    "--output-file", "-o",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default=None,
    envvar="PDF_OUT",
    help=f"Where to write the PDF?  [default: {DEFAULT_OUT_STEM}-<version>.pdf]",
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
    build_version: str, output_file: str | None, pandoc_binary: str, typst_binary: str
) -> None:
    """Build a single PDF of the whole site with pandoc and Typst."""
    version = build_version.strip() or "dev"
    out = Path(output_file or f"{DEFAULT_OUT_STEM}-{version.replace('.', '-')}.pdf")

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
    config = load_site_config()
    public_base = public_base_url(config, version)
    doc, missing = merge_pages(entries, SITE_DIR, public_base)
    pages = sum(1 for e in entries if e.md) - len(missing)
    headings = sum(1 for e in entries if e.md is None)
    if missing:
        print(
            f"WARNING: {len(missing)} page(s) in {NAV_YML} had no built HTML: "
            + ", ".join(missing[:5])
            + (" ..." if len(missing) > 5 else ""),
            file=sys.stderr,
        )
    print(f"Merged {pages} pages and {headings} section headings along {NAV_YML}")

    stats, warnings = normalize(doc, SITE_DIR)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    print("Normalized " + ", ".join(f"{count} {what}" for what, count in sorted(stats.items())))

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    html_path = WORK_DIR / "book.html"
    typ_path = WORK_DIR / "book.typ"
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
    for key, value in edition(config, version, public_base, date.today()).items():
        command += ["--input", f"{key}={value}"]
    run(command + [str(typ_path), str(out)], "typst")

    print(f"PDF written to {out} ({out.stat().st_size // 1024} KB)")
