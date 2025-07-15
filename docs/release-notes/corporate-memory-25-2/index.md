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

We are excited to announce the release of DataIntegration v25.2.0, which introduces powerful new file handling capabilities, enhanced workflow features, and important infrastructure updates.

**v25.2.0 of DataIntegration adds the following new features:**

-   New operators and dataset for improved file handling in workflows:
    -   **Add project files** workflow operator - Add files to projects directly from workflows
    -   **Get project files** workflow operator - Retrieve and process project files within workflow executions
    -   **Binary file dataset** - Handle binary files (PDF, images, etc.) in data integration pipelines
-   **Neo4j database configuration** - Added parameter to configure specific databases in Neo4j connections
-   **Project variable autocompletion** - All template operators now support autocompletion for project variables
-   **Camel case transform operator** - Convert text to camel case format for data standardization
-   **Project page URL suffix configuration** - New config key `workbench.project.defaultUrlSuffix` to configure the project page view (defaults to `?itemType=workflow&page=1&limit=10`)
-   **Path auto-completion** - Mapping and linking rule editors now feature intelligent path auto-completion like in value mapping forms

**v25.2.0 of DataIntegration introduces the following changes:**

-   **Infrastructure updates:**
    -   Migrated to Java 21 for improved performance and latest language features
    -   Updated Docker base image to `eclipse-temurin:21-ubi9-minimal`
-   **"Internal dataset (single graph)"** added to plugins to properly display reports using this dataset type
-   **Configurable favicon** - Organizations can customize the application favicon
-   **JSON dataset improvements:**
    -   New parameter to control automatic navigation into JSON arrays
    -   New `#arrayPath` path operator for explicit navigation into JSON arrays (available when automatic JSON array navigation is set to `false`)
    -   New `#uuid` path operator generates type 3 (name-based) UUIDs from JSON node string representations
    -   New `#arrayText` path operator for enhanced array value extraction

**v25.2.0 of DataIntegration ships the following fixes:**

-   Fixed queries with ORDER BY clauses in SQL dataset
-   Fixed create task dialog focus issues when opened via 'connect to newly created...' menu option
-   Fixed errors in Office365 dataset tests and adapted to Microsoft API changes
-   Fixed display issues for workflow reports containing internal datasets
-   Fixed drag-and-drop problems when adding operators to nested workflow editors
-   Non-printable characters in CSV datasets are now preserved during read/write transformations
-   XML datasets now return empty values for empty tags when string values are expected
-   Project variable updates now properly use the triggering user's credentials

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

### eccenca DataIntegration

-   The following plugins have been deprecated and will be removed in a future release:
    -   Old Python plugins depending on Jython (Python 2.x)
    -   Spark scripting plugins
    -   Spark virtual dataset
    -   Legacy REST operator
-   To check if your instance uses any deprecated plugins, use the endpoint: `GET {DataIntegrationURL}/api/core/usages/deprecatedPlugins`

### eccenca Corporate Memory Control (cmemc)

-   With the introduction of the `graph imports` command group, the `graph tree` command is now deprecated.
    -   use `graph imports tree` instead
