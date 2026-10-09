"""Test the author list of the print edition's imprint"""
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

import click
import pytest
import yaml

from tools.pdf_authors import (
    AuthorRules,
    add_names,
    authors_yaml,
    commit_accounts,
    count_commits,
    file_commits,
    get_json,
    github_token,
    imprint_names,
    printed_files,
    load_author_rules,
    load_imprint_names,
    next_page,
    prefill_names,
    select_authors,
)

# The shape of tools/pdf/print.yml: comments, and sections before and after `authors`.
PRINT_YML = """\
---
# The print edition.
publisher:
  name: eccenca GmbH

authors:
  # GitHub ID: the name to print.
  names: {}
  # GitHub IDs never to list.
  exclude: []

sections:
  build/reference/: list
"""

AUTHORS = [
    {"id": "seebi", "name": "Jane Doe", "commits": 3},
    {"id": "nameless", "name": None, "commits": 2},
    {"id": "Hubot", "name": "John Roe", "commits": 1},
]


def test_most_commits_first_and_ties_by_id_case_insensitive():
    contributors = [
        {"login": "haschek", "contributions": 10, "type": "User"},
        {"login": "seebi", "contributions": 532, "type": "User"},
        {"login": "BorderCloud", "contributions": 10, "type": "User"},
        {"login": "rpietzsch", "contributions": 639, "type": "User"},
    ]
    assert [a["id"] for a in select_authors(contributors)] == ["rpietzsch", "seebi", "BorderCloud", "haschek"]


def test_bots_agents_and_anonymous_contributions_are_not_authors():
    contributors = [
        {"login": "dependabot[bot]", "contributions": 40, "type": "Bot"},
        {"login": "claude-agent", "contributions": 30, "type": "User"},
        {"login": "Codex", "contributions": 20, "type": "User"},
        {"name": "Someone", "email": "someone@example.org", "contributions": 33, "type": "Anonymous"},
        {"login": "sobo", "contributions": 53, "type": "User"},
    ]
    assert select_authors(contributors) == [{"id": "sobo", "commits": 53}]


def test_printed_files_are_the_pages_not_generated_and_the_images_they_reference(tmp_path):
    docs = tmp_path / "docs"
    (docs / "build/tutorial").mkdir(parents=True)
    (docs / "build/shared").mkdir()
    (docs / "build/reference").mkdir()
    (docs / "build/tutorial/index.md").write_text(
        "# Tutorial\n\n"
        '![Shot](shot.png){ width="50%" }\n\n'
        '<img src="../shared/logo.png" alt="">\n\n'
        "![Remote](https://example.org/remote.png)\n\n"
        "![Missing](gone.png)\n"
    )
    (docs / "build/tutorial/shot.png").write_bytes(b"png")
    (docs / "build/shared/logo.png").write_bytes(b"png")
    (docs / "build/reference/index.md").write_text(
        "# Reference\n<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->\n\n![x](x.png)\n"
    )
    files = printed_files(["build/tutorial/index.md", "build/reference/index.md", "build/missing.md"], docs)
    assert [Path(f).relative_to(docs).as_posix() for f in files] == [
        "build/tutorial/index.md",
        "build/tutorial/shot.png",
        "build/shared/logo.png",
    ]


def test_each_commit_counts_once_for_the_account_that_made_it():
    commits = {
        "a1": "jane@example.org",
        "a2": "jane@example.org",
        "b1": "JOHN@example.org",
        "c1": "bot@example.org",
        "d1": "nobody@example.org",
    }
    api = [
        {"sha": "a1", "author": {"login": "jane", "type": "User"}, "commit": {"author": {"email": "jane@example.org"}}},
        {"sha": "x9", "author": {"login": "john", "type": "User"}, "commit": {"author": {"email": "john@example.org"}}},
        {"sha": "c1", "author": {"login": "dependabot[bot]", "type": "Bot"}, "commit": {"author": {"email": "bot@example.org"}}},
        {"sha": "d1", "author": None, "commit": {"author": {"email": "nobody@example.org"}}},
    ]
    by_sha, by_email = commit_accounts(api)
    records = count_commits(commits, by_sha, by_email)
    # a2 is not on GitHub yet and b1 was made elsewhere: their e-mail names the
    # account, case-insensitively. d1 maps to no account and is left out.
    assert sorted(records, key=lambda r: r["login"]) == [
        {"login": "dependabot[bot]", "type": "Bot", "contributions": 1},
        {"login": "jane", "type": "User", "contributions": 2},
        {"login": "john", "type": "User", "contributions": 1},
    ]
    assert [a["id"] for a in select_authors(records)] == ["jane", "john"]


