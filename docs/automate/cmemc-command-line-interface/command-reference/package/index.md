---
title: "cmemc: Command Group - package"
description: "List, (un)install, export, create, or inspect packages."
icon: material/shopping
tags:
  - cmemc
  - Package
---

# package Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, (un)install, export, create, or inspect packages.

## package create

Initialize an empty package directory with a minimal manifest.

```shell-session title="Usage"
cmemc package create [OPTIONS] PACKAGE_ID
```

??? info "Options"
    ```text

    --name TEXT         The package name in english. Defaults to package ID.
    --version TEXT      Semantic version identifier string of the package, but
                        limited to proper releases.  [default: 0.0.1]
    --description TEXT  The package description in english.  [default: This is
                        the first version of a wonderful eccenca Corporate
                        Memory package 🤓]
    ```

## package inspect

Inspect the manifest of a package.

```shell-session title="Usage"
cmemc package inspect [OPTIONS] PACKAGE_PATH
```

??? info "Options"
    ```text

    --key TEXT  Get a specific key only from the manifest.
    --raw       Outputs raw JSON.
    ```

## package list

List installed packages.

```shell-session title="Usage"
cmemc package list [OPTIONS]
```

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter installed packages by one of the following
                             filter names and a corresponding value: type, name,
                             id.
    --id-only                Lists only package IDs. This is useful for piping
                             the IDs into other commands.
    --raw                    Outputs raw JSON.
    ```

## package install

Install packages.

```shell-session title="Usage"
cmemc package install [OPTIONS] [PACKAGE_ID]
```

This command installs a package either from the marketplace or from local package archives (.cpa) or directories.

??? info "Options"
    ```text

    -i, --input PATH  Install a package from a package archive (.cpa) or
                      directory.
    --replace         Replace (overwrite) existing package version, if present.
    ```

## package uninstall

Uninstall installed packages.

```shell-session title="Usage"
cmemc package uninstall [OPTIONS] [PACKAGE_ID]
```

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter installed packages by one of the following
                             filter names and a corresponding value: type, name,
                             id.
    -a, --all                Uninstall all packages. This is a dangerous option,
                             so use it with care.
    ```

## package export

Export installed packages to package directories.

```shell-session title="Usage"
$ cmemc package export [OPTIONS] [PACKAGE_ID]
```

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter installed packages by one of the following
                             filter names and a corresponding value: type, name,
                             id.
    -a, --all                Export all installed packages.
    --replace                Replace (overwrite) existing files, if present.
    ```

## package build

Build a package archive from a package directory.

```shell-session title="Usage"
cmemc package build [OPTIONS] PACKAGE_DIRECTORY
```

This command processes a package directory, validates its content including the manifest, and creates a versioned Corporate Memory package archive (.cpa) with the following naming convention: {package_id}-v{version}.cpa

Package archives can be published to the marketplace using the `package publish` command.

??? info "Options"
    ```text

    --version TEXT          Set the package version.
    --replace               Replace package archive, if present.
    --output-dir DIRECTORY  Create the package archive in a specific directory.
                            [default: .]
    ```

## package publish

Publish a package archive to the marketplace server.

```shell-session title="Usage"
cmemc package publish [OPTIONS] PACKAGE_ARCHIVE
```

??? info "Options"
    ```text

    --marketplace-url TEXT  Alternative Marketplace URL.
    ```
