"""main package"""
from typing import List
import click

from tools.update_di_reference import update_di_reference
from tools.update_icons import update_icons


@click.group()
def cli():
    """documentation.eccenca.com build tool"""

cli.add_command(update_icons)
cli.add_command(update_di_reference)
