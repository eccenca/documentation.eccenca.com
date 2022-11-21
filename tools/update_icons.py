"""Update eccenca icons."""
import json
import re
from glob import glob
from json import load
from os import remove
from pprint import pprint
from shutil import rmtree
from subprocess import check_call
from tempfile import mkdtemp

import click
import requests

PACKAGE_JSON = "https://raw.githubusercontent.com/eccenca/gui-elements/{}/package.json"
ICON_NAMES = "https://raw.githubusercontent.com/eccenca/gui-elements/{}/src/components/Icon/canonicalIconNames.tsx"


@click.command()
@click.option(
    "--version",
    default="main",
    help="Which version of the GUI elements should be used?",
    show_default=True,
)
@click.option(
    "--output-dir", "-o",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default="overrides/.icons/eccenca",
    help="Where to save to SVGs?",
    show_default=True,
)
def update_icons(version, output_dir):
    """Update eccenca icons."""

    click.echo(f"used eccenca gui-elements git spec: {version}")
    click.echo(f"used eccenca icon directory: {output_dir}")
    # fetch carbon icons version from the gui-elements package json
    carbon_version = json.loads(
        requests.get(
            PACKAGE_JSON.format(version)
        ).text
    )["dependencies"]["@carbon/icons"]
    click.echo(f"used carbon icons version: {carbon_version}")

    # install carbon icons: @carbon/icons
    tmpdir = mkdtemp()
    click.echo(f"install directory: {tmpdir}")
    package = f"@carbon/icons@{carbon_version}"
    check_call(
        ["npm", "install", package],
        cwd=tmpdir
    )

    # load carbon icon metadata
    carbon_icons = {}
    metadata_json = f"{tmpdir}/node_modules/@carbon/icons/metadata.json"
    with open(metadata_json) as json_data:
        for _ in load(json_data)["icons"]:
            carbon_icons[_["moduleInfo"]["global"]] = _
    click.echo(f"loaded carbon icons: {len(carbon_icons)}")
    rmtree(tmpdir)
    click.echo(f"delete directory: {tmpdir}")

    # extract the used eccenca icons 1: find icon definitions
    tsx = {}
    icons = {}
    names_source = ICON_NAMES.format(version)
    for line_no, line in enumerate(requests.get(names_source).text.split('\n')):
        tsx[line_no] = line
        # Example: "    "item-question": {"
        match_icon = re.search(r"^\s+\"(.*)\":\s+{$", line, re.IGNORECASE)
        if match_icon:
            name = match_icon.group(1).lower()
            icon = {
                "line_no": line_no,
                "name": name
            }
            icons[name] = icon
    click.echo(f"found eccenca icons: {len(icons)}")

    # remove old SVG files
    old_svg_files = glob(f"{output_dir}/*.svg")
    for _ in old_svg_files:
        remove(_)
    click.echo(f"old SVG files deleted: {len(old_svg_files)}")

    # extract the used eccenca icons 2: get carbon Ids and fetch SVGs
    for name, icon in icons.items():
        name = icon["name"]
        # Example: "        small: icons.DataVis_116," -> DataVis_1
        # Example: "        small: icons.Csv16," -> Csv
        carbon_id = tsx[icon["line_no"] + 1]
        match_carbon_id = re.search(r"^\s+small: icons.([a-z_0-9]+)[0-9][0-9],", carbon_id, re.IGNORECASE)
        carbon_id = match_carbon_id.group(1)
        svg = carbon_icons[carbon_id]["assets"][0]["optimized"]["data"]
        output = f"{output_dir}/{name}.svg"
        with open(output, encoding='utf-8', mode="w") as svg_file:
            svg_file.write(svg)
    click.echo(f"created SVG files: {len(icons)}")
