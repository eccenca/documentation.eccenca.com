"""Tests for tools/render_tag_listings.py and overrides/partials/tags.html."""

import pathlib
import re

import pytest

from tools import render_tag_listings as rtl

TEMPLATE = pathlib.Path(__file__).resolve().parents[1] / "overrides" / "partials" / "tags.html"


# --- marker parsing -------------------------------------------------------


def test_bare_marker_has_no_filter():
    assert rtl.parse_marker("") is None
    assert rtl.parse_marker("  ") is None


def test_include_marker_yields_its_tags():
    assert rtl.parse_marker("{ include: [BeginnersTutorial] }") == ["BeginnersTutorial"]
    assert rtl.parse_marker("{include:[A, B]}") == ["A", "B"]


def test_quoted_tag_names_are_unwrapped():
    assert rtl.parse_marker('{ include: ["Load Balancer"] }') == ["Load Balancer"]


def test_unknown_argument_raises_rather_than_listing_everything():
    with pytest.raises(ValueError):
        rtl.parse_marker("{ exclude: [Foo] }")


def test_marker_regex_matches_both_forms():
    html = (
        "<p>x</p><!-- material/tags -->"
        "<!-- material/tags { include: [Beginners] } --><p>y</p>"
    )
    assert len(rtl.MARKER_RE.findall(html)) == 2


# --- slugs ----------------------------------------------------------------


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("BeginnersTutorial", "tag:beginnerstutorial"),
        ("Load Balancer", "tag:load-balancer"),
        ("Graph-Insights", "tag:graph-insights"),
        ("API", "tag:api"),
    ],
)
def test_tag_slug(tag, expected):
    assert rtl.tag_slug(tag) == expected


# --- relative links -------------------------------------------------------


@pytest.mark.parametrize(
    ("src", "dst", "expected"),
    [
        ("/tutorials/", "/build/active-learning/", "../build/active-learning/"),
        ("/tags/", "/build/reference/aggregator/min/", "../build/reference/aggregator/min/"),
        ("/a/b/c/", "/a/b/d/", "../d/"),
        ("/a/", "/a/b/", "b/"),
    ],
)
def test_relative_href(src, dst, expected):
    assert rtl.relative_href(src, dst) == expected


def test_relative_href_never_absolute():
    """mike serves under /latest/ and /26.2/, so absolute links would break."""
    assert not rtl.relative_href("/tags/", "/build/x/").startswith("/")


# --- title resolution -----------------------------------------------------


def write(tmp_path, rel, text):
    path = tmp_path / "docs" / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture(autouse=True)
def _docs_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(rtl, "DOCS_DIR", tmp_path / "docs")


def test_front_matter_title_beats_h1(tmp_path):
    page = write(tmp_path, "a/index.md", "---\ntitle: From Front Matter\n---\n\n# From H1\n")
    assert rtl.page_title(page) == "From Front Matter"


def test_h1_used_when_no_front_matter_title(tmp_path):
    page = write(tmp_path, "a/index.md", "---\ntags:\n  - X\n---\n\n# From H1\n")
    assert rtl.page_title(page) == "From H1"


def test_nav_title_used_when_page_offers_nothing(tmp_path):
    page = write(tmp_path, "a/b.md", "---\ntags:\n  - X\n---\n\n## only a subheading\n")
    assert rtl.page_title(page, {"a/b.md": "Nav Title"}) == "Nav Title"


def test_path_title_is_the_last_resort(tmp_path):
    page = write(tmp_path, "a/application-neptune-full.md", "---\ntags:\n  - X\n---\n\n## sub\n")
    assert rtl.page_title(page) == "Application neptune full"


def test_path_title_preserves_existing_casing(tmp_path):
    """Same rule as build_nav.py, so acronyms survive."""
    assert rtl.path_title(tmp_path / "docs" / "link-IDS-event-to-KG" / "index.md") == (
        "link IDS event to KG"
    )


def test_icon_shortcode_is_stripped_from_h1(tmp_path):
    page = write(tmp_path, "a/index.md", "---\n---\n\n# :material-star: Distribution\n")
    assert rtl.page_title(page) == "Distribution"


def test_hash_inside_a_fenced_block_is_not_a_heading(tmp_path):
    page = write(
        tmp_path,
        "a/index.md",
        "---\n---\n\n```bash\n# secure /api/** via resourceserver\n```\n\n# Real Heading\n",
    )
    assert rtl.page_title(page) == "Real Heading"


def test_malformed_front_matter_does_not_crash(tmp_path):
    page = write(tmp_path, "a/index.md", "---\ntags: [unclosed\n---\n\n# Still Works\n")
    assert rtl.page_title(page) == "Still Works"


