"""Test the preflight report of the print edition (tasks/spec.md, §8; backlog P14)"""
from pypdf import PdfWriter
from pypdf.annotations import Link
from pypdf.generic import (
    ArrayObject,
    DecodedStreamObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NumberObject,
    RectangleObject,
    TextStringObject,
)

from tools.pdf_preflight import (
    area_tints,
    check_annotations,
    check_blank_pages,
    check_fonts,
    check_images,
    check_light_areas,
    check_page_count,
    check_page_numbers,
    check_page_sizes,
    check_pdfx,
    check_soft_masks,
    check_transparency,
    parse_pdffonts,
    parse_pdfimages,
    read_pdf,
    read_transparency,
)

A4 = (595.28, 841.89)

PDFFONTS = """\
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
ABCDEF+Roboto-Light                  CID TrueType      Identity-H       yes yes yes      9  0
Helvetica                            Type 1            Standard         no  no  no      12  0
"""

PDFIMAGES = """\
page   num  type   width height color comp bpc  enc interp  object ID x-ppi y-ppi size ratio
--------------------------------------------------------------------------------------------
   1     0 image    1890   317  rgb     3   8  image  no         9  0   300   300 42.1K 2.3%
   2     1 image     500   300  rgb     3   8  image  no        12  0   150   150 10.0K 2.2%
   2     2 smask     500   300  gray    1   8  image  no        13  0   150   150 1.0K 0.1%
   3     3 image    1890   317  cmyk    4   8  image  no        15  0   301   301 42.1K 2.3%
   4     4 image      49    49  cmyk    4   8  image  no        16  0   294   294  1.0K 2.3%
   4     5 image      40    40  cmyk    4   8  image  no        17  0   250   250  1.0K 2.3%
"""


def test_every_page_count_and_size_problem_is_named():
    assert check_page_count(668, 1200).passed
    assert check_page_count(669, 1200).problems == ["669 pages - a printed book needs an even count"]
    assert check_page_count(1202, 1200).problems == ["1202 pages - more than 1200"]
    assert check_page_sizes([A4, (612.0, 792.0), A4]).problems == ["page 2: 612 x 792 pt, not A4"]


def test_fonts_that_are_not_embedded_fail():
    rows = parse_pdffonts(PDFFONTS)
    assert [row["name"] for row in rows] == ["ABCDEF+Roboto-Light", "Helvetica"]
    assert check_fonts(rows).problems == ["Helvetica (Type 1) is not embedded"]


def test_type3_fonts_fail():
    rows = parse_pdffonts(PDFFONTS + "NotoColorEmoji                       Type 3            Custom           yes no  yes     24  0\n")
    assert check_fonts(rows).problems[-1].startswith("NotoColorEmoji is a Type 3 font")


def test_images_below_300_ppi_and_soft_masks_fail():
    rows = parse_pdfimages(PDFIMAGES)
    assert len(rows) == 6
    # 49 pixels at 294 ppi are one pixel short of 300 - rounding; 40 at 250 are not.
    assert check_images(rows, pdfx=False).problems == ["page 2: image 1 at 150 ppi", "page 4: image 5 at 250 ppi"]
    assert check_soft_masks(rows).problems == ["page 2: soft mask on image 2"]


def test_with_pdfx_images_are_cmyk_or_grey_and_at_most_300_ppi():
    problems = check_images(parse_pdfimages(PDFIMAGES), pdfx=True).problems
    assert "page 1: image 0 in rgb, not CMYK" in problems
    assert "page 3: image 3 at 301 ppi" not in problems  # a pixel of rounding is fine


def test_the_output_intent_must_name_the_condition_the_edition_prints_by(tmp_path):
    writer = PdfWriter()
    writer.add_blank_page(*A4)
    writer.add_metadata({"/GTS_PDFXVersion": "PDF/X-4"})
    intent = DictionaryObject({
        NameObject("/Type"): NameObject("/OutputIntent"),
        NameObject("/S"): NameObject("/GTS_PDFX"),
        NameObject("/OutputConditionIdentifier"): TextStringObject("sGray"),
    })
    writer.root_object[NameObject("/OutputIntents")] = ArrayObject([intent])
    path = tmp_path / "gray.pdf"
    writer.write(path)
    assert check_pdfx(path, "sGray").passed
    assert check_pdfx(path).problems == ["output intent sGray, not FOGRA39"]


