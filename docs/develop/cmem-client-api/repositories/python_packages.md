# `python_packages` {#cmem_client.repositories.python_packages}

Repository for the Python packages installed in DataIntegration.

Provides PythonPackagesRepository for listing the installed packages, installing new
ones from PyPI or from a wheel, and removing them again. It also reports the plugins
those packages contribute to the workspace.

**Examples:**

List the installed packages:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for name in client.python_packages:
...     print(name, client.python_packages[name].version)
```

Install a plugin package and reload the plugin registry:

```pycon
>>> client.python_packages.install_by_name("cmem-plugin-graphql")
>>> client.python_packages.reload_plugins()
>>> client.python_packages.list_plugins()
```

Remove a package again:

```pycon
>>> client.python_packages.delete_item("cmem-plugin-graphql")
```

**Classes:**

- [**PythonPackagesDeleteConfig**](#cmem_client.repositories.python_packages.PythonPackagesDeleteConfig) – Python packages deletion configuration.
- [**PythonPackagesRepository**](#cmem_client.repositories.python_packages.PythonPackagesRepository) – Repository for python packages

## `PythonPackagesDeleteConfig` {#cmem_client.repositories.python_packages.PythonPackagesDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Python packages deletion configuration.

**Attributes:**

- **model_config** – 

## `PythonPackagesRepository` {#cmem_client.repositories.python_packages.PythonPackagesRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>

Repository for python packages

**Functions:**

- [**delete_all**](#cmem_client.repositories.python_packages.PythonPackagesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.python_packages.PythonPackagesRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.python_packages.PythonPackagesRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**install_by_file**](#cmem_client.repositories.python_packages.PythonPackagesRepository.install_by_file) – Install a Python package by uploading a source distribution or wheel file.
- [**install_by_name**](#cmem_client.repositories.python_packages.PythonPackagesRepository.install_by_name) – Install or reinstall a Python package by pip requirement specifier.
- [**items**](#cmem_client.repositories.python_packages.PythonPackagesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.python_packages.PythonPackagesRepository.keys) – Get the keys of the repository
- [**list_plugins**](#cmem_client.repositories.python_packages.PythonPackagesRepository.list_plugins) – List all discovered and registered workspace plugins.
- [**reload_plugins**](#cmem_client.repositories.python_packages.PythonPackagesRepository.reload_plugins) – Reload all installed plugins and return the server response.
- [**values**](#cmem_client.repositories.python_packages.PythonPackagesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.python_packages.PythonPackagesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `delete_all` {#cmem_client.repositories.python_packages.PythonPackagesRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

This overwrites the default protocol method and utilizes an internal behaviour of the server
to wipe the whole python environment.

### `delete_item` {#cmem_client.repositories.python_packages.PythonPackagesRepository.delete_item}

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

### `fetch_data` {#cmem_client.repositories.python_packages.PythonPackagesRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `install_by_file` {#cmem_client.repositories.python_packages.PythonPackagesRepository.install_by_file}

```python
install_by_file(package_path)
```

Install a Python package by uploading a source distribution or wheel file.

**Parameters:**

- **package_path** (<code>Path</code>) – Path to a .tar.gz or .whl package file.

**Returns:**

- <code>[PythonInstallResult](../models/python_install.md#cmem_client.models.python_install.PythonInstallResult)</code> – A PythonInstallResult with the server response and any plugin registration errors.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the upload request fails.

### `install_by_name` {#cmem_client.repositories.python_packages.PythonPackagesRepository.install_by_name}

```python
install_by_name(requirement)
```

Install or reinstall a Python package by pip requirement specifier.

**Parameters:**

- **requirement** (<code>[PipRequirementSpecifier](../models/python_package.md#cmem_client.models.python_package.PipRequirementSpecifier)</code>) – A PEP 440/508 requirement specifier (e.g. 'requests', 'requests>=2.0').

**Returns:**

- <code>[PythonInstallResult](../models/python_install.md#cmem_client.models.python_install.PythonInstallResult)</code> – A PythonInstallResult with the server response and any plugin registration errors.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the install request fails.

### `items` {#cmem_client.repositories.python_packages.PythonPackagesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.python_packages.PythonPackagesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `list_plugins` {#cmem_client.repositories.python_packages.PythonPackagesRepository.list_plugins}

```python
list_plugins()
```

List all discovered and registered workspace plugins.

**Returns:**

- <code>list[[WorkspacePlugin](../models/workspace_plugin.md#cmem_client.models.workspace_plugin.WorkspacePlugin)]</code> – A list of WorkspacePlugin instances representing all plugins discovered
- <code>list[[WorkspacePlugin](../models/workspace_plugin.md#cmem_client.models.workspace_plugin.WorkspacePlugin)]</code> – from installed packages. Handles both the legacy plain-list response
- <code>list[[WorkspacePlugin](../models/workspace_plugin.md#cmem_client.models.workspace_plugin.WorkspacePlugin)]</code> – (DI <= 22.1) and the current object response with a ``plugins`` key
- <code>list[[WorkspacePlugin](../models/workspace_plugin.md#cmem_client.models.workspace_plugin.WorkspacePlugin)]</code> – (DI >= 22.1.1).

### `logger` {#cmem_client.repositories.python_packages.PythonPackagesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `reload_plugins` {#cmem_client.repositories.python_packages.PythonPackagesRepository.reload_plugins}

```python
reload_plugins()
```

Reload all installed plugins and return the server response.

Triggers plugin discovery and registration for all installed packages.
Use this after manual package changes or to recover from a partial
installation state.

**Returns:**

- <code>[PluginReloadResult](../models/python_install.md#cmem_client.models.python_install.PluginReloadResult)</code> – A PluginReloadResult which may contain plugin registration errors.

### `values` {#cmem_client.repositories.python_packages.PythonPackagesRepository.values}

```python
values()
```

Get the values of the repository

