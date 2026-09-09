---
name: review-documentation-page
description: Review an existing documentation page against the eccenca documentation style guide, the repository conventions and - when an instance is reachable - the running product. Produces a findings report and changes nothing. Use for "review page X", "check page X against the style guide", "what is wrong with page X", or before rewriting a page.
---

# Review a documentation page

Read-only review of one page of this documentation, or of a small set of pages with one report each.
Produces a findings report and a short summary; it does not edit documentation files.

## Usage

```text
/review-documentation-page <page> [--instance <cmemc connection or URL>]
```

- `<page>` — a path (`docs/build/.../index.md`), a directory, or a page title to resolve.
  Ask which page is meant when the argument is missing or ambiguous.
- `--instance` — the deployment to check against, as a cmemc connection name or a URL.
  Without it, `CMEMC_CONNECTION` and a `.env` file are used; if nothing is reachable, product-dependent
  checks become open items in the report instead of being skipped.
- `--help` — print this usage summary and stop, without reviewing anything.

## Scope

- **Do not edit any file under `docs/`.** The only file written is the report under `dist/docs-review/`.
- **Do no git work.** No branch, no staging, no commit, no push.
- To fix the findings afterwards, use `update-documentation-page`.

## Steps

### 1. Resolve the target and check whether it is generated

```bash
head -5 <file> | grep -i "generated"
```

If the file is generated, stop reviewing it as Markdown.
Report which generator owns it (see `.claude/docs-guidelines/repo-conventions.md`) and collect the findings for
a ticket against the generator source instead.
Also check whether a `_README.md` in the directory declares neighbouring files as generated — those carry no
inline marker.

### 2. Load the guidelines

Read, in this order:

- `.claude/docs-guidelines/style-guide.md` — the editorial rules, cited by number.
- `.claude/docs-guidelines/repo-conventions.md` — mkdocs, links, images, icons, fences, lint.
- `.claude/docs-guidelines/live-verification.md` — instance handling and the report format.

Check for an existing report at `dist/docs-review/<page-slug>.md` and resume it rather than starting over.

### 3. Review what the sources can decide

Work through the page and check:

- **Structure** — is there an Introduction? Are prerequisites stated before they are needed? Does a Setup
  section come before the Usage that depends on it? Does the step numbering survive the embedded screenshots
  and admonitions?
- **Style guide** — bold for UI elements (1.1), backticks for values (1.4), consistent interaction verbs (2.3),
  imperative without "you" (3.2), one action per step (3.3), field values as lists (3.4), optional fields marked
  (3.5), present tense (3.6), product name (4.2), US English (4.3), sentence-case headings (4.6), one sentence
  per line (4.8), no contractions (4.9).
- **Conventions** — front matter tags mapped in `mkdocs.yml`, no duplicate tags, `.pages` entry and title
  correspondence, relative links to `index.md`, plain anchors for same-page links, image syntax with alt text
  and `class="bordered"`, eccenca icons instead of Material substitutes, code fence identifiers, `$` prompt in
  `shell-session` blocks, 4-space indentation.
- **Images** — orphaned files in the page directory, empty alt texts, screenshots older than the current
  documentation version (`git log --follow -1 --format=%ad <image>`).
- **Links** — internal targets exist; run the link checker if the page has many outgoing links.
- **Lint** — run rumdl on the single file and read the result:

```bash
poetry run rumdl --config .markdownlint.jsonc check <file>
```

- **Claims** — mark every statement of fact that cannot be checked from the sources: counts, durations,
  version-specific behavior, "the dialog shows ...".

### 4. Verify against the product

If an instance is reachable, follow `live-verification.md`: check the labels, the flow, the required fields, the
non-obvious interactions and the screenshots, and note the version that was checked.
Everything that needs the product and could not be checked becomes a `[needs-instance]` item.

### 5. Write the report and summarize

Write `dist/docs-review/<page-slug>.md` in the format from `live-verification.md`, grouped by status and
ordered by severity: wrong instructions first, then missing steps, then style and convention issues.

In the chat, give the counts, the three or four findings that matter most, and the exact command to continue —
either `update-documentation-page` to fix them, or this skill again with `--instance` to close the open items.
