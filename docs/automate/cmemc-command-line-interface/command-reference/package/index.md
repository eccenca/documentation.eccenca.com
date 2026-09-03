---
title: "cmemc: Command Group - package"
description: "List, (un)install, download, export, create, or inspect packages."
icon: eccenca/module-marketplace
tags:
  - cmemc
  - Package
  - Marketplace
---

# package Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, (un)install, download, export, create, or inspect packages.

Packages bundle re-usable content such as projects or vocabularies together with a manifest, so that it can be distributed and installed in other deployments. Packages are identified by a `PACKAGE_ID` and are used either as a package directory, as a Corporate Memory Package Archive (.cpa), or from a marketplace.

Typical workflows are to install packages from a marketplace (`package search` and `package install`), to fetch a package archive without installing it (`package download`), and to create packages from your own workspace (`package export`, `package build` and `package publish`).

!!! note
    To get a list of installed packages, execute the `package list` command or use tab-completion.



## package inspect

Inspect the manifest of a package.

```shell-session title="Usage"
cmemc package inspect [OPTIONS] PACKAGE_PATH
```




This command outputs the metadata of a package, taken from the manifest of a package archive (.cpa) or of an (extracted) package directory. Since the manifest is read from the given path, the package does not need to be installed in the workspace.

Without further options, all manifest keys and values are shown in a table. With the ``--key`` option, only the keys which start with the given value are shown; if this matches a single key, its plain value is output, which is useful for scripting. Use ``--key`all` to output the complete manifest again.



??? info "Options"
    ```text

    --key TEXT  Get a specific key only. If the given value is the prefix of
                more than one key, the table is reduced to these keys. Use `all`
                to output the complete table.
    --raw       Outputs raw JSON.
    ```

## package list

List installed packages.

```shell-session title="Usage"
cmemc package list [OPTIONS]
```




Outputs a table of the packages which are currently installed in your Corporate Memory, with their ID, installed version, type and name. The package IDs can be used as a reference for the `package uninstall` and `package export` commands.

!!! note
    In order to list the packages which are available on the marketplace but not necessarily installed, use the `package search` command instead.




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

## package download

Download a package archive from the marketplace.

```shell-session title="Usage"
cmemc package download [OPTIONS] PACKAGE_ID
```




This command downloads a package from the marketplace to your local file system, without installing it in Corporate Memory. The package archive is created in the output directory with the following naming convention: `{package_id}-v{version}.cpa`

The downloaded archive can be examined with the `package inspect` command, installed with `package install`--input``, or uploaded to another marketplace with the `package publish` command.

!!! note
    Available packages can be listed with the `package search` command.




??? info "Options"
    ```text

    --version TEXT          Specific version to download. Defaults to the latest
                            version.
    --output-dir DIRECTORY  Download the package archive into this directory.
                            [default: .]
    --replace               Replace (overwrite) existing package archives, if
                            present.
    --with-dependencies     Also download the marketplace packages this package
                            depends on.
    --marketplace-url TEXT  Base URL of the Marketplace - uses environment
                            variable ECCENCA_MARKETPLACE_URL if available.
                            [default: https://eccenca.market]
    ```

## package uninstall

Uninstall installed packages.

```shell-session title="Usage"
cmemc package uninstall [OPTIONS] [PACKAGE_ID]
```




This command removes installed packages from Corporate Memory. The packages to uninstall are selected either by giving a package ID, by using the ``--filter`` option, or by using the ``--all`` flag.

By default, dependencies between packages are respected, so uninstalling a package which is still needed by another installed package will fail. With the ``--all`` flag, all packages are removed regardless of their dependencies.

!!! warning
    Uninstalling a package removes the resources it provides from your Corporate Memory, so use this command with care.




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




This command exports installed packages from Corporate Memory to the local file system. For each exported package, a directory named after the package ID is created in the output directory, holding the manifest and the exported package content. The packages to export are selected either by giving a package ID, by using the ``--filter`` option, or by using the ``--all`` flag.

With the ``--extract`` flag, the build project archives referenced in the manifest are unpacked into directories and the archives are removed. This results in a directory structure which is better suited for version control. Note that the manifest still references the project ZIP files, and that the `package build` and `package install` commands zip such directories again on the fly.



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
cmemc package build [OPTIONS] PACKAGE_DIRECTORY
```




This command processes a package directory, validates its content including the manifest, and creates a versioned Corporate Memory Package Archive (.cpa) with the following naming convention: {package_id}-v{version}.cpa

If the package contains an extracted project (directory) instead of a ZIP, it is zipped automatically in a temporary copy — the original package directory is never modified. The manifest still need to reference the project ZIP. See the `package export` command for more information.

!!! note
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




This command uploads a Corporate Memory Package Archive (.cpa) to a marketplace server, so that it can be found with the `package search` command and installed with the `package install` command. Package archives are created with the `package build` command; the published package ID and version are taken from the manifest inside the archive.

Publishing requires a marketplace account. Account and password are given with the ``--marketplace-account`` and ``--marketplace-password`` options or with the corresponding environment variables, otherwise they are requested interactively.



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
cmemc package search [OPTIONS] [SEARCH_TERMS]...
```




This command fetches the list of packages which are available on the marketplace and outputs their ID, name, description and type. The package IDs can be used as a reference for the `package install` command.

Each search term is matched case-insensitively against the ID, name, description and type of package, and only packages which match all given terms are listed. Without any search term, all available packages are listed.

!!! note
    In order to list the packages which are installed in your Corporate Memory, use the `package list` command instead.




??? info "Options"
    ```text

    --raw                   Outputs raw JSON.
    --marketplace-url TEXT  Base URL of the Marketplace - uses environment
                            variable ECCENCA_MARKETPLACE_URL if available.
                            [default: https://eccenca.market]
    ```
