"""main package"""
from typing import List
import click

from tools.update_di_reference import update_di_reference
from tools.update_icons import update_icons
from tools.update_integrations import update_integrations

@click.group()
def cli():
    """documentation.eccenca.com build tool"""

cli.add_command(update_icons)
cli.add_command(update_di_reference)
cli.add_command(update_integrations)
