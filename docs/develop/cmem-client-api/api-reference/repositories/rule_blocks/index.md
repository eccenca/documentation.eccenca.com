---
title: "cmem-client: repositories.rule_blocks module"
description: "Rule block repository."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.rule_blocks` {#cmem_client.repositories.rule_blocks}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Rule block repository.

Rule blocks are listed through the generic task search endpoint. Because
``TaskSearchRepository.fetch_data`` already requests task parameters, the search
response carries the complete ``ruleBlockModel`` including the declared input
ports, so no additional request is needed to report them.

**Classes:**

- [**RuleBlockDeleteConfig**](#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig) – Rule block deletion configuration.
- [**RuleBlocksRepository**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository) – Repository for rule blocks.

## `RuleBlockDeleteConfig` {#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig}

Bases: <code>[DeleteConfig](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Rule block deletion configuration.

``remove_dependent_tasks`` maps to the required ``removeDependentTasks``
query parameter of the task delete endpoint. When true, DataIntegration
deletes every task that directly *or indirectly* references the rule block.
When false, referencing tasks are left behind holding a dangling reference,
which DataIntegration reports nowhere - callers are expected to check for
dependents themselves before passing false.

**Attributes:**

- [**model_config**](#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig.model_config) –
- [**remove_dependent_tasks**](#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig.remove_dependent_tasks) (<code>bool</code>) –

### `model_config` {#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `remove_dependent_tasks` {#cmem_client.repositories.rule_blocks.RuleBlockDeleteConfig.remove_dependent_tasks}

```python
remove_dependent_tasks: bool = False
```

## `RuleBlocksRepository` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository}

Bases: <code>[TaskSearchRepository](../../repositories/base/task_search/index.md#cmem_client.repositories.base.task_search.TaskSearchRepository)</code>, <code>[DeleteItemProtocol](../../repositories/protocols/delete_item/index.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>

Repository for rule blocks.

**Functions:**

- [**create_item**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.create_item) – Create a new rule block in a project.
- [**delete_all**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.delete_item) – Delete an item from the repository
- [**evaluate**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.evaluate) – Evaluate a rule block against the input examples stored with it.
- [**fetch_data**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.fetch_data) – Fetch a list from the DI task search endpoint via a type adapter.
- [**from_task_response**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.from_task_response) – Reshape a task detail response into the canonical RuleBlock structure.
- [**get_item**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.get_item) – Get full rule block details including metadata timestamps.
- [**get_task**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.get_task) – Get full task details from the API.
- [**items**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.keys) – Get the keys of the repository
- [**update_item**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.update_item) – Replace an existing rule block with the given one.
- [**values**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.rule_blocks.RuleBlocksRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.create_item}

```python
create_item(item)
```

Create a new rule block in a project.

**Parameters:**

- **item** (<code>[RuleBlock](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlock)</code>) – RuleBlock with ``project_id``, ``id``, ``metadata`` and
optionally ``data.rule_block_model``.

**Returns:**

- <code>[RuleBlock](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlock)</code> – The created rule block, read back from the server.

**Raises:**

- <code>HTTPStatusError</code> – If the creation request fails.

### `delete_all` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.delete_item}

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

### `evaluate` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.evaluate}

```python
evaluate(project_id, rule_block_id, model)
```

Evaluate a rule block against the input examples stored with it.

Both the project and the rule block task must exist; the endpoint is
task-scoped and there is no project-free evaluation mode.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **rule_block_id** (<code>str</code>) – The rule block ID.
- **model** (<code>[RuleBlockModel](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlockModel)</code>) – The rule block model to evaluate.

**Returns:**

- <code>list[Any]</code> – One result entry per stored input example.

**Raises:**

- <code>HTTPStatusError</code> – If the project or rule block does not exist.

### `fetch_data` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.fetch_data}

```python
fetch_data()
```

Fetch a list from the DI task search endpoint via a type adapter.

### `from_task_response` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.from_task_response}

```python
from_task_response(data)
```

Reshape a task detail response into the canonical RuleBlock structure.

The task detail endpoint nests the model under ``data.parameters``. It is
requested without labels, because with labels every parameter value is
wrapped into an additional ``value`` object.

**Parameters:**

- **data** (<code>dict[str, Any]</code>) – The JSON response of the task detail endpoint.

**Returns:**

- <code>[RuleBlock](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlock)</code> – The rule block with the ``ruleBlockModel`` parameter moved under ``data``.

### `get_item` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.get_item}

```python
get_item(project_id, rule_block_id)
```

Get full rule block details including metadata timestamps.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **rule_block_id** (<code>str</code>) – The rule block ID.

**Returns:**

- <code>[RuleBlock](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlock)</code> – RuleBlock model with the full model and metadata.

**Raises:**

- <code>HTTPStatusError</code> – If the rule block is not found.

### `get_task` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.get_task}

```python
get_task(project_id, task_id, with_labels=True)
```

Get full task details from the API.

**Parameters:**

- **project_id** (<code>str</code>) – The project ID.
- **task_id** (<code>str</code>) – The task ID.
- **with_labels** (<code>bool</code>) – Whether to include labels in the response.

**Returns:**

- <code>[TaskResponse](../../models/task/index.md#cmem_client.models.task.TaskResponse)</code> – The full task details as a TaskResponse model.

### `items` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `update_item` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.update_item}

```python
update_item(item)
```

Replace an existing rule block with the given one.

**Parameters:**

- **item** (<code>[RuleBlock](../../models/rule_block/index.md#cmem_client.models.rule_block.RuleBlock)</code>) – RuleBlock with ``project_id``, ``id``, ``metadata`` and
``data.rule_block_model``.

**Raises:**

- <code>HTTPStatusError</code> – If the update request fails.

### `values` {#cmem_client.repositories.rule_blocks.RuleBlocksRepository.values}

```python
values()
```

Get the values of the repository

