---
status: new
title: "Marketplace Packages: Overview"
icon: material/shopping
hide:
    - toc
---

# Marketplace Packages

Starting with version 26.1, we support the creation and use of Marketplace Packages.

Marketplace Packages bundle everything for a specific Corporate Memory–based solution or project into a single shareable, managed artifact:

-   Vocabularies / Ontologies
-   (SKOS) Taxonomies
-   (Instance / Data) Graphs
-   BUILD Projects
-   Dependencies on
    -   [python-plugins](../python-plugins/index.md)
    -   (other) Marketplace Packages

The lifecycle of a Corporate Memory Marketplace Package is shown in the following flowchart.

![Corporate Memory Marketplace Package Lifecycle](mpp-lifecycle.svg){ width="50%" }

The following pages give an overview of this feature:

<div class="grid cards" markdown>

-   :material-download-circle-outline: [Installation and Management](installation/index.md)

    ---

    Intended for Linked Data Experts and Corporate Memory Admins, this page outlines how to (un)install and manage Marketplace Packages.

    This section discusses the lifecycle commands and stages `copier copy`, _Package Definition and Release_, `inspect`, `install --input PATH` (from local), _Solution Development and Configuration_, `export`, `build`, and `publish`.

-   :material-code-json: [Development and Publication](development/index.md)

    ---

    Intended for Linked Data Experts, Consultants, and Partners, this page gives an overview of how to start developing and publish Marketplace Packages.

    This section discusses the lifecycle commands and stages `install`, `list` and `uninstall`.

</div>
