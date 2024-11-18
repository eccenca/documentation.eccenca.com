---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 24.3.0

Corporate Memory 24.3.0 is the third major release in 2023.

<!-- ![24.2: Explore - New Shacl(2) based Data Exploration](24-2-explore-shacl2.png "24.2: Explore - New Shacl(2) based Data Exploration"){ class="bordered" } -->
<!-- ![24.2: Explore - Sankey Chart Type](24-2-explore-charts-sankey.png "24.2: Explore - Sankey Chart Type"){ class="bordered" } -->
<!-- ![24.2: Build - Add new Datasets to Workflows by File Drag and Drop](24-2-build-add-ds-via-dnd.png "24.2: Build - Add new Datasets to Workflows by File Drag and Drop"){ class="bordered" } -->

The highlights of this release are:

-   Explore and Author:
    -
-   Build:
    -
-   Automate:
    -

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

This release delivers the following component versions:

-   eccenca DataIntegration v24.3.0
-   eccenca Explore v24.3.0 (formally separated into DataPlatform and DataManager)
-   eccenca Corporate Memory Control (cmemc) v24.3.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v10.8.0
-   Keycloak v26.0.5

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v24.3.0

...

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.
## eccenca Explore v24.3.0

...

## eccenca Corporate Memory Control (cmemc) v24.2.0

This version of cmemc adds the following new features:

-   `graph validation execute` command
    - `--inspect` option to return the list of violations instead of the summary (includes `--wait`)
-   `graph validation inpect` command
    - retrieval and display of titles as terminal links for resources
    - completion: retrieval and display of titles as descriptions
-   `graph validation list` command
    - retrieval and display of titles as terminal links for graphs
-   `graph export` command
    - option `--compress` to generate compressed ttl file
-   `graph import` command
    - support import of compressed ttl/nt files
-   `admin store export` command
    - `--replace` option to replace an existing file
    - if no BACKUP_FILE is given, a default of `{{date}}-{{connection}}.store.zip` is used
-   `project import` command
    - `--replace` option to replace an existing project
-   `project export` command
    - `--replace` option to replace an existing file
-   `admin workspace export`
    - `--replace` option to replace an existing file
-   `admin metrics` command group
    - support for build / data integration metrics, e.g. `build:cmem_workspace_task_spec_size`
    - support for graphdb store metrics, e.g. `store:graphdb_slow_queries_count`
-   `admin metrics list` command
    - documentation column to output table
    - `--filter` option to filter metrics table by job, name, ID, or type
-   `admin acl` command group
    - support for updated 24.3 access condition vocabulary and ACL graph
-   `admin migration` command group
    - `admin migration list` command - List migration recipies
    - `admin migration execute` command - Execute needed migration recipes
    - The following migration recipes are available:
        - `bootstrap-data` - Re-import bootstrap system data to match current version
        - `workspace-configurations` - Forward-upgrade explore workspace configurations
        - `acl-graph-24.3` - Move access conditions and used queries to new ACL graph
        - `acl-vocab-24.3` - Migrate auth vocabulary terms (actions and other grants)
        - `chart-widgets-24.3` - Migrate Chart Property Shapes to Widget Integrations
        - `workflow-trigger-widgets-24.3` - Migrate Workflow Trigger Property Shapes to Widget Integrations

In addition to that, these changes and fixes are included:

-   cmemc will not fail anymore when the config dir is not creatable (message in debug)
-   cmemc will not fail anymore when the config ini is not readable (message in debug)
-   For these commands `admin acl list`, `dataset list`, `graph list`, `project list`, `admin user list`, `project variable list`, `vocabulary list`, `workflow list`, `admin workspace python list`, `admin workspace python list-plugins`, `dataset resource list`, `workflow scheduler list`, and `vocabulary cache list`:
    - ommit empty tables with usage note message
-   `admin status` command
    - component name change: DI -> BUILD
    - component name change: DP -> EXPLORE
    - component removal: DM (merged into EXPLORE)
    - key prefix change: dp -> explore
    - key prefix change: di -> build
-   `project export` command
    - `--filename-template` completion examples adaption
-   `dataset create` command
    - Support compressed zip files for dataset types including CSV, XML, JSON, YAML, and plain text.
-   `admin metrics` command group
    - metrics identification now as combined ID of `job_id:metrics_name`
-   `admin metrics` command group
    - `--job` option, use `--filter job job_id` or combined metrics ID instead

## Migration Notes

!!! info

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v24.3.0 into DataIntegration v24.2.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v24.2.0 can be imported into DataIntegration v24.3.0.

### DataIntegration

...

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.
### Explore

...

### cmemc

-   All scripts which used the `admin status` command with the `--key` option:
    - adapt the key prefixes accordingly:
        - old: `cmemc admin status --key dp.info.license.validDate`
        - new: `cmemc admin status --key explore.info.license.validDate`
-   `admin store migrate` command deprecated
    - use the `admin migration` command group instead
-   `--overwrite` options deprecated - will be removed with the next major version
    - affected commands:
        - `project import` command
        - `project export` command
        - `admin workspace export` command
-   All scripts which used the `admin metrics` command group:
    - use combined metrics ID of `job_id:metrics_name`
    - use `--filter job job_id` instead of `--job job_id`

