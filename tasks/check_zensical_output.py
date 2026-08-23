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

Usage: python tools/check_zensical_output.py [site_dir]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

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

REDIRECTS = {
    "cmemc": "automate/cmemc-command-line-interface/",
    "explore-and-author/building-a-customized-user-interface": (
        "explore-and-author/graph-exploration/building-a-customized-user-interface/"
    ),
}

# Only tags that make the browser fetch something. Plain <a href> hyperlinks to
# the outside world are content, not a privacy problem.
ASSET_RE = re.compile(
    r"<(script|link|img|iframe|source|video|audio|embed)\b([^>]*?)"
    r'\b(?:src|href)="https?://([^/"]+)',
    re.IGNORECASE,
)
# <link rel="canonical"> and friends are metadata, not asset loads.
LINK_META_RE = re.compile(r'rel="(canonical|alternate|manifest)"', re.IGNORECASE)
ARTICLE_RE = re.compile(r"<article.*?</article>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")

failures: list[str] = []
notices: list[str] = []


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


def check_redirects(site: Path) -> None:
    """Redirect stubs replace the mkdocs-redirects plugin."""
    for source, target in REDIRECTS.items():
        page = site / source / "index.html"
        if not page.is_file():
            report("redirects", False, f"missing stub for /{source}/", required=True)
            continue
        body = page.read_text(encoding="utf-8", errors="replace")
        if "http-equiv" not in body.lower() or target.rstrip("/") not in body:
            report(
                "redirects",
                False,
                f"/{source}/ does not redirect to /{target}",
                required=True,
            )
            continue
        report("redirects", True, f"/{source}/ -> /{target}", required=True)


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


def article_words(page: Path) -> int:
    body = page.read_text(encoding="utf-8", errors="replace")
    match = ARTICLE_RE.search(body)
    return len(TAG_RE.sub(" ", match.group(0)).split()) if match else 0


def check_pending(site: Path, pages: list[Path]) -> None:
    """Features still missing from Zensical - warn only, never fail."""
    social = sum(1 for p in pages if 'property="og:image"' in p.read_text(encoding="utf-8", errors="replace"))
    report("social-cards", social > 0, f"og:image on {social} pages (backlog #37)", required=False)

    tags_page = site / "tags" / "index.html"
    words = article_words(tags_page) if tags_page.is_file() else 0
    report("tag-listings", words > 50, f"/tags/ article has {words} words (backlog #38)", required=False)

    revision = sum(1 for p in pages if "Last update" in p.read_text(encoding="utf-8", errors="replace"))
    report("revision-dates", revision > 0, f"last-update on {revision} pages (backlog #18)", required=False)


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    if not site.is_dir():
        print(f"error: {site}/ not found - run `task build` first", file=sys.stderr)
        return 2

    pages = html_files(site)
    print(f"Checking {len(pages)} HTML files in {site}/\n")

    check_redirects(site)
    check_comments(site, pages)
    check_external_assets(pages)
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
        return 1

    print("All required checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
