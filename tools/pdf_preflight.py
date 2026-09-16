"""Check the book block of the print edition before it goes to print (tasks/spec.md, §8; backlog P14).

The checks are what BoD rejects or prints badly: pages that are not A4, an odd
page count or too many pages, fonts that are not embedded, images below 300 ppi,
soft masks, annotations, page numbers on the inner edge, page furniture on blank
pages, and - as a warning - grey areas lighter than 20 % black. With `--pdfx`
the file must also declare PDF/X-4 with a FOGRA39 output intent and hold only
CMYK or grey images of at most 300 ppi.

The page data comes from pypdf and from poppler's pdffonts, pdfimages and
pdftotext.
"""
from __future__ import annotations

import html
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import click
from pypdf import PdfReader

from tools.pdf_normalize import is_pdfx4

A4 = (595.28, 841.89)
# The output intent of the book block; the greyscale preview names its grey profile instead.
FOGRA39 = "FOGRA39"
SIZE_TOLERANCE = 1.0
MAX_PAGES = 1200
MIN_PPI = 300
# pdfimages rounds densities to whole pixels.
PPI_TOLERANCE = 1
MIN_AREA_BLACK = 0.20
# The share of the page height below which the footer sits.
FOOTER_BAND = 0.9
# The operators that paint an area, and those that paint anything else.
AREA_PAINTING = {b"f", b"F", b"f*", b"B", b"B*", b"b", b"b*"}
OTHER_PAINTING = {b"S", b"s", b"Do", b"sh", b"BI"}
TOKEN = re.compile(
    rb"\((?:\\.|[^\\()])*\)"          # a literal string
    rb"|<<|>>|<[0-9A-Fa-f\s]*>"       # dictionary delimiters and hex strings
    rb"|\[|\]"
    rb"|/[^\s/\[\]()<>{}%]*"          # a name
    rb"|[-+]?(?:\d+\.?\d*|\.\d+)"     # a number
    rb"|[A-Za-z'\"*]+"                # an operator
)
WORD = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>')


@dataclass
class Check:
    """One preflight check: its findings, and whether they are errors or warnings."""

    name: str
    problems: list[str] = field(default_factory=list)
    level: str = "error"

    @property
    def passed(self) -> bool:
        return not self.problems


def check_page_count(count: int, max_pages: int = MAX_PAGES) -> Check:
    check = Check("even page count within the limit")
    if count % 2:
        check.problems.append(f"{count} pages - a printed book needs an even count")
    if count > max_pages:
        check.problems.append(f"{count} pages - more than {max_pages}")
    return check


def check_page_sizes(sizes: list[tuple[float, float]]) -> Check:
    check = Check("A4 pages")
    for number, (width, height) in enumerate(sizes, 1):
        if abs(width - A4[0]) > SIZE_TOLERANCE or abs(height - A4[1]) > SIZE_TOLERANCE:
            check.problems.append(f"page {number}: {width:g} x {height:g} pt, not A4")
    return check


def parse_pdffonts(text: str) -> list[dict]:
    """The rows of `pdffonts`: name, type, encoding and whether the font is embedded."""
    rows = []
    for line in text.splitlines()[2:]:
        tokens = line.split()
        if len(tokens) < 7:
            continue
        # The name is one token, the type may be several, the last six are fixed columns.
        rows.append({
            "name": tokens[0],
            "type": " ".join(tokens[1:-6]),
            "encoding": tokens[-6],
            "emb": tokens[-5],
        })
    return rows


def check_fonts(rows: list[dict]) -> Check:
    """Fonts are embedded, and none is a Type 3 font.

    Typst writes colour emoji as a Type 3 font whose glyphs carry shadings and
    soft masks - transparency, and content Ghostscript 10.08 drops or crashes on
    when it converts to CMYK. The print build renders them as images instead.
    """
    check = Check("fonts embedded, no Type 3 fonts")
    for row in rows:
        if row["emb"] != "yes":
            check.problems.append(f"{row['name']} ({row['type']}) is not embedded")
        if row["type"] == "Type 3":
            check.problems.append(f"{row['name']} is a Type 3 font - colour glyphs the print build did not render as images")
    return check