def test_file_commits_follow_renames_and_skip_merges(tmp_path):
    isolated = {
        **os.environ,
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Jane", "GIT_AUTHOR_EMAIL": "jane@example.org",
        "GIT_COMMITTER_NAME": "Jane", "GIT_COMMITTER_EMAIL": "jane@example.org",
    }

    def git(*args):
        subprocess.run(["git", *args], cwd=tmp_path, env=isolated, check=True, capture_output=True)

    git("init", "-q", "-b", "main")
    (tmp_path / "old.md").write_text("one\n")
    git("add", ".")
    git("commit", "-q", "-m", "one")
    git("mv", "old.md", "new.md")
    git("commit", "-q", "-m", "rename")
    git("checkout", "-q", "-b", "side")
    (tmp_path / "new.md").write_text("two\n")
    git("commit", "-q", "-am", "two")
    git("checkout", "-q", "main")
    (tmp_path / "other.md").write_text("other\n")
    git("add", ".")
    git("commit", "-q", "-m", "other")
    git("merge", "-q", "--no-ff", "-m", "merge", "side")
    commits = file_commits([Path("new.md")], repo=tmp_path, env=isolated)
    # one, rename and two - the merge commit does not count, other.md is not asked for.
    assert len(commits) == 3
    assert set(commits.values()) == {"jane@example.org"}


def test_excluded_ids_are_not_authors_whatever_their_case():
    contributors = [
        {"login": "seebi", "contributions": 532, "type": "User"},
        {"login": "BorderCloud", "contributions": 10, "type": "User"},
    ]
    rules = AuthorRules(names={}, exclude=frozenset({"bordercloud"}))
    assert select_authors(contributors, rules) == [{"id": "seebi", "commits": 532}]


def test_names_are_the_profile_names_and_a_blank_one_is_none():
    authors = [{"id": "a", "commits": 3}, {"id": "b", "commits": 2}, {"id": "c", "commits": 1}]
    profiles = {"a": "  Jane Doe ", "b": "", "c": None}
    assert add_names(authors, profiles.get) == [
        {"id": "a", "name": "Jane Doe", "commits": 3},
        {"id": "b", "name": None, "commits": 2},
        {"id": "c", "name": None, "commits": 1},
    ]


def test_pagination_follows_the_next_link_only():
    header = (
        '<https://api.github.com/repositories/1/contributors?per_page=100&page=2>; rel="next", '
        '<https://api.github.com/repositories/1/contributors?per_page=100&page=3>; rel="last"'
    )
    assert next_page(header) == "https://api.github.com/repositories/1/contributors?per_page=100&page=2"
    assert next_page("") is None


def test_the_file_names_its_source_and_keeps_the_order():
    authors = [{"id": "b", "name": "Jane Doe", "commits": 2}, {"id": "a", "name": None, "commits": 1}]
    text = authors_yaml("eccenca/docs", authors)
    assert text.startswith("---\n# Generated by `dec-tool pdf-authors`")
    # yamllint's default rules want list items indented under their key.
    assert "authors:\n  - id: b\n    name: Jane Doe\n    commits: 2\n" in text
    assert yaml.safe_load(text) == {"repository": "eccenca/docs", "authors": authors}


