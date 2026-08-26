---
title: "cmem-client: create_item module"
tags:
  - API
  - Python
  - cmem-client
---

# `create_item` {#cmem_client.repositories.protocols.create_item}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Protocol interface for repository item creation operations.

This module defines the CreateItemProtocol that repositories can implement
to provide item creation capabilities. It includes comprehensive error handling
for different API response formats and automatic repository refresh after
successful creation.

The protocol handles both DataIntegration (build) and DataPlatform (explore)
API error formats, providing consistent error reporting across different
Corporate Memory components.

**Classes:**

- [**CreateConfig**](#cmem_client.repositories.protocols.create_item.CreateConfig) – Abstract base class for repository item creation configurations.
- [**CreateItemProtocol**](#cmem_client.repositories.protocols.create_item.CreateItemProtocol) – Protocol which allows for creation of new items

**Attributes:**

- [**CreateItemConfig_contra**](#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) –

## `CreateConfig` {#cmem_client.repositories.protocols.create_item.CreateConfig}

Bases: <code>[Model](../../models/base.md#cmem_client.models.base.Model)</code>, <code>ABC</code>

Abstract base class for repository item creation configurations.

**Attributes:**

- **model_config** –

## `CreateItemConfig_contra` {#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra}

```python
CreateItemConfig_contra = TypeVar('CreateItemConfig_contra', bound=CreateConfig, contravariant=True)
```

## `CreateItemProtocol` {#cmem_client.repositories.protocols.create_item.CreateItemProtocol}

Bases: <code>Protocol[[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType), [CreateItemConfig_contra](#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra)]</code>

Protocol which allows for creation of new items

**Attributes:**

- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_dict** (<code>dict[str, [ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_config** (<code>[RepositoryConfig](../../repositories/base/abc.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which endpoint the repository fetches its data from.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**create_item**](#cmem_client.repositories.protocols.create_item.CreateItemProtocol.create_item) – Create (add) a new item to the repository
- [**fetch_data**](#cmem_client.repositories.protocols.create_item.CreateItemProtocol.fetch_data) – Fetch new data and update the repository
- [**raise_modification_error**](#cmem_client.repositories.protocols.create_item.CreateItemProtocol.raise_modification_error) – Raise an exception if needed

### `create_item` {#cmem_client.repositories.protocols.create_item.CreateItemProtocol.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `fetch_data` {#cmem_client.repositories.protocols.create_item.CreateItemProtocol.fetch_data}

```python
fetch_data()
```

Fetch new data and update the repository

### `logger` {#cmem_client.repositories.protocols.create_item.CreateItemProtocol.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.protocols.create_item.CreateItemProtocol.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

