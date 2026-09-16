"""Test the Ghostscript pass that turns the print edition into PDF/X-4 (tasks/spec.md, §7; backlog P13)"""
import glob
import hashlib
import shutil
import zipfile
from pathlib import Path

import click
import pytest
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DecodedStreamObject, DictionaryObject, NameObject, TextStringObject

from tools.pdf_normalize import (
    ensure_gray_profile,
    fetch_profile,
    ghostscript_command,
    ghostscript_is_tested,
    ghostscript_writes_pdfx4,
    gray_command,
    gray_path,
    gray_preview,
    is_pdfx4,
    normalize,
    normalized_path,
    pdfx_prefix,
    postscript_string,
)


def test_postscript_strings_escape_backslashes_and_parentheses():
    assert postscript_string(r"a (b) \c") == r"(a \(b\) \\c)"


def test_the_prefix_declares_pdfx4_and_the_fogra39_output_intent():
    prefix = pdfx_prefix(Path("/profiles/ISO (coated).icc"), "Corporate Memory (26.2)")
    assert "/GTS_PDFXVersion (PDF/X-4)" in prefix
    assert "/Trapped /False" in prefix
    assert r"/Title (Corporate Memory \(26.2\))" in prefix
    assert r"(/profiles/ISO \(coated\).icc) (r) file" in prefix
    assert "/OutputConditionIdentifier (FOGRA39)" in prefix
    assert "/N 4" in prefix


def test_the_ghostscript_command_follows_the_verified_recipe():
    command = ghostscript_command("gs", Path("prefix.ps"), Path("profile.icc"), Path("in.pdf"), Path("out.pdf"))
    for flag in (
        "-dPDFX=4", "-sDEVICE=pdfwrite", "-sColorConversionStrategy=CMYK", "-sProcessColorModel=DeviceCMYK",
        "-dColorImageResolution=300", "-dGrayImageResolution=300", "-dColorImageDownsampleThreshold=1.0",
        "-dPreserveAnnots=false", "--permit-file-read=profile.icc", "-sOutputFile=out.pdf",
    ):
        assert flag in command
    # The profile goes in through the prefix file only: -sOutputICCProfile with -dPDFX crashes Ghostscript.
    assert not any(part.startswith("-sOutputICCProfile") for part in command)
    assert command[-2:] == ["prefix.ps", "in.pdf"]


def test_the_gray_preview_is_the_same_pass_in_devicegray():
    command = gray_command("gs", Path("prefix.ps"), Path("gray.icc"), Path("in.pdf"), Path("out.pdf"))
    for flag in (
        "-dPDFX=4", "-sDEVICE=pdfwrite", "-sColorConversionStrategy=Gray", "-sProcessColorModel=DeviceGray",
        "-dColorImageResolution=300", "-dPreserveAnnots=false", "--permit-file-read=gray.icc",
        "-sOutputFile=out.pdf",
    ):
        assert flag in command
    assert not any(part.startswith("-sOutputICCProfile") for part in command)
    assert command[-2:] == ["prefix.ps", "in.pdf"]


def test_each_output_is_named_after_what_it_is():
    book = Path("dist/documentation-eccenca-com-26-2-print.pdf")
    assert normalized_path(book).name == "documentation-eccenca-com-26-2-print-x4.pdf"
    assert gray_path(book).name == "documentation-eccenca-com-26-2-print-gray-x4.pdf"


@pytest.mark.parametrize(
    "version, writes_pdfx4, tested",
    [
        ("10.08.0", True, True),
        ("10.10.0", True, True),
        ("11.0.0", True, True),
        ("10.07.1", True, False),   # writes PDF/X-4, but is not the verified release
        ("10.03.0", True, False),
        ("10.02.1", False, False),  # -dPDFX is a boolean here
        ("GPL Ghostscript 10.02.1 (2023-11-01)", False, False),
        ("9.55.0", False, False),
        ("", True, True),           # an unknown version says nothing
        ("Page 1\nPage 2", True, True),  # nor does a wrapper that answers with something of its own
    ],
)
def test_the_ghostscript_version_is_judged_by_what_it_can_do(version, writes_pdfx4, tested):
    assert ghostscript_writes_pdfx4(version) is writes_pdfx4
    assert ghostscript_is_tested(version) is tested


def test_the_grey_profile_can_be_named_by_the_environment(tmp_path, monkeypatch):
    profile = tmp_path / "gray.icc"
    profile.write_bytes(b"icc profile bytes")
    monkeypatch.setenv("PDF_GRAY_PROFILE", str(profile))
    assert ensure_gray_profile() == profile
    monkeypatch.setenv("PDF_GRAY_PROFILE", str(tmp_path / "gone.icc"))
    with pytest.raises(click.ClickException, match="not found"):
        ensure_gray_profile()


def test_the_grey_prefix_names_one_component_and_no_registry():
    prefix = pdfx_prefix(
        Path("/profiles/gray.icc"), "Book", components=1, identifier="sGray", condition="A grey profile",
        registry=None,
    )
    assert "/N 1" in prefix
    assert "/OutputConditionIdentifier (sGray)" in prefix
    assert "/Info (A grey profile)" in prefix
    assert "/RegistryName" not in prefix


