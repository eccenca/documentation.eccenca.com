# Repository conventions

Technical conventions for this mkdocs project, complementing the editorial rules in `style-guide.md`.
Sources: `CONTRIBUTING.md`, `mkdocs.yml`, `Taskfile.yml`, `.markdownlint.jsonc`, plus conventions
established in the page rewrites of 2026-08 and 2026-09.

## Generated files — never edit

About 500 of the 664 Markdown files under `docs/` are generated and carry
`<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->` (variant: `<!-- Auto-Generated. Do not edit directly! -->`).

Additionally, `docs/explore-and-author/graph-exploration/graph-insights/_README.md` declares `concepts.md`,
`tutorial.md` and `features/*.md` as generated **without** those files carrying an inline marker — a
marker-only search misses them.

Check before editing any file:

```bash
head -5 <file> | grep -i "generated"
```

Generators (see `Taskfile.yml`):

| Path | Task |
| --- | --- |
| `docs/automate/cmemc-command-line-interface/command-reference/` | `task update:cmemc` |
| `docs/develop/cmem-client-api/api-reference/` | `task update:cmem-client-api` |
| `docs/build/reference/` (tasks and operators) | `task update:di-reference` |
| `docs/build/integrations/index.md` | `task update:integrations` |
| `docs/explore-and-author/graph-exploration/building-a-customized-user-interface/{node-shapes,property-shapes,datatype-reference}/` | `task update:shape-reference` |
| `overrides/.icons/eccenca/` | `task update:icons` |

Findings in generated files are collected into a report under `dist/` (gitignored) for a ticket against the
generator source — plugin descriptions, Python docstrings, DataPlatform configuration.
They are never fixed in the Markdown.

## Page and navigation structure

- One directory per page with an `index.md` inside: `my-topic/index.md`.
- Add the page to the `.pages` file of its directory with the title used in the menu, then run
  `task update:navigation` — see "Navigation" below.
- A page carries its name in three places, which serve different purposes and are not required to match:
  the `.pages` entry is the label in the navigation menu, `title:` in the front matter is the site page title
  and the entry on the tags page, and the `# Heading` is the visible title on the page itself.
  A menu label is written for scanning inside its section and is often shorter than the heading, which is read
  without that context. Do not "fix" such a divergence as if it were drift.
- The front matter `title` is often written *longer* than the heading, because the tags page lists pages flat,
  without the navigation hierarchy that would say what a page belongs to. The cmemc pages are the model:
  `title: "cmemc: Installation"` against a heading of `Installation`, and the same for every page in that group.
- Images live next to the `index.md` that uses them.
- Renaming or moving a page requires a redirect stub — see "Redirects" below.

### One topic, one page

Cover a subject in one place. Extending an existing page is usually better than adding a second page on the
same subject: two pages describing the same procedure will disagree after the next change to the product.

A page may name what another page documents in detail only where the reader cannot follow the steps without
it — a prerequisite, or a choice that changes which path applies. Link to the other page for the detail
rather than restating it.

Front matter:

```yaml
---
icon: material/table          # optional, shown in section listings
tags:                         # only tags mapped in mkdocs.yml (extra.tags), no duplicates
  - BeginnersTutorial
  - KnowledgeGraph
status: new                   # optional: new | deprecated
---
```

A tag that is not mapped in `mkdocs.yml` renders without an icon — add the mapping or use an existing tag.

## Navigation

The `.pages` files are the source of the navigation, but Zensical does not read them. `mkdocs.yml` starts with
`INHERIT: nav.yml`, and `nav.yml` is generated from the `.pages` files:

```bash
task update:navigation      # dec-tool build-navigation - rewrites nav.yml
task check:navigation       # fails when nav.yml and the .pages files disagree
```

A `.pages` entry on its own therefore leaves the page out of the sidebar, and `zensical build --strict` does
not complain about it — the page compiles and is reachable by URL, only unlisted. `check:navigation`, part of
`task check`, is what catches this. Commit `nav.yml` together with the `.pages` file that changed.

