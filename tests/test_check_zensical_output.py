"""Test the redirect check of the Zensical output guard"""

import importlib

import pytest

from tools.check_zensical_output import check_redirects, page_url, redirect_maps

# `tools/__init__.py` rebinds `tools.check_zensical_output` to the click command,
# so the module itself has to come from the import system.
guard = importlib.import_module("tools.check_zensical_output")

CONFIG = """\
plugins:
  - search
  - redirects:
      redirect_maps:
        old/index.md: new/index.md
  - tags:
      listings_sort_by: !!python/name:material.plugins.tags.item_title
"""

# The shape Zensical 0.0.61+ writes for a page redirect.
REDIRECT_PAGE = '<head><meta http-equiv="refresh" content="0; url={url}"></head>'


@pytest.fixture(autouse=True)
def fresh_failures(monkeypatch):
    """Isolate the module-level failure list between tests"""
    monkeypatch.setattr(guard, "failures", [])


@pytest.fixture
def config(tmp_path):
    path = tmp_path / "mkdocs.yml"
    path.write_text(CONFIG, encoding="utf-8")
    return path


def build(site, pages):
    """Write one index.html per site-relative directory"""
    for directory, body in pages.items():
        page = site / directory / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(body, encoding="utf-8")


def test_page_url_follows_directory_urls():
    """Test that Markdown paths map to the URLs Zensical publishes them at"""
    assert page_url("index.md") == ""
    assert page_url("release-notes/2026/corporate-memory-26-2/index.md") == "release-notes/2026/corporate-memory-26-2/"
    assert page_url("guide.md") == "guide/"
    assert page_url("guide/index.md#setup") == "guide/#setup"


def test_redirect_maps_reads_past_python_name_tags(config):
    """Test that the !!python/name handles in mkdocs.yml do not break loading"""
    assert redirect_maps(config) == {"old/index.md": "new/index.md"}


def test_check_redirects_accepts_a_redirect_that_lands(tmp_path, config):
    """Test that a relative refresh URL is resolved against the redirect page"""
    site = tmp_path / "site"
    build(site, {"old": REDIRECT_PAGE.format(url="../new/"), "new": "<h1>New</h1>"})

    check_redirects(site, config)

    assert guard.failures == []


def test_check_redirects_rejects_a_redirect_that_lands_elsewhere(tmp_path, config):
    """Test that a redirect page pointing at the wrong page fails"""
    site = tmp_path / "site"
    build(site, {"old": REDIRECT_PAGE.format(url="../elsewhere/"), "new": "<h1>New</h1>"})

    check_redirects(site, config)

    assert guard.failures == ["redirects: /old/ redirects to /elsewhere/, expected /new/"]


def test_check_redirects_rejects_a_missing_redirect_page(tmp_path, config):
    """Test that a mapping Zensical wrote no page for fails"""
    site = tmp_path / "site"
    build(site, {"new": "<h1>New</h1>"})

    check_redirects(site, config)

    assert guard.failures == ["redirects: no redirect page at /old/"]


def test_check_redirects_fails_without_redirect_maps(tmp_path):
    """Test that dropping the plugin block counts as losing every old URL"""
    config = tmp_path / "mkdocs.yml"
    config.write_text("plugins:\n  - search\n", encoding="utf-8")

    check_redirects(tmp_path / "site", config)

    assert len(guard.failures) == 1
    assert "no redirect_maps" in guard.failures[0]
