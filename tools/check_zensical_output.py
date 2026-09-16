"""Post-build checks for the Zensical migration.

Zensical silently ignores MkDocs plugins it does not implement, so
``zensical build --strict`` stays green even when features disappear from the
output. This script inspects the generated ``site/`` directory instead of the
configuration and fails the build when a feature we have replaced ourselves
regresses.

Two classes of checks:

* REQUIRED - features we own. A failure here is a real regression and exits 1.
* PENDING  - features Zensical has not shipped yet. These never fail the build,
             but they shout loudly once they start passing, which is the signal
             to revisit the migration.

Usage: dec-tool check-zensical-output [--site-dir SITE_DIR] [--config-file CONFIG_FILE]
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import click
import yaml

# Hosts that may legitimately appear in the output. Everything else must be
# vendored locally - see the privacy-plugin replacement in handoff.md.
ALLOWED_EXTERNAL_HOSTS = {
    "www.googletagmanager.com",  # consent-gated analytics
    "giscus.app",  # consent-gated comments
    "img.shields.io",  # badges, previously in assets_exclude
    "badge.fury.io",  # badges, previously in assets_exclude
    "raw.githubusercontent.com",  # badges, previously in assets_exclude
    "cdn.jsdelivr.net",  # MathJax, previously in assets_exclude
}

# Pages that opt out of comments via `comments: false` front matter.
COMMENTS_OPT_OUT = [
    "",  # docs/index.md
    "getting-started/with-your-sandbox",
    "getting-started/with-your-sandbox/material",
]

# Zensical's redirect pages refresh to a URL relative to their own location.
REFRESH_RE = re.compile(r'<meta http-equiv="refresh" content="\d+;\s*url=([^"]+)"', re.IGNORECASE)
# Any absolute base will do: it only anchors urljoin while it resolves `..`.
URL_BASE = "https://site.invalid/"

# Only tags that make the browser fetch something. Plain <a href> hyperlinks to
# the outside world are content, not a privacy problem.
ASSET_RE = re.compile(
    r"<(script|link|img|iframe|source|video|audio|embed)\b([^>]*?)"
    r'\b(?:src|href)="https?://([^/"]+)',
    re.IGNORECASE,
)
# <link rel="canonical"> and friends are metadata, not asset loads.
LINK_META_RE = re.compile(r'rel="(canonical|alternate|manifest)"', re.IGNORECASE)
TAGS_LISTING_RE = re.compile(r'<h2 id="tag:([^"]+)"')
# Zensical (0.0.58+) renders tag chips as links to their /tags/ listing anchor
# natively; this just asserts every chip's target actually exists there.
TAG_CHIP_RE = re.compile(r'<a href="([^"]*tags/#tag:([^"]+))"[^>]*class="md-tag[ "]')

failures: list[str] = []
notices: list[str] = []


class TolerantLoader(yaml.SafeLoader):
    """A safe YAML loader that reads tags it cannot construct, such as `!!python/name:`, as null."""


TolerantLoader.add_multi_constructor("", lambda loader, suffix, node: None)


def report(name: str, ok: bool, detail: str, required: bool) -> None:
    """Record and print the outcome of a single check."""
    if required:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(f"{name}: {detail}")
    else:
        print(f"[{'NEW ' if ok else 'PEND'}] {name}: {detail}")
        if ok:
            notices.append(name)


def html_files(site: Path) -> list[Path]:
    return sorted(site.rglob("*.html"))


def redirect_maps(config: Path) -> dict[str, str]:
    """Return the `redirect_maps` of the redirects plugin in a MkDocs configuration."""
    data = yaml.load(config.read_text(encoding="utf-8"), Loader=TolerantLoader) or {}  # noqa: S506
    plugins = data.get("plugins") or []
    if isinstance(plugins, dict):
        plugins = [{name: options} for name, options in plugins.items()]
    for plugin in plugins:
        if isinstance(plugin, dict) and "redirects" in plugin:
            return dict((plugin["redirects"] or {}).get("redirect_maps") or {})
    return {}


def page_url(path: str) -> str:
    """Return the site-relative URL of a docs/ Markdown path, e.g. `a/index.md#b` -> `a/#b`."""
    path, hash_mark, fragment = path.partition("#")
    stem = path.removesuffix(".md")
    if stem == "index" or stem.endswith("/index"):
        url = stem.removesuffix("index")
    else:
        url = f"{stem}/"
    return url + hash_mark + fragment


def check_redirects(site: Path, config: Path) -> None:
    """Every page redirect in mkdocs.yml must land on its target in the build.

    Zensical's redirects plugin writes the redirect pages since 0.0.61, and
    `--strict` rejects a target that does not exist. What it cannot catch is a
    redirect page that is missing or points elsewhere - a regression in
    Zensical's output. Anchor redirects (`page.md#old`) are resolved in the
    browser from redirect.json and are not checked here.
    """
    if not config.is_file():
        report("redirects", False, f"{config} not found", required=True)
        return
    maps = redirect_maps(config)
    if not maps:
        report("redirects", False, f"no redirect_maps in {config}, so no old URL resolves", required=True)
        return

    for source, target in maps.items():
        if "#" in source:
            continue
        source_url = page_url(source)
        internal = not target.startswith(("http://", "https://"))
        expected = page_url(target) if internal else target
        shown = f"/{expected}" if internal else expected

        page = site / source_url / "index.html"
        if not page.is_file():
            report("redirects", False, f"no redirect page at /{source_url}", required=True)
            continue
        match = REFRESH_RE.search(page.read_text(encoding="utf-8", errors="replace"))
        if not match:
            report("redirects", False, f"/{source_url} is not a redirect page", required=True)
            continue
        landed = urljoin(URL_BASE + source_url, html.unescape(match.group(1))).removeprefix(URL_BASE)
        if landed != expected:
            report("redirects", False, f"/{source_url} redirects to /{landed}, expected {shown}", required=True)
            continue
        if internal and not (site / expected.partition("#")[0] / "index.html").is_file():
            report("redirects", False, f"/{source_url} redirects to {shown}, which was not built", required=True)
            continue
        report("redirects", True, f"/{source_url} -> {shown}", required=True)


def check_comments(site: Path, pages: list[Path]) -> None:
    """Giscus replaces the meta plugin's global `comments: true`.

    Default is on; the three pages below opt out via `comments: false` front
    matter and must stay opted out.
    """
    hits = sum(1 for p in pages if "giscus" in p.read_text(encoding="utf-8", errors="replace"))
    report(
        "comments-default-on",
        hits > len(pages) * 0.9,
        f"giscus present on {hits}/{len(pages)} pages",
        required=True,
    )

    leaked = []
    for rel in COMMENTS_OPT_OUT:
        page = site / rel / "index.html" if rel else site / "index.html"
        if page.is_file() and "giscus" in page.read_text(encoding="utf-8", errors="replace"):
            leaked.append(rel or "/")
    report(
        "comments-opt-out",
        not leaked,
        f"opt-out honoured on {len(COMMENTS_OPT_OUT)} pages"
        if not leaked
        else f"giscus leaked onto {', '.join(leaked)}",
        required=True,
    )


def check_tag_chip_links(site: Path, pages: list[Path]) -> None:
    """Every per-page tag chip must link to an anchor that exists on /tags/."""
    listing = site / "tags" / "index.html"
    anchors = set(
        TAGS_LISTING_RE.findall(listing.read_text(encoding="utf-8", errors="replace"))
        if listing.is_file()
        else []
    )

    linked_pages = 0
    chips = 0
    dangling: dict[str, str] = {}
    for page in pages:
        found = TAG_CHIP_RE.findall(page.read_text(encoding="utf-8", errors="replace"))
        if not found:
            continue
        linked_pages += 1
        chips += len(found)
        for _href, slug in found:
            if slug not in anchors:
                dangling.setdefault(slug, page.relative_to(site).as_posix())

    report(
        "tag-chips-linked",
        chips > 0,
        f"{chips} chip(s) on {linked_pages} page(s) link to /tags/"
        if chips
        else "no tag chips link anywhere - did Zensical stop linking tag chips?",
        required=True,
    )
    report(
        "tag-chips-resolve",
        not dangling,
        "every chip anchor exists on /tags/"
        if not dangling
        else f"{len(dangling)} slug(s) missing from /tags/, e.g. "
        + ", ".join(f"#tag:{s} (on {p})" for s, p in sorted(dangling.items())[:3]),
        required=True,
    )


def check_external_assets(pages: list[Path]) -> None:
    """No third-party requests - replaces the privacy plugin's assets_fetch."""
    offenders: dict[str, int] = {}
    for page in pages:
        body = page.read_text(encoding="utf-8", errors="replace")
        for tag, attrs, host in ASSET_RE.findall(body):
            if tag.lower() == "link" and LINK_META_RE.search(attrs):
                continue
            if host not in ALLOWED_EXTERNAL_HOSTS:
                offenders[host] = offenders.get(host, 0) + 1
    if offenders:
        listed = ", ".join(f"{h} ({n}x)" for h, n in sorted(offenders.items()))
        report("external-assets", False, f"unvendored hosts: {listed}", required=True)
    else:
        report("external-assets", True, "no unexpected third-party hosts", required=True)


