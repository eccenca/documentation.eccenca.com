---
name: new-documentation-page
description: Create a new page in this documentation - directory and index.md, .pages navigation entry, front matter and tags, page skeleton following the eccenca documentation style guide, plus the lint and build gate. Use for "add a page about X", "document feature X", "create a tutorial for X". Does no git work.
---

# Create a documentation page

## Usage

```text
/new-documentation-page <topic> [--section docs/<section>] [--instance <cmemc connection or URL>]
```

- `<topic>` — what the page documents. Ask when it is missing.
- `--section` — where the page belongs. Otherwise derived from the topic, and asked when two sections are
  equally plausible.
- `--instance` — the deployment the steps are written against, as a cmemc connection name or a URL.
  Without it, no walkthrough is invented: the steps that need the product stay open items in
  `dist/docs-review/<page-slug>.md`.
- `--help` — print this usage summary and stop, without creating anything.

## Scope

- **Do no git work.** No branch, no staging, no commit, no push.
  When the page is finished, offer `suggest-commit-message`.
- **Do not create a page inside a generated directory tree** — see the generator table in
  `.claude/docs-guidelines/repo-conventions.md`. Those directories are wiped on the next generator run.
- Create one page at a time, in an existing section, unless a new section is explicitly requested.

## Steps

### 1. Place the page

Determine the section it belongs to — `docs/build/`, `docs/explore-and-author/`, `docs/automate/`,
`docs/deploy-and-configure/`, `docs/consume/`, `docs/develop/`, `docs/getting-started/`, `docs/tutorials/`,
`docs/distribution/`, `docs/release-notes/`.
If two sections are equally plausible, ask; the choice determines the URL and the navigation.

Check that the topic is not already covered elsewhere — extending an existing page is usually better than a
second page on the same subject (`repo-conventions.md`, "One topic, one page").

Create the directory and its `index.md`:

```text
docs/<section>/<page-slug>/index.md
```

`<page-slug>` is lowercase and hyphen-separated, and short enough to stay readable as a URL.

### 2. Front matter

```yaml
---
tags:
  - <tag from the mapping in mkdocs.yml>
---
```

Only tags mapped under `extra.tags` in `mkdocs.yml` render with an icon.
Add `icon:` when the section lists its pages with icons, and `status: new` for a page documenting a feature of
the upcoming release.

### 3. Navigation

Add the page to the `.pages` file of its directory, in the position where a reader would expect it — a
tutorial after the concepts it needs:

```yaml
nav:
    - <Menu title>: <page-slug>
```

The menu title and the `# Heading` of the page must correspond.
If the directory has no `.pages` file, follow how the parent section orders its entries.

Then regenerate the navigation:

```bash
task update:navigation
```

The `.pages` files are the source, but Zensical does not read them.
`mkdocs.yml` pulls in the generated `nav.yml` through `INHERIT`, so a `.pages` entry alone leaves the page out
of the sidebar. Commit `nav.yml` together with the `.pages` change.

### 4. Write the page

Skeleton for a task or tutorial page:

```markdown
# <Sentence-case title>

## Introduction

<What the page covers and what the reader ends up with.>

## Prerequisites

<Installed vocabularies, existing graphs, permissions, sample files.>

## 1 <First step>

...
```

Skeleton for a reference or concept page: Introduction, then the concepts, then configuration, then a
troubleshooting or limitations section where it applies.

Follow `.claude/docs-guidelines/style-guide.md` while writing — imperative without "you" (3.2), bold for UI
elements (1.1), backticks for values (1.4), field values as lists (3.4), present tense (3.6), one sentence per
line (4.8) — and `.claude/docs-guidelines/repo-conventions.md` for links, icons, fences and admonitions.

Every documented step must have been performed against a running instance, or be recorded as an open item in
`dist/docs-review/<page-slug>.md`; see `.claude/docs-guidelines/live-verification.md`.
Do not write a walkthrough from assumption.

### 5. Images

Screenshots live next to the `index.md`, are named lowercase and hyphen-separated, carry descriptive alt text
and `class="bordered"`, and show only the relevant part of the interface with clearly fictional data.

### 6. Gate

```bash
task format:fix
task check          # link check, rumdl, yamllint, nav drift, build output
```

`task check` is the gate, not `task build` on its own: `zensical build --strict` compiles a page that is
missing from the navigation without complaining, and only `check:navigation` catches `nav.yml` drifting from
the `.pages` files.

Check the page in the local server (`task serve`): navigation entry, title, step numbering, image widths.

### 7. Report

Summarize which files were created, which navigation file changed, what is still open (screenshots,
verification), and that nothing is committed.
