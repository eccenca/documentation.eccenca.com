---
title: "cmem-client: task_search module"
description: "Repository implementation for Corporate Memory task search endpoints."
tags:
  - API
  - Python
  - cmem-client
---

# `task_search` {#cmem_client.repositories.base.task_search}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository implementation for Corporate Memory task search endpoints.

This module provides TaskSearchRepository, a specialized repository that uses
Corporate Memory's DataIntegration task search API to find and retrieve items.
The search functionality allows for flexible querying with filters, facets,
and text search capabilities.

**Classes:**

- [**TaskSearchRepository**](#cmem_client.repositories.base.task_search.TaskSearchRepository) – Subclass of a ReadRepository that uses the task search endpoint.
- [**TaskSearchRepositoryConfig**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig) – Configuration class for a Task Search read repository

## `TaskSearchRepository` {#cmem_client.repositories.base.task_search.TaskSearchRepository}

Bases: <code>[Repository](../../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)</code>

Subclass of a ReadRepository that uses the task search endpoint.

**Attributes:**

- **_dict** (<code>dict[str, [TaskSearchRepository[ItemType]](#cmem_client.repositories.base.task_search.TaskSearchRepository)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_config** (<code>[TaskSearchRepositoryConfig](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig)</code>) – Describes which task search endpoint to query and which task type to
search for.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.base.task_search.TaskSearchRepository.fetch_data) – Fetch a list from the DI task search endpoint via a type adapter.
- [**get_task**](#cmem_client.repositories.base.task_search.TaskSearchRepository.get_task) – Get full task details from the API.
- [**items**](#cmem_client.repositories.base.task_search.TaskSearchRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.base.task_search.TaskSearchRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.base.task_search.TaskSearchRepository.values) – Get the values of the repository

### `fetch_data` {#cmem_client.repositories.base.task_search.TaskSearchRepository.fetch_data}

```python
fetch_data()
```

Fetch a list from the DI task search endpoint via a type adapter.

### `get_task` {#cmem_client.repositories.base.task_search.TaskSearchRepository.get_task}

```python
get_task(project_id, task_id, with_labels=True)
```

Get full task details from the API.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **task_id** (<code>str</code>) – The task ID.
- **with_labels** (<code>bool</code>) – Whether to include labels in the response.

**Returns:**

- <code>[TaskResponse](../../models/task.md#cmem_client.models.task.TaskResponse)</code> – The full task details as a TaskResponse model.

### `items` {#cmem_client.repositories.base.task_search.TaskSearchRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.base.task_search.TaskSearchRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.base.task_search.TaskSearchRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.base.task_search.TaskSearchRepository.values}

```python
values()
```

Get the values of the repository

## `TaskSearchRepositoryConfig` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig}

```python
TaskSearchRepositoryConfig(fetch_data_adapter, item_type, component='build', fetch_data_path='/api/workspace/searchItems', facets=None)
```

Bases: <code>[RepositoryConfig](../../repositories/base/abc.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>

Configuration class for a Task Search read repository

**Attributes:**

- [**component**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.component) (<code>Literal['build', 'explore']</code>) – Which Corporate Memory API endpoint to address: ``build`` or ``explore``.
- [**fetch_data_path**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.fetch_data_path) (<code>str</code>) – API path of the task search endpoint.
- [**fetch_data_adapter**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.fetch_data_adapter) (<code>TypeAdapter</code>) – Pydantic TypeAdapter used to deserialize the search result set.
- [**item_type**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.item_type) (<code>str</code>) – Task type to search for, sent as ``itemType`` in the search request
(e.g. ``dataset`` or ``workflow``).
- [**facets**](#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.facets) (<code>list[dict[str, Any]] | None</code>) – Facet filters sent as ``facets`` in the search request. If None, no facet
filtering is applied.

### `component` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.component}

```python
component: Literal['build', 'explore']
```

### `facets` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.facets}

```python
facets: list[dict[str, Any]] | None = facets
```

### `fetch_data_adapter` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.fetch_data_adapter}

```python
fetch_data_adapter: TypeAdapter
```

### `fetch_data_path` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.fetch_data_path}

```python
fetch_data_path: str
```

### `item_type` {#cmem_client.repositories.base.task_search.TaskSearchRepositoryConfig.item_type}

```python
item_type: str = item_type
```