def blank_pdf(path, pdfx=False):
    writer = PdfWriter()
    writer.add_blank_page(595.28, 841.89)
    if pdfx:
        writer.add_metadata({"/GTS_PDFXVersion": "PDF/X-4"})
        intent = DictionaryObject({
            NameObject("/Type"): NameObject("/OutputIntent"),
            NameObject("/S"): NameObject("/GTS_PDFX"),
            NameObject("/OutputConditionIdentifier"): TextStringObject("FOGRA39"),
        })
        writer.root_object[NameObject("/OutputIntents")] = ArrayObject([intent])
    writer.write(path)
    return path


def test_only_a_file_with_the_marker_and_an_output_intent_counts_as_pdfx4(tmp_path):
    assert is_pdfx4(blank_pdf(tmp_path / "x4.pdf", pdfx=True))
    assert not is_pdfx4(blank_pdf(tmp_path / "plain.pdf"))


def test_the_profile_is_fetched_from_its_archive_and_checked(tmp_path):
    payload = b"icc profile bytes"
    archive = tmp_path / "profiles.zip"
    member = "ECI_Offset_2009/ISOcoated_v2_eci.icc"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr(member, payload)
    target = tmp_path / "cache" / "ISOcoated_v2_eci.icc"
    fetch_profile(target, archive.as_uri(), member, hashlib.sha256(payload).hexdigest())
    assert target.read_bytes() == payload
    with pytest.raises(click.ClickException, match="checksum"):
        fetch_profile(tmp_path / "other.icc", archive.as_uri(), member, "0" * 64)
    assert not (tmp_path / "other.icc").exists()


def ghostscript_cmyk_profile():
    """The generic CMYK profile Ghostscript ships, where a common install puts it."""
    patterns = (
        "/opt/homebrew/share/ghostscript/iccprofiles/default_cmyk.icc",
        "/opt/homebrew/Cellar/ghostscript/*/share/ghostscript/iccprofiles/default_cmyk.icc",
        "/usr/local/share/ghostscript/iccprofiles/default_cmyk.icc",
        "/usr/share/ghostscript/*/iccprofiles/default_cmyk.icc",
        "/usr/share/color/icc/ghostscript/default_cmyk.icc",
    )
    found = [path for pattern in patterns for path in glob.glob(pattern)]
    return Path(found[0]) if found else None


def test_a_failed_ghostscript_run_leaves_no_file_and_names_the_page(tmp_path):
    fake = tmp_path / "gs"
    fake.write_text(
        "#!/bin/sh\n"
        'for arg in "$@"; do case "$arg" in -sOutputFile=*) printf partial > "${arg#-sOutputFile=}";; esac; done\n'
        "echo 'Page 1'; echo 'Page 2'\n"
        "echo '   **** Error: error executing PDF token' >&2\n"
        "exit 1\n"
    )
    fake.chmod(0o755)
    output = tmp_path / "out.pdf"
    with pytest.raises(click.ClickException, match="after page 2") as failure:
        normalize(blank_pdf(tmp_path / "in.pdf"), output, tmp_path / "profile.icc", str(fake), title="Test")
    assert "error executing PDF token" in failure.value.message
    assert not output.exists()


def test_content_ghostscript_repaired_away_fails_the_run(tmp_path):
    fake = tmp_path / "gs"
    fake.write_text(
        "#!/bin/sh\n"
        'for arg in "$@"; do case "$arg" in -sOutputFile=*) printf repaired > "${arg#-sOutputFile=}";; esac; done\n'
        "printf 'The following errors were encountered at least once while processing this file:\\n"
        "\\terror executing PDF token\\n' >&2\n"
    )
    fake.chmod(0o755)
    output = tmp_path / "out.pdf"
    with pytest.raises(click.ClickException, match="left out content"):
        normalize(blank_pdf(tmp_path / "in.pdf"), output, tmp_path / "profile.icc", str(fake), title="Test")
    assert not output.exists()


@pytest.mark.skipif(shutil.which("gs") is None, reason="Ghostscript is not installed")
def test_ghostscript_writes_pdfx4(tmp_path):
    profile = ghostscript_cmyk_profile()
    if profile is None:
        pytest.skip("no CMYK profile of Ghostscript found")
    output = tmp_path / "out.pdf"
    normalize(blank_pdf(tmp_path / "in.pdf"), output, profile, "gs", title="Test (1)")
    assert is_pdfx4(output)


@pytest.mark.skipif(shutil.which("gs") is None, reason="Ghostscript is not installed")
def test_ghostscript_writes_a_gray_preview_as_pdfx4(tmp_path):
    try:
        ensure_gray_profile()
    except click.ClickException:
        pytest.skip("no grey ICC profile of Ghostscript found")
    writer = PdfWriter()
    page = writer.add_blank_page(595.28, 841.89)
    content = DecodedStreamObject()
    content.set_data(b"1 0 0 rg 0 0 100 100 re f 0 1 1 0 k 100 100 100 100 re f")
    page[NameObject("/Contents")] = writer._add_object(content)
    source = tmp_path / "colour.pdf"
    writer.write(source)
    output = gray_preview(source, tmp_path / "colour-gray.pdf", title="Test")
    data = PdfReader(output).pages[0].get_contents().get_data()
    assert b"re" in data  # the areas are still drawn
    assert b" rg" not in data and b" k\n" not in data and b" k " not in data
    assert is_pdfx4(output)
    intents = PdfReader(output).trailer["/Root"]["/OutputIntents"]
    assert str(intents[0].get_object()["/OutputConditionIdentifier"]) == "sGray"