def parse_pdfimages(text: str) -> list[dict]:
    """The rows of `pdfimages -list`."""
    rows = []
    for line in text.splitlines():
        tokens = line.split()
        if len(tokens) != 16 or not tokens[0].isdigit():
            continue

        def number(value: str) -> int:
            return int(value) if value.isdigit() else 0

        rows.append({
            "page": int(tokens[0]),
            "num": int(tokens[1]),
            "type": tokens[2],
            "width": number(tokens[3]),
            "height": number(tokens[4]),
            "color": tokens[5],
            "x_ppi": number(tokens[12]),
            "y_ppi": number(tokens[13]),
        })
    return rows


def check_images(rows: list[dict], pdfx: bool = False) -> Check:
    check = Check("images at 300 ppi" + (", CMYK and at most 300 ppi" if pdfx else ""))
    for row in rows:
        if row["type"] != "image":
            continue
        ppi = min(row["x_ppi"], row["y_ppi"])
        # A small image is a whole pixel away from any density: 49 pixels across an
        # emoji are 294 ppi where 50 would be 300. Ghostscript's downsampling rounds
        # to whole pixels, so one pixel either way passes.
        pixels = max(1, min(row["width"], row["height"]))
        where = f"page {row['page']}: image {row['num']}"
        if ppi and ppi * (pixels + 1) / pixels < MIN_PPI - PPI_TOLERANCE:
            check.problems.append(f"{where} at {ppi} ppi")
        if pdfx and row["color"] not in ("cmyk", "gray"):
            check.problems.append(f"{where} in {row['color']}, not CMYK")
        if pdfx and pixels > 1 and ppi * (pixels - 1) / pixels > MIN_PPI + PPI_TOLERANCE:
            check.problems.append(f"{where} at {ppi} ppi")
    return check


def check_soft_masks(rows: list[dict]) -> Check:
    check = Check("no soft masks")
    for row in rows:
        if row["type"] == "smask":
            check.problems.append(f"page {row['page']}: soft mask on image {row['num']}")
    return check


def resource_transparency(resources, found: set[str], depth: int = 0) -> None:
    """Collect the transparency a page's resources draw with, down through forms, patterns and Type 3 fonts."""
    if resources is None or depth > 8:
        return
    resources = resources.get_object()
    for state in resources.get("/ExtGState", {}).values():
        state = state.get_object()
        if state.get("/SMask", "/None") != "/None":
            found.add("soft mask")
        if float(state.get("/ca", 1)) < 1 or float(state.get("/CA", 1)) < 1:
            found.add("alpha")
    for xobject in resources.get("/XObject", {}).values():
        xobject = xobject.get_object()
        if xobject.get("/Subtype") == "/Form":
            if "/Group" in xobject:
                found.add("transparency group")
            resource_transparency(xobject.get("/Resources"), found, depth + 1)
    for pattern in resources.get("/Pattern", {}).values():
        resource_transparency(pattern.get_object().get("/Resources"), found, depth + 1)
    for font in resources.get("/Font", {}).values():
        font = font.get_object()
        if font.get("/Subtype") == "/Type3":
            resource_transparency(font.get("/Resources"), found, depth + 1)


def read_transparency(path: Path) -> dict[int, set[str]]:
    """The kinds of transparency each page draws with, by page number."""
    found: dict[int, set[str]] = {}
    for number, page in enumerate(PdfReader(path).pages, 1):
        found[number] = set()
        resource_transparency(page.get("/Resources"), found[number])
    return found


def check_transparency(found: dict[int, set[str]]) -> Check:
    """No transparency: BoD asks for none, and Ghostscript draws it incompletely when it writes PDF/X-4."""
    check = Check("no transparency")
    for number, kinds in sorted(found.items()):
        if kinds:
            check.problems.append(f"page {number}: {', '.join(sorted(kinds))}")
    return check


def check_annotations(counts: list[int]) -> Check:
    check = Check("no annotations")
    for number, count in enumerate(counts, 1):
        if count:
            check.problems.append(f"page {number}: {count} annotations")
    return check


