---
title: "Marketplace Packages: Development and Publication"
icon: material/code-json
tags:
    - Python
---
# Development and Publication of Marketplace Packages

## Introduction

Marketplace Packages are archives that wrap certain content, functionality and configuration of Corporate Memory used to share and extend any such.

Each package has its own release cycle.
Packages can can be installed and uninstalled during runtime.

In order to support the development and publication of Marketplace Packages, we published a [package-template](https://github.com/eccenca/cmem-package-template).
Please have a look at this to get started.

This page gives an overview of the concepts you need to understand in order to develop plugins.

## Package Structure

The [package-template](https://github.com/eccenca/cmem-package-template) will create the boilerplate for a package repository.

### License

!!! info "No publication without license"

    Packages without a license declaration can not be pusblished to a Corporate Memory Marketplace Server.

Our template will bootstrap with a _Apache License 2.0 ([`Apache-2.0`](https://spdx.org/licenses/Apache-2.0.html))_, see <https://spdx.org/licenses/> if you need a different.
You can remove a license entirely, however, a package that does not declare a license can not be published.

### Manifest

The `manifest.json` is the central package definition.
It contains all relevant package metadata and describes the package contents.
It is used to present package details and contents to the `inspect` commands<!-- or in the marketplace frontends-->, to install, configure and uninstall all parts of a package.

#### Metadata

`package_type`
:   `project`
    :   A package that may ship any content, mainly intended to contain BUILD projects, (instance/data) graphs, SHACL shapes, workspace configuration, query catalogs, etc.

    `vocabulary`
    :   A package that is supposed to contribute vocabulary / ontology contents, such as `rdf:`, `org:`, `sso:`, etc. Such package may contain multiple vocabularies / ontologies. Packaging related SHACL shapes is reasonable, too.

`package_id`
:   Unique package identifier

`package_version`
:   Semantic version identifier string of the package, but limited to proper releases.

`metadata.name`
:   The package name in english

`metadata.description`
:   The package description in english.

`metadata_comment`
:   A maintainer or publisher comment.

#### Files

##### Graphs

##### Projects

#### Dependencies

##### Python Plugin Packages

##### (Vocabulary) Packages

