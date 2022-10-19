---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 22.2

Corporate Memory 22.2 is the second release in 2022.

<!-- ![22.2: DataIntegration - Linking Editor](22-1-linking-editor.png "22.1: DataIntegration - Linking Editor") -->
<!-- ![22.2: DataManager - Workflow Execution](22-1-workflow-execution.png "22.1: DataManager - Workflow Execution") -->
![22.2: cmemc - Multiple Filter / Admin Status](22-2-cmemc-multiple-filter-and-admin-status.png "22.1: 22-2-cmemc-multiple-filter-and-admin-status.png")

The highlights of this release are:

-   Build:
    -   The all new **Active** (Link) **Learning UI**
    -   Extended **Python Plugin SDK**
-   Explore:
    -   New graph exploration module **EasyNav**
-   Consume:
        -   ... ?
-   Automate:
    -   ...

!!! warning

    With this release of Corporate Memory the DataPlatform configuration and behavior has changed and have to be adapted according to the migration notes below.

!!! warning

    With this release of Corporate Memory the (DataIntegration) Python plugin SDK added the `ExecutionContext` class. This results in a changed signature of the SDK API functions and thus in a breaking change. Your python SDK based plugins have to be adapted according to the migration notes below.

This release delivers the following component versions:

-   eccenca DataPlatform v22.2
-   eccenca DataIntegration v22.2
-   eccenca DataManager v22.2
-   eccenca Corporate Memory Control (cmemc) v22.2

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v22.2

This version of eccenca DataIntegration adds the following new features:

-   ...

In addition to that, these changes are shipped:

-   ...

In addition to that, multiple performance and stability issues were solved.

## eccenca DataManager v22.2

This version of eccenca DataManager adds the following new features:

-   Navigation
    -   Add DataIntegration workflows link to main navigation
-   Vocabulary Catalog
    -   Inline vocabulary metadata via (editable) shape
    -   Ability to activate git synchronization of changes
        -   Change history with diff view and ability to revert to a specific commit
-   Explore
    -   New (Shacl) Template based graph creation wizard
        -   Supporting different methods to define / select graph IRIs
        -   Support for bulk add via `.zip` archives containing multiple RDF files
-   i18n
    -   French translation
-   EasyNav
    -   New graph visualization module
    -   With search filter configuration
    -   Bulk node search and bulk add
    -   Ability to save, load and share explorations

In addition to that, these changes are shipped:

-   Increase height of Turtle editor in the resource details view.

In addition to that, multiple performance and stability issues were solved.

## eccenca DataPlatform v22.2

This version of eccenca DataPlatform ships the following new features:

-   …

In addition to that, these changes and fixes are shipped:

-   New store configuration properties, see below for migration notes
-   …

The following have been removed:

-   Support for provisioned store authorization
-   Command line options create-config, update-war
-   WAR build target and support for WAR servlet deployment
-   Property for DP query system timeout check interval
    -   `proxy.queryTimeoutCheckCron` not necessary anymore
-   Support for multiple endpoints

In addition to that, multiple performance and stability issues were solved.

## eccenca Corporate Memory Control (cmemc) v22.2

This version of cmemc adds the following new features:

-   `admin workspace python list-plugins` command
    -   New option `--package-id-only` to output only package IDs
-   `admin workspace python install` command completion
    -   now also provides plugin packages published on pypi.org
-   `query status` command
    -   New filter `query`:
        -   `graph` - List only queries which affected a certain graph (URL)
        -   `regex` - List only queries which query text matches a regular expression
        -   `trace-id` - List only queries which have the specified trace ID
        -   `user` - List only queries executed by the specified account (URL)
    -   New values for filter `status`:
        -   `cancelled`: List only queries which were cancelled
        -   `timeout`: List only queries which ran into a timeout
-   `query cancel` command
    -   cancel a running query - this stops the execution in the backend
    -   Depending on the backend store, this will result in a broken result stream (stardog, neptune and virtuoso) or a valid result stream with incomplete results (graphdb)
-   `dataset list`|`delete` commands
    -   New option `--filter` with the following concrete filter
        -   `project` - filter by project ID
        -   `regex` - filter by regular expression on the dataset label
        -   `tag` - filter by tag label
        -   `type` - filter by dataset type
-   `workflow list` command
    -   New option `--filter` with the following concrete filter
        -   `project` - filter by project ID
        -   `regex` - filter by regular expression on the dataset label
        -   `tag` - filter by tag label
        -   `io` - filter by io type
-   `admin status` command
    -   overall rewrite
    -   new table output
    -   new option `--raw` to output collected status / info values
    -   new option `--key` to output only specific values
    -   new option `--enforce-table` to enforce table output of `--key`
-   `vocabular import` command
    -   new option `--namespace`: In case the imported vocabulary file does not include a preferred namespace prefix, you can manually add a namespace prefix

In addition to that, these changes and fixes are shipped:

-   `admin workspace python list-plugins` command
    -   Additionally outputs the Package ID
-   `project import` command
    -   The project id is now optional when importing project files
-   `admin status` command
    -   new table output (similar to the other tables)
    -   `status` filter with `error` value
        -   only execution errors are listed
        -   this means esp. no cancelled and timeouted queries (they have there own status now)
-   Add pysocks dependency to cmempy
    -   This allows for using the `all_proxy` evironment variable
-   `dataset list --raw` output
    -   output was not a JSON array and not filtered correctly
-   cmempy get graph streames
    -   stream enabled
-   `admin status` command
    -   command will now always return, even if a component is down

The following commands are removed:

-   `admin bootstap` command
    -   was deprecated in 22.1, use `admin store bootstrap` command instead
-   `admin showcase` command
    -   was deprecated in 22.1, use `admin store showcase` command instead
