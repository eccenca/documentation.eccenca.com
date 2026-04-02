---
status: new
tags:
    - ReleaseNote
---

# Corporate Memory 26.1.0

Corporate Memory 26.1 is the first major release in 2026.

<!--
![26.1: Build - xxx](26-1-build-xxx.png "26.1: Build - ..."){ class="bordered" }

![26.1: Explore - xxx](26-1-explore-xxx.png "26.1: Explore - ..."){ class="bordered" }

![26.1: Explore - xxx](26-1-explore-xxx.png "26.1: Explore - ..."){ class="bordered" }
-->

The highlights of this release are:

-   Build: **Mapping Creator**
    -   ...

-   Explore: **Badges, Resource Representation and Resource Table**
    -   ...

-   Automate:
    -   ...

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

We are excited to announce DataIntegration v26.1, which introduces new features, improvements and bug fixes.

**v26.1.0 of DataIntegration adds the following new features:**

- New Mapping Creator features:
    - Support selecting individual connections in a n-to-1 property suggestion (CMEM-7233).
    - Add switch to Mapping Creator suggestion mode to remove the non-suggested source elements (CMEM-7201).
    - Target schema extraction for the Mapping Creator (CMEM-7161).
    - Support to easily add context to the Mapping Creator suggestion algorithm (CMEM-7150).
    - Add profiling data to mapping suggestion prompts (needs to be configured) (CMEM-6531).
    - New configuration flag `com.eccenca.di.assistant.ApiConfig.useDataPlatformGateway` (CMEM-7086).
        - If true, will use the eccenca DataPlatform gateway for AI requests instead of the manually configured OpenAI API.
    - Bulk delete of target mappings in the transform task mapping editor: select multiple suggestions via checkboxes and delete them in one step with a confirmation dialog. (CMEM-7232)
- Project-level access control: restrict project visibility to specific user groups (CMEM-7264).
    - Can be enabled via the `workspace.accessControl.enabled` configuration flag (disabled by default).
    - Access control groups can be configured per project.
    - Projects without configured groups remain visible to all users.
    - Users with the access control admin action (`Build-AdminWorkspace`) can see and manage all projects regardless of group membership.
    - New API endpoints to manage project access control groups.
    - Project and workspace export endpoints have a new `exportUserData` parameter that can be used to strip sensitive information from the exported data (CMEM-7544).
- Dataset management:
    - UI and API endpoint to clear a dataset without deleting the dataset itself. (CMEM-4052)
        - DELETE /api/workspace/projects/:projectId/datasets/:datasetId/content
    - 'Clear dataset' operator that clears a dataset that is connected to its output port in a workflow. (CMEM-3961)
    - Clear output dataset button in transform and linking execution tab in order to clear the output dataset manually before execution. (CMEM-3961)
    - New parameter to Knowledge Graph dataset to allow for streaming graph uploads (CMEM-7012).
- Deprecated plugin visibility:
    - Deprecated plugins page: shows all usages of deprecated plugins in the whole workspace. (CMEM-7133)
    - Deprecated plugins widget: shows deprecated plugin usages on project and item pages. (CMEM-7138)
- Additions to Python plugin API:
    - Added `cmem_base_uri`, `dp_api_endpoint`, and `di_api_endpoint` to `SystemContext`.
    - Added `refresh_token` to `UserContext`.
- Other additions:
    - Zip transformer that concatenates the values of two inputs in pairs (CMEM-7030).
    - Allow wrap in the code editor component when it is using Markdown mode and toolbar (CMEM-6891).
    - Workflow sidebar: add tooltip for full IRI of KG operator (CMEM-7098).

**v26.1.0 of DataIntegration introduces the following changes:**

- Mark dataset parameter 'Clear before execution' in all datasets as deprecated, put into advanced section and set default to false. (CMEM-3961)
- Nested transform tasks now work with a single input table, if the input can be rewinded. Amongst others, this is supported by the SPARQL Select query task (CMEM-7493).
- Tasks that failed to be loaded (e.g., because a required plugin is missing) can be removed in the UI now (CMEM-7182).
- Graph parameter auto-completion now shows exact matches (by label or URI) at the top of the result list. (CMEM-6977)
- Open 'Query editor' of Knowledge Graph dataset in new tab. (CMEM-6966)
- In workflow editor sidebar search, order matching tags to the front. (CMEM-7556)
- Project Variables widget now shows a warning when template variables could not be evaluated (CMEM-6240).

