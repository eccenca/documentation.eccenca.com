---
title: "Marketplace Packages: Installation and Management"
icon: material/download-circle-outline
tags:
    - Marketplace
    - Package
---
# Installation and Management of Marketplace Packages

## Introduction

Marketplace Packages can be installed directly from the eccenca Corporate Memory Marketplace Server (e.g. [https://eccenca.market](https://eccenca.market)), or from local **C**orporate Memory **P**ackage **A**rchives (`.cpa` files) and package directories.

This page describes how to search, install, list, and uninstall Marketplace Packages using `cmemc`.

!!! info "Managing packages in the user interface"

    Packages published on a Marketplace Server can also be installed and uninstalled in the [Marketplace](../../../distribution/marketplace/index.md) module of Corporate Memory.

!!! info "`cmemc package` reference"

    The [cmemc package command group](../../../automate/cmemc-command-line-interface/command-reference/package/index.md)
    contains all needed commands to support the complete package lifecycle.

## Search Packages

Use the following command to search a Marketplace Server for available packages:

```shell title="Search the Marketplace Server"
cmemc package search vocab
```

## Install Packages

Use the following command to install a package from a Marketplace Server:

```shell-session title="Install a package from the Marketplace Server"
$ cmemc package install w3c-xsd-vocab
Installing package 'w3c-xsd-vocab' from marketplace ... done
```

For installing local package archives (`.cpa` files) or package directories, use the `--input` option:

```shell-session title="Install a package from a .cpa file"
$ cmemc package install --replace --input my-package-v0.0.0-4b7516f.cpa
Installing package 'my-package' from 'my-package-v0.0.0-4b7516f.cpa'
done
```

!!! info "Replacing installed packages"

    Use `--replace` to overwrite an already installed package version or package content.
    Without this option, installing over existing content fails.

### Dependencies and Version Constraints

A package can depend on other Marketplace Packages and on Python plugin packages, and it can restrict the versions it accepts with a [version constraint](../development/index.md#version-constraints).
The installation takes care of the dependencies:

- A missing dependency is installed at the newest version that satisfies all constraints declared on it.
- An installed dependency at a satisfying version is left untouched.
- If an installed dependency violates a constraint, the installation fails before anything is changed.
- If the installation would violate the constraint of another installed package, it is refused before anything is changed, and the affected packages are named.

Use `--force-dependencies` to install anyway.
The option upgrades or downgrades the installed dependency and warns about every installed package it breaks.

!!! warning "Forcing dependencies can break installed packages"

    A package whose constraint is violated stays installed but is not guaranteed to work.
    Check the dependency tree after a forced installation.

Use the following command to show the dependency tree of the installed packages:

```bash title="Show the dependency tree"
cmemc package dependencies
```

Each dependency is listed with its declared constraint, the installed version and its state: `satisfied`, `violated`, or `missing`.
Add a package ID to show the tree of one installed package only.
Reinstalling a dependency at a satisfying version repairs a `violated` or `missing` dependency.

### Upgrade Packages

Use `--replace` to upgrade an installed package to the latest version of the Marketplace Server:

```bash title="Upgrade a package to the latest version"
cmemc package install --replace w3c-xsd-vocab
```

Add `--version` to install a specific version, which also changes to an older version:

```bash title="Install a specific version"
cmemc package install --replace --version 1.0.0 w3c-xsd-vocab
```

The rules for dependencies apply to an upgrade in the same way.

## List Packages

Use the following command to list all installed packages:

```shell title="List installed packages"
cmemc package list
```

To review the manifest of a package (installed, local directory, or `.cpa` file), use the `inspect` command:

```shell title="Inspect a package manifest"
cmemc package inspect my-package-v0.0.0-4b7516f.cpa
```

## Where Package Contents Appear

Depending on the content types inside it, an installed package appears in different places in Corporate Memory, with each item (graph, project, workflow, ...) surfacing in its respective component.

<div style="clear: both" markdown>

!!! info inline ""

    ![Example: Graphs](example-vocabulary.png "Example: Graphs"){ width="68%" }

**Graphs** such as data graphs but also **Vocabularies** or **Shapes Catalogs** are listed in [**Explore > Graphs**](../../../explore-and-author/graph-exploration/index.md#graphs).

</div>

<div style="clear: both" markdown>

!!! info inline ""

    ![Example: Projects](example-project.png "Example: Projects")

**Projects** are imported into [**Build**](../../../build/introduction-to-the-user-interface/index.md#projects).
When you install your first project package, Corporate Memory also creates a special project to store all installed files.
This project is automatically managed by the package system, and removed once the last package is uninstalled.

</div>

<div style="clear: both" />

## Uninstall Packages

Use the following command to uninstall a package:

```shell title="Uninstall a package"
cmemc package uninstall PACKAGE_ID
```

This removes all package contents from the Corporate Memory instance, including graphs and Build projects that were installed as part of the package.
