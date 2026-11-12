# Repository conventions

Technical conventions for this mkdocs project, complementing the editorial rules in `style-guide.md`.
Sources: `CONTRIBUTING.md`, `mkdocs.yml`, `Taskfile.yml`, `.markdownlint.jsonc`, plus conventions
established in the page rewrites of 2026-08 and 2026-09.

## Generated files — never edit

About 500 of the 664 Markdown files under `docs/` are generated and carry
`<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->` (variant: `<!-- Auto-Generated. Do not edit directly! -->`).

Additionally, in `docs/explore-and-author/graph-exploration/graph-insights/`, the files `concepts.md`,
`tutorial.md` and `features/*.md` are generated **without** carrying an inline marker — a marker-only search
misses them.
They are synced from the Graph Insights user guide, which Derivo generates with a single-source Jinja pipeline,
and every sync overwrites manual edits.
Route fixes to the Derivo team (`derivo-company/eccenca-support` on GitHub).
`index.md` and `navigating-to-cmem.md` in the same directory are written here and may be edited.
The upstream `_README.md` that states this does not belong in this repository; do not commit it with a sync.

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
| `<div class="try-result" markdown>` blocks in "Try it" boxes (see below) | `task update:try-results` |

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
- Renaming or moving a page requires a redirect — see "Redirects" below.

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

A renamed, moved or removed page keeps its old URL working through the `redirects` plugin, which Zensical
implements natively since 0.0.61. Add one line to `redirect_maps` in `mkdocs.yml`, from the old Markdown path
to the new one, both relative to `docs/`:

```yaml
plugins:
  - redirects:
      redirect_maps:
        release-notes/corporate-memory-26-2/index.md: release-notes/2026/corporate-memory-26-2/index.md
```

Zensical writes a redirect page at the old URL. Its links are relative, so it survives mike's versioned
prefixes, and it carries a `#fragment` over to the new page. No file may remain at the old path.

`zensical build --strict` fails when a target does not exist or a source is still a page.
`task check:output` resolves every page redirect in the built `site/` and fails when one is missing or lands
somewhere else, which also catches a regression in Zensical's redirect output.

Do not write `index.html` stubs under `docs/`.

## Links