def check_pdfx(path: Path, condition: str = FOGRA39) -> Check:
    """PDF/X-4 with the output intent the edition prints by: FOGRA39 for the book block in CMYK,
    the grey profile's condition for the greyscale preview."""
    check = Check(f"PDF/X-4 with a {condition} output intent")
    if not is_pdfx4(path):
        check.problems.append("no PDF/X-4 marker or no output intent")
        return check
    intents = PdfReader(path).trailer["/Root"]["/OutputIntents"]
    identifiers = [str(intent.get_object().get("/OutputConditionIdentifier", "")) for intent in intents]
    if not any(condition in identifier for identifier in identifiers):
        check.problems.append(f"output intent {', '.join(identifiers) or 'without an identifier'}, not {condition}")
    return check


def check_page_numbers(words: dict[int, list[tuple]], sizes: dict[int, tuple[float, float]]) -> Check:
    """A page number sits at the outer edge: left on an even page, right on an odd one."""
    check = Check("page numbers on the outer edge")
    for number, page_words in sorted(words.items()):
        width, height = sizes[number]
        folios = [word for word in page_words if word[0] == str(number) and word[2] > height * FOOTER_BAND]
        if not folios:
            continue
        _, x_min, _, x_max, _ = folios[-1]
        outer = x_max < width / 2 if number % 2 == 0 else x_min > width / 2
        if not outer:
            check.problems.append(f"page {number}: page number on the inner edge")
    return check


def check_blank_pages(
    words: dict[int, list[tuple]], sizes: dict[int, tuple[float, float]], painted: dict[int, bool]
) -> Check:
    """A page with nothing on it but its footer is a blank page that still carries page furniture."""
    check = Check("blank pages carry no page furniture")
    for number, page_words in sorted(words.items()):
        _, height = sizes[number]
        if page_words and not painted.get(number, False) and all(word[2] > height * FOOTER_BAND for word in page_words):
            check.problems.append(f"page {number}: only page furniture")
    return check


def area_tints(content: bytes) -> tuple[set[float], bool]:
    """The tints lighter than 20 % black that a page's content fills areas with, and whether it paints at all.

    Follows the fill colour through the colour operators and the graphics state;
    text in string literals is skipped.
    """
    operands: list[float] = []
    tint = 1.0
    saved: list[float] = []
    light: set[float] = set()
    painted = False

    def black(values: list[float]) -> float:
        if len(values) == 1:
            return 1 - values[0]
        if len(values) == 3:
            red, green, blue = values
            return 1 - (0.299 * red + 0.587 * green + 0.114 * blue)
        cyan, magenta, yellow, key = values
        return 1 - (1 - key) * (1 - (0.3 * cyan + 0.59 * magenta + 0.11 * yellow))

    for match in TOKEN.finditer(content):
        token = match.group(0)
        head = token[:1]
        if head in b"-+.0123456789":
            try:
                operands.append(float(token))
                continue
            except ValueError:
                pass
        if head in b"(<[]/" or token == b">>":
            continue
        if token == b"q":
            saved.append(tint)
        elif token == b"Q":
            tint = saved.pop() if saved else 1.0
        elif token == b"g" and operands:
            tint = black(operands[-1:])
        elif token == b"rg" and len(operands) >= 3:
            tint = black(operands[-3:])
        elif token == b"k" and len(operands) >= 4:
            tint = black(operands[-4:])
        elif token in (b"sc", b"scn") and len(operands) in (1, 3, 4):
            tint = black(operands)
        elif token == b"cs":
            tint = 1.0
        elif token in AREA_PAINTING:
            painted = True
            # 0.8 g is 20 % black, 0.19999... in floating point.
            if 0.005 < tint < MIN_AREA_BLACK - 0.005:
                light.add(round(tint, 2))
        elif token in OTHER_PAINTING:
            painted = True
        operands = []
    return light, painted


def check_light_areas(tints: dict[int, set[float]]) -> Check:
    """Grey areas lighter than 20 % black print unevenly - a warning, as artwork and emoji carry them too."""
    pages_by_tint: dict[float, list[int]] = {}
    for number, page_tints in sorted(tints.items()):
        for tint in page_tints:
            pages_by_tint.setdefault(tint, []).append(number)
    check = Check("grey areas at least 20 % black", level="warning")
    for tint, pages in sorted(pages_by_tint.items()):
        label = "page" if len(pages) == 1 else "pages"
        shown = ", ".join(str(page) for page in pages[:8])
        more = f" and {len(pages) - 8} more" if len(pages) > 8 else ""
        check.problems.append(f"{round(tint * 100):g} % black on {label} {shown}{more}")
    return check


