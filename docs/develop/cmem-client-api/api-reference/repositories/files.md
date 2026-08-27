---
title: "cmem-client: files module"
description: "Repository for the file resources of DataIntegration projects."
tags:
  - API
  - Python
  - cmem-client
---

# `files` {#cmem_client.repositories.files}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the file resources of DataIntegration projects.

Provides FilesRepository for uploading, reading, exporting and deleting the files of a
project. Items are keyed by the composite key ``project_id:file_path``, so a single
repository spans the files of all projects.

**Examples:**

Upload a local file into a project and read it back:

```pycon
>>> from pathlib import Path
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.files.import_item(
...     path=Path("customers.csv"), key="my-project:customers.csv"
... )
>>> client.files.read("my-project:customers.csv")
```

List the files of a single project and inspect one of them:

```pycon
>>> for resource in client.files.get_resources("my-project"):
...     print(resource.name)
>>> client.files.delete_item("my-project:customers.csv")
```

**Classes:**

- [**FilesDeleteConfig**](#cmem_client.repositories.files.FilesDeleteConfig) – Files Delete Configuration.
- [**FilesExportConfig**](#cmem_client.repositories.files.FilesExportConfig) – Files Export Configuration.
- [**FilesImportConfig**](#cmem_client.repositories.files.FilesImportConfig) – Files Import Configuration.
- [**FilesRepository**](#cmem_client.repositories.files.FilesRepository) – Repository for files

## `FilesDeleteConfig` {#cmem_client.repositories.files.FilesDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Files Delete Configuration.

**Attributes:**

- **model_config** –

## `FilesExportConfig` {#cmem_client.repositories.files.FilesExportConfig}

Bases: <code>[ExportConfig](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Files Export Configuration.

**Attributes:**

- **model_config** –

## `FilesImportConfig` {#cmem_client.repositories.files.FilesImportConfig}

Bases: <code>[ImportConfig](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportConfig)</code>

Files Import Configuration.

**Attributes:**

- [**use_archive_handler**](#cmem_client.repositories.files.FilesImportConfig.use_archive_handler) (<code>bool</code>) – Defaults to False here, unlike the base class, so a path is
imported as a single file instead of being unpacked by the ArchiveHandler.
- [**remote_file_url**](#cmem_client.repositories.files.FilesImportConfig.remote_file_url) (<code>str | None</code>) – URL to stream the file content from instead of reading it from a local
path. If set, the path argument may be omitted.

### `model_config` {#cmem_client.repositories.files.FilesImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `remote_file_url` {#cmem_client.repositories.files.FilesImportConfig.remote_file_url}

```python
remote_file_url: str | None = None
```

### `use_archive_handler` {#cmem_client.repositories.files.FilesImportConfig.use_archive_handler}

```python
use_archive_handler: bool = False
```

## `FilesRepository` {#cmem_client.repositories.files.FilesRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[ImportItemProtocol](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportItemProtocol)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[ExportItemProtocol](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>

Repository for files

**Functions:**

- [**delete_all**](#cmem_client.repositories.files.FilesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.files.FilesRepository.delete_item) – Delete an item from the repository
- [**export_item**](#cmem_client.repositories.files.FilesRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.files.FilesRepository.fetch_data) – Fetch all file resources from all projects.
- [**get_resource_metadata**](#cmem_client.repositories.files.FilesRepository.get_resource_metadata) – Retrieve metadata of a single resource
- [**get_resource_usage**](#cmem_client.repositories.files.FilesRepository.get_resource_usage) – Retrieve usage of a single resource
- [**get_resources**](#cmem_client.repositories.files.FilesRepository.get_resources) – Fetch the list of file resources for a specific project.
- [**import_item**](#cmem_client.repositories.files.FilesRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.files.FilesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.files.FilesRepository.keys) – Get the keys of the repository
- [**read**](#cmem_client.repositories.files.FilesRepository.read) – Read the content of a file into memory.
- [**values**](#cmem_client.repositories.files.FilesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.files.FilesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `delete_all` {#cmem_client.repositories.files.FilesRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.files.FilesRepository.delete_item}

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

### `export_item` {#cmem_client.repositories.files.FilesRepository.export_item}

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

### `fetch_data` {#cmem_client.repositories.files.FilesRepository.fetch_data}

```python
fetch_data()
```

Fetch all file resources from all projects.

### `get_resource_metadata` {#cmem_client.repositories.files.FilesRepository.get_resource_metadata}

```python
get_resource_metadata(resource)
```

Retrieve metadata of a single resource

### `get_resource_usage` {#cmem_client.repositories.files.FilesRepository.get_resource_usage}

```python
get_resource_usage(resource)
```

Retrieve usage of a single resource

### `get_resources` {#cmem_client.repositories.files.FilesRepository.get_resources}

```python
get_resources(project_id)
```

Fetch the list of file resources for a specific project.

### `import_item` {#cmem_client.repositories.files.FilesRepository.import_item}

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

### `items` {#cmem_client.repositories.files.FilesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.files.FilesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.files.FilesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `read` {#cmem_client.repositories.files.FilesRepository.read}

```python
read(key)
```

Read the content of a file into memory.

**Parameters:**

- **key** (<code>str</code>) – Composite key in format 'project_id:file_path'

**Returns:**

- <code>bytes</code> – The raw content of the file.

**Raises:**

- <code>[FilesReadError](../exceptions.md#cmem_client.exceptions.FilesReadError)</code> – If the key is malformed or the request fails.
- <code>[FilesNotFoundError](../exceptions.md#cmem_client.exceptions.FilesNotFoundError)</code> – If the file does not exist in the project.

### `values` {#cmem_client.repositories.files.FilesRepository.values}

```python
values()
```

Get the values of the repository

