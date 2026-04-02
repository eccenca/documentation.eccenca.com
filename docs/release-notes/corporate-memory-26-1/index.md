---
status: new
tags:
    - ReleaseNote
---

# Corporate Memory 26.1.0

Corporate Memory 26.1 is the first major release in 2026. It expands AI-assisted mapping in Build, refreshes the resource experience in Explore, and strengthens access-condition and query-catalog administration in cmemc.

<!--
![26.1: Build - xxx](26-1-build-xxx.png "26.1: Build - ..."){ class="bordered" }

![26.1: Explore - xxx](26-1-explore-xxx.png "26.1: Explore - ..."){ class="bordered" }

![26.1: Explore - xxx](26-1-explore-xxx.png "26.1: Explore - ..."){ class="bordered" }
-->

The highlights of this release are:

-   Build: **Mapping Creator**
    -   Mapping Creator continues to mature with target schema extraction, richer context and profiling data for AI-assisted suggestions, finer-grained connection handling, and faster cleanup of suggested mappings.

-   Explore: **Badges, Resource Representation, and Resource Tables**
    -   Explore introduces badges, a redesigned resource representation and table experience, a new versioning tab, and broader usability improvements across shaped resource views and graph exploration.

-   Automate: **Access Conditions and Query Catalog Operations**
    -   cmemc expands administrative automation with richer access-condition import/export and filtering, new query catalog create/update/delete/explain commands, and more consistent list and delete workflows.

This release delivers the following component versions:

-   eccenca DataIntegration v26.1.0
-   eccenca Explore v26.1.0
-   eccenca Corporate Memory Control (cmemc) v26.1.0
-   eccenca Graph Insights v19.1.1-2

We tested this release with the following dependency components:

-   Ontotext GraphDB v11.3.0
-   Keycloak v26.5.3

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v26.1.0

We are excited to announce the release of DataIntegration v26.1, which expands Mapping Creator, improves dataset lifecycle management, and adds better visibility into deprecated plugins.

**v26.1.0 of DataIntegration adds the following new features:**

-   **Mapping Creator:**
    -   Added support for selecting individual connections in an n-to-1 property suggestion.
    -   Added a toggle in suggestion mode to remove non-suggested source elements.
    -   Added target schema extraction for Mapping Creator.
    -   Added easier ways to provide context to the Mapping Creator suggestion algorithm.
    -   Added profiling data to mapping suggestion prompts when configured.
    -   Added the configuration flag `com.eccenca.di.assistant.ApiConfig.useDataPlatformGateway`.
        -   When enabled, AI requests use the eccenca DataPlatform gateway instead of a manually configured OpenAI API.
    -   Added bulk deletion of target mappings in the transform task mapping editor, allowing multiple suggestions to be removed in one step with confirmation.
-   **Project-level access control:**
    -   Added project-level access control to restrict project visibility to specific user groups.
    -   It can be enabled via the `workspace.accessControl.enabled` configuration flag and is disabled by default.
    -   Access control groups can be configured per project.
    -   Projects without configured groups remain visible to all users.
    -   Users with the access control admin action (`Build-AdminWorkspace`) can see and manage all projects regardless of group membership.
    -   Added new API endpoints to manage project access control groups.
    -   Project and workspace export endpoints now provide an `exportUserData` parameter that can be used to strip sensitive information from exported data.
-   **Dataset management:**
    -   Added UI support and an API endpoint to clear a dataset without deleting the dataset itself.
        -   `DELETE /api/workspace/projects/:projectId/datasets/:datasetId/content`
    -   Added a **Clear dataset** operator that clears a dataset connected to its output port in a workflow.
    -   Added a **Clear output dataset** button in the transform and linking execution tabs to clear the output dataset manually before execution.
    -   Added a parameter to the Knowledge Graph dataset to allow streaming graph uploads.
-   **Deprecated plugin visibility:**
    -   Added a deprecated plugins page that shows all usages of deprecated plugins across the workspace.
    -   Added a deprecated plugins widget that shows deprecated plugin usage on project and item pages.
-   **Python plugin API:**
    -   Added `cmem_base_uri`, `dp_api_endpoint`, and `di_api_endpoint` to `SystemContext`.
    -   Added `refresh_token` to `UserContext`.
-   **Other additions:**
    -   Added a Zip transformer that concatenates the values of two inputs pairwise.
    -   Enabled line wrapping in the code editor component when used in Markdown mode with the toolbar.
    -   Added a tooltip with the full IRI for Knowledge Graph operators in the workflow sidebar.

