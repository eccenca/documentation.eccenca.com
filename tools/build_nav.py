"""Build nav.yml from docs/.pages files recursively."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

DOCS_DIR = Path("docs")


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
    # No nav — emit a bare directory reference (zensical auto-discovers)
    path_str = str(docs_rel).replace("\\", "/")
    return {title: path_str} if title is not None else path_str


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


def main() -> None:
    pages = read_pages(DOCS_DIR)
    if not pages or "nav" not in pages:
        print("ERROR: docs/.pages missing or has no nav: block", file=sys.stderr)
        sys.exit(1)

    nav = build_nav_list(pages["nav"], DOCS_DIR, Path(""))

    # Dump with a custom representer that keeps strings unquoted where safe
    # and preserves unicode (e.g. &nbsp; in titles)
    output = yaml.dump(
        {"nav": nav},
        default_flow_style=False,
        allow_unicode=True,
        width=120,
        indent=2,
    )
    print(output, end="")


if __name__ == "__main__":
    main()
