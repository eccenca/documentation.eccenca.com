"""Write the author list the imprint of the print edition prints.

The authors are the GitHub accounts behind the commits to what the print
edition prints - its pages that are not generated, and the images they
reference - most commits first, each with the name its GitHub profile shows.
Anonymous commits - whose e-mail maps to no GitHub account - bot accounts,
software agents and the IDs excluded in tools/pdf/print.yml are not listed, and
the names of excluded IDs are never looked up.

The list is committed as tools/pdf/authors.yml, so a PDF build stays offline
and reproducible, and a changed list shows up in review. The hand-maintained
`authors` section of tools/pdf/print.yml names authors whose profile shows no
name or who print with a title, and excludes IDs; the build applies it to the
committed list (`load_imprint_names`). Each run adds the authors that section
does not list yet, without a name, so every name to maintain is in one place
(`prefill_names`). Invoked by `task pdf:authors`. Requests use GITHUB_TOKEN or
GH_TOKEN, else the token of a logged-in GitHub CLI: without a token GitHub
allows 60 requests an hour, and a run takes one per author and one per hundred
commits.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import click
import yaml

REPOSITORY = "eccenca/documentation.eccenca.com"
AUTHORS_YML = Path("tools/pdf/authors.yml")
# The hand-maintained names and exclusions: `authors` in the print configuration.
PRINT_YML = Path("tools/pdf/print.yml")
API = "https://api.github.com"
# Agents commit under ordinary accounts of type User, so they are named here.
AGENT = re.compile(r"claude|codex", re.IGNORECASE)


@dataclass(frozen=True)
class AuthorRules:
    """The hand-maintained part of the author list, keyed by GitHub ID in lower case.

    `names` holds the name an author prints with - one the GitHub profile does
    not show, or one with a title. `exclude` holds the IDs that are never listed.
    """

    names: dict[str, str] = field(default_factory=dict)
    exclude: frozenset[str] = frozenset()

    def excludes(self, login: str) -> bool:
        return login.casefold() in self.exclude

    def name(self, login: str) -> str | None:
        return self.names.get(login.casefold())


def load_author_rules(path: Path = PRINT_YML) -> AuthorRules:
    """The `authors` section of the print configuration; without one, nothing is renamed or excluded."""
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    section = data.get("authors") or {}
    if not isinstance(section, dict):
        raise click.ClickException(f"{path}: authors holds `names` and `exclude`")
    names = section.get("names") or {}
    exclude = section.get("exclude") or []
    # A name left empty is not given: the imprint prints the profile's.
    if not isinstance(names, dict) or not all(
        isinstance(login, str) and (name is None or isinstance(name, str)) for login, name in names.items()
    ):
        raise click.ClickException(f"{path}: authors.names maps GitHub IDs to the names they print with")
    if not isinstance(exclude, list) or not all(isinstance(login, str) for login in exclude):
        raise click.ClickException(f"{path}: authors.exclude is a list of GitHub IDs")
    return AuthorRules(
        names={login.casefold(): name.strip() for login, name in names.items() if name and name.strip()},
        exclude=frozenset(login.casefold() for login in exclude),
    )


def select_authors(contributors: list[dict], rules: AuthorRules = AuthorRules()) -> list[dict]:
    """The contributors the imprint lists, in its order: most commits first, ties by ID, case-insensitive."""
    people = [
        c for c in contributors
        if c.get("type") == "User"
        and c.get("login")
        and not AGENT.search(c["login"])
        and not rules.excludes(c["login"])
    ]
    people.sort(key=lambda c: (-int(c["contributions"]), c["login"].casefold()))
    return [{"id": c["login"], "commits": int(c["contributions"])} for c in people]


def add_names(authors: list[dict], profile_name: Callable[[str], str | None]) -> list[dict]:
    """Each author with the name its GitHub profile shows, or None when it shows none."""
    return [
        {"id": author["id"], "name": (profile_name(author["id"]) or "").strip() or None, "commits": author["commits"]}
        for author in authors
    ]


def imprint_names(authors: list[dict], rules: AuthorRules) -> tuple[list[str], list[str]]:
    """The names the imprint prints, in order, and the IDs that print as themselves for want of a name.

    A name in the rules comes first, then the profile's. Excluded IDs are left
    out, also when the committed list predates their exclusion.
    """
    names: list[str] = []
    unnamed: list[str] = []
    for author in authors:
        login = str(author["id"])
        if rules.excludes(login):
            continue
        name = rules.name(login) or author.get("name")
        if not name:
            unnamed.append(login)
        names.append(name or login)
    return names, unnamed


def load_imprint_names(
    authors_yml: Path = AUTHORS_YML, print_yml: Path = PRINT_YML
) -> tuple[list[str], list[str]]:
    """`imprint_names` for the committed author list and the print configuration."""
    data = yaml.safe_load(authors_yml.read_text(encoding="utf-8")) or {}
    return imprint_names(data.get("authors") or [], load_author_rules(print_yml))


def names_entry(login: str, profile_name: str | None) -> str:
    """An `authors.names` line that gives no name, with the profile's name in its comment."""
    # Dumped, so a login YAML would read as something else - `null`, `yes` - is quoted.
    key = yaml.safe_dump({login: None}, allow_unicode=True).rstrip("\n").removesuffix(" null")
    note = f"GitHub profile: {' '.join(profile_name.split())}" if profile_name else "no name on the GitHub profile"
    return f"    {key}  # {note}"


