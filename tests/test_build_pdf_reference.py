"""Test the compact operator reference of the print edition (tasks/spec.md, §11, D17)"""
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

RULE = SectionRule("build/reference/", "reference")
PUBLIC = "https://example.org/26.2/"


def operator(plugin_id, plugin_type="transformer", title=None, category="Value", **extra):
    """A plugin description as data/plugins.json holds it, filled in only where a test needs it."""
    record = {
        "pluginId": plugin_id,
        "title": title or plugin_id,
        "pluginType": plugin_type,
        "main_category": category,
        "categories": [category],
        "description": f"{plugin_id} description",
        "markdownDocumentation": None,
        "backendType": "scala",
        "distanceMeasureRange": None,
        "properties": {},
        "properties_advanced": {},
        "relatedPlugins": [],
        "is_deprecated": False,
    }
    record.update(extra)
    return record


def parameter(name, title, parameter_type="string", value="", description="", advanced=False, properties=None):
    return {
        "name": name,
        "title": title,
        "description": description,
        "type": "string",
        "parameterType": parameter_type,
        "value": value,
        "advanced": advanced,
        "visibleInDialog": True,
        "properties": properties or {},
    }


def write_page(site, md, body):
    path = site / md_to_built_html(md)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'<html><body><article class="md-content__inner">{body}</article></body></html>')


# The shape of the reference in nav.yml: a page per type, transformers grouped by category.
NAV = [
    NavEntry(0, "build/index.md", "Build"),
    NavEntry(1, "build/reference/index.md", "Task and Operator Reference"),
    NavEntry(2, "build/reference/aggregator/index.md", "Aggregators"),
    NavEntry(3, "build/reference/aggregator/max.md", "Maximum"),
    NavEntry(2, "build/reference/transformer/index.md", "Transformers"),
    NavEntry(3, title="Value"),
    NavEntry(4, "build/reference/transformer/Value/uuid.md", "UUID"),
    NavEntry(4, "build/reference/transformer/Value/constant.md", "Constant"),
    NavEntry(1, "build/spark.md", "Spark"),
]
OPERATORS = [operator("uuid", title="UUID"), operator("constant", title="Constant"), operator("max", "aggregator", title="Maximum")]
CATALOG = {
    "uuid": ("build/reference/transformer/Value/uuid.md", "UUID"),
    "constant": ("build/reference/transformer/Value/constant.md", "Constant"),
    "max": ("build/reference/aggregator/max.md", "Maximum"),
}


