# Backlog: print-on-demand book block

Work breakdown for [spec.md](spec.md). **Status 2026-09-15: P0-P12 done and verified, P13-P17 open.**

The previous content of this file (the temporary tag-listing renderer) is in the git history.

Every task names how it is verified. A task is not done until that verification passes.

---

## P0 - Decisions - done

Spec §4, D1-D11: BoD, A4, black and white on 80 g, no ISBN, authors by name (first GitHub IDs, revised 2026-09-15), separate screen and
print editions, section modes with A.3 and Release Notes as lists, page references and URL footnotes,
no logo or version on text pages, 10 pt body, optional Ghostscript normalization. D12-D14, decided
2026-09-15: excluding content from the print edition (spec §10), implemented by P18. D15-D18, decided
2026-09-15: the findings of the pull request review (spec §11), backlog P19-P24.

---

## P1 - Print edition - **done**

`task pdf:print` builds `dist/documentation-eccenca-com-<version>-print.pdf` next to the screen PDF:
the same merge and pandoc run, Typst compiled with `--input edition=print`. `style.typ` reads the input
once and branches where the editions differ. `task pdf` stays as it is.

**Verify:** both PDFs build; the screen PDF still has 1680 pages and an unchanged page 4.
**Est:** small. **Depends on:** nothing.

**Done 2026-09-15:** `dec-tool build-pdf --edition print` (`PDF_EDITION`), intermediates in
`dist/pdf/print/`, flag `print-edition` in `style.typ`. Against a baseline built from `c20d74b94`
before any change: the screen PDF has 1680 pages, the text of all pages is identical and page 4 differs
by 0 pixels. The print edition builds (1585 pages at that point).

---

## P2 - Mirrored page geometry - **done**

A4, `binding: left`, margins as `inside`/`outside` in the print edition; the peach bands' outset
mirrors with them.

**Verify:** render a spread (an even and the following odd page): the text blocks mirror, and the
text width is unchanged.
**Est:** small. **Depends on:** P1.

**Done 2026-09-15:** inside 3.0 cm, outside 2.0 cm. The header of the print edition is empty (P3), so
its top margin is 2.5 cm instead of 3.9 cm; the bands' outset is symmetric and needs no mirroring.
Measured with `pdftotext -bbox` on pages 20 and 21: even page margins 2.00 cm left and 3.00 cm right,
odd page 3.00 cm left and 2.00 cm right, text width 16.00 cm on both.

---

## P3 - Running titles and page numbers - **done**

- verso: page number at the outer left, part title; recto: page title, page number at the outer right
- no `| total`, no logo, no version stamp on text pages
- none on the title page, imprint, part covers and blank pages

**Verify:** a script reads `pdftotext -bbox` and asserts, for every page with a number, x below 20 %
of the page width on even pages and above 80 % on odd pages. Render two spreads.
**Est:** medium - the footer queries already exist; the parity and the exclusions are new.
**Depends on:** P2.

**Done 2026-09-15:** `print-footer()` and `bare-page()` in `style.typ`; the print header is empty. The
check over all 1604 pages of the print edition: 1575 pages carry a footer and each has its page number
at the outer edge (left on even, right on odd pages); the 29 pages without one are exactly the title
page, the imprint, the 9 part covers and the 18 blank pages. The checker becomes part of the preflight
report (P14).

---

## P4 - Recto starts and blank pages - **done**

- title page 1, imprint 2, front contents 3
- part cover, part contents and part text each start recto
- a blank page has no furniture: a state set by the page break, read by header and footer
- total padded to even

**Verify:** every part cover and the front contents on an odd page; every blank page has no text in
`pdftotext`; page count even.
**Est:** medium - suppressing furniture on inserted blank pages is the fiddly part (spec §1).
**Depends on:** P3.

