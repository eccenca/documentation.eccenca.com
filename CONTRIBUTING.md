# Contributing

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing to the eccenca Corporate Memory documention project.

## How Can I Contribute?

### Report Bugs

If you found a bug and its easy to fix, you can just click the edit button and fix it yourself sending a pull request 🤓.
However, you can also [file a bug](https://github.com/eccenca/documentation.eccenca.com/issues/new?assignees=&labels=bug&template=bug_report.md&title=) in the [issue tracker](https://github.com/eccenca/documentation.eccenca.com/issues) of this project.

### Suggest Enhancements

You always can [suggest enhancements](https://github.com/eccenca/documentation.eccenca.com/issues/new?assignees=&labels=enhancement&template=documentation-request.md&title=) in the [issue tracker](https://github.com/eccenca/documentation.eccenca.com/issues) of this project.

### Send Pull Requests

We are open for contributions via pull request.
Try to test your contribution locally before pushing your changes.

## What should I know before I get started?

This documentation project is made with [mkdocs](https://www.mkdocs.org/) and the [material theme for mkdocs](https://squidfunk.github.io/mkdocs-material/).
The documentation is written in [markdown](https://commonmark.org/) and the project dependency management is done by [poetry](https://python-poetry.org/).
We suggest to use a specialized markdown editor such as [obsidian](https://obsidian.md/) if you plan to not just fix a typo.

The following tools you need locally to get started:

- [poetry](https://python-poetry.org/)
- [task](https://taskfile.dev/)
- git, markdown editor

The following shell session demonstrates the local workflow (after you forked the repository):

``` shell-session
$ git clone <your repository fork>
Cloning into 'documentation.eccenca.com'...
...
$ cd documentation.eccenca.com/
$ task serve
task: [install] poetry install
Creating virtualenv in ...
Installing dependencies from lock file

Package operations: 62 installs, 0 updates, 0 removals
...
task: [serve] poetry run mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 20.03 seconds
INFO     -  [16:25:36] Watching paths for changes: 'docs', 'mkdocs.yml', 'overrides'
INFO     -  [16:25:36] Serving on http://127.0.0.1:8000/
```
After that, you can go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and start changing / adding files in the docs directory.
Changes are served live on localhost.

## Repository rules

- always create a directory + `index.md`, e.g. `my-topic/index.md` ([Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/automate/cmemc-command-line-interface))
- add new pages to the `.pages` file to add them in the right order and with correct title to the menu ([Example](https://github.com/eccenca/documentation.eccenca.com/blob/main/docs/automate/cmemc-command-line-interface/.pages))
- put images side by side to the `index.md` ([Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/release-notes/corporate-memory-22-1))
- do not use images for icons esp. icons from the application - use theme icons instead, e.g. `:material-play:` -> [icon list](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/?h=icon)
- name image files properly (not just `Screenshot.xxx.png`, [Example](https://github.com/eccenca/documentation.eccenca.com/tree/main/docs/release-notes/corporate-memory-22-1))
- used advanced features where suitable
  - [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage) (esp. use notes and warnings where needed)
  - [Code Blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#usage) (e.g. enable highlightning and add a title)
  - [Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage) (to structure complex pages)
