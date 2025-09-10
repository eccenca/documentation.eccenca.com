---
tags:
    - Configuration
---

## Configuration for connecting to GraphDB backend

Configuration example:

This example configures a connection with HTTPS to a remote graphdb store (<https://remote:7200>) using the workbench import directory
which is shared with the GraphDB instance. The repository will be created on startup of CMEM.

```yaml
store:
  type: graphdb
  owlImportsResolution: true
  authorization: REWRITE_FROM
  graphdb:
    host: "remote"
    port: 7200
    ssl-enabled: true
    repository: "newRepository"
    username: "admin"
    password: "admin"
    importDirectory: "/shared/mount"
    useDirectTransfer: false
    createRepositoryOnStartup: true
```


***Property: store.type***

The type of the store must be set to "graphdb"

| Category | Value |
|--- | ---: |
| Default | graphdb |
| Required | true |
| Valid values | GRAPHDB |
| Environment | STORE_TYPE |

### Specific settings for GraphDB


***Property: store.graphdb.host***

The host of the GraphDB database

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | true |
| Valid values | string |
| Environment | STORE_GRAPHDB_HOST |

***Property: store.graphdb.port***

The port of the GraphDB database

| Category | Value |
|--- | ---: |
| Default | 7200 |
| Required | false |
| Valid values | integer |
| Environment | STORE_GRAPHDB_PORT |

***Property: store.graphdb.ssl-enabled***

Whether SSL is enabled or not (http vs. https)

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | STORE_GRAPHDB_SSL_ENABLED |

***Property: store.graphdb.repository***

The name of the repository to connect to

| Category | Value |
|--- | ---: |
| Default | cmem |
| Required | false |
| Valid values | string |
| Environment | STORE_GRAPHDB_REPOSITORY |

***Property: store.graphdb.username***

The user name to connect with

| Category | Value |
|--- | ---: |
| Default | user |
| Required | true |
| Valid values | string |
| Environment | STORE_GRAPHDB_USERNAME |

***Property: store.graphdb.password***

The credentials of the given user

| Category | Value |
|--- | ---: |
| Default | password |
| Required | true |
| Valid values | string |
| Environment | STORE_GRAPHDB_PASSWORD |

***Property: store.graphdb.importDirectory***

Import directory to be utilized in the "workbench import with shared folder" approach. Not relevant when `useDirectTransfer` is true. Must be set when `useDirectTransfer` is false.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_GRAPHDB_IMPORTDIRECTORY |

***Property: store.graphdb.useDirectTransfer***

Set to true to use the native Graph Store API endpoint. Set to false to use the GraphDB workbench import. The import directory must be set then.

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | boolean |
| Environment | STORE_GRAPHDB_USEDIRECTTRANSFER |

***Property: store.graphdb.create-repository-on-startup***

Whether to create the given repository on startup if it does not exist

| Category | Value |
|--- | ---: |
| Default | true |
| Required | false |
| Valid values | boolean |
| Environment | STORE_GRAPHDB_CREATE_REPOSITORY_ON_STARTUP |

***Property: store.graphdb.gdbBaseIndex***

The iri of the lucene index to be used for searches. If the default index is used, Explore backend (DataPlatform) syncs the index with the configured `proxy.labelProperties`

| Category | Value |
|--- | ---: |
| Default | http://www.ontotext.com/connectors/lucene/instance#cmembaseindex |
| Required | false |
| Valid values | Valid URI of lucene index |
| Environment | STORE_GRAPHDB_GDBBASEINDEX |

***Property: store.graphdb.graphDbChangeTrackingActive***

Whether to make use of GraphDB change tracking during SPARQL updates (s. <https://graphdb.ontotext.com/documentation/10.0/change-tracking.html>). This setting is relevant in regards to selectively evicting DP caches depending on the outcome of the SPARQL update s. also `proxy.cacheSelectiveInvalidation`

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | STORE_GRAPHDB_GRAPHDBCHANGETRACKINGACTIVE |

***Property: store.graphdb.graphDbChangeTrackingMaxQuadMemory***

Maximum amount of quads of change tracking result which will be loaded in memory

| Category | Value |
|--- | ---: |
| Default | 1000 |
| Required | false |
| Valid values | int |
| Environment | STORE_GRAPHDB_GRAPHDBCHANGETRACKINGMAXQUADMEMORY |

