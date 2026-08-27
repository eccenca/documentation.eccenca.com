---
title: "cmem-client: export_item module"
description: "Protocol interface for repository item export operations."
tags:
  - API
  - Python
  - cmem-client
---

# `export_item` {#cmem_client.repositories.protocols.export_item}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Protocol interface for repository item export operations.

This module defines the ExportItemProtocol that repositories can implement
to support exporting items to files.

**Classes:**

- [**ExportConfig**](#cmem_client.repositories.protocols.export_item.ExportConfig) – Abstract base class for Export Item Configuration Objects
- [**ExportItemProtocol**](#cmem_client.repositories.protocols.export_item.ExportItemProtocol) – Protocol which allows for exporting of items to a file path.

**Attributes:**

- [**ExportItemConfig_contra**](#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) –

## `ExportConfig` {#cmem_client.repositories.protocols.export_item.ExportConfig}

Bases: <code>[Model](../../models/base.md#cmem_client.models.base.Model)</code>, <code>ABC</code>

Abstract base class for Export Item Configuration Objects

**Attributes:**

- **model_config** –

## `ExportItemConfig_contra` {#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra}

```python
ExportItemConfig_contra = TypeVar('ExportItemConfig_contra', bound=ExportConfig, contravariant=True)
```

## `ExportItemProtocol` {#cmem_client.repositories.protocols.export_item.ExportItemProtocol}

Bases: <code>Protocol[[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType), [ExportItemConfig_contra](#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra)]</code>

Protocol which allows for exporting of items to a file path.

This protocol defines the interface that repositories must implement to support
exporting items to files. It provides both a public interface method and requires
implementation of a concrete export method.

**Attributes:**

- **_client** (<code>[Client](../../client.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_dict** (<code>dict[str, [ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**export_item**](#cmem_client.repositories.protocols.export_item.ExportItemProtocol.export_item) – Export an item from the repository to a file path.

### `export_item` {#cmem_client.repositories.protocols.export_item.ExportItemProtocol.export_item}

```python
export_item(key, path=None, replace=False, configuration=None)
```

Export an item from the repository to a file path.

**Parameters:**

- **key** (<code>str</code>) – The key identifying the item to export.
- **path** (<code>Path | None</code>) – The target file path for export. If None, a path will be generated.
- **replace** (<code>bool</code>) – Whether to replace existing files at the target path.
- **configuration** (<code>[ExportItemConfig_contra](#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) | None</code>) – Optional configuration for export behavior.

**Returns:**

- <code>Path</code> – The actual path where the item was exported.

**Raises:**

- <code>[RepositoryItemNotFoundError](../../exceptions.md#cmem_client.exceptions.RepositoryItemNotFoundError)</code> – If the specified item key is not found.
- <code>[RepositoryReadError](../../exceptions.md#cmem_client.exceptions.RepositoryReadError)</code> – If there's an error during export or path mismatch.

### `logger` {#cmem_client.repositories.protocols.export_item.ExportItemProtocol.logger}

```python
logger: logging.Logger
```

Gets the client logger

