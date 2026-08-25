---
title: "datasets"
tags:
  - API
  - Python
  - cmem-client
---

# `datasets` {#cmem_client.repositories.datasets}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for managing datasets in Corporate Memory.

Provides DatasetsRepository for listing datasets across projects and for creating,
reading, updating and deleting a dataset inside a project. Datasets are addressed by
their project and dataset ID, and the available dataset types are described by the
dataset plugins.

**Examples:**

Inspect the dataset types the deployment offers:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> sorted(client.datasets.get_dataset_plugins())
>>> client.datasets.get_plugin_schema("csv")
```

Create a dataset in a project and read it back:

```pycon
>>> from cmem_client.models.dataset import Dataset
>>> client.datasets.create_item(
...     Dataset(
...         id="customers",
...         project_id="my-project",
...         data={"type": "csv", "parameters": {"file": "customers.csv"}},
...     )
... )
>>> client.datasets.get_item("my-project", "customers")
```

**Classes:**

- [**DatasetDeleteConfig**](#cmem_client.repositories.datasets.DatasetDeleteConfig) – Dataset deletion configuration.
- [**DatasetsRepository**](#cmem_client.repositories.datasets.DatasetsRepository) – Repository for datasets.

## `DatasetDeleteConfig` {#cmem_client.repositories.datasets.DatasetDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Dataset deletion configuration.

**Attributes:**

- **model_config** –

## `DatasetsRepository` {#cmem_client.repositories.datasets.DatasetsRepository}

Bases: <code>[TaskSearchRepository](../repositories/base/task_search.md#cmem_client.repositories.base.task_search.TaskSearchRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>

Repository for datasets.

**Functions:**

- [**create_item**](#cmem_client.repositories.datasets.DatasetsRepository.create_item) – Create a new dataset in a project.
- [**delete_all**](#cmem_client.repositories.datasets.DatasetsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.datasets.DatasetsRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.datasets.DatasetsRepository.fetch_data) – Fetch a list from the DI task search endpoint via a type adapter.
- [**get_dataset_plugins**](#cmem_client.repositories.datasets.DatasetsRepository.get_dataset_plugins) – Get all available dataset plugins.
- [**get_file_resource**](#cmem_client.repositories.datasets.DatasetsRepository.get_file_resource) – Return a streaming context manager for downloading a file resource.
- [**get_item**](#cmem_client.repositories.datasets.DatasetsRepository.get_item) – Get full dataset details including configuration parameters.
- [**get_plugin_schema**](#cmem_client.repositories.datasets.DatasetsRepository.get_plugin_schema) – Get the schema description of a specific task plugin.
- [**get_task**](#cmem_client.repositories.datasets.DatasetsRepository.get_task) – Get full task details from the API.
- [**items**](#cmem_client.repositories.datasets.DatasetsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.datasets.DatasetsRepository.keys) – Get the keys of the repository
- [**post_file_resource**](#cmem_client.repositories.datasets.DatasetsRepository.post_file_resource) – Upload a file as the resource of a dataset.
- [**update_item**](#cmem_client.repositories.datasets.DatasetsRepository.update_item) – Update the configuration of an existing dataset.
- [**values**](#cmem_client.repositories.datasets.DatasetsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.datasets.DatasetsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.datasets.DatasetsRepository.create_item}

```python
create_item(item)
```

Create a new dataset in a project.

**Parameters:**

- **item** (<code>[Dataset](../models/dataset.md#cmem_client.models.dataset.Dataset)</code>) – Dataset model with ``project_id``, ``id``, ``data`` (type, parameters,
read_only, uri_property) and optionally ``metadata``.

**Returns:**

- <code>[Dataset](../models/dataset.md#cmem_client.models.dataset.Dataset)</code> – Created dataset as a validated Dataset model.

**Raises:**

- <code>HTTPStatusError</code> – If the creation request fails.

### `delete_all` {#cmem_client.repositories.datasets.DatasetsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.datasets.DatasetsRepository.delete_item}

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

### `fetch_data` {#cmem_client.repositories.datasets.DatasetsRepository.fetch_data}

```python
fetch_data()
```

Fetch a list from the DI task search endpoint via a type adapter.

### `get_dataset_plugins` {#cmem_client.repositories.datasets.DatasetsRepository.get_dataset_plugins}

```python
get_dataset_plugins()
```

Get all available dataset plugins.

**Returns:**

- <code>dict[str, [DatasetPlugin](../models/dataset.md#cmem_client.models.dataset.DatasetPlugin)]</code> – Dictionary mapping plugin IDs to their plugin descriptions.

**Raises:**

- <code>HTTPStatusError</code> – If the request fails.

### `get_file_resource` {#cmem_client.repositories.datasets.DatasetsRepository.get_file_resource}

```python
get_file_resource(project_id, file_name)
```

Return a streaming context manager for downloading a file resource.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **file_name** (<code>str</code>) – The file resource name or path within the project.

**Returns:**

- <code>AbstractContextManager[Response]</code> – A context manager that yields an ``httpx.Response`` with streaming access.
- <code>AbstractContextManager[Response]</code> – Use ``response.iter_bytes()`` inside the ``with`` block to read chunks.

<details class="example" open markdown="1">
<summary>Example</summary>

>>> from pathlib import Path
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.files.import_item(
...     path=Path("customers.csv"), key="my-project:customers.csv"
... )
>>> with client.datasets.get_file_resource("my-project", "customers.csv") as response:
...     response.raise_for_status()
...     with Path("copy.csv").open("wb") as file:
...         for chunk in response.iter_bytes():
...             file.write(chunk)
>>> client.files.delete_item("my-project:customers.csv")

</details>

### `get_item` {#cmem_client.repositories.datasets.DatasetsRepository.get_item}

```python
get_item(project_id, dataset_id)
```

Get full dataset details including configuration parameters.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **dataset_id** (<code>str</code>) – The dataset ID.

**Returns:**

- <code>[Dataset](../models/dataset.md#cmem_client.models.dataset.Dataset)</code> – Dataset model with full details including parameters and metadata.

**Raises:**

- <code>HTTPStatusError</code> – If the dataset is not found or request fails.

### `get_plugin_schema` {#cmem_client.repositories.datasets.DatasetsRepository.get_plugin_schema}

```python
get_plugin_schema(plugin_id)
```

Get the schema description of a specific task plugin.

**Parameters:**

- **plugin_id** (<code>str</code>) – The plugin ID (e.g. ``csv``, ``json``, ``eccencaDataPlatform``).

**Returns:**

- <code>[DatasetPluginSchema](../models/dataset.md#cmem_client.models.dataset.DatasetPluginSchema)</code> – Plugin schema including ``properties`` and ``required`` fields.

**Raises:**

- <code>HTTPStatusError</code> – If the plugin is not found or the request fails.

### `get_task` {#cmem_client.repositories.datasets.DatasetsRepository.get_task}

```python
get_task(project_id, task_id, with_labels=True)
```

Get full task details from the API.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **task_id** (<code>str</code>) – The task ID.
- **with_labels** (<code>bool</code>) – Whether to include labels in the response.

**Returns:**

- <code>[TaskResponse](../models/task.md#cmem_client.models.task.TaskResponse)</code> – The full task details as a TaskResponse model.

### `items` {#cmem_client.repositories.datasets.DatasetsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.datasets.DatasetsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.datasets.DatasetsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `post_file_resource` {#cmem_client.repositories.datasets.DatasetsRepository.post_file_resource}

```python
post_file_resource(project_id, dataset_id, file_resource)
```

Upload a file as the resource of a dataset.

If the dataset resource already exists, uploading a new file replaces it.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **dataset_id** (<code>str</code>) – The dataset ID.
- **file_resource** (<code>BinaryIO</code>) – An open binary file object to upload.

**Raises:**

- <code>HTTPStatusError</code> – If the upload request fails.

### `update_item` {#cmem_client.repositories.datasets.DatasetsRepository.update_item}

```python
update_item(item)
```

Update the configuration of an existing dataset.

**Parameters:**

- **item** (<code>[Dataset](../models/dataset.md#cmem_client.models.dataset.Dataset)</code>) – Dataset model with ``project_id``, ``id``, and updated
``data`` (type, parameters, read_only, uri_property) and ``metadata``.

**Raises:**

- <code>HTTPStatusError</code> – If the update request fails.

### `values` {#cmem_client.repositories.datasets.DatasetsRepository.values}

```python
values()
```

Get the values of the repository