**v26.1.0 of DataIntegration introduces the following changes:**

-   Marked the dataset parameter **Clear before execution** as deprecated for all datasets, moved it to the advanced section, and changed the default to `false`.
-   Nested transform tasks now work with a single input table if the input can be rewound; this includes the SPARQL Select query task.
-   Tasks that fail to load, for example because a required plugin is missing, can now be removed in the UI.
-   Graph parameter autocompletion now shows exact matches by label or URI at the top of the result list.
-   The Knowledge Graph dataset now opens the **Query editor** in a new tab.
-   Workflow editor sidebar search now moves matching tags to the front.
-   The Project Variables widget now shows a warning when template variables cannot be evaluated.

**v26.1.0 of DataIntegration ships the following fixes:**

-   **Vocabulary:**
    -   The vocabulary cache no longer fails completely when an invalid vocabulary URI has been entered, and it now warns when a non-installed vocabulary exists in the list.
    -   Improved vocabulary loader performance by avoiding cartesian products; queries and processing now scale linearly with the number of triples in the vocabulary.
-   Fixed ghost connections that could appear in Mapping Creator when opened from the workflow page.
-   The **Distinct by** operator now deletes its cache file if an exception is thrown.
-   Fixed status updates for the pivot/unpivot operator.
-   Fixed invalid serialization of restrictions that prevented generated matching link specifications from being updated.
-   Fixed importing transform rules XML containing non-self-closing `<Input>` elements.
-   Transform execution now validates whether the received number of inputs matches the expected number.
-   Fixed invalid connections that could be drawn from newly added workflow nodes, for example from a data port to a dependency port.
-   Fixed an issue where opening and closing a node handle's port schema caused a subsequent drag from that port to create a connection.
-   Improved the **Clone task** dialog title to indicate shallow clone semantics and added an info box explaining that referenced tasks are not duplicated.
-   Correctly forwarded the user context to the peak examples endpoint.
-   The template switch button is no longer shown for template parameters.
-   Improved focus indication for keyboard navigation.
-   Fixed the `newlySelected` property of `MultiSelect` for `onSelection`.
-   Fixed cases where DI entity caches were not cleaned up.
-   Fixed cases where errors persisted after deleting the task from the project.

## eccenca Explore v26.1.0

We are pleased to announce the release of Explore v26.1, which introduces badges, a redesigned resource representation and table experience, versioning view, Companion improvements, and a broad platform refresh.

**v26.1.0 of Explore adds the following new features:**

-   **Explore:**
    -   Added extended resource actions such as copying IRIs and creating queries.
    -   Added a versioning tab.
-   **Companion:**
    -   Added initialization of Business Knowledge Editor visualizations.
    -   Added controls to limit which tools are used by the persistent Companion LLM.
    -   Made streamable MCP the default.
    -   Added support for deleting conversations.
    -   Added an OpenAI proxy endpoint for access via DataIntegration.
    -   Added a dedicated action for Companion usage.
-   **SHACL:**
    -   Resource bubbles can now link into different workspaces.
    -   Added `AskIfEditable` node shape queries.
    -   Added print support for shaped resource views.
    -   Added user-defined column widths to table reports.
    -   Added shapes, images, and ontology terms as sources for the Favorite Graph List.
-   **Query Catalog:**
    -   Added support for predefined query placeholders.
-   **Badges:**
    -   Introduced badges to the user interface.
-   **Other:**
    -   Added support for parallel GSP statement import when using GraphDB.
        -   `store.graphdb.useStatementParallelGspWrite` (default: `false`)
    -   Added an endpoint for SPARQL query plans, depending on the backend.
        -   Currently only supported with GraphDB.
        -   Changed the response of the existing defunct route `/dataplatform/api/querycatalog/logicalPlan`.
    -   Added support for stable pretty-printed Turtle export.
        -   Available via GSP GET requests with the accept header `text/turtle+pretty`.
        -   The `proxy.gspPrettyTurtlePrintSizeLimit` parameter controls the size limit.

**v26.1.0 of Explore introduces the following changes:**

-   **Explore:**
    -   Graph lists now use scrolling instead of pagination.
    -   Resource tables are now grouped into logical groups. Additional filters for bound/unbound and inclusive/exclusive value checks have been added, and string equality is now relaxed.
    -   SPARQL Excel downloads now use a frozen first row.
    -   Resource Table search can now be forced for queries shorter than 3 characters.
    -   Deletions and changes in the Turtle table are now recorded in the versioning graph.
