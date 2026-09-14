"""Test the PDF builder's navigation walk and HTML normalization"""
from collections import Counter
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

from tools.build_pdf import (
    NavEntry,
    admonitions,
    edition,
    flatten_code_blocks,
    inline_icons,
    merge_pages,
    nav_entries,
    pair_tabs,
    resolve_images,
    settle_internal_links,
)


def soup(markup: str) -> BeautifulSoup:
    return BeautifulSoup(f"<html><body>{markup}</body></html>", "html.parser")


def test_section_opens_with_its_index_page():
    nav = [
        {"Build": [
            {"Build": "build/index.md"},
            {"Rules": ["build/rules/index.md", {"Linking": "build/rules/linking.md"}]},
            {"Spark": "build/spark.md"},
        ]},
    ]
    assert nav_entries(nav) == [
        NavEntry(depth=0, md="build/index.md"),
        NavEntry(depth=1, md="build/rules/index.md"),
        NavEntry(depth=2, md="build/rules/linking.md"),
        NavEntry(depth=1, md="build/spark.md"),
    ]


def test_section_without_index_page_gets_a_heading():
    # The shape of Release Notes in nav.yml: no page stands for the section or
    # its years, so without headings the notes would continue the previous chapter.
    nav = [
        {"Release Notes": [
            {"2026": [{"v26.2.1": ["release-notes/2026/corporate-memory-26-2/index.md"]}]},
        ]},
    ]
    assert nav_entries(nav) == [
        NavEntry(depth=0, title="Release Notes"),
        NavEntry(depth=1, title="2026"),
        NavEntry(depth=2, md="release-notes/2026/corporate-memory-26-2/index.md"),
    ]


def test_page_listed_twice_appears_once_and_links_are_skipped():
    nav = [{"A": ["a/index.md", {"Again": "a/index.md"}, {"Site": "https://example.org/"}]}]
    assert nav_entries(nav) == [NavEntry(depth=0, md="a/index.md")]


def test_merge_breaks_chapters_adds_section_headings_and_drops_web_chrome(tmp_path):
    site = tmp_path / "site"
    (site / "release-notes" / "v1").mkdir(parents=True)
    (site / "release-notes" / "v1" / "index.html").write_text(
        '<html><body><article class="md-content__inner">'
        '<h1 id="v1">Version 1</h1><a class="headerlink" href="#v1">¤</a>'
        '<p>Text</p><h2 id="__comments">Comments</h2><div class="giscus"></div>'
        '</article></body></html>'
    )
    entries = [
        NavEntry(depth=0, title="Release Notes"),
        NavEntry(depth=1, md="release-notes/v1/index.md"),
        NavEntry(depth=1, md="release-notes/v2/index.md"),
    ]
    doc, missing = merge_pages(entries, site, "https://example.org/latest/")
    assert missing == ["release-notes/v2/index.md"]
    assert str(doc.body) == (
        '<body><div class="chapter-break"></div><h1>Release Notes</h1><div class="part-contents"></div>'
        '<section class="print-page" id="release-notes-v1">'
        '<h2 id="release-notes-v1-v1">Version 1</h2><p>Text</p></section></body>'
    )


def test_part_cover_is_the_title_then_the_diagram_the_page_shows_above_it(tmp_path):
    site = tmp_path / "site"
    (site / "build").mkdir(parents=True)
    (site / "build" / "index.html").write_text(
        '<html><body><article class="md-content__inner">'
        '<div class="admonition info inline end"><p><img alt="You are here" src="here.png"/></p></div>'
        '<h1 id="build">Build</h1><p>Intro</p>'
        '</article></body></html>'
    )
    doc, _ = merge_pages([NavEntry(depth=0, md="build/index.md")], site, "https://example.org/latest/")
    assert str(doc.body) == (
        '<body><div class="chapter-break"></div><section class="print-page" id="build">'
        '<h1 id="build-build">Build</h1><p><img alt="You are here" src="/build/here.png"/></p>'
        '<div class="part-contents"></div><p>Intro</p></section></body>'
    )


def test_code_block_is_flattened_keeping_language_and_title():
    doc = soup(
        '<div class="language-shell highlight"><span class="filename">Usage</span>'
        '<pre><span></span><code><a href="#l1" id="l1"></a>'
        '<span class="go">cmemc project list</span>\n</code></pre></div>'
    )
    flatten_code_blocks(doc, Counter())
    wrapper = doc.select_one("div.codeblock")
    assert wrapper["data-title"] == "Usage"
    assert str(wrapper.pre) == '<pre><code class="language-shell">cmemc project list</code></pre>'