- Relative links to the target `index.md`: `[Property Shapes](property-shapes/index.md)`, `[cmemc](../../automate/cmemc-command-line-interface/index.md)`.
- No absolute links to `https://documentation.eccenca.com/latest/...` for internal pages.
- No base-relative links such as `/automate/...`.
- Same-page references use a plain anchor: `[Configure OAuth clients](#configure-oauth-clients-helm)`, never a full path back to the same file.
- `task check:links` runs [lychee](https://lychee.cli.rs/) over the outgoing http(s) links; exclusions and accepted
  status codes live in `lychee.toml`. `task build` runs `zensical build --strict` and fails on unresolved internal links.
- An IRI written as an autolink (`<https://vocab.eccenca.com/...>`) is checked like any link. Identifier namespaces
  that do not resolve are excluded in `lychee.toml`; add a new one there rather than formatting the IRI differently.

## Images

```markdown
![Creating the Node Shape with Name and Target class](create-person-node-shape.png){ class="bordered" width="70%" }
```

- Alt text is descriptive and states what the screenshot shows (style guide 5.6). Empty `![]()` is not acceptable.
- `class="bordered"` on every product screenshot (436 uses in the tree).
- `width="50%"` or `width="70%"` for dialogs and modals, no width for full-screen views. Keep the width
  consistent within one page.
- A screenshot needs a width small enough for its pixels, or it prints coarse: an image of 900 pixels
  across the full 16 cm column prints at 143 ppi. `poetry run dec-tool image-widths` lists every raster
  image in a page that is not generated that prints below 150 ppi, and `--fix` writes the `width="NN%"`
  that reaches it — the pixel width divided by the column and the target, rounded down. The same width
  then governs the site.
- `.off-glb` opts an image out of the glightbox lightbox — used for inline icons and decorative images.
- File names: lowercase, hyphen-separated, descriptive (style guide 5.5).
- Delete screenshots that are no longer referenced. Orphan check for one page directory:

```bash
for img in <dir>/*.png; do grep -q "$(basename "$img")" <dir>/*.md || echo "orphan: $img"; done
```

## Screen recordings

A screen recording is a WebM (VP9) video next to the page, never an animated GIF and never an upload to a video
platform.

```html
<video src="create-scheduler.webm" poster="create-scheduler.png" title="Creating a scheduler for the workflow Process Replay JSON in the Create new item of type Scheduler dialog" class="bordered" controls loop muted playsinline preload="metadata"></video>
```

- No `autoplay`: the reader starts the video. `controls loop muted playsinline preload="metadata"` on every video.
- `title` takes the role of the alt text and follows the same rule (style guide 5.6).
- `poster` is a still of the recording that shows its result, without keystroke overlays. The print edition prints
  the poster in place of the video, with the `title` as alt text; a video without a poster prints as a link.
- Same file names as images (5.5): `create-scheduler.webm` and `create-scheduler.png`.
- Convert a GIF or a screen capture with:

```bash
ffmpeg -i in.gif -vf "scale='trunc(min(1440,iw)/2)*2':-2:flags=lanczos,scale=out_color_matrix=bt709:out_range=tv,format=yuv420p" \
  -c:v libvpx-vp9 -crf 36 -b:v 0 -row-mt 1 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -an out.webm
ffmpeg -ss <seconds> -i in.gif -frames:v 1 -vf "scale='min(1440,iw)':-2:flags=lanczos" out.png
```

  Without the BT.709 options, white turns a visible light grey.
  Video and poster are capped at 1440 pixels across: the content column shows a video about 690 CSS pixels wide,
  so 1440 still covers a 2x display, and a 2x capture shrinks to about a third (22 MB GIF, 2.7 MB at 2870 pixels,
  0.87 MB at 1436). A narrower recording keeps its width — scaling it down would make it soft.
  Two-pass encoding does not make the file smaller; a higher `-crf` or a lower frame rate does, at a visible cost.

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

## Leaving content out of the print edition

The print edition of the PDF (`task pdf:print`, `tasks/spec.md` §10) can leave out content that only makes sense online.

- A subtree or a single page: an `omit` entry under `sections` in `tools/pdf/print.yml`, keyed by its `docs/` path.
  The page itself carries no marker, so this works for generated pages too.
- A part of a page: the class `print-exclude` on the block. The print edition prints a note in its place that points
  to the page online; the site and the screen PDF show the part unchanged.

| Block | Markup |
| --- | --- |
| code block | `sql { .print-exclude }` right after the backticks of the opening fence |
| admonition or collapsible block | `??? example print-exclude "INSERT query"` |
| paragraph | `{ .print-exclude }` on the line after the paragraph |
| several blocks | `<div class="print-exclude" markdown>` … `</div>`, with blank lines around the content |

A generated page cannot carry the class: the next generator run removes it.

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

## "Try it" SPARQL boxes

A training page can let the reader run a query in the browser.
A box is a collapsible admonition with the extra class `try-sparql`, holding data and one or more queries:

````markdown
??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .
    ex:a ex:p "test" .
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>
    SELECT ?s WHERE { ?s ex:p "test" . }
    ```
````

- Data too large to show goes into a file next to the page, linked with `{ .try-data }`:
  `Data: [product data](data/product-data.ttl){ .try-data }`.
- The queries of one box share one store and run in order, so an update affects the queries after it.
- Write every prefix a query uses into the query: the box is copied and edited by readers.
- Run `task update:try-results` after changing data or a query.
  It runs every box with pyoxigraph and writes the result under each query as a
  `<div class="try-result" markdown>` block, which is generated — never edit it.
  `task check` fails when a written result is out of date.
- The written results make the box readable without JavaScript, in search and in the PDF.
  `docs/assets/training-sparql.js` makes the blocks editable, adds **Run** and **Reset**, and runs
  the queries with the WebAssembly build of Oxigraph in `docs/assets/oxigraph/`.
- pyoxigraph is pinned to the release of that WebAssembly build. Bump both together.

## Markdown linting

```bash
task format:fix     # rumdl --fix over ./docs and ./*.md
task check          # link check + rumdl (fails on all rules except the cosmetic ones)
task build          # zensical build --strict
```

- Config: `.rumdl.toml` (`rumdl --config .rumdl.toml check`).
- The rules are split into two sets. `task check:rumdl` runs every enabled rule except `MD061` and `MD044`
  and fails the stage on any issue (JUnit report: `dist/md-lint-issues.xml`).
  `task check:rumdl:cosmetic` runs only `MD061` and `MD044`, lists the issues and writes
  `dist/md-lint-cosmetic-issues.xml`, but never fails. The cosmetic set is `RUMDL_COSMETIC_RULES` in the Taskfile.
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
Plugins: `awesome-pages`, `glightbox`, `tags`, `redirects`, `social`, `git-revision-date-localized`.
