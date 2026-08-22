"""Test update DI references"""
import pytest

from tools.update_di_reference import (
    PluginDescription,
    PluginReference,
    RelatedPluginReferenceError,
    get_plugin_descriptions,
    resolve_related_plugin_links,
    create_plugin_markdown,
    build_plugin_paths,
    validate_related_plugin_references,
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
    "current_path, target_path, expected",
    [
        # same type, different category
        ("transformer/Extract/regexExtract.md", "transformer/Replace/regexReplace.md", "../Replace/regexReplace.md"),
        # different type entirely
        ("transformer/Extract/regexExtract.md", "aggregator/average.md", "../../aggregator/average.md"),
        # reverse: shallower page linking to a deeper one
        ("aggregator/average.md", "transformer/Extract/regexExtract.md", "../transformer/Extract/regexExtract.md"),
        # same directory
        ("customtask/sparqlSelectOperator.md", "customtask/sparqlUpdateOperator.md", "sparqlUpdateOperator.md"),
    ],
)
def test_resolve_related_plugin_links_path_shapes(current_path, target_path, expected):
    ref = PluginReference(id="target")
    plugin = _make_plugin("current", related=[ref])
    plugin_paths = {"current": current_path, "target": target_path}
    assert resolve_related_plugin_links(plugin, current_path, plugin_paths) == [(ref, expected)]


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
    with pytest.raises(RelatedPluginReferenceError, match="deprecatedPlugin"):
        resolve_related_plugin_links(plugin, "transformer/Extract/regexExtract.md", {"regexExtract": "transformer/Extract/regexExtract.md"})


def test_build_plugin_paths():
    plugins = {
        "transformer": [_make_plugin("regexExtract", plugin_type="transformer", main_category="Extract")],
        "dataset": [_make_plugin("sparqlEndpoint", plugin_type="dataset")],
        "customtask": [_make_plugin("deprecatedPlugin", plugin_type="customtask")],
    }
    paths = build_plugin_paths(plugins)
    assert paths == {
        "regexExtract": "transformer/Extract/regexExtract.md",
        "sparqlEndpoint": "dataset/sparqlEndpoint.md",
    }
    assert "deprecatedPlugin" not in paths


def test_validate_related_plugin_references_passes_when_all_resolve():
    plugins = {
        "transformer": [_make_plugin("regexExtract", related=[PluginReference(id="regexReplace")])],
    }
    plugin_paths = {
        "regexExtract": "transformer/Extract/regexExtract.md",
        "regexReplace": "transformer/Replace/regexReplace.md",
    }
    validate_related_plugin_references(plugins, plugin_paths)


def test_validate_related_plugin_references_raises_on_unresolvable():
    plugins = {
        "transformer": [_make_plugin("regexExtract", related=[PluginReference(id="removedPlugin")])],
    }
    plugin_paths = {"regexExtract": "transformer/Extract/regexExtract.md"}
    with pytest.raises(RelatedPluginReferenceError, match="removedPlugin"):
        validate_related_plugin_references(plugins, plugin_paths)


def test_validate_related_plugin_references_skips_deprecated_plugins():
    plugins = {
        "customtask": [_make_plugin("deprecatedPlugin", plugin_type="customtask", related=[PluginReference(id="removedPlugin")])],
    }
    validate_related_plugin_references(plugins, plugin_paths={})


def test_create_plugin_markdown_writes_resolved_links(tmp_path):
    plugin = _make_plugin(
        "sparqlSelectOperator",
        plugin_type="customtask",
        related=[PluginReference(id="sparqlEndpoint", description="a SPARQL endpoint dataset")],
    )
    plugin_paths = {
        "sparqlSelectOperator": "customtask/sparqlSelectOperator.md",
        "sparqlEndpoint": "dataset/sparqlEndpoint.md",
    }

    create_plugin_markdown(plugin, tmp_path, plugin_paths)

    written = (tmp_path / "customtask" / "sparqlSelectOperator.md").read_text()
    assert "[sparqlEndpoint](../dataset/sparqlEndpoint.md)" in written
    assert "**sparqlEndpoint**" not in written
    assert "[sparqlEndpoint](../dataset/sparqlEndpoint.md) — a SPARQL endpoint dataset" in written


@pytest.mark.parametrize(
    "plugin_id, plugin_path, related_id, related_path, expected_link",
    [
        # same type, different category
        ("regexExtract", "transformer/Extract/regexExtract.md", "regexReplace", "transformer/Replace/regexReplace.md", "../Replace/regexReplace.md"),
        # reverse: shallower page linking to a deeper one
        ("average", "aggregator/average.md", "regexExtract", "transformer/Extract/regexExtract.md", "../transformer/Extract/regexExtract.md"),
        # same directory
        ("sparqlSelectOperator", "customtask/sparqlSelectOperator.md", "sparqlUpdateOperator", "customtask/sparqlUpdateOperator.md", "sparqlUpdateOperator.md"),
    ],
)
def test_create_plugin_markdown_link_path_shapes(tmp_path, plugin_id, plugin_path, related_id, related_path, expected_link):
    plugin = _make_plugin(plugin_id, related=[PluginReference(id=related_id)])
    plugin_paths = {plugin_id: plugin_path, related_id: related_path}

    create_plugin_markdown(plugin, tmp_path, plugin_paths)

    written = (tmp_path / plugin_path).read_text()
    assert f"[{related_id}]({expected_link})" in written


def test_create_plugin_markdown_writes_multiple_resolved_links(tmp_path):
    plugin = _make_plugin(
        "regexExtract",
        plugin_type="transformer",
        main_category="Extract",
        related=[PluginReference(id="regexReplace"), PluginReference(id="regexSelect")],
    )
    plugin_paths = {
        "regexExtract": "transformer/Extract/regexExtract.md",
        "regexReplace": "transformer/Replace/regexReplace.md",
        "regexSelect": "transformer/Selection/regexSelect.md",
    }

    create_plugin_markdown(plugin, tmp_path, plugin_paths)

    written = (tmp_path / "transformer" / "Extract" / "regexExtract.md").read_text()
    assert "[regexReplace](../Replace/regexReplace.md)" in written
    assert "[regexSelect](../Selection/regexSelect.md)" in written


def test_create_plugin_markdown_omits_description_when_absent(tmp_path):
    plugin = _make_plugin(
        "sparqlSelectOperator",
        plugin_type="customtask",
        related=[PluginReference(id="sparqlEndpoint")],
    )
    plugin_paths = {
        "sparqlSelectOperator": "customtask/sparqlSelectOperator.md",
        "sparqlEndpoint": "dataset/sparqlEndpoint.md",
    }

    create_plugin_markdown(plugin, tmp_path, plugin_paths)

    written = (tmp_path / "customtask" / "sparqlSelectOperator.md").read_text()
    assert "[sparqlEndpoint](../dataset/sparqlEndpoint.md)" in written
    assert "[sparqlEndpoint](../dataset/sparqlEndpoint.md) —" not in written


def test_create_plugin_markdown_omits_section_when_no_related_plugins(tmp_path):
    plugin = _make_plugin("regexExtract", plugin_type="transformer", main_category="Extract", related=[])
    plugin_paths = {"regexExtract": "transformer/Extract/regexExtract.md"}

    create_plugin_markdown(plugin, tmp_path, plugin_paths)

    written = (tmp_path / "transformer" / "Extract" / "regexExtract.md").read_text()
    assert "Related Plugins" not in written
