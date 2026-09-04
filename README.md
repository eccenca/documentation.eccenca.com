# [documentation.eccenca.com](https://documentation.eccenca.com)

[![example workflow][build-shield]][github-actions] [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa] [![CC BY-SA 4.0][mkdocs-shield]][mkdocs] [![made-with-Markdown][markdown-shield]](http://commonmark.org)

Shared repository of the eccenca Corporate Memory documentation.

| Branch | Deployment |
| :----- | :--------- |
| `main` | [https://dev.documentation.eccenca.com](https://dev.documentation.eccenca.com) |
| `published` | [https://documentation.eccenca.com](https://documentation.eccenca.com) |

If you consider to contribute to this project, please have a look on [CONTRIBUTING.md](https://github.com/eccenca/documentation.eccenca.com/blob/main/CONTRIBUTING.md)

## Building the site

The site is built with [Zensical](https://zensical.org), the successor to Material for
MkDocs. Run `task build` to build into `site/` and `task check` for the full check suite.

For previewing there are two tasks:

| Task | Live reload | Shows |
| :--- | :---------- | :---- |
| `task serve` | yes | the pages as you write them |
| `task public:preview` | no | the site as it will be published |

Use `serve` while writing prose. It rebuilds into `site/` on every change, which overwrites
what the post-build steps produced, so it loads `glightbox` and the ResizeObserver polyfill
from a CDN instead of from the vendored copies - invisible on screen, and nothing
downstream trusts a `site/` left behind that way.

`task public:preview` is the one to run before publishing: it deploys into a throwaway copy
of the `published` branch, serves that on port 8002 (override with `PORT=…`), and deletes
the branch again when you stop it. Because it is `public:deploy` pointed at a scratch
branch, what it serves is what publishing produces - versioned URLs, the version selector,
the outdated-version banner and the root redirect included.

Two Material for MkDocs features are **not yet implemented by Zensical** and are
therefore missing from the output. They are tracked in `tools/check_zensical_output.py`,
which reports them as `PEND` on every build and prints a banner as soon as one starts
working:

| Feature | Zensical backlog | Effect today |
| :------ | :--------------- | :----------- |
| Social cards | [#37](https://github.com/zensical/backlog/issues/37) | No `og:image`, so link previews are blank |
| Revision dates | [#18](https://github.com/zensical/backlog/issues/18) | No "Last update" on any page |

Everything else Zensical leaves out is reimplemented here and **guarded as a required
check** - the build fails if any of it regresses:

| Feature | Replaced by |
| :------ | :---------- |
| Self-hosted fonts | `docs/assets/fonts.css` plus `theme.font: false` |
| `tablesort`, `glightbox`, `resize-observer-polyfill` | vendored under `docs/assets/`; `tools/localize_bundle_assets.py` rewrites the CDN URLs Zensical bakes into its JS bundle |
| Redirects | static stubs under `docs/` |
| Comment opt-out | `overrides/partials/comments.html` |

### Vendored third-party assets

Serving these from our own origin is what keeps visitor IP addresses away from third
parties - but it also makes us their redistributor, so each copy carries its licence:

| Asset | Version | Licence | Upstream |
| :---- | :------ | :------ | :------- |
| `assets/glightbox/glightbox.min.{js,css}` | 3.3.1 | MIT, © 2018 Biati Digital | [glightbox](https://github.com/biati-digital/glightbox) |
| `assets/resize-observer-polyfill/ResizeObserver.global.js` | 1.5.1 | MIT, © 2016 Denis Rul | [resize-observer-polyfill](https://github.com/que-etc/resize-observer-polyfill) |
| `assets/tablesort.min.js` | 5.2.1 | MIT, © 2021 Tristen Brown | [tablesort](http://tristen.ca/tablesort/demo/) |
| `assets/fonts/*.woff2` | - | Apache-2.0 | Roboto and Roboto Mono via Google Fonts |

The files are byte-identical to their upstream builds except for a prepended `/*! … */`
licence banner, which is the notice MIT asks to travel with a copy; the full licence text
sits next to each one where upstream ships it. Three of the URLs Zensical bakes into its
bundle are deliberately **not** vendored - mermaid, Ace and Pyodide are unreachable for
this corpus, and `localize_bundle_assets.py` fails the build if a page ever starts using
one.

Tag listings and the links from each page's tag chips to them are **native** as of
Zensical 0.0.58. The local stand-ins for both - a post-build renderer and a `tags.html`
partial override - are gone; the Markdown sources still carry Material's own
`<!-- material/tags -->` markers, which Zensical now expands itself.

`check-zensical-output` keeps guarding the result: it asserts that tag chips link
somewhere at all and that every anchor they point at exists on `/tags/`. A slug mismatch
between a chip and its listing would otherwise ship as hundreds of dead links rather than
fail the build.

`task check:navigation` additionally fails if `nav.yml` no longer matches the `docs/**/.pages`
files, which remain the source of truth for navigation (`task update:navigation` regenerates it).

See `tasks/handoff.md` for the full migration notes.

## License

Copyright © 2025 [eccenca GmbH](https://eccenca.com)

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[github-actions]: https://github.com/eccenca/documentation.eccenca.com/actions
[build-shield]: https://github.com/eccenca/documentation.eccenca.com/actions/workflows/pages.yml/badge.svg
[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[mkdocs-shield]: https://img.shields.io/badge/Made%20with-mkdocs-brightgreen
[mkdocs]: https://www.mkdocs.org/
[markdown-shield]: https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg
