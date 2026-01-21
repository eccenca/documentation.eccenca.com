---
title: "Marketplace Packages: Installation and Management"
icon: material/download-circle-outline
tags:
  - Package
---
# Installation and Management of Marketplace Packages

## Introduction

Marketplace Packages can be installed directly from a Corporate Memory Marketplace Server or from local package archives (`.cpa` files).

This page describes how to install, list, and uninstall packages using `cmemc`.

!!! info "`cmemc package` reference"

    Refer to [TODO: link](./) for the complete reference of the `package` command group.

## Install Packages

Use the following command to install a package from a Marketplace Server:

```sh
cmemc package install PACKAGE_ID
```

For installing local package archives (`.cpa` files) or package directories, use the `--input` option:

```sh
cmemc package install --input PATH
```

## List Packages

Use the following command to list all installed packages:

```sh
cmemc package list
```

## Uninstall Packages

Use the following command to uninstall a package:

```sh
cmemc package uninstall PACKAGE_ID
```

This removes all package contents from the Corporate Memory instance, including graphs and Build projects that were installed as part of the package.
