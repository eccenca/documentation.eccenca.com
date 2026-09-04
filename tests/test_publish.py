"""Test the publish helpers that guard what reaches the public branch"""

from tools.publish import canonical_url, prune


def test_prune_removes_copied_along_dotfiles(tmp_path):
    """Test that .pages and .DS_Store go, at any depth, and nothing else does"""
    (tmp_path / "nested").mkdir()
    keep = [tmp_path / "index.html", tmp_path / "nested" / "pages.html"]
    drop = [
        tmp_path / ".pages",
        tmp_path / ".DS_Store",
        tmp_path / "nested" / ".pages",
    ]
    for path in keep + drop:
        path.touch()

    removed = prune(tmp_path)

    assert sorted(removed) == sorted(drop)
    assert all(path.exists() for path in keep)
    assert not any(path.exists() for path in drop)


def test_prune_is_idempotent(tmp_path):
    """Test that a second publish of an already-clean site/ is a no-op"""
    (tmp_path / "index.html").touch()

    assert prune(tmp_path) == []


def test_canonical_url_reads_the_landing_page(tmp_path):
    """Test that the canonical URL is picked up, which is the version guard"""
    (tmp_path / "index.html").write_text(
        '<link rel="canonical" href="https://documentation.eccenca.com/26.2/">',
        encoding="utf-8",
    )

    assert canonical_url(tmp_path) == "https://documentation.eccenca.com/26.2/"


def test_canonical_url_without_a_landing_page(tmp_path):
    """Test that a missing or canonical-less index.html is reported, not raised"""
    assert canonical_url(tmp_path) is None

    (tmp_path / "index.html").write_text("<html></html>", encoding="utf-8")
    assert canonical_url(tmp_path) is None
