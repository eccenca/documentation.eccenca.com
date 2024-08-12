---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 24.2.0

Corporate Memory 24.2.0 is the first release in the 24.2 release line.

<!--
![24.1: Build - Key Shortcuts in Workflow Editor](24-1-build-workflow-editor-shortcuts.png "24.1: Build - Key Shortcuts in Workflow Editor"){ class="bordered" }
![24.1: Automate - New cmemc command groups Access Condition and Graph Validation](24-1-cmemc-new-command-groups.png "24.1: Automate - New cmemc command groups Access Condition and Graph Validation"){ class="bordered" }
![24.1: Explore and Author: Preview of our new SHACL Authoring Engine](24-1-explore-shacline2-preview.png "24.1: Explore and Author: Preview of our new SHACL Authoring Engine"){ class="bordered" }
-->

The highlights of this release are:

-   Explore and Author:
    -
-   Build:
    -
-   Automate:
    -  Extension to many **import commands** to allow for importing graphs, projects, datasets and vocabularies from the web
    -  Extension to the **graph validation export** command to produce JUnit XML reports for better integration into CI/CD pipelines

This release delivers the following component versions:

-   eccenca DataIntegration v24.2.0
-   eccenca DataManager v24.2.0
-   eccenca DataPlatform v24.2.0
-   eccenca Corporate Memory Control (cmemc) v24.2.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v10.7.1
-   Keycloak v24.0.5

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v24.2.0

...

## eccenca DataManager v24.2.0

...

## eccenca DataPlatform v24.2.0

...

## eccenca Corporate Memory Control (cmemc) v24.2.0

v24.2.0 of Corporate Memory Control (cmemc) adds the following new features:

-   `admin store migrate` command
    -   Migrate configuration resources to the current version.
-   `graph validation export` command
    -   export validation reports as JSON or jUnit XML
-   `graph import` command
    -   support for importing graphs from remote HTTP/HTTPS locations
-   `project import` command
    -   support for importing project zip files from remote HTTP/HTTPS locations
-   `dataset create` command
    -   support for creation of resource file from remote HTTP/HTTPS locations
-   `dataset upload` command
    -   support for uploading of resource file from remote HTTP/HTTPS locations
-   `vocabulary import` command
    -   support for importing vocabulary from remote HTTP/HTTPS locations
-   `smart_path` package as a replacement for `pathlib.Path` and expanded functionality to support both local file paths and remote file paths
-   `ClickSmartPath` parameter type, extending `click.path` to accommodate remote files
-   `graph validation execute` command group
    -   option `--query` to allow specifying a select query for resource selection.
    -   option `--ignore-graph` to provide multiple graph IRIs to be excluded from the resource selection.
    -   option `--result-graph` to specifies the graph where the validation results will be written.
    -   option `--replace` to replace the result graph with new validation results


v24.2.0 of Corporate Memory Control (cmemc) ships the following fixes:

-   `graph import` command
    -   importing a directory to a single graph no longer raises an error but imports all turtle files to this graph
-   `admin workspace python install` command
    -   report errors from update_plugins API
-   using not existing configurations (`-c` / `--configuration`) now results in a proper error message
-   `workflow io` command
    -   can now generate ttl output files
-   `admin workspace python list` command
    -   listing of published packages with the `--available` option now works for more than 19 packages
-   `graph export` command
    -   newly created directories have correct access conditions now
-   `vocabulary install` command
    -   raise proper usage error messages
-   `vocabulary uninstall` command
    -   raise proper usage error messages
-   `admin store export` command
    -   validates the exported zip and raises an error in case of a corrupted ZIP export

## Migration Notes

!!! info

    TODO

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v24.1.0 into DataIntegration v23.3.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v23.3.0 can be imported into DataIntegration v24.1.0.

### DataIntegration

TODO

### DataManager

TODO

### DataPlatform

TODO

### cmemc

No migrations are required going from cmemc 23.1.x to 24.2.x.

