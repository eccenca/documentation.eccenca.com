# Backlog: print-on-demand book block

Work breakdown for [spec.md](spec.md). **Status 2026-09-16: P0-P15 and P18-P26 done and verified;
P16 (CI) and P17 (the cover) open.**

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
the left an admonition. The greyscale preview of P13 did not exist then (it does now: `--gray`), so Ghostscript's `pnggray`
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

## P13 - Normalization pass (optional) - **done**

Done 2026-09-15: `dec-tool pdf-normalize` (`tools/pdf_normalize.py`), run by `task pdf:print -- --normalize`
or PDF_NORMALIZE=1, writes `…-print-x4.pdf`. Refinements:

- **Profile not vendored:** its copyright reads "All Rights Reserved" (spec §7). It is fetched from the ECI
  into `dist/icc/` with a SHA-256 check; `--icc-profile` / PDF_ICC_PROFILE name a copy.
- **No prefix file in the repository:** the pdfmark prefix is generated with the title and the profile's path.
- **Transparency first:** Ghostscript 10.08 segfaults on Typst's colour emoji and leaves out transparent
  SVG content (spec §7). The print edition therefore renders the 5 transparent SVGs and the 10 emoji sequences
  to PNG with Typst; the style swaps emoji by show rule, in code too. The screen PDF is verified unchanged.
- **Failures are loud:** the run fails on a non-zero exit, on `error executing PDF token` and on a missing
  PDF/X marker, and deletes the output.
- **Checked twice:** the build runs the preflight (P14) on the book block before Ghostscript, and on the
  PDF/X-4 copy with `--pdfx` after.
- **Greyscale preview:** `task pdf:print -- --gray` (PDF_GRAY=1; `dec-tool pdf-normalize --gray` for an
  existing PDF) writes `…-print-gray-x4.pdf`. It is the same pass in DeviceGray, and it serves as a screen
  check of the black-and-white print for P11. It combines with `--normalize`. Verified on the 868-page
  book block: 181 s, 59 MB, all 556 images grey, A4 unchanged. Since 2026-09-16 it is PDF/X-4 as well,
  by the generic `default_gray.icc` of Ghostscript (condition `sGray`, one component, no registry).
  Verified on the 872-page book: 176 s, 57 MB, the marker and a one-component intent, all 556 images grey,
  and `dec-tool pdf-preflight --pdfx --intent sGray` passes; four unit tests.

Verified on the full book block: 868 pages, Ghostscript 218 s, 175 MB; the preflight passes with
`--pdfx`: PDF/X-4 marker, FOGRA39 intent, 556 images all CMYK and none above 300 ppi, fonts embedded, no
Type 3 font, no transparency, no annotations. Rendered pages 26 (card icons), 472 (Excalidraw diagram)
and 662 (emoji) match the RGB file. 9 unit tests, 5 more for the rendered emoji and SVGs.

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

## P14 - Preflight report - **done**

Done 2026-09-15: `dec-tool pdf-preflight <pdf> [--pdfx] [--max-pages]` (`tools/pdf_preflight.py`). Page
sizes, annotations and fill colours come from pypdf, fonts, images and word boxes from poppler's
`pdffonts`, `pdfimages -list` and `pdftotext -bbox`. Light areas are a **warning** that does not fail the
run - artwork and emoji carry light fills too; every other check is an error. With `--pdfx` it also
requires the PDF/X-4 marker, a FOGRA39 output intent and CMYK or grey images at most 300 ppi.
`build-pdf --edition print` runs it on its final file, the normalized one when P13 ran, and fails on an
error after writing the PDF. Verified: 9 unit tests; the print book block (868 pages) passes every check
in 7 s; the screen PDF fails as it should - 778 pages with annotations, 840 page numbers on the inner
edge, soft masks, light fills. Refinement: a fill of exactly 20 % black (`0.8 g`, 0.19999… in floating
point) counts as passing - the first run reported it on 102 pages.

