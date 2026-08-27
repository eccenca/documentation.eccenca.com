---
title: "cmem-client: update_item module"
description: "Protocol interface for repository item update operations."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.protocols.update_item` {#cmem_client.repositories.protocols.update_item}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Protocol interface for repository item update operations.

This module defines the UpdateItemProtocol that repositories can implement
to provide item update capabilities. It includes error handling and automatic
repository refresh after successful updates.

The protocol handles both DataIntegration (build) and DataPlatform (explore)
API error formats, providing consistent error reporting across different
Corporate Memory components.

**Classes:**

- [**UpdateConfig**](#cmem_client.repositories.protocols.update_item.UpdateConfig) – Abstract base class for repository item update configurations.
- [**UpdateItemProtocol**](#cmem_client.repositories.protocols.update_item.UpdateItemProtocol) – Protocol which allows for updating of existing items.

**Attributes:**

- [**UpdateItemConfig_contra**](#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) –

## `UpdateConfig` {#cmem_client.repositories.protocols.update_item.UpdateConfig}

Bases: <code>[Model](../../models/base.md#cmem_client.models.base.Model)</code>, <code>ABC</code>

Abstract base class for repository item update configurations.

**Attributes:**

- **model_config** –

## `UpdateItemConfig_contra` {#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra}

```python
UpdateItemConfig_contra = TypeVar('UpdateItemConfig_contra', bound=UpdateConfig, contravariant=True)
```

## `UpdateItemProtocol` {#cmem_client.repositories.protocols.update_item.UpdateItemProtocol}

Bases: <code>Protocol[[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType), [UpdateItemConfig_contra](#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra)]</code>

Protocol which allows for updating of existing items.

**Attributes:**

- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_dict** (<code>dict[str, [ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_config** (<code>[RepositoryConfig](../../repositories/base/abc.md#cmem_client.repositories.base.abc.RepositoryConfig)</code>) – Describes which endpoint the repository fetches its data from.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.protocols.update_item.UpdateItemProtocol.fetch_data) – Fetch new data and update the repository
- [**update_item**](#cmem_client.repositories.protocols.update_item.UpdateItemProtocol.update_item) – Update an existing item in the repository.

### `fetch_data` {#cmem_client.repositories.protocols.update_item.UpdateItemProtocol.fetch_data}

```python
fetch_data()
```

Fetch new data and update the repository

### `logger` {#cmem_client.repositories.protocols.update_item.UpdateItemProtocol.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `update_item` {#cmem_client.repositories.protocols.update_item.UpdateItemProtocol.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

