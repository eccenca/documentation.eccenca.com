---
tags:
    - ReleaseNote
---
# Corporate Memory 20.10

Corporate Memory 20.10 is the third release in 2020.

![20.10 Dataset Profiling](20-10-DatasetProfiling.png "20.10 Dataset Profiling")

The highlights of this release are:

- Release of the new [DataIntegration workspace](../../build/introduction-to-the-user-interface/index.md).
- Support for [statement annotations](../../explore-and-author/graph-exploration/statement-annotations/index.md), in order to express knowledge about specific statements.
- Support for [tracking change sets](../../explore-and-author/graph-exploration/statement-annotations/index.md) for all shape based editing activities.
- Support for automation of vocabulary and dataset management with [cmemc](../../automate/cmemc-command-line-interface/index.md).

!!! warning

    With this release of Corporate Memory the DataIntegration and DataManager configurations have to be adapted according to the migration notes below. In addition to that, cmemc has a change default behaviour.

This release delivers the following component versions:

- eccenca DataPlatform v20.10.1
- eccenca DataIntegration v20.10
- eccenca DataManager v20.10.1
- eccenca Corporate Memory Control (cmemc) v20.10
- eccenca Corporate Memory PowerBI Connector v20.10

More detailed release notes for these versions are listed below.


## eccenca DataIntegration v20.10.1

This version of eccenca DataIntegration adds the following new features:

- Improvements to new Workspace UI:
    - New Workspace UI allows to export projects with and without file resources.
    - Basic support for multiple languages in the New Workspace UI. Initially English and German are supported and plugins are not translated yet.
    - Multi-step Project import in new workspace UI.
    - Multi-step, asynchronous project import REST API.
    - Profiling UI component to start dataset profiling and show profiling information in the dataset preview.
    - Navigation menu in new workspace UI.
    - In link tables, clicking on an entity redirects to the corresponding resource in DataManager, if the entity is coming from an RDF dataset.
- New/improved operators:
    - New transform operator to retrieve lat/long of a location from a specified API in order to normalize location data.
    - New operator to scale similarity values in linking rules by a specified factor.
    - Email operator improvements:
        - multiple recipients in TO, CC and BCC
        - CC and BCC recipients
        - Timeout parameter
        - SSL support
- Improvements to datasets
    - CSV Dataset supports UTF-8-BOM encoding for writing CSVs that open correctly in Excel.
    - Support for #id and #text paths in JSON sources.
- API improvements
    - Task activities API that allows to fetch a list of task activities with optional project and status filter.
    - Profiling data is available via the API.
- Global vocabulary cache that holds all installed vocabularies from the DataPlatform.
    - REST endpoint to trigger cache updates.

In addition to that, these changes are shipped:

- Vocabulary caches are not persisted between reboots and workspace reloads
- Disable geo location data type detector by default via plugin.blacklist parameter
- Item search API returns plugin IDs where available
- Expose some Amazon S3 client configuration. Can be changed in the Dataintegration configuration now
- Improvements to Spark execution engine
    - Entities are stored in DataFrames instead of RDDs
    - Performance improvements
    - Bugfixes
- Check for usages of resources in all tasks, before deleting them. This was checked only in datasets before
- File management improvements
    - Allow multi file uploads
    - Ask to replace existing files
    - Allow to delete uploaded files in upload dialog
    - When deleting files check for usages of resources in all items, before deleting them, e.g. transform tasks. This was checked only in datasets before
    - When deleting files that are in use, link the dependent items
    - Upload modal does not close when clicking outside of the modal
    - If the limit parameter of the itemSearch API is set to 0, it will now return all search results instead of none
    - Frontend initialisation endpoint returns initial language preference and configured DM base URL

Finally, the following performance and stability issues were solved:

- Regression: the output of a transformation is lost after reloading
- Added warning to the CSV datasets 'maxCharsPerColumn' parameter to make it clear that it affects the heap size
- Fixed reading of JSON files that contain Unicode byte order marks (BOMs)
- Workflow not interrupted on invalid XML from Triple-store
- Fixed generating paths for JSON files that contain keys with special characters, such as spaces. Those will be encoded now
- Project's rdfs:label uses project ID instead of label
- Generate consistent URIs for object mappings on JSON files
- Caches have not been written if the XML workspace provider was used
- Do not recreate caches on every run
- In link tables, the header shows the task labels instead of the task ids
- Fixed search field in link tables (did not work with characters that need to be URL encoded)
- Meta data description does not maintain whitespace formatting in XML serialisation
- New workspace UI has invalid favicon
- Creating a new project with description does not store the description in the new workspace UI
- XML Dataset: Values that include HTML entities are not retrieved
- Support for MS Internet Explorer 11 in new workspace
- Logout action not working. Should perform a global logout
- Deleting S3 backed resources broken due to a slash added to filenames
- Update PostgreSQL driver to v42.2.14 because of security vulnerability


## eccenca DataManager v20.10.1

This version of eccenca DataManager adds the following new features:

- General
    - Add translations and i18n language selection (and ship english and german translations)
    - Allow for [Annotation of Statements with additional meta data](../../explore-and-author/graph-exploration/statement-annotations/index.md)
    - Integrate with the new [DataIntegration workspace](../../build/introduction-to-the-user-interface/index.md) (Data Integration Tab)
