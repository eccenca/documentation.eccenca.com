---
title: "cmem-client: components.explore.sparql module"
description: "SPARQL Wrapper for eccenca Corporate Memory"
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.explore.sparql` {#cmem_client.components.explore.sparql}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

SPARQL Wrapper for eccenca Corporate Memory

**Classes:**

- [**SPARQLWrapper**](#cmem_client.components.explore.sparql.SPARQLWrapper) – Sparql wrapper class

## `SPARQLWrapper` {#cmem_client.components.explore.sparql.SPARQLWrapper}

```python
SPARQLWrapper(sparql_endpoint, update_endpoint, client)
```

Bases: <code>SPARQLConnector</code>

Sparql wrapper class

**Functions:**

- [**query**](#cmem_client.components.explore.sparql.SPARQLWrapper.query) – Query a SPARQL endpoint.
- [**update**](#cmem_client.components.explore.sparql.SPARQLWrapper.update) – Perform update SPARQL query.

**Attributes:**

- [**logger**](#cmem_client.components.explore.sparql.SPARQLWrapper.logger) –

### `logger` {#cmem_client.components.explore.sparql.SPARQLWrapper.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `query` {#cmem_client.components.explore.sparql.SPARQLWrapper.query}

```python
query(query, default_graph=None, named_graph=None, owl_imports_resolution=True)
```

Query a SPARQL endpoint.

### `update` {#cmem_client.components.explore.sparql.SPARQLWrapper.update}

```python
update(query, default_graph=None, named_graph=None)
```

Perform update SPARQL query.