def prefill_names(text: str, authors: list[dict]) -> tuple[str, list[str]]:
    """The print configuration with an `authors.names` entry for each author it neither lists nor excludes.

    Returns the text and the IDs added. An added entry gives no name, so the
    imprint keeps printing the profile's until someone fills one in. The file is
    edited as text, so its comments stay, and read back to make sure the new
    entries are all that changed.
    """
    before = yaml.safe_load(text) or {}
    section = before.get("authors") or {}
    listed = {str(login).casefold(): name for login, name in (section.get("names") or {}).items()}
    known = set(listed) | {str(login).casefold() for login in (section.get("exclude") or [])}
    missing = [author for author in authors if str(author["id"]).casefold() not in known]
    if not missing:
        return text, []
    ids = [str(author["id"]) for author in missing]
    entries = [names_entry(login, author.get("name")) for login, author in zip(ids, missing)]

    lines = text.splitlines()
    top = next((i for i, line in enumerate(lines) if re.match(r"authors:\s*(#.*)?$", line)), None)
    if top is None:
        lines += ["", "authors:", "  names:", *entries, "  exclude: []"]
    else:
        # The section runs until the next line that starts at the margin.
        end = next(
            (i for i in range(top + 1, len(lines)) if lines[i].strip() and not lines[i].startswith(" ")),
            len(lines),
        )
        names = next((i for i in range(top + 1, end) if re.match(r"  names:", lines[i])), None)
        if names is None:
            lines[top + 1:top + 1] = ["  names:", *entries]
        else:
            lines[names] = re.sub(r":\s*\{\s*\}", ":", lines[names], count=1)
            last = names
            for i in range(names + 1, end):
                if not lines[i].strip():
                    continue
                if not lines[i].startswith("    "):
                    break
                last = i
            lines[last + 1:last + 1] = entries
    result = "\n".join(lines) + "\n"

    after = yaml.safe_load(result) or {}
    after_section = after.get("authors") or {}
    after_names = {str(login).casefold(): name for login, name in (after_section.get("names") or {}).items()}
    others = lambda data: {key: value for key, value in data.items() if key != "authors"}
    if (
        after_names != {**listed, **{login.casefold(): None for login in ids}}
        or (after_section.get("exclude") or []) != (section.get("exclude") or [])
        or others(after) != others(before)
    ):
        raise click.ClickException(
            f"cannot add {', '.join(ids)} to authors.names of the print configuration - add them by hand"
        )
    return result, ids


def next_page(link_header: str) -> str | None:
    """The `rel="next"` URL of a GitHub Link header, if there is one."""
    match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return match.group(1) if match else None


TOKEN_HINT = "set GITHUB_TOKEN or GH_TOKEN, or log in with `gh auth login`"


def github_token() -> tuple[str | None, str | None]:
    """The token for the GitHub API, and where it comes from.

    GITHUB_TOKEN or GH_TOKEN when set, else the token the GitHub CLI is logged in
    with. Without either, requests go out unauthenticated.
    """
    for variable in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(variable):
            return os.environ[variable], variable
    gh = shutil.which("gh")
    if gh is None:
        return None, None
    try:
        result = subprocess.run([gh, "auth", "token"], capture_output=True, text=True, timeout=10, check=False)
    except (OSError, subprocess.SubprocessError):
        return None, None
    token = result.stdout.strip() if result.returncode == 0 else ""
    return (token, "the GitHub CLI") if token else (None, None)


