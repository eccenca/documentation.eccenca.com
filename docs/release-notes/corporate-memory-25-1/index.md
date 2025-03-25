---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 25.1.0

Corporate Memory 25.1.0 is the first major release in 2025.

<!--
todo
![24.3: Explore - New Shacl(2) based dossier view](24-3-explore-shacl2-dossier.png "24.3: Explore - New Shacl(2) based dossier view"){ class="bordered" }
![24.3: Build - Workflow report entity preview](24-3-build-wf-report-preview.png "24.3: Build - Workflow report entity preview"){ class="bordered" }
![24.3: Automate - Migration recipe list](24-3-automate-admin-migration-list.png "24.3: Automate - Migration recipe list"){ class="bordered" }
-->

The highlights of this release are:

-   Explore and Author:
    -   TODO
-   Build:
    -   TODO
-   Automate:
    -   TODO

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged into a single component eccenca Explore.

This release delivers the following component versions:

-   eccenca DataIntegration v25.1.0
-   eccenca Explore v25.1.0 (formerly DataPlatform and DataManager)
-   eccenca Corporate Memory Control (cmemc) v25.1.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v10.8.3
-   Keycloak v25.0.6

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v25.1.0

We're excited to bring you the latest update to DataIntegration v25.1, which introduces new features, improvements and bug fixes:

**v25.1.0 of DataIntegration adds the following new features:**

-   Use colors for workbench tags.
-   Added a new operator for concatenating input values into a file.
-   Enabled copy & paste functionality in rule editors.
-   Datasets with explicit schemas can now be directly connected to workflow operators.
    -   Supported for CSV and text datasets.
    -   If a supported dataset is connected to a workflow operator with a flexible input schema, the entire dataset (i.e., all properties of its primary type) is read.
    -   For CSV datasets, this results in entities being read with all columns included.
-   Allow changing the width of blocks in the mapping editor.

**v25.1.0 of DataIntegration introduces the following changes:**

-   Invisible parameters are now part of the config port schema.
-   Improved file names for downloaded projects and workspaces.
-   SPARQL results are streamed as JSON instead of XML.
-   The root breadcrumb and the _Build_ logo in the navigation sidebar now direct to the _projects_ search facet instead of _All types_.

**v25.1.0 of DataIntegration ships the following fixes:**

-   Fixed URI rule evaluation failure for empty object mappings.
-   No duplicate JDBC jar configuration is required anymore.
-   Fixed issue with JSON datasets not always navigating into arrays.
-   Fixed issue where direct transform execution does not use project variables.
-   Fixed Transform Evaluation failure when a rule contains a template transformer.
-   Fixed issue where URI pattern input sometimes resets to its initial value or crashes the mapping editor.
-   Fixed issue where SPARQL restriction expands the wrong SPARQL pattern when using property paths with prefixed names.
-   Fixed RDF file upload issue.
-   Fixed issue where the reference entities cache fails to load a large number of entities from the RDF store.
-   Fixed issue where tasks created in the workflow editor are not added to the recently viewed list.
-   Fixed issue where adding a note to a linking rule fails to save.

## eccenca Explore v25.1.0

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

We are excited to announce Explore v25.1, which introduces new features, improvements and bug fixes.

**v25.1.0 of Explore adds the following new features:**

-   TODO

**v25.1.0 of Explore ships the following changes:**

-   TODO

**v25.1.0 of Explore ships the following fixes:**

-   TOFO

## eccenca Corporate Memory Control (cmemc) v25.1.0

We're excited to bring you the latest update to Corporate Memory Control (cmemc) v25.1, which introduces new features, improvements and bug fixes.

**v25.1.0 of cmemc adds the following new features:**

-   TODO

**In addition the following changes and fixes are included:**

-   TODO

## Migration Notes

!!! info

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v25.1.0 into DataIntegration v24.3.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v24.3.0 can be imported into DataIntegration v25.1.0.

### eccenca DataIntegration

-   TODO

### eccenca Explore

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

-   TODO

### eccenca Corporate Memory Control (cmemc)

-   TODO
