# Working in this repository

This is the source of [documentation.eccenca.com](https://documentation.eccenca.com), the user documentation
for eccenca Corporate Memory. It is a Markdown tree under `docs/`, built with
[Zensical](https://zensical.org/) and published per version with `mike`.

The documentation is a product surface: what is written here is what users are told the product does. A page
that describes a flow the product no longer has is a defect, the same as a broken link.

## The rules live in `.claude/docs-guidelines/`

Read the file that covers the change before making it. They are the authority, not this page.

| File | Covers |
| --- | --- |
| `style-guide.md` | the editorial rules, numbered and cited by number (`field values as lists (3.4)`) |
| `repo-conventions.md` | generated files, navigation, links, images, icons, fences, admonitions, linting |
| `live-verification.md` | checking a page against a running deployment, and recording what could not be checked |

`style-guide.md` is a transcription of the Confluence page *eccenca Documentation Style Guide*. Do not invent
rules or renumber it — a convention this repository decided for itself belongs in `repo-conventions.md`.

## Skills do the documentation work

- `new-documentation-page` — create a page, its navigation entry and front matter.
- `review-documentation-page` — read-only review against the guidelines and the product; writes a report.
- `update-documentation-page` — rewrite a page against the product and the style guide.
- `suggest-commit-message` — print a commit message in the style of this repository.

They do no git work: no branch, no staging, no commit, no push. Committing is the user's decision.

## Four things that are easy to get wrong

**Most files under `docs/` are generated.** About 500 of 664. They carry a `generated` marker, except the
`graph-insights` files declared in a `_README.md`. Check before editing anything:

```bash
head -5 <file> | grep -i "generated"
```

A finding in a generated file becomes a report for a ticket against the generator, never an edit to the
Markdown.

**A `.pages` entry alone does not add a page to the navigation.** Zensical does not read `.pages`; the sidebar
comes from the generated `nav.yml`, pulled in by `INHERIT` at the top of `mkdocs.yml`. Run
`task update:navigation` to update `nav.yml` with the `.pages` change. `zensical build --strict` compiles an
unlisted page without complaining — only `task check` catches the drift.

**A page has three titles, and they need not be the same.** The `.pages` entry is the menu label, `title:` in
the front matter is the site page title and the tags page entry, and the `# Heading` is the visible title on
the page. They serve different purposes — a menu label is written for scanning inside its section. Divergence
between them is not drift and is not something to correct.

**`task check` is the gate, not `task build`.** It runs the link check, rumdl, yamllint, the navigation check
and the build-output check. Do not leave it failing.

```bash
task format:fix     # rumdl --fix
task check          # the full gate
task serve          # local preview
```

**Do not write a walkthrough from assumption.** Steps, labels, field names and counts are verified against a
running deployment, or recorded as `[needs-instance]` items in a report under `dist/` (gitignored). See
`live-verification.md`. Never verify against a customer deployment, and never put customer data in a
screenshot.

## Product naming

**eccenca Corporate Memory** on first mention in prose on a page, **Corporate Memory** afterwards. `CMEM` is
not acceptable in prose — keep it only in literal technical values (`CMEM_BASE_URI`, IRIs, JSON keys).

`cmemc` is exempt and is never expanded: it is the separately branded eccenca command line client, a product
name of its own rather than an abbreviation.

## Prose conventions that apply everywhere

One sentence per line in the Markdown source (4.8) — it is what makes a diff reviewable. Imperative, no "you"
and no "we" (3.1, 3.2). Present tense (3.6). US English (4.3). No contractions (4.9). Bold for UI elements
exactly as the product spells them (1.1), backticks for values (1.4).
