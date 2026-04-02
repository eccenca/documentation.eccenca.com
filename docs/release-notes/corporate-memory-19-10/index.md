---
tags:
    - ReleaseNote
---
# Corporate Memory 19.10

Corporate Memory 19.10 is the third release in 2019.

The highlights of this release are:

- Switched from an own OAuth 2.0 authorization server implementation to a more capable and supported solution based on Keycloak.
- Largely enhanced JDBC / SQL support:
- Overall performance improvements.
- Allowing hierarchical mappings to write to JDBC/SQL datasets.
- Support for Oracle SQL databases.
- Input validation of mandatory fields in shaceline resource details views.
- Resource Table results can be directly downloaded in Excel and other formats.

!!! warning

    With this release of Corporate Memory the DataPlatform configuration must be adapted according to the migration notes below.

Consequently this release delivers the following component versions:

- eccenca DataPlatform v19.10
- eccenca DataIntegration v19.10
- eccenca DataManager v19.10

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v19.10

This version of eccenca DataIntegration adds the following new features:

- Write support for hierarchical data via JDBC.
- Allow arbitrary column names on `SqlEndpoint` datasets.
- Support for Oracle SQL.
- JSON Rest endpoint that allows to evaluate portions of a linking rules.
- SPARQL 1.1 endpoint each `RdfDataset` thereby allowing instantaneous SPARQL access via REST and SPARQL SERVICE keyword.

In addition to that, these changes are shipped:

