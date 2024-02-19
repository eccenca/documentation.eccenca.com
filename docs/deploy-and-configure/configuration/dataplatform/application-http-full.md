---
tags:
    - Configuration
    - Docker
---

## Configuration for connecting to arbitrary SPARQL HTTP backend

To register a new SPARQL Store you need to make sure the store is available to the DataPlatform.
If it is available, use the following set of properties to connect to arbitrary HTTP SPARQL services in your `application.yml` (`conf/dataplatform/application.yml`).

``` yaml title="Configuration Example"
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

The type of the store must be set to `http`.

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

## Example: Jena Fuseki Store

This section provides an example configuration that uses an [Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/) as store.

### Add docker-compose File

Add a new docker-compose file to configure the execution of the store: `compose/docker-compose.store.fuseki.yml`.
In this case the two environment variables `FUSEKI_DOCKER_USER` and `FUSEKI_ENDPOINT_PORT` are introduced.

``` yaml title="docker-compose.store.fuseki.yml"
# Jena Fuseki
version: '2.4'
services:
  store_base:
    image: docker.io/secoresearch/fuseki:4.8.0
    user: ${FUSEKI_DOCKER_USER}
    ports:
      - "3030:3030"
    command: /jena-fuseki/fuseki-server --tdb2 --loc /data --update /cmem
    volumes:
      - "store_volume:/data"
    healthcheck:
      test: ["CMD", "echo", "true"]
      interval: 10s
      timeout: 1s
      retries: 5

  dataplatform:
    environment:
      - "FUSEKI_ENDPOINT_PORT=${FUSEKI_ENDPOINT_PORT}"
```

### Configure Variables

Now, the orchestration needs to know that it has to bring up the new store.
This happens with the variable `DP_STORE`.
But also the new variables (i.e. `FUSEKI_DOCKER_USER`, `FUSEKI_ENDPOINT_PORT`) introduced in the new docker-compose file need to be set.
This can be done in `environments/config.env` (see also [Docker Orchestration](../docker-orchestration/index.md))

``` bash title="environments/config.env (partially)"
# DP_STORE=virtuoso-enterprise
# DP_STORE=marklogic
# DP_STORE=neptune
DP_STORE=fuseki

###################
# FUSEKI SETTINGS #
###################
FUSEKI_DOCKER_USER=0:0
FUSEKI_ENDPOINT_PORT=3030
```

### Configure DataPlatform

Finally, the DataPlatform needs to know, how to access the new store.
This configuration happens in `conf/dataplatform/application.yml`.

1. Add the store to the section `spring.profiles.group`:

``` yaml title="conf/dataplaform/application.yml (partially"
# Profile groups for the supported stores - these groups are selected by DP_STORE
spring:
  profiles:
    group:
      […]
      fuseki: fuseki-store, auth-graph
```

2. At the end of the file, add a new section as follows (pay attention to the separator `---`):

``` yaml title="conf/dataplaform/application.yml (partially"
---

###
# Configuration for DP with Fuseki
###
spring:
  config:
    activate:
      on-profile: fuseki-store

## SPARQL Endpoints (Fuseki config)
store:
  type: http
  authorization: REWRITE_FROM
  http:
    query-endpoint-url: "http://store:${FUSEKI_ENDPOINT_PORT}/cmem/query"
    update-endpoint-url: "http://store:${FUSEKI_ENDPOINT_PORT}/cmem/update"
```

