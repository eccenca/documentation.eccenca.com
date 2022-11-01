---
hide:
  - toc
---

| Property | Environment | Default | Required | Valid values|
| --- | --- | --- | --- | --- |
| store.type | STORE_TYPE  | http| true | HTTP |
| store.authorization | STORE_AUTHORIZATION  | REWRITE_FROM| false | string |
| store.http.query-endpoint-url | STORE_HTTP_QUERY_ENDPOINT_URL  | <http://localhost:7200/repositories/cmem>| true | string |
| store.http.update-endpoint-url | STORE_HTTP_UPDATE_ENDPOINT_URL  | <http://localhost:7200/repositories/cmem/statements>| true | string |
| store.http.graph-store-endpoint-url | STORE_HTTP_GRAPH_STORE_ENDPOINT_URL  | <http://localhost:7200/repositories/cmem/rdf-graphs/service>| false | string |
| store.http.username | STORE_HTTP_USERNAME  | user| false | string |
| store.http.password | STORE_HTTP_PASSWORD  | password| false | string |
| store.http.graphListQuery | STORE_HTTP_GRAPHLISTQUERY  | SELECT distinct ?g {graph ?g {?s ?p ?o}}| false | Valid SPARQL query with bound variable "g" |
