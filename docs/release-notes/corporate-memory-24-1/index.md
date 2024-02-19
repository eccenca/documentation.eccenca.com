---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 24.1.0

Corporate Memory 24.1.0 is the first release in the 24.1 release line.

<!--
TODO: update feature pics
![23.3: Charts - Chart Definitions](23-3-explore-charts.png "23.3: Charts - Definition of CHarts based on eCharts "){ class="bordered" }
![23.3: Build - Keyboard Shortcuts](23-3-build-keyboard-shortcuts.png "23.3: Build - Keyboard Shortcuts"){ class="bordered" }
![23.3: Build - Workflow Ports](23-3-build-port-menu.png "23.3: Build - Workflow Ports"){ class="bordered" }
-->

The highlights of this release are:

<!--
TODO: update highlights section
-   Explore and Author:
    -   new **[charts catalog](../../explore-and-author/charts-catalog/index.md)** module added, which allows for defining BI widgets / charts which can be integrated into shapes
    -   preview release of our generative AI / LLM based **[Ontology](../../explore-and-author/easynav-module/index.md#llm-ontology-assist) and [Query](../../explore-and-author/query-module/index.md#llm-query-assist) Assistant**
-   Build:
    -   operate BUILD like never before by using the new **keyboard shortcuts** (press "?" in the build module to learn the details)
    -   several **improvements to the workflows view**: create new datasets and other workflow-operators in place, dependencies and execution order is now explicitly modeled, show schema or ports
-   Automate:
    -   new **`project variable` command group** plus several addition to existing commands
-->

This release delivers the following component versions:

-   eccenca DataIntegration v24.1.0
-   eccenca DataManager v24.1.0
-   eccenca DataPlatform v24.1.0
-   eccenca Corporate Memory Control (cmemc) v24.1.0

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v24.1.0

We're excited to bring you the latest update to DataIntegration v24.1.0, which introduces new features, improvements and bug fixes:

v24.1.0 of DataIntegration adds the following new features:

-   Error notification
    -   Add badge to error notification menu icon with error count.
-   Multiline editing of template values.
-   Added loose connection of workflow nodes similar to linking editor.
-   XML, JSON, Excel and CSV datasets support retrieving the line and column numbers.
    -   TODO: add the special paths here ...
-   Error report for (validation) errors in transform and linking rule editors and transform execution report
    -   Shows additional details like a stack-trace and input values.
-   Added hotkey integration for creating new items in the workflow editor.
-   Improved REST operator (v2)
    -   Support for multiple REST requests, one per input entity.
    -   _Paging support:_ If the API does not return all results in a single request, this features allows to page via multiple requests and merge the results of all requests.
    -   _Better error handling and retry mechanism:_ Retries requests and collects errors for execution report.
    -   _Rate limiting:_ Setting a delay between subsequent requests.
    -   _Limit and Offset:_ Only executes a specific "_window_" of the input entities/requests.
    -   _URL property:_ Allows to define a property that is injected into the result JSON that contains the original request URL.
    -   _Dataset file output:_ A file based dataset can be connected to the operator output, which overwrites the dataset file with the results from the REST requests
        -   This allows to handle REST results as any dataset content.
        -   Supports zip files. If a dataset (currently JSON, XML, RDF file, CSV) specifies a zip file (ending in `.zip`) a zip archive is written that contains one file per request result.
-   _Json dataset:_ Support bulk resources, i.e. JSON files in a zip file.
-   Python workflow plugins can now consume or produce hierarchical entities.
-   Additions to the workflow config ports:
    -   Allow to reconfigure transform and linking tasks in workflows.
    -   Datasets can be connected directly to the config port.
-   Extended auto-completion support when opening the mapping (rule) editor in a workflow context:
    -   Support auto-completion of target properties for fixed target schema and config port schema (transformation connected to config port).
    -   Support auto-completion of values paths for fixed input schema.
-   Added timer for workflow execution and in activity view.

v24.1.0 of DataIntegration introduces the following changes:

-   Show project variables re-ordering errors (with details) directly in project variables widget.
-   Support PATCH and DELETE requests in REST operators.
-   Upgraded libraries, in particular Play to v2.9.1 and Spark to v3.5.0.
-   Support of custom tasks as input for transform and linking tasks.
-   Create/update dialog:
    -   When a parameter value is changed that other parameters are depending on, those parameter values are reset because they might not be valid anymore.
-   Shortened workflow execution failure message shown in activity widget.
-   Added "_Fail workflow_" flag to "_Cancel workflow_" operator.

v24.1.0 of DataIntegration ships the following fixes:

-   Many errors occurring in a dialog/modal, e.g. from requests, are hidden because they are shown in the global error notification which cannot be accessed while the dialog is open.
-   Missing or problematic error handling in several dialogs and other places.
-   Transform editor should show plugin labels instead of ids.
-   Transform execution report validation icons in mapping tree do not update after running the execution.
-   When upgrading a plugin, new parameters are not shown in transform editor.
-   _Workflow editor:_ Creating a new connected task that has no input port connects to the output port.
-   Copying a project with custom prefixes into a project that misses these prefixes fails.
-   Workflow report always states "_...has not finished execution yet._".
-   Cannot add a new project variable after adding it empty valued.

## eccenca DataManager v24.1.0

We are excited to announce the latest update to DataManager v24.1.0, which introduces new features, improvements and bug fixes:

v24.1.0 of DataManager adds the following new features:

v24.1.0 of DataManager ships the following changes:

v24.1.0 of DataManager ships the following fixes:

## eccenca DataPlatform v24.1.0

We're excited to bring you the latest update to DataPlatform v24.1.0, which introduces new features, improvements and bug fixes:

v24.1.0 of DataPlatform adds the following new features:

-   Add license information to DP actuator info endpoint response.
-   Added endpoints for SHACL validation / Resource shaping
    -   SHACL validation and resource shaping
        -   endpoints for validation, node shape structure views and data retrieval.
    -   SHACL batch validation
        -   added application property `scheduler.backgroundQueryPoolSize` (Default: 4)
            -   maximum numbers of threads for background jobs (i.e. shacl batch validation).
        -   added application property `proxy.shaclBatchResultsMemoryBoundaryInMb` (Default: 100)
            -   amount in Megabytes (Mb) for shacl batch validation results kept in memory for status retrieval.
-   Access condition review endpoint
    -   ability to check user rights (access conditions) for a set of groups.

v24.1.0 of DataPlatform ships the following changes:

-   Static access condition prefix split for newly created access conditions
    -   `<http://eccenca.com/>` – prefix for Access Condition Groups / Users.
    -   `<http://eccenca.com/ac/>` – prefix for Access Conditions.
-   Added tracing id to audit logs.
-   Add feature flag field to workspace configuration.
-   Add support for GraphDb 10.5.

v24.1.0 of DataPlatform ships the following fixes:

-   Allow blank nodes in update queries.
-   DP APIs do not return null values for unset fields anymore.
-   Correct documentation of API endpoints for named query execution.

## eccenca Corporate Memory Control (cmemc) v24.1.0

We're excited to bring you the latest update to Corporate Memory Control (cmemc) v24.1.0, which introduces new features, improvements and bug fixes:

v24.1.0 of Corporate Memory Control (cmemc) adds the following new features:

-   Added support for importing vocabulary from standard input (stdin)
    -   `admin acl` command group
    -   `create` command - Create an access condition
    -   `delete` command - Delete access conditions
    -   `inspect` command - Inspects the access condition
    -   `list` command - List all access conditions
    -   `review` command - Reviews the graph rights for a given access condition
    -   `update` command - Updates an access condition
-   `graph validation` command group
    -   `execute` command - Start a validation process
    -   `inspect` command - Inspect validation process results
    -   `list` command - List validation processes
    -   `cancel` command - Cancel a running validation process
-   `admin user list` command
    -   `--filter` option - filter user list
-   `admin status` command
    -   raises an error if the Corporate Memory license is expired (grace period)
    -   raises a warning if the GraphDB license expires in less than one month
-   `dataset create` command
    -   support to use JSON Lines files as JSON datasets
    -   support to use YAML files as TEXT datasets

v24.1.0 of Corporate Memory Control (cmemc) ships the following changes:

-   `graph import` command
    -   importing a directory to a single graph no longer raises an error but imports all turtle files to this graph
-   docker image: python 3.11.8

## Migration Notes

!!! info

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v24.1.0 into DataIntegration v23.3.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v23.3.0 can be imported into DataIntegration v24.1.0.

### DataIntegration

There is a known issue and existing workaround with the new dependency port feature: you may receive a message like this when running your workflows:

```
Workflow Execution Error:
Not all workflow nodes were executed! Executed 2 of 7 nodes.
```

In this case, open the affected workflow in DataIntegration and click the save button once (no changes are required).
After saving it will work again.

### DataPlatform

DP APIs do not return null values for unset fields anymore.

!!! warning

    Check if null values of non mandatory fields are expected if you are using the DataPlatform APIs with a custom client.

### cmemc

No migrations are required going from cmemc 23.3.x to 24.1.x.

