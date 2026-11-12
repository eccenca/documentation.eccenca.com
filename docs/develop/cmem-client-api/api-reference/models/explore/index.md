---
title: "cmem-client: models.explore module"
description: "Models of the Corporate Memory Explore (DataPlatform) component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.explore` {#cmem_client.models.explore}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models of the Corporate Memory Explore (DataPlatform) component.

**Classes:**

- [**AdminOperationStatus**](#cmem_client.models.explore.AdminOperationStatus) – Current administrative operation reported by GET /api/admin/status.
- [**StoreInformation**](#cmem_client.models.explore.StoreInformation) – Information about the graph store instance and its capabilities.
- [**Title**](#cmem_client.models.explore.Title) – The human-readable title of an IRI, as the Explore title service resolves it.

## `AdminOperationStatus` {#cmem_client.models.explore.AdminOperationStatus}

Bases: <code>StrEnum</code>

Current administrative operation reported by GET /api/admin/status.

**Attributes:**

- [**BACKUP**](#cmem_client.models.explore.AdminOperationStatus.BACKUP) –
- [**BOOTSTRAP**](#cmem_client.models.explore.AdminOperationStatus.BOOTSTRAP) –
- [**DROP_ALL_GRAPHS**](#cmem_client.models.explore.AdminOperationStatus.DROP_ALL_GRAPHS) –
- [**NONE**](#cmem_client.models.explore.AdminOperationStatus.NONE) –
- [**RESTORE**](#cmem_client.models.explore.AdminOperationStatus.RESTORE) –
- [**SHOWCASE**](#cmem_client.models.explore.AdminOperationStatus.SHOWCASE) –

### `BACKUP` {#cmem_client.models.explore.AdminOperationStatus.BACKUP}

```python
BACKUP = 'BACKUP'
```

### `BOOTSTRAP` {#cmem_client.models.explore.AdminOperationStatus.BOOTSTRAP}

```python
BOOTSTRAP = 'BOOTSTRAP'
```

### `DROP_ALL_GRAPHS` {#cmem_client.models.explore.AdminOperationStatus.DROP_ALL_GRAPHS}

```python
DROP_ALL_GRAPHS = 'DROP_ALL_GRAPHS'
```

### `NONE` {#cmem_client.models.explore.AdminOperationStatus.NONE}

```python
NONE = 'NONE'
```

### `RESTORE` {#cmem_client.models.explore.AdminOperationStatus.RESTORE}

```python
RESTORE = 'RESTORE'
```

### `SHOWCASE` {#cmem_client.models.explore.AdminOperationStatus.SHOWCASE}

```python
SHOWCASE = 'SHOWCASE'
```

## `StoreInformation` {#cmem_client.models.explore.StoreInformation}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Information about the graph store instance and its capabilities.

This model represents metadata about the DataPlatform graph store,
including the store type and version information. This information
is useful for compatibility checks, monitoring, and debugging.

**Attributes:**

- [**type**](#cmem_client.models.explore.StoreInformation.type) (<code>str</code>) – The type of graph store (e.g., "GRAPHDB", "TENTRIS").
- [**version**](#cmem_client.models.explore.StoreInformation.version) (<code>str</code>) – The version string of the graph store implementation.

### `model_config` {#cmem_client.models.explore.StoreInformation.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `type` {#cmem_client.models.explore.StoreInformation.type}

```python
type: str
```

The type/implementation of the graph store (e.g., "GRAPHDB", "TENTRIS").

### `version` {#cmem_client.models.explore.StoreInformation.version}

```python
version: str
```

The version string of the graph store implementation.

## `Title` {#cmem_client.models.explore.Title}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The human-readable title of an IRI, as the Explore title service resolves it.

A resource with a label gets that label; any other IRI gets a title derived from the
IRI itself, marked with `from_iri`.

**Attributes:**

- [**iri**](#cmem_client.models.explore.Title.iri) (<code>str</code>) – The IRI the title belongs to.
- [**title**](#cmem_client.models.explore.Title.title) (<code>str</code>) – The label of the resource, or a title derived from the IRI.
- [**lang**](#cmem_client.models.explore.Title.lang) (<code>str | None</code>) – The language tag of the label, if it has one.
- [**from_iri**](#cmem_client.models.explore.Title.from_iri) (<code>bool</code>) – Whether the title was derived from the IRI instead of a label.
- [**predicate**](#cmem_client.models.explore.Title.predicate) (<code>str | None</code>) – The property the label was read from, if there is a label.

### `from_iri` {#cmem_client.models.explore.Title.from_iri}

```python
from_iri: bool = Field(default=False, alias='fromIri')
```

Whether the title was derived from the IRI instead of a label.

### `iri` {#cmem_client.models.explore.Title.iri}

```python
iri: str
```

The IRI the title belongs to.

### `lang` {#cmem_client.models.explore.Title.lang}

```python
lang: str | None = None
```

The language tag of the label, if it has one.

### `model_config` {#cmem_client.models.explore.Title.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `predicate` {#cmem_client.models.explore.Title.predicate}

```python
predicate: str | None = None
```

The property the label was read from, if there is a label.

### `title` {#cmem_client.models.explore.Title.title}

```python
title: str
```

The label of the resource, or a title derived from the IRI.

