---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 25.2.0

Corporate Memory 25.2.0 is the second major release in 2025.

<!--
![25.1: Build - Seamless Workflow Integration](25-1-build-connect-csv-datasets-directly.png "25.1: Build - Seamless Workflow Integration"){ class="bordered" }
![25.1: Build - Improved Rule Editing Experience](25-1-build-copy-paste.png "25.1: Build - Improved Rule Editing Experience"){ class="bordered" }
![25.1: Explore - Streamlined Shape Management](25-1-explore-node-shape-quick-access.png "25.1: Explore - Streamlined Shape Management"){ class="bordered" }
-->

The highlights of this release are:

-   Build: **Seamless Workflow Integration**
    -   Directly connecting datasets with explicit schemas to workflow operators simplifies data ingestion and processing, allowing users to quickly incorporate CSV and text data into their workflows.

-   Build: **Improved Rule Editing Experience**
    -   Enhanced copy & paste functionality in rule editors boosts productivity by making it easier to manage and edit rules accurately and efficiently.

-   Explore and Autor: **Streamlined Shape Management**
    -   The introduction of new SHACL shape quick-access options empowers users to effortlessly build, validate, and troubleshoot complex shape configuration.

-   Automate: **Lightning-fast Parameterized Queries**
    -   The new `cmemc` query placeholder specifications enable super-fast execution of parameterized queries by running background value queries to provide dynamic completions, significantly enhancing data query responsiveness.

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged into a single component eccenca Explore.

This release delivers the following component versions:

-   eccenca DataIntegration v25.1.1
-   eccenca Explore v25.1.1 (formerly DataPlatform and DataManager)
-   eccenca Corporate Memory Control (cmemc) v25.4.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v10.8.5
-   Keycloak v25.0.6

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v25.2.0

...

## eccenca Explore v25.2.0

...

## eccenca Corporate Memory Control (cmemc) v25.4.0

!!! info inline end "Important info"

    This eccenca Corporate Memory release is the first release where we introduced Semantic Versioning for our components.
    This cmemc release notes section reflects this by reporting multiple minor versions in one section.

We are excited to announce cmemc v25.4.0, which introduces new features, improvements and bug fixes.

**v25.4.0 of cmemc adds the following new features:**

-   `query` command group
    -   can be used with arbitrary query graphs now
    -   `query list` command - new `--catalog-graph` option to select query catalog
    -   `query execute` command - new `--catalog-graph` option to select query catalog
    -   `query open` command - new `--catalog-graph` option to select query catalog

**v25.3.0 of cmemc adds the following new features:**

-   `dataset create` command
    -   support for binary file datasets
        -   suggest pdf, png, jpg, jpeg, gif and tiff files as binary file dataset
        -   shell completion of these files
-   `workflow io` command
    -   support for binary file datasets
        -   accept `application/octet-stream` as mime type for input and output files
        -   shell completion of pdf, png, jpg, jpeg, gif and tiff files as input and output
    -   add support for markdown documents as text datasets

**v25.2.0 of cmemc adds the following new features:**

-   `graph imports` command group
    -   `graph imports create` command - Add graph import to a graph
    -   `graph imports delete` command - Delete graph import from a graph
    -   `graph imports list` command - List accessible graph's imports
-   `graph export` command
    -   `--include-import-statements` option to save a `*.imports` file preserving imports of a graph
-   `graph import` command
    -   `--include-import-statements` option to read the `*.imports` files and add the preserved imports to the store
-   `graph delete` command
    -   `--include-import-statements` option to delete imports from other graphs to the deleted graph

## Migration Notes

### eccenca Corporate Memory Control (cmemc)

- With the intoduction of the `graph imports` command group, the `graph tree` command is now deprecated.
    -   use `graph imports tree` instead

