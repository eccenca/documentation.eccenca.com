"""Test the MD044 allowlist for technical identifiers in .rumdl.toml

MD044 enforces the capitalization of proper names such as ``GitHub`` or ``eccenca``.
Some technical identifiers in the documentation contain those names but must keep
their exact spelling: Material icon shortcodes, hostnames and environment variables.

They are protected by listing the longer identifier in ``[MD044].names`` *before* the
brand name, so the longer match wins. These tests pin that behaviour down - both that
the identifiers survive ``rumdl --fix`` and that the rule still catches real prose.
"""
import json
import pathlib
import shutil
import subprocess
import tomllib

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
RUMDL_CONFIG = REPO_ROOT / ".rumdl.toml"

# Technical identifiers that contain a proper name but must never be rewritten.
# Each entry is a snippet taken from the documentation as it is written today.
PROTECTED_SNIPPETS = {
    "frontmatter-icon-github": '---\ntitle: "cmemc: Using GitHub Actions"\nicon: material/github\n---\n',
    "frontmatter-icon-gitlab": '---\ntitle: "cmemc: Using GitLab Pipelines"\nicon: material/gitlab\n---\n',
    "material-icon-github": "- :material-github: [GitHub Actions](github-action/index.md)\n",
    "material-icon-gitlab": "- :material-gitlab: [GitLab Pipelines](gitlab-pipeline/index.md)\n",
    "simple-icon-github": "- :simple-github:{ .lg .middle } GitHub\n",
    "simple-icon-gitlab": "- :simple-gitlab:{ .lg .middle } GitLab\n",
    "hostname": '=== "Installation via gitlab.eccenca.com"\n',
    "env-var": "| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND |\n",
    "env-var-long": (
        "| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_WEBAPP_WEB_FILTER_SIMPLECORSFILTER |\n"
    ),
}

# Misspellings in running text that MD044 must keep reporting, so that the
# allowlist above cannot silently switch the whole rule off.
PROSE_VIOLATIONS = [
    ("The Github project provides an example.", "Github", "GitHub"),
    ("You can use cmemc in Gitlab pipelines.", "Gitlab", "GitLab"),
    ("The backend delivers the javascript frontend.", "javascript", "JavaScript"),
    ("Upgraded to typescript version 5.5.3.", "typescript", "TypeScript"),
    ("Eccenca provides a custom authentication provider.", "Eccenca", "eccenca"),
    ("Lists all RDF graphs on this corporate memory instance.", "corporate memory", "Corporate Memory"),
]

pytestmark = pytest.mark.skipif(
    shutil.which("rumdl") is None, reason="rumdl is not installed in this environment"
)


def _rumdl(path, *extra_args):
    """Run rumdl for MD044 only against path and return the completed process."""
    result = subprocess.run(
        [
            "rumdl",
            "--config",
            str(RUMDL_CONFIG),
            "check",
            "--enable",
            "MD044",
            *extra_args,
            str(path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    # rumdl exits 1 when it reports findings, so only a crash is an error here
    assert result.returncode in (0, 1), f"rumdl failed: {result.stderr}"
    return result


def _findings(path):
    """Return the MD044 findings for path as parsed JSON."""
    result = _rumdl(path, "--output-format", "json")
    return json.loads(result.stdout or "[]")


def _fix(path):
    """Apply the MD044 auto-fix to path in place.

    Deliberately without ``--output-format json``: combining that with ``--fix``
    makes rumdl report the fixes but leave the file untouched, which would turn
    every assertion below into a no-op.
    """
    _rumdl(path, "--fix")


def _write(tmp_path, name, content):
    """Write a markdown fixture and return its path."""
    target = tmp_path / f"{name}.md"
    target.write_text(content, encoding="utf-8")
    return target


@pytest.mark.parametrize("name, snippet", sorted(PROTECTED_SNIPPETS.items()))
def test_md044_does_not_report_technical_identifiers(tmp_path, name, snippet):
    """Icon shortcodes, hostnames and environment variables are not MD044 findings."""
    findings = _findings(_write(tmp_path, name, snippet))
    assert findings == [], f"{name} should be covered by the MD044 allowlist"


@pytest.mark.parametrize("name, snippet", sorted(PROTECTED_SNIPPETS.items()))
def test_md044_fix_leaves_technical_identifiers_untouched(tmp_path, name, snippet):
    """`rumdl --fix` must not rewrite the protected identifiers.

    This is the regression that matters: a missing allowlist entry does not just add
    noise, it makes the auto-fix break icons, hostnames and environment variables.
    """
    target = _write(tmp_path, name, snippet)
    _fix(target)
    assert target.read_text(encoding="utf-8") == snippet


@pytest.mark.parametrize("text, wrong, correct", PROSE_VIOLATIONS)
def test_md044_still_reports_proper_names_in_prose(tmp_path, text, wrong, correct):
    """The allowlist must not weaken MD044 for ordinary running text."""
    findings = _findings(_write(tmp_path, "prose", f"{text}\n"))
    messages = [finding["message"] for finding in findings]
    assert messages == [f"Proper name '{wrong}' should be '{correct}'"]


def test_md044_fix_corrects_prose(tmp_path):
    """`rumdl --fix` still repairs the proper names it is meant to repair."""
    target = _write(tmp_path, "prose", "The Github project uses javascript.\n")
    _fix(target)
    assert target.read_text(encoding="utf-8") == "The GitHub project uses JavaScript.\n"


def test_md044_allowlist_orders_identifiers_before_brand_names():
    """The technical identifiers must stay listed before the brand names they contain.

    MD044 resolves overlapping names by the longer match, but keeping the order also
    keeps the intent readable for whoever edits the list next.
    """
    names = tomllib.loads(RUMDL_CONFIG.read_text(encoding="utf-8"))["MD044"]["names"]
    for identifier, brand in (
        ("material/github", "GitHub"),
        ("material-gitlab", "GitLab"),
        ("simple-github", "GitHub"),
        ("gitlab.eccenca.com", "eccenca"),
        ("COM_ECCENCA", "eccenca"),
    ):
        assert identifier in names, f"{identifier} is missing from [MD044].names"
        assert names.index(identifier) < names.index(brand), (
            f"{identifier} must be listed before {brand}"
        )
