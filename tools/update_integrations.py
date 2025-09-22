"""Update Integrations Page"""
import json
from pathlib import Path

import click
import yaml
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined
from pydantic import BaseModel, ConfigDict, TypeAdapter

from tools.update_di_reference import PluginDescription

jinja_environment = Environment(
    loader=PackageLoader("tools"),
    autoescape=select_autoescape(),
    undefined=StrictUndefined
)

ListOfPlugins = TypeAdapter(dict[str, PluginDescription])

class AttrDict(dict):
    """Dict subclass that allows attribute access."""

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


def get_plugin_placeholder(plugin_file: Path) -> object:
    """Get Plugin Placeholder to allow {{p.office365preadsheet}}"""
    placeholders = AttrDict()
    plugins = ListOfPlugins.validate_json(plugin_file.read_text())
    for pluginId, plugin in plugins.items():
        attribute_id = plugin.pluginId.replace("-", "_")
        attribute_id_ref = plugin.pluginId.replace("-", "_") + "_ref"
        plugin_link = f"../../build/reference/{plugin.pluginType}/{plugin.pluginId}.md"
        setattr(placeholders, attribute_id, f"[{plugin.title}]({plugin_link})")
        setattr(placeholders, attribute_id_ref, plugin_link)
    return placeholders


class Integration(BaseModel):
    """Integration Description"""

    model_config = ConfigDict(extra="forbid")

    name: str
    icon: str
    content: str

class IntegrationsFile(BaseModel):
    """Integration File Base Model"""

    model_config = ConfigDict(extra="forbid")

    integrations: list[Integration]

def create_integrations_markdown(yaml_source: Path, markdown_output: Path, plugins_file: Path) -> None:
    """Create the integration markdown file."""
    base_template = jinja_environment.get_template("integrations_base.md")
    integration_template = jinja_environment.get_template("integration.md")
    parsed_content = IntegrationsFile.model_validate(yaml.safe_load(yaml_source.read_text()))
    click.echo(f"Parsed {len(parsed_content.integrations)} integrations.")
    integrations = sorted(parsed_content.integrations, key=lambda i: i.name.lower())
    plugin_placeholder = get_plugin_placeholder(plugin_file=plugins_file)
    items = ""
    for integration in integrations:
        content_template = jinja_environment.from_string(integration.content)
        integration.content = content_template.render(p=plugin_placeholder) + "\n\n"
        items += integration_template.render(integration=integration)
    markdown = base_template.render(items=items)
    markdown_output.write_text(markdown)


@click.command()
@click.option(
    "--input-file", "-i",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default="data/integrations.yml",
    help="Where to get the integration descriptions from?",
    show_default=True,
)
@click.option(
    "--output-file", "-o",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default="docs/build/integrations/index.md",
    help="Where to save the markdown file?",
    show_default=True,
)
@click.option(
    "--plugins-file",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default="data/plugins.json",
    help="Where to load the plugin information from?",
    show_default=True,
)
def update_integrations(input_file: str, output_file: str, plugins_file: str) -> None:
    """Update the integrations page by parsing the integrations.yaml"""
    click.echo(f"Creating Integrations Pages as {output_file}")
    create_integrations_markdown(
        yaml_source=Path(input_file),
        markdown_output=Path(output_file),
        plugins_file=Path(plugins_file)
    )