-   **Business Knowledge Editor (BKE):**
    -   Business Knowledge Editor visualizations can now be saved in a user-chosen graph.
-   **SHACL:**
    -   Removed the workflow trigger ID.
    -   Overhauled SHACL validation messages.
    -   Table reports can now be downloaded.
-   **Resource display and table:**
    -   Completely overhauled resource representation, resource tables, and filters.
    -   Middle-clicking a resource link now opens the resource in a new tab.
    -   Added copy-IRI-to-clipboard functionality.
-   **Companion:**
    -   Companion now uses WebSockets for the client-server connection.
-   **Other:**
    -   The Node.js version is now 24.
    -   Explore now shows the default fallback depiction if the shape catalog is not readable.
    -   Charts now use the recent multi-select component.
    -   Improved workspace configuration versioning.
        -   A workspace configuration migration is required for existing workspaces.
    -   Improved access control enforcement for resource deletion.
        -   Resource delete and write permissions are now enforced more consistently.
    -   Upgraded to Spring Boot 4.
    -   Upgraded to Apache Jena 6.
    -   Added support for GraphDB 11.3.

**v26.1.0 of Explore ships the following fixes:**

-   **Explore:**
    -   Fixed the display of the **Remove resource** button in conditions.
    -   Fixed a SPARQL offset bug when viewing the resource table.
-   **SHACL:**
    -   Displayed violations for omitted fields.
    -   Added a link to the newly created resource in the success message after resource creation.
    -   Resolved target classes of resources across all readable graphs when no context graph is given, which also fixes depiction resolution in that case.
    -   Added an option in workspace configuration to fully validate a resource in edit modes.
    -   Property shapes with `maxCount: 1` and `readOnly: true` now display correctly.
    -   Text fields now allow emojis.
    -   Fixed mixing of statement annotations and versioning statements.
    -   Workflow Button and Workflow Trigger are now safeguarded when the user does not have permission to use BUILD.
-   **Business Knowledge Editor (BKE):**
    -   Improved loading time for the visualization catalog.
    -   Fixed an error when opening the connected resources panel for a node with an invalid `valueQuery` on a property shape.
    -   Fixed various display issues in BKE.
    -   Fixed a blocker error when saving after creating a new visualization.
    -   Improved wrapping of long labels.
-   **Query Catalog:**
    -   Fixed execution of SPARQL UPDATE queries when placeholders are used in the prefix list.
-   **Other:**
    -   Improved visibility of ongoing Graph Insights status.
    -   Metadata errors in access conditions no longer prevent Explore from starting.
        -   Invalid access conditions can be monitored via the metric `explore:application_access_conditions_invalid_count`.
    -   SPARQL Excel downloads now have clean file names.
    -   Notifications are now more robust when given non-string input.

## eccenca Corporate Memory Control (cmemc) v26.1.0

We are excited to announce the release of cmemc v26.1, which expands access-condition administration, adds richer project and query catalog operations, and improves list and output consistency across the CLI.

**v26.1.0 of cmemc adds the following new features:**

-   `admin workspace thread-dump` command
    -   Added a command to request a thread dump for all live threads of the Build/DataIntegration component.
-   `admin acl list` command
    -   Added a new `--filter` option with the following filters:
        -   `name` to filter by access condition name
        -   `user` to filter by required user account
        -   `group` to filter by required group membership
        -   `read-graph` to filter by readable graph
        -   `write-graph` to filter by writable graph
-   `admin acl delete` command
    -   Added a new `--filter` option with the same filters as the list command.
-   `admin acl export` command
    -   Added a command to export access conditions to a JSON file.
    -   Added a `--filter` option with the same filters as the list command.
    -   Added the `--output-file`, `--output-dir`, and `--filename-template` options to control file structure.
    -   Added a `--replace` option to replace existing files.
-   `admin acl import` command
    -   Added a command to import access conditions from a JSON file.
    -   Added a `--filter` option with the same filters as the list command.
    -   Added a `--replace` option to replace existing access conditions with the same IRI.
-   Object list infrastructure
    -   Added the `DirectMultiValuePropertyFilter` class for multi-value filtering with delimiter support.
    -   Added support for hidden filters, which are excluded from help text and shell completion.
-   `config list` command
    -   Added table output with **Connection**, **Base URI**, and **Grant Type**.
    -   Added the `--id-only` option to return only connection names.
    -   Added a `--filter` option with regex filtering for connection names.