**v26.1.0 of DataIntegration ships the following fixes:**

- Vocabulary:
    - Vocabulary cache should not fail completely when an invalid vocabulary URI has been entered; also warns the user when a non-installed vocabulary exists in the list. (CMEM-7170)
    - Vocabulary loader can have very bad performance: avoid cartesian product; queries and processing now run linear to the number of triples in the vocabulary. (CMEM-7270)
- Mapping Creator: Ghost connections appearing (only via workflow page). (CMEM-7454)
- "Distinct by" operator: Delete the cache file if an exception is thrown.
- Fix status update for pivot/unpivot operator. (CMEM-7404)
- Generated matching link spec cannot be updated because of invalid serialization of restriction. (CMEM-7134)
- Fixed importing transform rules XML containing non-self-closing `<Input>` elements (CMEM-7095).
- The transform execution should validate if the received number of inputs matches the expected one (CMEM-7493).
- From newly added workflow nodes it is possible to draw invalid connections, e.g. from data to dependency port. (CMEM-7416)
- Opening and closing the port schema of a node handle drags a connection from that port afterwards. (CMEM-7247)
- Clone task dialog: improved title to indicate shallow clone semantics and added info box explaining that referenced tasks are not duplicated (CMEM-7355).
- Correctly forward the user context to the peak examples endpoint (CMEM-7439).
- Do not show the template switch button for template parameters. (CMEM-7147)
- Fix insufficient focus indication for keyboard navigation (CMEM-7512).
- MultiSelect newlySelected property for onSelection is not correct (CMEM-7479).
- DI entities caches not cleaned up.
- Errors persist even after deleting the task from the project (CMEM-7178).

**v26.1.0 of DataIntegration removes the following functionality:**

## eccenca Explore v26.1.0

We are pleased to announce Explore v26.1, which introduces new features, improvements and bug fixes.

**v26.1.0 of Explore adds the following new features:**

- **Explore**
    - added extended resource options like copy iri, create query (CMEM-6207)
    - Versioning tab implementation (CMEM-6445)
- **Companion**
    - BKE Integration: Viz Initialization (CMEM-6864)
    - Limit tools which are used by Companion LLM (Persistence) (CMEM-7087)
    - Add MCP streamable as default (CMEM-6953)
    - Add functionality of deleting conversations (CMEM-7181)
    - Add OpenAI proxy endpoint for access via DI (CMEM-7086)
    - Add action for companion usage (CMEM-7085)
- **Shacl**
    - Allow resource bubble to link into different workspaces (CMEM-6604)
    - AskIfEditable node shape query (CMEM-6737)
    - Add printability for shaped resource views (CMEM-6985)
    - Add user-defined column widths to table reports (CMEM-6393)
    - Add shapes, images, ontology terms to provide Favorite Graph List (CMEM-7208)
- **Query Catalog**
    - Add support for pre-defined query placeholders (CMEM-7144)
- **Badges**
    - Introduction of badges to the user interface (CMEM-7042)
- **Other**
    - Add support for parallel GSP statement import when using GraphDB (CMEM-7038)
        - `store.graphdb.useStatementParallelGspWrite` (default: false)
    - Add endpoint for SPARQL query plan (depending on backend) (CMEM-7278)
        - only works in GraphDB
        - changed response of existing defunct route: `/dataplatform/api/querycatalog/logicalPlan`
    - Add support for stable pretty print turtle export (CMEM-7325)
        - GSP get request with accept header `text/turtle+pretty`
        - Parameter `proxy.gspPrettyTurtlePrintSizeLimit` for controlling size limit

**v26.1.0 of Explore introduces the following changes:**

- **Explore**
    - Graph Lists now use scrolling instead of pagination  (CMEM-7216)
    - Resource Table are now grouped into logic groups. Additional filters for Bound/NotBount and Inclusive and Exclusive Value checks are added. string equality is now relaxed.  (CMEM-7257)
    - SPARQL excel downloads have fixed first row (CMEM-7360)
    - Added forced search for the search query less than 3 characters in the Resource Table (CMEM-7293)
    - Deletion and Changes in turtle table are recorded in versioning graph (CMEM-7310)
