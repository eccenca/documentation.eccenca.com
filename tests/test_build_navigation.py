"""Test the navigation builder"""
from pathlib import Path

import click
import pytest
from click.testing import CliRunner

from tools.build_navigation import (
    NAV_HEADER,
    build_nav_list,
    build_navigation,
    dir_title,
    discover_dir,
    expand_dir,
    expand_item,
    has_markdown,
    read_pages,
    render_nav,
)


def make_docs(root: Path, files: dict[str, str]) -> Path:
    """Create a docs tree below root from a {relative path: content} mapping."""
    docs = root / "docs"
    docs.mkdir(exist_ok=True)
    for rel, content in files.items():
        path = docs / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return docs


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("getting-started", "Getting started"),
        ("build", "Build"),
        ("with_your_sandbox", "With your sandbox"),
        # Capitalisation only happens for all-lowercase names, which is what
        # keeps acronyms intact instead of mangling them to "Link Ids Event".
        ("link-IDS-event-to-KG", "link IDS event to KG"),
        ("cmemc", "Cmemc"),
    ],
)
def test_dir_title(name, expected):
    """Directory names become titles the way MkDocs derives them"""
    assert dir_title(name) == expected


def test_read_pages_without_file(tmp_path):
    """A directory without a .pages file has no nav configuration"""
    assert read_pages(tmp_path) is None


def test_read_pages_empty_file(tmp_path):
    """An empty .pages file is treated as no configuration, not as an error"""
    (tmp_path / ".pages").write_text("")
    assert read_pages(tmp_path) is None


def test_read_pages_returns_the_parsed_yaml(tmp_path):
    """A .pages file is parsed into its YAML mapping"""
    (tmp_path / ".pages").write_text("title: Overview\nnav:\n    - index.md\n")
    assert read_pages(tmp_path) == {"title": "Overview", "nav": ["index.md"]}


def test_has_markdown_finds_nested_pages(tmp_path):
    """Markdown anywhere below a directory counts, however deeply nested"""
    (tmp_path / "deep" / "deeper").mkdir(parents=True)
    (tmp_path / "deep" / "deeper" / "page.md").write_text("# Page")
    assert has_markdown(tmp_path) is True


def test_has_markdown_ignores_directories_without_markdown(tmp_path):
    """A directory holding only assets is not navigable"""
    (tmp_path / "assets").mkdir()
    (tmp_path / "assets" / "logo.svg").write_text("<svg/>")
    assert has_markdown(tmp_path) is False


def test_discover_dir_orders_like_mkdocs(tmp_path):
    """Index first, then the remaining markdown files, then subdirectories"""
    docs = make_docs(tmp_path, {
        "guide/zebra.md": "# Zebra",
        "guide/index.md": "# Guide",
        "guide/alpha.md": "# Alpha",
        "guide/nested/index.md": "# Nested",
    })

    assert discover_dir(docs / "guide", Path("guide")) == [
        "guide/index.md",
        "guide/alpha.md",
        "guide/zebra.md",
        {"Nested": ["guide/nested/index.md"]},
    ]


def test_discover_dir_skips_directories_without_markdown(tmp_path):
    """Asset directories never reach the navigation"""
    docs = make_docs(tmp_path, {
        "guide/index.md": "# Guide",
        "guide/img/diagram.svg": "<svg/>",
    })

    assert discover_dir(docs / "guide", Path("guide")) == ["guide/index.md"]


def test_expand_dir_prefers_a_nested_pages_file(tmp_path):
    """A directory's own .pages wins over discovery, including its order"""
    docs = make_docs(tmp_path, {
        "guide/.pages": "nav:\n    - second.md\n    - first.md\n",
        "guide/first.md": "# First",
        "guide/second.md": "# Second",
    })

    assert expand_dir("Guide", docs / "guide", Path("guide")) == {
        "Guide": ["guide/second.md", "guide/first.md"]
    }


def test_expand_dir_expands_a_directory_without_pages(tmp_path):
    """A directory without .pages is walked, never emitted as a bare reference

    Zensical does not resolve a bare directory to a page object: doing so costs
    the entry its icon front matter, empties the sidebar under navigation.tabs
    and drops every other page in the directory from the navigation.
    """
    docs = make_docs(tmp_path, {
        "guide/index.md": "# Guide",
        "guide/details.md": "# Details",
    })

    resolved = expand_dir("Guide", docs / "guide", Path("guide"))

    assert resolved == {"Guide": ["guide/index.md", "guide/details.md"]}
    assert resolved != {"Guide": "guide"}


def test_expand_dir_keeps_a_titled_lone_index_page_as_a_section(tmp_path):
    """A titled directory holding only an index page stays a one-item section

    This is what lets MkDocs' `navigation.indexes` attach the page to the
    section header (self-link) while still keeping it as its own resolvable
    nav item -- collapsing it to a bare link here would instead attach it to
    the *parent* section, silently swallowing this title from the sidebar.
    """
    docs = make_docs(tmp_path, {"guide/index.md": "# Guide"})

    assert expand_dir("Guide", docs / "guide", Path("guide")) == {
        "Guide": ["guide/index.md"]
    }


def test_expand_dir_without_a_title_returns_bare_children(tmp_path):
    """Titleless expansion splices the children into the parent list"""
    docs = make_docs(tmp_path, {
        "guide/index.md": "# Guide",
        "guide/details.md": "# Details",
    })

    assert expand_dir(None, docs / "guide", Path("guide")) == [
        "guide/index.md",
        "guide/details.md",
    ]


