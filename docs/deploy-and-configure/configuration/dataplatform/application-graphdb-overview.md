---
hide:
  - toc
---

| Property | Environment | Default | Required | Valid values|
| --- | --- | --- | --- | --- |
| store.type | STORE_TYPE  | graphdb| true | GRAPHDB |
| store.graphdb.host | STORE_GRAPHDB_HOST  | *none*| true | string |
| store.graphdb.port | STORE_GRAPHDB_PORT  | 7200| false | integer |
| store.graphdb.ssl-enabled | STORE_GRAPHDB_SSL_ENABLED  | false| false | boolean |
| store.graphdb.repository | STORE_GRAPHDB_REPOSITORY  | cmem| false | string |
| store.graphdb.username | STORE_GRAPHDB_USERNAME  | user| true | string |
| store.graphdb.password | STORE_GRAPHDB_PASSWORD  | password| true | string |
| store.graphdb.importDirectory | STORE_GRAPHDB_IMPORTDIRECTORY  | *none*| false | string |
| store.graphdb.useDirectTransfer | STORE_GRAPHDB_USEDIRECTTRANSFER  | true| false | boolean |
| store.graphdb.create-repository-on-startup | STORE_GRAPHDB_CREATE_REPOSITORY_ON_STARTUP  | true| false | boolean |
| store.graphdb.gdbBaseIndex | STORE_GRAPHDB_GDBBASEINDEX  | <http://www.ontotext.com/connectors/lucene/instance#cmembaseindex>| false | Valid URI of lucene index |
| store.graphdb.graphDbChangeTrackingActive | STORE_GRAPHDB_GRAPHDBCHANGETRACKINGACTIVE  | true| false | boolean |
| store.graphdb.graphDbChangeTrackingMaxQuadMemory | STORE_GRAPHDB_GRAPHDBCHANGETRACKINGMAXQUADMEMORY  | 1000| false | int |