-   `project list` command
    -   Added a new `--filter` option with the following filters:
        -   `id` to filter by project ID (name)
        -   `regex` to filter by project name, label, or description
        -   `tag` to filter by tag label
-   `project delete` command
    -   Added a new `--filter` option with the same filters as the list command.
-   `project file delete` command
    -   Added a new `--filter` option with the following filters:
        -   `project` to filter by project ID
        -   `regex` to filter by resource name
    -   Added the `-a, --all` option to delete all file resources.
-   `project variable delete` command
    -   Added a new `--filter` option with the following filters:
        -   `project` to filter by project ID
        -   `regex` to filter by variable ID, value, description, or template
    -   Added the `-a, --all` option to delete all variables.
-   Project import/export with Access Conditions
    -   Added the `--include-access-conditions` flag to `project export` and `project import` to bundle access control data with project archives.
-   `graph delete` command
    -   Added a new `--filter` option with the `imported-by` filter to select graphs imported by the specified graph IRI.
-   `query list` command
    -   Added a new `--filter` option with the following filters:
        -   `id` to filter by query URI pattern (regex match on `short_url`)
        -   `type` to filter by query type (`SELECT`, `CONSTRUCT`, `ASK`, `DESCRIBE`, `UPDATE`)
        -   `placeholder` to filter by queries containing specific placeholder keys
        -   `regex` to filter by regex matches in query text or label
-   Workspace import/export with Access Conditions
    -   Added the `--include-access-conditions` flag to `admin workspace export` and `admin workspace import` to bundle access control data with project archives.
-   `query explain` command
    -   Added a command to show the query optimization plan for a SPARQL query.
    -   The command accepts a file path or a catalog query URI.
    -   Added the `--catalog-graph` option to select the query catalog graph.
-   `query create` command
    -   Added a command to create a query in the catalog from a SPARQL file.
    -   Added the `--id` option to set the query URI, or auto-generate it from the filename.
    -   Added the `--label` and `--description` options.
    -   Added the `--catalog-graph` option to select the query catalog graph.
-   `query update` command
    -   Added a command to update an existing query in the catalog.
    -   Added the `--query-file`, `--label`, and `--description` options.
    -   Added the `--catalog-graph` option to select the query catalog graph.
-   `query delete` command
    -   Added a command to delete one or more queries from the catalog.
    -   Added the `-a, --all` option to delete all queries.
    -   Added a `--filter` option with the same filters as the list command.
    -   Added the `--catalog-graph` option to select the query catalog graph.
-   Object list infrastructure
    -   Added the `MultiFieldPropertyFilter` class for searching across multiple object fields.
-   cmem-client logging
    -   Added a new `ClickHandler` class for logging output that matches cmemc logging.
    -   Added the `CMEMC_LOG_LEVEL` configuration variable for setting the log level (default: `DEBUG`).

**v26.1.0 of cmemc ships the following fixes:**

-   SSL CA bundle forwarding when custom certificates are used
    -   `REQUESTS_CA_BUNDLE` is now passed as the CA bundle path to `httpx` via `config.verify`.
    -   Fixed parsing of `SSL_VERIFY=false`, where any string value was previously treated as `True`.
-   Shell completion on msys2/Windows
    -   Removed the custom zsh completion script in favor of Click's built-in completion.
    -   Users on msys2/Windows should use `eval "$(_CMEMC_COMPLETE=zsh_source cmemc | tr -d '\r')"` instead.
-   `graph export` command
    -   Fixed MIME type extension handling for RDF formats on Windows systems where `mimetypes.guess_extension()` can return `None`.
-   Project import from a directory
    -   Fixed a regression caused by the addition of Access Conditions to the command group.

**v26.1.0 of cmemc introduces the following changes:**

-   Delete command normalization
    -   `dataset delete`, `admin user delete`, `admin acl delete`, `project delete`, `graph delete`, `graph insights delete`, and `project variable delete` now accept multiple IDs.
    -   Added a zero-padded counter format (`01/10` instead of `1/10`).
    -   Changed the success message from `done` to `deleted`.
    -   Added upfront validation to prevent mixing IDs with `--all` or `--filter`.
    -   Added deduplication to prevent deleting the same item twice.
-   Shell completion descriptions now use the full terminal width
    -   Command group descriptions in shell completion now adapt to terminal width instead of being truncated at 45 characters.
    -   This improves readability in modern wide terminals.
