---
title: "cmem-client: models.graph module"
description: "RDF graph models for Corporate Memory knowledge graphs."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.graph` {#cmem_client.models.graph}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

RDF graph models for Corporate Memory knowledge graphs.

This module defines models for representing RDF graphs in Corporate Memory's
DataPlatform (explore) environment. Graphs contain semantic data and are
the primary storage units for knowledge graphs.

The Graph model includes metadata about graph permissions, assigned semantic
classes, and access control, providing the foundation for graph-based
operations in the explore APIs. GraphFileSerialization describes an RDF serialization
the graphs repository imports and exports.

**Classes:**

- [**Graph**](#cmem_client.models.graph.Graph) – A graph
- [**GraphFileSerialization**](#cmem_client.models.graph.GraphFileSerialization) – Supported graph format description
- [**GraphLabel**](#cmem_client.models.graph.GraphLabel) – Label metadata for a graph returned by the /graphs/list endpoint.

## `Graph` {#cmem_client.models.graph.Graph}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A graph

**Attributes:**

- [**iri**](#cmem_client.models.graph.Graph.iri) (<code>str</code>) – IRI of the graph. This is the key of the repository.
- [**writeable**](#cmem_client.models.graph.Graph.writeable) (<code>bool</code>) – Whether the authenticated account may write to the graph. Access is
decided by the access conditions of the deployment.
- [**assigned_classes**](#cmem_client.models.graph.Graph.assigned_classes) (<code>list[str]</code>) – IRIs of the classes assigned to the graph, which is how
Corporate Memory tells a vocabulary from a data graph or a shape graph.
- [**di_project_graph**](#cmem_client.models.graph.Graph.di_project_graph) (<code>bool</code>) – Whether the graph is a DataIntegration project graph.
- [**system_resource**](#cmem_client.models.graph.Graph.system_resource) (<code>bool</code>) – Whether the graph is a system resource, e.g. a shape or
query catalog graph.
- [**label**](#cmem_client.models.graph.Graph.label) (<code>[GraphLabel](#cmem_client.models.graph.GraphLabel) | None</code>) – Label of the graph, or ``None`` if it carries none.

**Functions:**

- [**get_id**](#cmem_client.models.graph.Graph.get_id) – Get the IRI of the graph

### `assigned_classes` {#cmem_client.models.graph.Graph.assigned_classes}

```python
assigned_classes: list[str] = Field(alias='assignedClasses')
```

### `di_project_graph` {#cmem_client.models.graph.Graph.di_project_graph}

```python
di_project_graph: bool = Field(alias='diProjectGraph')
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

### `system_resource` {#cmem_client.models.graph.Graph.system_resource}

```python
system_resource: bool = Field(alias='systemResource')
```

### `writeable` {#cmem_client.models.graph.Graph.writeable}

```python
writeable: bool
```

## `GraphFileSerialization` {#cmem_client.models.graph.GraphFileSerialization}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Supported graph format description

**Attributes:**

- [**mime_type**](#cmem_client.models.graph.GraphFileSerialization.mime_type) (<code>str</code>) – MIME type of the serialization, sent as ``Content-Type`` on import and as
``Accept`` on export.
- [**file_extensions**](#cmem_client.models.graph.GraphFileSerialization.file_extensions) (<code>list[str]</code>) – File extensions mapped to this serialization, used by
``guess_file_type()`` to detect the format of a path.
- [**encoding**](#cmem_client.models.graph.GraphFileSerialization.encoding) (<code>str | None</code>) – Content encoding of the file, sent as ``Content-Encoding`` on import when set.
- [**known_not_supporters**](#cmem_client.models.graph.GraphFileSerialization.known_not_supporters) (<code>list[str]</code>) – Store types known not to support this serialization, matched against
the type reported by the graph store. The client does not enforce this; the test suite
uses it to skip combinations a store cannot handle.
- [**export_supported**](#cmem_client.models.graph.GraphFileSerialization.export_supported) (<code>bool</code>) – Whether graphs can be exported in this serialization.
- [**import_supported**](#cmem_client.models.graph.GraphFileSerialization.import_supported) (<code>bool</code>) – Whether graphs can be imported from this serialization.

### `encoding` {#cmem_client.models.graph.GraphFileSerialization.encoding}

```python
encoding: str | None = None
```

### `export_supported` {#cmem_client.models.graph.GraphFileSerialization.export_supported}

```python
export_supported: bool = True
```

### `file_extensions` {#cmem_client.models.graph.GraphFileSerialization.file_extensions}

```python
file_extensions: list[str]
```

### `import_supported` {#cmem_client.models.graph.GraphFileSerialization.import_supported}

```python
import_supported: bool = True
```

### `known_not_supporters` {#cmem_client.models.graph.GraphFileSerialization.known_not_supporters}

```python
known_not_supporters: list[str] = Field(default_factory=list)
```

### `mime_type` {#cmem_client.models.graph.GraphFileSerialization.mime_type}

```python
mime_type: str
```

### `model_config` {#cmem_client.models.graph.GraphFileSerialization.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `GraphLabel` {#cmem_client.models.graph.GraphLabel}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

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