def test_terminal_table_carries_its_widest_line_so_it_can_shrink_to_fit():
    doc = soup(
        '<div class="highlight"><pre><code>$ cmemc admin acl list\n'
        '┏━━━━━┳━━━━━━┓\n┃ URI ┃ Name ┃\n</code></pre></div>'
        '<div class="highlight"><pre><code>plain output</code></pre></div>'
    )
    flatten_code_blocks(doc, Counter())
    wrapper = doc.select_one("div.codeblock")
    assert wrapper["data-columns"] == "22"
    assert "data-title" not in wrapper.attrs
    assert doc.body.find_all("pre", recursive=False)[0].get_text() == "plain output"


def test_details_print_as_admonitions_with_a_title_div():
    doc = soup('<details class="info"><summary>Options</summary><p>--raw</p></details>')
    admonitions(doc, Counter())
    div = doc.select_one("div.admonition.info")
    assert div.select_one("div.admonition-title").get_text() == "Options"
    assert div.p.get_text() == "--raw"
    assert doc.find("details") is None


def test_tabs_pair_each_label_with_its_panel():
    doc = soup(
        '<div class="tabbed-set"><input/><div class="tabbed-labels">'
        '<label>Corporate Memory</label><label>cmemc</label></div>'
        '<div class="tabbed-content"><div class="tabbed-block"><p>Click</p></div>'
        '<div class="tabbed-block"><p>Run</p></div></div></div>'
    )
    pair_tabs(doc, Counter())
    tabs = doc.select("div.tabs > div.tab")
    assert [(t["data-label"], t.get_text()) for t in tabs] == [("Corporate Memory", "Click"), ("cmemc", "Run")]


def test_icons_are_dropped_from_headings_and_inlined_elsewhere():
    doc = soup(
        '<h1 id="build"><span class="twemoji"><svg viewbox="0 0 24 24"><path d="M0 0"/></svg></span> Build</h1>'
        '<p><span class="twemoji"><svg viewbox="0 0 24 24"><path d="M0 0"/></svg></span> Search</p>'
    )
    stats = Counter()
    inline_icons(doc, stats)
    assert str(doc.h1) == '<h1 id="build">Build</h1>'
    assert doc.p.img["class"] == ["icon"] and doc.p.img["src"].startswith("data:image/svg+xml;base64,")
    assert stats == Counter({"icons dropped from headings": 1, "icons": 1})


def test_internal_links_target_headings_or_are_unwrapped():
    doc = soup(
        '<section class="print-page" id="build-spark"><h2 id="build-spark-spark">Spark</h2>'
        '<p><a href="#build-spark">page</a> <a href="#build-spark-gone">gone</a> '
        '<span id="build-spark-x">x</span></p></section>'
    )
    settle_internal_links(doc, Counter())
    assert str(doc.body) == (
        '<body><h2 id="build-spark-spark">Spark</h2>'
        '<p><a href="#build-spark-spark">page</a> gone <span>x</span></p></body>'
    )


def test_images_are_embedded_emoji_become_characters_and_badges_alt_text(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    site = Path("site")
    (site / "build").mkdir(parents=True)
    (site / "build" / "shot.png").write_bytes(b"png")
    (site / "build" / "chart.svg").write_text('<svg><foreignObject><div>label</div></foreignObject></svg>')
    doc = soup(
        '<img class="twemoji" alt="😄" src="https://cdn.example/1f604.svg">'
        '<img alt="Python Version" src="https://img.shields.io/badge/python">'
        '<a class="glightbox" href="x"><img alt="Shot" src="/build/shot.png"></a>'
        '<img alt="Chart" src="/build/chart.svg">'
    )
    warnings: list[str] = []
    resolve_images(doc, site, Counter(), warnings)
    assert str(doc.body) == (
        '<body>😄Python Version<img alt="Shot" src="/site/build/shot.png"/>'
        '<img alt="Chart" src="/site/build/chart.svg"/></body>'
    )
    assert warnings == ["SVG text in foreignObject elements does not render, embed a PNG instead: /build/chart.svg"]


def test_edition_reads_copyright_as_plain_text():
    config = {"copyright": 'Copyright &copy; 2026\n<a href="https://eccenca.com">eccenca GmbH</a>'}
    values = edition(config, "26.2", "https://documentation.eccenca.com/26.2/", date(2026, 9, 14), "31b5663")
    assert values["copyright"] == "Copyright © 2026 eccenca GmbH"
    assert values["subtitle"] == "Version 26.2"
    assert values["generated"] == "2026-09-14"
    assert values["commit"] == "31b5663"
