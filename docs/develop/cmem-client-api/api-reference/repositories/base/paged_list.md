---
title: "cmem-client: paged_list module"
tags:
  - API
  - Python
  - cmem-client
---

# `paged_list` {#cmem_client.repositories.base.paged_list}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository implementation for paginated API endpoints.

This module provides PagedListRepository, a repository implementation that
handles paginated API responses commonly used in Corporate Memory's DataPlatform
(explore) APIs. It automatically fetches all pages of results and provides
a unified dictionary-like interface.

The PagedListRepository is typically used for endpoints that return results
in a paginated format with metadata about page size, number, and totals.

**Classes:**

- [**PageDescription**](#cmem_client.repositories.base.paged_list.PageDescription) – A description of a paged list.
- [**PagedListRepository**](#cmem_client.repositories.base.paged_list.PagedListRepository) – Repository that uses a paged list endpoint.

## `PageDescription` {#cmem_client.repositories.base.paged_list.PageDescription}

Bases: <code>[Model](../../models/base.md#cmem_client.models.base.Model)</code>

A description of a paged list.

**Attributes:**

- [**size**](#cmem_client.repositories.base.paged_list.PageDescription.size) (<code>int</code>) – Number of items requested per page. ``fetch_data()`` stops paging as soon as a page
returns fewer items than this.
- [**number**](#cmem_client.repositories.base.paged_list.PageDescription.number) (<code>int</code>) – Zero based index of this page.
- [**total_elements**](#cmem_client.repositories.base.paged_list.PageDescription.total_elements) (<code>int</code>) – Total number of items across all pages, sent as ``totalElements``.
- [**total_pages**](#cmem_client.repositories.base.paged_list.PageDescription.total_pages) (<code>int</code>) – Total number of pages, sent as ``totalPages``.

### `model_config` {#cmem_client.repositories.base.paged_list.PageDescription.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `number` {#cmem_client.repositories.base.paged_list.PageDescription.number}

```python
number: int
```

### `size` {#cmem_client.repositories.base.paged_list.PageDescription.size}

```python
size: int
```

### `total_elements` {#cmem_client.repositories.base.paged_list.PageDescription.total_elements}

```python
total_elements: int = Field(alias='totalElements')
```

### `total_pages` {#cmem_client.repositories.base.paged_list.PageDescription.total_pages}

```python
total_pages: int = Field(alias='totalPages')
```

## `PagedListRepository` {#cmem_client.repositories.base.paged_list.PagedListRepository}

Bases: <code>[Repository](../../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)</code>

Repository that uses a paged list endpoint.

**Attributes:**

- **_dict** (<code>dict[str, [PagedListRepository[ItemType]](#cmem_client.repositories.base.paged_list.PagedListRepository)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_config** (<code>[RepositoryConfig](../../repositories/base/abc.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which paged endpoint the repository fetches its data from.

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

