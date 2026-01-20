---
status: new
title: "Marketplace Packages: Overview"
icon: material/shopping
hide:
    - toc
---

# Marketplace Packages

Beginning from version 26.1, we support the creation and use of Marketplace Packages.

Marketplace Packages are a mechanism to wrap everything belonging to a certain configuration of a Corporate Memory based solution or project into a single sharable and managed artifact:

-   Vocabularies / Ontologies
-   (SKOS) Taxonomies
-   (Instance / Data) Graphs
-   BUILD Projects
-   Dependencies to
    -   [python-plugins](../python-plugins/index.md)
    -   (other) Marketplace Packages

The lifecycle of a Corporate Memory Marketplace Package is shown in the following flow chart

The following pages give an overview about this feature:

![Corporate Memory Marketplace Package Lifecycle](mpp-lifecycle.svg){ width="50%" }

<div class="grid cards" markdown>

-   :material-download-circle-outline: [Installation and Management](installation/index.md)

    ---

    Intended for Linked Data Experts and Corporate Memory Admins, this page outlines how to (un)install and manage Marketplace Packages.

    This section discusses the lifecycle commands and staged `copier copy`, _Package Definition and Release_, `install --input PATH` (from local), `export` as well as `build` and `publish`.

-   :material-code-json: [Development and Publication](development/index.md)

    ---

    Intended for Linked Data Experts, Consultanta and Partners, this page gives an overview on how to start develop and publish Marketplace Packages.

</div>
