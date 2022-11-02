
## License

By default, DataPlatform is subject to the eccenca free Personal, Evaluation and Development License Agreement (PEDAL), a license intended for non-commercial usage. When your delivery includes a dedicated license file, you have to configure DataPlatform to enable your license. 
To change the default configuration, you have several options. If the properties under license are not provided the default license included (PEDAL) is used.

In case a dedicated license file is used, different configuration options can overwrite each other. The license is read in the following sequence:

1. license.key property
2. license.file property
3. license.asc file in the same folder, where the application is started from (in Standalone Mode)
4. Fallback to eccenca free Personal, Evaluation and Development License Agreement (PEDAL)


***Property: license.key***

Use this property to specify the license key as a YAML multiline string value of the license.key property.


```yaml
key: |
    -----BEGIN PGP MESSAGE-----
    ...
    ...
    -----END PGP MESSAGE-----
```


| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | PGP Key (Message) |
  | Conflicts with | license.file |
| Environment | LICENSE_KEY |

***Property: license.file***

Use this property to specify the location of the license file

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | location of the license file |
  | Conflicts with | license.key |
| Environment | LICENSE_FILE |

## General platform settings for DataPlatform

This section provides general configuration settings.


### Caching

DataPlatform provides caching support which is enabled by default with an in-memory Caffeine cache.

***Property: spring.cache.type***

Use this property to define the type of cache to use. The default type (CAFFEINE) provides an in-memory cache suitable for simple standalone installations or test deployments.

To disable caching, set the type to NONE (not recommended).


| Category | Value |
|--- | ---: |
| Default | CAFFEINE |
| Required | true |
| Valid values | CAFFEINE, REDIS, NONE |
| Environment | SPRING_CACHE_TYPE |

#### Redis

Set REDIS to use a Redis cache. Use this cache type in scenarios with higher scalability demands or clustered setups. If this cache type is used, you must set the spring.cache.redis.host and spring.cache.redis.port properties, too.

Configuration example:

```yaml
spring:
  cache:
    type: REDIS
  redis:
    host: localhost
    port: 6379
```


***Property: spring.cache.redis.host***

Use this property to set the hostname where the Redis cache is available.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | only if spring.cache.type=REDIS provided |
| Valid values | string |
| Environment | SPRING_CACHE_REDIS_HOST |

***Property: spring.cache.redis.port***

Use this property to set the TCP port where the Redis cache is available.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | only if spring.cache.type=REDIS provided |
| Valid values | string |
| Environment | SPRING_CACHE_REDIS_PORT |

Multipart upload limits config
You may need to set the following parameter values to 2048MB for implementations
that cannot handle large requests


***Property: spring.servlet.multipart.max-file-size***

Use this property to define the maximum size of an uploaded file in number of bytes. Values can use the suffixed "MB" or "KB" (e.g. '1024MB').

**Note:** If DataPlatform is deployed in a Servlet container, make sure to also configure support for large file sizes.


| Category | Value |
|--- | ---: |
| Default | 4096MB |
| Required | false |
| Valid values | string |
| Environment | SPRING_SERVLET_MULTIPART_MAX_FILE_SIZE |

***Property: spring.servlet.multipart.max-request-size***

Use this property to define the maximum size of HTTP request in number of bytes. Values can use the suffixed "MB" or "KB" (e.g. '1024MB').

| Category | Value |
|--- | ---: |
| Default | 4096MB |
| Required | false |
| Valid values | string |
| Environment | SPRING_SERVLET_MULTIPART_MAX_REQUEST_SIZE |

Spring Cloud configuration

***Property: spring.cloud.config.enabled***


| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | string |
| Environment | SPRING_CLOUD_CONFIG_ENABLED |

Spring Sleuth Zipkin exporter configuration (tracing)

***Property: spring.zipkin.base-url***


| Category | Value |
|--- | ---: |
| Default | http://localhost:9411/ |
| Required | false |
| Valid values | string |
| Environment | SPRING_ZIPKIN_BASE_URL |

***Property: spring.zipkin.enabled***

Whether the export to zipkin is enabled

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | string |
| Environment | SPRING_ZIPKIN_ENABLED |

The service name for DataPlatform under which the traces are stored

