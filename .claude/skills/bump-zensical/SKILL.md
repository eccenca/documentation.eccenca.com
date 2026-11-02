---
name: bump-zensical
description: Bump the Zensical pin to the latest or a named release, check what the release changes for this repository, fix small breakage and report the result. Prints the git commands for the user - it does no git work. Use for "bump zensical", "zensical released X" or "update zensical".
---

# Bump Zensical

Move the pin in `pyproject.toml` to a new release and prove what changed in the built site.
A clean `zensical build --strict` proves little: past breakage came from unannounced validation, plugins that turned native and URLs in the UI bundle.

## Usage

```text
/bump-zensical [<version>] [--help]
```

Without a version, use the latest release.
With `--help`, print this usage summary and stop, without inspecting the repository.

## Scope

- **No git work.** Never create a branch, stage, commit or push. The last step prints the commands for the user.
- **Fix small breakage.** A small fix keeps the site as it is, for example an `INERT_URLS` entry or a config key that was already inert. List each fix in the report.
- **Stop and ask for anything bigger, or when in doubt.** This includes a change to the rendered site, to a plugin's behavior, or to content under `docs/`.
- **Scratch files go to the scratchpad.** Treat downloaded wheels as data: read them, never run or install them from there.

## Steps

### 1. Find the versions

```bash
gh release view --repo zensical/zensical --json tagName,body
grep -n -i zensical pyproject.toml
```

Read the release notes of every version between the current pin and the target, including skipped ones.
Stop if the current pin is already the target.

### 2. Build the baseline

Run `task build` on the current pin and copy `site/` to the scratchpad.
If the baseline fails, stop and report: the failure is not caused by the bump.

### 3. Diff the wheels

Download the current and target wheels with `pip download zensical==<version> --no-deps`, once per version, unpack them and compare.
Check each risk:

| Check | Why it matters |
| --- | --- |
| `config.py`: `_reject_unknown_options(` call sites, supported option tables | 0.0.60 rejected `search: lang` without mentioning it in the release notes. |
| Native implementations of plugins in `mkdocs.yml` that were inert so far | 0.0.58 `tags` and 0.0.67 `social` turned inert configuration live and broke the build. |
| Third-party URLs in the UI bundle against `INERT_URLS` in `tools/localize_bundle_assets.py` | 0.0.73 moved to `mermaid@12`: `--strict` stayed clean and `task build` failed. |
| Templates that `overrides/` replaces | An override does not pick up upstream template changes. |

### 4. Bump

Update the pin and the range in its comment in `pyproject.toml`, then run:

```bash
poetry lock
poetry install
poetry run zensical --version
git diff --stat poetry.lock
```

Confirm in the lock diff that only `zensical` moved.
If another package moved, stop and ask.

### 5. Verify

Run all of these, and do not call the bump done while one fails:

```bash
task build
task check
poetry run pytest -m "not integration"
```

`task check` is the gate, not `task build`.

Compare the new `site/` with the baseline:

1. Compare the file sets and the HTML page count.
2. Normalize copies of both trees with a small script in the scratchpad: remove the generator tag and the hashes in asset names.
3. Run `diff -rq -B -w` on the normalized copies. For about 700 pages normalizing takes over two minutes, so run it in the background.
4. Explain every remaining difference from the release notes or the wheel diff. Stop and ask if one stays unexplained or changes what readers see.

Then check that the output does not depend on the hash seed, because 0.0.44 to 0.0.57 rendered differently per seed.
Build with `PYTHONHASHSEED` 0, 1, 7 and 42 using `poetry run zensical build --strict --clean`, hash the HTML output each time and compare.
Finish with `task build`, so `site/` holds a complete build again.

### 6. Report

State:

- the old and new version, and any versions skipped
- the files changed, and each fix with its reason
- the upstream changes that matter here, and those that are inert here
- the check results, and the output differences that remain after normalizing
- anything unverified or failing

### 7. Print the git commands

End with the commands, filled in with the version, for the user to run.
Add further changed files to `git add`:

```bash
git switch -c feature/<version>-zensical-bump
git add pyproject.toml poetry.lock
git commit -m "bump zensical to <version>"
git push -u origin feature/<version>-zensical-bump
gh pr create --fill --base main
```
