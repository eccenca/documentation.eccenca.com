---
title: "cmem-client: variables module"
tags:
  - API
  - Python
  - cmem-client
---

# `variables` {#cmem_client.repositories.variables}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the variables of DataIntegration projects.

Provides VariablesRepository for creating, updating and deleting project variables.
Variables are keyed by the composite key ``project_id:variable_name``, so a single
repository spans the variables of all projects.

**Examples:**

Create a variable in a project and read its value back:

```pycon
>>> from cmem_client.client import Client
>>> from cmem_client.models.variable import Variable
>>> client = Client.from_env()
>>> client.variables.create_item(
...     Variable(name="greeting", project_id="my-project", value="hello")
... )
>>> client.variables["my-project:greeting"].value
>>> client.variables.get_item("my-project", "greeting").value
```

List every variable of the deployment and delete one:

```pycon
>>> list(client.variables)
>>> client.variables.delete_item("my-project:greeting")
```

**Classes:**

- [**VariableCreateConfig**](#cmem_client.repositories.variables.VariableCreateConfig) – Variable creation configuration.
- [**VariableDeleteConfig**](#cmem_client.repositories.variables.VariableDeleteConfig) – Variable deletion configuration.
- [**VariableUpdateConfig**](#cmem_client.repositories.variables.VariableUpdateConfig) – Variable update configuration.
- [**VariablesRepository**](#cmem_client.repositories.variables.VariablesRepository) – Repository for project variables.

## `VariableCreateConfig` {#cmem_client.repositories.variables.VariableCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Variable creation configuration.

**Attributes:**

- **model_config** –

## `VariableDeleteConfig` {#cmem_client.repositories.variables.VariableDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Variable deletion configuration.

**Attributes:**

- **model_config** –

## `VariableUpdateConfig` {#cmem_client.repositories.variables.VariableUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Variable update configuration.

**Attributes:**

- **model_config** –

## `VariablesRepository` {#cmem_client.repositories.variables.VariablesRepository}

Bases: <code>[Repository](../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for project variables.

Manages project variables across all projects in the Corporate Memory
DataIntegration (build) environment. Variables are fetched per project and
stored with combined keys in the form ``project_id:variable_name``.

**Functions:**

- [**create_item**](#cmem_client.repositories.variables.VariablesRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.variables.VariablesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.variables.VariablesRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.variables.VariablesRepository.fetch_data) – Fetch all variables from all projects.
- [**get_item**](#cmem_client.repositories.variables.VariablesRepository.get_item) – Get a single variable by project and name.
- [**items**](#cmem_client.repositories.variables.VariablesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.variables.VariablesRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.variables.VariablesRepository.raise_modification_error) – Raise an exception if needed
- [**update_item**](#cmem_client.repositories.variables.VariablesRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.variables.VariablesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.variables.VariablesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.variables.VariablesRepository.create_item}

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

### `delete_all` {#cmem_client.repositories.variables.VariablesRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.variables.VariablesRepository.delete_item}

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

### `fetch_data` {#cmem_client.repositories.variables.VariablesRepository.fetch_data}

```python
fetch_data()
```

Fetch all variables from all projects.

### `get_item` {#cmem_client.repositories.variables.VariablesRepository.get_item}

```python
get_item(project_id, variable_name)
```

Get a single variable by project and name.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **variable_name** (<code>str</code>) – The variable name.

**Returns:**

- <code>[Variable](../models/variable.md#cmem_client.models.variable.Variable)</code> – Variable model.

**Raises:**

- <code>HTTPStatusError</code> – If the variable is not found or the request fails.

### `items` {#cmem_client.repositories.variables.VariablesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.variables.VariablesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.variables.VariablesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.variables.VariablesRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `update_item` {#cmem_client.repositories.variables.VariablesRepository.update_item}

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

### `values` {#cmem_client.repositories.variables.VariablesRepository.values}

```python
values()
```

Get the values of the repository