***Property: spring.zipkin.service.name***


| Category | Value |
|--- | ---: |
| Default | DP |
| Required | false |
| Valid values | string |
| Environment | SPRING_ZIPKIN_SERVICE_NAME |

Spring Cloud Sleuth distributed tracing. This generated IDs for queries/updates and all operations in DataPlatform. Write to tracing exporter s. spring.zipkin.

***Property: spring.sleuth.enabled***

Whether tracing is enabled. If not then IDs for i.e. queries are generated via UUID mechanism. Backend store "neptune" is not compatible with tracing enabled.

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | string |
| Environment | SPRING_SLEUTH_ENABLED |

## OpenAPI Specification and Swagger UI

You can activate endpoints to expose an OpenAPI compliant specification of the available DataPlatform APIs. Developers can make use of this information to understand the API and to bootstrap client integration code.

The servers URLs can be customized by setting the environment variable OPENAPI_SERVER_URLS on the machine or in the docker container that runs DataManager:

```bash
export OPENAPI_SERVER_URLS="https://my-custom.domain.com:443/dataplatform"
```

Configuration example:

```yaml
springdoc:
  swagger-ui:
   enabled: true
 api-docs:
   enabled: true
```


***Property: springdoc.api-docs.enabled***

Use this property to enable and expose endpoint that provide the OpenAPI compliant specification of the DataPlatform APIs. The following endpoints will become available when this option is set to true:

- <DATA_PLATFORM_URI>/v3/api-docs
- <DATA_PLATFORM_URI>/v3/api-docs.yaml
- <DATA_PLATFORM_URI>/v3/api-docs/swagger-config


| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | SPRINGDOC_API_DOCS_ENABLED |

***Property: springdoc.swagger-ui.enabled***

Use this property to enable and expose a Swagger UI browser interface that can be used to explore and interact with the APIs. The following endpoints will become available when this option is set to true:

- <DATA_PLATFORM_URI>/swagger-ui.html


| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | SPRINGDOC_SWAGGER_UI_ENABLED |

## Cross-origin resource sharing (CORS)

DataPlatform supports Cross-origin resource sharing (CORS).

Configuration example:

```yaml
http:
  cors:
    allowedOrigins:
    - http://example.org
    - https://example.com
```


***Property: http.cors.allowedOrigins***

Use this property to define the list of allowed origins. The values must be either specific origins, e.g. http://example.org, or * for all origins.

| Category | Value |
|--- | ---: |
| Default | [*] |
| Required | false |
| Valid values | list of strings |
| Environment | HTTP_CORS_ALLOWEDORIGINS |

***Property: http.cors.allowedMethods***

Use this property to define the list of allowed HTTP methods. The special value * allows all methods.

| Category | Value |
|--- | ---: |
| Default | [OPTIONS, HEAD, GET, POST, PUT, DELETE, PATCH] |
| Required | false |
| Valid values | list of strings (of OPTIONS, HEAD, GET, POST,  PUT, DELETE, PATCH) |
| Environment | HTTP_CORS_ALLOWEDMETHODS |

***Property: http.cors.allowedHeaders***

Use this property to define the list of allowed HTTP headers. The special value * may be used to allow all headers.

| Category | Value |
|--- | ---: |
| Default | [Authorization, X-Requested-With, Content-Type, Content-Length, ETag] |
| Required | false |
| Valid values | list of strings |
| Environment | HTTP_CORS_ALLOWEDHEADERS |

***Property: http.cors.exposedHeaders***

Use this property to define the list of headers that an actual response might have and can be exposed.

| Category | Value |
|--- | ---: |
| Default | [WWW-Authenticate, Link, ETag] |
| Required | false |
| Valid values | list of strings |
| Environment | HTTP_CORS_EXPOSEDHEADERS |

***Property: http.cors.allowCredentials***

Use this property to define whether the browser should send credentials, such as cookies along with cross domain requests.

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | HTTP_CORS_ALLOWCREDENTIALS |

***Property: http.cors.maxAge***

Use this property to define how long in seconds the response from a pre-flight request can be cached by clients.

| Category | Value |
|--- | ---: |
| Default | 3600 |
| Required | false |
| Valid values | non-negative integer |
| Environment | HTTP_CORS_MAXAGE |