-   `dataset list`|`delete` command
    -   `--project` option, use `--filter projext XXX` instead

In addition to that, multiple performance and stability issues were solved.

## Migration Notes

### DataIntegration

-   CSV attributes specified via the `properties` parameter had inconsistent encoding rules. For CSV datasets where the `properties` parameter is used this can lead to changed source paths.

#### Python plugins

Due to the added context classes, the signature of a number of functions has been changed. The following changes need to be made to implementation of these classes:

##### WorkflowPlugin

-   The execute function has a new parameter `context`:
    -   `def execute(self, inputs: Sequence[Entities], context: ExecutionContext)`

##### ParameterType

-   The `project_id` parameters of the label and the autocompletion functions have been replaced by the PluginContext:
    -   `def autocomplete(self, query_terms: list[str], context: PluginContext) -> list[Autocompletion]`
    -   `def label(self, value: str, context: PluginContext) -> Optional[str]`
    -   The project identifier can still be accessed via `context.project_id`
-   The `fromString` function has a new parameter `context`:
    -   `def from_string(self, value: str, context: PluginContext) -> T`

### DataManager

-   ...

### DataPlatform

Due to the removed multiple endpoint support the store configuration properties have changed. Please revise your store configuration section(s) in your DataPlatform `application.yml`. The new configuration properties are:

-   Type of store (general settings)
    -   `store.type`: MEMORY, HTTP, GRAPHDB, STARDOG, VIRTUOSO, NEPTUNE
    -   `store.authorization`: NONE, REWRITE_FROM
-   MEMORY:
    -   `store.memory.files`: List of files loaded on startup
-   HTTP:
    -   `store.http.queryEndpointUrl`: SPARQL Query endpoint (mandatory)
    -   `store.http.updateEndpointUrl`: SPARQL Update endpoint (mandatory)
    -   `store.http.graphStoreEndpointUrl`: SPARQL GSP endpoint (optional but highly recommended)
    -   `store.http.username`: Username (optional)
    -   `store.http.password`: Password (optional)
-   GRAPHDB:
    -   `store.graphdb.host`: host of graphdb backend (i.e. localhost)
    -   `store.graphdb.port`: port of graphdb backend (i.e. 7200)
    -   `store.graphdb.ssl-enabled`: flag if ssl (https) is enabled (default: false)
    -   `store.graphdb.repository`: name of repository (i.e. cmem)
    -   `store.graphdb.username`: Username (optional)
    -   `store.graphdb.password`: Password (optional)
    -   `store.graphdb.useDirectTransfer`: flag if direct GSP endpoints of graphdb shall be used instead of workbench upload (default: true)
    -   `store.graphdb.importDirectory`: Import directory to be utilized in the "workbench import with shared folder" approach.
    -   `store.graphdb.graphDbChangeTrackingActive`: Whether change tracking for updates is active - better results for cache invalidation (default: true)
    -   `store.graphdb.graphDbChangeTrackingMaxQuadMemory`: Amount of quads as a result of an update which are loaded into memory for analyzing consequences for caches (default: 1000)
-   STARDOG:
    -   `store.stardog.host`: host of stardog backend (i.e. localhost)
    -   `store.stardog.port`: port of stardog backend (i.e. 5820)
    -   `store.stardog.ssl-enabled`: flag if ssl (https) is enabled (default: false)
    -   `store.stardog.repository`: name of repository (i.e. cmem)
    -   `store.stardog.username`: Username (optional)
    -   `store.stardog.password`: Password (optional)
    -   `store.stardog.userPasswordSalt`: salt for generated user password (optional)
    -   `store.stardog.updateTimeoutInMilliseconds`: Timeout in ms for updates (default: 0 = deactivated)
    -   `store.stardog.graphListQuery`: Query for graph list - graph must be bound to variable ?g
-   NEPTUNE:
    -   `store.neptune.host`: host of neptune backend (i.e. neptune-cluster123.eu-central-1.neptune.amazonaws.com)
    -   `store.neptune.port`: port of neptune backend (i.e. 8182)
    -   `store.neptune.graphListQuery`: Query for graph list - graph must be bound to variable ?g
    -   Settings under store.neptune.aws (mandatory):
        -   `store.neptune.aws.region`: AWS region where the configured neptune cluster is located (i.e. eu-central-1)
        -   `store.neptune.aws.authEnabled`: Flag on whether authentication is enabled on neptune cluster (default: true)
    -   Settings under `store.neptune.s3` for upload of large files (>150MB uncompressed) (optional):
        -   `store.neptune.s3.bucketNameOrAPAlias`: Name of bucket or access point for S3 bulk load
        -   `store.neptune.s3.iamRoleArn`: ARN of role under which neptune cluster loads from S3
        -   `store.neptune.s3.bulkLoadThresholdInMb`: Load threshold in MB for GSP access, if graph data greater than S3 upload is used (default: 150)
        -   `store.neptune.s3.bulkLoadParallelism`: Degree of parallelism for neptune S3 bulk loader (LOW (default), MEDIUM, HIGH, OVERSUBSCRIBE)
-   VIRTUOSO:
    -   `store.virtuoso.host`: host of virtuoso backend (i.e. localhost)
    -   `store.virtuoso.port`: http port of virtuoso backend (i.e. 8080)
    -   `store.virtuoso.databasePort`: database port of virtuoso backend (i.e. 1111)
    -   `store.virtuoso.ssl-enabled`: flag if ssl (https) is enabled (default: false)
    -   `store.virtuoso.username`: Username (optional)
    -   `store.virtuoso.password`: Password (optional)

### cmemc

-   `dataset list`|`delete command`
    -   option `--project` is removed
    -   Please use `--filter project XXX` instead
-   `admin status` command
    -   in case you piped the normal output of this command and reacted on that, you need to use the `--key` command now
