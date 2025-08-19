"""Update DI Reference documentation"""

import json
import re
from contextlib import suppress
from pathlib import Path
from shutil import rmtree
from typing import List, Annotated, Self

import click
from cmem.cmempy import config
from cmem.cmempy.api import send_request
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined
from pydantic import (
    BaseModel,
    AfterValidator,
    model_validator,
    Field,
)

jinja_environment = Environment(
    loader=PackageLoader("tools"),
    autoescape=select_autoescape(),
    undefined=StrictUndefined
)

def stripped_single_line(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()

class ActionDescription(BaseModel):
    """Action description"""

    label: str
    description: str
    icon: str | None = None


class PropertyDescription(BaseModel):
    """Property description"""

    name: str
    title: str
    description: Annotated[str, AfterValidator(stripped_single_line)]
    type: str
    parameterType: str
    value: str | None | dict
    advanced: bool
    visibleInDialog: bool
    properties: dict[str, dict] = {}

    def get_pygments_code(self) -> str:
        """Get a markdown pygments code based on the parameterType

        https://pygments.org/docs/lexers/
        """
        codes = {
            "code-json": "json",
            "code-python": "python",
            "code-yaml": "yaml",
            "code-sql": "sql",
            "code-sparql": "sparql",
        }
        return codes.get(self.parameterType, "text")


class PluginDescription(BaseModel):
    """Plugin description."""

    pluginId: str
    title: str
    categories: List[str]
    main_category: str | None = None
    description: Annotated[str, AfterValidator(stripped_single_line)]
    markdownDocumentation: str | None = None
    pluginIcon: str | None = None
    properties: dict[str, PropertyDescription]
    properties_advanced: dict[str, PropertyDescription] = Field(default_factory=dict)
    actions: dict[str, ActionDescription]
    required: list[str]
    distanceMeasureRange: str | None = None
    backendType: str
    is_deprecated: bool | None = None
    tags: list[str] = Field(default_factory=list)
    pluginType: str | None = None

    @model_validator(mode="after")
    def move_advanced_properties(self) -> Self:
        """move advanced properties to advanced_properties"""
        self.properties_advanced = {property.name: property for property in self.properties.values() if property.advanced}
        self.properties = {property.name: property for property in self.properties.values() if not property.advanced}
        return self

    @model_validator(mode="after")
    def create_main_category(self) -> Self:
        """main_category is used for transformer navigation"""
        with suppress(ValueError):
            self.categories.remove("Recommended")
        try:
            self.main_category = self.categories[0]
        except IndexError:
            self.main_category = "Uncategorized"
        return self

    @model_validator(mode="after")
    def check_tags(self) -> Self:
        if self.pluginType == "customtask":
            self.tags.append("WorkflowTask")
        if self.pluginType == "dataset":
            self.tags.append("Dataset")
        if self.pluginType == "distancemeasure":
            self.tags.append("DistanceMeasure")
        if self.pluginType == "transformer":
            self.tags.append("TransformOperator")
        if self.backendType == "python":
            self.tags.append("PythonPlugin")
        return self

    @model_validator(mode="after")
    def set_deprecated(self) -> Self:
        self.is_deprecated = False
        if "deprecated" in self.title:
            self.is_deprecated = True
        if "deprecated" in self.description:
            self.is_deprecated = True
        if "deprecated" in self.categories:
            self.is_deprecated = True
        return self


def get_plugin_descriptions() -> dict[str, list[PluginDescription]]:
    """Return list of plugin descriptions."""
    plugin_types = [
        "org.silkframework.config.CustomTask",
        "org.silkframework.dataset.Dataset",
        "org.silkframework.rule.similarity.DistanceMeasure",
        "org.silkframework.rule.input.Transformer",
        "org.silkframework.rule.similarity.Aggregator"
    ]
    plugins = {}
    for plugin_type in plugin_types:
        type_id = plugin_type.split(".")[-1].lower()
        response = send_request(
            config.get_di_api_endpoint() + f"/core/plugins/{plugin_type}",
            params={"addMarkdownDocumentation": "true"}
        )
        plugins_dict = json.loads(response.decode("utf-8"))
        plugins_of_type = []
        for plugin_dict in plugins_dict.values():
            plugin_dict["pluginType"] = type_id
            plugin = PluginDescription(**plugin_dict)
            plugins_of_type.append(plugin)
        plugins_of_type.sort(key=lambda p: p.title.lower())
        plugins[type_id] = plugins_of_type
    return plugins

def create_plugin_markdown(plugin: PluginDescription, plugin_type: str, base_dir: Path) -> None:
    """Create markdown document from plugin description."""
    if plugin.is_deprecated:
        click.echo(f"Ignore deprecated plugin {plugin.pluginId}")
        return
    click.echo(f"Create reference documentation for {plugin.pluginId}")

    # create content
    plugin_template = jinja_environment.get_template(f"plugin.md")
    parameter_template = jinja_environment.get_template(f"parameter.md")
    parameter_content = ""
    for _ in plugin.properties.values():
        parameter_content += parameter_template.render(property=_) + "\n\n"

    parameter_advanced_content = ""
    for _ in plugin.properties_advanced.values():
        parameter_advanced_content += parameter_template.render(property=_) + "\n\n"

    content = plugin_template.render(
        plugin=plugin,
        parameters=parameter_content,
        parameters_advanced=parameter_advanced_content,
    )

    # create the file (incl. directory)
    if plugin.pluginType == "transformer":
        directory = base_dir / plugin_type / plugin.main_category
    else:
        directory = base_dir / plugin_type
    directory.mkdir(parents=True, exist_ok=True)
    file = directory / f"{plugin.pluginId}.md"
    with file.open("w", encoding="utf-8") as f:
        f.write(content)

def create_umbrella_pages(plugins: dict[str, list[PluginDescription]], base_dir: Path) -> None:
    """Create umbrellas markdown documents"""
    reference_base_template = jinja_environment.get_template("references_base.md")
    reference_base_file = base_dir / f"index.md"
    with reference_base_file.open("w", encoding="utf-8") as f:
        click.echo(f"Create the main index.md file: {reference_base_file}")
        f.write(reference_base_template.render())

    # Create the main .pages file
    reference_base_pages_file = base_dir / f".pages"
    with reference_base_pages_file.open("w", encoding="utf-8") as f:
        click.echo(f"Create the main .pages file: {reference_base_pages_file}")
        content = """nav:
    - "Task and Operator Reference": index.md
    - "Aggregators": aggregator
    - "Custom Workflow Tasks": customtask
    - "Datasets": dataset
    - "Distance Measures": distancemeasure
    - "Transformers": transformer"""
        f.write(content)

    for plugin_type in plugins:
        plugins_of_type = plugins[plugin_type]
        if plugin_type == "transformer":
            table_template = jinja_environment.get_template(f"operator_table_with_category.md")
        else:
            table_template = jinja_environment.get_template(f"operator_table.md")

        # Create type-specific index.md file
        index_file = base_dir / f"{plugin_type}/index.md"
        index_template = jinja_environment.get_template(f"{plugin_type}_base.md")
        items = table_template.render(plugins=plugins_of_type)
        with index_file.open("w", encoding="utf-8") as f:
            click.echo(f"Create {plugin_type} index file in {index_file}")
            f.write(index_template.render(items=items))

        # Create the .pages files
        pages_file = base_dir / plugin_type / ".pages"
        pages_content = "nav:\n    - index.md"
        if plugin_type == "transformer":
            # transformer get separated per main_category
            categories = list(set([plugin.main_category for plugin in plugins[plugin_type]]))
            categories.sort()
            for category in categories:
                pages_content += f'\n    - "{category}": {category}'

                sub_pages_file = base_dir / plugin_type / category / ".pages"
                sub_pages_content = "nav:"
                category_plugins = [plugin for plugin in plugins[plugin_type] if plugin.main_category == category]
                for plugin in category_plugins:
                    sub_pages_content += f"\n    - \"{plugin.title}\": {plugin.pluginId}.md"
                with sub_pages_file.open("w", encoding="utf-8") as f:
                    click.echo(f"Create .pages file {sub_pages_file}")
                    f.write(sub_pages_content)
        else:
            for plugin in plugins_of_type:
                if plugin.is_deprecated:
                    continue
                pages_content += f"\n    - \"{plugin.title}\": {plugin.pluginId}.md"
        with pages_file.open("w", encoding="utf-8") as f:
            click.echo(f"Create .pages file {pages_file}")
            f.write(pages_content)


@click.command()
@click.option(
    "--output-dir", "-o",
    type=click.Path(exists=False, dir_okay=True, file_okay=False),
    default="docs/build/reference",
    help="Where to save the markdown files",
    show_default=True,
)
def update_di_reference(output_dir):
    """Update DI Reference documentation."""
    basedir = Path(output_dir)
    click.echo(f"Creating DI reference documentation in {basedir}")
    plugins = get_plugin_descriptions()

    # create directory structure
    rmtree(basedir, ignore_errors=True)
    basedir.mkdir(parents=True, exist_ok=True)
    for type_id in plugins:
        Path(basedir / type_id).mkdir(parents=True, exist_ok=True)
        for plugin in plugins[type_id]:
            create_plugin_markdown(plugin, type_id, basedir)
    create_umbrella_pages(plugins=plugins, base_dir=basedir)
