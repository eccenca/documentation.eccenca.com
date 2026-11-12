"""Test what the print edition renders as images for Ghostscript: colour emoji and transparent SVGs (backlog P13)"""
import base64
import shutil
from collections import Counter
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from PIL import Image

from tools.build_pdf import (
    EMOJI_FONT,
    TEXT_FONT,
    emoji_images,
    emoji_pattern,
    font_codepoints,
    rasterize_transparent_svgs,
    render_emoji,
    typst_png,
)


def test_the_cmaps_of_the_vendored_fonts_are_read():
    emoji = font_codepoints(EMOJI_FONT)
    text = font_codepoints(TEXT_FONT)
    assert {0x26A0, 0x1F604, 0x1F1E9} <= emoji
    assert {ord("A"), ord("é"), ord("€")} <= text
    assert 0x1F604 not in text


def test_emoji_sequences_are_found_whole_and_text_is_left_alone():
    pattern = emoji_pattern()
    text = "Warn ⚠️, wave 👋🏽, coder 👩‍💻, flag 🇩🇪, smile 😄 - plain text, 42 € and é."
    assert pattern.findall(text) == ["⚠️", "👋🏽", "👩‍💻", "🇩🇪", "😄"]


def test_emoji_of_text_and_code_are_rendered_longest_first(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    html = '<p>Warn ⚠️ now 😄</p><pre><code>🎤 Type of package</code></pre><script>let s = "✨";</script>'
    doc = BeautifulSoup(html, "html.parser")
    rendered = []

    def fake_render(sequences, targets, typst):
        rendered.append(list(sequences))
        assert [target.name for target in targets] == ["26a0-fe0f.png", "1f3a4.png", "1f604.png"]

    stats = Counter()
    pairs = emoji_images(doc, Path("emoji"), "typst", stats, render=fake_render)
    assert rendered == [["⚠️", "🎤", "😄"]]
    assert pairs == [["⚠️", "/emoji/26a0-fe0f.png"], ["🎤", "/emoji/1f3a4.png"], ["😄", "/emoji/1f604.png"]]
    assert str(doc) == html  # the style swaps them; the document keeps its text
    assert stats["emoji rendered as images"] == 3
    assert emoji_images(BeautifulSoup("<p>No emoji here, 42 €.</p>", "html.parser"), Path("emoji"), "typst", stats) == []


def svg_uri(markup):
    return "data:image/svg+xml;base64," + base64.b64encode(markup.encode()).decode()


def test_svgs_that_draw_with_transparency_become_png(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "site").mkdir()
    (tmp_path / "site/masked.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><mask id="m"/></svg>')
    (tmp_path / "site/plain.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><rect/></svg>')
    translucent = svg_uri('<svg xmlns="http://www.w3.org/2000/svg"><path opacity=".5"/></svg>')
    solid = svg_uri('<svg xmlns="http://www.w3.org/2000/svg"><path/></svg>')
    doc = BeautifulSoup(
        f'<img src="/site/masked.svg"/><img src="/site/plain.svg"/>'
        f'<img class="icon" src="{translucent}"/><img class="icon" src="{solid}"/><img src="/site/shot.png"/>',
        "html.parser",
    )
    calls = []

    def fake_render(pages, targets, typst, preamble, what):
        calls.append((pages, [target.parent.name for target in targets]))

    stats = Counter()
    rasterize_transparent_svgs(doc, Path("svg"), "typst", stats, render=fake_render)
    sources = [img["src"] for img in doc.find_all("img")]
    assert sources[0].startswith("/svg/masked-") and sources[0].endswith(".png")
    assert sources[1] == "/site/plain.svg"
    assert sources[2].startswith("/svg/") and sources[2].endswith(".png")
    assert sources[3] == solid
    assert sources[4] == "/site/shot.png"
    pages, directories = calls[0]
    assert len(pages) == 2 and '#image("/site/masked.svg")' in pages and directories == ["svg", "svg"]
    assert stats["SVG images with transparency rendered as PNG"] == 2


@pytest.mark.skipif(shutil.which("typst") is None, reason="Typst is not installed")
def test_typst_renders_an_emoji_and_an_svg_on_white(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    emoji = Path("out/26a0-fe0f.png")
    render_emoji(["⚠️"], [emoji], "typst")
    with Image.open(emoji) as image:
        assert image.mode == "RGB"
        # 10 pt from ascender to descender, 1.172 em, at 600 ppi.
        assert abs(image.height - 98) <= 2
        assert image.convert("L").getextrema()[0] < 128
    Path("icon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="72" height="36">'
        '<rect width="72" height="36" fill="black" opacity="0.5"/></svg>'
    )
    svg = Path("out/icon.png")
    typst_png(['#image("/icon.svg")'], [svg], "typst", "", "typst (SVG)")
    with Image.open(svg) as image:
        assert image.mode == "RGB"
        assert abs(image.width - 450) <= 2  # 72 CSS px are 54 pt, at 600 ppi
        assert 100 < image.convert("L").getpixel((225, 112)) < 160  # half black on white
    assert not list(Path("out").glob("page-*.png"))
