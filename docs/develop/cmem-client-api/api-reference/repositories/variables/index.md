---
title: "cmem-client: repositories.variables module"
description: "Repository for the variables of DataIntegration projects."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.variables` {#cmem_client.repositories.variables}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the variables of DataIntegration projects.

Provides VariablesRepository for creating, updating and deleting project variables and
the execution variables of tasks. Project variables are keyed by
``project_id:variable_name``, execution variables by
``project_id:task_id:variable_name``, so a single repository spans the variables of all
projects and their tasks.

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

Create an execution variable on a task and read its value back:

```pycon
>>> client.variables.create_item(
...     Variable(
...         name="limit", project_id="my-project", task_id="my-workflow", value="10", scope="execution"
...     )
... )
>>> client.variables.get_item("my-project", "limit", task_id="my-workflow").value
```

See what still uses a variable, list every variable of the deployment and
delete one:

```pycon
>>> client.variables.get_dependents("my-project:greeting")
```

```pycon
>>> list(client.variables)
>>> client.variables.delete_item("my-project:my-workflow:limit")
```

**Classes:**

- [**VariableCreateConfig**](#cmem_client.repositories.variables.VariableCreateConfig) – Variable creation configuration.
- [**VariableDeleteConfig**](#cmem_client.repositories.variables.VariableDeleteConfig) – Variable deletion configuration.
- [**VariableUpdateConfig**](#cmem_client.repositories.variables.VariableUpdateConfig) – Variable update configuration.
- [**VariablesRepository**](#cmem_client.repositories.variables.VariablesRepository) – Repository for project variables, execution variables and global variables.

## `VariableCreateConfig` {#cmem_client.repositories.variables.VariableCreateConfig}

Bases: <code>[CreateConfig](../../repositories/protocols/create_item/index.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Variable creation configuration.

**Attributes:**

- **model_config** –

## `VariableDeleteConfig` {#cmem_client.repositories.variables.VariableDeleteConfig}

Bases: <code>[DeleteConfig](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Variable deletion configuration.

**Attributes:**

- **model_config** –

## `VariableUpdateConfig` {#cmem_client.repositories.variables.VariableUpdateConfig}

Bases: <code>[UpdateConfig](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Variable update configuration.

**Attributes:**

- **model_config** –

## `VariablesRepository` {#cmem_client.repositories.variables.VariablesRepository}

Bases: <code>[Repository](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.Repository)</code>, <code>[DeleteItemProtocol](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[CreateItemProtocol](../../repositories/protocols/create_item/index.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[UpdateItemProtocol](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for project variables, execution variables and global variables.

Manages the variables of all projects in the Corporate Memory DataIntegration
(Build) environment together with the execution variables of their tasks.
Project variables are stored with keys in the form ``project_id:variable_name``,
execution variables with keys in the form ``project_id:task_id:variable_name``.

The global variables are part of the repository as well, with their name as key.
They are defined in the configuration of DataIntegration, so they are read-only
and can neither be created, updated nor deleted.

Fetching all variables masks sensitive ones, their ``value`` is empty. Use
``get_item()`` to read a single project or execution variable including its value.

**Attributes:**

- [**tasks**](#cmem_client.repositories.variables.VariablesRepository.tasks) (<code>dict[str, str]</code>) – Labels of all tasks of all projects by ``project_id:task_id``, including
tasks without execution variables, as of the last fetch.
- [**errors**](#cmem_client.repositories.variables.VariablesRepository.errors) (<code>dict[str, str]</code>) – Errors the server reported for single variables on the last fetch, by
variable ID. A variable has an error, e.g. if its template can not be resolved.

**Functions:**

- [**create_item**](#cmem_client.repositories.variables.VariablesRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.variables.VariablesRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.variables.VariablesRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.variables.VariablesRepository.fetch_data) – Fetch the global variables, those of all projects and the execution variables of their tasks.
- [**get_dependents**](#cmem_client.repositories.variables.VariablesRepository.get_dependents) – Get the variables and tasks which still use a variable.
- [**get_item**](#cmem_client.repositories.variables.VariablesRepository.get_item) – Get a single variable by project, name and optionally task.
- [**items**](#cmem_client.repositories.variables.VariablesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.variables.VariablesRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.variables.VariablesRepository.raise_modification_error) – Raise an exception if needed
- [**update_item**](#cmem_client.repositories.variables.VariablesRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.variables.VariablesRepository.values) – Get the values of the repository

### `create_item` {#cmem_client.repositories.variables.VariablesRepository.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](../../repositories/protocols/create_item/index.md#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
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

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `errors` {#cmem_client.repositories.variables.VariablesRepository.errors}

```python
errors: dict[str, str]
```

### `fetch_data` {#cmem_client.repositories.variables.VariablesRepository.fetch_data}

```python
fetch_data()
```

Fetch the global variables, those of all projects and the execution variables of their tasks.

**Raises:**

- <code>[RepositoryReadError](../../exceptions/index.md#cmem_client.exceptions.RepositoryReadError)</code> – If Build does not provide the variables in one request,
because it is too old.

### `get_dependents` {#cmem_client.repositories.variables.VariablesRepository.get_dependents}

```python
get_dependents(key)
```

Get the variables and tasks which still use a variable.

A variable which is used cannot be deleted. The server reports only some of
its dependents on a failed deletion, while this lists all of them.

**Parameters:**

- **key** (<code>str</code>) – Combined variable key in the format ``project_id:variable_name`` or
``project_id:task_id:variable_name``.

**Returns:**

- <code>[VariableDependents](../../models/variable/index.md#cmem_client.models.variable.VariableDependents)</code> – The variables and tasks which use the variable.

**Raises:**

- <code>HTTPStatusError</code> – If the variable is not found or the request fails.

### `get_item` {#cmem_client.repositories.variables.VariablesRepository.get_item}

```python
get_item(project_id, variable_name, task_id=None)
```

Get a single variable by project, name and optionally task.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **variable_name** (<code>str</code>) – The variable name.
- **task_id** (<code>str | None</code>) – The task ID of an execution variable. Omit it for a project variable.

**Returns:**

- <code>[Variable](../../models/variable/index.md#cmem_client.models.variable.Variable)</code> – Variable model.

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

### `tasks` {#cmem_client.repositories.variables.VariablesRepository.tasks}

```python
tasks: dict[str, str]
```

### `update_item` {#cmem_client.repositories.variables.VariablesRepository.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../../repositories/base/abc/index.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](../../repositories/protocols/update_item/index.md#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../../exceptions/index.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

### `values` {#cmem_client.repositories.variables.VariablesRepository.values}

```python
values()
```

Get the values of the repository