def test_expand_item_resolves_a_plain_filename(tmp_path):
    """A bare filename becomes a docs-relative path"""
    docs = make_docs(tmp_path, {"guide/index.md": "# Guide"})

    assert expand_item("index.md", docs / "guide", Path("guide")) == "guide/index.md"


def test_expand_item_inherits_the_title_from_a_subdirectory(tmp_path):
    """An untitled directory entry picks up the title: key of its own .pages"""
    docs = make_docs(tmp_path, {
        "guide/.pages": "title: Inherited\nnav:\n    - index.md\n",
        "guide/index.md": "# Guide",
    })

    assert expand_item("guide", docs, Path("")) == {"Inherited": ["guide/index.md"]}


def test_expand_item_titles_a_single_file(tmp_path):
    """A one-key mapping to a file becomes a titled link"""
    docs = make_docs(tmp_path, {"intro.md": "# Intro"})

    assert expand_item({"Introduction": "intro.md"}, docs, Path("")) == {
        "Introduction": "intro.md"
    }


def test_expand_item_builds_an_inline_section(tmp_path):
    """A one-key mapping to a list becomes a section, flattening expansions"""
    docs = make_docs(tmp_path, {
        "intro.md": "# Intro",
        "guide/index.md": "# Guide",
        "guide/details.md": "# Details",
    })

    assert expand_item({"Section": ["intro.md", "guide"]}, docs, Path("")) == {
        "Section": ["intro.md", "guide/index.md", "guide/details.md"]
    }


def test_build_nav_list_skips_unresolvable_entries(tmp_path):
    """Entries that resolve to nothing drop out instead of failing the build"""
    docs = make_docs(tmp_path, {"intro.md": "# Intro"})

    assert build_nav_list(["intro.md", None], docs, Path("")) == ["intro.md"]


def test_render_nav_without_a_pages_file(tmp_path):
    """A docs tree with no .pages cannot describe a navigation"""
    docs = make_docs(tmp_path, {"index.md": "# Home"})

    with pytest.raises(click.ClickException):
        render_nav(docs)


def test_render_nav_without_a_nav_block(tmp_path):
    """A .pages file carrying only a title cannot describe a navigation"""
    docs = make_docs(tmp_path, {".pages": "title: Docs\n", "index.md": "# Home"})

    with pytest.raises(click.ClickException):
        render_nav(docs)


def test_render_nav_keeps_unicode_unescaped(tmp_path):
    """Titles survive the YAML dump as characters, not escape sequences"""
    docs = make_docs(tmp_path, {
        ".pages": "nav:\n    - \u00dcberblick: index.md\n",
        "index.md": "# Home",
    })

    assert "\u00dcberblick" in render_nav(docs)


def test_render_nav_is_yamllint_clean(tmp_path):
    """The rendered file carries the header and indents sequences under their key

    This is the shape yamllint's default rules accept: a `---` document start,
    sequences indented beneath their parent mapping key (`indent-sequences`),
    a single space after each hyphen (`hyphens`), and a consistent two-column
    step throughout (`indentation` with `spaces: consistent`).
    """
    docs = make_docs(tmp_path, {
        ".pages": "nav:\n    - Section: sub\n",
        "sub/index.md": "# Sub",
        "sub/page.md": "# Page",
    })

    assert render_nav(docs) == NAV_HEADER + (
        "nav:\n"
        "  - Section:\n"
        "      - sub/index.md\n"
        "      - sub/page.md\n"
    )


def test_check_passes_when_in_sync(tmp_path):
    """A nav file matching the .pages files exits 0"""
    docs = make_docs(tmp_path, {".pages": "nav:\n    - index.md\n", "index.md": "# Home"})
    nav = tmp_path / "nav.yml"

    runner = CliRunner()
    written = runner.invoke(build_navigation, ["--docs-dir", str(docs), "-o", str(nav)])
    assert written.exit_code == 0
    assert nav.read_text() == NAV_HEADER + "nav:\n  - index.md\n"

    checked = runner.invoke(
        build_navigation, ["--docs-dir", str(docs), "-o", str(nav), "--check"]
    )
    assert checked.exit_code == 0
    assert "matches the .pages files" in checked.output


def test_check_fails_and_diffs_on_drift(tmp_path):
    """A stale nav file exits 1 and reports what drifted"""
    docs = make_docs(tmp_path, {".pages": "nav:\n    - index.md\n", "index.md": "# Home"})
    nav = tmp_path / "nav.yml"
    nav.write_text("nav:\n- outdated.md\n")

    result = CliRunner().invoke(
        build_navigation, ["--docs-dir", str(docs), "-o", str(nav), "--check"]
    )
    assert result.exit_code == 1
    assert "-- outdated.md" in result.output
    assert "+  - index.md" in result.output
    assert "Run 'task update:navigation' and commit the result." in result.output
    # the stale file is left untouched, so the diff stays reproducible
    assert nav.read_text() == "nav:\n- outdated.md\n"


def test_check_treats_a_missing_nav_file_as_drift(tmp_path):
    """Checking before the file exists reports drift rather than crashing"""
    docs = make_docs(tmp_path, {".pages": "nav:\n    - index.md\n", "index.md": "# Home"})
    nav = tmp_path / "nav.yml"

    result = CliRunner().invoke(
        build_navigation, ["--docs-dir", str(docs), "-o", str(nav), "--check"]
    )
    assert result.exit_code == 1
    assert not nav.exists()


def test_missing_docs_dir_is_a_usage_error(tmp_path):
    """Pointing at a docs tree that is not there fails as a usage error"""
    result = CliRunner().invoke(
        build_navigation, ["--docs-dir", str(tmp_path / "absent")]
    )
    assert result.exit_code == 2