## HTTP client settings

Java 11 HTTP client settings for HTTP access to the backend store.


***Property: httpclient.connectionPoolSize***

The maximum number of connections to keep in the HTTP/1.1 keep alive cache. A value of 0 means that the cache is unbounded

| Category | Value |
|--- | ---: |
| Default | 200 |
| Required | false |
| Valid values | string |
| Environment | HTTPCLIENT_CONNECTIONPOOLSIZE |

***Property: httpclient.keepalive.timeout***

The number of seconds to keep idle HTTP/1.1 connections alive in the keep alive cache

| Category | Value |
|--- | ---: |
| Default | 1200 |
| Required | false |
| Valid values | string |
| Environment | HTTPCLIENT_KEEPALIVE_TIMEOUT |

## Authorization

DataPlatform supports authorization of RDF named graphs and actions. Authorization for clients and/or users is specified by the access conditions model which is described in section Access conditions. You can configure root access for a specific group of users who are given unrestricted access regardless of the defined access conditions. Refer to section Root Access for more information.

***Property: authorization.rootAccess***

Use this property to enable or disable root access.
DataPlatform allows root access for a specific administrator group (see property authorization.abox.adminGroup). You can toggle root access using the property authorization.rootAccess. Regardless of the access conditions declared in the access conditions model (see Access conditions), all members of the administrator group are permitted to read and write all graphs of all endpoints and are allowed to perform all actions.

For example, the following configuration grants root access to any user in the group admins:

```yaml
authorization:
  rootAccess: true
  abox:
    adminGroup: admins
```


| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | boolean |
| Environment | AUTHORIZATION_ROOTACCESS |

Use the following configuration options to specify values used by DataPlatform when working with RDF data, such as default URIs and prefixes.

***Property: authorization.abox.adminGroup***

Use this property to configure the group that gets root access if enabled (see section Root access).

| Category | Value |
|--- | ---: |
| Default | elds-admins |
| Required | false |
| Valid values | string |
| Environment | AUTHORIZATION_ABOX_ADMINGROUP |

***Property: authorization.abox.publicGroup***

Use this property to configure the URI of the public user group (see section Public access).
**Note:** If you change this property, you also need to change existing URI descriptions and existing access conditions.


| Category | Value |
|--- | ---: |
| Default | urn:elds-backend-public-group |
| Required | false |
| Valid values | string |
| Environment | AUTHORIZATION_ABOX_PUBLICGROUP |

***Property: authorization.abox.anonymousUser***

Use this property to configure the URI of the public user (see section Public access).
**Note:** If you change this property, you also need to change existing URI descriptions and existing access conditions.


| Category | Value |
|--- | ---: |
| Default | urn:elds-backend-anonymous-user |
| Required | false |
| Valid values | string |
| Environment | AUTHORIZATION_ABOX_ANONYMOUSUSER |

***Property: authorization.abox.prefix***

Use this property to set the namespace of URIs created by DataPlatform.
**Note:** If you change this property, you also need to change the corresponding shape definitions for access conditions (more precisely, the URI template), as well as existing URI descriptions and existing access conditions.


| Category | Value |
|--- | ---: |
| Default | https://ns.eccenca.com/ |
| Required | false |
| Valid values | string |
| Environment | AUTHORIZATION_ABOX_PREFIX |

#### Access conditions

**Note:** The access conditions model is empty if you provide no configuration in this section.

Access conditions are defined in the access conditions model, an RDF named graph containing instances of the OWL class eccauth:AccessCondition defined by the eLDS Auth schema Ontology.

An access condition consists of the following elements:

    - type: Only RDF resources of type eccauth:AccessCondition are valid access conditions.
    - requirements: Conditions to be fulfilled by the logged-in user such as group membership. All conditions must be fulfilled, otherwise the access condition is not fulfilled.
    - grants: Actions or data the user is allowed to execute and/or access such as accessing a specific API or reading a graph.

For simplicity, the Turtle serialization syntax is used in the following examples, but you can define the access conditions model in any RDF serialization.


***Property: authorization.abox.accessConditions.url***

