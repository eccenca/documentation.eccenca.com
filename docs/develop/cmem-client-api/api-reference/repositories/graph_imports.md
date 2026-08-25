---
title: "graph_imports"
tags:
  - API
  - Python
  - cmem-client
---

# `graph_imports` {#cmem_client.repositories.graph_imports}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the ``owl:imports`` relations between named graphs.

Provides GraphImportsRepository for adding and removing an import statement between two
graphs, and for resolving the resulting import tree of a graph. Items are keyed by
``from_graph::::to_graph``.

**Examples:**

Declare that one graph imports another and remove the relation again:

```pycon
>>> from cmem_client.client import Client
>>> from cmem_client.models.graph_import import GraphImport
>>> client = Client.from_env()
>>> client.graph_imports.create_item(
...     GraphImport(
...         from_graph="https://example.org/data/",
...         to_graph="https://example.org/vocab/",
...     )
... )
>>> client.graph_imports.delete_item(
...     "https://example.org/data/::::https://example.org/vocab/"
... )
```

Resolve what a graph pulls in, directly and transitively:

```pycon
>>> client.graph_imports.get_transitive_imports("https://example.org/data/")
>>> client.graph_imports.get_import_tree("https://example.org/data/")
```

**Classes:**

- [**GraphImportsCreateConfig**](#cmem_client.repositories.graph_imports.GraphImportsCreateConfig) – Graph Imports creation configuration
- [**GraphImportsDeleteConfig**](#cmem_client.repositories.graph_imports.GraphImportsDeleteConfig) – Graph Imports deletion configuration.
- [**GraphImportsRepository**](#cmem_client.repositories.graph_imports.GraphImportsRepository) – Repository for managing Graph Imports

**Attributes:**

- [**GRAPH_IMPORTS_CREATE_SPARQL**](#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_CREATE_SPARQL) –
- [**GRAPH_IMPORTS_DELETE_SPARQL**](#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_DELETE_SPARQL) –
- [**GRAPH_IMPORTS_LIST_SPARQL**](#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_LIST_SPARQL) –

## `GRAPH_IMPORTS_CREATE_SPARQL` {#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_CREATE_SPARQL}

```python
GRAPH_IMPORTS_CREATE_SPARQL = '\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\n\nINSERT DATA {{\n  GRAPH <{from_graph}> {{\n    <{from_graph}> owl:imports <{to_graph}> .\n  }}\n}}\n'
```

## `GRAPH_IMPORTS_DELETE_SPARQL` {#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_DELETE_SPARQL}

```python
GRAPH_IMPORTS_DELETE_SPARQL = '\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\n\nDELETE DATA {{\n  GRAPH <{from_graph}> {{\n    <{from_graph}> owl:imports <{to_graph}> .\n  }}\n}}\n'
```

## `GRAPH_IMPORTS_LIST_SPARQL` {#cmem_client.repositories.graph_imports.GRAPH_IMPORTS_LIST_SPARQL}

```python
GRAPH_IMPORTS_LIST_SPARQL = '\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\n\nSELECT ?from_graph ?to_graph\nWHERE\n{\n  GRAPH ?from_graph {\n    ?from_graph owl:imports ?to_graph\n  }\n}\n'
```

## `GraphImportsCreateConfig` {#cmem_client.repositories.graph_imports.GraphImportsCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Graph Imports creation configuration

**Attributes:**

- **model_config** –

## `GraphImportsDeleteConfig` {#cmem_client.repositories.graph_imports.GraphImportsDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Graph Imports deletion configuration.

**Attributes:**

- **model_config** –

## `GraphImportsRepository` {#cmem_client.repositories.graph_imports.GraphImportsRepository}

Bases: <code>[Repository](../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>

Repository for managing Graph Imports

**Functions:**

- [**create_item**](#cmem_client.repositories.graph_imports.GraphImportsRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.graph_imports.GraphImportsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.graph_imports.GraphImportsRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.graph_imports.GraphImportsRepository.fetch_data) – Fetch new data and update the repository
- [**get_import_tree**](#cmem_client.repositories.graph_imports.GraphImportsRepository.get_import_tree) – Get the hierarchical import tree structure for a graph.
- [**get_transitive_imports**](#cmem_client.repositories.graph_imports.GraphImportsRepository.get_transitive_imports) – Get the list of graphs imported by a graph, resolved transitively.
- [**items**](#cmem_client.repositories.graph_imports.GraphImportsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.graph_imports.GraphImportsRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.graph_imports.GraphImportsRepository.raise_modification_error) – Raise an exception if needed
- [**values**](#cmem_client.repositories.graph_imports.GraphImportsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.graph_imports.GraphImportsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.graph_imports.GraphImportsRepository.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `delete_all` {#cmem_client.repositories.graph_imports.GraphImportsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.graph_imports.GraphImportsRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `fetch_data` {#cmem_client.repositories.graph_imports.GraphImportsRepository.fetch_data}

```python
fetch_data()
```

Fetch new data and update the repository

### `get_import_tree` {#cmem_client.repositories.graph_imports.GraphImportsRepository.get_import_tree}

```python
get_import_tree(graph_iri)
```

Get the hierarchical import tree structure for a graph.

**Parameters:**

- **graph_iri** (<code>str</code>) – The IRI of the graph to retrieve the import tree for.

**Returns:**

- <code>[GraphImportTree](../models/graph_import.md#cmem_client.models.graph_import.GraphImportTree)</code> – A GraphImportTree with tree and ignored dicts mapping graph IRIs to lists of IRIs.

### `get_transitive_imports` {#cmem_client.repositories.graph_imports.GraphImportsRepository.get_transitive_imports}

```python
get_transitive_imports(graph_iri)
```

Get the list of graphs imported by a graph, resolved transitively.

**Parameters:**

- **graph_iri** (<code>str</code>) – The IRI of the graph to retrieve transitive imports for.

**Returns:**

- <code>list[str]</code> – A flat list of graph IRIs that are transitively imported by graph_iri.

### `items` {#cmem_client.repositories.graph_imports.GraphImportsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.graph_imports.GraphImportsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.graph_imports.GraphImportsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.graph_imports.GraphImportsRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `values` {#cmem_client.repositories.graph_imports.GraphImportsRepository.values}

```python
values()
```

Get the values of the repository

