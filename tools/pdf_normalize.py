"""Turn the print edition into PDF/X-4 in CMYK with Ghostscript (tasks/spec.md, §7).

The recipe was verified with Ghostscript 10.08: `-dPDFX=4` with a prefix file
that writes the PDF/X-4 marker and the output intent, CMYK conversion, images
downsampled to 300 ppi and re-encoded losslessly, and annotations dropped.
Ghostscript gives three traps a wide berth only if they are known: a page with
an annotation makes it write plain PDF with a one-line warning, `-dPDFX=4` alone
writes no marker, and `-sOutputICCProfile` together with `-dPDFX` crashes it. So
the profile goes in through the prefix file only, and the output is checked for
the marker instead of trusting the exit code.

The output intent is ISO Coated v2 (ECI), the FOGRA39 profile BoD assumes for
CMYK. Its copyright does not allow redistribution, so it is not committed: it is
fetched from the ECI once, checked against its checksum and cached in the
gitignored `dist/icc/`, unless `--icc-profile` or PDF_ICC_PROFILE names a copy.

`--gray` runs the same pass in greyscale instead: a preview of how the book
prints in black and white, for checking the palette on screen (P11). It is
PDF/X-4 as well, with the generic grey profile Ghostscript ships as its output
intent - one component instead of four, and no colour registry to name.
"""
from __future__ import annotations

import glob
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

import click
from pypdf import PdfReader

PROFILE_URL = "https://www.eci.org/lib/exe/eci_offset_2009.zip"
PROFILE_MEMBER = "ECI_Offset_2009/ISOcoated_v2_eci.icc"
PROFILE_SHA256 = "128dc02f7246cc3807af0323695379f64151a8f27a587736acc59f8b6ce894b8"
PROFILE_CACHE = Path("dist/icc/ISOcoated_v2_eci.icc")
# The recipe of tasks/spec.md, §7 was verified with this release.
TESTED_GHOSTSCRIPT = "10.08"
# PDF/X-4 needs `-dPDFX=4`, and pdfwrite took that parameter as an integer only
# from 10.03 on. Before that it is a boolean (`gs_param_type_bool` in
# devices/vector/gdevpdfp.c), so the 4 raises `/typecheck in --pdfmark--` -
# Ubuntu 24.04 ships 10.02 and cannot write PDF/X-4 at all.
PDFX4_GHOSTSCRIPT = "10.03"
FOGRA39 = "FOGRA39"
FOGRA39_INFO = "ISO Coated v2 (ECI)"
COLOR_REGISTRY = "http://www.color.org"
# The greyscale preview prints by the generic grey profile Ghostscript ships.
GRAY_PROFILE_PATTERNS = (
    "/opt/homebrew/share/ghostscript/*/iccprofiles/default_gray.icc",
    "/opt/homebrew/Cellar/ghostscript/*/share/ghostscript/iccprofiles/default_gray.icc",
    "/usr/local/share/ghostscript/*/iccprofiles/default_gray.icc",
    "/usr/share/ghostscript/*/iccprofiles/default_gray.icc",
    "/usr/share/color/icc/ghostscript/default_gray.icc",
)
GRAY_CONDITION = "sGray"
GRAY_CONDITION_INFO = "Artifex Software sGray ICC Profile (Ghostscript default_gray.icc)"
# Both passes: images downsampled to 300 ppi and re-encoded losslessly, annotations dropped.
IMAGE_AND_ANNOTATION_OPTIONS = [
    "-dDownsampleColorImages=true", "-dColorImageDownsampleType=/Bicubic",
    "-dColorImageResolution=300", "-dColorImageDownsampleThreshold=1.0",
    "-dDownsampleGrayImages=true", "-dGrayImageDownsampleType=/Bicubic",
    "-dGrayImageResolution=300", "-dGrayImageDownsampleThreshold=1.0",
    "-dAutoFilterColorImages=false", "-dColorImageFilter=/FlateEncode",
    "-dAutoFilterGrayImages=false", "-dGrayImageFilter=/FlateEncode",
    "-dPreserveAnnots=false",
]


def postscript_string(text: str) -> str:
    """A PostScript string literal: backslashes and parentheses escaped."""
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return f"({escaped})"


