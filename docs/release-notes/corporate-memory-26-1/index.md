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

-   Build:
    -   ...

-   Explore:
    -   ...

-   Automate
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

We are excited to announce the release of DataIntegration v26.1, ...


## eccenca Explore v26.1.0

We are pleased to announce Explore v26.1,  ...


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
  - `--include-access-conditions` flag to `admin workspace export` and `admin workspace import` to bundle access control
    data with project archives
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

...

### eccenca Explore

...

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

