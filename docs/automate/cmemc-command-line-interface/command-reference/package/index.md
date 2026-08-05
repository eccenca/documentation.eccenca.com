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


## package inspect

Inspect the manifest of a package.

```shell-session title="Usage"
$ cmemc package inspect [OPTIONS] PACKAGE_PATH
```





??? info "Options"
    ```text

    --key TEXT  Get a specific key only from the manifest.
    --raw       Outputs raw JSON.
    ```

## package list

List installed packages.

```shell-session title="Usage"
$ cmemc package list [OPTIONS]
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
$ cmemc package install [OPTIONS] [PACKAGE_ID]
```




This command installs a package either from the marketplace or from local package archives (.cpa) or package directories.

If a local package is chosen which has unzipped project directories, the installation will handle the zipping silently. See the `package export` command for more information.



??? info "Options"
    ```text

    -i, --input PATH        Install a package from a package archive (.cpa) or
                            directory.
    --replace               Replace (overwrite) an existing package version or
                            package content, if present.
    --no-cache              Disable using cached package versions.
    --ignore-lock           Ignore and release the package lock file for this
                            operation. Use this to recover from a stale lock
                            left by an interrupted run. Dangerous under
                            concurrent access (it removes the lock other
                            processes rely on); use with care.
    --version TEXT          Specific version to install from the marketplace.
                            Defaults to the latest version.
    --marketplace-url TEXT  Base URL of the Marketplace - uses environment
                            variable ECCENCA_MARKETPLACE_URL if available.
                            [default: https://eccenca.market]
    ```

## package uninstall

Uninstall installed packages.

```shell-session title="Usage"
$ cmemc package uninstall [OPTIONS] [PACKAGE_ID]
```





??? info "Options"
    ```text

    --ignore-lock            Ignore and release the package lock file for this
                             operation. Use this to recover from a stale lock
                             left by an interrupted run. Dangerous under
                             concurrent access (it removes the lock other
                             processes rely on); use with care.
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

    --mime_type [text/turtle|text/turtle+pretty]
                                    Choose the MIME type for graphs when
                                    exporting packages.  [default:
                                    text/turtle+pretty]
    --filter <TEXT TEXT>...         Filter installed packages by one of the
                                    following filter names and a corresponding
                                    value: type, name, id.
    -a, --all                       Export all installed packages.
    --output-dir DIRECTORY          Create package directories in this base
                                    directory.  [default: .]
    --replace                       Replace (overwrite) existing files, if
                                    present.
    --extract                       Extract the project files specified in the
                                    manifest and replace the archive with
                                    itsextracted directory. This is useful for
                                    version controlled package directories.
    ```

## package build

Build a package archive from a package directory.

```shell-session title="Usage"
$ cmemc package build [OPTIONS] PACKAGE_DIRECTORY
```




This command processes a package directory, validates its content including the manifest, and creates a versioned Corporate Memory Package Archive (.cpa) with the following naming convention: {package_id}-v{version}.cpa

If the package contains an extracted project (directory) instead of a ZIP, it is zipped automatically in a temporary copy — the original package directory is never modified. The manifest still need to reference the project ZIP. See the `package export` command for more information.

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
$ cmemc package publish [OPTIONS] PACKAGE_ARCHIVE
```





??? info "Options"
    ```text

    --timeout INTEGER            Timeout for marketplace requests.
    --marketplace-url TEXT       Base URL of the Marketplace - uses environment
                                 variable ECCENCA_MARKETPLACE_URL if available.
                                 [default: https://eccenca.market]
    --marketplace-account TEXT   Marketplace account - uses environment variable
                                 ECCENCA_MARKETPLACE_ACCOUNT if available.
    --marketplace-password TEXT  Marketplace password - uses environment
                                 variable ECCENCA_MARKETPLACE_PASSWORD if
                                 available.
    ```

## package search

Search for available packages with a given search text.

```shell-session title="Usage"
$ cmemc package search [OPTIONS] [SEARCH_TERMS]...
```





??? info "Options"
    ```text

    --raw                   Outputs raw JSON.
    --marketplace-url TEXT  Base URL of the Marketplace - uses environment
                            variable ECCENCA_MARKETPLACE_URL if available.
                            [default: https://eccenca.market]
    ```

