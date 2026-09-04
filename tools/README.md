# documentation.eccenca.com -> tools

This directory is the `dec-tool` package: every script that builds, generates or
checks part of this site is a subcommand of it. Run `poetry run dec-tool --help`
for the current list, or a subcommand with `--help` for its options.

Nothing here is meant to be called directly - the `Taskfile.yml` targets are the
supported entry points and pass the right options.

| Command | Used by | Purpose |
| :------ | :------ | :------ |
| `build-navigation` | `task update:navigation`, `task check:navigation` | Build `nav.yml` from the `docs/**/.pages` files; `--check` diffs instead of writing and fails on drift |
| `check-zensical-output` | `task check:output` | Inspect the built `site/` and fail if a feature we reimplemented for Zensical regressed |
| `localize-bundle-assets` | `task build` | Rewrite the third-party asset URLs Zensical bakes into its JavaScript bundle to the vendored copies |
| `update-icons` | `task update:icons` | Fetch the eccenca icon set from the gui-elements repository |
| `update-di-reference` | `task update:di-reference` | Generate the task and operator reference pages from a running Corporate Memory |
| `update-integrations` | `task update:integrations` | Render the integrations page from `data/integrations.yml` |
