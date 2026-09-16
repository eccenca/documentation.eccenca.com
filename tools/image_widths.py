"""Size raster images in the Markdown sources so they print sharply.

An image prints as many pixels per inch as its width on the page allows: a
screenshot of 900 pixels across the full 16 cm column prints at 143 ppi, the
same screenshot at half the column at 286 ppi. `dec-tool image-widths` writes
the `{ width="NN%" }` that brings an image to at least 150 ppi - the density
below which the print edition lists it as too coarse (tasks/spec.md, §11, and
backlog P24).

The width follows from the pixels alone: `pixels / (16 cm in inches * 150)`,
rounded down, because the declared width cancels out of
`declared * density / target`. It is rounded down to a whole percent, so the
result never falls short of the target, and an image already at 150 ppi or more
keeps the width it has.

The same width serves the site, where the image then takes the share of the
article it fills on paper. Generated pages are left alone: their generators own
them.

Without `--fix` the command lists what prints too coarse and fails, so a check
can catch a new screenshot; with `--fix` it writes the widths.
"""
from __future__ import annotations

import math
import re
import urllib.parse
from pathlib import Path

import click
from PIL import Image, UnidentifiedImageError

DOCS_DIR = Path("docs")
# The text column of the print edition, the width an image at 100 % fills.
COLUMN_INCHES = 16 / 2.54
TARGET_PPI = 150
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
# The marker a generated page carries (.claude/docs-guidelines/repo-conventions.md).
GENERATED_MARK = re.compile(r"generated - do not change it manually|auto-generated", re.IGNORECASE)
# A Markdown image, with an optional title, and the attribute list that may follow it.
IMAGE = re.compile(r'!\[[^\]]*\]\((?P<src>[^)\s]+)(?:\s+"[^"]*")?\)(?P<attrs>\{[^}\n]*\})?')
# A width attribute, quoted or not: both spellings occur in the sources.
WIDTH = re.compile(r"""width\s*=\s*["']?(?P<percent>\d+)%["']?""")
FENCE = re.compile(r"^\s*(```|~~~)")


def printed_density(pixels: int, percent: int) -> int:
    """How many pixels per inch an image of `pixels` across prints at `percent` of the text column."""
    return round(pixels / (COLUMN_INCHES * percent / 100))


def target_width(pixels: int, percent: int) -> int:
    """The width in percent that brings an image to at least 150 ppi, at most the width it has now.

    Rounded down, and a step further where the rounding of the density would
    leave it a pixel short of the target.
    """
    width = max(1, math.floor(percent * printed_density(pixels, percent) / TARGET_PPI))
    while width > 1 and printed_density(pixels, width) < TARGET_PPI:
        width -= 1
    return min(width, percent)


def image_pixels(page_dir: Path, source: str) -> int | None:
    """How many pixels across the image a page references is, or None for one this tool leaves alone.

    Remote images, SVGs and files that are missing or unreadable get no width.
    """
    if re.match(r"^[a-z][a-z0-9+.-]*:", source, re.IGNORECASE) or source.startswith("/"):
        return None
    path = page_dir / urllib.parse.unquote(source.split("#")[0].split("?")[0])
    if path.suffix.lower() not in RASTER_SUFFIXES or not path.is_file():
        return None
    try:
        with Image.open(path) as image:
            return image.width
    except (OSError, UnidentifiedImageError):
        return None


def fit_widths(text: str, page_dir: Path) -> tuple[str, list[tuple[str, int, int, int, int]]]:
    """A page's Markdown with every image that prints below 150 ppi narrowed, and what changed.

    An image without a width fills the column, so it is measured at 100 %. An
    existing width is replaced, whether it is quoted or not; an attribute list
    without one gains it; an image without attributes gets
    `{ width="NN%" }`. Images inside fenced code blocks stay as they are.
    """
    lines = text.split("\n")
    changes: list[tuple[str, int, int, int, int]] = []
    fenced = False

    def narrow(match: re.Match) -> str:
        attrs = match.group("attrs") or ""
        declared = WIDTH.search(attrs)
        percent = int(declared.group("percent")) if declared else 100
        pixels = image_pixels(page_dir, match.group("src"))
        if pixels is None:
            return match.group(0)
        density = printed_density(pixels, percent)
        if density >= TARGET_PPI:
            return match.group(0)
        width = target_width(pixels, percent)
        changes.append((match.group("src"), percent, width, density, printed_density(pixels, width)))
        if declared:
            return match.group(0)[: -len(attrs)] + attrs[: declared.start()] + f'width="{width}%"' + attrs[declared.end():]
        if attrs:
            return match.group(0)[: -len(attrs)] + attrs[:-1].rstrip() + f' width="{width}%" }}'
        return match.group(0) + f'{{ width="{width}%" }}'

    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced and "![" in line:
            lines[index] = IMAGE.sub(narrow, line)
    return "\n".join(lines), changes


@click.command(name="image-widths")
@click.option("--fix", is_flag=True, help="Write the widths into the pages instead of listing what is too coarse.")
@click.argument("paths", nargs=-1, type=click.Path(exists=True, path_type=Path))
def image_widths(fix: bool, paths: tuple[Path, ...]) -> None:
    """List the raster images that print below 150 ppi in pages that are not generated - or narrow them."""
    roots = paths or (DOCS_DIR,)
    pages = sorted({page for root in roots for page in ([root] if root.is_file() else root.rglob("*.md"))})
    count = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if GENERATED_MARK.search("\n".join(text.splitlines()[:15])):
            continue
        result, changes = fit_widths(text, page.parent)
        if not changes:
            continue
        count += len(changes)
        for source, percent, width, density, target in changes:
            print(f"{page}: {source} {percent}% -> {width}%, {density} -> {target} ppi")
        if fix:
            page.write_text(result, encoding="utf-8")
    if fix:
        print(f"{count} image widths written")
    elif count:
        raise click.ClickException(
            f"{count} images print below {TARGET_PPI} ppi - run `dec-tool image-widths --fix`"
        )
    else:
        print(f"every image prints at {TARGET_PPI} ppi or more")
