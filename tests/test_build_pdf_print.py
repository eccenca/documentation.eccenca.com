"""Test the print edition's section modes: full, list and omit"""
import click
import pytest

from tools.build_pdf import (
    Generated,
    NavEntry,
    SectionRule,
    apply_section_rules,
    load_section_rules,
    md_to_built_html,
    merge_pages,
)

REFERENCE = [
    NavEntry(0, "build/index.md"),
    NavEntry(1, "build/reference/index.md"),
    NavEntry(2, "build/reference/aggregator/index.md"),
    NavEntry(3, "build/reference/aggregator/average.md"),
    NavEntry(2, "build/reference/transformer/index.md"),
    NavEntry(3, "build/reference/transformer/Numeric/index.md"),
    NavEntry(4, "build/reference/transformer/Numeric/add.md"),
    NavEntry(1, "build/spark.md"),
]

# The shape of Release Notes in nav.yml: no page stands for the section or its years.
RELEASES = [
    NavEntry(0, title="Release Notes"),
    NavEntry(1, title="2026"),
    NavEntry(2, "release-notes/2026/cm-26-2/index.md"),
    NavEntry(2, "release-notes/2026/cm-26-1/index.md"),
    NavEntry(1, title="2025"),
    NavEntry(2, "release-notes/2025/cm-25-3/index.md"),
    NavEntry(0, "tutorials/index.md"),
]

# The shape of Transformers in nav.yml: the overview page lists every operator,
# and the categories are titles without a page.
CATEGORIES = [
    NavEntry(1, "build/reference/index.md", "Task and Operator Reference"),
    NavEntry(2, "build/reference/transformer/index.md", "Transformers"),
    NavEntry(3, title="Combine"),
    NavEntry(4, "build/reference/transformer/Combine/concat.md", "Concatenate"),
    NavEntry(4, "build/reference/transformer/Combine/zip.md", "Zip"),
    NavEntry(3, title="Date"),
    NavEntry(4, "build/reference/transformer/Date/duration.md"),
    NavEntry(1, "build/spark.md", "Spark"),
]
CATEGORY_TABLE = Generated(
    "groups", "build/reference/", "list", columns=("Category", "Transformers"),
    groups=[("Combine", [CATEGORIES[3], CATEGORIES[4]]), ("Date", [CATEGORIES[6]])],
)


