"""Write the missing width of raster images into the Markdown sources.

An image without a width prints at the pixel density it declares - 72 dpi when
it declares none - and the site shows it at its pixel size. `dec-tool
image-widths` writes `{ width="NN%" }` instead: the image's natural width as a
share of the full page width. A screenshot then prints at the size it had on the
screen it was captured on, and the site shows it in the same proportion
(tasks/spec.md, §11, D18). Generated pages are left alone: their generators own
them.

Without `--fix` the command lists the images without a width and fails, so a
check can catch a new screenshot; with `--fix` it writes the widths.
"""
from __future__ import annotations

import math
import re
import urllib.parse
from pathlib import Path

import click
from PIL import Image, UnidentifiedImageError

DOCS_DIR = Path("docs")
# The full page width in CSS pixels: the 16 cm text column of the print edition, at 96 per inch.
FULL_PAGE_WIDTH = 16 / 2.54 * 96
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
# The marker a generated page carries (.claude/docs-guidelines/repo-conventions.md).
GENERATED_MARK = re.compile(r"generated - do not change it manually|auto-generated", re.IGNORECASE)
# A Markdown image, with an optional title, and the attribute list that may follow it.
IMAGE = re.compile(r'!\[[^\]]*\]\((?P<src>[^)\s]+)(?:\s+"[^"]*")?\)(?P<attrs>\{[^}\n]*\})?')
FENCE = re.compile(r"^\s*(```|~~~)")


def capture_scale(dpi: float | None) -> float:
    """How many image pixels one CSS pixel took on the screen the image was captured on.

    144 dpi is a Retina capture on macOS, twice its 72 dpi base. Any other declared
    density counts against 96 dpi. An image that declares none, or less than 96 dpi,
    has scale 1.
    """
    if not dpi or dpi < 96:
        return 1.0
    if round(dpi) == 144:
        return 2.0
    return dpi / 96


def width_percent(pixels: int, dpi: float | None) -> int:
    """The image's natural width as a share of the full page width, rounded to 5 %, between 5 and 100 %."""
    natural = pixels / capture_scale(dpi)
    percent = 5 * math.floor(natural / FULL_PAGE_WIDTH * 20 + 0.5)
    return max(5, min(100, percent))


def image_width(page_dir: Path, source: str) -> int | None:
    """The width to write for an image a page references, or None for one that gets none.

    Remote images, SVGs and files that are missing or unreadable get none.
    """
    if re.match(r"^[a-z][a-z0-9+.-]*:", source, re.IGNORECASE) or source.startswith("/"):
        return None
    path = page_dir / urllib.parse.unquote(source.split("#")[0].split("?")[0])
    if path.suffix.lower() not in RASTER_SUFFIXES or not path.is_file():
        return None
    try:
        with Image.open(path) as image:
            dpi = image.info.get("dpi")
            return width_percent(image.width, float(dpi[0]) if dpi and dpi[0] else None)
    except (OSError, UnidentifiedImageError):
        return None


def add_widths(text: str, page_dir: Path) -> tuple[str, list[tuple[str, int]]]:
    """A page's Markdown with a width on every raster image that lacks one, and the images that got one.

    An existing attribute list gains the width; an image without one gets
    `{ width="NN%" }`. An image that would get 100 % gets none: it fills the
    column in print either way, and the width would only stretch a narrower
    screenshot to the article width on the site. Images inside fenced code
    blocks stay as they are.
    """
    lines = text.split("\n")
    changes: list[tuple[str, int]] = []
    fenced = False

    def widen(match: re.Match) -> str:
        attrs = match.group("attrs") or ""
        if "width" in attrs:
            return match.group(0)
        percent = image_width(page_dir, match.group("src"))
        if percent is None or percent >= 100:
            return match.group(0)
        changes.append((match.group("src"), percent))
        if attrs:
            return match.group(0)[: -len(attrs)] + attrs[:-1].rstrip() + f' width="{percent}%" }}'
        return match.group(0) + f'{{ width="{percent}%" }}'

    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced and "![" in line:
            lines[index] = IMAGE.sub(widen, line)
    return "\n".join(lines), changes


@click.command(name="image-widths")
@click.option("--fix", is_flag=True, help="Write the missing widths into the pages instead of listing them.")
@click.argument("paths", nargs=-1, type=click.Path(exists=True, path_type=Path))
def image_widths(fix: bool, paths: tuple[Path, ...]) -> None:
    """List the raster images without a width in pages that are not generated - or write their widths."""
    roots = paths or (DOCS_DIR,)
    pages = sorted({page for root in roots for page in ([root] if root.is_file() else root.rglob("*.md"))})
    count = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if GENERATED_MARK.search("\n".join(text.splitlines()[:15])):
            continue
        result, changes = add_widths(text, page.parent)
        if not changes:
            continue
        count += len(changes)
        for source, percent in changes:
            print(f'{page}: {source} width="{percent}%"')
        if fix:
            page.write_text(result, encoding="utf-8")
    if fix:
        print(f"{count} image widths written")
    elif count:
        raise click.ClickException(f"{count} images have no width - run `dec-tool image-widths --fix`")
    else:
        print("no image needs a width")
