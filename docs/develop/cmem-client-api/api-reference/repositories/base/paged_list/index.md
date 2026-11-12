---
title: "cmem-client: repositories.base.paged_list module"
description: "Repository implementation for paginated API endpoints."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.base.paged_list` {#cmem_client.repositories.base.paged_list}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository implementation for paginated API endpoints.

This module provides PagedListRepository, a repository implementation that
handles paginated API responses commonly used in Corporate Memory's DataPlatform
(explore) APIs. It automatically fetches all pages of results and provides
a unified dictionary-like interface.

The PagedListRepository is typically used for endpoints that return results
in a paginated format with metadata about page size, number, and totals.

**Classes:**

- [**PagedListRepository**](#cmem_client.repositories.base.paged_list.PagedListRepository) – Repository that uses a paged list endpoint.

## `PagedListRepository` {#cmem_client.repositories.base.paged_list.PagedListRepository}

Bases: <code>[Repository](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.Repository)</code>

Repository that uses a paged list endpoint.

**Attributes:**

- **_dict** (<code>dict[str, [PagedListRepository[ItemType]](#cmem_client.repositories.base.paged_list.PagedListRepository)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_config** (<code>[RepositoryConfig](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which paged endpoint the repository fetches its data from.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.base.paged_list.PagedListRepository.fetch_data) – Fetch a paged list from a JSON endpoint via a type adapter.
- [**items**](#cmem_client.repositories.base.paged_list.PagedListRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.base.paged_list.PagedListRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.base.paged_list.PagedListRepository.values) – Get the values of the repository

### `fetch_data` {#cmem_client.repositories.base.paged_list.PagedListRepository.fetch_data}

```python
fetch_data()
```

Fetch a paged list from a JSON endpoint via a type adapter.

Use this method to fetch data if your result set is a pageable spring endpoint.

### `items` {#cmem_client.repositories.base.paged_list.PagedListRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.base.paged_list.PagedListRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.base.paged_list.PagedListRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.base.paged_list.PagedListRepository.values}

```python
values()
```

Get the values of the repository

