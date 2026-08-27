---
title: "cmem-client: repositories.marketplace_packages module"
description: "Repository for the marketplace packages installed in Corporate Memory."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.marketplace_packages` {#cmem_client.repositories.marketplace_packages}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the marketplace packages installed in Corporate Memory.

Provides MarketplacePackagesRepository for installing packages from an archive or
directory, exporting an installed package again and removing one. The packages
available on a marketplace server are offered by the Marketplace component
(``client.marketplace``) instead.

**Examples:**

List the installed packages:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> list(client.marketplace_packages)
```

Install a package archive and export an installed package:

```pycon
>>> from pathlib import Path
>>> from cmem_client.repositories.marketplace_packages import (
...     MarketplacePackagesExportConfig,
...     MarketplacePackagesImportConfig,
... )
>>> from cmem_client.repositories.protocols.import_item import ImportConflictPolicy
>>> client.marketplace_packages.import_item(
...     key="w3c-geo-vocab",
...     configuration=MarketplacePackagesImportConfig(install_from_marketplace=True),
...     on_conflict=ImportConflictPolicy.REPLACE
... )
>>> client.marketplace_packages.export_item(
...     key="w3c-geo-vocab",
...     path=Path("w3c-geo-vocab"),
...     configuration=MarketplacePackagesExportConfig(export_as_zip=False),
... )
>>> client.marketplace_packages.delete_item(key="w3c-geo-vocab", skip_if_missing=True)
```

**Classes:**

- [**MarketplacePackagesDeleteConfig**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig) – Package deletion configuration
- [**MarketplacePackagesExportConfig**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig) – Package export configuration
- [**MarketplacePackagesImportConfig**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig) – Configuration for marketplace package import operations.
- [**MarketplacePackagesRepository**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository) – Repository for marketplace package operations.

**Functions:**