- **Busines Knowledge Editor**
    - Busines Knowledge Editor visualizations can be saved in a user chosen graph (CMEM-7279)
- **Shacl**
    - Removal of workflow trigger id (CMEM-7235)
    - Overhaul of SHACL valdiation messages (CMEM-7312)
    - Allow download of data in table report (CMEM-7545)
- **Resource Display and Table**
    - Complete overhaul of resource representation, resource table and filter (CMEM-7176, CMEM-7211)
    - Middle click on resource link opens new tab with resource (CMEM-7322)
    - Copy IRI to clipboard functionality (CMEM-6996)
- **Companion**
    - Changed client/server connection of companion to websockets (CMEM-6776)
- **Other**
    - Node version is now 24 (CMEM-7141)
    - Show the default fallback depiction if the shape catalogue is not readable (CMEM-6972)
    - Charts switched to recent multi-select (CMEM-6983)
    - Workspace configuration versioning improved (CMEM-6237)
        - workspace configuration migration necessary for existing workspaces
    - Improved access control enforcement for resource deletion (CMEM-7110, CMEM-7073)
        - Strengthened consistency between resource delete and write permissions to ensure access rules are applied uniformly
    - Spring Boot 4 (CMEM-6693)
    - Apache Jena 6 (CMEM-7469)
    - GraphDB 11.3 (CMEM-7517)

**v26.1.0 of Explore ships the following fixes:**

- **Explore**
    - Fix the display of the "Remove resource" button in conditions (CMEM-7470)
    - Fix bug in SPARQL offset when viewing resource table (CMEM-6998)
- **Shacl**
    - Display violations for omitted fields (CMEM-6493)
    - Resource successfully created info message: add a link to the new resource (CMEM-6986)
    - Resolve target classes of resources over all readable graphs if no context graph is given (CMEM-7281)
      - fixes issue when resolving depictions without given context graph
    - Added option in workspace configuration to fully validate a resource in edit modes (CMEM-6314)
    - Display property shapes with `maxCount: 1` and `readOnly: true` properly (CMEM-7403)
    - Allow using emojis in text fields (CMEM-7217)
    - Fix mixing of statement annotations and versioning statements (CMEM-6582)
    - Workflow Button & Workflow Trigger safeguarded in case the user has no permission to use BUILD (CMEM-7234).
- **Busines Knowledge Editor**
    - Visualization catalogue takes too long to load (CMEM-7255)
    - Fix error when opening connected resources panel for a node with an invalid valueQuery on a property shape (CMEM-7309)
    - BKE display issues (CMEM-7184)
    - Fixed blocker error when saving after creating a new viz (CMEM-7262)
    - Wrapping of long labels (CMEM-7375)
- Query Catalog
    - Can't execute SPARQL update query when using placeholder in prefix list (CMEM-7456, CMEM-7274)
- Other
    - Add shapes, images, ontology terms to provide Favorite Graph List (CMEM-7208)
    - Graph Insights: Ongoing status visibility fix (CMEM-7245)
    - Metadata error on access condition does not break start of explore (CMEM-6962)
        - invalid access conditions can be monitored via metric `explore:application_access_conditions_invalid_count`
    - SPARQL excel downloads have clean file names. (CMEM-7359)
    - Notifications more robust with non-string input (CMEM-7388)

## eccenca Corporate Memory Control (cmemc) v26.1.0

We are excited to announce cmemc v26.1.0, which introduces new features, improvements and bug fixes.

**v26.1.0 of cmemc adds the following new features:**

- `admin workspace thread-dump` command
    - new command to request a thread dump for all live threads of the build / dataintegration component
- `admin acl list` command
    - new `--filter` option with the following concrete filters:
        - `name` - filter by access condition name
        - `user` - filter by required user account
        - `group` - filter by required group membership
        - `read-graph` - filter by readable graph
        - `write-graph` - filter by writable graph
- `admin acl delete` command
    - new `--filter` option with the same filters as the list command
- `admin acl export` command
    - new command to export access conditions to a JSON file
    - `--filter` option with the same filters as the list command
    - `--output-file`. `--output-dir` and `--filename-template` option to control file structure
    - `--replace` option to replace existing files
