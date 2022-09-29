# Corporate Memory 20.03

Corporate Memory 20.03 is the first release in 2020.

The highlights of this release are:

- DataIntegration supports resources to be stored in an AWS S3 buckets.
- Rich [SHACL forms](../../explore-and-author/building-a-customized-user-interface/index.md) can be used for the creation of new resources.
- New BUILD module is introduced in DataManager to provide an experts shortcut to DataIntegration.
- SPARQL queries can now be used to define arbitrary result tables directly in [SHACL views](../../explore-and-author/building-a-customized-user-interface/index.md).
- Object properties can be switched between chips and resource table view in [SHACL views](../../explore-and-author/building-a-customized-user-interface/index.md).
- [cmemc](../../automate/cmemc-command-line-interface/index.md), our Corporate Memory Command Line Interface is now generally available

!!! warning

    With this release of Corporate Memory the DataIntegration, DataManager and DataPlatform configuration must be adapted according to the migration notes below.

This release delivers the following component versions:

- eccenca DataPlatform v20.03
- eccenca DataIntegration v20.03
- eccenca DataManager v20.03
- eccenca Corporate Memory Control (cmemc) v20.03

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v20.03


This version of eccenca DataIntegration adds the following new features:

- Support for additional value types for mapping targets (XML Schema date/time types, duration, etc.).
- More date types to `DateTypeParser`.
- Script operator can also be used in local execution mode.
- Operator search in mapping rule editor.
- Safe-mode that prevents access to external data systems, e.g. JDBC, SPARQL dataset:
    - Data access in executed workflows is not affected by the safe-mode.
    - Safe-mode can be toggled on and off at runtime in the UI.
    - To enable safe-mode, set following parameter in the config: `config.production.safeMode = true`.
- Config parameter `caches.config.enableAutoRun`, to enable/disable automatic execution of caches (default: `true`).
- Knowledge Graph File Upload Operator: Lets the user upload N-Triples files from the file repository into a DataPlatform graph.
- Support for file resource repositories on S3.

In addition to that, these changes are shipped:

- Improved password encryption
    - Using AES-256 instead of AES-128.
    - If no valid key has been configured in production mode, application does not start.
    - Better error messages, if key is invalid.
    - Secret AES-256 key is generated from the configured key using SHA256 hashing, allowing for arbitrarily long keys.
- Improved SQL writing performance for MariaDB and MySQL.
- Rework of the dataset view:
    - If a dataset is opened, the SPARQL (for RDF datasets) or table view (other datasets) is directly opened.
    - Added Material Design formatting.
    - Added scrollbars to tables with many columns.
- Active learning UI uses Material Design cards.
- the config endpoint `/core/config` is no longer available when running in production mode.
- If a mapping reads from a CSV column that does not exist, the mapping still executes successfully, but a warning is displayed in the execution report.
- With XML dataset in streaming mode default URIs are now created by using the row and column numbers of the XML element instead of a hash value.
- Reduce memory foot print of linking evaluation and execution.
- We are now sorting tasks in workspace by label.
- Now displaying the modification date in resource dialog.

In addition to that, multiple performance and stability issues were solved.


## eccenca DataManager v20.03

This version of eccenca DataManager adds the following new features:

- General
    - Blank nodes are filtered in shacline views.
    - Open external links in a new browser window.
    - `shui:valueQuery` for tabular representation
        - load of pre-defined queries as a `shui:valueQuery`.
    - `ResourceTable` now allow to resolve labels on download results.
- Access Control
    - Allow to create user and groups providing just a label.
- Module Explore
    - Shacl views now allow to switch object property links between chip and `ResourceTable` view
    - allow to add additional columns, search and filter using a `ResourceTable`.
    - `sh:path` is no longer mandatory on Shacl. One of both `sh:path` or `shui:valueQuery` is now mandatory.

In addition to that, these changes are shipped:

- General
    - Layout make better use of widescreen estate.
    - Show existing resources linked by an object property in a `ResourceTable` in edit mode.
- Module Explore
    - Navigation box uses search query only when a search term is present.
    - Creation of new resources can now make use of rich shacline forms.
    - Add new config parameter `modules.explore.navigation.defaultClass` that selects a default class EXPLORE should start with when `modules.explore.graphlist.defaultGraph` is defined.

The following features have been removed in this release:

- Datasets management
    - Config parameter `includeOAuthToken` is no longer used. DataIntegration authentication will be done in an iFrame instead.
- Access Control
    - Support for parameter `Requires client` has been removed from Access Control module.

In addition to that, multiple stability issues were solved.


## eccenca DataPlatform v20.03

This version of eccenca DataPlatform adds the following new features:

- SPARQL 1.1 Query endpoint
    - Support for non-string literals when using the `contains`, `startsWith` and `endsWith` filter functions.
    - Server side label resolution by using `resolveLabels`, which allows `NONE` and `LABEL` for resolving IRIs to literals.
    - The search parameter utilizes Stardog's built-in text match instead of `SPARQL CONTAINS` if a Stardog database is used. The search string is cleaned from special characters and english stop words and conjuncts all search terms.
