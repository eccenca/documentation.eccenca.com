---
name: update-documentation-page
description: Rewrite or update an existing documentation page so that it matches the current product and the eccenca documentation style guide, including screenshots and the lint gate. Use for "update page X", "rewrite page X against 26.2", "bring page X in line with the style guide", or "fix the findings on page X". Does no git work.
---

# Update a documentation page

Brings one page back in line with the product and with the style guide.
The order matters: diagnose first, then restructure, then rewrite, then images, then the gate.

## Usage

```text
/update-documentation-page <page> [--instance <cmemc connection or URL>]
```

- `<page>` — a path, a directory, or a page title to resolve. Ask which page is meant when it is missing.
- `--instance` — the deployment to write the page against, as a cmemc connection name or a URL.
  Without it, `CMEMC_CONNECTION` and a `.env` file are used; if nothing is reachable, the page is corrected
  only where the sources allow, and the product-dependent points stay open items in
  `dist/docs-review/<page-slug>.md`.
- `--help` — print this usage summary and stop, without changing anything.

## Scope

- **Do no git work.** No branch, no staging, no commit, no push, no PR.
  When the page is finished, offer `suggest-commit-message`.
- **Never edit a generated file.** Check for the marker first; findings there go into a report for a ticket
  against the generator.
- **Document the product as it behaves, and do not repair the product.** When a step turns out to be broken,
  confusing or self-contradictory in the product itself, write down what actually happens and record the
  defect as a finding for a ticket. Describing the intended behavior instead produces a page that reads
  correctly and cannot be followed, which is the failure that survives review longest.
- Change what is wrong or unclear. Do not reflow a whole page that is already correct.

## Steps

### 1. Diagnose before writing

Run `review-documentation-page` on the page, or read an existing report under `dist/docs-review/`.
Do not start editing until the list of defects exists — the diagnosis is what the change is built on, and it
becomes the body of the commit message later.

Note the product version the page is being written against, and the instance used (see
`.claude/docs-guidelines/live-verification.md`).

### 2. Repair the structure

- Introduction that says what the page is for and what it produces.
- Prerequisites before the steps that need them.
- Setup before Usage when Usage depends on it.
- Numbered sections for a walkthrough, headings in sentence case (style guide 4.6).
- Split a step that changes the screen into separate steps (3.3).
- Remove sections that document a flow the product no longer has.

### 3. Rewrite the text

Apply `.claude/docs-guidelines/style-guide.md` while rewriting, in particular:

- Bold for UI elements exactly as the product spells them (1.1, 2.1), backticks for values (1.4, 2.2).
- Imperative, no "you", no "we" (3.1, 3.2).
- Field values as a list (3.4), optional fields marked as optional (3.5).
- The non-obvious interactions the product requires — confirming a suggestion, adding a field through a menu
  before it can be filled (2.4).
- Present tense (3.6), no filler (3.7), no politeness (3.9), no contractions (4.9).
- One sentence per line in the Markdown source (4.8).
- Full product name on first mention, `CMEM` only inside literal technical values (4.2).
- Remove claims that cannot be reproduced instead of restating them.

Keep the conventions in `.claude/docs-guidelines/repo-conventions.md`: fence identifiers, icons, link form,
4-space indentation, admonition types.

### 4. Bring the images up to date

Follow the screenshot part of `live-verification.md`:

- Replace screenshots that no longer match the UI; leave the ones that still do.
- Descriptive alt text, `class="bordered"`, consistent width for dialogs.
- Delete screenshots that the rewritten page no longer references:

```bash
for img in <dir>/*.png; do grep -q "$(basename "$img")" <dir>/*.md || echo "orphan: $img"; done
```

- Without a reachable instance, do not invent images: list which screenshots are needed, what each has to
  show, and the file name to save it under, and keep them as open items in the report.

### 5. Gate

```bash
task format:fix     # rumdl --fix
poetry run rumdl --config .markdownlint.jsonc check <file>
task build          # zensical build --strict; task check also covers nav drift and links
```

Check the rendered page if the local server is running (`task serve`), especially step numbering and image
widths. Fix what the gate reports; do not leave a failing build behind.

### 6. Report

Summarize in the chat:

- what was wrong and what changed, in the order of the diagnosis,
- which version it was verified against, or that verification is still open,
- which screenshots are still missing,
- that the change is uncommitted, and that `suggest-commit-message` produces the message.