- `admin acl import` command
    - new command to import access conditions from a JSON file
    - `--filter` option with the same filters as the list command
    - `--replace` option to replace existing access conditions with same IRI
- object list infrastructure
    - new `DirectMultiValuePropertyFilter` class for multi-value filtering with delimiter support
    - support for hidden filters (excluded from help text and shell completion)
- `config list` command
    - added table output with Connection, Base URI, and Grant Type
    - `--id-only` option: get only connection names
    - `--filter` option with regex filter for connection names
- `project list` command
    - new `--filter` option with the following concrete filters:
        - `id` - filter by project ID (name)
        - `regex` - filter by regex matching project name, label, or description
        - `tag` - filter by tag label
- `project delete` command
    - new `--filter` option with the same filters as the list command
- `project file delete` command
    - new `--filter` option with the following concrete filters:
        - `project` - filter by project ID
        - `regex` - filter by regex matching resource name
    - new `-a, --all` option to delete all file resources
- `project variable delete` command
    - new `--filter` option with the following concrete filters:
        - `project` - filter by project ID
        - `regex` - filter by regex matching variable id, value, description, or template
    - new `-a, --all` option to delete all variables
- `project import/export` with Access Conditions
    - `--include-access-conditions` flag to `project export` and `project import` to bundle access control
    data with project archives
- `graph delete` command
    - new `--filter` option with the following concrete filter:
        - `imported-by` - filter by graphs imported by the specified graph IRI
- `query list` command
    - new `--filter` option with the following concrete filters:
        - `id` - filter by query URI pattern (regex match on short_url)
        - `type` - filter by query type (SELECT, CONSTRUCT, ASK, DESCRIBE, UPDATE)
        - `placeholder` - filter by queries containing specific placeholder keys
        - `regex` - filter by regex pattern in query text or label
- `workspace import/export` with Access Conditions
    - `--include-access-conditions` flag to `admin workspace export` and `admin workspace import` to bundle access control data with project archives
- `query explain` command
    - new command to show the query optimization plan for a SPARQL query
    - accepts a file path or a catalog query URI
    - new `--catalog-graph` option to select the query catalog graph
- `query create` command
    - new command to create a new query in the catalog from a SPARQL file
    - new `--id` option to set the query URI (auto-generated from filename if not provided)
    - new `--label` and `--description` options
    - new `--catalog-graph` option to select the query catalog graph
- `query update` command
    - new command to update an existing query in the catalog
    - new `--query-file`, `--label`, and `--description` options
    - new `--catalog-graph` option to select the query catalog graph
- `query delete` command
    - new command to delete one or more queries from the catalog
    - new `-a, --all` option to delete all queries
    - new `--filter` option with the same filters as the list command
    - new `--catalog-graph` option to select the query catalog graph
- object list infrastructure
    - new `MultiFieldPropertyFilter` class for searching across multiple object fields
- cmem-client logging
    - new `ClickHandler` class for custom logging output to look the same as cmemc logging
    - `CMEMC_LOG_LEVEL` config variable for setting log level (default: `DEBUG`)

**v26.1.0 of cmemc ships the following fixes:**

- SSL CA bundle not forwarded to httpx when using custom certificates
    - `REQUESTS_CA_BUNDLE` is now passed as the CA bundle path to httpx via `config.verify`
    - Fixed `SSL_VERIFY=false` parsing bug where any string value was treated as `True`
- Shell completion on msys2/Windows
    - Removed custom zsh completion script in favour of Click's built-in completion
    - Users on msys2/Windows should use: `eval "$(_CMEMC_COMPLETE=zsh_source cmemc | tr -d '\r')"`
- `graph export` command
    - Fixed MIME type extension handling for RDF formats on Windows systems where `mimetypes.guess_extension()` can return None
- Project import from a directory
    - This was caused by the addition of Access Conditions to the command group

**v26.1.0 of cmemc introduces the following changes:**

- Delete commands normalization
    - `dataset delete`, `admin user delete`, `admin acl delete`, `project delete`, `graph delete`, `graph insights delete`, `project variable delete` now accept multiple IDs
    - Added zero-padded counter format (01/10 instead of 1/10)
    - Changed success message from "done" to "deleted"
    - Added upfront validation to prevent mixing IDs with --all/--filter options
    - Added deduplication to prevent deleting same item twice