## Redirects

The `mkdocs-redirects` plugin is not implemented by Zensical, so a moved page leaves a hand-written stub
behind: an `index.html` at the old path under `docs/`, which Zensical copies into `site/` verbatim.
`docs/cmemc/index.html` is the model — relative `http-equiv` refresh and visible link so that they survive
mike's versioned prefixes, absolute canonical URL, `robots: noindex, follow`.

Register the stub in `REDIRECTS` in `tools/check_zensical_output.py`; `task check:output` then fails if it
disappears or stops pointing at its target.

## Links

- Relative links to the target `index.md`: `[Property Shapes](property-shapes/index.md)`, `[cmemc](../../automate/cmemc-command-line-interface/index.md)`.
- No absolute links to `https://documentation.eccenca.com/latest/...` for internal pages.
- No base-relative links such as `/automate/...`.
- Same-page references use a plain anchor: `[Configure OAuth clients](#configure-oauth-clients-helm)`, never a full path back to the same file.
- `task check:links` runs the link checker; `task build` runs `zensical build --strict` and fails on unresolved internal links.

## Images

```markdown
![Creating the Node Shape with Name and Target class](create-person-node-shape.png){ class="bordered" width="70%" }
```

- Alt text is descriptive and states what the screenshot shows (style guide 5.6). Empty `![]()` is not acceptable.
- `class="bordered"` on every product screenshot (436 uses in the tree).
- `width="50%"` or `width="70%"` for dialogs and modals, no width for full-screen views. Keep the width
  consistent within one page.
- `.off-glb` opts an image out of the glightbox lightbox — used for inline icons and decorative images.
- File names: lowercase, hyphen-separated, descriptive (style guide 5.5).
- Delete screenshots that are no longer referenced. Orphan check for one page directory:

```bash
for img in <dir>/*.png; do grep -q "$(basename "$img")" <dir>/*.md || echo "orphan: $img"; done
```

## Icons

- Icon shortcode = file name in `overrides/.icons/eccenca/` without the extension: `application-explore.svg` -> `:eccenca-application-explore:`.
- Module and application references carry their icon before the bold name:
  `:eccenca-application-explore: **Knowledge Graphs**`.
- Frequently used: `:eccenca-item-add-artefact:` (create/add), `:eccenca-item-edit:`, `:eccenca-item-moremenu:`,
  `:eccenca-toggler-showmore:`, `:eccenca-item-info:`, `:eccenca-artefact-project:`.
- Material icons (`:material-cog-outline:`) only where no eccenca icon exists.
- Never a PNG of an icon, never a similar-looking substitute (style guide 5.1).

## Admonitions

```markdown
!!! info "Optional title"

    Content indented by 4 spaces.
```

Types and their purpose (from `CONTRIBUTING.md`): `info` (essential detail on the topic), `note` (additional,
possibly tangential detail), `abstract` (summary at the start of a page), `warning` (risk of data loss or
unexpected change), `tip` (best practice or shortcut), `success`, `bug`, `example`, `task`.
`???` makes an admonition collapsible — prefer inline admonitions for screenshots that a reader needs to follow the steps.

## Content tabs

Used to document alternative paths, most often UI versus CLI:

```markdown
=== "Corporate Memory"

    1. Click ...

=== "cmemc"

    ``` shell-session
    $ cmemc graph import ...
    ```
```

Content inside a tab is indented by 4 spaces.

## Code blocks

Language identifiers, based on the usage in the generated reference pages (consistent there) and `CONTRIBUTING.md`:

| Identifier | Use for |
| --- | --- |
| `shell-session` | terminal sessions: commands prefixed with `$` plus their output |
| `bash` | shell scripts, environment variable assignments, anything with a shebang |
| `python`, `json`, `yaml`, `sparql`, `turtle`, `xml`, `text`, `ini`, `conf`, `sql` | content of that type |

