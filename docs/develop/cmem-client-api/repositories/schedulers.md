# `schedulers` {#cmem_client.repositories.schedulers}

Repository for the workflow schedulers of DataIntegration.

Provides SchedulersRepository for listing the schedulers which trigger workflows, and
for enabling or disabling a single one.

**Examples:**

List the schedulers and inspect one:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for scheduler_id in client.schedulers:
...     print(scheduler_id, client.schedulers[scheduler_id])
```

Disable a scheduler and enable it again:

```pycon
>>> client.schedulers.update_enabled("my-project:my-scheduler", enabled=False)
>>> client.schedulers.update_enabled("my-project:my-scheduler", enabled=True)
```

**Classes:**

- [**SchedulerUpdateConfig**](#cmem_client.repositories.schedulers.SchedulerUpdateConfig) – Configuration for updating schedulers.
- [**SchedulersRepository**](#cmem_client.repositories.schedulers.SchedulersRepository) – Repository for managing workflow schedulers.

## `SchedulerUpdateConfig` {#cmem_client.repositories.schedulers.SchedulerUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Configuration for updating schedulers.

**Attributes:**

- **model_config** – 

## `SchedulersRepository` {#cmem_client.repositories.schedulers.SchedulersRepository}

Bases: <code>[TaskSearchRepository](../repositories/base/task_search.md#cmem_client.repositories.base.task_search.TaskSearchRepository)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for managing workflow schedulers.

Provides access to workflow schedulers in Corporate Memory. Schedulers
execute workflows at specified intervals and are identified by a
'project_id:scheduler_id' composite key.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.schedulers.SchedulersRepository.fetch_data) – Fetch a list from the DI task search endpoint via a type adapter.
- [**get_task**](#cmem_client.repositories.schedulers.SchedulersRepository.get_task) – Get full task details from the API.
- [**items**](#cmem_client.repositories.schedulers.SchedulersRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.schedulers.SchedulersRepository.keys) – Get the keys of the repository
- [**update_enabled**](#cmem_client.repositories.schedulers.SchedulersRepository.update_enabled) – Update the enabled state of a scheduler.
- [**update_item**](#cmem_client.repositories.schedulers.SchedulersRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.schedulers.SchedulersRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.schedulers.SchedulersRepository.logger) (<code>Logger</code>) – Gets the client logger

### `fetch_data` {#cmem_client.repositories.schedulers.SchedulersRepository.fetch_data}

```python
fetch_data()
```

Fetch a list from the DI task search endpoint via a type adapter.

### `get_task` {#cmem_client.repositories.schedulers.SchedulersRepository.get_task}

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

### `items` {#cmem_client.repositories.schedulers.SchedulersRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.schedulers.SchedulersRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.schedulers.SchedulersRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `update_enabled` {#cmem_client.repositories.schedulers.SchedulersRepository.update_enabled}

```python
update_enabled(scheduler_id, enabled)
```

Update the enabled state of a scheduler.

**Parameters:**

- **scheduler_id** (<code>str</code>) – Composite scheduler ID in 'project_id:scheduler_id' format.
- **enabled** (<code>bool</code>) – True to enable, False to disable.

**Returns:**

- <code>bool</code> – True if the state was changed, False if already in the desired state.

### `update_item` {#cmem_client.repositories.schedulers.SchedulersRepository.update_item}

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

### `values` {#cmem_client.repositories.schedulers.SchedulersRepository.values}

```python
values()
```

Get the values of the repository

