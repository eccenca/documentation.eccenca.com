# `graph` {#cmem_client.models.graph}

RDF graph models for Corporate Memory knowledge graphs.

This module defines models for representing RDF graphs in Corporate Memory's
DataPlatform (explore) environment. Graphs contain semantic data and are
the primary storage units for knowledge graphs.

The Graph model includes metadata about graph permissions, assigned semantic
classes, and access control, providing the foundation for graph-based
operations in the explore APIs.

**Classes:**

- [**Graph**](#cmem_client.models.graph.Graph) – A graph
- [**GraphLabel**](#cmem_client.models.graph.GraphLabel) – Label metadata for a graph returned by the /graphs/list endpoint.

## `Graph` {#cmem_client.models.graph.Graph}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A graph

**Attributes:**

- [**iri**](#cmem_client.models.graph.Graph.iri) (<code>str</code>) – IRI of the graph. This is the key of the repository.
- [**writeable**](#cmem_client.models.graph.Graph.writeable) (<code>bool</code>) – Whether the authenticated account may write to the graph. Access is
decided by the access conditions of the deployment.
- [**assigned_classes**](#cmem_client.models.graph.Graph.assigned_classes) (<code>list[str]</code>) – IRIs of the classes assigned to the graph, which is how
Corporate Memory tells a vocabulary from a data graph or a shape graph.
- [**label**](#cmem_client.models.graph.Graph.label) (<code>[GraphLabel](#cmem_client.models.graph.GraphLabel) | None</code>) – Label of the graph, or ``None`` if it carries none.

**Functions:**

- [**get_id**](#cmem_client.models.graph.Graph.get_id) – Get the IRI of the graph

### `assigned_classes` {#cmem_client.models.graph.Graph.assigned_classes}

```python
assigned_classes: list[str] = Field(alias='assignedClasses')
```

### `get_id` {#cmem_client.models.graph.Graph.get_id}

```python
get_id()
```

Get the IRI of the graph

### `iri` {#cmem_client.models.graph.Graph.iri}

```python
iri: str
```

### `label` {#cmem_client.models.graph.Graph.label}

```python
label: GraphLabel | None = None
```

### `model_config` {#cmem_client.models.graph.Graph.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `writeable` {#cmem_client.models.graph.Graph.writeable}

```python
writeable: bool
```

## `GraphLabel` {#cmem_client.models.graph.GraphLabel}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Label metadata for a graph returned by the /graphs/list endpoint.

**Attributes:**

- [**title**](#cmem_client.models.graph.GraphLabel.title) (<code>str</code>) – Text of the label.
- [**lang**](#cmem_client.models.graph.GraphLabel.lang) (<code>str | None</code>) – Language tag of the label, e.g. ``en``, or ``None`` for a label without
one.

### `lang` {#cmem_client.models.graph.GraphLabel.lang}

```python
lang: str | None = None
```

### `model_config` {#cmem_client.models.graph.GraphLabel.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `title` {#cmem_client.models.graph.GraphLabel.title}

```python
title: str
```

