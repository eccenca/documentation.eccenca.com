"""Commit an already-built site/ into a mike-managed branch.

``mike deploy`` builds and commits in one step: it shells out to ``zensical``
itself and then commits whatever that produced. That build is not our build - it
runs without ``--strict`` and, more importantly, without the post-build steps of
``task build``. A published version would therefore carry the unpkg.com URLs
that ``dec-tool localize-bundle-assets`` exists to rewrite, and building first
does not help: mike's rebuild overwrites the localized bundle before committing.

So this command takes mike's build step away and keeps everything else. mike
still owns the branch layout - versions.json, the alias symlinks, the root
redirect - via ``mike.commands.deploy``, which is a context manager that yields
where the build would happen and commits ``site_dir`` afterwards. Here the build
has already happened, so the body is empty.

``site/`` must have been built with ``MIKE_DOCS_VERSION`` set to the same
version, or the pages carry a canonical URL without the version prefix; the
build is not repeated here, so that is checked rather than assumed.

Usage: dec-tool publish --branch published --version 26.2 --alias latest
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import click
from mike import commands, utils

CANONICAL_RE = re.compile(r'<link rel="canonical" href="([^"]+)"')

# Zensical copies docs_dir verbatim, so these end up in the output; MkDocs
# excluded every dotfile by default (`.*`, before `exclude_docs` was consulted)
# and Zensical has no equivalent yet - zensical/backlog#65. Pruning matters most
# here: whatever this commits stays in the branch history for good.
PRUNE = (".pages", ".DS_Store")


def canonical_url(site: Path) -> str | None:
    """Return the canonical URL of the built landing page, if it has one."""
    index = site / "index.html"
    if not index.is_file():
        return None
    match = CANONICAL_RE.search(index.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def prune(site: Path) -> list[Path]:
    """Delete the copied-along dotfiles from the build output.

    Runs on every publish rather than once: Zensical's ``--clean`` cleans its
    cache, not ``site_dir``, so a file that appeared there stays until something
    removes it - see zensical/zensical#728 for why dotfiles in particular are
    spared.
    """
    removed = [path for name in PRUNE for path in site.rglob(name)]
    for path in removed:
        path.unlink()
    return removed


@click.command()
@click.option("--version", required=True, help="Version to publish as, e.g. 26.2")
@click.option("--branch", required=True, help="Branch to commit to, e.g. published")
@click.option(
    "--alias",
    "aliases",
    multiple=True,
    help="Alias for this version, e.g. latest. Repeatable.",
)
def publish(version: str, branch: str, aliases: tuple[str, ...]) -> None:
    """Commit the built site/ as VERSION on BRANCH, the way mike would."""
    cfg = utils.load_config()
    site = Path(cfg["site_dir"])

    if not site.is_dir() or not any(site.iterdir()):
        raise click.ClickException(
            f"{site} is empty or missing - run `task build` first"
        )

    site_url = cfg.get("site_url")
    expected = urljoin(site_url, f"{version}/") if site_url else None
    found = canonical_url(site)
    if expected and found != expected:
        raise click.ClickException(
            f"site/ carries the canonical URL {found or '(none)'}, expected "
            f"{expected}. Rebuild with `MIKE_DOCS_VERSION={version} task build` "
            f"- publishing this would point every page at the wrong place."
        )

    pruned = prune(site)
    if pruned:
        print(f"Pruned {len(pruned)} copied-along dotfile(s)", file=sys.stderr)

    # Empty body: mike commits site_dir when the context manager exits.
    with commands.deploy(
        cfg,
        version,
        aliases=list(aliases),
        update_aliases=True,
        branch=branch,
    ):
        pass

    listed = ", ".join(aliases) or "no aliases"
    print(f"Committed {site} as {version} ({listed}) on {branch}", file=sys.stderr)