def api_failure(error: urllib.error.HTTPError, url: str, authenticated: bool) -> str:
    """What a failed GitHub API request means, and what to do about it."""
    headers = error.headers or {}
    reset, retry = headers.get("X-RateLimit-Reset"), headers.get("Retry-After")
    limited = headers.get("X-RateLimit-Remaining") == "0" or retry or "rate limit" in str(error.reason).lower()
    if error.code in (403, 429) and limited:
        if reset and str(reset).isdigit():
            when = f"; it resets at {time.strftime('%H:%M', time.localtime(int(reset)))}"
        elif retry and str(retry).isdigit():
            when = f"; retry in {retry} seconds"
        else:
            when = ""
        advice = "" if authenticated else f" - {TOKEN_HINT} for 5,000 requests an hour"
        return f"the GitHub API rate limit is exceeded{when}{advice}"
    if error.code == 401:
        return "GitHub rejected the token (HTTP 401) - check GITHUB_TOKEN, GH_TOKEN or `gh auth status`"
    return f"the GitHub API answered HTTP {error.code} {error.reason} for {url}"


def get_json(url: str, token: str | None) -> tuple[object, str | None]:
    """A GitHub API response, and the URL of its next page.

    A failed request ends the command with what it means, not with a traceback.
    """
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response), next_page(response.headers.get("Link", ""))
    except urllib.error.HTTPError as error:
        raise click.ClickException(api_failure(error, url, token is not None)) from error
    except (urllib.error.URLError, TimeoutError) as error:
        raise click.ClickException(f"cannot reach the GitHub API ({getattr(error, 'reason', error)})") from error


# The marker a generated page carries (.claude/docs-guidelines/repo-conventions.md).
GENERATED_MARK = re.compile(r"generated - do not change it manually|auto-generated", re.IGNORECASE)
# An image a page references, in Markdown or as an <img> element.
IMAGE_REFERENCE = re.compile(r'!\[[^\]]*\]\(\s*<?([^)\s>]+)|<img\b[^>]*\bsrc="([^"]+)"')


def printed_pages() -> list[str]:
    """The pages the print edition prints, after the section rules of print.yml."""
    # Imported here: tools.build_pdf imports this module for the imprint.
    from tools.build_pdf import apply_section_rules, load_nav_entries, load_section_rules

    entries, _ = apply_section_rules(load_nav_entries(), load_section_rules())
    return [entry.md for entry in entries if entry.md]


def printed_files(pages: list[str], docs_dir: Path = Path("docs")) -> list[Path]:
    """The source files of printed pages: the pages that are not generated, and the images they reference.

    A generated page credits whoever ran its generator, so it does not count.
    """
    files: list[Path] = []
    for md in pages:
        page = docs_dir / md
        if not page.is_file():
            continue
        text = page.read_text(encoding="utf-8", errors="ignore")
        if GENERATED_MARK.search("\n".join(text.splitlines()[:15])):
            continue
        files.append(page)
        for match in IMAGE_REFERENCE.finditer(text):
            source = urllib.parse.unquote((match.group(1) or match.group(2)).split("#")[0].split("?")[0])
            if not source or source.startswith(("http://", "https://", "data:", "/")):
                continue
            image = Path(os.path.normpath(page.parent / source))
            if image.is_file() and image not in files:
                files.append(image)
    return files


def file_commits(files: list[Path], repo: Path = Path("."), env: dict | None = None) -> dict[str, str]:
    """The commits of the files, without merges and following renames: each hash with its author's e-mail."""

    def log(path: Path) -> list[list[str]]:
        result = subprocess.run(
            ["git", "log", "--no-merges", "--follow", "--format=%H%x09%ae", "--", str(path)],
            cwd=repo, env=env, capture_output=True, text=True, check=False,
        )
        return [line.split("\t", 1) for line in result.stdout.splitlines() if "\t" in line]

    commits: dict[str, str] = {}
    # One `git log` per file: --follow follows a single path only.
    with ThreadPoolExecutor(max_workers=8) as pool:
        for rows in pool.map(log, files):
            commits.update(rows)
    return commits


def commit_accounts(commits: list[dict]) -> tuple[dict[str, dict], dict[str, dict]]:
    """The GitHub accounts behind commits, from the commits API: by commit hash, and by author e-mail.

    The e-mail names the account of a commit the API does not list - one that is
    not pushed yet, or that was made on another branch.
    """
    by_sha: dict[str, dict] = {}
    by_email: dict[str, dict] = {}
    for item in commits:
        author = item.get("author") or {}
        if not author.get("login"):
            continue
        account = {"login": author["login"], "type": author.get("type", "User")}
        by_sha[item["sha"]] = account
        email = ((item.get("commit") or {}).get("author") or {}).get("email")
        if email:
            by_email.setdefault(email.casefold(), account)
    return by_sha, by_email