def test_rules_read_a_mode_or_a_mapping_with_columns(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text(
        "sections:\n"
        "  build/reference/: list\n"
        "  release-notes:\n"
        "    mode: list\n"
        "    columns: [Release, Summary]\n"
        "  tutorials/: full\n"
    )
    assert load_section_rules(path) == [
        SectionRule("build/reference/", "list"),
        SectionRule("release-notes/", "list", ("Release", "Summary")),
        SectionRule("tutorials/", "full"),
    ]


def test_an_unknown_mode_fails(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("sections:\n  build/: shorten\n")
    with pytest.raises(click.ClickException, match="shorten"):
        load_section_rules(path)


def test_list_keeps_the_overview_pages_and_drops_what_they_list():
    entries, dropped = apply_section_rules(REFERENCE, [SectionRule("build/reference/", "list")])
    assert entries == [
        NavEntry(0, "build/index.md"),
        NavEntry(1, "build/reference/index.md"),
        NavEntry(1, generated=Generated("note", "build/reference/", "list", ["build/reference/index.md"])),
        NavEntry(2, "build/reference/aggregator/index.md"),
        NavEntry(2, "build/reference/transformer/index.md"),
        NavEntry(1, "build/spark.md"),
    ]
    assert dropped == {
        "build/reference/aggregator/average.md",
        "build/reference/transformer/Numeric/index.md",
        "build/reference/transformer/Numeric/add.md",
    }


def test_list_without_overview_pages_makes_a_table_under_each_heading():
    rule = SectionRule("release-notes/", "list", ("Release", "Summary"))
    entries, dropped = apply_section_rules(RELEASES, [rule])
    first = "release-notes/2026/cm-26-2/index.md"
    assert entries == [
        NavEntry(0, title="Release Notes"),
        NavEntry(1, generated=Generated("note", "release-notes/", "list", [first], name="Release Notes")),
        NavEntry(1, title="2026"),
        NavEntry(2, generated=Generated(
            "table", "release-notes/", "list", [first, "release-notes/2026/cm-26-1/index.md"], ("Release", "Summary")
        )),
        NavEntry(1, title="2025"),
        NavEntry(2, generated=Generated(
            "table", "release-notes/", "list", ["release-notes/2025/cm-25-3/index.md"], ("Release", "Summary")
        )),
        NavEntry(0, "tutorials/index.md"),
    ]
    assert len(dropped) == 3


def test_list_turns_the_titles_an_overview_empties_into_one_table():
    entries, dropped = apply_section_rules(CATEGORIES, [SectionRule("build/reference/", "list")])
    assert entries == [
        CATEGORIES[0],
        NavEntry(1, generated=Generated("note", "build/reference/", "list", ["build/reference/index.md"])),
        CATEGORIES[1],
        NavEntry(3, generated=CATEGORY_TABLE),
        CATEGORIES[7],
    ]
    assert dropped == {CATEGORIES[3].md, CATEGORIES[4].md, CATEGORIES[6].md}


def test_omit_drops_the_pages_and_leaves_a_heading_with_a_note():
    entries, dropped = apply_section_rules(REFERENCE, [SectionRule("build/reference/", "omit")])
    assert entries == [
        NavEntry(0, "build/index.md"),
        NavEntry(1, generated=Generated("note", "build/reference/", "omit", ["build/reference/index.md"])),
        NavEntry(1, "build/spark.md"),
    ]
    assert len(dropped) == 6


def test_omitting_a_whole_part_without_a_page_leaves_nothing_of_it():
    entries, dropped = apply_section_rules(RELEASES, [SectionRule("release-notes/", "omit")])
    assert entries == [NavEntry(0, "tutorials/index.md")]
    assert len(dropped) == 3


def test_full_changes_nothing():
    assert apply_section_rules(RELEASES, [SectionRule("release-notes/", "full")]) == (RELEASES, set())


def test_a_section_without_pages_in_the_navigation_fails():
    with pytest.raises(click.ClickException, match="build/nothing/"):
        apply_section_rules(REFERENCE, [SectionRule("build/nothing/", "list")])


def write_page(site, md, body):
    path = site / md_to_built_html(md)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'<html><body><article class="md-content__inner">{body}</article></body></html>')


def test_merge_renders_notes_and_tables_and_unlinks_what_the_section_drops(tmp_path):
    site = tmp_path / "site"
    write_page(site, "build/reference/index.md", '<h1 id="ref">Task and Operator Reference</h1><p>All operators.</p>')
    write_page(
        site, "build/reference/aggregator/index.md",
        '<h1 id="agg">Aggregators</h1><table><tr><td><a href="average/">Average</a></td></tr></table>'
        '<p>See <a href="../../spark/">Spark</a>.</p>',
    )
    write_page(
        site, "release-notes/2026/cm-26-2/index.md",
        '<h1 id="r">Corporate Memory 26.2.1</h1><p>The second <a href="x/">major</a> release.</p>'
        '<h2 id="di">DataIntegration v26.2.0</h2>',
    )
    write_page(
        site, "release-notes/2026/cm-26-1/index.md",
        '<h1 id="r">Corporate Memory 26.1.3</h1><div>no paragraph</div>'
        '<h2 id="di">DataIntegration v26.1.0</h2><h2 id="ex">Explore v26.1.3</h2>',
    )
    first, second = "release-notes/2026/cm-26-2/index.md", "release-notes/2026/cm-26-1/index.md"
    entries = [
        NavEntry(1, "build/reference/index.md"),
        NavEntry(1, generated=Generated("note", "build/reference/", "list", ["build/reference/index.md"])),
        NavEntry(2, "build/reference/aggregator/index.md"),
        NavEntry(0, title="Release Notes"),
        NavEntry(1, generated=Generated("note", "release-notes/", "list", [first], name="Release Notes")),
        NavEntry(1, title="2026"),
        NavEntry(2, generated=Generated("table", "release-notes/", "list", [first, second], ("Release", "Summary"))),
    ]
    rules = [SectionRule("build/reference/", "list"), SectionRule("release-notes/", "list", ("Release", "Summary"))]
    dropped = {"build/reference/aggregator/average.md", first, second}
    doc, missing = merge_pages(entries, site, "https://example.org/26.2/", rules, dropped)
    assert missing == []
    html = str(doc.body)
    text = " ".join(doc.body.get_text(" ").split())

    # The overview's link to a dropped operator page prints as its text; a link
    # to a page outside the print edition still leads to the published site.
    assert "<td>Average</td>" in html
    assert 'href="https://example.org/26.2/build/spark/"' in html

    # A note names the section and where it is complete: the section's own URL
    # when it has a page, else the first page it lists.
    assert (
        "This print edition lists the Task and Operator Reference in short. The complete section is part of "
        "the online edition: https://example.org/26.2/build/reference/"
    ) in text
    assert (
        "This print edition lists the Release Notes in short. The complete section is part of the online "
        "edition: https://example.org/26.2/release-notes/2026/cm-26-2/"
    ) in text

    # The table: each page's title and first paragraph, without links; a page
    # without a paragraph is summarized by its headings.
    table = doc.find("table", class_="print-list")
    rows = [[cell.get_text(" ", strip=True) for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")]
    assert rows == [
        ["Release", "Summary"],
        ["Corporate Memory 26.2.1", "The second major release."],
        ["Corporate Memory 26.1.3", "DataIntegration v26.1.0, Explore v26.1.3"],
    ]
    assert table.find("a") is None


def test_merge_renders_the_emptied_titles_as_one_table_of_their_pages(tmp_path):
    site = tmp_path / "site"
    write_page(site, "build/reference/transformer/Date/duration.md", '<h1 id="d">Duration</h1>')
    doc, _ = merge_pages([NavEntry(3, generated=CATEGORY_TABLE)], site, "https://example.org/26.2/")
    table = doc.find("table", class_="print-list")
    rows = [[cell.get_text(" ", strip=True) for cell in row.find_all(["th", "td"])] for row in table.find_all("tr")]
    # A page without a navigation title is named by its own title.
    assert rows == [
        ["Category", "Transformers"],
        ["Combine", "Concatenate, Zip"],
        ["Date", "Duration"],
    ]
    assert doc.body.find(["h1", "h2", "h3", "h4", "h5", "h6"]) is None
    # Without an alignment pandoc would centre the cells.
    assert {cell.get("style") for cell in table.find_all(["th", "td"])} == {"text-align: left;"}


def test_merge_renders_an_omitted_section_as_its_title_and_a_note(tmp_path):
    site = tmp_path / "site"
    write_page(site, "build/reference/index.md", '<h1 id="ref">Task and Operator Reference</h1>')
    entries = [NavEntry(1, generated=Generated("note", "build/reference/", "omit", ["build/reference/index.md"]))]
    doc, _ = merge_pages(entries, site, "https://example.org/26.2/", [SectionRule("build/reference/", "omit")], set())
    assert doc.body.find("h2").get_text() == "Task and Operator Reference"
    assert (
        "The Task and Operator Reference is not part of this print edition. It is part of the online edition: "
        "https://example.org/26.2/build/reference/"
    ) in " ".join(doc.body.get_text(" ").split())
