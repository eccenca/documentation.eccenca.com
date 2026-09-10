---
title: "cmem-client: models.base module"
description: "Base model classes for all cmem_client data models."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.base` {#cmem_client.models.base}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Base model classes for all cmem_client data models.

This module provides the foundational model classes that all other models
inherit from, establishing common patterns for data validation, serialization,
and repository interactions.

The Model class serves as the base for all Pydantic models in the library,
while ReadRepositoryItem provides an additional interface for entities that
can be retrieved from repositories and have identifiable IDs.

Two settings apply to every model of the library and are worth knowing:

- Fields can be set under their Python name as well as under the alias the API uses,
  so ``Graph(iri=..., assigned_classes=[])`` and ``assignedClasses=[]`` both work.
  Serializing with ``model_dump(by_alias=True)`` produces what the API expects.
- Fields the models do not declare are kept rather than rejected, and end up in
  ``model_extra``. A deployment which returns more than a model knows therefore still
  validates, and no data is lost. The flip side is that a field the server renames is
  only noticed when it was required: a renamed optional field silently stays at its
  default, with the unknown name sitting in ``model_extra``.

**Classes:**

- [**Model**](#cmem_client.models.base.Model) – Base model for all cmem-client models.
- [**ReadRepositoryItem**](#cmem_client.models.base.ReadRepositoryItem) – Abstract base class for items of a read repository

## `Model` {#cmem_client.models.base.Model}

Bases: <code>BaseModel</code>

Base model for all cmem-client models.

**Attributes:**

- [**model_config**](#cmem_client.models.base.Model.model_config) – Accepts both field names and API aliases as input, and keeps
unknown fields in ``model_extra`` instead of rejecting them.

### `model_config` {#cmem_client.models.base.Model.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `ReadRepositoryItem` {#cmem_client.models.base.ReadRepositoryItem}

Bases: <code>BaseModel</code>, <code>ABC</code>

Abstract base class for items of a read repository

An item knows the key it is stored under, which ``get_id()`` returns. For most
resources that is their ID or IRI, while items living inside a project combine
both, as in ``{project_id}:{id}``.

**Attributes:**

- [**model_config**](#cmem_client.models.base.ReadRepositoryItem.model_config) – Same settings as on ``Model``: aliases are accepted as input and
unknown fields are kept in ``model_extra``.

**Functions:**

- [**get_id**](#cmem_client.models.base.ReadRepositoryItem.get_id) – Get the id of the item.

### `get_id` {#cmem_client.models.base.ReadRepositoryItem.get_id}

```python
get_id()
```

Get the id of the item.

### `model_config` {#cmem_client.models.base.ReadRepositoryItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