def test_transparency_in_page_resources_fails(tmp_path):
    writer = PdfWriter()
    page = writer.add_blank_page(*A4)
    form = DecodedStreamObject()
    form.set_data(b"0 0 1 1 re f")
    form.update({
        NameObject("/Type"): NameObject("/XObject"),
        NameObject("/Subtype"): NameObject("/Form"),
        NameObject("/BBox"): ArrayObject([NumberObject(0), NumberObject(0), NumberObject(1), NumberObject(1)]),
        NameObject("/Group"): DictionaryObject({NameObject("/S"): NameObject("/Transparency")}),
    })
    page[NameObject("/Resources")] = DictionaryObject({
        NameObject("/ExtGState"): DictionaryObject({
            NameObject("/G0"): DictionaryObject({NameObject("/ca"): FloatObject(0.5)}),
            NameObject("/G1"): DictionaryObject({NameObject("/ca"): FloatObject(1)}),
        }),
        NameObject("/XObject"): DictionaryObject({NameObject("/X0"): writer._add_object(form)}),
    })
    writer.add_blank_page(*A4)
    path = tmp_path / "transparent.pdf"
    writer.write(path)
    found = read_transparency(path)
    assert found == {1: {"alpha", "transparency group"}, 2: set()}
    assert check_transparency(found).problems == ["page 1: alpha, transparency group"]


def test_annotations_fail():
    assert check_annotations([0, 2, 0]).problems == ["page 2: 2 annotations"]


def test_page_numbers_sit_on_the_outer_edge():
    words = {
        2: [("2", 60.0, 800.0, 66.0, 812.0)],
        3: [("3", 530.0, 800.0, 536.0, 812.0)],
        4: [("4", 530.0, 800.0, 536.0, 812.0)],
        5: [("Cover", 100.0, 100.0, 150.0, 120.0)],
    }
    check = check_page_numbers(words, {n: A4 for n in words})
    assert check.problems == ["page 4: page number on the inner edge"]


def test_a_blank_page_carries_no_page_furniture():
    words = {
        5: [("5", 530.0, 800.0, 536.0, 812.0), ("Part", 60.0, 800.0, 80.0, 812.0)],
        6: [("Text", 60.0, 100.0, 90.0, 112.0), ("6", 60.0, 800.0, 66.0, 812.0)],
        7: [("7", 530.0, 800.0, 536.0, 812.0)],
    }
    painted = {5: False, 6: False, 7: True}
    check = check_blank_pages(words, {n: A4 for n in words}, painted)
    assert check.problems == ["page 5: only page furniture"]


def test_light_area_fills_are_found_and_text_is_ignored():
    content = (
        b"q 0.95 g 0 0 10 10 re f Q 0.5 g 0 0 5 5 re f 1 1 1 rg 0 0 1 1 re f "
        b"/Cs1 cs 0.9 0.9 0.9 scn 0 0 2 2 re f BT /F1 9 Tf (0.95 g 0 0 1 1 re f) Tj ET "
        b"0 0 0 0.1 k 0 0 3 3 re f*"
    )
    tints, painted = area_tints(content)
    assert tints == {0.05, 0.1}
    assert painted
    assert area_tints(b"BT /F1 10 Tf (hello) Tj ET") == (set(), False)
    assert area_tints(b"0.8 g 0 0 1 1 re f 0.8 0.8 0.8 rg 0 0 1 1 re f") == (set(), True)  # exactly 20 %
    check = check_light_areas({3: {0.05}, 4: set(), 7: {0.05, 0.1}})
    assert check.level == "warning"
    assert check.problems == ["5 % black on pages 3, 7", "10 % black on page 7"]


def test_the_pdf_is_read_page_by_page(tmp_path):
    writer = PdfWriter()
    writer.add_blank_page(*A4)
    writer.add_blank_page(612, 792)
    writer.add_annotation(1, Link(rect=RectangleObject((10, 10, 20, 20)), target_page_index=0))
    path = tmp_path / "book.pdf"
    writer.write(path)
    sizes, annotations, contents = read_pdf(path)
    assert [tuple(round(value) for value in size) for size in sizes] == [(595, 842), (612, 792)]
    assert annotations == [0, 1]
    assert len(contents) == 2
