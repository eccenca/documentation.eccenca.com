---
tags:
    - ReleaseNote
---
# Corporate Memory 20.06

Corporate Memory 20.06 is the second release in 2020.

The highlights of this release are:

- Jinja template support in DataIntegration workflows
- Physical unit normalization and distance measure operators
- Versioning of user edits in SHACL based forms
- Named query API to get data without SPARQL know-how
- OpenAPI compliant DataPlatform API specification and UI
- Preview/Beta release of the upcoming DataIntegration Workspace
- Preview/Beta support for [GraphDB](../../deploy-and-configure/configuration/quad-store-configuration/index.md) as triple store backend → [Vendor Homepage](http://graphdb.ontotext.com/)

!!! warning

    With this release of Corporate Memory the DataIntegration, DataManager and DataPlatform configuration must be adapted according to the migration notes below. In addition to that, cmemc has some changed default outputs.

This release delivers the following component versions:

- eccenca DataPlatform v20.06
- eccenca DataIntegration v20.06
- eccenca DataManager v20.06
- eccenca Corporate Memory Control (cmemc) v20.06
- eccenca Corporate Memory PowerBI Connector v20.06

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v20.06

This version of eccenca DataIntegration adds the following new features:

- Workflow operator that evaluates a user-defined template on entities.
    - Jinja templating language is supported.
    - Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel.
    - For each input entity, an output entity is generated that provides a single output attribute, which contains the evaluated template.
    - `DataIntegration` transformation tasks can be used as Jinja filters.
- Operators to normalize and compare physical quantities.
    - Transform rule operator to normalize physical quantities to a base unit.
    - Distance measure to compare two physical quantities.
- The transform evaluate tab allows the selection of the mapping rule to be evaluated.
- Rule operator for generating UUIDs.
- Complete rework of the workspace UI

In addition to that, these changes are shipped:

- Removed deprecated SQL query strategies.
- Updated eccenca logo and favicon.
- Consistent resource deletion behavior for resource repositories:
    - For resource repositories that do not share resources between projects, resources are removed on project deletion.
    - For resource repositories that do share resources between projects, resources are NOT removed on project deletion.
    - In both cases, the user is informed in the UI about the behavior of the configured resource repository.
- RDF Workspace Provider: Improved reading of project data if Graph Store protocol is supported by RDF endpoint.
- RDF Workspace Provider: Improved import of projects if Graph Store protocol is supported by RDF endpoint.
- More consistent labels for tasks, operators and their parameters.
- If active learning is started with an existing linkage rule, it's also used to generate the unlabeled pool.
- `ExcelMapTransformer` reloads the referenced resource if it's modification time changed. For performance reasons the check may be deferred by some seconds.

In addition to that, multiple performance and stability issues were solved.

## eccenca DataManager v20.06

This version of eccenca DataManager adds the following new features:

- Query Module
    - The results of CONSTRUCT queries can now be downloaded.
- General
    - Support to send base64 encoded queries in SPARQL and framed requests (configure with `js.config.api.sparqlQueryBase64Enconded`).
    - Add new helper for unify datatype info (as regex)
- Build module
    - Show/hide build module based on user (ACL) action `urn:eccenca:di`.
- Shacline
    - Allow sh:name and sh:description to used multiple times - in different languages - in the SHAPE definitions.
    - Support for the `xsd` formats `gYearMonth`, `gYear`, `gMonthDay`, `gDay`, `gMonth` and `duration`.

In addition to that, these changes are shipped:

- General
    - Upgrade node, npm and yarn.
    - Allow `sh:pattern` and `sh:flags` for shapes definition of literals of type string, numeric and dates.
- Shacline
- Shacl-groups without content are now hidden.
- ReadOnly properties are not available for adding on edit mode.
- Use languages from `js.config.titleHelper.languages` from config file as default languages.

In addition to that, multiple stability issues were solved.

## eccenca DataPlatform v20.06

This version of eccenca DataPlatform adds the following new features:

- SPARQL 1.1 Query & Update endpoint
    - Support for base64 encoded query strings.
- Manual Edit Endpoint
    - Fine grained access control schemes for edits performed on SHACL shapes.
    - Basic versioning of those edits.
    - Shapes that support the configuration of those features directly in DataManager
- OpenAPI 3 compliant API documentation
    - OpenAPI compliant documentation of all DataPlatform APIs
    - Swagger UI based browser interface for interactive learning and experiments with the APIs
- Backend Support
    - Support for GraphDB was added.
- Additional APIs
    - Title Helper (`/api/explore/title`): Finds short labels for Resources.
    - Named Query (`/api/queries`): Allows passing the identifier of the query and a parameterization to generate a CSV report

In addition to that, these changes are shipped:

- OpenAPI 3 compliant API documentation
    - All REST controllers have been annotated with OpenAPI metadata annotations
    - `SecurityConfiguration` has been modified to allow access to the `/v3/api-docs`(`.yaml`) and `/swagger-ui` endpoints.

The following features have been removed in this release:

- OpenAPI 3 compliant API documentation
    - RAML documentation

In addition to that, multiple performance and stability issues were solved.

## eccenca Corporate Memory Control (cmemc) v20.06

This version of eccenca Corporate Memory Control (cmemc) adds the following new features:

- Shipped with a MacOSX binary (installable as copy deployment or via the homebrew package manager).
- Support for base64 encoded SPARQL queries and updates (`--base64`) - this needs eccenca DataPlatform v20.06.
- Extension of the query list command to list labels and parameters of queries in the query catalog (also the `--id-only` parameter to get an ID only list).
- Support for parameterized SPARQL queries: the query execute command now has the option `-p` / `--parameter` to provide parameter/value pairs for the query execution.

In addition to that, these changes are shipped:

- query execute
    - default result format is now `text/csv` for tables and text/turtle for graphs (was `*` before)
    - Migration Note: use `--accept` in case you need the old defaults
- query list
    - now has a tabularized output
    - Migration Note: use `--id-only` option to get the old URI only list

In addition to that, multiple performance and stability issues were solved:

- cmemc now supports all SPARQL query types when executing a query from a file (there were errors on `ASK`, `DESCRIBE` and `CONSTRUCT` before)
- all tab completion results are now correctly sorted as well as filtered case-insensitively

## eccenca Corporate Memory PowerBI Connector (v20.06)

This is the first release of our PowerBI Connector which enables PowerBI users to retrieve data into PowerBI, based on collected queries in the Corporate Memory Query Catalog.

The feature of this release are:

- add and delete eccenca Corporate Memory data sources
- get data out of SELECT queries from the Query Catalog

We provided a tutorial for this new component: [Consuming Graphs in Power BI](../../consume/consuming-graphs-in-power-bi/index.md)

## Migration Notes

### DataIntegration

With v20.06 the API has been improved:

- The JSON format of transform, linking and workflow tasks has changed and is now consistent with dataset and custom tasks, i.e. all config parameters are now under property `parameters`.
- The JSON format of transform tasks has in addition following changes:
    - `output` instead of `outputs` property that is a single string value instead of an array of strings.
    - `mappingRule` instead of `root` for the property of the mapping rule.
- The JSON format of linking tasks had in addition following change:
    - `output` instead of `outputs` property that is a single string value instead of an array of strings.
- The JSON format for the `/plugins` endpoint has changed. The `type` attribute is now correctly specifying the JSON schema data type, e.g. `string` or `object`.
- The actual, more specific, parameter type has been renamed to `parameterType`.
- JSON format of resources have no relative and absolute path anymore.

### DataManager

With v20.06 a new title helper configuration section is introduced.
It is used to define you language preferences in the data:

``` yaml title="DataManager application.yml BUILD module configuration"
js.config.titleHelper:
  languages:
    - en
    - ''
```

In addition to that, we introduced a new Access Condition Action which represents the right to use the EXPLORE tab.
Please have a look at the access condition documentation and add `urn:eccenca:ExploreUserInterface` to already existing conditions if needed.

### cmemc

With v20.06 the following changed need to be made:

- `query execute` default result format has changed, to keep the previous behavior change your cmemc `query execute` calls to:
    - `cmemc query execute --accept '*'`
- `query list` has a different default output, to return to the previous behavior change your cmemc `query list` calls to:
    - `cmemc query list --id-only`