def read_pdf(path: Path) -> tuple[list[tuple[float, float]], list[int], list[bytes]]:
    """Each page's size, number of annotations and decoded content."""
    reader = PdfReader(path)
    sizes, annotations, contents = [], [], []
    for page in reader.pages:
        box = page.mediabox
        sizes.append((float(box.width), float(box.height)))
        annots = page.get("/Annots")
        annotations.append(len(annots.get_object()) if annots else 0)
        content = page.get_contents()
        contents.append(content.get_data() if content is not None else b"")
    return sizes, annotations, contents


def tool_output(*command: str) -> str:
    if shutil.which(command[0]) is None:
        raise click.ClickException(f"{command[0]} not found - install poppler")
    return subprocess.run(command, capture_output=True, text=True, check=False).stdout


def page_words(path: Path) -> dict[int, list[tuple]]:
    """The words of each page with their boxes, from `pdftotext -bbox`."""
    words: dict[int, list[tuple]] = {}
    for number, page in enumerate(tool_output("pdftotext", "-bbox", str(path), "-").split("<page ")[1:], 1):
        words[number] = [
            (html.unescape(text), float(x_min), float(y_min), float(x_max), float(y_max))
            for x_min, y_min, x_max, y_max, text in WORD.findall(page)
        ]
    return words


def run_preflight(
    path: Path, pdfx: bool = False, max_pages: int = MAX_PAGES, condition: str = FOGRA39
) -> list[Check]:
    """All checks of a PDF."""
    sizes, annotations, contents = read_pdf(path)
    size_map = dict(enumerate(sizes, 1))
    tints: dict[int, set[float]] = {}
    painted: dict[int, bool] = {}
    for number, content in enumerate(contents, 1):
        tints[number], painted[number] = area_tints(content)
    images = parse_pdfimages(tool_output("pdfimages", "-list", str(path)))
    words = page_words(path)
    checks = [
        check_page_count(len(sizes), max_pages),
        check_page_sizes(sizes),
        check_fonts(parse_pdffonts(tool_output("pdffonts", str(path)))),
        check_images(images, pdfx),
        check_soft_masks(images),
        check_transparency(read_transparency(path)),
        check_annotations(annotations),
        check_page_numbers(words, size_map),
        check_blank_pages(words, size_map, painted),
    ]
    if pdfx:
        # Grey areas are judged before the conversion: a neutral grey in CMYK
        # mixes all four inks, which the tint estimate reads as lighter than it prints.
        checks.append(check_pdfx(path, condition))
    else:
        checks.append(check_light_areas(tints))
    return checks


def print_report(path: Path, checks: list[Check], shown: int = 10) -> bool:
    """Print the checks with their findings. Returns whether no check found an error."""
    print(f"Preflight of {path}:")
    for check in checks:
        status = "ok" if check.passed else ("WARNING" if check.level == "warning" else "FAILED")
        count = "" if check.passed else f" - {len(check.problems)}"
        print(f"  {status:<8} {check.name}{count}")
        for problem in check.problems[:shown]:
            print(f"           {problem}")
        if len(check.problems) > shown:
            print(f"           ... and {len(check.problems) - shown} more")
    return all(check.passed or check.level == "warning" for check in checks)


@click.command(name="pdf-preflight")
@click.argument("pdf", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--pdfx",
    is_flag=True,
    help="Also require PDF/X-4: the marker, a FOGRA39 output intent, CMYK images. Grey areas are not judged in CMYK.",
)
@click.option("--max-pages", type=int, default=MAX_PAGES, show_default=True, help="How many pages may the book have?")
@click.option(
    "--intent",
    default=FOGRA39,
    show_default=True,
    help="Which output condition must the PDF/X-4 intent name? The greyscale preview names its grey profile.",
)
def pdf_preflight(pdf: Path, pdfx: bool, max_pages: int, intent: str) -> None:
    """Check the book block of the print edition before it goes to print."""
    if not print_report(pdf, run_preflight(pdf, pdfx, max_pages, intent)):
        raise click.ClickException(f"preflight found errors in {pdf}")
