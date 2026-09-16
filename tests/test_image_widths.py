"""Test the screenshot widths written into the Markdown sources (tasks/spec.md, §11, D18; backlog P24)"""
import pytest
from PIL import Image

from tools.image_widths import TARGET_PPI, fit_widths, printed_density, target_width


@pytest.mark.parametrize(
    "pixels, percent, ppi",
    [
        (945, 100, 150),   # the 16 cm column is 6.3 inches
        (472, 50, 150),    # half the column, half the pixels
        (945, 50, 300),    # the same image at half the width prints twice as sharp
        (300, 100, 48),
    ],
)
def test_the_density_follows_from_the_width_on_the_page(pixels, percent, ppi):
    assert printed_density(pixels, percent) == ppi


@pytest.mark.parametrize(
    "pixels, percent, width",
    [
        (472, 100, 50),    # 75 ppi at the full column: half of it reaches the target exactly
        (472, 50, 50),     # the declared width cancels out - the pixels decide
        (904, 100, 95),    # 144 ppi: floor gives 96 %, which still measures 149
        (282, 50, 29),     # 90 ppi at half the column
        (150, 20, 15),     # a thumbnail keeps shrinking
    ],
)
def test_the_width_brings_the_image_to_the_target_density(pixels, percent, width):
    assert target_width(pixels, percent) == width
    assert printed_density(pixels, width) >= TARGET_PPI


def test_an_image_too_small_for_the_target_keeps_the_smallest_width():
    assert target_width(9, 100) == 1
    assert printed_density(9, 1) < TARGET_PPI


def picture(path, width):
    Image.new("RGB", (width, 10), "white").save(path)


def test_images_that_print_too_coarse_are_narrowed_and_the_rest_stay_as_they_are(tmp_path):
    picture(tmp_path / "plain.png", 472)
    picture(tmp_path / "framed.png", 472)
    picture(tmp_path / "quoted.png", 282)
    picture(tmp_path / "unquoted.png", 282)
    picture(tmp_path / "sharp.png", 1200)
    picture(tmp_path / "titled.png", 472)
    picture(tmp_path / "coded.png", 300)
    (tmp_path / "diagram.svg").write_text("<svg/>")
    text = (
        "# Page\n\n"
        "![Plain](plain.png)\n\n"
        '![Framed](framed.png){ class="bordered" }\n\n'
        '![Quoted](quoted.png){ class="bordered" width="50%" }\n\n'
        "![Unquoted](unquoted.png){ width=50% }\n\n"
        "![Sharp](sharp.png)\n\n"
        '![Titled](titled.png "A title")\n\n'
        "![Remote](https://example.org/remote.png)\n\n"
        "![Vector](diagram.svg)\n\n"
        "![Missing](gone.png)\n\n"
        "```markdown\n![Coded](coded.png)\n```\n"
    )
    result, changes = fit_widths(text, tmp_path)
    assert result == (
        "# Page\n\n"
        '![Plain](plain.png){ width="50%" }\n\n'
        '![Framed](framed.png){ class="bordered" width="50%" }\n\n'
        '![Quoted](quoted.png){ class="bordered" width="29%" }\n\n'
        '![Unquoted](unquoted.png){ width="29%" }\n\n'
        "![Sharp](sharp.png)\n\n"
        '![Titled](titled.png "A title"){ width="50%" }\n\n'
        "![Remote](https://example.org/remote.png)\n\n"
        "![Vector](diagram.svg)\n\n"
        "![Missing](gone.png)\n\n"
        "```markdown\n![Coded](coded.png)\n```\n"
    )
    assert [(source, percent, width) for source, percent, width, _, _ in changes] == [
        ("plain.png", 100, 50),
        ("framed.png", 100, 50),
        ("quoted.png", 50, 29),
        ("unquoted.png", 50, 29),
        ("titled.png", 100, 50),
    ]


def test_a_page_whose_images_print_sharply_is_unchanged(tmp_path):
    picture(tmp_path / "sized.png", 472)
    text = '![Sized](sized.png){ width="40%" }\n'
    assert fit_widths(text, tmp_path) == (text, [])
