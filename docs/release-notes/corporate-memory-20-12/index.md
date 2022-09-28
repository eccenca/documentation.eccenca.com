# Corporate Memory 20.12

Corporate Memory 20.12 is the fourth release in 2020.

![20.12 Knowledge Graph View](20-12-IntegrationOfKnowledgeGraphView.png "20.12 Knowledge Graph View")

The highlights of this release are:

- Build: With the integration of all main views of the Data Integration build workbench, building Knowledge Graphs was never so smooth and streamlined.
- Automate: With cmemc's workflow io command, execution of workflows with variable file payload (input) as well as receiving data from a workflows (output) was never so easy before. Please refer to the corresponding tutorial.

!!! warning

    With this release of Corporate Memory the DataIntegration and DataManager configurations have to be adapted according to the migration notes below. In addition to that, cmemc deprecates a command which will be removed in the next release.

This release delivers the following component versions:

- eccenca DataPlatform v20.12
- eccenca DataIntegration v20.12
- eccenca DataManager v20.12
- eccenca Corporate Memory Control (cmemc) v20.12
- eccenca Corporate Memory PowerBI Connector v20.12

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v20.12

This version of eccenca DataIntegration adds the following new features:

- Improvements to new Workspace UI
    - Existing views (e.g. editors and reporting interfaces) are now integrated.
        - Knowledge graph datasets show an embedded query and explore view.
    - Quick search dialog: The hotkey ++slash++ allows to quickly switch between projects and tasks.
- Optimized DataPlatform entity retrieval strategy for stability and performance.
- RDF workspace backend does write additional convenience properties for transform tasks and linking tasks
    - `di:usedSourceClass`: lists all classes for which entities are read by this task.
    - `di:usedSourceProperty`: lists all properties that are read by this task.
    - `di:usedTargetClass`: lists all classes for which entities are written by this task.
    - `di:usedTargetProperty`: lists all properties that are written by this task.
- Project resource download button.
- Persisted execution reports:
    - Added a configurable report manager that persists execution reports and allows to retrieve previous reports.
    - Configurable retention time. Reports older than that will be deleted.
- Error output for transformations:
    - Transformations have a new parameter "error output". When executing the workflow, all erroneous entities together with the error description are written to the configured dataset.
- Add JSON sink
- Simple variable workflow execution REST endpoint
    - Allows to execute simple variables workflow (at most one variable input and/or output dataset)
    - Input is provided via query parameters or directly in the request body
    - Output is defined by the `ACCEPT` header and is output in the corresponding MIME type in the response body

In addition to that, these changes are shipped:

- ExcelMap operator:
    - If there are multiple values for a given key, it now returns all values instead of just the last one
- Project file multi-upload:
    - Upload one file after the other instead of all at once
- The configuration parameter `workbench.showHeader` is no longer supported. Instead, a URL parameter is used to decide whether the header should be shown.
- Data preview for XML, CSV and JSON now automatically loaded and shown on the dataset details page.
- After deleting an item the user is now redirected to the project page (previously to the workbench page).
- In addition to that, multiple performance and stability issues were solved.

## eccenca DataManager v20.12

This version of eccenca DataManager adds the following new features:

- General:
    - Support for datatype `rdf:HTML` in object view.
- Data Integration:
    - Add config parameter `DIWorkspace.baseURL` for logout.

In addition to that, these changes are shipped

- General:
    - Add error message if browser is not compatible: Safari, IE.
    - Override default config language with workspace language if user did not select a language before.
- Shacline:
    - Redirect to new resource after use the clone resource feature.
    - Load graph permissions directly from the data request.

In addition to that, multiple performance and stability issues were solved.

## eccenca DataPlatform v20.12

This version of eccenca DataPlatform ships the following changes:

- Spring libraries:
    - Spring Boot version upgraded to `2.2.10.RELEASE`, Spring Cloud version upgraded to `Hoxton.RELEASE`.
- Bootstrap & Vocabularies:
    - cmem ontologies and graphs can now be updated using the bootstrap endpoint.
- Statement Annotation:
    - additional endpoints for browsing and bulk editing
- Graph List:
    - enriched endpoint with additional information
- Label Resolution:
    - per default, in case no language matches, the precedence is ignored an any one value of the defined properties is taken as fallback.
    - in case of multiple matches, the alphabetically first entry is chosen.
- Localization / i18n (20.10.1):
    - language selection in titlehelper, shapes and facets API
    - uses `shui:languageIn` instead of `sh:languageIn`

In addition to that, multiple performance and stability issues were solved.

## eccenca Corporate Memory Control (cmemc) v20.12

This version of cmemc adds the following new features:

- The `workflow io` command was added to allow for executing workflows with variable file payload (input) and receive data from a workflow (output).
    - This feature is described in the advanced tutorial [Processing data with variable input workflows](../../build/processing-data-with-variable-input-workflows/index.md).
    - In addition to that, the concepts of io workflows is described in [Workflow execution and orchestration](../../automate/cmemc-command-line-interface/workflow-execution-and-orchestration/index.md).
- The `admin` command group was added and includes the following commands:
    - `bootstrap` - Update/Import bootstrap data.
    - `showcase` - Create showcase data.
    - `status` - Output health and version information.
- The `template` option of the `graph export` command allows for using the `{{iriname}}` placeholder now.

In addition to that, these changes are shipped:

- The `config check` command outputs a deprecation warning now (use the `admin status` command instead).
- cmemc now sends a User-Agent header with every call, currently: `cmemc/20.12 (Python 3.7.7)`

## eccenca Corporate Memory PowerBI Connector v20.12

This release of our PowerBI Connector does not introduce new features or relevant changes.
We provided a tutorial on how to use this component: [Consuming Graphs in Power BI](../../consume/consuming-graphs-in-power-bi/index.md).

## Migration Notes

### DataIntegration

- No Forward Compatibility of Dataintegration Projects Exports
    - Due to a change in the internal XML serialization DI projects from this version can not be imported into instances running older version of DataIntegration.
    - Please try the following workaround if this is something you need to perform. Contact our support team in case this procedure does not work in your case:

!!! info

    1. download your project resources (if needed)
    1. export the project using cmemc:
        - cmemc project export --type rdfTurtle <your-project-id>
    1. import the project at the back-level instance using cmemc:
        - cmemc project import <your-project-id>.project.ttl <your-project-id>
    1. upload your file resources to the back-level instance (if needed)

- Configuration
    - Remove the following configuration parameter: `workbench.showHeader`
    - In order to enable the new Execution Report Manager you need to configure the respective plugin, see "Execution Report Manager" in DataIntegration for Details.

### DataManager

- In your workspaces configuration add `DIWorkspace.baseUrl` (mostly this will be `"/dataintegration"`):
``` yaml
js.config.workspaces:
  default:
	...
    DIWorkspace:
      ...
      baseUrl: /dataintegration
```

### cmemc

- The `config check` command has be deprecated, please use the `admin status` command instead.

