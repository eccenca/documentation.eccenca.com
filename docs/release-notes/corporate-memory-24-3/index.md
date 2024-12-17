---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 24.3.0

Corporate Memory 24.3.0 is the third major release in 2024.

<!-- ![24.2: Explore - New Shacl(2) based Data Exploration](24-2-explore-shacl2.png "24.2: Explore - New Shacl(2) based Data Exploration"){ class="bordered" } -->
<!-- ![24.2: Explore - Sankey Chart Type](24-2-explore-charts-sankey.png "24.2: Explore - Sankey Chart Type"){ class="bordered" } -->
<!-- ![24.2: Build - Add new Datasets to Workflows by File Drag and Drop](24-2-build-add-ds-via-dnd.png "24.2: Build - Add new Datasets to Workflows by File Drag and Drop"){ class="bordered" } -->

The highlights of this release are:

-   Explore and Author:
    -   …
-   Build:
    -   …
-   Automate:
    -   …

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

This release delivers the following component versions:

-   eccenca DataIntegration v24.3.0
-   eccenca Explore v24.3.0 (formerly DataPlatform and DataManager)
-   eccenca Corporate Memory Control (cmemc) v24.3.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v10.8.2
-   Keycloak v25.0.6

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v24.3.0

We're excited to bring you the latest update to DataIntegration v24.3, which introduces new features, improvements and bug fixes:

v24.3.0 of DataIntegration adds the following new features:

-   Workspace search:
    -   Support to filter workflows that contain replaceable datasets.
    -   Display tags on workflow search items when they contain replaceable datasets.
    -   Add file name and graph URIs to search items as searchable tags.
-   Workflow editor:
    -   Support creating knowledge graph datasets from DataPlatform graphs matching the search query.
    -   Added copy prefixes option in copy task dialog.
-   Integration of a Prometheus endpoint to expose many useful metrics.
-   Transform operators to retrieve attributes from input tasks:
    -   _Input Task attributes_ retrieves individual attributes from the input task (such as the modified date) or the entire task as JSON.
    -   _Input file attributes_ retrieves a metadata attribute from the input file (such as the file name).
-   JdbcDialect implementation for Trino: Fixes STRING type mapping, adds isolationLevel option to avoid Connections resetting AutoCommit mode and serves as example for the dialect concept.
-   File hash transformer:
    -   Calculates the hash sum of a given file
    -   Works on either the input file dataset or a selected file from the project
-   JSON special paths:
    -   `#propertyName` accesses the current object key
    -   `*` selects all direct children of the current token
-   Add link from a task parameter description into the task's Markdown documentation for this parameter, if available.
-   Show sample (output) entities for workflow operators in the workflow reports.
-   Text dataset allows to configure the zip regex.
-   Support setting the locale for the 'Parse date pattern' and 'Parse date' transform operators.
    -   `*` selects all direct children of the current token
-   More fine-grained access control:
    -   In addition to a base action, it is possible to specify as many specific actions that protect specific endpoints.
    -   Endpoints are configured in a whitelist as URI prefixes per specific action.
    -   All endpoints that are protected by any specific action cannot be accessed anymore via the base action.
    -   Two new actions are configured by default and protect the Python plugin management and specific workspace API endpoints. See changes and migrations.
-   Global variables can be marked sensitive for storing passwords:
    -   Sensitive variables can only be used in password fields.
    -   Using sensitive variables in other fields or in variable templates fails and does not expose the value.
    -   Example:

        ```conf
        config.variables = {
            global = {
                sensitiveVar = {
                    value = "value 2"
                    isSensitive = true
                }
            }
        }
        ```

-   Delete project files operator: Allows to delete project files in a workflow based on a regex.
-   Added Snowflake dataset type.

v24.3.0 of DataIntegration introduces the following changes:

-   Optimized writing to Neo4j, resulting in a 25x speed improvement.
-   Upgraded Spark to 3.5.3.
-   Upgraded to typescript version 5.5.3.
-   After saving a workflow the undo/redo queues are cleared which is consistent with other editors in DI/DM.
-   Renamed DI action from `urn:eccenca:di` to `<https://vocab.eccenca.com/auth/Action/Build>`.
-   Line breaks are forced for evaluation preview tooltips.
-   If a project is copied to another project, all referenced project variables and their dependent variables are copied to the target project as well.
-   docker image: switch to `eclipse-temurin:17-ubi9-minimal` base image
-   Prefix handling:
    -   Only prefixes added to a specific project are serialized/exported, no prefixes loaded by the workspace (e.g. from DP).
    -   Only load user prefixes and prefixes of installed vocabularies from DP into DI.
