# documentation.eccenca.com -> tools

This directory is the `dec-tool` package: every script that builds, generates or
checks part of this site is a subcommand of it. Run `poetry run dec-tool --help`
for the current list, or a subcommand with `--help` for its options.

Nothing here is meant to be called directly - the `Taskfile.yml` targets are the
supported entry points and pass the right options.

| Command | Used by | Purpose |
| :------ | :------ | :------ |
| `build-navigation` | `task update:navigation`, `task check:navigation` | Build `nav.yml` from the `docs/**/.pages` files; `--check` diffs instead of writing and fails on drift |
| `build-pdf` | `task pdf`, `task pdf:print` | Merge the built `site/` along `nav.yml` into one document and typeset it as a single PDF with pandoc and Typst; style, filter and fonts are in `pdf/` |
| `pdf-authors` | `task pdf:authors` | Write the print edition's author list `pdf/authors.yml` from the commits to the printed pages and the names on the authors' GitHub profiles; names and exclusions are kept in `pdf/print.yml`, where it adds each new author without a name |
| `pdf-normalize` | `task pdf:print -- --normalize`, `task pdf:print -- --gray` | Write the print PDF as PDF/X-4 in CMYK with Ghostscript, checking the result for the PDF/X marker; the ISO Coated v2 profile is fetched into `dist/icc/`. `--gray` writes a greyscale preview of the black-and-white print instead, PDF/X-4 by the grey profile Ghostscript ships |
| `pdf-preflight` | `task pdf:print` | Check the book block for print: A4, even page count, embedded fonts, image resolution, soft masks, annotations, page-number position, blank pages, light grey areas |
| `check-zensical-output` | `task check:output` | Inspect the built `site/` and fail if a feature we reimplemented for Zensical regressed |
| `image-widths` | - | List raster images that print below 150 ppi in pages that are not generated; `--fix` writes the `width="NN%"` their pixels support in the 16 cm print column |
| `localize-bundle-assets` | `task build` | Rewrite the third-party asset URLs Zensical bakes into its JavaScript bundle to the vendored copies |
| `update-icons` | `task update:icons` | Fetch the eccenca icon set from the gui-elements repository |
| `update-di-reference` | `task update:di-reference` | Generate the task and operator reference pages from a running Corporate Memory |
| `update-integrations` | `task update:integrations` | Render the integrations page from `data/integrations.yml` |