def count_commits(commits: dict[str, str], by_sha: dict[str, dict], by_email: dict[str, dict]) -> list[dict]:
    """Contributor records - login, type and commits - counting each commit once.

    A commit that maps to no account is anonymous and left out.
    """
    counts: Counter = Counter()
    types: dict[str, str] = {}
    for sha, email in commits.items():
        account = by_sha.get(sha) or by_email.get(email.casefold())
        if account is None:
            continue
        counts[account["login"]] += 1
        types[account["login"]] = account["type"]
    return [{"login": login, "type": types[login], "contributions": count} for login, count in counts.items()]


def fetch_commits(repository: str, token: str | None) -> list[dict]:
    """Every commit the GitHub API lists for the repository's default branch, following the pagination."""
    url: str | None = f"{API}/repos/{repository}/commits?per_page=100"
    commits: list[dict] = []
    while url:
        page, url = get_json(url, token)
        commits.extend(page)
    return commits


def fetch_profile_name(login: str, token: str | None) -> str | None:
    """The name a GitHub account's public profile shows, if it shows one."""
    profile, _ = get_json(f"{API}/users/{urllib.parse.quote(login)}", token)
    return profile.get("name")


class IndentedDumper(yaml.SafeDumper):
    """Indents list items under their key, as the repository's yamllint rules require."""

    def increase_indent(self, flow: bool = False, indentless: bool = False) -> None:
        return super().increase_indent(flow, False)


def authors_yaml(repository: str, authors: list[dict]) -> str:
    """The committed file: a header naming its source, then the list in imprint order."""
    header = (
        "---\n"
        "# Generated by `dec-tool pdf-authors` from the commits to the pages of the print\n"
        f"# edition, their GitHub accounts in {repository} and the names on their profiles.\n"
        "# Do not edit - run `task pdf:authors`. Names and exclusions: tools/pdf/print.yml.\n"
    )
    body = yaml.dump(
        {"repository": repository, "authors": authors},
        Dumper=IndentedDumper, sort_keys=False, allow_unicode=True,
    )
    return header + body


@click.command(name="pdf-authors")
@click.option(
    "--repository",
    default=REPOSITORY,
    help="Which GitHub repository maps the commits to accounts?",
    show_default=True,
)
@click.option(
    "--output-file", "-o",
    type=click.Path(exists=False, dir_okay=False, file_okay=True),
    default=str(AUTHORS_YML),
    help="Where to write the author list?",
    show_default=True,
)
def pdf_authors(repository: str, output_file: str) -> None:
    """Write the imprint's author list from the commits to the printed pages and the authors' profile names."""
    token, source = github_token()
    if source:
        # Flushed, so the line comes before an error message also when the output is piped.
        print(f"Using the GitHub token from {source}", flush=True)
    else:
        print(
            "WARNING: no GitHub token - GitHub allows 60 requests an hour without one, and this run takes one "
            f"per author and one per hundred commits; {TOKEN_HINT}",
            file=sys.stderr,
        )
    rules = load_author_rules()
    files = printed_files(printed_pages())
    commits = file_commits(files)
    print(f"{len(commits)} commits to {len(files)} printed files", flush=True)
    by_sha, by_email = commit_accounts(fetch_commits(repository, token))
    authors = select_authors(count_commits(commits, by_sha, by_email), rules)
    if not authors:
        raise click.ClickException("no author found in the commits to the printed pages")
    authors = add_names(authors, lambda login: fetch_profile_name(login, token))
    Path(output_file).write_text(authors_yaml(repository, authors), encoding="utf-8")
    print(f"{len(authors)} authors written to {output_file}")
    prefilled, added = prefill_names(PRINT_YML.read_text(encoding="utf-8"), authors)
    if added:
        PRINT_YML.write_text(prefilled, encoding="utf-8")
        print(f"{len(added)} authors added to authors.names in {PRINT_YML}: {', '.join(added)}")
    _, unnamed = imprint_names(authors, load_author_rules())
    if unnamed:
        print(
            f"WARNING: {len(unnamed)} authors show no name on their GitHub profile and have none in "
            f"{PRINT_YML} (authors.names), so the imprint prints their ID: {', '.join(unnamed)}",
            file=sys.stderr,
        )
