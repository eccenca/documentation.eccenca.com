"""Build nav.yml from docs/.pages files recursively."""

from __future__ import annotations

import difflib
import sys
from pathlib import Path

import click
import yaml


def read_pages(directory: Path) -> dict | None:
    pf = directory / ".pages"
    if not pf.exists():
        return None
    text = pf.read_text(encoding="utf-8").strip()
    return yaml.safe_load(text) if text else None


def expand_dir(title: str | None, abs_dir: Path, docs_rel: Path) -> object:
    """Expand a directory into nav items using its .pages file if present."""
    pages = read_pages(abs_dir)
    if pages and "nav" in pages and pages["nav"]:
        children = build_nav_list(pages["nav"], abs_dir, docs_rel)
        return {title: children} if title is not None else children
    # No .pages nav in this directory, so discover its contents.
    #
    # This used to emit a bare directory reference on the assumption that
    # Zensical auto-discovers what is inside. It does not - a bare directory is
    # never resolved to a page object, which costs the entry its `icon:` front
    # matter, leaves the target page with no active nav position (making the
    # whole left sidebar render empty under `navigation.tabs`), and drops every
    # other page in the directory from the navigation entirely.
    #
    # On `main` this worked because there is no `nav:` at all: MkDocs walks the
    # docs tree itself and `.pages` only reorders what it finds. Here `nav.yml`
    # is the complete navigation, so the walk has to happen at generation time
    # or those pages become unreachable. The ordering below mirrors MkDocs'
    # automatic navigation: index page first, then remaining Markdown files,
    # then subdirectories, each group sorted by name.
    children = discover_dir(abs_dir, docs_rel)
    if not children:
        path_str = str(docs_rel).replace("\\", "/")
        return {title: path_str} if title is not None else path_str
    if title is None and len(children) == 1 and isinstance(children[0], str):
        # Titleless expansion has no section name to preserve, so splice the
        # lone index page straight into the parent list as a plain link.
        return children[0]
    return {title: children} if title is not None else children


def dir_title(name: str) -> str:
    """Section title for an auto-discovered directory, as MkDocs derives it.

    MkDocs replaces the separators and then capitalises the result *only* when
    the name is entirely lower case, so directories that already carry casing
    keep it. That is what preserves acronyms: `link-IDS-event-to-KG` stays
    "link IDS event to KG" rather than becoming "Link Ids Event To Kg".
    """
    title = name.replace("-", " ").replace("_", " ")
    return title.capitalize() if title.lower() == title else title


def has_markdown(directory: Path) -> bool:
    return any(directory.rglob("*.md"))


def discover_dir(abs_dir: Path, docs_rel: Path) -> list:
    """List a directory's nav entries the way MkDocs' automatic nav would."""
    rel = str(docs_rel).replace("\\", "/")
    entries: list = []

    if (abs_dir / "index.md").is_file():
        entries.append(f"{rel}/index.md")

    for md in sorted(
        (p for p in abs_dir.iterdir() if p.is_file() and p.suffix == ".md"),
        key=lambda p: p.name,
    ):
        if md.name != "index.md":
            entries.append(f"{rel}/{md.name}")

    for sub in sorted((p for p in abs_dir.iterdir() if p.is_dir()), key=lambda p: p.name):
        if not has_markdown(sub):
            continue
        # Recurse through expand_dir so a nested .pages still wins.
        entries.append(expand_dir(dir_title(sub.name), sub, docs_rel / sub.name))

    return entries


def expand_item(item: object, abs_base: Path, docs_rel_base: Path) -> object:
    """Convert one .pages nav entry to MkDocs nav format."""
    if isinstance(item, str):
        # Plain path, no title
        abs_path = abs_base / item
        docs_rel = docs_rel_base / item
        if abs_path.is_dir():
            # Inherit title from sub-directory's .pages `title:` key if present
            sub = read_pages(abs_path)
            inherited_title = sub.get("title") if sub else None
            return expand_dir(inherited_title, abs_path, docs_rel)
        return str(docs_rel).replace("\\", "/")

    if isinstance(item, dict):
        assert len(item) == 1, f"Expected single-key dict, got: {item}"
        title, value = next(iter(item.items()))

        if isinstance(value, list):
            # Inline section: "Title: [children]"
            children = []
            for child in value:
                resolved = expand_item(child, abs_base, docs_rel_base)
                if resolved is not None:
                    if isinstance(resolved, list):
                        children.extend(resolved)
                    else:
                        children.append(resolved)
            return {title: children}

        if isinstance(value, str):
            abs_path = abs_base / value
            docs_rel = docs_rel_base / value
            if abs_path.is_dir():
                return expand_dir(title, abs_path, docs_rel)
            return {title: str(docs_rel).replace("\\", "/")}

    return None


def build_nav_list(nav: list, abs_dir: Path, docs_rel: Path) -> list:
    result = []
    for item in nav:
        resolved = expand_item(item, abs_dir, docs_rel)
        if resolved is None:
            continue
        if isinstance(resolved, list):
            result.extend(resolved)
        else:
            result.append(resolved)
    return result


def render_nav(docs_dir: Path) -> str:
    """Render the nav.yml body for a docs tree."""
    pages = read_pages(docs_dir)
    if not pages or "nav" not in pages:
        raise click.ClickException(f"{docs_dir}/.pages missing or has no nav: block")

    nav = build_nav_list(pages["nav"], docs_dir, Path(""))

    # Dump with a custom representer that keeps strings unquoted where safe
    # and preserves unicode (e.g. &nbsp; in titles)
    return yaml.dump(
        {"nav": nav},
        default_flow_style=False,
        allow_unicode=True,
        width=120,
        indent=2,
    )


@click.command()
@click.option(
    "--docs-dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    default="docs",
    help="Where to read the .pages files from?",
    show_default=True,
)
@click.option(
    "--output-file", "-o",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default="nav.yml",
    help="Where to save the navigation to?",
    show_default=True,
)
@click.option(
    "--check",
    is_flag=True,
    help="Compare against the output file instead of writing it, exit 1 on drift.",
)
def build_navigation(docs_dir: str, output_file: str, check: bool) -> None:
    """Build the navigation from the .pages files."""
    output = render_nav(Path(docs_dir))
    target = Path(output_file)

    if not check:
        click.echo(f"Write the navigation of {docs_dir} to {target}")
        target.write_text(output)
        return

    current = target.read_text() if target.exists() else ""
    if current == output:
        click.echo(f"{target} matches the .pages files.")
        return

    diff = difflib.unified_diff(
        current.splitlines(keepends=True),
        output.splitlines(keepends=True),
        fromfile=str(target),
        tofile=f"{docs_dir}/**/.pages",
    )
    click.echo("".join(diff), nl=False)
    click.echo()
    click.echo(f"{target} is out of date with respect to the {docs_dir}/**/.pages files.")
    click.echo("Run 'task update:navigation' and commit the result.")
    sys.exit(1)
