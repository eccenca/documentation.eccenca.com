"""Test the list of low-resolution originals the print edition reports (backlog P15)"""
from collections import Counter
from pathlib import Path

import click
import pytest
from bs4 import BeautifulSoup
from PIL import Image

from tools.build_pdf import load_accepted_low_resolution, resolve_images, unaccepted_low_resolution


def test_originals_below_150_ppi_at_their_printed_size_are_listed_once(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    site = Path("site")
    (site / "build").mkdir(parents=True)
    Image.new("RGB", (300, 100), "white").save(site / "build/small.png")
    Image.new("RGB", (2000, 100), "white").save(site / "build/wide.png")
    Image.new("RGB", (600, 100), "white").save(site / "build/half.png")
    doc = BeautifulSoup(
        '<p><img src="/build/small.png" alt=""/><img src="/build/wide.png" alt=""/>'
        '<img src="/build/half.png" width="50%" alt=""/><img src="/build/small.png" alt=""/></p>',
        "html.parser",
    )
    low: dict[str, int] = {}
    resolve_images(doc, site, Counter(), [], Path("print-images"), low_resolution=low)
    # 300 px without a declared density print at 300 pt, 72 ppi; 2000 px fill the
    # 16 cm column at 317 ppi; 600 px at 50 % of the column print at 190 ppi.
    assert low == {"build/small.png": 72}


def test_the_screen_edition_lists_nothing(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    site = Path("site")
    (site / "build").mkdir(parents=True)
    Image.new("RGB", (300, 100), "white").save(site / "build/small.png")
    doc = BeautifulSoup('<img src="/build/small.png" alt=""/>', "html.parser")
    low: dict[str, int] = {}
    resolve_images(doc, site, Counter(), [], None, low_resolution=low)
    assert low == {}


def test_accepted_originals_are_not_listed(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("accepted-low-resolution:\n  - build/small.png\n")
    accepted = load_accepted_low_resolution(path)
    assert accepted == {"build/small.png"}
    assert unaccepted_low_resolution({"build/small.png": 72, "build/tiny.png": 40, "build/mid.png": 120}, accepted) == [
        ("build/tiny.png", 40),
        ("build/mid.png", 120),
    ]


def test_without_an_accepted_list_nothing_is_accepted(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("body-weight: light\n")
    assert load_accepted_low_resolution(path) == set()
    path.write_text("accepted-low-resolution: build/small.png\n")
    with pytest.raises(click.ClickException, match="accepted-low-resolution"):
        load_accepted_low_resolution(path)
