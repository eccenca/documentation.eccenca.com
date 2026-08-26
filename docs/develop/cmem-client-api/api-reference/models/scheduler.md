---
title: "cmem-client: scheduler module"
tags:
  - API
  - Python
  - cmem-client
---

# `scheduler` {#cmem_client.models.scheduler}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Scheduler models

A scheduler is the DataIntegration task which starts a workflow on a fixed interval.
The schedulers of all projects are the items of ``client.schedulers``, keyed by
``{project_id}:{scheduler_id}``.

**Classes:**

- [**Scheduler**](#cmem_client.models.scheduler.Scheduler) – A workflow scheduler task.
- [**SchedulerItemLink**](#cmem_client.models.scheduler.SchedulerItemLink) – A link associated with a scheduler.
- [**SchedulerParameters**](#cmem_client.models.scheduler.SchedulerParameters) – Parameters of a scheduler task.
- [**SchedulerSearchResults**](#cmem_client.models.scheduler.SchedulerSearchResults) – Wrapper for the task search API response containing schedulers.

## `Scheduler` {#cmem_client.models.scheduler.Scheduler}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A workflow scheduler task.

**Attributes:**

- [**id**](#cmem_client.models.scheduler.Scheduler.id) (<code>str</code>) – ID of the scheduler, unique within its project.
- [**project_id**](#cmem_client.models.scheduler.Scheduler.project_id) (<code>str</code>) – ID of the project holding the scheduler.
- [**label**](#cmem_client.models.scheduler.Scheduler.label) (<code>str</code>) – Human readable name of the scheduler.
- [**parameters**](#cmem_client.models.scheduler.Scheduler.parameters) (<code>[SchedulerParameters](#cmem_client.models.scheduler.SchedulerParameters)</code>) – Interval, enabled state and scheduled workflow.
- [**item_links**](#cmem_client.models.scheduler.Scheduler.item_links) (<code>list[[SchedulerItemLink](#cmem_client.models.scheduler.SchedulerItemLink)]</code>) – Links into the user interface for this scheduler.

**Functions:**

- [**get_id**](#cmem_client.models.scheduler.Scheduler.get_id) – Get the scheduler ID in the form 'project_id:scheduler_id'.

### `get_id` {#cmem_client.models.scheduler.Scheduler.get_id}

```python
get_id()
```

Get the scheduler ID in the form 'project_id:scheduler_id'.

### `id` {#cmem_client.models.scheduler.Scheduler.id}

```python
id: str
```

### `item_links` {#cmem_client.models.scheduler.Scheduler.item_links}

```python
item_links: list[SchedulerItemLink] = Field(default_factory=list, alias='itemLinks')
```

### `label` {#cmem_client.models.scheduler.Scheduler.label}

```python
label: str
```

### `model_config` {#cmem_client.models.scheduler.Scheduler.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `parameters` {#cmem_client.models.scheduler.Scheduler.parameters}

```python
parameters: SchedulerParameters
```

### `project_id` {#cmem_client.models.scheduler.Scheduler.project_id}

```python
project_id: str = Field(alias='projectId')
```

## `SchedulerItemLink` {#cmem_client.models.scheduler.SchedulerItemLink}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A link associated with a scheduler.

**Attributes:**

- [**path**](#cmem_client.models.scheduler.SchedulerItemLink.path) (<code>str</code>) – Path the link points at, relative to the DataIntegration user interface.
- [**label**](#cmem_client.models.scheduler.SchedulerItemLink.label) (<code>str | None</code>) – Text shown for the link.

### `label` {#cmem_client.models.scheduler.SchedulerItemLink.label}

```python
label: str | None = None
```

### `model_config` {#cmem_client.models.scheduler.SchedulerItemLink.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `path` {#cmem_client.models.scheduler.SchedulerItemLink.path}

```python
path: str
```

## `SchedulerParameters` {#cmem_client.models.scheduler.SchedulerParameters}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Parameters of a scheduler task.

**Attributes:**

- [**interval**](#cmem_client.models.scheduler.SchedulerParameters.interval) (<code>str</code>) – How often the workflow is started, as an ISO 8601 duration such as
``PT1H``.
- [**enabled**](#cmem_client.models.scheduler.SchedulerParameters.enabled) (<code>bool</code>) – Whether the scheduler currently runs. A disabled scheduler keeps its
interval but does not start anything.
- [**task**](#cmem_client.models.scheduler.SchedulerParameters.task) (<code>str</code>) – ID of the workflow the scheduler starts.

**Functions:**

- [**extract_task_id**](#cmem_client.models.scheduler.SchedulerParameters.extract_task_id) – Extract task ID from either a plain string or a dict with a 'value' key.
- [**parse_enabled**](#cmem_client.models.scheduler.SchedulerParameters.parse_enabled) – Convert API string 'true'/'false' to bool.
- [**serialize_enabled**](#cmem_client.models.scheduler.SchedulerParameters.serialize_enabled) – Serialize bool back to API string format.

### `enabled` {#cmem_client.models.scheduler.SchedulerParameters.enabled}

```python
enabled: bool
```

### `extract_task_id` {#cmem_client.models.scheduler.SchedulerParameters.extract_task_id}

```python
extract_task_id(v)
```

Extract task ID from either a plain string or a dict with a 'value' key.

### `interval` {#cmem_client.models.scheduler.SchedulerParameters.interval}

```python
interval: str
```

### `model_config` {#cmem_client.models.scheduler.SchedulerParameters.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `parse_enabled` {#cmem_client.models.scheduler.SchedulerParameters.parse_enabled}

```python
parse_enabled(v)
```

Convert API string 'true'/'false' to bool.

### `serialize_enabled` {#cmem_client.models.scheduler.SchedulerParameters.serialize_enabled}

```python
serialize_enabled(v)
```

Serialize bool back to API string format.

### `task` {#cmem_client.models.scheduler.SchedulerParameters.task}

```python
task: str
```

## `SchedulerSearchResults` {#cmem_client.models.scheduler.SchedulerSearchResults}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Wrapper for the task search API response containing schedulers.

**Attributes:**

- [**results**](#cmem_client.models.scheduler.SchedulerSearchResults.results) (<code>list[[Scheduler](#cmem_client.models.scheduler.Scheduler)]</code>) – The schedulers the search returned.

### `model_config` {#cmem_client.models.scheduler.SchedulerSearchResults.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `results` {#cmem_client.models.scheduler.SchedulerSearchResults.results}

```python
results: list[Scheduler]
```