Use this property to set the URL of the access conditions model file. This can be either a remote (http://...) or a local (file:...) .rdf file. Refer to section Access conditions for more information on the access conditions model.


| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | AUTHORIZATION_ABOX_ACCESSCONDITIONS_URL |

***Property: authorization.abox.accessConditions.graph***

Use this property to set the graph containing the access conditions model.
**Note:** If you change this property, you also need to change the corresponding shape definitions for access conditions (more precisely, the UI SPARQL queries).


| Category | Value |
|--- | ---: |
| Default | urn:elds-backend-access-conditions-graph |
| Required | false |
| Valid values | string |
  | Conflicts with | url |
| Environment | AUTHORIZATION_ABOX_ACCESSCONDITIONS_GRAPH |

## SPARQL endpoints

SPARQL endpoints declare how DataPlatform connects to a SPARQL-capable store or service. This includes stores that are capable of reading and writing RDF such as Virtuoso as well as read-only services like remote SPARQL HTTP endpoints (e.g. DBpedia).

With the default configuration, DataPlatform uses an in-memory database. This means, that no persistent storage is available, unless a store supporting data persistence is configured.

The following example showcases a setup in which for each Resource all rdfs:label, Literals with language es, then en and in the end those without a language are evaluated. 
If nothing matches here, skos:prefLabel is examined in the same way

```yaml
proxy:
  endpointIds:
    - my_stardog
  labelProperties:
    - "http://www.w3.org/2000/01/rdf-schema#label"
    - "http://www.w3.org/2004/02/skos/core#prefLabel"
  languagePreferences:
    - "es"
    - "en"
    - ""
```


***Property: proxy.defaultBaseIri***

Base IRI for this Corporate Memory instance. If not set falls back to environment variable DEPLOY_BASE_URL, further fallback to https://fallback.eccenca.com/

| Category | Value |
|--- | ---: |
| Default | https://fallback.eccenca.com/ |
| Required | false |
| Valid values | URI |
| Environment | PROXY_DEFAULTBASEIRI |

***Property: proxy.labelProperties***

Use this property to specify which RDF properties should be used to provide label values when matching IRIs against a search term during rewriting SELECT-queries.
**Note:** This configuration property affects modification of SELECT-queries for search triggered by the search-string query parameter. Results of SELECT-queries when the resolveLabels property is set to LABELS


| Category | Value |
|--- | ---: |
| Default | [http://www.w3.org/2004/02/skos/core#prefLabel, http://www.w3.org/2000/01/rdf-schema#label, http://purl.org/dc/terms/title, http://www.w3.org/ns/shacl#name] |
| Required | false |
| Valid values | list of Properties |
| Environment | PROXY_LABELPROPERTIES |

***Property: proxy.descriptionProperties***

Use this property to specify which RDF properties should be used to provide description values when matching IRIs against a search term during rewriting SELECT-queries.
**Note:** This configuration property affects modification of SELECT-queries for search triggered by the search-string query parameter. Results of SELECT-queries when the resolveLabels property is set to LABELS


| Category | Value |
|--- | ---: |
| Default | [http://purl.org/dc/terms/description, http://www.w3.org/2000/01/rdf-schema#comment] |
| Required | false |
| Valid values | list of Properties |
| Environment | PROXY_DESCRIPTIONPROPERTIES |

***Property: proxy.languagePreferences***

Specifies base language preferences for this instance. 

**Note:** This configuration property affects results of SELECT-queries when the resolveLabels property is set to LABELS.


| Category | Value |
|--- | ---: |
| Default | [de, en, ] |
| Required | false |
| Valid values | string |
| Environment | PROXY_LANGUAGEPREFERENCES |

***Property: proxy.languagePreferencesAnyLangFallback***

Allows the fallback to ignoring the languagePreferences, in case none of the configured match the data.

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | string |
| Environment | PROXY_LANGUAGEPREFERENCESANYLANGFALLBACK |

***Property: proxy.maxCBDDepth***

The Concise Boundary Description is used for viewing and editing resoures.
By default up to a max of 5 Blank nodes are traversed for calculation.
Increasing the max fetch will support deeper constructs, but will also add to loading time.


| Category | Value |
|--- | ---: |
| Default | 5 |
| Required | false |
| Valid values | string |
| Environment | PROXY_MAXCBDDEPTH |

***Property: proxy.shapedMaxValueCount***

Maximum Values for shaped Resources
When a resource is shaped by shacl forms, *shapedMaxValueCount* limits the number of values
returned per `shacl:PropertyShape`. The default needs to be larger than the DataManager setting for
for 'propertyLimit', which is up to 25. Changing this value allows custom
endpoints to fetch more data. Increasing this value will increase response time


| Category | Value |
|--- | ---: |
| Default | 26 |
| Required | false |
| Valid values | string |
| Environment | PROXY_SHAPEDMAXVALUECOUNT |

***Property: proxy.cacheInvalidationCron***

Cache Invalidation Frequency - Caches in DataPlatform are invalidated on updates and in regular intervals. This allows setting a cron for a scheduled eviction of all caches

| Category | Value |
|--- | ---: |
| Default | 0 */30 * * * * |
| Required | false |
| Valid values | Cron setting according to https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling-cron-expression |
| Environment | PROXY_CACHEINVALIDATIONCRON |

***Property: proxy.cacheSelectiveInvalidation***

Indicates whether the DataPlatform caches should selectively invalidate based upon the result of the done operations (insofar as determinable) or not

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | boolean |
| Environment | PROXY_CACHESELECTIVEINVALIDATION |

***Property: proxy.queryMonitorMaxMemoryInMb***

Maximum memory entries in the query monitor can take in the heap space. The actual usage is an estimated usage only!

| Category | Value |
|--- | ---: |
| Default | 30 |
| Required | false |
| Valid values | Value in MB |
| Environment | PROXY_QUERYMONITORMAXMEMORYINMB |

***Property: proxy.fetchValuesStrategy***

Value Fetch Strategy
Determines how the Knowledge Graph is walked for values for specific resources.
Used for resolving titles & comments and loading shaped resources.
- RESOURCE_IN_VALUES uses a SPARQL `VALUES (?resource ) { (:resource1)(:resource2)}`
- FILTER_ONLY Uses SPARQL uses a SPARQL `FILTER (?resource in (:resource1, :resource2))`


| Category | Value |
|--- | ---: |
| Default | RESOURCE_IN_VALUES |
| Required | false |
| Valid values | RESOURCE_IN_VALUES, FILTER_ONLY |
| Environment | PROXY_FETCHVALUESSTRATEGY |

## Syncing graph via git repositories

DataPlatform can sync graphs between git repositories and the backend store.
Changes of graphs in the backend are transferred to the git repository on each update / write of the graph.
Changes of the graph in the git repository are synchronized to the store on a scheduled basis.
<!--A git repository can be configured for the graph in the graph configuration. -->
<!--If no repository is configured the configured repository from the DataPlatform configuration is being used. -->
Only HTTP git repositories with basic authentication can be used.
A local public bare repository reachable from DataPlatform can be used in the DataPlatform configuration (for testing purposes).

For details how to provide the correct git authentication refer to <https://www.codeaffine.com/2014/12/09/jgit-authentication/>.

!!! note
  All properties need to be written as camel case (e.g. "gitSync"), hyphens as separators must not be used.

An example git DataPlatform configuration using a gitlab git repository looks like:

```yaml
gitSync:
  enabled: true
  remoteUrl: https://gitlab-ci-token:abcMyCiTokenxy5@gitlab.example.com/username/gitsync.git
  user: username
  password: abcMyCiTokenxy5
  branch: master
  scheduledPullCron: "0 */5 * * * *"
```


***Property: gitSync.enabled***

Activates / Deactivates git graph sync feature

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | GITSYNC_ENABLED |

***Property: gitSync.dataFolder***

The folder inside the repositories where Corporate Memory places the synchronized files

| Category | Value |
|--- | ---: |
| Default | data |
| Required | false |
| Valid values | string |
| Environment | GITSYNC_DATAFOLDER |

***Property: gitSync.remoteUrl***

A remote git repository (http, local) - configured http repositories in graph configuration take precedence over this

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | HTTP or local repository which can be reached from DataPlatform |
| Environment | GITSYNC_REMOTEURL |

***Property: gitSync.branch***

The main branch on which the git sync takes place - the sync may create new branches on conflict. The branch must exist before using the feature.

| Category | Value |
|--- | ---: |
| Default | main |
| Required | false |
| Valid values | An existing branch in the repository |
| Environment | GITSYNC_BRANCH |

***Property: gitSync.user***

The git username for simple user/password authentification - may be empty for local repository (s. remoteUrl) w/o authentification

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | Existing git repository user |
| Environment | GITSYNC_USER |

***Property: gitSync.password***

The git password for simple user/password authentification - may be empty for local repository (s. remoteUrl) w/o authentification

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | Existing git repository password |
| Environment | GITSYNC_PASSWORD |

***Property: gitSync.committerName***

The committer name which appears in the commit message on system commits

| Category | Value |
|--- | ---: |
| Default | eccenca DataPlatform |
| Required | false |
| Valid values | string |
| Environment | GITSYNC_COMMITTERNAME |

***Property: gitSync.committerEmail***

The committer email which appears in the commit message  on system commits

| Category | Value |
|--- | ---: |
| Default | info@eccenca.com |
| Required | false |
| Valid values | string |
| Environment | GITSYNC_COMMITTEREMAIL |

***Property: gitSync.scheduledPullCron***

Schedules Pull Frequency - Configured git repositories for sync are pulled regularly to check for external updates of synchronized graphs. This setting sets the frequency of the pull.

| Category | Value |
|--- | ---: |
| Default | 0 */30 * * * * |
| Required | false |
| Valid values | Cron setting according to https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling-cron-expression |
| Environment | GITSYNC_SCHEDULEDPULLCRON |

## Application logging

By default, DataPlatform only logs to the console. You can change the log level or configure logging into a file.

There are multiple levels of logging you can choose from that are explained in the table below.

Available log levels are: TRACE, DEBUG, INFO, WARN, ERROR, FATAL and OFF.
The default root log level is WARN.
It is also possible to set the log level per package.
Per default only console output is activated. To enable file output,
specify a log file (auto-rotating, 10Mb file size).
Possible log settings for specific modules:
Query Logging: com.eccenca.elds.backend.sparql.query.logging: DEBUG

The levels can also be configured on runtime via the loggers HTTP endpoint as described in section Application loggers of the Developer Manual.

```yaml
logging:
  level:
    root: WARN
    com.eccenca.elds.backend: DEBUG
    org.springframework: INFO
  file: /var/logs/dataplatform.log
```


Use these properties to specify where you want to store your logging file. Specifying a file leads to both, logging to standard output and the file.
File output creates an auto-rotating file with 10 MB file size each.


***Property: logging.file.name***

Log file name (for instance, `myapp.log`). Names can be an exact location or relative to the current directory.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string (file name) - empty to disable file output |
| Environment | LOGGING_FILE_NAME |

***Property: logging.file.path***

Location of the log file. For instance, `/var/log`.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string (file path) - empty to disable file output |
| Environment | LOGGING_FILE_PATH |

***Property: logging.config***

Logging for DataPlatform can also be configured with Logback, which, for example, allows a more granular control on file rolling strategies. For further information on configuration options, refer to the Logback’s Configuration manual section and the Spring Boot’s Configure Logback for Logging manual section.

Use this property to specify where the Logback configuration is located.

```yaml
logging:
  configuration: ELDS_HOME/etc/dataplatform/logback.xml
```


| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string (file path) |
| Environment | LOGGING_CONFIG |

***Property: logging.level.audit***


| Category | Value |
|--- | ---: |
| Default | INFO |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_AUDIT |

***Property: logging.level.com.eccenca.elds.backend***


| Category | Value |
|--- | ---: |
| Default | INFO |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND |

***Property: logging.level.org.springframework***


| Category | Value |
|--- | ---: |
| Default | WARN |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_ORG_SPRINGFRAMEWORK |

***Property: logging.level.com.eccenca.elds.backend.webapp.web.filter.SimpleCorsFilter***


| Category | Value |
|--- | ---: |
| Default | WARN |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_WEBAPP_WEB_FILTER_SIMPLECORSFILTER |

***Property: logging.level.com.eccenca.elds.backend.webapp.web.GlobalControllerExceptionHandler***


| Category | Value |
|--- | ---: |
| Default | TRACE |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_WEBAPP_WEB_GLOBALCONTROLLEREXCEPTIONHANDLER |

***Property: logging.level.com.eccenca.elds.backend.stardog.StardogTemplate***


| Category | Value |
|--- | ---: |
| Default | INFO |
| Required | false |
| Valid values | string |
| Environment | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_STARDOG_STARDOGTEMPLATE |

## Audit trail logging

DataPlatform is able to log the access of each user to named graphs in form of an audit trail log under the logger name audit.

```yaml
auditTrail:
  enabled: true
  auditedGraphs:
  - "example.org/data"
  - "aksw.org"
```


***Property: audit-trail.enabled***

Use this property to enable logging of read and write access to every graph access. If auditTrail.auditedGraphs is specified, only those graphs are logged.
**Note:** If audit trail logging is enabled, RDF upload over the Graph Store Protocol interface is limited to triple formats. Any attempt to upload a quad format results in an HTTP 415 error.


| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | AUDIT_TRAIL_ENABLED |

***Property: audit-trail.auditedGraphs***

Use this property to specify graphs whose read and write access you want to be logged. Omit this value to log access to all graphs.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | List of graph IRIs |
| Environment | AUDIT_TRAIL_AUDITEDGRAPHS |

Limits the size of the query response

***Property: sparql.query.limit***


| Category | Value |
|--- | ---: |
| Default | 100000 |
| Required | false |
| Valid values | string |
| Environment | SPARQL_QUERY_LIMIT |

## Embedded Tomcat

The URL under which DataPlatform is accessible has the following form: PROTOCOL://HOST:PORT/CONTEXT_PATH
where:

    - PROTOCOL: http or https depending on SSL configuration (see section SSL support)
    - HOST: The hostname pointing to the server where DataPlatform is installed
    - PORT: The TCP port where the embedded server is available (see the property server.port)
    - CONTEXT_PATH: The context path under which DataPlatform is available (see the property server.servlet.contextPath)

```yaml
server:
  port: 9090
  servlet:
    contextPath: /dataplatform
```


***Property: server.port***

Use this property to set the TCP port where the embedded server is available.

| Category | Value |
|--- | ---: |
| Default | 9090 |
| Required | false |
| Valid values | integer |
| Environment | SERVER_PORT |

***Property: server.servlet.contextPath***

Use this property to define the context path under which DataPlatform is available. If this property is provided, use a leading slash.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | SERVER_SERVLET_CONTEXTPATH |

### HTTPS support for standalone mode

If DataPlatform is executed in standalone mode (see Standalone), the embedded servlet container can be configured to support one-way (server certification) or two-way (server and client certification) SSL. A KeyStore is required for one-way SSL and both a KeyStore as well as a TrustStore are required for two-way SSL.

Refer to the Oracle documentation to see how to create KeyStore and TrustStore files.

Configuration example:

```yaml
server:
  ssl:
    key-store: ./key-store.jks
    key-store-password: jks-password
    client-auth: NEED
```


***Property: server.ssl.key-store***

Use this property to define the path to the KeyStore used for one-way or two-way SSL authentication.

In case of two-way authentication, a TrustStore must also be configured. This configuration must be provided as Java system properties either directly in the execution command or as part of the JAVA_TOOL_OPTIONS environment variable, e.g.:

```bash
JAVA_TOOL_OPTIONS=-Djavax.net.ssl.trustStore=path_to_trust_store.jks -Djavax.net.ssl.trustStorePassword=trust_store_password (ADD TO EXISTING JAVA_TOOL_OPTIONS)
```


| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | SERVER_SSL_KEY_STORE |

***Property: server.ssl.key-store-password***

Use this property to set the password to unlock the KeyStore used for one-way or two-way SSL authentication.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | SERVER_SSL_KEY_STORE_PASSWORD |

***Property: server.ssl.client-auth***

Use this property to define the client identification policy.

If WANT is set, client identification is optional. If NEED is set, client identification is mandatory, so unauthenticated clients are refused.


| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | none, NEED, WANT |
| Environment | SERVER_SSL_CLIENT_AUTH |

### HTTPS support for proxy deployment

If DataPlatform is running behind a proxy server (e.g. Apache) then you must use all of the following properties to enforce HTTPS.

Configuration recommendation:

```yaml
  server:
    tomcat:
     remoteIpHeader: x-forwarded-for
     protocolHeader: x-forwarded-proto

    security:
      requireSsl: true
```

**Note:** This configuration recommendation provides settings for headers most commonly used by proxies. Make sure to add all three properties in order to enforce HTTPS.


***Property: server.tomcat.remoteIpHeader***

Use this property to set the request header which is required to identify the originating IP address of the client connecting to DataPlatform through an HTTP proxy.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | SERVER_TOMCAT_REMOTEIPHEADER |

***Property: server.tomcat.protocolHeader***

Use this property to set the request header which is required to identify the originating protocol of an HTTP request through an HTTP proxy.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | SERVER_TOMCAT_PROTOCOLHEADER |

## Scheduler for asynchronous operations

Schedulers Configuration (Thread Pools) for asynchronous operations like background file uploads

***Property: scheduler.bulkLoadPoolSize***

Bulk upload Pool Size - Limits how many (bulk/large) uploads via GSP / bulk load can be run in parallel in file upload.

| Category | Value |
|--- | ---: |
| Default | 1 |
| Required | false |
| Valid values | integer |
| Environment | SCHEDULER_BULKLOADPOOLSIZE |

***Property: scheduler.analyticalPoolSize***

Limits how many analytical requests can be run in parallel. Analytical requests  can have longer runtimes than retrieval requests.

| Category | Value |
|--- | ---: |
| Default | 10 |
| Required | false |
| Valid values | integer |
| Environment | SCHEDULER_ANALYTICALPOOLSIZE |

## Asynchronous file uploads

Files can be asynchronously uploaded to the backend store in multiple steps which include an analysis of the uploaded file. 
Please s. API documentation under /api/upload/ for further information.


***Property: files.maxStorageSingleFileSizeMb***

Maximum size of one stored file (as uploaded i.e. can also be compressed size)
Value in Mb


| Category | Value |
|--- | ---: |
| Default | 3000 |
| Required | false |
| Valid values | string |
| Environment | FILES_MAXSTORAGESINGLEFILESIZEMB |

***Property: files.minStorageTempSpaceLeftMb***

Minimum storage space left on temp device of DataPlatform for file uploads
Value in Mb


| Category | Value |
|--- | ---: |
| Default | 3000 |
| Required | false |
| Valid values | string |
| Environment | FILES_MINSTORAGETEMPSPACELEFTMB |

***Property: files.maintenanceExpirationDuration***

Cron setting for housekeeping / maintenance job
Stored files and saved analysis will be deleted if older than maintenanceExpirationDuration


| Category | Value |
|--- | ---: |
| Default | P1D |
| Required | false |
| Valid values | string |
| Environment | FILES_MAINTENANCEEXPIRATIONDURATION |

***Property: files.maintenanceCron***

Cron setting for housekeeping / maintenance job
Stored files and saved analysis will be deleted if older than maintenanceExpirationDuration


| Category | Value |
|--- | ---: |
| Default | 0 0 1 * * ? |
| Required | false |
| Valid values | string |
| Environment | FILES_MAINTENANCECRON |

## Store configuration

Store properties for connecting to a triple store backend. Please see specific sections in documentation for each backend.

***Property: store.type***

One of the supported types of backends DataPlatform can connect to

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | true |
| Valid values | MEMORY, HTTP, GRAPHDB, STARDOG, VIRTUOSO, NEPTUNE |
| Environment | STORE_TYPE |

***Property: store.owlImportsResolution***

Use this property to enable OWL imports resolution

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | string |
| Environment | STORE_OWLIMPORTSRESOLUTION |

***Property: store.authorization***

Strategies to realize authorization for an RDF endpoint

| Category | Value |
|--- | ---: |
| Default | none |
| Required | false |
| Valid values | NONE, REWRITE_FROM |
| Environment | STORE_AUTHORIZATION |

***Property: store.queryTimeoutGeneral***

Query timeout as duration which is active if no timeout in request has been set

| Category | Value |
|--- | ---: |
| Default | PT1H |
| Required | false |
| Valid values | ISO 8601 duration format |
| Environment | STORE_QUERYTIMEOUTGENERAL |