def pdfx_prefix(
    profile: Path,
    title: str,
    components: int = 4,
    identifier: str = FOGRA39,
    condition: str = FOGRA39_INFO,
    registry: str | None = COLOR_REGISTRY,
) -> str:
    """The PostScript Ghostscript reads before the PDF: the PDF/X-4 marker, the title and the output intent.

    The book block prints by FOGRA39 in four components; the greyscale preview by
    the grey profile in one, and an unregistered condition names no registry.
    """
    intent = [
        "[{OutputIntent_PDFX} <<",
        "  /Type /OutputIntent",
        "  /S /GTS_PDFX",
        f"  /OutputCondition {postscript_string(condition)}",
        f"  /OutputConditionIdentifier {postscript_string(identifier)}",
    ]
    if registry:
        intent.append(f"  /RegistryName {postscript_string(registry)}")
    return "\n".join([
        "%!",
        "% PDF/X-4 definitions of dec-tool pdf-normalize (tasks/spec.md, section 7).",
        f"[/GTS_PDFXVersion (PDF/X-4) /Title {postscript_string(title)} /Trapped /False /DOCINFO pdfmark",
        "[/_objdef {icc_PDFX} /type /stream /OBJ pdfmark",
        f"[{{icc_PDFX}} <</N {components}>> /PUT pdfmark",
        f"[{{icc_PDFX}} {postscript_string(str(profile))} (r) file /PUT pdfmark",
        "[/_objdef {OutputIntent_PDFX} /type /dict /OBJ pdfmark",
        *intent,
        f"  /Info {postscript_string(condition)}",
        "  /DestOutputProfile {icc_PDFX}",
        ">> /PUT pdfmark",
        "[{Catalog} <</OutputIntents [ {OutputIntent_PDFX} ]>> /PUT pdfmark",
        "",
    ])


def ghostscript_command(ghostscript: str, prefix: Path, profile: Path, source: Path, output: Path) -> list[str]:
    """The Ghostscript call of tasks/spec.md, §7: PDF/X-4, CMYK, images at 300 ppi, no annotations."""
    return [
        ghostscript,
        "-dPDFX=4", "-dBATCH", "-dNOPAUSE",
        f"--permit-file-read={profile}",
        "-sDEVICE=pdfwrite",
        "-sColorConversionStrategy=CMYK", "-sProcessColorModel=DeviceCMYK",
        *IMAGE_AND_ANNOTATION_OPTIONS,
        f"-sOutputFile={output}",
        str(prefix), str(source),
    ]


def gray_command(ghostscript: str, prefix: Path, profile: Path, source: Path, output: Path) -> list[str]:
    """The greyscale preview: the same pass in DeviceGray, PDF/X-4 by the grey profile."""
    return [
        ghostscript,
        "-dPDFX=4", "-dBATCH", "-dNOPAUSE",
        f"--permit-file-read={profile}",
        "-sDEVICE=pdfwrite",
        "-sColorConversionStrategy=Gray", "-sProcessColorModel=DeviceGray",
        *IMAGE_AND_ANNOTATION_OPTIONS,
        f"-sOutputFile={output}",
        str(prefix), str(source),
    ]


def is_pdfx4(path: Path) -> bool:
    """Whether a PDF declares PDF/X-4 and carries an output intent."""
    reader = PdfReader(path)
    metadata = reader.metadata or {}
    return metadata.get("/GTS_PDFXVersion") == "PDF/X-4" and "/OutputIntents" in reader.trailer["/Root"]


def fetch_profile(target: Path, url: str = PROFILE_URL, member: str = PROFILE_MEMBER, sha256: str = PROFILE_SHA256) -> Path:
    """Download the profile's archive, take the profile out, check its checksum and store it at `target`."""
    print(f"Fetching the ICC profile from {url}", flush=True)
    try:
        with urllib.request.urlopen(url, timeout=120) as response:
            archive = response.read()
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            data = bundle.read(member)
    except (urllib.error.URLError, zipfile.BadZipFile, KeyError, OSError) as error:
        raise click.ClickException(f"cannot fetch {member} from {url} ({error})") from error
    if hashlib.sha256(data).hexdigest() != sha256:
        raise click.ClickException(f"{member} from {url} does not match its checksum - not using it")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return target