-   Error handling improvements
    -   Replaced `ClickException` with `CmemcError` throughout the codebase for consistent error handling.
    -   `CmemcError` now auto-retrieves the Click context, removing the need for explicit context passing.
    -   Simplified error handling by removing redundant context parameters from error calls.
    -   Added the `suppress_completion_errors` decorator to handle connection errors in shell completion functions.
-   Object list infrastructure refactoring
    -   Enhanced `DirectListPropertyFilter` with a transform option for flexible list transformations.
    -   Added the `transform_list_none` function as the default no-op transform for list filters.
    -   Added the `transform_extract_labels` function to extract labels from lists of dictionaries.
    -   Improved consistency between the `DirectValuePropertyFilter` and `DirectListPropertyFilter` APIs.
-   Improved table output for list commands
    -   Added consistent captions to all list command tables showing count, item type, and instance.
    -   Replaced the `timeago` library with `humanize` for better time formatting.
    -   Enhanced empty table messages to distinguish between filtered and unfiltered results.
    -   Affected commands: `acl list`, `admin client list`, `admin user list`, `dataset list`, `graph list`, `graph imports list`, `graph insights list`, `admin metrics list`, `admin migration list`, `project list`, `project variable list`, `admin workspace python list`, `admin workspace python list-plugins`, `query list`, `query status`, `workflow scheduler list`, `graph validation list`, `vocabulary list`, `vocabulary cache list`, and `workflow list`.
-   `dataset list` and `dataset delete` commands
    -   Refactored to use ObjectList infrastructure for consistent filtering.
    -   Dataset types are now displayed as clickable documentation links.
    -   The type column now shows human-readable titles, such as `JSON`, `CSV`, and `Excel`, instead of raw plugin IDs.
    -   Links now point directly to the official eccenca Corporate Memory dataset documentation.
    -   Dataset IDs are now displayed as clickable workspace links.
-   `graph list` command
    -   Graph labels are now displayed as clickable links to the graph in the web interface.
    -   Refactored to use ObjectList infrastructure for consistent filtering.
-   `project list` command
    -   Project labels are now displayed as clickable links to the project in the web interface.
    -   Added a **Modified** timestamp column with humanized time display.
    -   The table minimum width now matches the caption length for better formatting.
-   `project variable delete` command
    -   Refactored to use ObjectList infrastructure for consistent filtering.
-   `query list` command
    -   Query labels are now displayed as clickable links to the query editor in the web interface.
-   `query` command group
    -   `--catalog-graph` completion now only suggests graphs that contain queries.
    -   Dependent placeholder value completion now resolves using already-provided `-p` values.
    -   Placeholder key completion now shows labels and dependency hints when a value query requires another placeholder.
-   `workflow list` command
    -   Workflow labels are now displayed as clickable links to the workflow editor in the web interface.
-   `config list` command
    -   Default output changed from a simple list to table format.
    -   Use `--id-only` to get the simple connection name list for piping.
    -   Previously deprecated commands and groups were removed; see migration notes.

## Migration Notes

!!! info "Backward and Forward Compatibility"

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v26.1.0 into DataIntegration v25.3.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v25.3.0 can be imported into DataIntegration v26.1.0.

!!! info "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

### eccenca DataIntegration

-   The dataset parameter **Clear before execution** is now deprecated, moved to the advanced section, and defaults to `false`.
    Review workflows or templates that relied on the previous default behavior.

!!! warning "Breaking Change Pre-Announcement"

    Changes to DataIntegration container configuration mount points will be rolled out with the next release, v26.2.
    We are harmonizing configuration paths under a single central entry point to simplify configuration.

    Details will be provided as part of the `helm` and `docker-compose` deployment templates.
Please read the migration notes carefully.


### eccenca Explore

-   Custom navigation queries need to be adjusted manually.
-   Existing workspaces require a workspace configuration migration to introduce the new workspace configuration versioning description field.

### cmemc

**v26.1.0 of cmemc removes the following deprecated functionality:**

-   `dataset resource` command group
    -   Deprecated in v25.6.0. Use the `project file` command group instead.
-   `graph tree` command
    -   Deprecated in v25.2.0. Use the `graph imports tree` command instead.
-   `admin store migrate` command
    -   Deprecated in v25.0.0. Use the `admin migration` command group instead.
-   `--overwrite` options
    -   Deprecated in v25.0.0. Use the `--replace` option instead.
    -   Affected commands: `admin store export`, `project import`, `project export`, `admin workspace export`
-   Removed deprecated auto-completion URIs.
-   `dataset delete` command
    -   The `--project` option was removed. Use `--filter project XXX` instead.
-   Removed the `project create --from-transformation` option.