-   All datasets that support zips can be written now.
-   Increase visibility of breadcrumbs in application header.
-   Configurable Favicon in DataIntegration.

v24.3.0 of DataIntegration ships the following fixes:

-   Jinja templates can lead to OutOfMemory issues.
-   Loading of JDBC Type 4 Drivers from Jar at runtime.
-   Add add-opens JDK option to sbt parameters to avoid Serialization errors in executors.
-   User defined function removed to prevent startup error in local dev mode.
-   After saving a workflow the workflow editor can be closed without warning of unsaved changes.
-   Race condition in Excel map transformer cache.
-   Remote Client-Side Code Execution through CSV Injection identified in penetration testing.
-   CSV datasets should not be cleared at the beginning of a workflow since they are overwritten anyway.
-   Ports of datasets are shown as required in workflow validation, but are not.
-   In workspace/project item search disable Enter behavior while a search is pending.
-   Use correct icons for copy/clone actions.
-   Workflow editor:
    -   Workflow is not re-validated after undo/redo operations.
    -   Re-configuring a workflow node to not having a data output is not immediately visible (only after reload).
    -   When the `Create new dataset` operator is used it always creates a _dataset_ even though the item type was changed.
    -   Caches of file base datasets are not refreshed when updated via file download operator.
    -   Dependency ports checkbox does not show checkmark in workflow tasks with unconnected output port.
    -   Fix text on node menu options that have a checkbox. Always show the _enabled_ text.
-   REST task:
    -   When paging is enabled and entities are output only the last request result is output.
    -   Add TLSv1.3 support.
-   Hierarchical mapping editor: Entity relationship direction input does not show current selection.
-   Transform rule editor:
    -   Validation errors are not shown when starting the evaluation.
    -   Notifications are not correctly cleared and shown.
-   Transform execution report:
    -   Type URI validation issues are not shown in the transform execution report.
    -   Rule tree in transform execution report and evaluation tab has a broken collapse/expand state.
-   Password parameter templates are empty initially.
-   Fix issues in create/update dialog:
    -   Depending input gets disabled if dependent input has an empty default value.
    -   Data preview of dataset with nested parameters is not working.
-   Task config preview has a different parameter ordering than in the create/update dialog.
-   Evaluation of a text path of a text dataset in a rule editor fails.
-   Cannot execute SPARQL update queries with parameter templates.
-   `Evaluate template` operator: Changed project variable not updated without evaluating transform.
-   Jinja interpreter does not clear previous errors.
-   Process of opening and closing the handle tools menu.
-   Manually defined project prefixes are automatically copied to other projects after reload.
-   Removing a vocabulary does not remove the vocabulary prefix from the DI projects.
-   Cannot reconfigure parameter values with templates in workflows.
-   Workflow report shows multiple executions of some operators even though they were only executed once.
-   Python Workflow status incorrect.
-   Python Workflow operators could not be cancelled in some cases.
-   Alignment dataset should support the clear method so it can be used in workflows.
-   Drop zone in workflow editor freezes sometimes after dropping an operator.
-   Transform/Linking operator's 'Restriction' documentation is incorrectly formatted.
-   DI project "Items per page" cuts off "100" as "1...".
-   Wide task descriptions are not nicely scrollable.
-   Inline documentation of `Clean HTML` is incomplete/wrong.
-   Cannot delete mapping rule target type anymore.
-   SPARQL Construct task does not update its execution report.

## eccenca Explore v24.3.0

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

We are excited to announce Explore v24.3, which introduces new features, improvements and bug fixes.

v24.3.0 of Explore adds the following new features:

-   …

v24.3.0 of Explore ships the following changes:

-   …

v24.3.0 of Explore ships the following fixes:

-   …

## eccenca Corporate Memory Control (cmemc) v24.2.0

This version of cmemc adds the following new features:

-   `graph validation execute` command
    -   `--inspect` option to return the list of violations instead of the summary (includes `--wait`)
-   `graph validation inpect` command
    -   retrieval and display of titles as terminal links for resources
    -   completion: retrieval and display of titles as descriptions
-   `graph validation list` command
    -   retrieval and display of titles as terminal links for graphs