def ensure_profile(profile: Path | None = None) -> Path:
    """The output intent profile: the one named, else PDF_ICC_PROFILE, else the cached ECI profile, fetched if missing."""
    if profile is None and os.environ.get("PDF_ICC_PROFILE"):
        profile = Path(os.environ["PDF_ICC_PROFILE"])
    if profile is not None:
        if not profile.is_file():
            raise click.ClickException(f"ICC profile {profile} not found")
        return profile
    if PROFILE_CACHE.is_file() and hashlib.sha256(PROFILE_CACHE.read_bytes()).hexdigest() == PROFILE_SHA256:
        return PROFILE_CACHE
    return fetch_profile(PROFILE_CACHE)


def ensure_gray_profile(profile: Path | None = None) -> Path:
    """The grey output intent profile: the one named, else PDF_GRAY_PROFILE, else the one Ghostscript ships.

    Where a distribution puts `default_gray.icc` differs, so a build that cannot
    rely on the search paths - CI, for one - names the file it found instead.
    """
    if profile is None and os.environ.get("PDF_GRAY_PROFILE"):
        profile = Path(os.environ["PDF_GRAY_PROFILE"])
    if profile is not None:
        if not profile.is_file():
            raise click.ClickException(f"ICC profile {profile} not found")
        return profile
    found = [path for pattern in GRAY_PROFILE_PATTERNS for path in sorted(glob.glob(pattern))]
    if not found:
        raise click.ClickException(
            "no grey ICC profile found - Ghostscript ships default_gray.icc with its iccprofiles; "
            "name one with --icc-profile"
        )
    return Path(found[0])


def normalized_path(pdf: Path) -> Path:
    """Where the PDF/X-4 copy of a PDF goes: next to it, with -x4 before the suffix."""
    return pdf.with_name(f"{pdf.stem}-x4.pdf")


def gray_path(pdf: Path) -> Path:
    """Where the greyscale preview of a PDF goes: next to it, with -gray-x4 before the suffix - it is PDF/X-4 too."""
    return pdf.with_name(f"{pdf.stem}-gray-x4.pdf")


def ghostscript_at_least(version: str, wanted: str) -> bool:
    """Whether a Ghostscript version string names `wanted` or a newer release.

    Only a dotted `major.minor` counts as a version; anything else - a wrapper
    that answers `--version` with something of its own - passes unjudged.
    """
    found = re.search(r"(\d+)\.(\d+)", version)
    if found is None:
        return True
    return tuple(int(number) for number in found.groups()) >= tuple(int(n) for n in wanted.split("."))


def ghostscript_is_tested(version: str) -> bool:
    """Whether a Ghostscript version is the release series the recipe was verified with, or a newer one."""
    return ghostscript_at_least(version, TESTED_GHOSTSCRIPT)


def ghostscript_writes_pdfx4(version: str) -> bool:
    """Whether a Ghostscript version can write PDF/X-4 at all - `-dPDFX=4` is an integer only from 10.03 on."""
    return ghostscript_at_least(version, PDFX4_GHOSTSCRIPT)


def ghostscript_binary(ghostscript: str) -> str:
    """The Ghostscript to run, with a word about its version - an old one fails deep inside pdfmark."""
    binary = shutil.which(ghostscript)
    if binary is None:
        raise click.ClickException(f"{ghostscript} not found - install Ghostscript or name the binary with --ghostscript")
    version = subprocess.run([binary, "--version"], capture_output=True, text=True, check=False).stdout.strip()
    if version and not ghostscript_writes_pdfx4(version):
        raise click.ClickException(
            f"Ghostscript {version} cannot write PDF/X-4: `-dPDFX=4` is a boolean before {PDFX4_GHOSTSCRIPT} and "
            "the 4 raises `/typecheck in --pdfmark--`. Name a newer one with --ghostscript or GHOSTSCRIPT "
            f"(the recipe is verified with {TESTED_GHOSTSCRIPT})."
        )
    if version and not ghostscript_is_tested(version):
        print(
            f"NOTE: Ghostscript {version} is older than the {TESTED_GHOSTSCRIPT} the recipe was verified with.",
            file=sys.stderr,
        )
    return binary