Rules:

- `shell-session` requires the `$` prompt on every command line. A block without a prompt is not a session — use `bash`.
- Do not use `console` (0 occurrences; it was converted to `shell-session`).
- Do not use `shell` for new content. It is a Pygments alias of `bash`, and using both splits the convention
  (71 `shell` versus 40 `bash` blocks in hand-written pages). `CONTRIBUTING.md` names `bash`.
- No line numbers unless the text refers to them.
- A title is helpful on longer blocks: ` ```yaml title="values.yaml" `.

Known drift to fix when touching a page: 32 `shell-session` blocks in hand-written pages have no `$` prompt.

## Lists and indentation

- Nested list content is indented by 4 spaces (`MD007`, `.markdownlint.jsonc`).
- A screenshot or admonition inside a numbered step must be indented to the step's content level, otherwise the
  numbering restarts at 1 in the rendered page. Check the rendered result for any step list you touch.
- `sane_lists` is enabled: an unordered item does not continue an ordered list.

## Editorial decisions beyond the style guide

`style-guide.md` is a transcription of the Confluence page and is not extended locally.
These are the rulings this repository made where the transcription leaves room.
Cite them by heading, the way style guide rules are cited by number.

### The cmemc exemption

Style guide 4.2 keeps `CMEM` out of prose and allows it only in literal technical values.
`cmemc` is not covered by that rule and is never expanded: it is the separately branded eccenca command line
client, a product name of its own rather than an abbreviation of Corporate Memory.
It appears in 186 files under `docs/`, in prose as well as in commands, and is correct in both.

The same applies to identifiers that carry the string verbatim — `CMEM_BASE_URI`, `cmem-plugin-base`, module
paths and IRIs. They are written as they are, wherever they appear.

### Do not infer terminology from majority usage

Style guide 4.1 requires one term per concept, and prefers the term the product itself uses.
Do not settle which term that is by counting how often each variant occurs in `docs/`.
Majority usage is frequently the term the team has been trying to retire, and about 500 of the Markdown files
are generated from sources that lag behind the interface, so a count is weighted towards the older wording.
Check the running product, or ask, when the correct term is not obvious.

## Markdown linting

```bash
task format:fix     # rumdl --fix over ./docs and ./*.md
task check          # link check + rumdl report (does not fail the stage)
task build          # zensical build --strict
```

- Config: `.markdownlint.jsonc` (`rumdl --config .markdownlint.jsonc check`).
- `MD044` (proper names) has a `names` allowlist. Resolve new false positives — icon shortcodes, host names,
  environment variables — by adding the longer technical identifier to that allowlist, not by adding
  `rumdl-disable` comments to the prose.
- `MD044` does not inspect Markdown link text. `[Github Actions](x.md)` passes the linter. Search separately:

```bash
grep -rnE '\[[^]]*\b(Gitlab|Github|Javascript|Typescript|Eccenca)\b[^]]*\]' --include='*.md' docs
```

- `MD061` flags contractions and politeness phrases. "cannot" is deliberately allowed.
- `rumdl check` silently ignores a directory when files are passed in the same invocation
  (`rumdl check docs *.md`). The Taskfile avoids this with `find ... -print0 | xargs -0`.

## Enabled mkdocs extensions worth using

`attr_list`, `md_in_html`, `admonition`, `pymdownx.details`, `pymdownx.highlight`, `pymdownx.inlinehilite`,
`pymdownx.snippets`, `pymdownx.keys` (`++tab++`), `pymdownx.tasklist`, `pymdownx.tabbed`,
`pymdownx.superfences` (including mermaid), `toc`, `pymdownx.emoji` with `overrides/.icons`.
Plugins: `awesome-pages`, `autolinks`, `glightbox`, `tags`, `social`, `git-revision-date-localized`, `redirects`, `meta`, `privacy`.
