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
- Add the page to the `.pages` file of its directory (awesome-pages plugin) with the title used in the menu.
- The page title (`# Heading`) and the `.pages` nav title must correspond.
- Images live next to the `index.md` that uses them.
- Renaming or moving a page requires an entry in `redirect_maps` in `mkdocs.yml` (mkdocs-redirects).

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

## Links

- Relative links to the target `index.md`: `[Property Shapes](property-shapes/index.md)`, `[cmemc](../../automate/cmemc-command-line-interface/index.md)`.
- No absolute links to `https://documentation.eccenca.com/latest/...` for internal pages.
- No base-relative links such as `/automate/...`.
- Same-page references use a plain anchor: `[Configure OAuth clients](#configure-oauth-clients-helm)`, never a full path back to the same file.
- `task check:links` runs the link checker; `task build` runs `mkdocs build --strict` and fails on unresolved internal links.

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

## Markdown linting

```bash
task format:fix     # rumdl --fix over ./docs and ./*.md
task check          # link check + rumdl report (does not fail the stage)
task build          # mkdocs build --strict
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
