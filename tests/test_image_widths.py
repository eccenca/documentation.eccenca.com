"""Test the screenshot widths written into the Markdown sources (tasks/spec.md, §11, D18)"""
import pytest
from PIL import Image

from tools.image_widths import add_widths, capture_scale, width_percent


@pytest.mark.parametrize(
    "dpi, scale",
    [(None, 1.0), (72, 1.0), (96, 1.0), (120, 1.25), (144, 2.0), (192, 2.0)],
)
def test_the_capture_scale_follows_the_declared_density(dpi, scale):
    assert capture_scale(dpi) == scale


@pytest.mark.parametrize(
    "pixels, dpi, percent",
    [
        (605, None, 100),   # the full page width at scale 1
        (300, None, 50),    # 49.6 % rounds to 50
        (1210, 144, 100),   # a Retina capture: 605 CSS pixels
        (400, 144, 35),     # 200 CSS pixels: 33 % rounds to 35
        (480, 120, 65),     # 384 CSS pixels: 63.5 % rounds to 65
        (20, None, 5),      # never below 5 %
        (2000, None, 100),  # never above 100 %
    ],
)
def test_the_width_is_the_natural_width_as_a_share_of_the_full_page(pixels, dpi, percent):
    assert width_percent(pixels, dpi) == percent


def picture(path, width, dpi=None):
    image = Image.new("RGB", (width, 10), "white")
    if dpi:
        image.save(path, dpi=(dpi, dpi))
    else:
        image.save(path)


def test_images_without_a_width_get_one_and_the_rest_stay_as_they_are(tmp_path):
    picture(tmp_path / "plain.png", 300)
    picture(tmp_path / "framed.png", 600, dpi=144)
    picture(tmp_path / "sized.png", 300)
    picture(tmp_path / "titled.png", 400)
    picture(tmp_path / "wide.png", 1500)
    picture(tmp_path / "coded.png", 300)
    (tmp_path / "diagram.svg").write_text("<svg/>")
    text = (
        "# Page\n\n"
        "![Plain](plain.png)\n\n"
        '![Framed](framed.png){ class="bordered" }\n\n'
        '![Sized](sized.png){ class="bordered" width="70%" }\n\n'
        '![Titled](titled.png "A title")\n\n'
        "![Wide](wide.png)\n\n"
        "![Remote](https://example.org/remote.png)\n\n"
        "![Vector](diagram.svg)\n\n"
        "![Missing](gone.png)\n\n"
        "```markdown\n![Coded](coded.png)\n```\n"
    )
    result, changes = add_widths(text, tmp_path)
    # A full-width image gets no width: it fills the column in print either way.
    assert result == (
        "# Page\n\n"
        '![Plain](plain.png){ width="50%" }\n\n'
        '![Framed](framed.png){ class="bordered" width="50%" }\n\n'
        '![Sized](sized.png){ class="bordered" width="70%" }\n\n'
        '![Titled](titled.png "A title"){ width="65%" }\n\n'
        "![Wide](wide.png)\n\n"
        "![Remote](https://example.org/remote.png)\n\n"
        "![Vector](diagram.svg)\n\n"
        "![Missing](gone.png)\n\n"
        "```markdown\n![Coded](coded.png)\n```\n"
    )
    assert changes == [("plain.png", 50), ("framed.png", 50), ("titled.png", 65)]


def test_a_page_whose_images_all_have_widths_is_unchanged(tmp_path):
    picture(tmp_path / "sized.png", 300)
    text = '![Sized](sized.png){ width="40%" }\n'
    assert add_widths(text, tmp_path) == (text, [])
