---
hide:
  - toc
---

| Property | Environment | Default | Required | Valid values|
| --- | --- | --- | --- | --- |
| license.key | LICENSE_KEY  | *none*| false | PGP Key (Message) |
| license.file | LICENSE_FILE  | *none*| false | location of the license file |
| spring.cache.type | SPRING_CACHE_TYPE  | CAFFEINE| true | CAFFEINE, REDIS, NONE |
| spring.cache.redis.host | SPRING_CACHE_REDIS_HOST  | *none*| only if spring.cache.type=REDIS provided | string |
| spring.cache.redis.port | SPRING_CACHE_REDIS_PORT  | *none*| only if spring.cache.type=REDIS provided | string |
| spring.servlet.multipart.max-file-size | SPRING_SERVLET_MULTIPART_MAX_FILE_SIZE  | 4096MB| false | string |
| spring.servlet.multipart.max-request-size | SPRING_SERVLET_MULTIPART_MAX_REQUEST_SIZE  | 4096MB| false | string |
| spring.cloud.config.enabled | SPRING_CLOUD_CONFIG_ENABLED  | false| false | string |
| spring.zipkin.base-url | SPRING_ZIPKIN_BASE_URL  | <http://localhost:9411/>| false | string |
| spring.zipkin.enabled | SPRING_ZIPKIN_ENABLED  | false| false | string |
| spring.zipkin.service.name | SPRING_ZIPKIN_SERVICE_NAME  | DP| false | string |
| spring.sleuth.enabled | SPRING_SLEUTH_ENABLED  | true| false | string |
| springdoc.api-docs.enabled | SPRINGDOC_API_DOCS_ENABLED  | false| false | boolean |
| springdoc.swagger-ui.enabled | SPRINGDOC_SWAGGER_UI_ENABLED  | false| false | boolean |
| http.cors.allowedOrigins | HTTP_CORS_ALLOWEDORIGINS  | [*]| false | list of strings |
| http.cors.allowedMethods | HTTP_CORS_ALLOWEDMETHODS  | [OPTIONS, HEAD, GET, POST, PUT, DELETE, PATCH]| false | list of strings (of OPTIONS, HEAD, GET, POST,  PUT, DELETE, PATCH) |
| http.cors.allowedHeaders | HTTP_CORS_ALLOWEDHEADERS  | [Authorization, X-Requested-With, Content-Type, Content-Length, ETag]| false | list of strings |
| http.cors.exposedHeaders | HTTP_CORS_EXPOSEDHEADERS  | [WWW-Authenticate, Link, ETag]| false | list of strings |
| http.cors.allowCredentials | HTTP_CORS_ALLOWCREDENTIALS  | false| false | boolean |
| http.cors.maxAge | HTTP_CORS_MAXAGE  | 3600| false | non-negative integer |
| httpclient.connectionPoolSize | HTTPCLIENT_CONNECTIONPOOLSIZE  | 200| false | string |
| httpclient.keepalive.timeout | HTTPCLIENT_KEEPALIVE_TIMEOUT  | 1200| false | string |
| authorization.rootAccess | AUTHORIZATION_ROOTACCESS  | true| false | boolean |
| authorization.abox.adminGroup | AUTHORIZATION_ABOX_ADMINGROUP  | elds-admins| false | string |
| authorization.abox.publicGroup | AUTHORIZATION_ABOX_PUBLICGROUP  | urn:elds-backend-public-group| false | string |
| authorization.abox.anonymousUser | AUTHORIZATION_ABOX_ANONYMOUSUSER  | urn:elds-backend-anonymous-user| false | string |
| authorization.abox.prefix | AUTHORIZATION_ABOX_PREFIX  | <https://ns.eccenca.com/>| false | string |
| authorization.abox.accessConditions.url | AUTHORIZATION_ABOX_ACCESSCONDITIONS_URL  | *none*| false | string |
| authorization.abox.accessConditions.graph | AUTHORIZATION_ABOX_ACCESSCONDITIONS_GRAPH  | urn:elds-backend-access-conditions-graph| false | string |
| proxy.defaultBaseIri | PROXY_DEFAULTBASEIRI  | <https://fallback.eccenca.com/>| false | URI |
| proxy.labelProperties | PROXY_LABELPROPERTIES  | [<http://www.w3.org/2004/02/skos/core#prefLabel>, <http://www.w3.org/2000/01/rdf-schema#label>, <http://purl.org/dc/terms/title>, <http://www.w3.org/ns/shacl#name>]| false | list of Properties |
| proxy.descriptionProperties | PROXY_DESCRIPTIONPROPERTIES  | [<http://purl.org/dc/terms/description>, <http://www.w3.org/2000/01/rdf-schema#comment>]| false | list of Properties |
| proxy.languagePreferences | PROXY_LANGUAGEPREFERENCES  | [de, en, ]| false | string |
| proxy.languagePreferencesAnyLangFallback | PROXY_LANGUAGEPREFERENCESANYLANGFALLBACK  | true| false | string |
| proxy.maxCBDDepth | PROXY_MAXCBDDEPTH  | 5| false | string |
| proxy.shapedMaxValueCount | PROXY_SHAPEDMAXVALUECOUNT  | 26| false | string |
| proxy.cacheInvalidationCron | PROXY_CACHEINVALIDATIONCRON  | 0 */30* ** *| false | Cron setting according to <https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling-cron-expression> |
| proxy.cacheSelectiveInvalidation | PROXY_CACHESELECTIVEINVALIDATION  | true| false | boolean |
| proxy.queryMonitorMaxMemoryInMb | PROXY_QUERYMONITORMAXMEMORYINMB  | 30| false | Value in MB |
| proxy.fetchValuesStrategy | PROXY_FETCHVALUESSTRATEGY  | RESOURCE_IN_VALUES| false | RESOURCE_IN_VALUES, FILTER_ONLY |
| gitSync.enabled | GITSYNC_ENABLED  | false| false | boolean |
| gitSync.dataFolder | GITSYNC_DATAFOLDER  | data| false | string |
| gitSync.remoteUrl | GITSYNC_REMOTEURL  | *none*| false | HTTP or local repository which can be reached from DP |
| gitSync.branch | GITSYNC_BRANCH  | main| false | An existing branch in the repository |
| gitSync.user | GITSYNC_USER  | *none*| false | Existing git repository user |
| gitSync.password | GITSYNC_PASSWORD  | *none*| false | Existing git repository password |
| gitSync.committerName | GITSYNC_COMMITTERNAME  | eccenca DataPlatform| false | string |
| gitSync.committerEmail | GITSYNC_COMMITTEREMAIL  | info@eccenca.com| false | string |
| gitSync.scheduledPullCron | GITSYNC_SCHEDULEDPULLCRON  | 0 */30* ** *| false | Cron setting according to <https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling-cron-expression> |
| logging.file.name | LOGGING_FILE_NAME  | *none*| false | string (file name) - empty to disable file output |
| logging.file.path | LOGGING_FILE_PATH  | *none*| false | string (file path) - empty to disable file output |
| logging.config | LOGGING_CONFIG  | *none*| false | string (file path) |
| logging.level.audit | LOGGING_LEVEL_AUDIT  | INFO| false | string |
| logging.level.com.eccenca.elds.backend | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND  | INFO| false | string |
| logging.level.org.springframework | LOGGING_LEVEL_ORG_SPRINGFRAMEWORK  | WARN| false | string |
| logging.level.com.eccenca.elds.backend.webapp.web.filter.SimpleCorsFilter | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_WEBAPP_WEB_FILTER_SIMPLECORSFILTER  | WARN| false | string |
| logging.level.com.eccenca.elds.backend.webapp.web.GlobalControllerExceptionHandler | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_WEBAPP_WEB_GLOBALCONTROLLEREXCEPTIONHANDLER  | TRACE| false | string |
| logging.level.com.eccenca.elds.backend.stardog.StardogTemplate | LOGGING_LEVEL_COM_ECCENCA_ELDS_BACKEND_STARDOG_STARDOGTEMPLATE  | INFO| false | string |
| audit-trail.enabled | AUDIT_TRAIL_ENABLED  | false| false | boolean |
| audit-trail.auditedGraphs | AUDIT_TRAIL_AUDITEDGRAPHS  | *none*| false | List of graph IRIs |
| sparql.query.limit | SPARQL_QUERY_LIMIT  | 100000| false | string |
| server.port | SERVER_PORT  | 9090| false | integer |
| server.servlet.contextPath | SERVER_SERVLET_CONTEXTPATH  | *none*| false | string |
| server.ssl.key-store | SERVER_SSL_KEY_STORE  | *none*| false | string |
| server.ssl.key-store-password | SERVER_SSL_KEY_STORE_PASSWORD  | *none*| false | string |
| server.ssl.client-auth | SERVER_SSL_CLIENT_AUTH  | *none*| false | none, NEED, WANT |
| server.tomcat.remoteIpHeader | SERVER_TOMCAT_REMOTEIPHEADER  | *none*| false | string |
| server.tomcat.protocolHeader | SERVER_TOMCAT_PROTOCOLHEADER  | *none*| false | string |
| scheduler.bulkLoadPoolSize | SCHEDULER_BULKLOADPOOLSIZE  | 1| false | integer |
| scheduler.analyticalPoolSize | SCHEDULER_ANALYTICALPOOLSIZE  | 10| false | integer |
| files.maxStorageSingleFileSizeMb | FILES_MAXSTORAGESINGLEFILESIZEMB  | 3000| false | string |
| files.minStorageTempSpaceLeftMb | FILES_MINSTORAGETEMPSPACELEFTMB  | 3000| false | string |
| files.maintenanceExpirationDuration | FILES_MAINTENANCEEXPIRATIONDURATION  | P1D| false | string |
| files.maintenanceCron | FILES_MAINTENANCECRON  | 0 0 1 ** ?| false | string |
| store.type | STORE_TYPE  | *none*| true | MEMORY, HTTP, GRAPHDB, STARDOG, VIRTUOSO, NEPTUNE |
| store.owlImportsResolution | STORE_OWLIMPORTSRESOLUTION  | true| false | string |
| store.authorization | STORE_AUTHORIZATION  | none| false | NONE, REWRITE_FROM |
| store.queryTimeoutGeneral | STORE_QUERYTIMEOUTGENERAL  | PT1H| false | ISO 8601 duration format |
