"""main package"""
from typing import List
import click

from tools.update_icons import update_icons


@click.group()
def cli():
    """documentation.eccenca.com build tool"""

cli.add_command(update_icons)