**Done 2026-09-15:** `recto-break()` brackets `pagebreak(weak: true, to: "odd")` with two metadata
markers, and a page strictly between them counts as blank. Typst cannot pad to an even count itself -
a page break that depends on the page count never converges - so the build reads the unpadded count
with `typst eval` (`unpadded_pages`) and compiles with `--input pad=true` when it is odd (1603 → 1604).
Checked on all pages: title page 1, imprint 2, front contents 3; the 9 part covers and the 9 part
contents start on odd pages; 18 blank pages, all even, all without text, never three in a row.

---

## P5 - Title page - **done**

Publisher **eccenca GmbH** on the title block; site link and copyright move to the imprint.

**Verify:** render page 1.
**Est:** trivial. **Depends on:** P4.

**Done 2026-09-15:** rendered page 1: logo, the house title block and version, the publisher from
`tools/pdf/print.yml` at the foot of the page; no date, link or copyright. The screen title page is
unchanged.

---

## P6 - Author list - **done**

`dec-tool pdf-authors` (run by `task pdf:authors`) writes `tools/pdf/authors.yml`: GitHub ID and
commits, most commits first, ties by ID case-insensitive.

- source: the GitHub contributors API without anonymous entries
- excludes accounts of type `Bot` and agent IDs matching `claude` or `codex`
- committed, so the PDF build stays offline and reproducible and a changed list shows in review

**Verify:** unit tests for ordering, tie-break and exclusion; the generated file matches the spec §3
table (22 IDs).
**Est:** small. **Depends on:** nothing.

**Done 2026-09-15:** `tools/pdf_authors.py`, `tests/test_pdf_authors.py` (4 tests: order and tie-break,
exclusion of bots, agents and anonymous entries, pagination, file format), `task pdf:authors`. The
generated `tools/pdf/authors.yml` lists the 22 IDs of spec §3 in the same order and passes yamllint -
list items are indented, which PyYAML's default dumper does not do.

**Revised 2026-09-15 - names instead of IDs (D4):** `dec-tool pdf-authors` also writes the name each
GitHub profile shows (`GET /users/<id>`), and skips the IDs in `authors.exclude` of `tools/pdf/print.yml`
before any lookup. The build applies `authors.names` - for a profile without a name, or to add a title -
and the exclusions to the committed list (`load_imprint_names`), passes the names to Typst as the
`authors` input, and warns about each author it still prints as an ID. 16 of the 22 profiles show a
name; `rpietzsch`, `annamakor`, `MaximilianWenzel`, `adelahaye-ecc`, `dgrtner-ecc` and `pkgut` need an
entry. Each run also adds the authors `authors.names` does not list yet, without a name and with the
profile's name in a comment (`prefill_names`); it edits `print.yml` as text, so comments stay, and reads
it back to check that only those entries changed. A name left empty prints the profile's. First run: all
22 IDs added; a second run adds none. Requests use GITHUB_TOKEN or GH_TOKEN, else the token of a
logged-in GitHub CLI; without one GitHub allows 60 requests an hour, and a run takes one per author. A
failed request - rate limit with its reset time, rejected token, unreachable API - ends the command with
a message instead of a traceback, before any file is written. `tests/test_pdf_authors.py` has 28 tests:
rules, exclusion, profile names, the order of names, the prefill, token sources and API failures.

---

## P7 - Imprint - **done**

Page 2 as spec R3, with the publisher address `eccenca GmbH, Hainstraße 8, 04109 Leipzig, Germany`, no
ISBN. Typst reads `tools/pdf/authors.yml` with `yaml()`; edition, commit and date come from the
existing `--input` values.

**Verify:** render page 2; the author order matches `authors.yml`.
**Est:** small. **Depends on:** P5, P6.

**Done 2026-09-15:** `imprint()` in `style.typ`, set at the foot of page 2: edition stamp with commit,
publisher and address from `tools/pdf/print.yml`, the 22 author IDs, licence and copyright, the online
edition - with a sentence that the print edition shortens sections whenever `print.yml` lists one as
`list` or `omit` - and the typesetting. Checked on the rendered page and in its text: the author IDs match
`authors.yml` in order. The licence URL is set as a string, because Typst links URLs written in markup.