def run_ghostscript(command: list[str], output: Path) -> subprocess.CompletedProcess:
    """Run Ghostscript, and fail - leaving no output - when it exits with an error or leaves content out."""
    started = time.monotonic()
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        output.unlink(missing_ok=True)
        lines = (result.stdout + result.stderr).splitlines()
        pages = [line for line in lines if line.startswith("Page ")]
        errors = [line.strip() for line in lines if "error" in line.lower()]
        where = f" after {pages[-1].lower()}" if pages else ""
        raise click.ClickException(
            f"Ghostscript failed{where} (exit {result.returncode}), no file written:\n" + "\n".join(errors[:20])
        )
    if "error executing PDF token" in result.stdout + result.stderr:
        # Ghostscript "repairs" such an error by leaving out what it could not
        # interpret - a colour emoji glyph, for one.
        output.unlink(missing_ok=True)
        raise click.ClickException(
            "Ghostscript left out content it could not interpret (error executing PDF token), no file written - "
            "look for Type 3 fonts in the source with `dec-tool pdf-preflight`"
        )
    print(f"Ghostscript took {time.monotonic() - started:.0f}s")
    return result


def normalize(source: Path, output: Path, profile: Path, ghostscript: str = "gs", title: str = "") -> Path:
    """Write `source` as PDF/X-4 in CMYK to `output`, and fail if Ghostscript fell back to plain PDF."""
    binary = ghostscript_binary(ghostscript)
    title = title or (PdfReader(source).metadata or {}).get("/Title") or source.stem
    with tempfile.TemporaryDirectory() as work:
        prefix = Path(work) / "pdfx.ps"
        prefix.write_text(pdfx_prefix(profile.resolve(), str(title)), encoding="utf-8")
        result = run_ghostscript(ghostscript_command(binary, prefix, profile.resolve(), source, output), output)
    require_pdfx4(output, result)
    return output


def require_pdfx4(output: Path, result: subprocess.CompletedProcess) -> None:
    """Fail if Ghostscript wrote plain PDF instead: one annotation left anywhere makes it fall back."""
    if is_pdfx4(output):
        return
    warnings = "\n".join(line for line in result.stdout.splitlines() if "warning" in line.lower())[-800:]
    raise click.ClickException(
        f"Ghostscript wrote plain PDF instead of PDF/X-4 to {output} - a page with an annotation makes it fall "
        f"back. Its warnings:\n{warnings}"
    )


def gray_preview(
    source: Path, output: Path, profile: Path | None = None, ghostscript: str = "gs", title: str = ""
) -> Path:
    """Write `source` in greyscale to `output` as PDF/X-4: how the book block prints in black and white (P11)."""
    binary = ghostscript_binary(ghostscript)
    profile = ensure_gray_profile(profile)
    title = title or (PdfReader(source).metadata or {}).get("/Title") or source.stem
    with tempfile.TemporaryDirectory() as work:
        prefix = Path(work) / "pdfx-gray.ps"
        prefix.write_text(
            pdfx_prefix(
                profile.resolve(), str(title),
                components=1, identifier=GRAY_CONDITION, condition=GRAY_CONDITION_INFO, registry=None,
            ),
            encoding="utf-8",
        )
        result = run_ghostscript(gray_command(binary, prefix, profile.resolve(), source, output), output)
    require_pdfx4(output, result)
    return output


@click.command(name="pdf-normalize")
@click.argument("pdf", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--output-file", "-o",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Where to write the file?  [default: next to the PDF, with -x4, or -gray-x4 with --gray]",
)
@click.option(
    "--gray",
    is_flag=True,
    help="Write a greyscale preview instead: how the book prints in black and white, PDF/X-4 by a grey profile.",
)
@click.option(
    "--icc-profile",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    envvar="PDF_ICC_PROFILE",
    default=None,
    help="Which profile is the output intent?  [default: ISO Coated v2 (ECI), fetched once into dist/icc/; "
    "with --gray, the grey profile Ghostscript ships]",
)
@click.option(
    "--ghostscript",
    default="gs",
    envvar="GHOSTSCRIPT",
    show_default=True,
    help="Which Ghostscript binary converts the PDF?",
)
def pdf_normalize(pdf: Path, output_file: Path | None, gray: bool, icc_profile: Path | None, ghostscript: str) -> None:
    """Write a PDF as PDF/X-4 in CMYK with Ghostscript, for print on demand - or in greyscale, as a preview."""
    if gray:
        output = output_file or gray_path(pdf)
        gray_preview(pdf, output, icc_profile, ghostscript)
        print(f"Greyscale preview written to {output} ({output.stat().st_size // 1024} KB)")
        return
    output = output_file or normalized_path(pdf)
    normalize(pdf, output, ensure_profile(icc_profile), ghostscript)
    print(f"PDF/X-4 written to {output} ({output.stat().st_size // 1024} KB)")