- Shell completion descriptions now use full terminal width
    - Command group descriptions in shell completions adapt to terminal width instead of being truncated at 45 characters
    - Improves user experience by showing complete command descriptions in modern wide terminals
- Error handling improvements
    - Replaced `ClickException` with `CmemcError` throughout codebase for consistent error handling
    - Made `CmemcError` auto-retrieve click context, removing need for explicit context passing
    - Simplified error handling by removing redundant context parameters from all error calls
    - Added `suppress_completion_errors` decorator to handle connection errors in shell completion functions
- Object list infrastructure refactoring
    - Enhanced `DirectListPropertyFilter` with transform option for flexible list transformations
    - Added `transform_list_none` function as default no-op transform for list filters
    - Added `transform_extract_labels` function to extract labels from list of dictionaries
    - Improved consistency between `DirectValuePropertyFilter` and `DirectListPropertyFilter` APIs
- Improved table output for list commands
    - Added consistent captions to all list command tables showing count, item type, and instance
    - Replaced `timeago` library with `humanize` for better time formatting
    - Enhanced empty table messages to distinguish between filtered and unfiltered results
    - Affected commands: `acl list`, `admin client list`, `admin user list`, `dataset list`,
      `graph list`, `graph imports list`, `graph insights list`, `admin metrics list`,
      `admin migration list`, `project list`, `project variable list`, `admin workspace python list`,
      `admin workspace python list-plugins`, `query list`, `query status`, `workflow scheduler list`,
      `graph validation list`, `vocabulary list`, `vocabulary cache list`, `workflow list`
- `dataset list` and `dataset delete` commands
    - Refactored to use ObjectList infrastructure for consistent filtering
    - Dataset types are now displayed as clickable documentation links
    - Type column shows human-readable titles (e.g., "JSON", "CSV", "Excel") instead of raw plugin IDs
    - Links direct to official eccenca Corporate Memory dataset documentation
    - Dataset IDs are now displayed as clickable workspace links
- `graph list` command
    - Graph labels now displayed as clickable links to the graph in the web interface
    - Refactored to use ObjectList infrastructure for consistent filtering
- `project list` command
    - Project labels now displayed as clickable links to the project in the web interface
    - Added "Modified" timestamp column with humanized time display
    - Table minimum width now set to match caption length for better formatting
- `project variable delete` command
    - Refactored to use ObjectList infrastructure for consistent filtering
- `query list` command
    - Query labels now displayed as clickable links to the query editor in the web interface
- `query` command group
    - `--catalog-graph` completion now only suggests graphs that contain queries
    - dependent placeholder value completion now resolves using already-provided `-p` values
    - placeholder key completion shows labels and dependency hints when a value query requires another placeholder
- `workflow list` command
    - Workflow labels now displayed as clickable links to the workflow editor in the web interface
- `config list` command
    - default output changed from simple list to table format
    - use `--id-only` to get the simple connection name list for piping
    - removal of previously deprecated commands / groups - see migration notes

## Migration Notes

TODO

!!! info "Backward and Forward Compatibility"

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v25.2.0 into DataIntegration v25.1.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v24.3.0 can be imported into DataIntegration v25.1.0.

!!! info "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

### eccenca DataIntegration

!!! info "Breaking Change Pre-Announcement"

    Changes to the configuration paths of DataIntegration

### eccenca Explore

- The navigation queries need to be adjusted, and manual migration of customizations is required
- Workspace migration is necessary to introduce a new workspace configuration versioning description field

### cmemc

**v26.1.0 of cmemc finally removes the following deprecated functionality:**

- `dataset resource` command group
    - deprecated in v25.6.0, use `project file` command group instead
- `graph tree` command
    - deprecated in v25.2.0, use the `graph imports tree` command instead
- `admin store migrate` command
    - deprecated in v25.0.0, use the `admin migration` command group instead
- `--overwrite` options
    - deprecated in v25.0.0, use the `--replace` option instead
    - affected commands: `admin store export`, `project import`, `project export`, `admin workspace export`
- deprecated auto-completion URIs
- `dataset delete` command
    - `--project` option, use `--filter projext XXX` instead
- `project create --from-transformation` option