def check_pending(site: Path, pages: list[Path]) -> None:
    """Features still missing from Zensical - warn only, never fail."""
    social = sum(1 for p in pages if 'property="og:image"' in p.read_text(encoding="utf-8", errors="replace"))
    report("social-cards", social > 0, f"og:image on {social} pages (backlog #37)", required=False)


    revision = sum(1 for p in pages if "Last update" in p.read_text(encoding="utf-8", errors="replace"))
    report("revision-dates", revision > 0, f"last-update on {revision} pages (backlog #18)", required=False)


@click.command()
@click.option(
    "--site-dir",
    type=click.Path(exists=False, dir_okay=True, file_okay=False),
    default="site",
    help="Which build output should be checked?",
    show_default=True,
)
@click.option(
    "--config-file",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default="mkdocs.yml",
    help="Which configuration holds the redirect_maps?",
    show_default=True,
)
def check_zensical_output(site_dir: str, config_file: str) -> None:
    """Check the build output for regressed Zensical workarounds."""
    site = Path(site_dir)
    if not site.is_dir():
        print(f"error: {site}/ not found - run `task build` first", file=sys.stderr)
        sys.exit(2)

    pages = html_files(site)
    print(f"Checking {len(pages)} HTML files in {site}/\n")

    check_redirects(site, Path(config_file))
    check_comments(site, pages)
    check_external_assets(pages)
    check_tag_chip_links(site, pages)
    print()
    check_pending(site, pages)
    print()

    if notices:
        print("=" * 68)
        print("Zensical now ships: " + ", ".join(notices))
        print("Remove the local workaround and drop the check from PENDING.")
        print("=" * 68)

    if failures:
        print(f"\n{len(failures)} required check(s) failed:")
        for item in failures:
            print(f"  - {item}")
        sys.exit(1)

    print("All required checks passed.")
