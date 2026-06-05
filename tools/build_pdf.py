"""Build a single-PDF of the site by serving `site/` and printing /print_page/.

Standalone helper (not part of dec-tool CLI) — invoked by `task pdf`.
Reads CHROME, PORT and PDF_OUT from the environment; everything has a default.
"""
from __future__ import annotations

import os
import re
import socket
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from contextlib import closing
from datetime import datetime
from pathlib import Path

DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEFAULT_OUT_STEM = "dist/documentation-eccenca-com"
SITE_DIR = Path("site")
PRINT_PATH = "/print_page/"
HEADING_TAGS = ("h1", "h2", "h3", "h4", "h5", "h6")
# Material insiders' tags plugin emits placeholders like
# "tutorials/index.md:224-279/name" before its second pass fills in the actual
# listings — but print-site has already captured page content by then.
# Headings around these placeholders carry a trailing headerlink glyph,
# so we search() instead of match() and avoid anchoring to start/end.
PLACEHOLDER_RE = re.compile(r"([\w\-./]+\.md):\d+-\d+/(?:name|slug)")


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


def url_to_section_id(url_path: str) -> str:
    """Convert a URL path like /build/active-learning/ to its print-page section id.

    The mkdocs-print-site-plugin builds section ids from URL slugs joined by
    dashes — '/build/active-learning/' -> 'build-active-learning'.
    """
    return url_path.strip("/").replace("/", "-")


