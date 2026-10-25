"""Test the print edition's image copies: on white, at 300 ppi at the printed width"""
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

from tools.build_pdf import print_image, resolve_images


def make(path: Path, size: tuple[int, int], dpi: tuple[int, int] | None = None) -> None:
    image = Image.new("RGB", size, (0, 0, 255))
    image.save(path, **({"dpi": dpi} if dpi else {}))


def test_a_wide_screenshot_prints_at_the_text_width_with_300_ppi(tmp_path):
    source = tmp_path / "wide.png"
    make(source, (4000, 1000))
    with Image.open(print_image(source, None, tmp_path / "cache")) as copy:
        # 16 cm are 453.54 pt, which at 300 ppi take 1890 pixels.
        assert copy.size == (1890, 472)
        assert round(copy.info["dpi"][0]) == 300


def test_a_small_screenshot_keeps_its_printed_size_and_gains_pixels(tmp_path):
    source = tmp_path / "small.png"
    make(source, (300, 100), dpi=(144, 144))
    with Image.open(print_image(source, None, tmp_path / "cache")) as copy:
        # At 144 dpi it prints 150 pt wide, which at 300 ppi take 625 pixels.
        assert copy.size == (625, 208)
        assert round(copy.info["dpi"][0]) == 300


def test_a_percentage_width_is_that_share_of_the_text_width(tmp_path):
    source = tmp_path / "half.png"
    make(source, (2000, 1000))
    with Image.open(print_image(source, "50%", tmp_path / "cache")) as copy:
        assert copy.width == 945


def test_transparency_is_flattened_onto_white(tmp_path):
    source = tmp_path / "alpha.png"
    image = Image.new("RGBA", (200, 100), (0, 0, 0, 0))
    image.putpixel((0, 0), (255, 0, 0, 255))
    image.save(source)
    with Image.open(print_image(source, None, tmp_path / "cache")) as copy:
        assert copy.mode == "RGB"
        assert copy.getpixel((copy.width - 1, copy.height - 1)) == (255, 255, 255)


def test_a_gif_becomes_a_png_of_its_first_frame(tmp_path):
    source = tmp_path / "animation.gif"
    frames = [Image.new("P", (100, 50), index) for index in (1, 2)]
    frames[0].save(source, save_all=True, append_images=frames[1:])
    copy = print_image(source, None, tmp_path / "cache")
    assert copy.suffix == ".png"
    with Image.open(copy) as image:
        assert image.mode == "RGB"


def test_the_copy_is_reused_while_the_image_and_its_width_stay_the_same(tmp_path):
    source = tmp_path / "shot.png"
    make(source, (900, 300))
    first = print_image(source, None, tmp_path / "cache")
    written = first.stat().st_mtime_ns
    assert print_image(source, None, tmp_path / "cache") == first
    assert first.stat().st_mtime_ns == written
    assert print_image(source, "50%", tmp_path / "cache") != first


def test_print_images_point_at_their_copies_and_vector_images_stay(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    site = Path("site")
    (site / "build").mkdir(parents=True)
    make(site / "build" / "shot.png", (900, 300))
    (site / "build" / "chart.svg").write_text("<svg/>")
    doc = BeautifulSoup('<img alt="Shot" src="/build/shot.png"/><img alt="Chart" src="/build/chart.svg"/>', "html.parser")
    stats: Counter = Counter()
    resolve_images(doc, site, stats, [], Path("dist/pdf/print/images"))
    shot, chart = doc.find_all("img")
    assert shot["src"].startswith("/dist/pdf/print/images/") and shot["src"].endswith(".png")
    assert chart["src"] == "/site/build/chart.svg"
    assert stats["images normalized for print"] == 1
