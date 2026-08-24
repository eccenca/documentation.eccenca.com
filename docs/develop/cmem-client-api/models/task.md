# `task` {#cmem_client.models.task}

Task models for the DataIntegration task endpoint.

A task is what DataIntegration calls the items of a project: a dataset, a workflow, a
transformation and so on. These models carry the full detail of a single one, as
returned by ``TaskSearchRepository.get_task()``, which is more than the search result
the repositories list.

**Classes:**

- [**TaskData**](#cmem_client.models.task.TaskData) – The data section of a task endpoint response.
- [**TaskResponse**](#cmem_client.models.task.TaskResponse) – Response model for GET /workspace/projects/{project}/tasks/{task}.

## `TaskData` {#cmem_client.models.task.TaskData}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

The data section of a task endpoint response.

**Attributes:**

- [**task_type**](#cmem_client.models.task.TaskData.task_type) (<code>str | None</code>) – Kind of task, e.g. ``Dataset`` or ``Workflow``.
- [**parameters**](#cmem_client.models.task.TaskData.parameters) (<code>dict[str, Any]</code>) – Parameters of the task, keyed by parameter name. Which ones are
present depends on the plugin behind the task.

### `model_config` {#cmem_client.models.task.TaskData.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `parameters` {#cmem_client.models.task.TaskData.parameters}

```python
parameters: dict[str, Any] = Field(default_factory=dict)
```

### `task_type` {#cmem_client.models.task.TaskData.task_type}

```python
task_type: str | None = Field(default=None, alias='taskType')
```

## `TaskResponse` {#cmem_client.models.task.TaskResponse}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Response model for GET /workspace/projects/{project}/tasks/{task}.

**Attributes:**

- [**id**](#cmem_client.models.task.TaskResponse.id) (<code>str</code>) – Identifier of the task, unique within its project.
- [**label**](#cmem_client.models.task.TaskResponse.label) (<code>str | None</code>) – Human readable name of the task, if one is set.
- [**data**](#cmem_client.models.task.TaskResponse.data) (<code>[TaskData](#cmem_client.models.task.TaskData)</code>) – Type and parameters of the task.

### `data` {#cmem_client.models.task.TaskResponse.data}

```python
data: TaskData
```

### `id` {#cmem_client.models.task.TaskResponse.id}

```python
id: str
```

### `label` {#cmem_client.models.task.TaskResponse.label}

```python
label: str | None = None
```

### `model_config` {#cmem_client.models.task.TaskResponse.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

