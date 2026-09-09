# Verifying documentation against a live instance

How the documentation skills check a page against a running eccenca Corporate Memory deployment, and how a
check that could not be performed is recorded so that it can be completed later.

## Choosing an instance

An instance can be named in three ways, in this order of precedence:

1. Explicitly in the prompt: `/review-documentation-page <page> --instance mycmem` or a URL.
2. `CMEMC_CONNECTION` in the environment, or a `.env` file in the repository root.
3. A connection configured in cmemc — `cmemc config list --id-only` lists the connection names.

Check reachability before relying on it.
`admin status` prints the version and health information of the deployment, and warns when the cmemc client
is newer than the backend:

```bash
cmemc -c <connection> admin status
```

If no instance is named and none is reachable, do not stop and do not guess.
Continue with everything that can be checked from the sources (Markdown, `mkdocs.yml`, generator output,
linter) and record every product-dependent claim as an open item, as described below.

Never verify against a customer deployment, and never put data from one into a screenshot (style guide 5.3).

## What to verify against the product

- Every UI label, button, tab, menu entry, and field name quoted on the page (style guide 2.1).
- The order of steps: does the documented flow still work in the current version?
- Required fields that the page does not mention, and fields the page mentions that no longer exist.
- Non-obvious interactions that the page omits — a value that has to be confirmed by selecting a suggestion,
  a field that has to be added through a menu before it can be filled (style guide 2.4).
- Screenshots: labels, icons, navigation, dialogs, field names, layout (style guide 5.2).
- Numbers and counts stated as fact — triple counts, result sizes, durations.
  If a number cannot be reproduced, remove it rather than restate it.
- CLI output shown in `shell-session` blocks: run the command and compare.

Tools:

- The browser (Playwright MCP) for anything in the web UI.
- `cmemc` for CLI behavior, command output, and API-level facts.
- `cmemc --version` for the CLI version, `cmemc -c <connection> admin status` for the deployment version.

Record the version that was checked, in the form used in the commit history:
"Verified against CMEM v26.2.0". The documentation version currently being written is `CURRENT_VERSION` in
`Taskfile.yml`.

## Screenshots

Only take screenshots when the instance is reachable and the existing image is actually wrong — a screenshot
that still matches the product is left alone.

- Capture the relevant part of the interface, not the whole desktop (style guide 5.4, `CONTRIBUTING.md`).
- Crop scrollbars, keep an even margin, use the same framing for screens that appear next to each other.
- Save into the page directory, lowercase and hyphen-separated: `create-person-node-shape.png`.
- Use clearly fictional example data.
- Reference it with descriptive alt text and `{ class="bordered" }`, plus a width for dialogs.
- Delete images that are no longer referenced after the rewrite.

If the user prefers to take screenshots themselves, list exactly which images are needed, what each one has to
show, and under which file name it should be saved.

## Deferred verification

Findings are written to `dist/docs-review/<page-slug>.md`.
`dist/` is gitignored, so a report never becomes part of a commit.

Each finding carries a status:

- `[confirmed]` — checked against the product or against a repository source.
- `[open]` — a defect that is certain from the source alone (broken link, lint violation, style guide breach).
- `[needs-instance]` — cannot be decided without a running deployment.

Report format:

```markdown
# Review: <page path>

Instance: none | <connection or URL>, checked <version>
Date: <YYYY-MM-DD>
Status: 7 confirmed, 3 needs-instance

## needs-instance

- [needs-instance] R1 — Section "2 Uploading of the data": the **Add new graph** checkbox is documented,
  but the dialog may have changed in 26.2. Check the second wizard step.
- [needs-instance] R2 — Screenshot `create-workflow.png` was taken on 24.1. Compare against the current
  workflow editor, reshoot if the toolbar differs.

## confirmed

- [confirmed] R3 — Style guide 4.2: "CMEM" in prose text, line 34. -> "eccenca Corporate Memory".
```

When a skill runs on a page that already has a report:

1. Read the existing report.
2. If an instance is now available, work through the `needs-instance` items first and update their status.
3. Re-check the rest of the page as usual, and merge new findings into the report.

This is why no separate skill is needed for catching up on verification: run the same skill again on the same
page and name the instance.
