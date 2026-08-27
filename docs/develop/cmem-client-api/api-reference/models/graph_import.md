---
title: "cmem-client: graph_import module"
description: "Graph import models for Corporate Memory."
tags:
  - API
  - Python
  - cmem-client
---

# `graph_import` {#cmem_client.models.graph_import}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Graph import models for Corporate Memory.

An import is an ``owl:imports`` statement, which makes the content of one graph visible
in another. The single statements are the items of ``client.graph_imports``, keyed by
``{from_graph}::::{to_graph}``, while the transitive closure of one graph is returned
as a tree by that repository.

**Classes:**

- [**GraphImport**](#cmem_client.models.graph_import.GraphImport) – Graph Import model.
- [**GraphImportTree**](#cmem_client.models.graph_import.GraphImportTree) – Import tree structure for a graph.

## `GraphImport` {#cmem_client.models.graph_import.GraphImport}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

Graph Import model.

**Attributes:**

- [**from_graph**](#cmem_client.models.graph_import.GraphImport.from_graph) (<code>str</code>) – IRI of the importing graph, the one which carries the
``owl:imports`` statement.
- [**to_graph**](#cmem_client.models.graph_import.GraphImport.to_graph) (<code>str</code>) – IRI of the imported graph.

**Functions:**

- [**get_id**](#cmem_client.models.graph_import.GraphImport.get_id) – Get the id of the item.

### `from_graph` {#cmem_client.models.graph_import.GraphImport.from_graph}

```python
from_graph: str
```

### `get_id` {#cmem_client.models.graph_import.GraphImport.get_id}

```python
get_id()
```

Get the id of the item.

### `model_config` {#cmem_client.models.graph_import.GraphImport.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `to_graph` {#cmem_client.models.graph_import.GraphImport.to_graph}

```python
to_graph: str
```

## `GraphImportTree` {#cmem_client.models.graph_import.GraphImportTree}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Import tree structure for a graph.

**Attributes:**

- [**tree**](#cmem_client.models.graph_import.GraphImportTree.tree) (<code>dict[str, list[str]]</code>) – Resolved imports, mapping the IRI of each graph to the IRIs of the graphs
it imports.
- [**ignored**](#cmem_client.models.graph_import.GraphImportTree.ignored) (<code>dict[str, list[str]]</code>) – Imports which were not resolved, mapping the IRI of each graph to the
IRIs it points at in vain, for example because the target does not exist or

would close a cycle.

### `ignored` {#cmem_client.models.graph_import.GraphImportTree.ignored}

```python
ignored: dict[str, list[str]] = Field(default_factory=dict)
```

### `model_config` {#cmem_client.models.graph_import.GraphImportTree.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `tree` {#cmem_client.models.graph_import.GraphImportTree.tree}

```python
tree: dict[str, list[str]] = Field(default_factory=dict)
```