- SPARQL 1.1 Update endpoint
    - `owl:imports` resolution on `USING`/`USING NAMED` clauses.
- `/info` and `/health` in addition to defaults `/actuator/info` and `/actuator/health` for backward compatibility.
- Show Redis status in application health if used as cache.
- The property `spring.security.oauth2.resourceserver.jwt.issuerUri` or `spring.security.oauth2.resourceserver.jwt.jwk-set-uri` must now be set in order to allow for JWT (signature) validation (see migration notes below).
- Access Conditions
    - Allow embedded creation of elements of type `eccauth:Account` or `eccauth:Group`.

In addition to that, these changes are shipped:

- Upgraded Stardog support to version 7.1.1.
- The default value of the property `spring.security.oauth2.resourceserver.jwt.claims.clientId` has been changed from `azp` to `clientId`.
- The properties under `security.oauth2.resource.jwt.claims.*` have been moved to `spring.security.oauth2.resourceserver.jwt.claims.*`.
- The property `security.oauth2.resource.anonymous` has been moved to `spring.security.oauth2.resourceserver.anonymous`.
- The property `http.cors.allowOriginRegex` has been moved to `http.cors.allowedOrigins`.
- The property `http.cors.allowMethods` has been moved to `http.cors.allowedMethods`.
- The property `http.cors.allowHeaders` has been moved to `http.cors.allowedHeaders`.
- The property `http.cors.exposeHeaders` has been moved to `http.cors.exposedHeaders`.

The following features have been removed in this release:

- Versioning support has been removed.
- Access Conditions
    - Support for `eccauth:requiresProtocol` and `eccauth:requiresClient` has been removed.
- The properties `security.oauth2` have been removed.
- The property `http.cors.enabled` has been removed.

In addition to that, multiple performance and stability issues were solved.

# eccenca Corporate Memory Control (cmemc) v20.03

This version of eccenca Corporate Memory Control (cmemc) adds the following new features:

- `config` command group, to `list`, `edit` and `check` configurations
- `graph` command group, to `list`, `import`, `export`, `delete` and `open` graphs
- `project` command group, to `list`, `import`, `export`, `create` and `delete` projects
- `query` command group, to `list` and `execute` local and remote SPARQL queries
- `workflow` command group, to `list`, `execute`, `open` or `inspect` workflows
- `workspace` command group, to `import` and `export` the workspace
- ability to work with SSL enabled deployments (add CA certs)


## Migration Notes

### DataIntegration

With v20.03 the following changes need to be made in your dataintegration.conf file when upgrading from v19.10:

- Remove the `play.crypto.secret` property, it has been deprecated with v20.03.
- Two properties need to be added: `play.http.secret.key` and `plugin.parameters.password.crypt.key`
    - both take an arbitrary alpha numerical string of minimum 16 characters length
    - depending on your deployment set them in your `production.conf` or `application.conf` DataIntegration configuration file

```
...
play.http.secret.key = "uiodshfoun78qwg8asd7gfasdasddfgn87gsn8fdsngasdfsngf8ds"
...
plugin.parameters.password.crypt.key = "uiodshfoun78qwg8"
...
```

!!! note

    In case you are deploying based on the DataIntegration docker images eccenca provides a `production.conf` configuration file needs to be used, the `dataintegration.conf` cannot be used to set the `play.http.secret.key` parameter.

!!! warning

    The property `plugin.parameters.password.crypt.key` is used to encrypt / decrypt the passwords stored with you project configuration (e.g. JDBC passwords). When you set or change this property, all passwords in your DataIntegration projects need to be re-entered.

### DataManager

With v20.03 a the new BUILD module is introduced. In order to enable and configure it add the following section to you `application.yml`:

``` yaml title="DataManager application.yml BUILD module configuration"
js.config.modules.build:
  enable: true
  url: "<DI-BASE_URI>/workspace"
```

Where `<DI-BASE-URI>` need to point to the DataIntegration URI (e.g. `https://host.domain.com/dataintegration`).

### DataPlatform

With v20.03 the following changes need to be made in your `application.yml` file when upgrading from v19.10:

- the key `http.cors.enabled` has been removed
- the key `http.cors.allowOriginRegex` has been renamed to `http.cors.allowedOrigins` and takes now a list of origins:

``` yaml title="DataPlatform application.yml http.cors configuration"
http:
  cors:
    allowedOrigins: # optional, defaults to allow all: "*"
      - "http://docker.local"
      - "https://docker.local"
```

- the key `security.oauth2.resource.jwt.keyValue` has been removed
- the key `spring.security.oauth2.resourceserver.jwt.jwk-set-uri` need to be specified.
    - Refer to your keycloaks Corporate Memory (cmem) realm "OpenID Endpoint Configuration" details where the relevant uri is listed as `jwks_uri`:

``` yaml title="DataPlatform application.yml spring.security configuration"
spring:
## OAuth2Properties
  security:
    oauth2:
      resourceserver:
        jwt:
          jwk-set-uri: http://keycloak:8080/auth/realms/cmem/protocol/openid-connect/certs
```

