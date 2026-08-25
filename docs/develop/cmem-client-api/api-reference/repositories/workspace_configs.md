---
title: "workspace_configs"
tags:
  - API
  - Python
  - cmem-client
---

# `workspace_configs` {#cmem_client.repositories.workspace_configs}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the custom workspace configurations of DataIntegration.

Provides WorkspaceConfigsRepository for reading, creating, updating and deleting the
workspace configuration profiles, and for importing and exporting them as JSON. The
effective default profile is merged from the system and project defaults.

**Examples:**

List the profiles and read the effective default:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> list(client.workspace_configs)
>>> client.workspace_configs["default"]
>>> client.workspace_configs.project_default
```

Export a profile to a JSON file and import it into another deployment:

```pycon
>>> from pathlib import Path
>>> from cmem_client.repositories.protocols.import_item import ImportConflictPolicy
>>> from cmem_client.repositories.workspace_configs import WorkspaceConfigsImportConfig
>>> client.workspace_configs.export_item(key="default", path=Path("profiles.json"))
>>> client.workspace_configs.import_item(
...     path=Path("profiles.json"),
...     key="default",
...     on_conflict=ImportConflictPolicy.REPLACE,
...     configuration=WorkspaceConfigsImportConfig(replace_id=True),
... )
```

**Classes:**

- [**WorkspaceConfigsCreateConfig**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsCreateConfig) – Custom workspace configuration creation config.
- [**WorkspaceConfigsDeleteConfig**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsDeleteConfig) – Custom workspace configuration deletion config.
- [**WorkspaceConfigsExportConfig**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsExportConfig) – Custom workspace configuration export config.
- [**WorkspaceConfigsImportConfig**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig) – Custom workspace configuration import config.
- [**WorkspaceConfigsRepository**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository) – Repository for Explore (DataPlatform) workspace configurations.
- [**WorkspaceConfigsUpdateConfig**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsUpdateConfig) – Custom workspace configuration update config.

## `WorkspaceConfigsCreateConfig` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Custom workspace configuration creation config.

**Attributes:**

- **model_config** –

## `WorkspaceConfigsDeleteConfig` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Custom workspace configuration deletion config.

**Attributes:**

- **model_config** –

## `WorkspaceConfigsExportConfig` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsExportConfig}

Bases: <code>[ExportConfig](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Custom workspace configuration export config.

**Attributes:**

- **model_config** –

## `WorkspaceConfigsImportConfig` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig}

Bases: <code>[ImportConfig](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportConfig)</code>

Custom workspace configuration import config.

**Attributes:**

- [**use_archive_handler**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig.use_archive_handler) (<code>bool</code>) – Defaults to False here, unlike the base class, so the JSON file is
read directly instead of being unpacked by the ArchiveHandler.
- [**replace_id**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig.replace_id) (<code>bool</code>) – If True and the file contains exactly one configuration, adopt the given key
as its id instead of failing because no entry matches the key.

### `model_config` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `replace_id` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig.replace_id}

```python
replace_id: bool = False
```

### `use_archive_handler` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsImportConfig.use_archive_handler}

```python
use_archive_handler: bool = False
```

## `WorkspaceConfigsRepository` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>, <code>[ImportItemProtocol](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportItemProtocol)</code>, <code>[ExportItemProtocol](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>

Repository for Explore (DataPlatform) workspace configurations.

Provides access to all workspace configurations: the system default
(fetched from /api/conf/workspaces/systemDefault) followed by custom
workspace configurations (fetched from /api/conf/workspaces/customWorkspaces).
Custom workspace configurations support full CRUD operations.

**Functions:**

- [**create_item**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.delete_item) – Delete an item from the repository
- [**export_item**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**get_export_payload**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.get_export_payload) – Return the export-ready payload for the given profile ID.
- [**import_item**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.keys) – Get the keys of the repository
- [**migrate**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.migrate) – Trigger workspace configuration migration on the DataPlatform.
- [**raise_modification_error**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.raise_modification_error) – Raise an exception if needed
- [**update_item**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.logger) (<code>Logger</code>) – Gets the client logger
- [**project_default**](#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.project_default) (<code>[WorkspaceConfig](../models/workspace_config.md#cmem_client.models.workspace_config.WorkspaceConfig)</code>) – Return the raw project-level default overrides (not merged with system default).

### `create_item` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `delete_all` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `export_item` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.export_item}

```python
export_item(key, path=None, replace=False, configuration=None)
```

Export an item from the repository to a file path.

**Parameters:**

- **key** (<code>str</code>) – The key identifying the item to export.
- **path** (<code>Path | None</code>) – The target file path for export. If None, a path will be generated.
- **replace** (<code>bool</code>) – Whether to replace existing files at the target path.
- **configuration** (<code>[ExportItemConfig_contra](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) | None</code>) – Optional configuration for export behavior.

**Returns:**

- <code>Path</code> – The actual path where the item was exported.

**Raises:**

- <code>[RepositoryItemNotFoundError](../exceptions.md#cmem_client.exceptions.RepositoryItemNotFoundError)</code> – If the specified item key is not found.
- <code>[RepositoryReadError](../exceptions.md#cmem_client.exceptions.RepositoryReadError)</code> – If there's an error during export or path mismatch.

### `fetch_data` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `get_export_payload` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.get_export_payload}

```python
get_export_payload(key)
```

Return the export-ready payload for the given profile ID.

For the default workspace, returns the raw project-level overrides
(not merged with system defaults) to ensure a clean export/import round-trip.
For custom workspaces, returns the full config excluding the computed label.

**Parameters:**

- **key** (<code>str</code>) – The profile ID of the workspace configuration to serialize.

**Returns:**

- <code>dict</code> – A dict ready for JSON serialization.

### `import_item` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.import_item}

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

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item already exists and the conflict
policy is FAIL, if the import type is not allowed for this repository, if
the import request failed, or if the item is not present afterwards.

### `items` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `migrate` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.migrate}

```python
migrate()
```

Trigger workspace configuration migration on the DataPlatform.

Instructs the DataPlatform to migrate all workspace configurations
that are flagged as needing migration (reported in StatusInfo.explore.workspaces_to_migrate).

**Raises:**

- <code>HTTPStatusError</code> – If the migration request fails.

### `project_default` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.project_default}

```python
project_default: WorkspaceConfig
```

Return the raw project-level default overrides (not merged with system default).

Use this for export to preserve the round-trip: export raw overrides,
import back to projectDefault without accumulating redundant system values.

### `raise_modification_error` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `update_item` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

### `values` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsRepository.values}

```python
values()
```

Get the values of the repository

## `WorkspaceConfigsUpdateConfig` {#cmem_client.repositories.workspace_configs.WorkspaceConfigsUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Custom workspace configuration update config.

**Attributes:**

- **model_config** –

