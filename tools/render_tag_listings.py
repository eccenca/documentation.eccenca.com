"""Render the tag listings that Zensical does not implement.

Material's ``tags`` plugin expands ``<!-- material/tags -->`` markers into a list
of the pages carrying each tag. Zensical renders the per-page tag *chips* but not
the *listings*, and it passes the markers through to the output verbatim - so
``/tags/`` and ``/tutorials/`` publish with an empty body and no warning.

This script fills them in after the build, the same way
``tools/localize_bundle_assets.py`` patches the JS bundle. Working on ``site/``
rather than on ``docs/`` keeps the Markdown sources untouched: they still use
Material's own marker syntax, so when Zensical ships listings
(https://github.com/zensical/backlog/issues/38) the feature lights up natively
and this file is simply deleted. See tasks/spec.md.

The emitted markup mirrors what Material produces today, verified against
https://documentation.eccenca.com/latest/tutorials/.

Usage: python tools/render_tag_listings.py [site_dir]
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import yaml

DOCS_DIR = Path("docs")
CONFIG = Path("mkdocs.yml")
NAV = Path("nav.yml")

# `<!-- material/tags -->` or `<!-- material/tags { include: [Tag, Other] } -->`
MARKER_RE = re.compile(r"<!--\s*material/tags\b(?P<args>.*?)-->", re.DOTALL)
INCLUDE_RE = re.compile(r"^\{\s*include:\s*\[(?P<tags>[^\]]*)\]\s*\}$")

# Left behind so a later run can tell "we already rendered this" apart from
# "Zensical rendered it natively" - the latter is the signal to delete this
# script (tasks/spec.md, "Removal").
SENTINEL = "<!-- tag-listing rendered by tools/render_tag_listings.py -->"

FRONT_MATTER_RE = re.compile(r"^---\n(?P<fm>.*?)\n---\n?", re.DOTALL)
PERMALINK_RE = re.compile(r"^  - toc:\n(?:      .*\n)*?      permalink:\s*(?P<mark>.+?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.MULTILINE)
# A `#` inside a fenced block is a comment, not a heading - strip fences first.
FENCE_RE = re.compile(r"^(?P<f>```+|~~~+).*?^(?P=f)\s*$", re.MULTILINE | re.DOTALL)
# Material renders `:material-star:` as an icon; the text title excludes it.
ICON_RE = re.compile(r":[a-z0-9_]+(?:-[a-z0-9_]+)*:")
INLINE_RE = re.compile(r"[`*_]+")

# Zensical emits the same `<article>` wrapper Material does; the marker always
# lands inside it, so no additional scoping is required.


def load_tag_icons() -> dict[str, str]:
    """`extra.tags` maps a tag name to the icon key used in its CSS class.

    Tags missing from the map render as a bare `md-tag`, which is what Material
    does and what production ships today (14 of the 45 tags in use).
    """
    text = CONFIG.read_text(encoding="utf-8")
    block = re.search(r"^  tags:\n((?:    .*\n)+)", text, re.MULTILINE)
    if not block:
        return {}
    icons: dict[str, str] = {}
    for line in block.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.match(r'"?(?P<tag>[^":]+?)"?\s*:\s*(?P<icon>\S+)', stripped)
        if match:
            icons[match.group("tag").strip()] = match.group("icon").strip()
    return icons


def permalink_mark() -> str:
    """The `toc.permalink` glyph, so our headings match every other heading."""
    match = PERMALINK_RE.search(CONFIG.read_text(encoding="utf-8"))
    return match.group("mark").strip("\"'") if match else "\u00a4"


def load_nav_titles() -> dict[str, str]:
    """`{docs-relative md path: explicit nav title}` from the generated nav.yml."""
    if not NAV.is_file():
        return {}
    titles: dict[str, str] = {}

    def walk(items: object) -> None:
        if isinstance(items, list):
            for item in items:
                walk(item)
        elif isinstance(items, dict):
            for title, value in items.items():
                if isinstance(value, str) and value.endswith(".md"):
                    titles[value] = str(title)
                else:
                    walk(value)

    try:
        walk((yaml.safe_load(NAV.read_text(encoding="utf-8")) or {}).get("nav"))
    except yaml.YAMLError:
        return {}
    return titles


def path_title(source: Path) -> str:
    """MkDocs' last-resort title: separators to spaces, capitalise only if the
    name is entirely lower case, so acronyms survive."""
    stem = source.parent.name if source.name == "index.md" else source.stem
    title = stem.replace("-", " ").replace("_", " ")
    return title.capitalize() if title.lower() == title else title


def page_title(source: Path, nav_titles: dict[str, str] | None = None) -> str:
    """Resolve a page's listing title the way MkDocs does.

    Precedence, each step verified against production:

    1. an explicit nav title - MkDocs assigns it before anything else and then
       returns early, so it outranks even front matter. `cmemc-command-line-
       interface` proves it: front matter says "cmemc (Overview)", nav says
       "cmemc - Command Line Interface", and production lists the latter.
    2. front-matter `title:`
    3. the first `# ` heading
    4. the path, capitalised only when entirely lower case

    Note this makes listings agree with the navigation, which is the point:
    build_nav.py now gives every entry an explicit title, so a handful of pages
    list under their nav title where production - whose nav auto-discovers them
    without one - falls through to their H1.
    """
    text = source.read_text(encoding="utf-8", errors="replace")
    match = FRONT_MATTER_RE.match(text)
    body = text[match.end() :] if match else text
    if match:
        try:
            meta = yaml.safe_load(match.group("fm")) or {}
        except yaml.YAMLError:
            meta = {}
        if isinstance(meta, dict) and meta.get("title"):
            return str(meta["title"]).strip()
    heading = H1_RE.search(FENCE_RE.sub("", body))
    if heading:
        title = ICON_RE.sub("", heading.group("title"))
        title = INLINE_RE.sub("", title).strip()
        if title:
            return title
    rel = source.relative_to(DOCS_DIR).as_posix()
    if nav_titles and rel in nav_titles:
        return nav_titles[rel]
    return path_title(source)


def page_meta(source: Path) -> dict:
    match = FRONT_MATTER_RE.match(source.read_text(encoding="utf-8", errors="replace"))
    if not match:
        return {}
    try:
        meta = yaml.safe_load(match.group("fm")) or {}
    except yaml.YAMLError:
        return {}
    return meta if isinstance(meta, dict) else {}


def site_url(source: Path) -> str:
    """Map a docs-relative Markdown path to its published directory URL."""
    rel = source.relative_to(DOCS_DIR).as_posix()
    rel = rel[: -len("index.md")] if rel.endswith("index.md") else rel[: -len(".md")] + "/"
    return "/" + rel.lstrip("/")


def build_index(docs: Path = DOCS_DIR) -> tuple[dict[str, list[tuple[str, str]]], list[str]]:
    """Collect `{tag: [(title, url)]}` from every page's front matter."""
    index: dict[str, list[tuple[str, str]]] = {}
    problems: list[str] = []
    nav_titles = load_nav_titles()
    for source in sorted(docs.rglob("*.md")):
        meta = page_meta(source)
        tags = meta.get("tags") or []
        if not isinstance(tags, list) or not tags:
            continue
        title = page_title(source, nav_titles)
        url = site_url(source)
        for tag in tags:
            index.setdefault(str(tag), []).append((title, url))
    # `listings_sort_by: item_title`
    for entries in index.values():
        entries.sort(key=lambda e: e[0].casefold())
    return index, problems