- Shacline
    - Add support for 'sh:languageIn' (as multiple values) in literal properties
- Resource Tables
    - Allow Lucene syntax in the search field of any resource table ([Query Syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html))
        - This search will be applied to the label(s) configured in `proxy.labelProperties`; by default the search will only be applied to the first column, the labels of the selected resource

In addition to that, these changes are shipped:

- Shacline
    - Use the new resource/shaped API to generate / save shacl forms.
    - Rendering empty fields on every change
    - Add class triple to save only if class is a string.
    - Prevent labels to be cloned on adding a new block.
    - Nested Table query now defines default graph
    - `{graph}` can now be used as a placeholder in RFC6570 URI Template string
- ResourceTable
    - Download data does not retain column order
    - Add pagination/limit on config file
    - Lock Drag and Drop while adding columns to prevent collision
    - Update default pagination limit to 25 and default pagination interval to 5, 10, 25, 100, 500, 1000
- General
    - use new backend API to retrieve labels.
    - use new backend API to retrieve facets (possible columns)
    - **DEPRECATE** titleHelper configuration parameters
    - **BREAKING** remove support for Internet Explorer 11.
    - Disable Datasets module, moved to Data Integration
    - Disable Build module, moved to Data Integration
- ResourceSelect
    - Wait until click on it to load values.
- Explore
    - Cyclic references on Tabs content crash the app
    - modules.explore.navigation.topQuery changed in order to list configured graph classes (`shui:managedClasses`)
    - Update Navigation pagination limit to 15
    - Load ResourceTable pagination limit from config file

In addition to that, multiple performance and stability issues were solved.


## eccenca DataPlatform v20.10

This version of eccenca DataPlatform adds the following new features:

- Custom endpoint
    - Create custom json endpoints by defining a query for retrieving the data and a template for transforming the result.
- Concise Boundary Description retrieval depth is adjustable.
- New submodule `:src:it` for integration tests
- Statement Annotations/Metadata
    - APIs for providing access and managing existing relations
- Additional APIs
    - Explore Facets (`/api/explore/facets`): Lists the properties of a class or query.
    - Graph List (`/api/graphs/list`): Returns a list of graphs readable by the current user, optionally including OWL imports.
    - Graph List Detailed (`/api/graphs/list-detailed`): Like the previous one, but adding details of triples, classes and instances counts.
    - Added openapi.server.urls env variable in order to define custom baseUrl to be used in
    - Added resource shaping to the backend, this includes
        - Resource (`/api/resources`) api for getting information about individual resources
        - Shape (`/api/shapes`) api for applying shape information onto the graph
        - Statement Level Metadata (`/api/statementmetadata/`) management for adding statement annotations.
    - Added Caching to internal handling of prefixes, vocabularies and shapes lists. Caches are invalidated by updates.
    - Added Showcase (`/api/admin/showcase`) endpoint, which inserts a scalable test dataset into the configured endpoint.

In addition to that, multiple performance and stability issues were solved.


## eccenca Corporate Memory Control (cmemc) v20.10

This version of cmemc adds the following new features:

- A `dataset` command group, enabling users to `create`, `delete` and `update` datasets as well as `upload` and `download` dataset file resources.
- A `vocabulary` command group, enabling users to manage vocabularies similar to the [vocabulary catalog](../../explore-and-author/vocabulary-catalog/index.md).
- The `query execute` command has some new options for limit, offset distinct and timeout settings.

In addition to that, these changes are shipped:

- Added:
    - The `workflow status` command has a `--project` option
- Changed:
    - The `graph import` command outputs a replace/add status message per graph.
    - Much faster `workflow status` retrieval by using a new activity API
    - The `dataset export` command default file template changed to `{{date}}-{{connection}}-{{id}}.project`
    - The `query execute` command now uses POST instead of GET requests for SPARQL queries
- Fixed:
    - The `graph import --replace` command  does not re-replace a same graph with a different file anymore.
    - The completion of `--filename-template` resulted in files with wrong chars.
    - The python version is disabled in completion mode.


## eccenca Corporate Memory PowerBI Connector (v20.10)

This release of our PowerBI Connector does not introduce new features or relevant changes. We provided a tutorial on how to use this component: [Consuming Graphs in Power BI](../../consume/consuming-graphs-in-power-bi/index.md)


# Migration Notes

## DataIntegration

- XML serialization for meta data elements is not forward compatible, i.e. projects exported with this version cannot be imported in older DataIntegration versions.
- The logout URL needs to be set to make sure that DataIntegration also triggers a logout inside the Keycloak instance:
    ```
    oauth.logoutRedirectUrl = ${DEPLOY_BASE_URL}"/auth/realms/cmem/protocol/openid-connect/logout?redirect_uri="${DEPLOY_BASE_URL}
    ```

## DataManager

- The `graphInfo` flag in the explore module is now enabled by default.
- Due to the introduction of the new DataIntegration workspace these changes need to be applied:
    - The modules `build` as well as `datasets` are disabled now by default.
    - The module `explore` is the default first entry point (`startsWith`).
    - This section needs to be added to each workspace configuration:
    ``` yaml
        DIWorkspace:
          enable: true
          url: /dataintegration/workbench
      ```

## cmemc

- If your automation scripts rely on the created file name of the project export command, you need to change your scripts and set the old export name explicitly with `-t {{id}}`.

