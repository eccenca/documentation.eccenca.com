"""Build a single linearized PDF of the whole documentation.

Assembles one HTML document from `nav.yml` - the generated, `check:navigation`
gated navigation spine - splicing in the already-rendered per-page HTML from
`site/`, then serves that document and prints it with headless Chrome.

Standalone helper (not part of dec-tool CLI) - invoked by `task pdf`.
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
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

DEFAULT_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEFAULT_OUT_STEM = "dist/documentation-eccenca-com"
SITE_DIR = Path("site")
NAV_YML = Path("nav.yml")
MKDOCS_YML = Path("mkdocs.yml")
COVER_TEMPLATE = Path("overrides/print_cover.html")
# Any built page works as the shell: it supplies the theme <head>, the stylesheet
# links and the header chrome that docs/assets/extra.css already styles for print.
SHELL_PAGE = SITE_DIR / "index.html"
PRINT_PATH = "/print_page/"
PRINT_PAGE = SITE_DIR / "print_page" / "index.html"
CONTENT_SELECTOR = "article.md-content__inner"
HEADING_TAGS = ("h1", "h2", "h3", "h4", "h5", "h6")
# Interactive widgets that carry no meaning in a PDF.
NOISE_SELECTORS = ("#__comments", ".giscus", ".md-feedback")


@dataclass
class NavEntry:
    """One page in the navigation spine."""

    md: str
    depth: int


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


def load_nav_entries() -> list[NavEntry]:
    """Flatten nav.yml into the page order the PDF follows.

    A nav item is either a bare path, a `Title: path` mapping, or a
    `Title: [children]` section which nests one level deeper. Section titles
    are not emitted: every page already opens with its own <h1>, which the
    heading demotion below places at the right outline level.
    """
    data = yaml.safe_load(NAV_YML.read_text(encoding="utf-8")) or {}
    entries: list[NavEntry] = []
    seen: set[str] = set()

    def walk(items: list, depth: int) -> None:
        for item in items:
            if isinstance(item, str):
                add(item, depth)
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        add(value, depth)
                    elif isinstance(value, list):
                        walk(value, depth + 1)

    def add(md: str, depth: int) -> None:
        if md.endswith(".md") and md not in seen:
            seen.add(md)
            entries.append(NavEntry(md=md, depth=depth))

    walk(data.get("nav") or [], 0)
    # Top-level nav items are sections, so their pages start one level in.
    # Rebase so the shallowest page is <h1> and the PDF outline gets a top
    # level - otherwise every heading is demoted and the outline is headless.
    if entries:
        floor = min(e.depth for e in entries)
        for entry in entries:
            entry.depth -= floor
    return entries


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
    """Convert a URL path like /build/active-learning/ to its section id."""
    return url_path.strip("/").replace("/", "-")


def namespace_ids(section, section_id: str) -> None:
    """Prefix every element id in a spliced page with its section id.

    656 pages share one document, so bare per-page ids such as `overview`
    collide. Same-page fragment links are rewritten to match, which is also
    what makes the cross-page rewriting below resolve.
    """
    for el in section.find_all(id=True):
        el["id"] = f"{section_id}-{el['id']}"
    for a in section.find_all("a", href=True):
        # A bare "#" is a placeholder link with no target; namespacing it would
        # manufacture a dangling anchor.
        if a["href"].startswith("#") and a["href"] != "#":
            a["href"] = f"#{section_id}-{a['href'][1:]}"


def resolve_links(section, base_url: str, valid_ids: set) -> None:
    """Turn page-relative URLs into something valid inside the merged document.

    Links to other documented pages become in-PDF anchor jumps. Everything
    else relative - images, downloads, pages outside the nav - is made
    root-absolute, because the merged document is served from /print_page/ and
    would otherwise resolve them against the wrong directory.
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
            a["href"] = absolute

    for el in section.find_all(src=True):
        src = el["src"]
        if src and not src.startswith(("http://", "https://", "data:", "/")):
            el["src"] = urllib.parse.urljoin(base_url, src)


def demote_headings(section, depth: int) -> None:
    """Shift a page's headings down by its nav depth.

    Every page renders its title as <h1>. Left alone, Chrome's PDF outline
    comes out flat; shifting by nav depth makes the outline mirror the
    navigation tree.
    """
    if depth <= 0:
        return
    for h in section.find_all(HEADING_TAGS):
        h.name = f"h{min(6, int(h.name[1]) + depth)}"