-   `graph export` command
    -   option `--compress` to generate compressed ttl file
-   `graph import` command
    -   support import of compressed ttl/nt files
-   `admin store export` command
    -   `--replace` option to replace an existing file
    -   if no BACKUP_FILE is given, a default of `{{date}}-{{connection}}.store.zip` is used
-   `project import` command
    -   `--replace` option to replace an existing project
-   `project export` command
    -   `--replace` option to replace an existing file
-   `admin workspace export`
    -   `--replace` option to replace an existing file
-   `admin metrics` command group
    -   support for build / data integration metrics, e.g. `build:cmem_workspace_task_spec_size`
    -   support for GraphDB store metrics, e.g. `store:graphdb_slow_queries_count`
-   `admin metrics list` command
    -   documentation column to output table
    -   `--filter` option to filter metrics table by job, name, ID, or type
-   `admin acl` command group
    -   support for updated 24.3 access condition vocabulary and ACL graph
-   `admin migration` command group
    -   `admin migration list` command - List migration recipies
    -   `admin migration execute` command - Execute needed migration recipes
    -   The following migration recipes are available:
        -   `bootstrap-data` - Re-import bootstrap system data to match current version
        -   `workspace-configurations` - Forward-upgrade explore workspace configurations
        -   `acl-graph-24.3` - Move access conditions and used queries to new ACL graph
        -   `acl-vocab-24.3` - Migrate auth vocabulary terms (actions and other grants)
        -   `chart-widgets-24.3` - Migrate Chart Property Shapes to Widget Integrations
        -   `workflow-trigger-widgets-24.3` - Migrate Workflow Trigger Property Shapes to Widget Integrations

In addition to that, these changes and fixes are included:

-   cmemc will not fail anymore when the config dir is not creatable (message in debug)
-   cmemc will not fail anymore when the config ini is not readable (message in debug)
-   For these commands `admin acl list`, `dataset list`, `graph list`, `project list`, `admin user list`, `project variable list`, `vocabulary list`, `workflow list`, `admin workspace python list`, `admin workspace python list-plugins`, `dataset resource list`, `workflow scheduler list`, and `vocabulary cache list`:
    -   ommit empty tables with usage note message
-   `admin status` command
    -   component name change: DI -> BUILD
    -   component name change: DP -> EXPLORE
    -   component removal: DM (merged with DP into EXPLORE)
    -   key prefix change: dp -> explore
    -   key prefix change: di -> build
-   `project export` command
    -   `--filename-template` completion examples adaption
-   `dataset create` command
    -   Support compressed zip files for dataset types including CSV, XML, JSON, YAML, and plain text.
-   `admin metrics` command group
    -   metrics identification now as combined ID of `job_id:metrics_name`
-   `admin metrics` command group
    -   `--job` option, use `--filter job job_id` or combined metrics ID instead

## Migration Notes

!!! info

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v24.3.0 into DataIntegration v24.2.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v24.2.0 can be imported into DataIntegration v24.3.0.

### DataIntegration

-   CSV files are no longer deleted by default at the beginning of a workflow execution. This behavior can be changed in the CSV dataset configuration.
-   Access control changes. Action URIs have been renamed and new actions are introduced by default:
    -   `urn:eccenca:di` -> `<https://vocab.eccenca.com/auth/Action/Build>`
    -   `urn:elds-backend-all-actions` -> `<https://vocab.eccenca.com/auth/Action/AllActions>`
    -   Python plugin management endpoints are now secured via `<https://vocab.eccenca.com/auth/Action/Build-AdminPython>` action.
    -   Workspace admin functions (reload workspace, import workspace) are now secured via `<https://vocab.eccenca.com/auth/Action/Build-AdminWorkspace>` action.

### Explore

!!! info inline end "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

...

### cmemc

-   All scripts which used the `admin status` command with the `--key` option:
    -   adapt the key prefixes accordingly:
        -   old: `cmemc admin status --key dp.info.license.validDate`
        -   new: `cmemc admin status --key explore.info.license.validDate`
-   `admin store migrate` command deprecated
    -   use the `admin migration` command group instead
-   `--overwrite` options deprecated - will be removed with the next major version
    -   affected commands:
        -   `project import` command
        -   `project export` command
        -   `admin workspace export` command
-   All scripts which used the `admin metrics` command group:
    -   use combined metrics ID of `job_id:metrics_name`
    -   use `--filter job job_id` instead of `--job job_id`
