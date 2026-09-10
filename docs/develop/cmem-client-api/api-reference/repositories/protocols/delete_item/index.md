---
title: "cmem-client: repositories.protocols.delete_item module"
description: "Protocol interface for repository item deletion operations."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.protocols.delete_item` {#cmem_client.repositories.protocols.delete_item}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Protocol interface for repository item deletion operations.

This module defines the DeleteItemProtocol that repositories can implement
to provide item deletion capabilities. It includes validation to ensure items
exist before deletion and provides both individual and bulk deletion methods.

The protocol implements the Python **delitem** method to support standard
dictionary-style deletion syntax while providing comprehensive error handling
for HTTP communication failures.

**Classes:**

- [**DeleteConfig**](#cmem_client.repositories.protocols.delete_item.DeleteConfig) – Abstract base class for repository item deletion configurations.
- [**DeleteItemProtocol**](#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol) – Protocol which allows for deletion of items

**Attributes:**

- [**DeleteItemConfig_contra**](#cmem_client.repositories.protocols.delete_item.DeleteItemConfig_contra) –

## `DeleteConfig` {#cmem_client.repositories.protocols.delete_item.DeleteConfig}

Bases: <code>[Model](../../../models/base/index.md#cmem_client.models.base.Model)</code>, <code>ABC</code>

Abstract base class for repository item deletion configurations.

**Attributes:**

- **model_config** –

## `DeleteItemConfig_contra` {#cmem_client.repositories.protocols.delete_item.DeleteItemConfig_contra}

```python
DeleteItemConfig_contra = TypeVar('DeleteItemConfig_contra', bound=DeleteConfig, contravariant=True)
```

## `DeleteItemProtocol` {#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol}

Bases: <code>Protocol[[ItemType](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.ItemType), [DeleteItemConfig_contra](#cmem_client.repositories.protocols.delete_item.DeleteItemConfig_contra)]</code>

Protocol which allows for deletion of items

**Attributes:**

- **_client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_dict** (<code>dict[str, [ItemType](../../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.ItemType)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**delete_all**](#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol.delete_item) – Delete an item from the repository

### `delete_all` {#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `logger` {#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol.logger}

```python
logger: logging.Logger
```

Gets the client logger

