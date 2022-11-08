"""Update eccenca icons."""
import re
from json import load
import urllib.request

import click
import requests

ICON_NAMES = "https://raw.githubusercontent.com/eccenca/gui-elements/develop/src/components/Icon/canonicalIconNames.tsx"
CARBON_BASE_URL = "https://raw.githubusercontent.com/carbon-design-system/carbon/main/packages/icons/src/svg/"


@click.command()
@click.option(
    "--eccenca-canonical-names", "-s", "names_source",
    default=ICON_NAMES,
    help="Where to load the eccenca canonical names from?",
    show_default=True,
)
@click.option(
    "--carbon-metadata", "-i",
    type=click.Path(exists=True, dir_okay=False, file_okay=True),
    default="tmp/node_modules/@carbon/icons/metadata.json",
    help="Where to load the carbon icon metadata from?",
    show_default=True,
)
@click.option(
    "--output-dir", "-o",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default="overrides/.icons/eccenca",
    help="Where to save to SVGs?",
    show_default=True,
)
def update_icons(carbon_metadata, output_dir, names_source):
    """Update eccenca icons."""

    # load carbon icon metadata
    carbon_icons = {}
    with open(carbon_metadata) as json_data:
        for _ in load(json_data)["icons"]:
            carbon_icons[_["moduleInfo"]["global"]] = _

    # extract used eccenca icons 1: find icon definitions
    tsx = {}
    icons = {}
    for line_no, line in enumerate(requests.get(names_source).text.split('\n')):
        tsx[line_no] = line
        # Example: "    "item-question": {"
        match_icon = re.search(r"^\s+\"(.*)\":\s+{$", line, re.IGNORECASE)
        if match_icon:
            name = match_icon.group(1)
            icon = {
                "line_no": line_no,
                "name": name
            }
            icons[name] = icon

    # extract used eccenca icons 2: get carbon Ids and fetch SVGs
    for name, icon in icons.items():
        name = icon["name"]
        # Example: "        small: icons.DataVis_116," -> DataVis_1
        # Example: "        small: icons.Csv16," -> Csv
        carbon_id = tsx[icon["line_no"] + 1]
        match_carbon_id = re.search(r"^\s+small: icons.([a-z\_0-9]+)[0-9][0-9],", carbon_id, re.IGNORECASE)
        carbon_id = match_carbon_id.group(1)
        file_path = carbon_icons[carbon_id]["assets"][0]["filepath"]
        url = f"{CARBON_BASE_URL}{file_path}"
        output = f"{output_dir}/{name}.svg"
        urllib.request.urlretrieve(url, output)
        print(f"{url} -> {output}")
