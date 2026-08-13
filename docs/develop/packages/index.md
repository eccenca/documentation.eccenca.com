---
status: new
title: "Marketplace Packages: Overview"
icon: material/shopping
tags:
    - Marketplace
    - Package
hide:
    - toc
---

# Marketplace Packages

Starting with version 26.1, we support the creation and use of Marketplace Packages.

Marketplace Packages bundle everything for a specific Corporate Memory–based solution or project into a single shareable, managed artifact:

- Vocabularies / Ontologies
- (SKOS) Taxonomies
- (Instance / Data) Graphs
- Build Projects
- Dependencies on
    - [python-plugins](../python-plugins/index.md)
    - (other) Marketplace Packages

This lets you share and reuse them across projects, teams, and different Corporate Memory instances.

A Marketplace Package is distributed as a **C**orporate Memory **P**ackage **A**rchive (`.cpa` file), a zip-based archive which you can either hand over directly or publish to a Marketplace Server - a central repository which supports pushing and pulling packages.

The lifecycle of a Corporate Memory Marketplace Package is shown in the following flowchart.

![Corporate Memory Marketplace Package Lifecycle](mpp-lifecycle.svg){ width="50%" }

!!! info "Looking for the user interface?"

    The [Marketplace](../../distribution/marketplace/index.md) chapter describes how to discover, install and uninstall packages in the Corporate Memory user interface.
    The pages below focus on the command line and on package development.

The following pages give an overview of this feature:

<div class="grid cards" markdown>

- :material-download-circle-outline: [Installation and Management](installation/index.md)

    ---

    Intended for Linked Data Experts, Deployment Engineers, and Corporate Memory Admins, this page outlines how to (un)install and manage Marketplace Packages, and where installed contents appear in Corporate Memory.

    This section discusses the lifecycle commands and stages `search`, `install`, `list` and `uninstall`.

- :material-code-json: [Development and Publication](development/index.md)

    ---

    Intended for Developers, Linked Data Experts, Consultants, and Partners, this page gives an overview of how to start developing and publish Marketplace Packages, followed by a [step-by-step tutorial](development/tutorial/index.md).

    This section discusses the lifecycle commands and stages `copier copy`, _Package Definition and Release_, `inspect`, `install --input PATH` (from local), _Solution Development and Configuration_, `export`, `build`, and `publish`.

</div>