- Add parameter that decides how empty values are handled by the concat transformer.
- Add 'ZIP file regex' parameter to all bulk resource datasets that allows to filter resources inside the bulk resource container (currently ZIP files only).
- Simplify Hive Serialization, refactor SQL utility methods.
- SPARQL Update operator
- Do not read from input data source when the SPARQL Update template is static, i.e. when it always runs the same static SPARQL Update query exactly once.
- Add SPARQL Update execution report containing various statistics, e.g. number of queries, query throughput etc.
- Support Apache Velocity Engine based templates. This adds logic like conditional branching and loops to the templates. For more information visit [https://velocity.apache.org](https://velocity.apache.org)
- SPARQL Select operator generates an execution report with various statistics, e.g. rows processed, runtime etc.
- SPARQL dataset generates execution report when executing SPARQL Update queries e.g. from the SPARQL Update operator with statistics like remaining queries, time estimation etc.
- Extended SQL Endpoint documentation.
- Added local execution to JDBC dataset. The execution is more efficient and pushes limits and group-by columns into the database.
- While workspace is initializing, subsequent requests will timeout.
    - Config parameter `workspace.timeouts.waitForWorkspaceInitialization` (in milliseconds, default: 5000ms).
- Scheduler: Added 'Stop On Error' parameter. If enabled this will stop a scheduler on the first execution error. Default: `false`.
- Added `addMarkdownDocumentation` parameter to `/plugins` and `/plugins/:pluginType` REST endpoints in order to request the optional Markdown documentation for plugins.
- Added SPARQL query timeout parameter in order to limit query execution times to 'Knowledge Graph' and 'SPARQL endpoint' datasets and to the SPARQL Select operator.
- RDF serialization: Tasks referenced in RDF serialization with `di:output` and `di:task` use the correct project task URIs instead of artificial URIs or literals.
- Complete Zip Stream support (replacing reliability on zip files only).
- MultiCsvZip are now BulkResourceDatasets.
- JDBC dataset: Removed database parameter. If required, the database needs to be specified as part of the JDBC URL, e.g., `jdbc:mysql://localhost:port/databaseName`. Appending connection parameters to the URL is supported now.
- Safer defaults:
    - SPARQL Endpoint and Knowledge Graph dataset: Do not clear graphs before execution to prevent accidental deletion of graphs.
    - Knowledge Graph dataset: Increase page size from 1000 to 100,000, because small page sizes lead to suboptimal execution performance.
    - SPARQL Update operator: Decrease batch size from 10 to 1.
- Upgraded to Apache Spark 2.3.3
- SQL datasets: If a URI attribute is specified, the URI will be added as a new column of that name.
- All projects are loaded first, before any cache or any other autorun activity is started. This improves loading when both the workspace provider and some caches load from the same database.
- Improved JDBC dataset performance for MySQL and MariaDB by using the 'Load Data' command to load a local CSV file into the database.
- Shipping with MariaDB JDBC driver.
- Redirect to original request URL instead of the start page after authenticating a user and logging in.
- Revised generation of table names in JDBC dataset (see documentation). Keep letter case of table names.
- Schedulers are always started by the super user, if the super user is configured.
- On start-up if DataPlatform is configured, DI will wait for DP to become healthy for a configurable amount of time. Parameters:
    - `eccencaDataPlatform.health.waitingTimeInSeconds`: Overall time in seconds DI should wait for DP to be up and healthy. Setting this to 0 will disable this check. Default: 60.
    - `eccencaDataPlatform.health.delayBetweenRetriesInSeconds`: Amount of time in seconds to wait between retries. Default: 5.
- Enhanced `JdbcDataset` and `SqlEndpoint` parameters and improve their descriptions.
- Suppress case changes in `SqlEndpoint` table names.

In addition to that, multiple performance and stability issues were solved.

## eccenca DataManager v19.10

This version of eccenca DataManager adds the following new features:

- New module `task`
    - Offers a direct resource actions. Interfaces only available by URL. See documentation for more details.
    - Path `/task/resource/create` allows to create a new resource by given graph and type.
- General
    - Config parameter `js.config.api.defaultTimeout` for default UI queries timeout.
    - Config parameter `js.config.resourceTable.timeoutDownload` for Resource Table timeout on download requests on Explore and Query modules.
    - Validation of mandatory fields in `shacline` view.
    - Add new property `shui:onUpdateUpdate` for `sh:NodeShape`.
- Module Explore
    - Config parameter `js.config.modules.explore.graphlist.whiteList` to filter specific graphs.
    - Config parameter `js.config.modules.explore.graphlist.internalGraphs` to hide specific graphs.
    - Config parameter `js.config.modules.explore.navigation.itemsPerPage` show items per page in navigation box.
    - Support for inverse property relations.
- Module Query
    - Config parameter `js.config.modules.query.timeout` for manual queries.
    - Config parameter `js.config.modules.query.graph` to define the graph were data is saved and requested.

In addition to that, these changes are shipped:

- General
    - Default pagination size of 20 elements for all Resource Tables.
    - Allow datatype `xsd:anyURI` for literals.
    - Upgraded to react 16.
- Module Explore
    - Merged graph view `RDFDoc` into 'resource details view'.
    - Renamed global search label.
    - Graph creation will add the type `void:Dataset` instead of `owl:Ontology`.
    - Use the label of the type of the instances for the name of the CSV file downloaded from the Resource Table.
    - Display the context graph in `properties` and `references` tables.
- Module Dataset
    - Adjusted position and tooltip of parameter `uriProperty` in 'Add data stepper'.
- Module Query
    - Use the dataset label for the name of the CSV file downloaded from the Resource Table.
- Module Login
    - Renew tokens when they expire.
- Module Administration
    - Allow to search in IRIs for list of readable and writeable graphs.

The following features have been removed in this release:

- Module Explore
    - Config parameter `js.config.modules.explore.graphlist.listQuery` which is now obsolete.
    - Config parameter `js.config.modules.explore.details.history` which is now obsolete as the feature is no longer supported.
    - 'History' tab.
- Module Sync also known as `SubscriptionManagement`.

In addition to that, multiple stability issues were solved.

## eccenca DataPlatform v19.10

This version of eccenca DataPlatform adds the following new features:

- SPARQL 1.1 Query endpoint
    - An `in-iris` property to the JSON `search` parameter to enable search over IRIs.
    - A `timeout` parameter which allows to configure the maximal amount of milliseconds that a query execution can run.
    - Support for Microsoft Excel (`.xlsx`) file download for `SELECT` queries.
- SPARQL 1.1 Update endpoint
    - A `timeout` parameter which allows to configure the maximal amount of milliseconds that an update execution can run (Stardog only).
- SPARQL 1.1 Graph Store Protocol
    - `multipart/form-data` support for HTTP PUT.
    - Added the `timeout` parameter, which allows to configure the maximal amount of milliseconds that a request execution should run.
    - Documentation for content negotiation by `format` query parameter.

The following features have been removed in this release:

- Data Sharing: A WebSub based Publish-Subscribe service for RDF named graphs.
- IoT Permissions Plugin: A plugin which enables the usage of the IoT Permissions Service API 2.
- OAuth 2.0 authorization server: Issues access tokens to a client after successfully authenticating a user.
- Authentication: User management via authentication providers as it was only needed by the OAuth 2.0 authorization server.

In addition to that, these changes are shipped:

- Stardog
    - Upgraded support to version 7.0.2.
    - Versioning does no longer work with Stardog 7.
    - Legacy versioning support for Stardog 6 (deprecated).
- OAuth 2.0: Resource protection is now mandatory (can no longer be disabled, use anonymous access instead).
- SPARQL 1.1 Query endpoint
    - The value of the `string` property of the JSON `search` parameter is now tokenized which means that each token will be searched separately. Only results matching all tokens will be returned.
    - Updated Spring Boot version from 1.5.21 to 1.5.22.

In addition to that, multiple performance and stability issues were solved.

## Migration Notes

With the removal of the OAuth 2.0 authorization server capability, many configuration properties have been changed.

- Removed
    - The properties `oauth2.clients.*` have been removed.
    - The properties `authentication.*` have been removed.
- Moved
    - The property `oauth2.jwt.signing.verificationKey` has been moved to `security.oauth2.resource.jwt.keyValue` .
    - The property `oauth2.anonymous` has been moved to `security.oauth2.resource.anonymous` .
    - The claims mapping properties under `oauth2.resourceServer.claimsMapping.*` have been moved to `security.oauth2.resource.jwt.claims.*` .
    - The properties `oauth2.authorizeRequests.*` to configure the resources to be protected by the resource server have been moved to `security.oauth2.resource.authorizeRequests.*` .
- Added
    - The value of the property `security.oauth2.resource.id`  (defaults to `dataplatform`) must be part of the `aud` (audience) claim in the JWT used to access a protected resource.

Don't forget to update your configuration accordingly.
For instance, assuming you have the following old configuration:

``` yaml
oauth2:
  anonymous: true
  clients:
    - id: client
      secret: secret
      grantTypes:
        - authorization_code
      redirectUris:
        - http://example.org/oauth/client
  jwt:
    enabled: true
      signing:
        verificationKey: |
          -----BEGIN PUBLIC KEY-----
          ...
          -----END PUBLIC KEY-----
  resourceServer:
    claimsMapping:
      username: 'preferred_username'
      clientId: 'azp'
      groups:
        key: 'groups'
```

The migrated properties should look like this:

``` yaml
security:
  oauth2:
    resource:
      anonymous: true # optional, defaults to `false`
      jwt:
        keyValue: |
          -----BEGIN PUBLIC KEY-----
          ...
          -----END PUBLIC KEY-----
     claims:
       username: preferred_username # optional, defaults to `preferred_username`
       groups: groups # optional, defaults to `groups`
       clientId: azp # optional, defaults to `azp`
```
