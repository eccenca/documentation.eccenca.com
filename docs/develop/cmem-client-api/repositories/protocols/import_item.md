# `import_item` {#cmem_client.repositories.protocols.import_item}

Protocol interface for repository item import operations.

This module defines the ImportItemProtocol that repositories can implement
to support importing items from files. This is commonly used for importing
exported projects, graphs, or other resources into Corporate Memory.

The protocol supports replacement, skip-if-existing, fail-if-existing, and
merge behaviours, controlled via the on_conflict parameter on import_item().

**Examples:**

A repository declares which import items it accepts and which import
configuration applies when the caller passes none:

```pycon
>>> from collections.abc import Sequence
>>> from typing import ClassVar
>>> from cmem_client.models.item import FileImportItem, ImportItem, ZipImportItem
>>> from cmem_client.repositories.base.plain_list import PlainListRepository
>>> from cmem_client.repositories.projects import ProjectsImportConfig
>>> from cmem_client.repositories.protocols.import_item import (
...     ImportConfig,
...     ImportItemProtocol,
... )
>>> class ProjectsRepository(PlainListRepository, ImportItemProtocol):
...     _allowed_import_items: ClassVar[Sequence[type[ImportItem]]] = [
...         FileImportItem,
...         ZipImportItem,
...     ]
...     _default_import_config: ImportConfig | None = ProjectsImportConfig()
```

**Classes:**

- [**ImportConfig**](#cmem_client.repositories.protocols.import_item.ImportConfig) – Abstract base class for Import Item Configuration Objects
- [**ImportConflictPolicy**](#cmem_client.repositories.protocols.import_item.ImportConflictPolicy) – Controls behavior when the import target already exists.
- [**ImportItemProtocol**](#cmem_client.repositories.protocols.import_item.ImportItemProtocol) – Protocol which allows for importing of items from a file path.

**Attributes:**

- [**ImportItemConfig_contra**](#cmem_client.repositories.protocols.import_item.ImportItemConfig_contra) – 

## `ImportConfig` {#cmem_client.repositories.protocols.import_item.ImportConfig}

Bases: <code>[Model](../../models/base.md#cmem_client.models.base.Model)</code>, <code>ABC</code>

Abstract base class for Import Item Configuration Objects

**Attributes:**

- [**use_archive_handler**](#cmem_client.repositories.protocols.import_item.ImportConfig.use_archive_handler) (<code>bool</code>) – When True, automatically uses ArchiveHandler to handle
zip files, directories, and single files transparently.

### `model_config` {#cmem_client.repositories.protocols.import_item.ImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `use_archive_handler` {#cmem_client.repositories.protocols.import_item.ImportConfig.use_archive_handler}

```python
use_archive_handler: bool = True
```

## `ImportConflictPolicy` {#cmem_client.repositories.protocols.import_item.ImportConflictPolicy}

Bases: <code>StrEnum</code>

Controls behavior when the import target already exists.

REPLACE: Delete the existing item, then import the new one.
SKIP: Leave the existing item untouched and return without importing.
FAIL: Raise an error if the item already exists.
MERGE: Add the imported data to the existing item without clearing it first.

**Attributes:**

- [**FAIL**](#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.FAIL) – 
- [**MERGE**](#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.MERGE) – 
- [**REPLACE**](#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.REPLACE) – 
- [**SKIP**](#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.SKIP) – 

### `FAIL` {#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.FAIL}

```python
FAIL = 'fail'
```

### `MERGE` {#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.MERGE}

```python
MERGE = 'merge'
```

### `REPLACE` {#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.REPLACE}

```python
REPLACE = 'replace'
```

### `SKIP` {#cmem_client.repositories.protocols.import_item.ImportConflictPolicy.SKIP}

```python
SKIP = 'skip'
```

## `ImportItemConfig_contra` {#cmem_client.repositories.protocols.import_item.ImportItemConfig_contra}

```python
ImportItemConfig_contra = TypeVar('ImportItemConfig_contra', bound=ImportConfig, contravariant=True)
```

## `ImportItemProtocol` {#cmem_client.repositories.protocols.import_item.ImportItemProtocol}

Bases: <code>Protocol[[ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType), [ImportItemConfig_contra](#cmem_client.repositories.protocols.import_item.ImportItemConfig_contra)]</code>

Protocol which allows for importing of items from a file path.

**Attributes:**

- **_client** (<code>[Client](../../index.md#cmem_client.client.Client)</code>) – Corporate Memory client used for the HTTP requests of this repository.
- **_dict** (<code>dict[str, [ItemType](../../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)]</code>) – Cached contents of the repository, mapping the key of each item to the item
itself. Backs the Mapping interface and is populated by ``fetch_data()``.
- **_allowed_import_items** (<code>Sequence[type[[ImportItem](../../models/item.md#cmem_client.models.item.ImportItem)]]</code>) – ImportItem types this repository accepts. Repositories may
declare it to narrow or widen what ``import_item()`` takes. If not defined,
defaults to ``FileImportItem`` and ``ZipImportItem``, which excludes
``DirectoryImportItem``.
- **_default_import_config** (<code>[ImportConfig](#cmem_client.repositories.protocols.import_item.ImportConfig) | None</code>) – Import configuration applied when the caller passes none.
Repositories declare it for example when ``use_archive_handler`` has to be turned
off. If not defined, defaults to None.
- **_logger** (<code>Logger</code>) – Logger of this repository, created lazily on first access through the
``logger`` property as a child of the client logger.

**Functions:**

- [**import_item**](#cmem_client.repositories.protocols.import_item.ImportItemProtocol.import_item) – Import an exported file to the repository

### `import_item` {#cmem_client.repositories.protocols.import_item.ImportItemProtocol.import_item}

```python
import_item(path=None, key=None, on_conflict=ImportConflictPolicy.FAIL, configuration=None)
```

Import an exported file to the repository

By default, automatically handles zip files, directories, and single files
using ImportItem model. Can be disabled by setting use_archive_handler=False
in the configuration.

**Returns:**

- <code>str</code> – The key of the imported item.

**Raises:**

- <code>[RepositoryModificationError](../../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item already exists and the conflict
policy is FAIL, if the import type is not allowed for this repository, if
the import request failed, or if the item is not present afterwards.

### `logger` {#cmem_client.repositories.protocols.import_item.ImportItemProtocol.logger}

```python
logger: logging.Logger
```

Gets the client logger

