# Spec: print-on-demand book block

**Status:** accepted 2026-09-14 - all decisions made (§4). Backlog P0-P12 implemented 2026-09-15
(`task pdf:print`, 962 pages); P13-P17 open. The backlog's "Done" notes record where the implementation
refines this spec. §10, excluding content from the print edition, was decided on 2026-09-15 (D12-D14)
and implemented the same day (backlog P18): the print edition has 666 pages.
**Branch:** `feature/print-on-demand`, based on `main` at `c20d74b94` (PDF export merged).
**Goal:** a *book block* - the interior file of a printed, perfect-bound book - built next to the
screen PDF, which BoD accepts without rework.
**Not in scope:** the cover file (front, spine, back); see §9.

The previous content of this file (the temporary tag-listing renderer, removed 2026-09-03) is in the
git history.

---

## 1. Starting point

Measured on the level-4 build of `main` (`dist/documentation-eccenca-com-26-2.pdf`).

| Aspect | Today |
| :-- | :-- |
| Size | 1680 pages, A4, 118 MB |
| Type | body 10 pt Roboto Light (`size-base`, one step below the house style's measured 11 pt); tables 8.6 pt, admonitions and cards 9.1 pt, code 7.7 pt; 3 terminal tables shrink to fit, the widest (114 columns) to about 6.3 pt |
| Line length | about 104 characters per full body line (75th percentile, pages 40-80) |
| Parts | A Build pp. 3-734 (732) · B Explore 735-861 (127) · C Consume 862-900 (39) · D Distribution 901-910 (10) · E Deploy and Configure 911-1075 (165) · F Automate 1076-1192 (117) · G Develop 1193-1490 (298) · H Release Notes 1491-1677 (187) · I Tutorials 1678-1680 (3) |
| Largest blocks | A.3 Task and Operator Reference pp. 23-480 (458) · G Develop 298 · H Release Notes 187 |
| Geometry | symmetric margins: left/right 2.5 cm, top 3.9 cm, bottom 2.2 cm (`style.typ`, `set page`) |
| Header | logo left on every page; `Version 26.2` / `Generated <date> (<commit>)` right on every page but page 1 |
| Footer | running title (`A Build › A.3 …`) left, `Page n \| total` right, orange, on every page but page 1 |
| Pagination | page 1 title page, page 2 parts contents; a part starts on whichever page follows |
| Spacing | paragraph spacing 2.24 em, block spacing 1.52 em (house style) |
| Links | 3193 internal jumps, 614 external links plus 70 into the published site; blue, underlined, external ones with `↗`; no footnotes |
| Images | 641, all ICC-based RGB; 565 carry a soft mask (transparency). Effective resolution in the print scope (§5), 586 images: 331 below 300 ppi, 144 below 200, 49 below 150 |
| Colour | orange, peach, slate and link blue; grey code ground; red for danger admonitions; the part diagrams mark their part with a red frame |
| Text | justified, hyphenation off |
| Tables | 273 header rows emitted by pandoc as `table.header`, which Typst repeats on every page |
| PDF | Typst 0.15.1 writes PDF 1.4-2.0, PDF/A and PDF/UA, **not PDF/X**; Ghostscript 10.08 is available (§7) |

Verified in a Typst 0.15.1 probe: `set page(binding: left, margin: (inside: …, outside: …))`,
`pagebreak(to: "odd")`, `calc.odd(here().page())` in header and footer, `text(costs: (widow: …,
orphan: …))` and `footnote`. A blank page inserted by `pagebreak(to: "odd")` **still gets header and
footer**; suppressing them needs its own rule.

## 2. Provider: BoD

Decided (D2). Researched 2026-09-14; re-check the current specification before ordering.

| Requirement | BoD | Source |
| :-- | :-- | :-- |
| Pages, A4 paperback | 1,200 on 80 g, 1,050 on 90 g white, 900 on 90 g cream, 120 g or 130 g | Buch drucken |
| Paper | white or cream 80 g is **for publishers only**; 90 g for everyone | Grafiken und Farbmanagement |
| Image resolution | at least **300 dpi** at printed size; line art without grey levels (bitmap) **1200 dpi** | Grafiken und Farbmanagement |
| Grey areas | at least **20 % black**, not lighter; grey steps in charts at least 20 % apart | Grafiken und Farbmanagement |
| Transparency | to be reduced before delivery; otherwise BoD reduces it, which "can change objects" | Grafiken und Farbmanagement |
| Colour | RGB recommended - BoD converts to CMYK for its presses; untagged RGB is read as sRGB, CMYK as ISO Coated v2 (FOGRA39); no colour separation | Grafiken und Farbmanagement |
| Bleed | 5 mm per side, only for content that runs off the page; no crop marks | Grafiken und Farbmanagement |
| Fonts and images | embedded | Hilfe |

Sources:
[BoD Buch drucken](https://www.bod.de/buch-drucken.html),
[BoD Grafiken und Farbmanagement](https://www.bod.de/bodfiles/GLOBAL-Storage/documents/help-documents/bod-grafiken-und-farbmanagement.pdf),
[BoD Hilfe](https://www.bod.de/hilfe/hilfe-und-service.html).

For comparison, not pursued: Amazon KDP allows 828 pages (black ink on white), Lulu 800.

## 3. Requirements

### R1 - Page furniture for verso and recto pages

- Page numbers sit on the **outer edge**: left on even (verso) pages, right on odd (recto) pages.
- Running titles mirror too, following book convention (the larger unit on the left page):
  - verso: `1234` at the outer left, `A Build` beside it
  - recto: `A.3 Task and Operator Reference` beside `1235` at the outer right
- `| total` is dropped - it has no meaning on paper.
- No logo and no version stamp on text pages (D9); both stay on the title page and the imprint.
- Margins become `inside`/`outside` with `binding: left` on A4 (D7). The gutter must grow with the
  spine; a starting proposal is inside 3.0 cm, outside 2.0 cm, which keeps today's 16 cm text width.
- No header and no footer on the title page, the imprint, blank pages and part covers.

### R2 - The title page is page 1 of the book block

- Page 1, recto. It keeps the house title block (eyebrow, title, version) and names the publisher,
  **eccenca GmbH**.
- The site link and the copyright line move to the imprint.
- Counted as page 1, number not printed.

### R3 - Imprint on page 2

Page 2, verso, no page furniture. Contents:

- title and edition: `eccenca Corporate Memory - Documentation, Version 26.2`, print edition,
  generated `<date>` from commit `<commit>` (moves here from the running header)
- publisher: **eccenca GmbH, Hainstraße 8, 04109 Leipzig, Germany**
- authors: the list below
- licence: CC BY-SA 4.0, as `README.md` states, with the copyright line from `mkdocs.yml`
- online edition: `https://documentation.eccenca.com/26.2/`, named as the complete reference for what
  the print edition shortens (§5)
- colophon: typeset with Typst from the Markdown sources; fonts Roboto, Roboto Mono, Noto Color
  Emoji, DejaVu
- no ISBN (D3)

#### Authors

Rule (D4, revised 2026-09-15): GitHub accounts of the contributors to
[eccenca/documentation.eccenca.com](https://github.com/eccenca/documentation.eccenca.com), **most
commits first**, printed with their **names**: the name in the hand-maintained `authors.names` of
`tools/pdf/print.yml` - for a profile without a name, or to add a title - else the name the GitHub
profile shows, else the GitHub ID. Not listed: anonymous contributions (commits whose e-mail maps to no
GitHub account), bot accounts, software agents (codex, claude) and the IDs in `authors.exclude`, whose
names are not looked up. Ties are ordered by ID, case-insensitive. `task pdf:authors` adds each author
that `authors.names` does not list yet, without a name and with the profile's name in a comment, so all
names are maintained in one place; an entry left empty prints the profile's name.

Measured with `gh api repos/eccenca/documentation.eccenca.com/contributors` on 2026-09-14:

| # | Commits | GitHub ID |
| --: | --: | :-- |
| 1 | 639 | rpietzsch |
| 2 | 532 | seebi |
| 3 | 66 | irangareddy |
| 4 | 62 | muddymudskipper |
| 5 | 61 | mgns |
| 6 | 53 | sobo |
| 7 | 29 | annamakor |
| 8 | 25 | msaipraneeth |
| 9 | 22 | saradaimi786 |
| 10 | 20 | louiswesterheide |
| 11 | 18 | robertisele |
| 12 | 12 | spl0tt |
| 13 | 11 | white-gecko |
| 14 | 10 | BorderCloud |
| 15 | 10 | haschek |
| 16 | 9 | MaximilianWenzel |
| 17 | 7 | tomatophantastico |
| 18 | 5 | adelahaye-ecc |
| 19 | 1 | dgrtner-ecc |
| 20 | 1 | looooph |
| 21 | 1 | peterfreytag |
| 22 | 1 | pkgut |

Dropped: two anonymous entries (33 and 2 commits).

Names, checked with `gh api users/<id>` on 2026-09-15: 16 of the 22 profiles show a name. `rpietzsch`,
`annamakor`, `MaximilianWenzel`, `adelahaye-ecc`, `dgrtner-ecc` and `pkgut` show none; they need an entry
in `authors.names`, or they print as their ID, and the build warns about each.

- **No software agent is in the list today.** Claude's commits carry a `Co-Authored-By` trailer and
  count for the human author; GitHub does not list co-authors as contributors. The exclusion rule
  still belongs in the tooling.
- GitHub counts commits on the default branch only.

### R4 - Links on paper

In the print edition (D8): internal links print their text plus a page reference `(p. 34)`; external
links print their text with a footnote holding the URL; no colour, underline or arrow. Link annotations
are left out of the book block - Ghostscript refuses PDF/X output while a page carries one (§7).

## 4. Decisions

D1-D11 made 2026-09-14; D12-D14 made 2026-09-15 (§10).

| # | Question | Decision |
| :-- | :-- | :-- |
| D1 | Scope | The print edition reduces sections instead of printing them in full, **configurable per section** as `full`, `list` or `omit`. Default: A.3 Task and Operator Reference → `list`, H Release Notes → `list`, everything else `full` (§5) |
| D2 | Provider | **BoD** (§2) |
| D3 | ISBN | none for now; may come later |
| D4 | Authors | names, most commits first: from `authors.names` in `print.yml`, else the GitHub profile, else the ID; no anonymous entries, bots, agents or excluded IDs (§3). Revised 2026-09-15 - first decided as GitHub IDs |
| D5 | Colour and paper | black and white interior on 80 g paper. BoD offers 80 g to publishers only - eccenca GmbH needs a publisher account |
| D6 | Editions | separate screen and print PDFs. `task pdf` stays the screen edition, unchanged; `task pdf:print` builds the book block, switched by a Typst input (`edition=print`) and a print configuration |
| D7 | Trim size | A4 |
| D8 | Links on paper | page references and URL footnotes, no link styling (R4) |
| D9 | Logo and version in the running header | title page and imprint only (R1) |
| D10 | Body type size | keep 10 pt and tighten the spacing (§5). A smaller body, 9 pt or even 8 pt, only if the page limit is still exceeded - not needed for the default configuration |
| D11 | Normalization | an **optional** Ghostscript pass after Typst: PDF/X-4, CMYK, all images at 300 dpi (§7) |
| D12 | Subtrees and pages | path rules in `tools/pdf/print.yml`: a `sections` key may name a page, which accepts `omit` only; no front matter property, no `.pdfexclude` (§10) |
| D13 | Parts of a page | the class `print-exclude`, effective in the print edition only; the site and the screen PDF are unchanged (§10) |
| D14 | What stands in for excluded content | pages and subtrees: nothing, also for a directory's `omit` (revises §5); parts of a page: one note per run of parts, pointing to the page in the online edition for the full details (§10) |

## 5. Page budget

### Type size and spacing

Measured by compiling variants of the current book (`dist/pdf/book.typ`) with modified copies of
`style.typ`:

| Variant | Pages | Characters per line |
| :-- | --: | --: |
| today: 10 pt, paragraph spacing 2.24 em, block spacing 1.52 em | 1680 | 104 |
| body 9 pt | 1512 (−10 %) | 115 |
| paragraph spacing 1.2 em, block spacing 1.0 em | 1571 (−6.5 %) | 105 |
| both | 1414 (−16 %) | 115 |

At 10 pt a full line already holds about 104 characters, well above the 45-75 recommended for
continuous reading; 9 pt makes it 115, and thinner light strokes on black-and-white 80 g paper make it
worse. The spacing saves two thirds as much without touching legibility.

A two-column A4 layout would bring lines to a comfortable length, but wide tables, code blocks and
screenshots would need to break out of the columns. Not proposed.

A heavier weight than Light for the print body (Regular) may print more reliably in black and white;
measure its page cost before deciding.

### Section modes

`full` prints the section as today. `omit` leaves it out without a trace in the text (D14, revised
2026-09-15); the imprint names the online edition as the complete reference. `list` reduces it to a
two-column table:

| Section | `list` renders | Measured |
| :-- | :-- | :-- |
| A.3 Task and Operator Reference | the section's own page and its five overview pages (Aggregators, Custom Workflow Tasks, Datasets, Distance Measures, Transformers), which already are generated `Name \| Description` tables; the 176 individual operator pages are dropped, and the navigation's operator categories under Transformers print as one **Category** \| **Transformers** table instead of empty headings | 458 → about 17 pages |
| H Release Notes | one table: **Release** (e.g. `Corporate Memory 26.2.1`) and **Summary** (the release page's introductory paragraph; where a release has none, the components it lists, e.g. `DataIntegration v26.2.0, Explore v26.2.2, …`) | 22 releases, 187 → about 3 pages |

In `list` mode, links from the kept tables to dropped pages print as plain text, not as footnotes; the
section opens with a sentence naming the online reference URL.

The configuration lives in `tools/pdf/print.yml`, keyed by the section's path in `nav.yml`
(`build/reference/`, `release-notes/`), so a section can be switched without touching code.

### Estimate for the default configuration

| Step | Pages |
| :-- | --: |
| today | 1680 |
| A.3 as `list` | ≈ 1239 |
| H Release Notes as `list` | ≈ 1055 |
| tighter spacing (−6.5 %) | ≈ 985 |
| imprint, recto starts and blank pages (at most 28) | ≈ 1015 |

About 1,015 pages: within BoD's 1,200 for A4 on 80 g.

## 6. Further changes towards a print-ready book block

### Pagination

- Parts start on a recto page: cover recto, then contents recto, then the part's text recto
  (`pagebreak(to: "odd")`). Costs at most three blank pages per part, 27 in total.
- The front contents start on page 3, recto.
- Blank pages stay empty - no header, no footer, no page number.
- The final page count is even.

### Typography

- Hyphenation on for the print edition (`lang: "en"`); justified text without it opens wide gaps.
- Widow and orphan costs, so no single line is left at the top or bottom of a page.
- Minimum type size: code 7.7 pt and the 6.3 pt terminal tables are acceptable on A4; set a floor in
  `codeblock()` so a wider table cannot shrink below 6 pt.
- Hairlines: table rules are 0.3 pt, dividers 0.5 pt - above the usual 0.25 pt minimum.
- Tighter paragraph and block spacing (§5).

### Black and white

- **Grey areas at least 20 % black** (BoD). Today's grounds are far lighter: the code and note ground
  `ec-wash` (`#F3F5F6`) and the peach bands print as a few percent grey. Either raise them to 20 % or
  drop the fills in favour of rules.
- Orange footer text, the link blue and the admonition accents need values that stay distinguishable
  in grey; the orange running title in particular turns into a pale grey.
- The part diagrams mark their part with a red frame; in grey the frame stays visible but no longer
  stands out. Check the four diagrams.
- Screenshots print in grey; UI states that differ only by colour lose their meaning.

### Images

- In the print scope 331 of 586 images are below 300 ppi at their printed size, 49 below 150.
- Stop scaling small screenshots up to the text width, which lowers their resolution further - the
  cheapest way to bring images closer to 300 ppi.
- 565 images carry transparency, almost all of them PNG screenshots with an alpha channel over a white
  page. BoD wants transparency reduced before delivery, and PDF/X-4 does not remove it (§7). Composite
  the alpha channel onto white while normalizing images, before Typst embeds them - lossless for these
  images, and the book block then carries no transparency at all.

### PDF output

- The optional normalization pass (§7).
- A preflight report per build: page size, page count against 1,200 and parity, all fonts embedded
  (`pdffonts`), images below 300 ppi (`pdfimages -list`), soft masks left, page-number position per page
  (`pdftotext -bbox`), blank pages really blank.

### Content

- Web-only phrasing: "click here", "Next chapter:" links, embedded videos printed as
  `[iframe: <url>]`. Print them as a footnote, or as a QR code for the few videos.
- Tutorial step headings that number themselves print as `A.9.3 1 Install …` - a content cleanup.
- An index at the back from the front-matter tags (45 tags on 531 pages) would give a paper reader a
  second way in. Optional.

### Delivery

- CI builds the book block as a second artifact next to the screen PDF.
- The cover (§9) needs the final page count and paper for its spine width, so it comes last.

## 7. Optional normalization pass (Ghostscript)

An optional post-processing step on the print PDF: `task pdf:print` runs it when asked
(`--normalize` / `PDF_NORMALIZE=1`) and writes `…-print-x4.pdf` next to the unnormalized file. BoD
accepts either; the normalized file is what a provider preflight sees.

### What it does

| Target | How |
| :-- | :-- |
| PDF/X-4 | `-dPDFX=4` with a prefix file derived from Ghostscript's `lib/PDFX_def.ps`, which writes `/GTS_PDFXVersion (PDF/X-4)`, `/Trapped /False` and the output intent |
| CMYK | `-sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK`; the output intent profile is ISO Coated v2 (FOGRA39), the space BoD assumes for CMYK |
| Images at 300 dpi | down: `-dDownsampleColorImages=true -dColorImageDownsampleType=/Bicubic -dColorImageResolution=300 -dColorImageDownsampleThreshold=1.0`, the same for grey images; lossless re-encoding with `/FlateEncode`. **Up: not possible in Ghostscript** (below) |
| No annotations | `-dPreserveAnnots=false` |

### Verified with Ghostscript 10.08.0

Converted pages 3-40 of the current PDF on 2026-09-14:

- the file carries `/GTS_PDFXVersion (PDF/X-4)` in the document info and `pdfxid:GTS_PDFXVersion='PDF/X-4'`
  in XMP, one output intent, `/Trapped /False`, no annotations, all 154 fonts embedded
- all 7 images converted from ICC-based RGB to CMYK; the 610 ppi image came out at 300 ppi
- the 215 ppi image **stayed at 215 ppi: Ghostscript downsamples, it never upsamples**
- all 7 soft masks survived - PDF/X-4 keeps transparency
- the Build cover rendered from the CMYK file shows no visible colour shift against the RGB original at
  screen resolution; the red frame, the orange and the peach band stay distinct
- 38 pages in 6 s: the whole book block takes a few minutes
- Ghostscript 10.08's documentation (`doc/src/VectorDevices.rst`) confirms `-dPDFX` values 1, 3 and 4
  (default 3) and PDF/X-4 support; the rendered manual page still says X-1 and X-3 only

Traps found:

- **A page with any annotation makes Ghostscript revert to normal PDF output**, with only a one-line
  warning. The book has about 3,900 link annotations - drop them (`-dPreserveAnnots=false`) and fail the
  task if the output lacks the PDF/X marker.
- `-dPDFX=4` alone writes **no** PDF/X marker and no output intent; the prefix file is required.
- `-sOutputICCProfile` with `-dPDFX` crashes the PDF interpreter (`/undefined in --runpdf--`) and leaves a
  truncated file - supply the profile only through the prefix file, which reads it with
  `--permit-file-read=<profile>`.
- Ghostscript ships a generic `default_cmyk.icc`, not FOGRA39. The ISO Coated v2 profile comes from the
  ECI and has to be downloaded and vendored (with its licence) or fetched in CI.

### Upsampling to 300 dpi

Ghostscript cannot raise an image's resolution. Images below 300 ppi at their printed size have to be
resampled **before** Typst embeds them, in the build:

- the printed width is known at build time for the common case: an image wider than the text column
  prints at the text width (16 cm), a narrower one at its natural size
- the build writes a resampled copy (Lanczos) to `dist/pdf/images/` with enough pixels for 300 ppi at
  that width, and points Typst at it; the originals under `site/` stay untouched
- the same step composites alpha onto white (§6), so resampling and transparency reduction happen once

Upsampling adds no detail - BoD says so itself: an image does not get better by raising its resolution
in a graphics program. It gives the printer a 300 dpi image to rasterize instead of leaving the
interpolation to the press, and it makes the preflight report clean. The originals below 150 ppi still
need replacing (P14).

### Black and white

The book prints in black and white, but BoD converts RGB itself and the pass is specified as CMYK. A
greyscale variant (`-sColorConversionStrategy=Gray`, output intent from a grey profile) would show the
final tones on screen and give smaller files. Keep CMYK as specified; add greyscale as a preview mode of
the same task, for checking the palette (P11).

## 8. Acceptance

- `task pdf` builds the screen PDF exactly as before: 1680 pages, unchanged look
- `task pdf:print` builds the book block with the configuration in `tools/pdf/print.yml`
- page 1 is the title page naming eccenca GmbH as publisher; page 2 is the imprint with the publisher's
  address and the authors by name, from `tools/pdf/authors.yml` and `print.yml`, most commits first
- on every numbered page the page number sits at the outer edge: left on even pages, right on odd
  pages - checked by the preflight report, not by eye
- title page, imprint, part covers and blank pages carry no header and no footer; text pages carry no
  logo and no version stamp
- the front contents and every part cover start on an odd page
- A.3 and H Release Notes print as two-column lists in the default configuration; switching either to
  `full` or `omit` in `print.yml` works without code changes
- internal links print page references, external links footnotes; the book block has no link annotations
- page count even and at most 1,200
- grey areas at least 20 % black; all fonts embedded; no soft masks left
- every image at 300 ppi or more at its printed size, or listed and accepted
- with normalization: the file declares PDF/X-4, carries a FOGRA39 output intent, CMYK images only, no
  image above 300 ppi
- a page key in `print.yml` drops that page; `omit` leaves no title and no note for a page or a section
- in the print edition, each run of `.print-exclude` parts is replaced by one note with the page's
  online address; the site and the screen PDF show the parts unchanged
- `task check` and `task test:unit` pass

## 9. Out of scope

- the cover file: front, spine and back, spine width from page count and paper, barcode
- ISBN and retail distribution (D3, maybe later)
- EPUB or other e-book formats
- translations

## 10. Excluding content from the print edition

**Status:** decided and implemented 2026-09-15 (D12-D14 in §4, backlog P18). With the three examples
configured, the print edition has 666 pages instead of 966.

The section modes (§5) shorten whole reference sections. Some content is unfit for paper at a finer
grain:

| Grain | Example | Print pages |
| :-- | :-- | --: |
| subtree | G.5 cmem-client: Python API, `develop/cmem-client-api/` - 75 pages, 74 of them generated | 207 |
| subtree | A.16 How to link IDS to OSINT, `build/tutorial-how-to-link-ids-to-osint/` - all 7 pages (decided 2026-09-15) | 68 |
| page | none configured yet; a page key leaves out a single page when one needs it | - |
| part of a page | A.14 Connect to Snowflake: the SQL code block of the collapsed `??? example "INSERT query"` block, lines 92-1094 of `docs/build/snowflake-tutorial/index.md` on 2026-09-15 - about 1,000 lines (decided 2026-09-15) | 25 (pp. 122-146) |

Measured in the print edition of 2026-09-15 (966 pages). Excluding all three saves about 300 pages.

### Constraints

- The build reads the rendered site, not the Markdown. A marker for a part of a page must survive
  Zensical's rendering; a rule for a page or subtree must be decidable from the paths in `nav.yml`.
- Generated pages are rewritten wholesale: `task update:cmemc` and `task update:cmem-client-api` run
  `rm -rf <dir>/*`, and `dec-tool update-di-reference` deletes its whole tree. Whatever is stored in a
  generated page, or next to it, is lost on the next run.
- The site and the screen PDF stay as they are (D6).

### Options

| Option | Subtree | Page | Part | Verdict |
| :-- | :-- | :-- | :-- | :-- |
| front matter property, e.g. `print: exclude` | each page marked | yes | no | rejected: lost on generated pages; a subtree means marking every page; no single place shows what the book leaves out |
| `.pdfexclude` file in gitignore syntax | yes | yes | no | rejected: a second configuration next to `print.yml`, with a new format and a discovery rule, spread over the tree; deleted with a generated directory |
| path rules in `tools/pdf/print.yml` | yes - `omit` exists | yes, once a key may name a page | no | **chosen** for subtrees and pages (D12) |
| comment pair `<!-- pdf-print-exclude-begin -->` … `<!-- pdf-print-exclude-end -->` | no | no | yes | works, not proposed: the pair must stay siblings, a single block costs two extra lines, and a misspelt marker is ignored without a trace |
| class `print-exclude` on the rendered element | no | no | yes | **chosen** for parts of a page (D13) |
| CSS selectors per page in `print.yml` | no | no | yes | rejected: ties the configuration to theme markup |
| `exclude_docs` or `not_in_nav` in `mkdocs.yml` | yes | yes | no | rejected: removes the pages from the site as well |

Verified on 2026-09-15 in a scratch project with Zensical 0.0.62 and the Markdown extensions of
`mkdocs.yml`:

- **Comment pairs:** they arrive in the HTML as unescaped comments. Both comments of a pair stay
  side by side, at top level and inside an admonition, a content tab and a list item.
- **The class:** it lands on the element in every spelling listed below. Removing the `.print-exclude`
  elements leaves exactly the unmarked content.
- **Front matter:** an unknown front matter key builds without a warning.

### Design

#### Subtrees and pages: path rules in `print.yml` (D12)

A key under `sections` names a docs directory, ending in `/` as today, or a single page, ending in
`.md`:

```yaml
sections:
  develop/cmem-client-api/: omit
  build/tutorial-how-to-link-ids-to-osint/: omit
  # a single page: <docs path>/index.md: omit
```

- A directory key keeps its three modes (§5). `omit` drops the section without a title or a note (D14).
  The first implementation (P8) left both; the imprint names the online edition as the complete
  reference instead.
- A page key accepts `omit` only; any other mode fails the build. The page is dropped without a note.
- Dropping the index page of a section keeps its other pages, under a heading with the section's
  navigation title - the shape Release Notes already has (§3).
- Keys do not nest: a key inside a directory that another key shortens fails the build.
- A key that matches no page in `nav.yml` fails the build, as today.
- A link to a dropped page prints the page's online address in a footnote, like any link that leaves
  the book (R4). Within a section that `list` or `omit` shortens, it prints as text, as today.

#### Parts of a page: the class `print-exclude` (D13)

One class, spelled the way the element takes it:

````markdown
??? example print-exclude "INSERT query"

    ```sql
    INSERT INTO product(...) VALUES ...
    ```

```{ .sql .print-exclude }
SELECT ...
```

A paragraph the print edition leaves out.
{ .print-exclude }

<div class="print-exclude" markdown>

Several blocks - also inside a list item, a content tab or an admonition.

</div>
````

- The print edition removes every element with the class from a page's article, before ids, links and
  headings are processed. The class has no effect on the site and the screen PDF.
- A heading inside a removed part leaves the numbering and the contents. Links to it print as text, the
  rule for any link without a target.
- The build logs how many parts it removed per page, so a marker that no longer matches shows.
- A note takes the place of a removed part (D14): *This print edition leaves out a part of this page.
  The online edition has the full details:* followed by the page's online address, with the anchor of
  the heading the part belongs to. Consecutive removed parts share one note.
- In the Snowflake tutorial the class goes on the SQL code block, as `{ .sql .print-exclude }` on its
  opening fence: exactly lines 92-1094 are removed. The `??? example "INSERT query"` block around it keeps
  its title and holds the note.
- A generated page cannot carry the class: its generator has to emit it, or a path rule drops the page.
- The name follows the edition. The site does not style the class; a later `@media print` rule could
  use it for printing from the browser.

### Implementation outline

- **Rules:** `load_section_rules` accepts `.md` keys, rejects any mode but `omit` for them and rejects
  nested keys.
- **Page `omit`:** `apply_section_rules` drops the page's entry. For an index page it inserts a heading
  entry with the navigation title, which `NavEntry.title` already carries.
- **Parts:** in the print edition, `page_article` replaces the `.print-exclude` elements with the note -
  one per run of consecutive parts - and counts them.
- **`omit` for directories:** no title and no note any more. `test_omit_drops_the_pages_and_leaves_a_heading_with_a_note`
  and `test_merge_renders_an_omitted_section_as_its_title_and_a_note` change with it.
- **Tests:** `tests/test_build_pdf_print.py` gets page keys, the mode check, nesting, a dropped index
  page, and the removal with its note and online address in the print edition only.
- **Documentation:** the `sections` comment in `print.yml`, and for authors a line in
  `.claude/docs-guidelines/repo-conventions.md` on the class, including that generated pages cannot
  carry it.
- **Effort:** small to medium; backlog P18.