**Revised 2026-09-15:** the imprint prints the authors' names, not their IDs. `imprint()` no longer
reads `authors.yml`; the build passes the names as the `authors` input (P6).

---

## P8 - Section modes - **done**

`tools/pdf/print.yml` maps `nav.yml` section paths to `full`, `list` or `omit`; `tools/build_pdf.py`
reads it for the print edition only.

- `omit`: the section's pages are not merged; the part contents name the online edition instead
- `list` for the operator reference (`build/reference/`): merge the section page and the five overview
  pages, drop their children; links from the overview tables to dropped pages print as plain text
- `list` for Release Notes (`release-notes/`): replace the release pages with one generated table,
  Release | Summary, the summary being the release page's first paragraph or, without one, its component
  headings
- a section in `list` or `omit` mode starts with a sentence naming its online URL
- an unknown path or mode in `print.yml` fails the build

**Verify:** unit tests per mode on small fixtures; with the default configuration A.3 takes about
17 pages and Release Notes about 3; switching either to `full` restores today's pages; no internal
link targets a dropped page.
**Est:** medium - the release summary fallback and the links into dropped pages are the fiddly parts.
**Depends on:** P1.

**Done 2026-09-15:** `load_section_rules`, `apply_section_rules` (`list_section`, `omit_section`) and
`render_generated` in `tools/build_pdf.py`; `tests/test_build_pdf_print.py` (10 tests). A `list` section
keeps its own page and its subsections' overview pages; a page no overview lists goes into a table under
its heading, one per run of pages. Release Notes have no overview pages, so they become 8 tables - one
per year - with the 22 releases. Measured on the print edition: A.3 takes 17 pages (pp. 23-39, 389 pages
dropped), the Release Notes part 6 pages including cover, contents and blank pages; the book goes from
1604 to 1012 pages. Setting both sections back to `full` gives 1604 pages again. The two notes name
`…/26.2/build/reference/` and, since `release-notes/` has no page, the first release page. Links from
the overview tables to dropped pages print as text; 105 links from other pages to dropped operator
pages lead to the published site - a dropped page has no label, so no internal link can target one.

---

## P9 - Links on paper - **done**

In the print edition: internal links print their text plus `(p. N)`; external links print their text
with a footnote holding the URL; no colour, underline, arrow or link annotation.

**Verify:** sample pages; the number of footnotes equals the number of external links in the printed
sections; no page reference is `p. 0`; `strings` finds no `/Annots` in the book block.
**Est:** medium - thousands of page lookups; watch for Typst's "layout did not converge" warning.
**Depends on:** P1, P8.

**Done 2026-09-15:** the print branch of `show link` in `style.typ`; contents entries are laid out
without their link. Of 524 external links, 73 print their address as their own text and get no
footnote; 451 get one, 2 of them repeating the address their text already shows. 2154 page references,
none `p. 0`. A reference printed only for a target on another page never let the layout converge - it
moves lines, which moves the target back - so it is printed always, and the build now has no
convergence warning. Deviation from the check above: Typst's own footnotes link marker and entry, so
the book block keeps 902 internal link annotations; none of them leads to an address (`/S /URI`: 0).
The optional Ghostscript pass (P13) removes them.

---

## P10 - Typography for print - **done**

- paragraph spacing 1.2 em and block spacing 1.0 em (measured −6.5 % pages)
- hyphenation on, widow and orphan costs
- a 6 pt floor for shrinking terminal tables
- measure Regular instead of Light for the body; decide with a greyscale print sample
- body stays 10 pt; 9 or 8 pt only as a fallback if the preflight page limit is exceeded (D10)

**Verify:** page count after each change; render pages with justified text.
**Est:** small. **Depends on:** P1.