def parse_marker(args: str) -> list[str] | None:
    """Return the `include:` tag filter, or None for an unfiltered listing.

    Raises ValueError on an argument we do not understand, so that an unknown
    filter fails the build instead of silently listing every tag.
    """
    args = args.strip()
    if not args:
        return None
    match = INCLUDE_RE.match(args)
    if not match:
        raise ValueError(f"unsupported marker argument: {args!r}")
    tags = [t.strip().strip("\"'") for t in match.group("tags").split(",")]
    return [t for t in tags if t]


def relative_href(from_url: str, to_url: str) -> str:
    """Relative link between two directory URLs, for mike's versioned prefixes."""
    if from_url == to_url:
        return "./"
    src = [p for p in from_url.strip("/").split("/") if p]
    dst = [p for p in to_url.strip("/").split("/") if p]
    common = 0
    while common < len(src) and common < len(dst) and src[common] == dst[common]:
        common += 1
    up = [".."] * (len(src) - common)
    return "/".join(up + dst[common:]) + "/" if (up or dst[common:]) else "./"


def tag_slug(tag: str) -> str:
    return "tag:" + tag.lower().replace(" ", "-")


def render_listing(
    tags: list[str],
    index: dict[str, list[tuple[str, str]]],
    icons: dict[str, str],
    page_url: str,
    mark: str,
) -> str:
    """Render one marker's worth of listing HTML."""
    out: list[str] = []
    for tag in tags:
        entries = [e for e in index.get(tag, []) if e[1] != page_url]
        if not entries:
            continue
        slug = tag_slug(tag)
        icon = icons.get(tag)
        css = f"md-tag md-tag-icon md-tag--{icon}" if icon else "md-tag"
        out.append(
            f'<h2 id="{html.escape(slug, quote=True)}">\n'
            f'<span class="{css}">{html.escape(tag)}</span>'
            f'<a class="headerlink" href="#{html.escape(slug, quote=True)}"'
            f' title="Permanent link">{html.escape(mark)}</a></h2>'
        )
        items = "\n".join(
            f'      <li>\n        <a href="{html.escape(relative_href(page_url, url), quote=True)}">\n'
            f"          {html.escape(title)}\n        </a>\n      </li>"
            for title, url in entries
        )
        out.append(f"  <ul>\n{items}\n  </ul>")
    return "\n".join(out)


