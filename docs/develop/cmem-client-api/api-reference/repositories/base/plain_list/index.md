---
title: "cmem-client: repositories.base.plain_list module"
description: "Repository implementation for simple list API endpoints."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.base.plain_list` {#cmem_client.repositories.base.plain_list}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository implementation for simple list API endpoints.

This module provides PlainListRepository, a repository implementation for
API endpoints that return a simple array of objects without pagination.
It's commonly used with Corporate Memory's DataIntegration (build) APIs
that provide straightforward list responses.

The PlainListRepository fetches the entire list in a single request and
provides dictionary-like access to the items by their ID.

**Classes:**

- [**PlainListRepository**](#cmem_client.repositories.base.plain_list.PlainListRepository) – Subclass of a ReadRepository that uses a plain list endpoint.

## `PlainListRepository` {#cmem_client.repositories.base.plain_list.PlainListRepository}

Bases: <code>[Repository](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.Repository)</code>

Subclass of a ReadRepository that uses a plain list endpoint.

**Attributes:**

- **_dict** (<code>dict[str, [PlainListRepository[ItemType]](#cmem_client.repositories.base.plain_list.PlainListRepository)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_config** (<code>[RepositoryConfig](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which endpoint the repository fetches its data from.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.base.plain_list.PlainListRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**items**](#cmem_client.repositories.base.plain_list.PlainListRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.base.plain_list.PlainListRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.base.plain_list.PlainListRepository.values) – Get the values of the repository

### `fetch_data` {#cmem_client.repositories.base.plain_list.PlainListRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `items` {#cmem_client.repositories.base.plain_list.PlainListRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.base.plain_list.PlainListRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.base.plain_list.PlainListRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.base.plain_list.PlainListRepository.values}

```python
values()
```

Get the values of the repository