**Done 2026-09-15:** paragraph spacing 1.2 em and block spacing 1.0 em take the book from 1012 to 962
pages; hyphenation on for body text, off for titles; code in a shrinking terminal table never below
6 pt. Typst's defaults already cost widows and orphans at 100 % (`text.costs`, checked), so they needed
no setting. A Regular body costs 2 pages (963 instead of 961 before padding); `body-weight` in
`tools/pdf/print.yml` switches it, and it stays `light` until a printed sample decides. Sample pages 26
and 268 checked on the render: justified text without gaps, code and terminal table legible.

---

## P11 - Black-and-white palette - **done**

- grey areas at least 20 % black (BoD): `ec-wash` code and note grounds, peach bands - raise to 20 % or
  replace fills with rules
- print-edition values for orange, link blue and the admonition accents that stay distinguishable in
  grey
- check the red frames of the four part diagrams

**Verify:** render sample pages with the greyscale preview of P13 and compare with the screen
edition; the preflight measures the lightest fill.
**Est:** small. **Depends on:** P1.

**Done 2026-09-15:** in print, text and alarm accents are black, the orange a dark grey, the peach bands
20 % black; code, code spans and admonitions have no ground - a thin frame marks a code block, the bar on
the left an admonition. The greyscale preview of P13 does not exist yet, so Ghostscript's `pnggray`
rendered all 962 pages instead: on the 610 pages without images no area is lighter than 20 % black, and
the bands measure 204 (20 % black) on 36 pages. The part diagrams' red frames are part of their images and
stay visible as a dark frame on the covers.

---

## P12 - Print images - **done**

In `tools/build_pdf.py`, for the print edition: every image Typst embeds is a normalized copy in
`dist/pdf/images/`.

- alpha composited onto white, so the book block carries no transparency
- resampled (Lanczos) to 300 ppi at its printed width: text width (16 cm) when the image is wider than
  the column, its natural size otherwise
- no longer scaled up beyond its natural size (spec §6)
- originals under `site/` untouched; cached by content hash, so a rebuild does not resample again

Needs an image library. Pillow is importable today only as a transitive dependency (11.3.0) and is not
declared in `pyproject.toml` - declare it before relying on it. ImageMagick is the alternative: installed
locally, not yet in CI.

**Verify:** unit tests on fixture PNGs (alpha, small, large); in the book block `pdfimages -list` shows
no soft mask and no image below 300 ppi; render pages with former low-resolution screenshots.
**Est:** medium - the printed-width rule must match how Typst sizes images. **Depends on:** P1.

**Done 2026-09-15:** `print_image` and `printed_width_pt` in `tools/build_pdf.py`, Pillow declared in
`pyproject.toml` (it was installed only as a leftover of CairoSVG); `tests/test_build_pdf_images.py`
(7 tests). The printed width follows how Typst sizes an image, measured in a probe: a percentage of the
16 cm column, otherwise pixels × 72 / declared dpi (72 without one), never wider than the column and
never scaled up - so "no longer scaled up" needed no change. The copy declares 300 dpi and keeps that
printed width. In the book block: 586 images, 0 soft masks, the lowest at 300 ppi, none below; 571
copies in `dist/pdf/print/images/`. The PDF grows from 72 to 165 MB with the lossless upsampled copies.

---

## P13 - Normalization pass (optional)

`dec-tool pdf-normalize <pdf>` (run by `task pdf:print` with `--normalize` / `PDF_NORMALIZE=1`), spec §7:

- Ghostscript pdfwrite with `-dPDFX=4`, CMYK conversion, bicubic downsampling of colour and grey
  images above 300 dpi, Flate re-encoding, `-dPreserveAnnots=false`
- prefix file `tools/pdf/PDFX_def.ps`, derived from Ghostscript's `lib/PDFX_def.ps`, with title and
  a FOGRA39 output intent; the profile passed with `--permit-file-read`
- ISO Coated v2 (FOGRA39) profile vendored under `tools/pdf/icc/` with its ECI licence, listed in the
  README asset table - or downloaded in CI if the licence does not allow vendoring
