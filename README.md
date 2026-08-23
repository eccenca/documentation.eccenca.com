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
MkDocs. Run `task build` to build into `site/`, `task serve` for a local preview and
`task check` for the full check suite.

Three Material for MkDocs features are **not yet implemented by Zensical** and are
therefore missing from the output. They are tracked in `tools/check_zensical_output.py`,
which reports them as `PEND` on every build and prints a banner as soon as one starts
working:

| Feature | Zensical backlog | Effect today |
| :------ | :--------------- | :----------- |
| Social cards | [#37](https://github.com/zensical/backlog/issues/37) | No `og:image`, so link previews are blank |
| Tag listings | [#38](https://github.com/zensical/backlog/issues/38) | `/tags/` and `/tutorials/` show no generated lists |
| Revision dates | [#18](https://github.com/zensical/backlog/issues/18) | No "Last update" on any page |

Features Zensical does not implement but that this repository replaces itself - self-hosted
fonts, vendored `tablesort` and `glightbox`, redirect stubs and the comment opt-out - are
guarded by the same script; it fails the build if any of them regress. `task check:nav`
additionally fails if `nav.yml` no longer matches the `docs/**/.pages` files, which remain
the source of truth for navigation (`task nav` regenerates it).

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
