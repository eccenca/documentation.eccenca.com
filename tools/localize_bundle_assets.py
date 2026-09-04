"""Rewrite third-party asset URLs baked into Zensical's JavaScript bundle.

Zensical ships a pre-built ``bundle.<hash>.min.js`` that lazy-loads a handful of
libraries from ``unpkg.com`` at runtime. Those URLs are compiled into the
bundle: there is no configuration option for them, and because the requests are
issued by JavaScript rather than by a ``<script>`` tag in the HTML,
``tools/check_zensical_output.py`` cannot see them.

For this site only ``glightbox`` is actually reachable - it is pulled in on
every page that contains a lightbox image, which is most of the image-carrying
pages. The previous Material for MkDocs build served glightbox from its own
origin, so leaving it on unpkg would be a genuine regression: it leaks visitor
IP addresses to a third party on page view. This script vendors it instead.

The remaining URLs are unreachable for this corpus (no mermaid diagrams, no Ace
editor blocks, no Pyodide REPLs, and the ResizeObserver polyfill only loads on
browsers that predate ResizeObserver). They are listed in ``INERT_URLS`` and
asserted to stay unchanged, so that a Zensical upgrade which adds or moves a
third-party URL fails the build instead of silently shipping it.

Run after ``zensical build``. Usage: dec-tool localize-bundle-assets [--site-dir SITE_DIR]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import click

# Rewritten to the vendored copies under docs/assets/glightbox/. Zensical writes
# a per-page `{"base": "."|".."|...}` into the `__config` element, which is what
# the bundle itself uses to build relative URLs; reusing it keeps the rewrite
# correct at any nesting depth and under mike's versioned /latest/ prefix.
BASE_EXPR = 'JSON.parse(document.getElementById("__config").textContent).base'

REWRITES = {
    "https://unpkg.com/glightbox@3/dist/js/glightbox.min.js": "assets/glightbox/glightbox.min.js",
    "https://unpkg.com/glightbox@3/dist/css/glightbox.min.css": "assets/glightbox/glightbox.min.css",
}

# Third-party URLs left in the bundle because no page can trigger them. Keep in
# sync deliberately - see ``check_inert`` for what "cannot trigger" is checked
# against.
INERT_URLS = {
    "https://unpkg.com/ace-builds@1.44.0/src-noconflict/ace.js",
    "https://unpkg.com/mermaid@11/dist/mermaid.min.js",
    "https://unpkg.com/pyodide@314.0.2/pyodide.js",
    "https://cdn.jsdelivr.net/pyodide/v314.0.2/full/",
    "https://unpkg.com/resize-observer-polyfill",
}

URL_RE = re.compile(r'https://(?:unpkg\.com|cdn\.jsdelivr\.net|cdnjs\.cloudflare\.com)/[^"\')\s]+')

# Markers that would mean one of the INERT_URLS is reachable after all.
REACHABLE_MARKERS = {
    "mermaid": re.compile(r'class="mermaid"|<pre class="mermaid'),
    "ace/pyodide": re.compile(r'data-md-component="editor"|data-md-exec-state'),
}


def bundles(site: Path) -> list[Path]:
    return sorted(site.glob("assets/javascripts/bundle*.min.js"))


def check_inert(site: Path) -> list[str]:
    """Fail if a page uses a feature whose loader still points at a CDN."""
    problems = []
    for name, marker in REACHABLE_MARKERS.items():
        hits = [
            p.relative_to(site).as_posix()
            for p in site.rglob("*.html")
            if marker.search(p.read_text(encoding="utf-8", errors="replace"))
        ]
        if hits:
            problems.append(
                f"{name} is used on {len(hits)} page(s) (e.g. {hits[0]}) but its "
                f"loader still points at a third-party CDN - vendor it too"
            )
    return problems


@click.command()
@click.option(
    "--site-dir",
    type=click.Path(exists=False, dir_okay=True, file_okay=False),
    default="site",
    help="Which build output should be rewritten?",
    show_default=True,
)
def localize_bundle_assets(site_dir: str) -> None:
    """Rewrite third-party asset URLs in the built JavaScript bundle."""
    site = Path(site_dir)
    if not site.is_dir():
        print(f"error: {site}/ not found - run `task build` first", file=sys.stderr)
        sys.exit(2)

    found = bundles(site)
    if not found:
        print("error: no assets/javascripts/bundle*.min.js in the build", file=sys.stderr)
        sys.exit(1)

    problems: list[str] = []
    for bundle in found:
        body = bundle.read_text(encoding="utf-8")
        for url, local in REWRITES.items():
            literal = f'"{url}"'
            count = body.count(literal)
            if count == 0 and f'"/{local}"' in body:
                print(f"[OK] {bundle.name}: {url} already localised")
                continue
            if count != 1:
                problems.append(f"{bundle.name}: expected 1 occurrence of {url}, found {count}")
                continue
            body = body.replace(literal, f'{BASE_EXPR}+"/{local}"')
            print(f"[OK] {bundle.name}: {url} -> <base>/{local}")

        leftover = set(URL_RE.findall(body))
        for url in sorted(leftover - INERT_URLS):
            problems.append(f"{bundle.name}: unexpected third-party URL {url}")
        for url in sorted(INERT_URLS - leftover):
            problems.append(
                f"{bundle.name}: {url} is no longer in the bundle - drop it from INERT_URLS"
            )
        bundle.write_text(body, encoding="utf-8")

    for local in REWRITES.values():
        if not (site / local).is_file():
            problems.append(f"vendored asset missing from the build: {local}")

    problems += check_inert(site)

    if problems:
        print(f"\n{len(problems)} problem(s):", file=sys.stderr)
        for item in problems:
            print(f"  - {item}", file=sys.stderr)
        sys.exit(1)

    print(f"[OK] {len(INERT_URLS)} remaining third-party URL(s) are unreachable for this corpus")