- a `--gray` preview variant for P11
- fails when the output lacks `GTS_PDFXVersion (PDF/X-4)` - Ghostscript silently falls back to plain
  PDF when a page still carries an annotation
- never `-sOutputICCProfile` together with `-dPDFX` (crashes, truncated file)

**Verify:** on the full book block: PDF/X-4 marker in info and XMP, one output intent naming FOGRA39,
`pdfimages -list` shows only `cmyk` images and none above 300 ppi, `pdffonts` all embedded, page count
unchanged; render sample pages before and after and compare.
**Est:** small - the recipe is verified on 38 pages. **Depends on:** P9 (no annotations), P12.

---

## P14 - Preflight report

`dec-tool pdf-preflight <pdf>`: A4 page size, page count at most 1,200 and even, fonts embedded, images
below 300 ppi, soft masks, lightest fill below 20 % black, page-number position (P3's check), blank
pages blank. Non-zero exit on a violation; run by `task pdf:print`, on the normalized file when P13 ran.

**Verify:** unit tests on small fixture PDFs; deliberately break one rule, the report must fail.
**Est:** medium. **Depends on:** P3, P4, P8.

---

## P15 - Low-resolution originals

49 images were below 150 ppi at printed size; resampling (P12) hides that from the preflight but adds no
detail. After P18, 43 images in the printed pages that are not generated print below 150 ppi, 37 of them
without a `width` - P24 sizes those first (spec §11). Work through what stays below 150 ppi: replace it
with a fresh screenshot, or accept it in spec §8.

**Verify:** every entry replaced or accepted.
**Est:** medium, mostly content. **Depends on:** P12, P24.

---

## P16 - CI

`.github/workflows/pdf.yml` also builds the normalized book block and uploads it with the preflight
report, as a separate artifact. Installs Ghostscript on the runner.

**Verify:** a push to `main` produces both artifacts.
**Est:** small. **Depends on:** P1, P13, P14.

---

## P17 - Cover (separate deliverable)

Front, spine and back; the spine width follows from the final page count and 80 g paper. Tracked here
so it is not forgotten; it has its own spec.

**Depends on:** P8, P14.

---

## P18 - Content exclusion - **done**

Spec §10, D12-D14: leave subtrees, pages and parts of a page out of the print edition.

- `sections` keys in `tools/pdf/print.yml` may name a page (`.md`), which accepts `omit` only; a nested
  key, or one that matches no page in `nav.yml`, fails the build
- `omit` drops a page or a subtree without a title or a note. For directories this revises P8, which
  left the section's title and a note naming the online edition
- dropping a section's index page keeps its other pages under a heading with the navigation title
- in the print edition, elements with the class `print-exclude` are removed from the page's article
  before ids, links and headings are processed. A note takes their place: "This print edition leaves
  out a part of this page. The online edition has the full details:" and the page's online address,
  with the anchor of the heading before the part; consecutive parts share one note. The build logs the
  parts removed per page
- the site and the screen PDF ignore the class
- documentation: the `sections` comment in `print.yml`, and a line for authors in
  `.claude/docs-guidelines/repo-conventions.md` on the class, which generated pages cannot carry
- configuration: `develop/cmem-client-api/: omit`, `build/tutorial-how-to-link-ids-to-osint/: omit` (all
  7 pages), and `{ .sql .print-exclude }` on the SQL code block of the Snowflake tutorial - lines 92-1094
  of `docs/build/snowflake-tutorial/index.md` on 2026-09-15, inside `??? example "INSERT query"`, which
  keeps its title

**Verify:** unit tests for page keys, the mode check, nesting, a dropped index page, the removal with
one note per run of parts and its address, and no removal in the screen edition. `task pdf:print` with
the three examples: G.5 and A.16 leave no heading or note, the `INSERT query` block of
the Snowflake tutorial holds the note instead of the listing, and the page count drops by about 300
(spec §10). `task pdf`: page count and text unchanged apart
from the stamp. `task check` passes.
**Est:** small to medium. **Depends on:** P8, P9.

**Done 2026-09-15:**

- `SectionRule` knows page rules (`page`, `matches`). `load_section_rules` accepts page keys with `omit`
  only and rejects nested keys.
- `omit_section` drops a page or a subtree without a trace. An index page omitted on its own leaves its
  navigation title as a heading.
- `exclude_parts` replaces each run of `.print-exclude` elements with the note, whose address carries the
  anchor of the heading before the part. `merge_pages` returns the parts left out per page, which the
  build logs. List tables skip marked elements as well.
- `print.yml` omits `develop/cmem-client-api/` (75 pages) and `build/tutorial-how-to-link-ids-to-osint/`
  (7 pages). The SQL block of the Snowflake tutorial carries `sql { .print-exclude }`. Authors find the
  markup in `.claude/docs-guidelines/repo-conventions.md`.
- Measured:
    - The print edition drops from 966 to 666 pages, the Snowflake tutorial from 46 to 22.
    - No bookmark is left for G.5 or A.16.
    - The note stands inside the `INSERT query` block (p. 120), with the anchor
      `#1-create-a-database-in-snowflake`.
    - No page runs into the footer and no line runs past the text column.
    - The screen PDF keeps 1683 pages, its text unchanged and the listing in it.
    - 134 unit tests pass.
    - The `task check` steps pass; yamllint passes on the tracked files, while the untracked `scratch/`
      folder still fails it.

---

## P19 - Part label in the footer

Spec §11: the running footer of a left-hand page prints the part as the part band does, `Part A: Build`.
The contents, the bookmarks and the right-hand footer keep theirs. `print-footer` in `tools/pdf/style.typ`.

**Verify:** render a left-hand and a right-hand page of two parts; the screen PDF is unchanged.
**Est:** small. **Depends on:** P3.

---

## P20 - Web addresses as endnotes

Spec §11, D15. In the print edition, a link out of the book prints its text and a superscript number
instead of a footnote. The numbers run within a part and start again at 1 in the next; an address cited
twice in a part keeps its first number. A list "Web addresses" on a new page, under an unnumbered heading,
closes each part that cites any: number, address and the pages citing it, laid out without link
annotations. Links within the book keep their page reference.

**Verify:** no footnote left in the book block; each part's list holds every number of that part with its
address and correct pages; numbering restarts per part; no link annotations from notes; Typst reports no
layout that failed to converge; compile time and page count before and after.
**Est:** medium. **Depends on:** P9.

---

## P21 - Author order from the printed content

Spec §11, D16. `dec-tool pdf-authors` counts only the commits to the files the print edition
prints: the pages left after the section rules and the images in their directories, from
`git log --no-merges` following renames, each commit once, generated pages left out. The GitHub
commits API maps each commit to its account. Bots, agents, anonymous commits and `authors.exclude`
stay excluded; the imprint says "most commits to the printed pages first".

**Verify:** unit tests with a fake history for file selection, rename following, counting and account
mapping; a real run shows the new order next to today's; the imprint follows it.
**Est:** medium. **Depends on:** P6, P18.

---

## P22 - Cards of equal height

Spec §11: `cards()` in `tools/pdf/style.typ` lays out its grid row by row and gives both cards of a row
the height of the taller one; a card alone in the last row keeps its own height. The rounded frame and
`breakable: false` stay; the screen PDF changes with it.

**Verify:** render the card grids of the part pages in both editions; facing cards end on one line; no
card breaks across pages.
**Est:** small. **Depends on:** nothing.

---

## P23 - Operator reference in a compact format

Spec §11, D17. A section mode `reference` prints `build/reference/` as one compact, harmonized
entry per operator; the entries replace the overview tables.

- **Structure:** each type chapter keeps its introduction. Operators follow alphabetically, numbered
  A.3.x.y and listed in the part contents; the transformer category moves into the entry.
- **Entry:** the title and a field line with type, category, plugin ID, `Python plugin` and a distance
  range. Then the rendered description without `## Examples` and without the Python plugin note, its
  headings as run-in labels. Then one parameter table with the columns Parameter and its ID, Type, Default
  and Description, an `Advanced` row and `parent.child` sub-parameters, and a `Related:` line with page
  references.
- **Sparse data prints as nothing:** no table without parameters, `–` for a missing default, and
  `see below` with a code block for a multi-line default. The data types map to the vocabulary of spec
  §11.
- **Data:** structure and parameters come from `data/plugins.json`, the description from the site page.
  The build fails when pages and JSON disagree.
- **Configuration:** `print.yml` switches `build/reference/` from `list` to `reference`. The A.3
  introduction names the online examples and Python plugins once.

**Verify:** unit tests build entries from a JSON fixture - an operator without parameters, one with
advanced and sub-parameters, a multi-line default, every data type - and cover the page/JSON check. The
print build shows 389 entries, no Examples heading and no `None`. The page count is measured against the
estimate of spec §11 (about 860) and BoD's limit (P14). Render a transformer, a dataset and a custom task
with more than 20 parameters.
**Est:** medium to large. **Depends on:** P8.

---

## P24 - Image widths in the sources

Spec §11, D18. `dec-tool image-widths --check|--fix` writes `{ width="NN%" }` for raster images without a
width in pages that are not generated: the pixel width divided by the capture scale and by the full page
width - the 16 cm text column, 605 CSS pixels - rounded to 5 %, at most 100 %. The capture scale is 2 for
144 dpi (macOS Retina), otherwise the declared density / 96, and 1 without one. Optionally `task check`
runs `--check`.

**Verify:** unit tests for capture scale, percentage, rounding and the skip rules; after `--fix` no raster
image in a page that is not generated lacks a width; spot checks of the changed pages on the site and in
the print edition; the count below 150 ppi in the print edition before and after - no image prints less
sharply than before.
**Est:** medium, touches many pages. **Depends on:** nothing. P15 follows it.

---

## Sequencing

```text
P1 ──> P2 ──> P3 ──> P4 ──> P5 ──> P7
 │                    │     P6 ──┘
 ├──> P8 ──> P9 ──────┼─────────────┐
 ├──> P10             │             │
 ├──> P11             │             │
 └──> P12 ──> P15     │             │
       └──────────────┼──> P13 <────┘
                      └──> P14 ──> P16
P17 after P8 and P14
P18 after P8 and P9
P19 after P3, P20 after P9, P21 after P6 and P18, P22 any time, P23 after P8
P24 before P15
```

P1, P6, P8, P10, P11 and P12 can start now.

## Risks

- **The page budget is an estimate.** It adds measured savings that were taken separately; P8 and P10
  must re-measure, and P14 enforces the limit.
- **Ghostscript falls back to plain PDF silently.** One annotation left anywhere and the output is not
  PDF/X; P13 checks the marker instead of trusting the exit code.
- **CMYK conversion and downsampling change screenshots.** Compare renders before and after P13 on pages
  with dense UI text; Flate keeps the re-encoding lossless, the bicubic resampling does not.
- **Upsampled images look sharper in the preflight than on paper.** P15 exists because P12 cannot add
  detail that is not there.
- **Black and white loses colour cues** in screenshots and in the part diagrams' red frames, and today's
  light fills fall below BoD's 20 % rule; only a greyscale sample shows how much.
- **Page references cost compile passes.** Thousands of `(p. N)` lookups can move page breaks that move
  page numbers; Typst stops after five layout attempts and warns.
- **80 g paper is for publishers only at BoD.** Without a publisher account the book prints on 90 g,
  where the limit is 1,050 pages.
- **The screen PDF must not drift.** Every print change goes behind the `edition=print` switch (P1), and
  the screen PDF's page count is part of every verification.
