---
title: "projects"
tags:
  - API
  - Python
  - cmem-client
---

# `projects` {#cmem_client.repositories.projects}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for managing DataIntegration projects.

Provides ProjectsRepository for creating, deleting, importing and exporting build
projects, and for reloading a project and reading its failed task report.

**Examples:**

Create a project and list the projects of the workspace:

```pycon
>>> from cmem_client.client import Client
>>> from cmem_client.models.project import Project
>>> client = Client.from_env()
>>> client.projects.create_item(
...     Project(name="my-project", meta_data={"label": "My Project"}),
...     skip_if_existing=True,
... )
>>> list(client.projects)
```

Export a project to a ZIP archive and reload it afterwards:

```pycon
>>> from pathlib import Path
>>> client.projects.export_item(key="my-project", path=Path("my-project.zip"))
>>> client.projects.reload_project("my-project")
```

Find out which tasks of a project failed to load:

```pycon
>>> for failed in client.projects.get_failed_tasks_report("my-project"):
...     print(failed)
```

**Classes:**

- [**ProjectImportStatus**](#cmem_client.repositories.projects.ProjectImportStatus) – Response of the project import status endpoint.
- [**ProjectsCreateConfig**](#cmem_client.repositories.projects.ProjectsCreateConfig) – Project Create Configuration.
- [**ProjectsDeleteConfig**](#cmem_client.repositories.projects.ProjectsDeleteConfig) – Project Delete Configuration.
- [**ProjectsExportConfig**](#cmem_client.repositories.projects.ProjectsExportConfig) – Project Export Configuration.
- [**ProjectsImportConfig**](#cmem_client.repositories.projects.ProjectsImportConfig) – Project Import Configuration.
- [**ProjectsRepository**](#cmem_client.repositories.projects.ProjectsRepository) – Repository for Build (DataIntegration) projects.

## `ProjectImportStatus` {#cmem_client.repositories.projects.ProjectImportStatus}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Response of the project import status endpoint.

**Attributes:**

- [**project_id**](#cmem_client.repositories.projects.ProjectImportStatus.project_id) (<code>str</code>) – Identifier of the imported project, sent as ``projectId``.
- [**success**](#cmem_client.repositories.projects.ProjectImportStatus.success) (<code>bool | None</code>) – Whether the import finished successfully. None while the import is still
running, which is what ``import_item()`` polls on.
- [**failure_message**](#cmem_client.repositories.projects.ProjectImportStatus.failure_message) (<code>str | None</code>) – Reason the import failed, sent as ``failureMessage``. Only set when
the import failed.

### `failure_message` {#cmem_client.repositories.projects.ProjectImportStatus.failure_message}

```python
failure_message: str | None = Field(alias='failureMessage', default=None)
```

### `model_config` {#cmem_client.repositories.projects.ProjectImportStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_id` {#cmem_client.repositories.projects.ProjectImportStatus.project_id}

```python
project_id: str = Field(alias='projectId')
```

### `success` {#cmem_client.repositories.projects.ProjectImportStatus.success}

```python
success: bool | None = None
```

## `ProjectsCreateConfig` {#cmem_client.repositories.projects.ProjectsCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Project Create Configuration.

**Attributes:**

- **model_config** –

## `ProjectsDeleteConfig` {#cmem_client.repositories.projects.ProjectsDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Project Delete Configuration.

**Attributes:**

- **model_config** –

## `ProjectsExportConfig` {#cmem_client.repositories.projects.ProjectsExportConfig}

Bases: <code>[ExportConfig](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Project Export Configuration.

**Attributes:**

- [**marshalling_plugin**](#cmem_client.repositories.projects.ProjectsExportConfig.marshalling_plugin) (<code>Literal['xmlZip', 'xmlZipWithoutResources']</code>) – Export format plugin. ``xmlZip`` includes the project resources,
``xmlZipWithoutResources`` omits them.
- [**extract_project_zip**](#cmem_client.repositories.projects.ProjectsExportConfig.extract_project_zip) (<code>bool</code>) – If True, extract the exported archive into the given path as a
directory instead of writing a single zip file.
- [**include_access_conditions**](#cmem_client.repositories.projects.ProjectsExportConfig.include_access_conditions) (<code>bool</code>) – If True, export the access conditions of the project.
Sent as ``exportGroups``.
- [**export_user_data**](#cmem_client.repositories.projects.ProjectsExportConfig.export_user_data) (<code>bool</code>) – If True, include user data in the export. Sent as ``exportUserData``.

### `export_user_data` {#cmem_client.repositories.projects.ProjectsExportConfig.export_user_data}

```python
export_user_data: bool = True
```

### `extract_project_zip` {#cmem_client.repositories.projects.ProjectsExportConfig.extract_project_zip}

```python
extract_project_zip: bool = False
```

### `include_access_conditions` {#cmem_client.repositories.projects.ProjectsExportConfig.include_access_conditions}

```python
include_access_conditions: bool = False
```

### `marshalling_plugin` {#cmem_client.repositories.projects.ProjectsExportConfig.marshalling_plugin}

```python
marshalling_plugin: Literal['xmlZip', 'xmlZipWithoutResources'] = 'xmlZip'
```

### `model_config` {#cmem_client.repositories.projects.ProjectsExportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `ProjectsImportConfig` {#cmem_client.repositories.projects.ProjectsImportConfig}

Bases: <code>[ImportConfig](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportConfig)</code>

Project Import Configuration.

**Attributes:**

- [**use_archive_handler**](#cmem_client.repositories.projects.ProjectsImportConfig.use_archive_handler) (<code>bool</code>) – Defaults to False here, unlike the base class, so the project archive
is passed to the API as-is instead of being unpacked by the ArchiveHandler.
- [**include_access_conditions**](#cmem_client.repositories.projects.ProjectsImportConfig.include_access_conditions) (<code>bool</code>) – If True, import the access conditions contained in the archive.
Sent as ``importGroups``.

### `include_access_conditions` {#cmem_client.repositories.projects.ProjectsImportConfig.include_access_conditions}

```python
include_access_conditions: bool = False
```

### `model_config` {#cmem_client.repositories.projects.ProjectsImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `use_archive_handler` {#cmem_client.repositories.projects.ProjectsImportConfig.use_archive_handler}

```python
use_archive_handler: bool = False
```

## `ProjectsRepository` {#cmem_client.repositories.projects.ProjectsRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[ImportItemProtocol](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportItemProtocol)</code>, <code>[ExportItemProtocol](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>

Repository for Build (DataIntegration) projects.

This repository manages Build (DataIntegration) projects which are described with
the [Project model](../models/project.md#cmem_client.models.project.Project).

**Functions:**

- [**create_item**](#cmem_client.repositories.projects.ProjectsRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.projects.ProjectsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.projects.ProjectsRepository.delete_item) – Delete an item from the repository
- [**export_item**](#cmem_client.repositories.projects.ProjectsRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.projects.ProjectsRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**get_failed_tasks_report**](#cmem_client.repositories.projects.ProjectsRepository.get_failed_tasks_report) – Get all failed tasks from project from its ID
- [**import_item**](#cmem_client.repositories.projects.ProjectsRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.projects.ProjectsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.projects.ProjectsRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.projects.ProjectsRepository.raise_modification_error) – Raise an exception if needed
- [**reload_project**](#cmem_client.repositories.projects.ProjectsRepository.reload_project) – Reload all task from project from its ID
- [**values**](#cmem_client.repositories.projects.ProjectsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.projects.ProjectsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.projects.ProjectsRepository.create_item}

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

### `delete_all` {#cmem_client.repositories.projects.ProjectsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.projects.ProjectsRepository.delete_item}

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

### `export_item` {#cmem_client.repositories.projects.ProjectsRepository.export_item}

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

### `fetch_data` {#cmem_client.repositories.projects.ProjectsRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `get_failed_tasks_report` {#cmem_client.repositories.projects.ProjectsRepository.get_failed_tasks_report}

```python
get_failed_tasks_report(project_id)
```

Get all failed tasks from project from its ID

### `import_item` {#cmem_client.repositories.projects.ProjectsRepository.import_item}

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

### `items` {#cmem_client.repositories.projects.ProjectsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.projects.ProjectsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.projects.ProjectsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.projects.ProjectsRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `reload_project` {#cmem_client.repositories.projects.ProjectsRepository.reload_project}

```python
reload_project(project_id)
```

Reload all task from project from its ID

### `values` {#cmem_client.repositories.projects.ProjectsRepository.values}

```python
values()
```

Get the values of the repository