def rewrite_intra_doc_links(section, base_url: str, valid_ids: set) -> None:
    """In a spliced section, rewrite <a href> values that point to other doc
    pages so they become in-PDF anchor jumps.

    Skips external URLs, mailto/tel, already-fragment-only links, and any
    target whose section id isn't present in the combined print page.
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
        if not section_id or section_id not in valid_ids:
            continue
        a["href"] = (
            f"#{section_id}-{parsed.fragment}" if parsed.fragment else f"#{section_id}"
        )


def splice_rendered_articles(print_page_html: Path, site_dir: Path) -> int:
    """Replace print-page sections whose content includes unrendered tag-listing
    placeholders with the fully-rendered ``<article>`` from the per-page HTML.

    Returns the number of sections spliced.
    """
    from bs4 import BeautifulSoup  # transitive via mkdocs

    soup = BeautifulSoup(print_page_html.read_text(encoding="utf-8"), "html.parser")
    affected: dict = {}  # section -> source markdown path (first match wins)
    for heading in soup.find_all(HEADING_TAGS):
        m = PLACEHOLDER_RE.search(heading.get_text())
        if not m:
            continue
        section = heading.find_parent("section", class_="print-page")
        if section is not None:
            affected.setdefault(section, m.group(1))

    if not affected:
        return 0

    valid_ids = {
        s.get("id")
        for s in soup.find_all("section", class_="print-page")
        if s.get("id")
    }

    count = 0
    for section, src_md in affected.items():
        built = site_dir / md_to_built_html(src_md)
        if not built.exists():
            continue
        page_soup = BeautifulSoup(built.read_text(encoding="utf-8"), "html.parser")
        article = page_soup.select_one("article.md-content__inner")
        if article is None:
            continue
        section.clear()
        for child in list(article.children):
            section.append(child)
        rewrite_intra_doc_links(section, md_to_url_path(src_md), valid_ids)
        count += 1

    if count:
        print_page_html.write_text(str(soup), encoding="utf-8")
    return count


def stamp_cover_page(print_page_html: Path, version: str, generated_at: str) -> None:
    """Replace the version + generated-at placeholders in the cover page."""
    from bs4 import BeautifulSoup  # transitive via mkdocs

    soup = BeautifulSoup(print_page_html.read_text(encoding="utf-8"), "html.parser")
    ver = soup.find(id="print-cover-version")
    if ver is not None:
        ver.string = version
    date = soup.find(id="print-cover-date")
    if date is not None:
        date.string = generated_at
    print_page_html.write_text(str(soup), encoding="utf-8")


def demote_headings_by_nav_depth(print_page_html: Path) -> None:
    """Demote headings inside each <section class="print-page"> by its nav depth.

    The mkdocs-print-site-plugin emits every page's <h1> at level 1 regardless
    of nav nesting, which makes Chrome's PDF outline come out flat. Each
    print-page section already carries a ``heading-number`` attribute like
    ``1.4.2.1`` — the number of dot-separated components minus one is its nav
    depth. Shifting every heading down by that depth makes the PDF outline
    mirror the navigation tree.
    """
    from bs4 import BeautifulSoup  # transitive via mkdocs

    soup = BeautifulSoup(print_page_html.read_text(encoding="utf-8"), "html.parser")
    sections = soup.find_all("section", class_="print-page")
    for section in sections:
        hn = section.get("heading-number")
        if not hn:
            continue
        depth = hn.count(".")
        if depth == 0:
            continue
        for h in section.find_all(HEADING_TAGS):
            # Only demote headings that belong directly to this section —
            # nested print-page sections handle their own demotion.
            if h.find_parent("section", class_="print-page") is not section:
                continue
            new_level = min(6, int(h.name[1]) + depth)
            h.name = f"h{new_level}"
    print_page_html.write_text(str(soup), encoding="utf-8")


def free_port() -> int:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wait_for(url: str, timeout: float = 30.0) -> None:
    deadline = time.monotonic() + timeout
    last_err: Exception | None = None
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as r:
                if r.status == 200:
                    return
        except Exception as exc:
            last_err = exc
            time.sleep(0.2)
    raise RuntimeError(
        f"Server at {url} did not respond within {timeout}s "
        f"(last error: {last_err!r})"
    )


def main() -> int:
    chrome = os.environ.get("CHROME", DEFAULT_CHROME)
    version = os.environ.get("BUILD_VERSION", "").strip() or "dev"
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    default_out = f"{DEFAULT_OUT_STEM}-{version.replace('.', '-')}.pdf"
    out = Path(os.environ.get("PDF_OUT", default_out))
    port_env = os.environ.get("PORT", "").strip()
    port = int(port_env) if port_env else free_port()

    print_page = SITE_DIR / "print_page" / "index.html"
    if not print_page.exists():
        print(
            f"ERROR: {print_page} not found — run `mkdocs build` first.",
            file=sys.stderr,
        )
        return 1
    if not Path(chrome).exists():
        print(f"ERROR: Chrome binary not found at: {chrome}", file=sys.stderr)
        return 1

    stamp_cover_page(print_page, version, generated_at)
    spliced = splice_rendered_articles(print_page, SITE_DIR)
    if spliced:
        print(f"Spliced {spliced} section(s) with deferred-listing placeholders")
    demote_headings_by_nav_depth(print_page)
    out.parent.mkdir(parents=True, exist_ok=True)
    url = f"http://127.0.0.1:{port}{PRINT_PATH}"
    log_path = out.parent / "build_pdf.server.log"
    log = log_path.open("w")
    server = subprocess.Popen(
        [
            sys.executable, "-u", "-m", "http.server", str(port),
            "--directory", str(SITE_DIR), "--bind", "127.0.0.1",
        ],
        stdout=log, stderr=subprocess.STDOUT,
    )
    try:
        try:
            wait_for(url)
        except RuntimeError as exc:
            log.flush()
            print(
                f"ERROR: {exc}\n--- server log ({log_path}) ---\n"
                f"{log_path.read_text()}",
                file=sys.stderr,
            )
            return 1

        print(f"Rendering {url} -> {out}")
        chrome_log_path = out.parent / "build_pdf.chrome.log"
        with chrome_log_path.open("w") as chrome_log:
            result = subprocess.run(
                [
                    chrome,
                    "--headless",
                    "--disable-gpu",
                    "--no-sandbox",
                    "--hide-scrollbars",
                    "--no-pdf-header-footer",
                    "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=60000",
                    "--export-tagged-pdf",
                    "--generate-pdf-document-outline",
                    # Suppress Chrome telemetry/feature noise. The Google updater
                    # daemon runs in a *separate* process and ignores these, so
                    # we also pipe stdout/stderr to a log file (see chrome_log).
                    "--log-level=3",
                    "--disable-background-networking",
                    "--disable-component-update",
                    "--disable-sync",
                    "--disable-default-apps",
                    "--no-first-run",
                    "--no-default-browser-check",
                    "--disable-features="
                    "OptimizationGuideModelDownloading,OptimizationHints,Translate",
                    f"--print-to-pdf={out}",
                    url,
                ],
                stdout=chrome_log,
                stderr=subprocess.STDOUT,
                check=False,
            )
        if result.returncode != 0:
            print(
                f"ERROR: Chrome exited with {result.returncode}. "
                f"Server log: {log_path}  Chrome log: {chrome_log_path}",
                file=sys.stderr,
            )
            return result.returncode
        if not out.exists() or out.stat().st_size < 1024:
            print(
                f"ERROR: PDF missing or suspiciously small: {out}",
                file=sys.stderr,
            )
            return 1
        size_kb = out.stat().st_size // 1024
        print(f"PDF written to {out} ({size_kb} KB)")
        return 0
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()
        log.close()


if __name__ == "__main__":
    sys.exit(main())
