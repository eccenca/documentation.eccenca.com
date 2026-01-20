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

Use the [package-template](https://github.com/eccenca/cmem-package-template) to create the boilerplate for a package repository.

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

A package can contain graphs or Build projects, those contents are referenced in the `manifest.json`

##### Graphs

Add the following structure to add a graph.
`register_as_vocabulary` and `import_into` are optional instructions.
We suggest to organize graphs in a respective sub-folder (here `graphs/`), but this is up to you:

```json
"files": [
    …
    {
        "file_type": "graph",
        "file_path": "graphs/file.ttl",
        "graph_iri": "http://www.example.org/file/",
        "register_as_vocabulary": true,
        "import_into": [
            "http://www.example.org/integration_graph/"
        ]
    },
    …
]
```

##### Projects

Add the following structure to add a project.
We suggest to organize projects in a respective sub-folder (here `projects/`), but this is up to you:

```json
"files": [
    …
    {
        "file_type": "project",
        "file_path": "projects/my-build-project.zip",
        "project_id": "my-build-project"
    },
    …
]
```

#### Dependencies

Dependencies to other (vocabulary) packages or to python plugins can be declared in `copier copy` answers.
The dependencies are added to the `manifest.json` as described in the next sections.

##### Python Plugin Packages

Add the following to declare a dependency to a python plugin:

```json
"dependencies": [
    …
    {
      "dependency_type": "python-package",
      "pypi_id": "cmem-plugin-pyshacl"
    },
    …
]
```

##### (Vocabulary) Packages

Add the following to declare a dependency to a (vocabulary) package:

```json
"dependencies": [
    …
    {
      "dependency_type": "vocabulary",
      "package_id": "w3c-rdfs-vocab"
    }
    …
]
```

## Building Packages

!!! info "`cmemc package build` reference"

    Refer to [TODO: link](./) for the complete command reference.

During development you can install a package from a local path (plain folder or a `.cpa` package) using the `cmemc package install --input PATH` command.

Use the `cmemc package build` command.
This will build a package archive from a package directory.

This command processes a package directory, validates its content including the manifest, and creates a versioned Corporate Memory package archive (`.cpa`) with the following naming convention: `{package_id}-v{version}.cpa`.

## Publishing Packages

!!! info "`cmemc package publish` reference"

    Refer to [TODO: link](./) for the complete command reference.

Package archives can be published to the marketplace using the `cmemc package publish` command.