- [**get_installation_metadata_query**](#cmem_client.repositories.marketplace_packages.get_installation_metadata_query) – Get the query for the installation metadata of the package.

**Attributes:**

- [**LOCK_FILE_RESOURCE**](#cmem_client.repositories.marketplace_packages.LOCK_FILE_RESOURCE) –
- [**MAX_DEPENDENCY_DEPTH**](#cmem_client.repositories.marketplace_packages.MAX_DEPENDENCY_DEPTH) –

## `LOCK_FILE_RESOURCE` {#cmem_client.repositories.marketplace_packages.LOCK_FILE_RESOURCE}

```python
LOCK_FILE_RESOURCE = f'{MARKETPLACE_PROJECT_ID}:mp-lock.json'
```

## `MAX_DEPENDENCY_DEPTH` {#cmem_client.repositories.marketplace_packages.MAX_DEPENDENCY_DEPTH}

```python
MAX_DEPENDENCY_DEPTH = 5
```

## `MarketplacePackagesDeleteConfig` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig}

Bases: <code>[DeleteConfig](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Package deletion configuration

**Attributes:**

- [**skip_missing_dependencies**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_dependencies) (<code>bool</code>) – If True, dependencies which are not installed are skipped
instead of raising an error.
- [**skip_missing_graphs**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_graphs) (<code>bool</code>) – If True, graphs of the package which do not exist are skipped
instead of raising an error.
- [**skip_missing_projects**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_projects) (<code>bool</code>) – If True, projects of the package which do not exist are skipped
instead of raising an error.
- [**ignore_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_lock) (<code>bool</code>) – If set to True, ignore the lock mechanism.
- [**ignore_dependencies**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_dependencies) (<code>bool</code>) – If True, dependencies of the package are not deleted.
- [**dependency_level**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.dependency_level) (<code>int</code>) – Current recursion depth for dependency resolution. Used internally to
identify the top-level call. Should not be set manually.

### `dependency_level` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.dependency_level}

```python
dependency_level: int = 0
```

### `ignore_dependencies` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_dependencies}

```python
ignore_dependencies: bool = False
```

### `ignore_lock` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_lock}

```python
ignore_lock: bool = False
```

### `model_config` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `skip_missing_dependencies` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_dependencies}

```python
skip_missing_dependencies: bool = True
```

### `skip_missing_graphs` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_graphs}

```python
skip_missing_graphs: bool = True
```

### `skip_missing_projects` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_projects}

```python
skip_missing_projects: bool = True
```

## `MarketplacePackagesExportConfig` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig}

Bases: <code>[ExportConfig](../../repositories/protocols/export_item/index.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Package export configuration

**Attributes:**

- [**export_graph_serialization**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig.export_graph_serialization) (<code>Literal['turtle', 'pretty-turtle']</code>) – Graph export serialization format.
- [**export_as_zip**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig.export_as_zip) (<code>bool</code>) – If true, export the package as a zip file, otherwise as a directory.

### `export_as_zip` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig.export_as_zip}

```python
export_as_zip: bool = True
```

### `export_graph_serialization` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig.export_graph_serialization}

```python
export_graph_serialization: LiteralType['turtle', 'pretty-turtle'] = 'pretty-turtle'
```

### `model_config` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesExportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `MarketplacePackagesImportConfig` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig}

Bases: <code>[ImportConfig](../../repositories/protocols/import_item/index.md#cmem_client.repositories.protocols.import_item.ImportConfig)</code>

Configuration for marketplace package import operations.

**Attributes:**

- [**ignore_dependencies**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.ignore_dependencies) (<code>bool</code>) – If True, skips installation of package dependencies.
- [**install_from_marketplace**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.install_from_marketplace) (<code>bool</code>) – If True, downloads packages from the marketplace server.
If False, loads packages from local filesystem.
- [**package_version**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.package_version) (<code>PackageVersionIdentifier | None</code>) – Specific version to install. If None, installs the latest version.
- [**dependency_level**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.dependency_level) (<code>int</code>) – Current recursion depth for dependency resolution. Used internally
to prevent infinite recursion. Should not be set manually.
- [**use_cache**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.use_cache) (<code>bool</code>) – Weather to use the cache directory to look packages up which have already been downloaded.
To prevent the cache entirely, set this up in the marketplace component.
- [**ignore_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.ignore_lock) (<code>bool</code>) – If set to True, ignore the lock mechanism.

### `dependency_level` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.dependency_level}

```python
dependency_level: int = 0
```

### `ignore_dependencies` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.ignore_dependencies}

```python
ignore_dependencies: bool = False
```

### `ignore_lock` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.ignore_lock}

```python
ignore_lock: bool = False
```

### `install_from_marketplace` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.install_from_marketplace}

```python
install_from_marketplace: bool = True
```

### `model_config` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `package_version` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.package_version}

```python
package_version: PackageVersionIdentifier | None = None
```

### `use_archive_handler` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.use_archive_handler}

```python
use_archive_handler: bool = True
```

### `use_cache` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.use_cache}

```python
use_cache: bool = True
```

## `MarketplacePackagesRepository` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository}

Bases: <code>[Repository](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.Repository)</code>, <code>[ImportItemProtocol](../../repositories/protocols/import_item/index.md#cmem_client.repositories.protocols.import_item.ImportItemProtocol)</code>, <code>[ExportItemProtocol](../../repositories/protocols/export_item/index.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>, <code>[DeleteItemProtocol](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>

Repository for marketplace package operations.

**Functions:**

- [**delete_all**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_item) – Delete an item from the repository
- [**export_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.fetch_data) – Fetch installed packages from the package data graph via SPARQL query.
- [**import_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `delete_all` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `export_item` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.export_item}

```python
export_item(key, path=None, replace=False, configuration=None)
```

Export an item from the repository to a file path.

**Parameters:**

- **key** (<code>str</code>) – The key identifying the item to export.
- **path** (<code>Path | None</code>) – The target file path for export. If None, a path will be generated.
- **replace** (<code>bool</code>) – Whether to replace existing files at the target path.
- **configuration** (<code>[ExportItemConfig_contra](../../repositories/protocols/export_item/index.md#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) | None</code>) – Optional configuration for export behavior.

**Returns:**

- <code>Path</code> – The actual path where the item was exported.

**Raises:**

- <code>[RepositoryItemNotFoundError](../../exceptions/index.md#cmem_client.exceptions.RepositoryItemNotFoundError)</code> – If the specified item key is not found.
- <code>[RepositoryReadError](../../exceptions/index.md#cmem_client.exceptions.RepositoryReadError)</code> – If there's an error during export or path mismatch.

### `fetch_data` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.fetch_data}

```python
fetch_data()
```

Fetch installed packages from the package data graph via SPARQL query.

Queries the package data graph for all installed packages and their metadata.

### `import_item` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.import_item}

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

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item already exists and the conflict
policy is FAIL, if the import type is not allowed for this repository, if
the import request failed, or if the item is not present afterwards.

### `items` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.values}

```python
values()
```

Get the values of the repository

## `get_installation_metadata_query` {#cmem_client.repositories.marketplace_packages.get_installation_metadata_query}

```python
get_installation_metadata_query(package_iri)
```

Get the query for the installation metadata of the package.

