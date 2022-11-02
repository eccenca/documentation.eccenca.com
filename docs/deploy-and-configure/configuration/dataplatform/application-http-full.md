
## Configuration for connecting to arbitrary SPARQL HTTP backend

Use the following set of properties to connect to arbitrary HTTP SPARQL services.

Configuration example:

```yaml
store:
  type: http
  authorization: REWRITE_FROM
  http:
    query-endpoint-url: "http://localhost:7200/repositories/cmem"
    update-endpoint-url: "http://localhost:7200/repositories/cmem/statements"
    graph-store-endpoint-url: "http://localhost:7200/repositories/cmem/rdf-graphs/service"
    username: "user"
    password: "password"
```


***Property: store.type***

The type of the store must be set to "http"

| Category | Value |
|--- | ---: |
| Default | http |
| Required | true |
| Valid values | HTTP |
| Environment | STORE_TYPE |

***Property: store.authorization***


| Category | Value |
|--- | ---: |
| Default | REWRITE_FROM |
| Required | false |
| Valid values | string |
| Environment | STORE_AUTHORIZATION |

Specific settings for HTTP. At least query and update endpoints must be provided.

***Property: store.http.query-endpoint-url***

Use this property to configure the endpoint to which SPARQL 1.1 queries are sent.

| Category | Value |
|--- | ---: |
| Default | http://localhost:7200/repositories/cmem |
| Required | true |
| Valid values | string |
| Environment | STORE_HTTP_QUERY_ENDPOINT_URL |

***Property: store.http.update-endpoint-url***

Use this property to configure the endpoint to which SPARQL 1.1 updates are sent.

| Category | Value |
|--- | ---: |
| Default | http://localhost:7200/repositories/cmem/statements |
| Required | true |
| Valid values | string |
| Environment | STORE_HTTP_UPDATE_ENDPOINT_URL |

***Property: store.http.graph-store-endpoint-url***

Use this property to configure the endpoint to SPARQL 1.1 Graph Store Protocol requests are sent.

| Category | Value |
|--- | ---: |
| Default | http://localhost:7200/repositories/cmem/rdf-graphs/service |
| Required | false |
| Valid values | string |
| Environment | STORE_HTTP_GRAPH_STORE_ENDPOINT_URL |

***Property: store.http.username***

Basic authentication is used if this parameter is provided.

| Category | Value |
|--- | ---: |
| Default | user |
| Required | false |
| Valid values | string |
| Environment | STORE_HTTP_USERNAME |

***Property: store.http.password***

Basic authentication is used if this parameter is provided.

| Category | Value |
|--- | ---: |
| Default | password |
| Required | false |
| Valid values | string |
| Environment | STORE_HTTP_PASSWORD |

***Property: store.http.graphListQuery***

Defines how the raw list of graphs is retrieved, and therefore which graphs are visible to the system. Graph must be bound to variable ?g !

| Category | Value |
|--- | ---: |
| Default | SELECT distinct ?g {graph ?g {?s ?p ?o}} |
| Required | false |
| Valid values | Valid SPARQL query with bound variable "g" |
| Environment | STORE_HTTP_GRAPHLISTQUERY |

