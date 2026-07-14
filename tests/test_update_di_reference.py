"""Test update DI references"""
import pytest

from tools.update_di_reference import (
    PluginDescription,
    PluginReference,
    get_plugin_descriptions,
    resolve_related_plugin_links,
    _relative_link,
    _shared_prefix_length,
    create_plugin_markdown,
)


@pytest.mark.integration
def test_get_plugin_descriptions():
    """Test get DI plugin descriptions"""
    descriptions = get_plugin_descriptions()
    assert set(descriptions.keys()) == {"customtask", "dataset", "distancemeasure", "transformer", "aggregator"}
    assert len(descriptions["transformer"]) > 0
    assert len(descriptions["dataset"]) > 0
    for plugin_type, plugins in descriptions.items():
        for plugin in plugins:
            assert isinstance(plugin, PluginDescription)
            assert plugin.pluginType == plugin_type
        titles = [p.title.lower() for p in plugins]
        assert titles == sorted(titles)


def _make_plugin(plugin_id, plugin_type="transformer", main_category="Extract", related=None):
    """Build a minimal valid PluginDescription for a test, filling in only what varies."""
    return PluginDescription(
        pluginId=plugin_id,
        title=plugin_id,
        categories=[main_category],
        description="test plugin",
        properties={},
        actions={},
        required=[],
        backendType="scala",
        pluginType=plugin_type,
        relatedPlugins=related or [],
    )


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (("customtask",), ("dataset",), 0),
        (("transformer", "Extract"), ("transformer", "Extract"), 2),
        (("transformer", "Extract"), ("transformer", "Replace"), 1),
        ((), ("dataset",), 0),
        (("transformer", "Extract"), ("transformer",), 1),
    ],
)
def test_shared_prefix_length(a, b, expected):
    assert _shared_prefix_length(a, b) == expected


@pytest.mark.parametrize(
    "current_dir_parts, target_path, expected",
    [
        # same type, different category
        (("transformer", "Extract"), "transformer/Replace/regexReplace.md", "../Replace/regexReplace.md"),
        # different type entirely
        (("transformer", "Extract"), "aggregator/average.md", "../../aggregator/average.md"),
        # reverse: shallower page linking to a deeper one
        (("aggregator",), "transformer/Extract/regexExtract.md", "../transformer/Extract/regexExtract.md"),
        # same directory
        (("customtask",), "customtask/sparqlUpdateOperator.md", "sparqlUpdateOperator.md"),
    ],
)
def test_relative_link(current_dir_parts, target_path, expected):
    assert _relative_link(current_dir_parts, target_path) == expected


def test_resolve_related_plugin_links_empty():
    plugin = _make_plugin("regexExtract", related=[])
    assert resolve_related_plugin_links(plugin, "transformer/Extract/regexExtract.md", {}) == []


def test_resolve_related_plugin_links_single():
    ref = PluginReference(id="regexReplace", description="replaces text")
    plugin = _make_plugin("regexExtract", related=[ref])
    plugin_paths = {"regexExtract": "transformer/Extract/regexExtract.md", "regexReplace": "transformer/Replace/regexReplace.md"}
    resolved = resolve_related_plugin_links(plugin, "transformer/Extract/regexExtract.md", plugin_paths)
    assert resolved == [(ref, "../Replace/regexReplace.md")]


def test_resolve_related_plugin_links_multiple_preserves_order():
    ref_a = PluginReference(id="regexReplace")
    ref_b = PluginReference(id="regexSelect")
    plugin = _make_plugin("regexExtract", related=[ref_a, ref_b])
    plugin_paths = {
        "regexExtract": "transformer/Extract/regexExtract.md",
        "regexReplace": "transformer/Replace/regexReplace.md",
        "regexSelect": "transformer/Selection/regexSelect.md",
    }
    resolved = resolve_related_plugin_links(plugin, "transformer/Extract/regexExtract.md", plugin_paths)
    assert [ref for ref, _ in resolved] == [ref_a, ref_b]


def test_resolve_related_plugin_links_unresolvable_raises():
    ref = PluginReference(id="deprecatedPlugin")
    plugin = _make_plugin("regexExtract", related=[ref])
    with pytest.raises(Exception, match="deprecatedPlugin"):
        resolve_related_plugin_links(plugin, "transformer/Extract/regexExtract.md", {"regexExtract": "transformer/Extract/regexExtract.md"})


def test_create_plugin_markdown_writes_resolved_links(tmp_path):
    target = _make_plugin("sparqlEndpoint", plugin_type="dataset")
    plugin = _make_plugin(
        "sparqlSelectOperator",
        plugin_type="customtask",
        related=[PluginReference(id="sparqlEndpoint", description="a SPARQL endpoint dataset")],
    )
    plugin_paths = {
        "sparqlSelectOperator": "customtask/sparqlSelectOperator.md",
        "sparqlEndpoint": "dataset/sparqlEndpoint.md",
    }

    create_plugin_markdown(plugin, "customtask", tmp_path, plugin_paths)

    written = (tmp_path / "customtask" / "sparqlSelectOperator.md").read_text()
    assert "[sparqlEndpoint](../dataset/sparqlEndpoint.md)" in written
    assert "**sparqlEndpoint**" not in written
