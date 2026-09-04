"""Test the navigation builder"""
from pathlib import Path

from click.testing import CliRunner

from tools.build_navigation import build_navigation


def write_docs_tree(docs: Path) -> None:
    """Create a minimal docs tree with a single page."""
    docs.mkdir()
    (docs / ".pages").write_text("nav:\n    - index.md\n")
    (docs / "index.md").write_text("# Home\n")


def test_check_passes_when_in_sync(tmp_path):
    """A nav file matching the .pages files exits 0"""
    docs = tmp_path / "docs"
    write_docs_tree(docs)
    nav = tmp_path / "nav.yml"

    runner = CliRunner()
    written = runner.invoke(build_navigation, ["--docs-dir", str(docs), "-o", str(nav)])
    assert written.exit_code == 0
    assert nav.read_text() == "nav:\n- index.md\n"

    checked = runner.invoke(
        build_navigation, ["--docs-dir", str(docs), "-o", str(nav), "--check"]
    )
    assert checked.exit_code == 0
    assert "matches the .pages files" in checked.output


def test_check_fails_and_diffs_on_drift(tmp_path):
    """A stale nav file exits 1 and reports what drifted"""
    docs = tmp_path / "docs"
    write_docs_tree(docs)
    nav = tmp_path / "nav.yml"
    nav.write_text("nav:\n- outdated.md\n")

    result = CliRunner().invoke(
        build_navigation, ["--docs-dir", str(docs), "-o", str(nav), "--check"]
    )
    assert result.exit_code == 1
    assert "-- outdated.md" in result.output
    assert "+- index.md" in result.output
    assert "Run 'task update:navigation' and commit the result." in result.output
    # the stale file is left untouched, so the diff stays reproducible
    assert nav.read_text() == "nav:\n- outdated.md\n"
