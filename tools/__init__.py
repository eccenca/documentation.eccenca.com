"""main package"""
from typing import List
import click

from tools.build_navigation import build_navigation
from tools.check_zensical_output import check_zensical_output
from tools.localize_bundle_assets import localize_bundle_assets
from tools.publish import publish
from tools.update_di_reference import update_di_reference
from tools.update_icons import update_icons
from tools.update_integrations import update_integrations

@click.group()
def cli():
    """documentation.eccenca.com build tool"""

cli.add_command(build_navigation)
cli.add_command(check_zensical_output)
cli.add_command(localize_bundle_assets)
cli.add_command(publish)
cli.add_command(update_icons)
cli.add_command(update_di_reference)
cli.add_command(update_integrations)