`dec-tool pdf-preflight <pdf>`: A4 page size, page count at most 1,200 and even, fonts embedded, images
below 300 ppi, soft masks, lightest fill below 20 % black, page-number position (P3's check), blank
pages blank. Non-zero exit on a violation; run by `task pdf:print`, on the normalized file when P13 ran.

**Verify:** unit tests on small fixture PDFs; deliberately break one rule, the report must fail.
**Est:** medium. **Depends on:** P3, P4, P8.

---

## P15 - Low-resolution originals - **done**

49 images were below 150 ppi at printed size; resampling (P12) hides that from the preflight but adds no
detail. After P18, 43 images in the printed pages that are not generated print below 150 ppi, 37 of them
without a `width` - P24 sizes those first (spec §11). Work through what stays below 150 ppi: replace it
with a fresh screenshot, or accept it in spec §8.

**Verify:** every entry replaced or accepted.
**Est:** medium, mostly content. **Depends on:** P12, P24.

Done 2026-09-16 by the revised P24: no screenshot had to be replaced. Narrowing the 42 entries to the
width their pixels support empties the report, so `accepted-low-resolution` in `tools/pdf/print.yml`
stays an empty list, and the report keeps watch over new screenshots.

Tooling done 2026-09-15: the print build collects every original below 150 ppi at its printed size
(`resolve_images(..., low_resolution)`), leaves out those listed under `accepted-low-resolution` in
`tools/pdf/print.yml`, writes the rest lowest first to `dist/pdf/print/low-resolution.tsv` - density, the
width the page declares (the `width="NN%"` of the Markdown source, empty where there is none) and the
image - and prints their count. Accepting moved from spec §8 to `print.yml`, next to the other print
settings. The 42 entries it listed - 85 to 149 ppi, most in `consume/populate-data-to-neo4j` (8),
`explore-and-author/bke-module` (5) and `distribution/marketplace` (4) - are resolved by the revised P24:
the report is empty.

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
- configuration: `develop/cmem-client-api/: omit` (P26 widened it to all of `develop/`),
  `build/tutorial-how-to-link-ids-to-osint/: omit` (all
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
- `print.yml` omits `develop/cmem-client-api/` (75 pages, widened to all of `develop/` by P26) and
  `build/tutorial-how-to-link-ids-to-osint/` (7 pages). The SQL block of the Snowflake tutorial carries `sql { .print-exclude }`. Authors find the
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

## P19 - Part label in the footer - **done**

Spec §11: the running footer of a left-hand page prints the part as the part band does, `Part A: Build`.
The contents, the bookmarks and the right-hand footer keep theirs. `print-footer` in `tools/pdf/style.typ`.

**Verify:** render a left-hand and a right-hand page of two parts; the screen PDF is unchanged.
**Est:** small. **Depends on:** P3.

**Done 2026-09-15:** `print-footer` prints a part on a left-hand page as `Part A: Build`; right-hand footers,
contents and bookmarks keep `A Build`. 313 left-hand pages carried the label in the build before P23;
the screen PDF is unchanged.

---

## P20 - Web addresses as endnotes - **done**

Spec §11, D15. In the print edition, a link out of the book prints its text and a superscript number
instead of a footnote. The numbers run within a part and start again at 1 in the next; an address cited
twice in a part keeps its first number. A list "Web addresses" on a new page, under an unnumbered heading,
closes each part that cites any: number, address and the pages citing it, laid out without link
annotations. Links within the book keep their page reference.

**Verify:** no footnote left in the book block; each part's list holds every number of that part with its
address and correct pages; numbering restarts per part; no link annotations from notes; Typst reports no
layout that failed to converge; compile time and page count before and after.
**Est:** medium. **Depends on:** P9.

**Done 2026-09-15:**

- `web-address()` in `style.typ` places the address as metadata and prints a superscript number, counted
  within the part with `context` and `query`. `part-addresses()` sets the list on a new page under an
  unnumbered heading that is bookmarked but not in the contents: number, address and the pages citing it.
- In the print edition, `merge_pages` puts a `part-end` marker at the end of every part, and
  `filter.lua` turns it into `#part-addresses()`; a unit test covers the markers.
- Measured with P23 in place: 8 lists with 390 entries, 159 of them in part A. Typst compiles in 4 s
  without a convergence warning; the screen PDF is unchanged.

---

## P21 - Author order from the printed content - **done**

Spec §11, D16. `dec-tool pdf-authors` counts only the commits to the files the print edition
prints: the pages left after the section rules and the images in their directories, from
`git log --no-merges` following renames, each commit once, generated pages left out. The GitHub
commits API maps each commit to its account. Bots, agents, anonymous commits and `authors.exclude`
stay excluded; the imprint says "most commits to the printed pages first".

**Verify:** unit tests with a fake history for file selection, rename following, counting and account
mapping; a real run shows the new order next to today's; the imprint follows it.
**Est:** medium. **Depends on:** P6, P18.

**Done 2026-09-15:**

- `tools/pdf_authors.py` counts the commits to the printed files. `printed_pages` applies the section
  rules, and `printed_files` returns the pages that are not generated plus the images they reference.
  `file_commits` runs `git log --no-merges --follow` per file, and `commit_accounts` with
  `count_commits` maps each commit once to its account, falling back to the author e-mail.
  `fetch_commits` replaces the contributors API.
- The imprint reads "most commits to the printed pages first".
- `tests/test_pdf_authors.py` has 31 tests; new are printed files, counting and rename following in an
  isolated git repository.
- Measured: 661 commits to 638 printed files, 18 authors instead of 19 - `haschek` has no commit to
  printed content. The order starts with `rpietzsch` (249), `seebi` (156), `sobo` (46),
  `muddymudskipper` (45) and `irangareddy` (37).

---

## P22 - Cards of equal height - **done**

Spec §11: `cards()` in `tools/pdf/style.typ` lays out its grid row by row and gives both cards of a row
the height of the taller one; a card alone in the last row keeps its own height. The rounded frame and
`breakable: false` stay; the screen PDF changes with it.

**Verify:** render the card grids of the part pages in both editions; facing cards end on one line; no
card breaks across pages.
**Est:** small. **Depends on:** nothing.

**Done 2026-09-15:** `cards()` measures the cards of each row at the column width and frames both with
`card-frame()` at the height of the taller one; `card()` now only passes the content through. Checked on
the card grids of the Build page (p. 11) and the reference (p. 30); the screen PDF keeps its page count
and text.

---

## P23 - Operator reference in a compact format - **done**

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

**Done 2026-09-15:**

- Section mode `reference` in `tools/build_pdf.py`. `reference_section` places a note after the section
  page and the operators of each type after its overview page, alphabetically, drops the category
  headings, and fails when pages and `data/plugins.json` disagree. `merge_pages` removes the overview
  tables.
- `operator_entries` renders each entry: `operator_fields`; `operator_description` without the title,
  the Python plugin note and the template sections, with headings as run-in labels; `parameter_table`
  with the type vocabulary of `data_type`, an `Advanced` row, `parent.child` sub-parameters, `see below`
  defaults and Markdown descriptions; and `operator_related`.
- `operator-fields()` in `style.typ` and its mapping in `filter.lua`. `print.yml` switches
  `build/reference/` to `reference`. `tests/test_build_pdf_reference.py` has 5 tests.
- Measured: 389 entries with bookmarks; A.3 takes 213 pages (pp. 29-241) and the book 870 (spec §11
  estimated 860). No `Advanced Parameter` heading and no generated example is left; 9 defaults print as
  `see below`, 80 entries have a `Related:` line, and 1 web address still points to an operator page.
  The screen PDF is unchanged.
- Open: example subsections the plugins write into their own documentation - `5. Example` in Pivot,
  `6. Examples` in RDF file, `Example usage` in Knowledge Graph - still print as run-in labels with their
  text; only the generated `## Examples` sections are dropped.

---

## P24 - Image widths in the sources - **done**

Revised on 2026-09-16, once the report of P15 made the effect visible: the width follows from the density
an image *prints* at, not from the density it was *captured* at. `dec-tool image-widths`
(`tools/image_widths.py`) narrows every raster image that prints below 150 ppi in the 16 cm column, in
pages that are not generated, and leaves the rest as it is.

- **Width:** `pixels / (6.3 inches * 150)`, rounded down to a whole percent - not to a multiple of 5. The
  width a page already declares cancels out of `declared * density / target`, so the pixels alone decide;
  one further step down covers the case where the rounding of the density leaves it a pixel short.
- **Measured at** the width the page declares, quoted or not - two of 187 are written `width=11%` - and an
  image without one fills the column, so it counts as 100 %.
- **No floor:** the smallest results are `marketplace-filter-installed.png` at 14 % and
  `marketplace-filter-package-type.png` at 21 %. Both show a single snippet of a dialog, so the user chose
  the calculated value over a floor.
- **Scope:** raster images only; SVGs, remote images and fenced code stay untouched, and generated pages
  belong to their generators - none of them held an image below the target.

**Verified:** `--fix` wrote 47 widths into 21 pages; the report of P15 is empty afterwards and the book
shrinks from 872 to 864 pages. The gate was a throwaway PDF of just those images at their new widths.
Five of the 47 sit in the IDS/OSINT tutorial, which print omits, so they change the site only. rumdl
clean; the unit tests cover the density, the target width, and the rewriting of quoted, unquoted and
missing width attributes.

**Superseded:** the first implementation (2026-09-15, D18 as written) took the natural width from the
capture scale, rounded it to 5 % and skipped anything at 100 %. Its 24 widths stay where the new rule does
not narrow them further. `task check` runs the check as `check:images`.

---

## P25 - A heading with a single line at the foot of a page - **done**

Review finding of 2026-09-16: A.3 Task and Operator Reference sat at the foot of page 29 with its
intended-audience line under it, and the section started on the next page. A heading is sticky, so it is
never last on a page - but a one-line lead satisfies that, and the break falls after the line.

Done the same day: `keep_lead_with_heading` in `tools/build_pdf.py` (print edition only) wraps a paragraph
that directly follows a heading of level 1 to 4 and is at most 200 characters long in
`div.keep-with-next`; `filter.lua` maps it to `keep-with-next` in `style.typ`, a sticky block, so the lead
carries heading and line to the block that follows. Levels 5 and 6 are left out: they are the operator
entries, which have their own sticky field blocks.

**Verified:** 304 lead lines wrapped; A.3 now starts a page with its content; across the book, headings
with at most one line under them at a page foot fall from 23 to 6, and the book grows from 868 to 872
pages. Measured against levels 1 to 3 alone, which leaves 17 of them at 868 pages: the four pages buy
eleven fewer stranded headings, and one new one appears (B.2.2.6). `LEAD_HEADINGS` is the one place to
change if the shorter book matters more. The screen edition does not run the step. One unit test.

---

## P26 - The first edition is a user guide - **done**

Decided 2026-09-16: the first print edition serves users, so what an administrator or a developer needs
stays in the online edition. `tools/pdf/print.yml` omits part E (`deploy-and-configure/`, 34 pages) and
part G (`develop/`, 89 pages) whole, and the narrower `develop/cmem-client-api/` key goes, since section
keys do not nest.

**Verified:** the book drops from 864 to 668 pages and the preflight passes unchanged. No cross-reference
dies: a link from a printed page into an omitted part becomes a web address in its part's endnote list -
the JDBC driver setup, for one, prints as
`https://documentation.eccenca.com/latest/deploy-and-configure/configuration/dataintegration/jdbc/` -
and internal links without a target fall from 17 to 4, because most of those lived in the dropped trees.

**Open:** the imprint's author list counts commits to the printed pages (D16), and 123 pages left the
book, so `task pdf:authors` should run before the edition goes to print.

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