def page_url_for(page: Path, site: Path) -> str:
    rel = page.relative_to(site).as_posix()
    rel = rel[: -len("index.html")] if rel.endswith("index.html") else rel
    return "/" + rel.lstrip("/")


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    if not site.is_dir():
        print(f"error: {site}/ not found - run `task build` first", file=sys.stderr)
        return 2

    index, problems = build_index()
    icons = load_tag_icons()
    mark = permalink_mark()
    all_tags = sorted(index, key=str.casefold)  # `listings_tags_sort_by: tag_name_casefold`

    rendered = 0
    for page in sorted(site.rglob("*.html")):
        body = page.read_text(encoding="utf-8", errors="replace")
        if "material/tags" not in body:
            continue
        url = page_url_for(page, site)

        def substitute(match: re.Match[str]) -> str:
            nonlocal rendered
            try:
                include = parse_marker(match.group("args"))
            except ValueError as exc:
                problems.append(f"{page.relative_to(site)}: {exc}")
                return match.group(0)
            tags = all_tags if include is None else include
            unknown = [t for t in tags if t not in index]
            if unknown:
                problems.append(
                    f"{page.relative_to(site)}: no pages carry {', '.join(unknown)}"
                )
                return match.group(0)
            rendered += 1
            return SENTINEL + "\n" + render_listing(tags, index, icons, url, mark)

        patched = MARKER_RE.sub(substitute, body)
        if patched != body:
            page.write_text(patched, encoding="utf-8")
            print(f"[OK] {page.relative_to(site)}: rendered listing(s)")

    leftover = [
        p.relative_to(site).as_posix()
        for p in site.rglob("*.html")
        if MARKER_RE.search(p.read_text(encoding="utf-8", errors="replace"))
    ]
    for item in leftover:
        problems.append(f"{item}: marker still unexpanded after rendering")

    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for item in problems:
            print(f"  - {item}", file=sys.stderr)
        return 1

    if not rendered and not any(
        SENTINEL in p.read_text(encoding="utf-8", errors="replace")
        for p in site.rglob("*.html")
    ):
        print("=" * 68)
        print("No `material/tags` markers found and nothing of ours in the output:")
        print("Zensical now renders tag listings itself. Delete this script, drop it")
        print("from `build` in Taskfile.yml, and see tasks/spec.md 'Removal'.")
        print("=" * 68)
        return 0

    print(f"[OK] {rendered} listing(s) rendered from {len(index)} tag(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