def test_rules_read_names_and_exclusions_case_insensitive(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("authors:\n  names:\n    Octocat: Dr. Jane Doe\n  exclude:\n    - Hubot\n")
    assert load_author_rules(path) == AuthorRules(names={"octocat": "Dr. Jane Doe"}, exclude=frozenset({"hubot"}))


def test_without_an_authors_section_nothing_is_renamed_or_excluded(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("publisher:\n  name: eccenca GmbH\n")
    assert load_author_rules(path) == AuthorRules(names={}, exclude=frozenset())


@pytest.mark.parametrize(
    "section",
    [
        "authors:\n  exclude: hubot\n",
        "authors:\n  names:\n    - octocat\n",
        "authors:\n  names:\n    octocat: 42\n",
    ],
)
def test_malformed_rules_fail(tmp_path, section):
    path = tmp_path / "print.yml"
    path.write_text(section)
    with pytest.raises(click.ClickException, match="authors"):
        load_author_rules(path)


def test_a_name_left_empty_is_not_given(tmp_path):
    path = tmp_path / "print.yml"
    path.write_text("authors:\n  names:\n    octocat:\n    hubot: ''\n")
    assert load_author_rules(path) == AuthorRules(names={}, exclude=frozenset())


def test_prefill_lists_every_author_with_the_profile_name_as_a_comment():
    text, added = prefill_names(PRINT_YML, AUTHORS)
    assert added == ["seebi", "nameless", "Hubot"]
    assert (
        "  # GitHub ID: the name to print.\n"
        "  names:\n"
        "    seebi:  # GitHub profile: Jane Doe\n"
        "    nameless:  # no name on the GitHub profile\n"
        "    Hubot:  # GitHub profile: John Roe\n"
        "  # GitHub IDs never to list.\n"
        "  exclude: []\n"
    ) in text
    data = yaml.safe_load(text)
    # Left empty, an entry gives no name: the imprint keeps printing the profile's.
    assert data["authors"] == {"names": {"seebi": None, "nameless": None, "Hubot": None}, "exclude": []}
    assert data["publisher"] == {"name": "eccenca GmbH"}
    assert data["sections"] == {"build/reference/": "list"}
    assert text.startswith("---\n# The print edition.\n")


def test_prefill_keeps_the_names_given_and_adds_only_the_ids_not_listed(tmp_path):
    given = PRINT_YML.replace("  names: {}\n", "  names:\n    SEEBI: Dr. Jane Doe\n")
    text, added = prefill_names(given, AUTHORS)
    assert added == ["nameless", "Hubot"]
    assert (
        "  names:\n"
        "    SEEBI: Dr. Jane Doe\n"
        "    nameless:  # no name on the GitHub profile\n"
        "    Hubot:  # GitHub profile: John Roe\n"
        "  # GitHub IDs never to list.\n"
    ) in text
    path = tmp_path / "print.yml"
    path.write_text(text)
    assert load_author_rules(path) == AuthorRules(names={"seebi": "Dr. Jane Doe"}, exclude=frozenset())


def test_prefill_skips_excluded_ids_and_a_second_run_changes_nothing():
    excluding = PRINT_YML.replace("  exclude: []\n", "  exclude:\n    - hubot\n")
    once, added = prefill_names(excluding, AUTHORS)
    assert added == ["seebi", "nameless"]
    assert prefill_names(once, AUTHORS) == (once, [])


def test_prefill_adds_an_authors_section_where_there_is_none():
    text, added = prefill_names("---\npublisher:\n  name: eccenca GmbH\n", [{"id": "null", "name": None, "commits": 1}])
    assert added == ["null"]
    # A login YAML would read as something else is quoted.
    assert "\nauthors:\n  names:\n    'null':  # no name on the GitHub profile\n  exclude: []\n" in text
    assert yaml.safe_load(text) == {"publisher": {"name": "eccenca GmbH"}, "authors": {"names": {"null": None}, "exclude": []}}


def failing_urlopen(error):
    def urlopen(request, timeout):
        raise error
    return urlopen


def rate_limited(reset: int) -> urllib.error.HTTPError:
    headers = {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(reset)}
    return urllib.error.HTTPError("https://api.github.com/users/x", 403, "rate limit exceeded", headers, None)


def test_a_rate_limit_fails_with_the_reset_time_and_how_to_raise_the_limit(monkeypatch):
    reset = 1_900_000_000
    monkeypatch.setattr(urllib.request, "urlopen", failing_urlopen(rate_limited(reset)))
    with pytest.raises(click.ClickException) as raised:
        get_json("https://api.github.com/users/x", None)
    message = raised.value.message
    assert "rate limit" in message
    assert time.strftime("%H:%M", time.localtime(reset)) in message
    assert "GITHUB_TOKEN" in message and "gh auth login" in message


def test_with_a_token_a_rate_limit_fails_with_the_reset_time_only(monkeypatch):
    monkeypatch.setattr(urllib.request, "urlopen", failing_urlopen(rate_limited(1_900_000_000)))
    with pytest.raises(click.ClickException) as raised:
        get_json("https://api.github.com/users/x", "a-token")
    assert "rate limit" in raised.value.message
    assert "GITHUB_TOKEN" not in raised.value.message


@pytest.mark.parametrize(
    "error, expected",
    [
        (urllib.error.HTTPError("https://api.github.com/users/gone", 404, "Not Found", {}, None), "HTTP 404 Not Found"),
        (urllib.error.HTTPError("https://api.github.com/users/x", 401, "Unauthorized", {}, None), "rejected the token"),
        (urllib.error.URLError("nodename nor servname provided"), "cannot reach the GitHub API"),
        (TimeoutError("timed out"), "cannot reach the GitHub API"),
    ],
)
def test_other_failures_end_with_a_message_instead_of_a_traceback(monkeypatch, error, expected):
    monkeypatch.setattr(urllib.request, "urlopen", failing_urlopen(error))
    with pytest.raises(click.ClickException, match=expected):
        get_json("https://api.github.com/users/gone", "a-token")


def without_token_variables(monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("GH_TOKEN", raising=False)


def test_the_token_of_the_environment_comes_first(monkeypatch):
    without_token_variables(monkeypatch)
    monkeypatch.setenv("GH_TOKEN", "from-env")
    monkeypatch.setattr(shutil, "which", lambda name: pytest.fail("the GitHub CLI is not asked"))
    assert github_token() == ("from-env", "GH_TOKEN")


def test_without_one_in_the_environment_the_github_cli_lends_its_token(monkeypatch):
    without_token_variables(monkeypatch)
    monkeypatch.setattr(shutil, "which", lambda name: "/usr/local/bin/gh")
    monkeypatch.setattr(
        subprocess, "run", lambda *args, **kwargs: subprocess.CompletedProcess(args, 0, stdout="gho_cli\n", stderr="")
    )
    assert github_token() == ("gho_cli", "the GitHub CLI")


@pytest.mark.parametrize(
    "which, run",
    [
        (lambda name: None, None),
        (
            lambda name: "/usr/local/bin/gh",
            lambda *args, **kwargs: subprocess.CompletedProcess(args, 1, stdout="", stderr="not logged in"),
        ),
    ],
)
def test_without_a_variable_or_a_logged_in_github_cli_there_is_no_token(monkeypatch, which, run):
    without_token_variables(monkeypatch)
    monkeypatch.setattr(shutil, "which", which)
    if run is not None:
        monkeypatch.setattr(subprocess, "run", run)
    assert github_token() == (None, None)


def test_the_imprint_prints_a_given_name_before_the_profile_name_and_the_id_last():
    authors = [
        {"id": "a", "name": "Jane Doe", "commits": 4},
        {"id": "B", "name": "John Roe", "commits": 3},
        {"id": "c", "name": None, "commits": 2},
        {"id": "d", "name": "Richard Miles", "commits": 1},
    ]
    rules = AuthorRules(names={"b": "Dr. John Roe"}, exclude=frozenset({"d"}))
    # The names in imprint order, and the IDs that print as themselves for want of a name.
    assert imprint_names(authors, rules) == (["Jane Doe", "Dr. John Roe", "c"], ["c"])


def test_the_imprint_reads_the_generated_list_and_the_rules(tmp_path):
    authors_yml = tmp_path / "authors.yml"
    authors_yml.write_text(authors_yaml("eccenca/docs", [{"id": "a", "name": None, "commits": 1}]))
    print_yml = tmp_path / "print.yml"
    print_yml.write_text("authors:\n  names:\n    a: Jane Doe\n")
    assert load_imprint_names(authors_yml, print_yml) == (["Jane Doe"], [])