def render_cover(config: dict, version: str, generated_at: str) -> str:
    """Fill the cover template's placeholders.

    The template was written for MkDocs and carries three Jinja handles plus
    two spans the build stamps; substituting them directly avoids pulling in a
    template engine for one fragment.
    """
    html = COVER_TEMPLATE.read_text(encoding="utf-8")
    # No template engine runs here, so Jinja comment blocks would otherwise be
    # rendered as visible text on the cover.
    html = re.sub(r"\{#.*?#\}", "", html, flags=re.DOTALL)
    for handle, value in (
        ("{{ config.site_name }}", str(config.get("site_name", ""))),
        ("{{ config.site_url }}", str(config.get("site_url", ""))),
        ("{{ config.copyright | safe }}", str(config.get("copyright", ""))),
    ):
        html = html.replace(handle, value)
    soup = BeautifulSoup(html, "html.parser")
    # The cover lives one directory down once served from /print_page/.
    for img in soup.find_all("img", src=True):
        img["src"] = urllib.parse.urljoin("/print_page/", img["src"])
    for span_id, value in (
        ("print-cover-version", version),
        ("print-cover-date", generated_at),
    ):
        span = soup.find(id=span_id)
        if span is not None:
            span.string = value
    return str(soup)


def assemble_print_page(
    entries: list[NavEntry], config: dict, version: str, generated_at: str
) -> tuple[int, list[str]]:
    """Build the merged document at PRINT_PAGE. Returns (pages, missing)."""
    shell = BeautifulSoup(SHELL_PAGE.read_text(encoding="utf-8"), "html.parser")
    # The shell's own asset URLs are relative to the site root, but the merged
    # document is served one level down.
    for el in shell.find_all(["link", "script", "img"]):
        for attr in ("href", "src"):
            value = el.get(attr)
            if value and value.startswith("./"):
                el[attr] = "/" + value[2:]

    # The theme's skip link targets the shell page's own <h1>, which is
    # replaced below.
    for skip in shell.select("a.md-skip"):
        skip.decompose()

    container = shell.select_one(CONTENT_SELECTOR)
    if container is None:
        raise RuntimeError(f"{SHELL_PAGE} has no {CONTENT_SELECTOR}")
    container.clear()
    container.append(BeautifulSoup(render_cover(config, version, generated_at),
                                   "html.parser"))

    valid_ids = {url_to_section_id(md_to_url_path(e.md)) for e in entries}
    missing: list[str] = []
    count = 0

    for entry in entries:
        built = SITE_DIR / md_to_built_html(entry.md)
        if not built.exists():
            missing.append(entry.md)
            continue
        page = BeautifulSoup(built.read_text(encoding="utf-8"), "html.parser")
        article = page.select_one(CONTENT_SELECTOR)
        if article is None:
            missing.append(entry.md)
            continue

        for selector in NOISE_SELECTORS:
            for el in article.select(selector):
                el.decompose()

        section_id = url_to_section_id(md_to_url_path(entry.md))
        section = shell.new_tag("section")
        section["class"] = "print-page"
        section["id"] = section_id
        for child in list(article.children):
            section.append(child.extract())

        namespace_ids(section, section_id)
        resolve_links(section, md_to_url_path(entry.md), valid_ids)
        demote_headings(section, entry.depth)
        container.append(section)
        count += 1

    PRINT_PAGE.parent.mkdir(parents=True, exist_ok=True)
    PRINT_PAGE.write_text(str(shell), encoding="utf-8")
    return count, missing


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

    if not SHELL_PAGE.exists():
        print(
            f"ERROR: {SHELL_PAGE} not found - run `task build` first.",
            file=sys.stderr,
        )
        return 1
    if not Path(chrome).exists():
        print(f"ERROR: Chrome binary not found at: {chrome}", file=sys.stderr)
        return 1

    entries = load_nav_entries()
    if not entries:
        print(f"ERROR: no pages found in {NAV_YML}", file=sys.stderr)
        return 1
    print(f"Assembling {len(entries)} pages from {NAV_YML}")
    count, missing = assemble_print_page(
        entries, load_site_config(), version, generated_at
    )
    if missing:
        print(
            f"WARNING: {len(missing)} page(s) in nav.yml had no built HTML: "
            + ", ".join(missing[:5])
            + (" ..." if len(missing) > 5 else ""),
            file=sys.stderr,
        )
    print(f"Merged {count} pages into {PRINT_PAGE}")

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
                    "--virtual-time-budget=120000",
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
