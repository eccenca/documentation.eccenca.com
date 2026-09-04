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

For previewing there are two tasks, and the difference matters:

| Task | Live reload | Shows the site as it ships |
| :--- | :---------- | :------------------------- |
| `task serve` | yes | **no** |
| `task preview` | no | yes |

`zensical serve` rebuilds into `site/` on every change, which would overwrite whatever the
post-build steps produce - so its preview has no tag listings and still loads `glightbox`
from a CDN. `task preview` builds once with every post-build step and serves the result on
port 8001 (override with `PORT=…`). Use `serve` while writing prose, `preview` before you
trust what you see.

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
| `tablesort`, `glightbox` | vendored under `docs/assets/`; `tools/localize_bundle_assets.py` rewrites the CDN URLs Zensical bakes into its JS bundle |
| Redirects | static stubs under `docs/` |
| Comment opt-out | `overrides/partials/comments.html` |
| Tag listings ([#38](https://github.com/zensical/backlog/issues/38)) | `tools/render_tag_listings.py` - **temporary**, see `tasks/spec.md` |
| Tag chip links ([#38](https://github.com/zensical/backlog/issues/38)) | `overrides/partials/tags.html` - **temporary**, same removal trigger |

The tag-listing renderer expands the `<!-- material/tags -->` markers on `/tags/` and
`/tutorials/` after the build, and the `tags.html` override links each page's tag chips to
its section there. Both are deliberately throwaway: the Markdown sources still use
Material's own marker syntax and Zensical's stock template already knows how to render a
linked chip - it just has no listing to point at yet. When Zensical ships listings the
feature works natively, the renderer prints a banner telling you to delete it, and the
override can go with it.

The two build the anchor slug independently - MiniJinja in the template, Python in the
renderer - so `check_zensical_output.py` asserts that every chip anchor resolves on
`/tags/`. That check is what turns a slug mismatch into a failed build instead of 703 dead
links.

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
