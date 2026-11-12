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

- [**get_file_resource_key**](#cmem_client.repositories.marketplace_packages.get_file_resource_key) – Get the composite key a packaged image or text file is stored under in Corporate Memory.
- [**get_installation_metadata_query**](#cmem_client.repositories.marketplace_packages.get_installation_metadata_query) – Get the query for the installation metadata of the package.

**Attributes:**

- [**LOCK_FILE_RESOURCE**](#cmem_client.repositories.marketplace_packages.LOCK_FILE_RESOURCE) –
- [**MAX_DEPENDENCY_DEPTH**](#cmem_client.repositories.marketplace_packages.MAX_DEPENDENCY_DEPTH) – Hard ceiling on marketplace-package dependency recursion depth.

## `LOCK_FILE_RESOURCE` {#cmem_client.repositories.marketplace_packages.LOCK_FILE_RESOURCE}

```python
LOCK_FILE_RESOURCE = f'{MARKETPLACE_PROJECT_ID}:mp-lock.json'
```

## `MAX_DEPENDENCY_DEPTH` {#cmem_client.repositories.marketplace_packages.MAX_DEPENDENCY_DEPTH}

```python
MAX_DEPENDENCY_DEPTH = 20
```

Hard ceiling on marketplace-package dependency recursion depth.

Not a cycle guard -- a real cycle is resolved for free by ``dependency_chain`` on
``MarketplacePackagesImportConfig``/``MarketplacePackagesDeleteConfig`` (see there), which
stops re-descending into a package already in progress higher up the same chain, whatever the
depth. This exists for a pathologically deep-but-acyclic chain, or a misbehaving marketplace.
The number is generous headroom above any realistic dependency chain, not a meaningful
business limit.

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
- [**skip_missing_views**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_views) (<code>bool</code>) – If True, application views of the package which do not exist (for
example because somebody deleted them by hand after the installation) are skipped
instead of raising an error.
- [**ignore_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_lock) (<code>bool</code>) – If set to True, ignore the lock mechanism.
- [**ignore_dependencies**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.ignore_dependencies) (<code>bool</code>) – If True, dependencies of the package are not deleted.
- [**dependency_level**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.dependency_level) (<code>int</code>) – Current recursion depth for dependency resolution. Used internally to
identify the top-level call and to enforce MAX_DEPENDENCY_DEPTH. Should not be set
manually.
- [**dependency_chain**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.dependency_chain) (<code>tuple[PackageIdentifier, ...]</code>) – package_ids of the packages currently being deleted, from the
top-level call down to (but not including) the package about to be deleted. Used
internally to skip re-descending into a package a dependency cycle leads back
to -- it is already being deleted higher up this chain. Should not be set
manually.

### `dependency_chain` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.dependency_chain}

```python
dependency_chain: tuple[PackageIdentifier, ...] = ()
```

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

### `skip_missing_views` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesDeleteConfig.skip_missing_views}

```python
skip_missing_views: bool = True
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
to enforce MAX_DEPENDENCY_DEPTH. Should not be set manually.
- [**dependency_chain**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.dependency_chain) (<code>tuple[PackageIdentifier, ...]</code>) – package_ids of the packages currently being installed, from the
top-level call down to (but not including) the package about to be installed.
Used internally to skip re-descending into a package a dependency cycle leads

back to -- it is already being installed higher up this chain. Should not be
set manually.

- [**use_cache**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.use_cache) (<code>bool</code>) – Weather to use the cache directory to look packages up which have already been downloaded.
To prevent the cache entirely, set this up in the marketplace component.
- [**ignore_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.ignore_lock) (<code>bool</code>) – If set to True, ignore the lock mechanism.
- [**force_dependencies**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.force_dependencies) (<code>bool</code>) – If True, an installed dependency whose version violates the
constraint a package declares on it is upgraded or downgraded to a version which
satisfies the constraint, and the installation proceeds although a version it puts
in place (the package itself, or a dependency) violates the constraint of an
installed package, which is then listed in ``broken_dependants``. If False, such
an installation fails before anything is installed.
- [**resolution**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.resolution) (<code>DependencyResolution | None</code>) – Resolved dependency versions of the whole installation tree. Used
internally to hand the resolution down to dependency installations. Should not
be set manually.
- [**source**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.source) (<code>PackageSource | None</code>) – Where versions, dependency lists and archives are read from. If None, the
marketplace server of the client (``client.marketplace``) is used.
- [**broken_dependants**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.broken_dependants) (<code>list[BrokenDependant]</code>) – Output of the installation: the installed packages whose version
constraint it broke because the dependencies were forced. Cleared at the start of
every top-level installation, so it always describes the last one made with this
configuration. Empty after an installation which broke nothing.

### `broken_dependants` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.broken_dependants}

```python
broken_dependants: list[BrokenDependant] = Field(default_factory=list)
```

### `dependency_chain` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.dependency_chain}

```python
dependency_chain: tuple[PackageIdentifier, ...] = ()
```

### `dependency_level` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.dependency_level}

```python
dependency_level: int = 0
```

### `force_dependencies` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.force_dependencies}

```python
force_dependencies: bool = False
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
model_config = ConfigDict(arbitrary_types_allowed=True)
```

### `package_version` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.package_version}

```python
package_version: PackageVersionIdentifier | None = None
```

### `resolution` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.resolution}

```python
resolution: DependencyResolution | None = None
```

### `source` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesImportConfig.source}

```python
source: PackageSource | None = None
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

- [**acquire_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.acquire_lock) – Acquire the shared marketplace-packages install/uninstall lock for a whole operation.
- [**delete_all**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.delete_item) – Delete an item from the repository
- [**dependency_tree**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.dependency_tree) – Report the dependency tree of the installed packages.
- [**export_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.export_item) – Export an item from the repository to a file path.
- [**fetch_data**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.fetch_data) – Fetch installed packages from the package data graph via SPARQL query.
- [**get_installed_file**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.get_installed_file) – Read a packaged image or text file of an installed package back from Corporate Memory.
- [**import_item**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.keys) – Get the keys of the repository
- [**release_lock**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.release_lock) – Release the shared marketplace-packages install/uninstall lock acquired by `acquire_lock`.
- [**values**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `acquire_lock` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.acquire_lock}

```python
acquire_lock(package_id, activity='Install')
```

Acquire the shared marketplace-packages install/uninstall lock for a whole operation.

Import/delete each threads a fragile ``ignore_lock``/``dependency_level`` pair through
every recursive call to know which one is responsible for acquiring and releasing the
shared lock -- correct for a plain recursive walk, but it breaks down when a step in
that walk is skipped for an unrelated reason (e.g. a dependency turns out to already be
installed): nothing acquires the lock in that call's place, and a caller that assumed it
had can go on to (wrongly) treat a lock still held from a genuinely separate, earlier,
possibly-orphaned operation as its own.

Call this once, explicitly, before a multi-step operation that composes several
import/delete calls into one logical whole (see e.g.
``eccenca_marketplace.services.install_local_package``), then pass ``ignore_lock=True``
to every one of those calls -- no per-call bookkeeping needed. Pair with `release_lock`
in a ``finally``, regardless of whether every step actually ran.

**Parameters:**

- **package_id** (<code>str</code>) – The package this operation is ultimately for -- recorded in the lock,
and named in the error message if another process already holds it.
- **activity** (<code>Literal['Install', 'Uninstall']</code>) – What the lock records itself as doing.

**Raises:**

- <code>[MarketplacePackagesImportError](../../exceptions/index.md#cmem_client.exceptions.MarketplacePackagesImportError)</code> – If another process already holds the lock.

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

### `dependency_tree` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.dependency_tree}

```python
dependency_tree(package_id=None)
```

Report the dependency tree of the installed packages.

Every installed package is listed with the dependencies its manifest declares -
marketplace packages and Python packages alike - each with the declared constraint,
the installed version and whether it is satisfied, violated or missing, and with the
installed packages which depend on it. The violations of the tree collect every
violated and missing dependency, so an empty list means the installed tree is
consistent. A dependency which is missing because its dependant was installed while
ignoring the dependencies, or because it was uninstalled, is reported as missing.
The roots of the tree are the installed packages nothing else requires, and the
nested tree expands them, every package once, for a caller which renders it.

**Parameters:**

- **package_id** (<code>str | None</code>) – Report only the part of the tree this installed package pulls in,
rooted at it (see ``installed_subtree()``).

**Returns:**

- <code>DependencyTree</code> – The tree, read from Corporate Memory right now.

**Raises:**

- <code>[MarketplacePackagesNotFoundError](../../exceptions/index.md#cmem_client.exceptions.MarketplacePackagesNotFoundError)</code> – If ``package_id`` is not installed.

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
- <code>[RepositoryReadError](../../exceptions/index.md#cmem_client.exceptions.RepositoryReadError)</code> – If there is an error during export or path mismatch.

### `fetch_data` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.fetch_data}

```python
fetch_data()
```

Fetch installed packages from the package data graph via SPARQL query.

Queries the package data graph for all installed packages and their metadata.

### `get_installed_file` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.get_installed_file}

```python
get_installed_file(package_id, file_path)
```

Read a packaged image or text file of an installed package back from Corporate Memory.

An installation keeps the icon, the marketplace images, the readme, the license and
the changelog of a package as file resources, whether the package came from a
marketplace or from a file, so they can be shown after the archive is gone. Only a
path the installed manifest declares as an image or text file can be read.

**Parameters:**

- **package_id** (<code>str</code>) – The ID of the installed package.
- **file_path** (<code>str</code>) – The path of the file as the installed manifest declares it.

**Returns:**

- <code>bytes</code> – The raw content of the file.

**Raises:**

- <code>[MarketplacePackagesNotFoundError](../../exceptions/index.md#cmem_client.exceptions.MarketplacePackagesNotFoundError)</code> – If the package is not installed.
- <code>[MarketplacePackagesFileNotFoundError](../../exceptions/index.md#cmem_client.exceptions.MarketplacePackagesFileNotFoundError)</code> – If the installed manifest declares no image or
text file with this path.
- <code>FilesNotFoundError</code> – If the file resource is missing in Corporate Memory.

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

### `release_lock` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.release_lock}

```python
release_lock()
```

Release the shared marketplace-packages install/uninstall lock acquired by `acquire_lock`.

Safe to call even if the assets project or the lock file no longer exist (e.g. the
last package was also removed as part of the same operation).

### `values` {#cmem_client.repositories.marketplace_packages.MarketplacePackagesRepository.values}

```python
values()
```

Get the values of the repository

## `get_file_resource_key` {#cmem_client.repositories.marketplace_packages.get_file_resource_key}

```python
get_file_resource_key(package_id, file_path)
```

Get the composite key a packaged image or text file is stored under in Corporate Memory.

## `get_installation_metadata_query` {#cmem_client.repositories.marketplace_packages.get_installation_metadata_query}

```python
get_installation_metadata_query(package_iri)
```

Get the query for the installation metadata of the package.

