---
title: "abc"
tags:
  - API
  - Python
  - cmem-client
---

# `abc` {#cmem_client.repositories.base.abc}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Abstract base classes and configuration for CMEM repositories.

This module provides the foundational classes for building repositories in the CMEM client:

- RepositoryConfig: Configuration class that defines component type, fetch paths, and data adapters
- Repository: Abstract base class implementing a lazy-loading, read-only, dictionary-like interface
  for accessing CMEM resources with automatic data fetching and caching capabilities

**Classes:**

- [**Repository**](#cmem_client.repositories.base.abc.Repository) – ABC of a lazy loading, read-only, dictionary-mimicking repository
- [**RepositoryConfig**](#cmem_client.repositories.base.abc.RepositoryConfig) – Configuration class for a read repository.

**Attributes:**

- [**ItemType**](#cmem_client.repositories.base.abc.ItemType) –
- [**KeysViewType**](#cmem_client.repositories.base.abc.KeysViewType) –

## `ItemType` {#cmem_client.repositories.base.abc.ItemType}

```python
ItemType = TypeVar('ItemType', bound=ReadRepositoryItem)
```

## `KeysViewType` {#cmem_client.repositories.base.abc.KeysViewType}

```python
KeysViewType = KeysView[str]
```

## `Repository` {#cmem_client.repositories.base.abc.Repository}

```python
Repository(client)
```

Bases: <code>ABC</code>, <code>Mapping</code>

ABC of a lazy loading, read-only, dictionary-mimicking repository

**Attributes:**

- **_dict** (<code>dict[str, [Repository[ItemType]](#cmem_client.repositories.base.abc.Repository[ItemType])]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_config** (<code>[RepositoryConfig](#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which endpoint the repository fetches its data from.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.base.abc.Repository.fetch_data) – Fetch new data and update the repository
- [**items**](#cmem_client.repositories.base.abc.Repository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.base.abc.Repository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.base.abc.Repository.values) – Get the values of the repository

### `fetch_data` {#cmem_client.repositories.base.abc.Repository.fetch_data}

```python
fetch_data()
```

Fetch new data and update the repository

### `items` {#cmem_client.repositories.base.abc.Repository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.base.abc.Repository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.base.abc.Repository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.base.abc.Repository.values}

```python
values()
```

Get the values of the repository

## `RepositoryConfig` {#cmem_client.repositories.base.abc.RepositoryConfig}

```python
RepositoryConfig(component, fetch_data_path, fetch_data_adapter)
```

Configuration class for a read repository.

This class defines the essential configuration parameters needed to set up
a repository that can fetch data from CMEM components.

**Attributes:**

- [**component**](#cmem_client.repositories.base.abc.RepositoryConfig.component) (<code>Literal['build', 'explore', 'keycloak']</code>) – Which Corporate Memory API endpoint to address: ``build``, ``explore`` or ``keycloak``.
- [**fetch_data_path**](#cmem_client.repositories.base.abc.RepositoryConfig.fetch_data_path) (<code>str</code>) – API path used to retrieve the repository data.
- [**fetch_data_adapter**](#cmem_client.repositories.base.abc.RepositoryConfig.fetch_data_adapter) (<code>TypeAdapter</code>) – Pydantic TypeAdapter used to deserialize the API response.

### `component` {#cmem_client.repositories.base.abc.RepositoryConfig.component}

```python
component: Literal['build', 'explore', 'keycloak'] = component
```

### `fetch_data_adapter` {#cmem_client.repositories.base.abc.RepositoryConfig.fetch_data_adapter}

```python
fetch_data_adapter: TypeAdapter = fetch_data_adapter
```

### `fetch_data_path` {#cmem_client.repositories.base.abc.RepositoryConfig.fetch_data_path}

```python
fetch_data_path: str = fetch_data_path
```