# --- index ----------------------------------------------------------------


def test_build_index_groups_and_sorts_by_title(tmp_path):
    write(tmp_path, "b.md", "---\ntags:\n  - X\n---\n\n# Zebra\n")
    write(tmp_path, "a.md", "---\ntags:\n  - X\n  - Y\n---\n\n# Apple\n")
    index, problems = rtl.build_index(tmp_path / "docs")
    assert problems == []
    assert [t for t, _ in index["X"]] == ["Apple", "Zebra"]
    assert index["Y"] == [("Apple", "/a/")]


def test_untagged_pages_are_ignored(tmp_path):
    write(tmp_path, "a.md", "---\ntitle: No Tags\n---\n\n# A\n")
    index, problems = rtl.build_index(tmp_path / "docs")
    assert index == {} and problems == []


def test_site_url_maps_index_to_its_directory(tmp_path):
    assert rtl.site_url(tmp_path / "docs" / "a" / "index.md") == "/a/"
    assert rtl.site_url(tmp_path / "docs" / "a" / "b.md") == "/a/b/"


# --- rendering ------------------------------------------------------------


def test_mapped_tag_renders_with_its_icon_class():
    html = rtl.render_listing(
        ["BeginnersTutorial"],
        {"BeginnersTutorial": [("Some Page", "/build/x/")]},
        {"BeginnersTutorial": "beginners"},
        "/tutorials/",
        "¤",
    )
    assert 'class="md-tag md-tag-icon md-tag--beginners"' in html
    assert 'id="tag:beginnerstutorial"' in html
    assert 'href="../build/x/"' in html


def test_unmapped_tag_renders_bare(tmp_path):
    """Decision Q1: match production, no invented icons."""
    html = rtl.render_listing(
        ["TransformOperator"],
        {"TransformOperator": [("Some Page", "/build/x/")]},
        {},
        "/tags/",
        "¤",
    )
    assert 'class="md-tag"' in html
    assert "md-tag-icon" not in html


def test_listing_excludes_the_page_it_is_on():
    html = rtl.render_listing(
        ["X"], {"X": [("Self", "/tags/"), ("Other", "/a/")]}, {}, "/tags/", "¤"
    )
    assert "Other" in html and "Self" not in html


def test_titles_are_escaped():
    html = rtl.render_listing(
        ["X"], {"X": [("A & B <script>", "/a/")]}, {}, "/tags/", "¤"
    )
    assert "<script>" not in html
    assert "&amp;" in html


def test_include_order_is_preserved_not_sorted():
    index = {"Zed": [("p", "/z/")], "Alpha": [("p", "/a/")]}
    html = rtl.render_listing(["Zed", "Alpha"], index, {}, "/t/", "¤")
    assert html.index("tag:zed") < html.index("tag:alpha")


# --- slug parity with overrides/partials/tags.html -------------------------
#
# The chip links are built in MiniJinja, the listing anchors in Python. They must
# agree or every link dangles. `check_zensical_output.py` catches drift against a
# real build; these tests catch it without one, and pin the contract in words.


def _template_slug_expression() -> str:
    match = re.search(r'\{%\s*set anchor = (.+?)\s*%\}', TEMPLATE.read_text(encoding="utf-8"))
    assert match, "the override no longer sets `anchor` - did the template change?"
    return match.group(1)


def test_override_exists():
    """Without it Zensical renders inert <span> chips."""
    assert TEMPLATE.is_file()


def test_template_builds_the_anchor_from_the_tags_page():
    expr = _template_slug_expression()
    assert '"tags/" | url' in expr, "link must be relative, for mike's versioned prefixes"
    assert '"#tag:"' in expr


def test_template_slug_rules_match_tag_slug():
    """lower-case and spaces to hyphens - the same two rules as tag_slug()."""
    expr = _template_slug_expression()
    assert "| lower" in expr
    assert '| replace(" ", "-")' in expr


@pytest.mark.parametrize(
    "tag",
    ["Load Balancer", "Application View", "Graph-Insights", "API", "cmemc", "TransformOperator"],
)
def test_python_slug_agrees_with_the_template_rules(tag):
    """Mirror of the MiniJinja expression, applied to the tags that stress it."""
    assert rtl.tag_slug(tag) == "tag:" + tag.lower().replace(" ", "-")


def test_multiword_tags_are_the_case_that_actually_breaks():
    """Dropping the replace() only shows up on tags containing a space."""
    assert rtl.tag_slug("Load Balancer") == "tag:load-balancer"
    assert rtl.tag_slug("Load Balancer") != "tag:load balancer"