def test_reference_is_a_mode_for_a_directory_only(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("sections:\n  build/reference/: reference\n")
    assert load_section_rules(path) == [RULE]
    path.write_text("sections:\n  build/reference/index.md: reference\n")
    with pytest.raises(click.ClickException, match="only `omit`"):
        load_section_rules(path)


def test_the_operators_of_a_type_follow_its_overview_page_in_alphabetical_order():
    entries, dropped = apply_section_rules(NAV, [RULE], operators=OPERATORS)
    assert entries == [
        NAV[0],
        NAV[1],
        NavEntry(1, generated=Generated("note", "build/reference/", "reference", ["build/reference/index.md"])),
        NAV[2],
        NavEntry(3, generated=Generated(
            "operators", "build/reference/", "reference", [CATALOG["max"][0]],
            operators=[OPERATORS[2]], catalog=CATALOG,
        )),
        NAV[4],
        # The category heading is gone: the category is a field of the entry.
        NavEntry(3, generated=Generated(
            "operators", "build/reference/", "reference", [CATALOG["constant"][0], CATALOG["uuid"][0]],
            operators=[OPERATORS[1], OPERATORS[0]], catalog=CATALOG,
        )),
        NAV[8],
    ]
    # The operator pages print, as entries - none is dropped.
    assert dropped == set()


def test_the_build_fails_when_the_pages_and_the_operators_disagree():
    with pytest.raises(click.ClickException) as raised:
        apply_section_rules(NAV, [RULE], operators=OPERATORS[1:] + [operator("zip", title="Zip")])
    assert "transformer/Value/uuid.md" in raised.value.message
    assert "zip" in raised.value.message


def test_an_operator_entry_is_compact(tmp_path):
    site = tmp_path / "site"
    write_page(
        site, "build/reference/transformer/index.md",
        '<h1 id="t">Transformers</h1><p>Transform values.</p><table><tr><td>Overview row</td></tr></table>',
    )
    write_page(
        site, "build/reference/transformer/Value/constant.md",
        '<h1 id="constant">Constant</h1>'
        '<div class="admonition note inline end"><p class="admonition-title">Python Plugin</p>'
        "<p>This operator is part of a Python Plugin Package.</p></div>"
        '<p>Generates a constant value. See <a href="../../../../spark/">Spark</a>.</p>'
        '<h2 id="characteristics">Characteristics</h2><p>Compares single values.</p>'
        '<h2 id="examples">Examples</h2><p>Returns [John].</p><hr/><ul><li>Returns: John</li></ul>'
        '<h2 id="parameter">Parameter</h2><h3 id="value">Value</h3><p>The constant value</p>'
        '<h2 id="advanced-parameter">Advanced Parameter</h2><p>None</p>'
        '<h2 id="related-plugins">Related Plugins</h2><ul><li>UUID</li></ul>',
    )
    write_page(site, "build/reference/transformer/Value/uuid.md", '<h1 id="uuid">UUID</h1><p>Generates a UUID.</p>')
    constant = operator(
        "constant", title="Constant", backendType="python",
        properties={
            "value": parameter("value", "Value", description="The constant `value`"),
            "secret": parameter("secret", "Secret", "password", value="PASSWORD_PARAMETER:x"),
            "connection": parameter(
                "connection", "Connection", "objectParameter", value={"parameters": {"host": "localhost"}},
                properties={"host": parameter("host", "Host", value="localhost")},
            ),
        },
        properties_advanced={
            "query": parameter("query", "Query", "code-sparql", value="SELECT *\nWHERE {}", advanced=True),
            "count": parameter("count", "Count", "Long", value="5", advanced=True),
        },
        relatedPlugins=[{"id": "uuid", "description": "Makes an identifier."}],
    )
    uuid = operator("uuid", title="UUID")
    entries = [
        NavEntry(2, "build/reference/transformer/index.md", "Transformers"),
        NavEntry(3, generated=Generated(
            "operators", "build/reference/", "reference", [CATALOG["constant"][0], CATALOG["uuid"][0]],
            operators=[constant, uuid], catalog=CATALOG,
        )),
    ]
    doc, missing, _ = merge_pages(entries, site, PUBLIC, [RULE], set(), print_edition=True)
    assert missing == []
    text = " ".join(doc.body.get_text(" ").split())

    # The overview keeps its introduction; its table gives way to the entries.
    assert "Transform values." in text and "Overview row" not in text
    assert [(h.name, h.get_text()) for h in doc.body.find_all(["h3", "h4", "h5"])] == [
        ("h3", "Transformers"), ("h4", "Constant"), ("h4", "UUID"),
    ]

    fields = doc.body.find_all("div", class_="operator-fields")
    assert [" ".join(f.get_text(" ").split()) for f in fields] == [
        "Transformer · Value · constant · Python plugin",
        "Transformer · Value · uuid",
    ]

    # The description: without the Python plugin note and the examples, its own
    # headings as run-in labels, its links resolved like any page's.
    assert "Python Plugin Package" not in text and "Returns" not in text
    assert doc.body.find("strong", string="Characteristics") is not None
    assert doc.body.find("a", string="Spark")["href"] == f"{PUBLIC}build/spark/"

    # One table, for Constant only: UUID has no parameters.
    tables = doc.body.find_all("table")
    assert len(tables) == 1
    rows = [[" ".join(c.get_text(" ").split()) for c in row.find_all(["th", "td"])] for row in tables[0].find_all("tr")]
    assert rows == [
        ["Parameter", "Type", "Default", "Description"],
        ["Value value", "text", "–", "The constant value"],
        ["Secret secret", "password", "–", ""],
        ["Connection connection", "group", "–", ""],
        ["Host connection.host", "text", "localhost", ""],
        ["Advanced"],
        ["Query query", "SPARQL", "see below", ""],
        ["Count count", "integer", "5", ""],
    ]
    default = doc.body.find("pre")
    assert "SELECT *" in default.get_text()
    assert default.find_previous("p").get_text() == "Default of query:"

    related = doc.body.find("p", class_="operator-related")
    assert " ".join(related.get_text(" ").split()) == "Related: UUID"
    assert related.find("a")["href"] == "#build-reference-transformer-Value-uuid"


def test_the_reference_opens_with_a_note_on_what_an_entry_shows(tmp_path):
    site = tmp_path / "site"
    write_page(site, "build/reference/index.md", '<h1 id="r">Task and Operator Reference</h1>')
    note = Generated("note", "build/reference/", "reference", ["build/reference/index.md"])
    doc, _, _ = merge_pages([NavEntry(1, generated=note)], site, PUBLIC, [RULE], set(), print_edition=True)
    text = " ".join(doc.body.get_text(" ").split())
    assert "every operator of the Task and Operator Reference with its description and parameters" in text
    assert f"The examples are part of the online edition: {PUBLIC}build/reference/" in text
    assert "Python plugin" in text
