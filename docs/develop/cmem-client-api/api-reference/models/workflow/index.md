---
title: "cmem-client: models.workflow module"
description: "Workflow models"
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.workflow` {#cmem_client.models.workflow}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Workflow models

A workflow is the DataIntegration task which moves data between datasets. The workflows
of all projects are the items of ``client.workflows``, keyed by
``{project_id}:{workflow_id}``.

A workflow which came out of the repository carries a client, so it can start itself
and report its own status instead of going back through the repository:

    >>> from cmem_client.client import Client
    >>> client = Client.from_env()
    >>> workflow = client.workflows["my-project:my-workflow"]
    >>> workflow.execute_wait_for_completion()
    >>> workflow.get_status().concrete_status

**Classes:**

- [**Workflow**](#cmem_client.models.workflow.Workflow) – A workflow
- [**WorkflowSearchResultSet**](#cmem_client.models.workflow.WorkflowSearchResultSet) – Wrapper for the search API response envelope.
- [**WorkflowStatus**](#cmem_client.models.workflow.WorkflowStatus) – Workflow execution status

**Attributes:**

- [**ACTIVITY_NAME**](#cmem_client.models.workflow.ACTIVITY_NAME) –
- [**ACTIVITY_TYPE_EXECUTE_DEFAULTWORKFLOW**](#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_DEFAULTWORKFLOW) –
- [**ACTIVITY_TYPE_EXECUTE_LOCALWORKFLOW**](#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_LOCALWORKFLOW) –
- [**ACTIVITY_TYPE_EXECUTE_WITH_PAYLOAD**](#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_WITH_PAYLOAD) –
- [**VALID_WORKFLOW_STATUSES**](#cmem_client.models.workflow.VALID_WORKFLOW_STATUSES) –

## `ACTIVITY_NAME` {#cmem_client.models.workflow.ACTIVITY_NAME}

```python
ACTIVITY_NAME = Literal['ExecuteDefaultWorkflow', 'ExecuteLocalWorkflow', 'ExecuteWorkflowWithPayload']
```

## `ACTIVITY_TYPE_EXECUTE_DEFAULTWORKFLOW` {#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_DEFAULTWORKFLOW}

```python
ACTIVITY_TYPE_EXECUTE_DEFAULTWORKFLOW = 'ExecuteDefaultWorkflow'
```

## `ACTIVITY_TYPE_EXECUTE_LOCALWORKFLOW` {#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_LOCALWORKFLOW}

```python
ACTIVITY_TYPE_EXECUTE_LOCALWORKFLOW = 'ExecuteLocalWorkflow'
```

## `ACTIVITY_TYPE_EXECUTE_WITH_PAYLOAD` {#cmem_client.models.workflow.ACTIVITY_TYPE_EXECUTE_WITH_PAYLOAD}

```python
ACTIVITY_TYPE_EXECUTE_WITH_PAYLOAD = 'ExecuteWorkflowWithPayload'
```

## `VALID_WORKFLOW_STATUSES` {#cmem_client.models.workflow.VALID_WORKFLOW_STATUSES}

```python
VALID_WORKFLOW_STATUSES = ['Idle', 'Not executed', 'Finished', 'Cancelled', 'Failed', 'Successful', 'Canceling', 'Running', 'Waiting']
```

## `Workflow` {#cmem_client.models.workflow.Workflow}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A workflow

**Attributes:**

- [**id**](#cmem_client.models.workflow.Workflow.id) (<code>str</code>) – ID of the workflow, unique within its project.
- [**label**](#cmem_client.models.workflow.Workflow.label) (<code>str</code>) – Human readable name of the workflow.
- [**project_id**](#cmem_client.models.workflow.Workflow.project_id) (<code>str</code>) – ID of the project holding the workflow. Together with ``id`` it
forms the ``{project_id}:{id}`` key of the repository.
- [**project_label**](#cmem_client.models.workflow.Workflow.project_label) (<code>str</code>) – Human readable name of that project.
- [**variable_inputs**](#cmem_client.models.workflow.Workflow.variable_inputs) (<code>list[str]</code>) – IDs of the inputs which can be replaced at execution time,
which is what ``execute_io()`` writes its payload into.
- [**variable_outputs**](#cmem_client.models.workflow.Workflow.variable_outputs) (<code>list[str]</code>) – IDs of the outputs which can be replaced at execution time,
which is what ``execute_io()`` reads its result from.
- [**warnings**](#cmem_client.models.workflow.Workflow.warnings) (<code>list[str]</code>) – Warnings DataIntegration reported for the workflow.
- [**tags**](#cmem_client.models.workflow.Workflow.tags) (<code>list[[Tag](../../models/common/index.md#cmem_client.models.common.Tag)]</code>) – Tags attached to the workflow.
- [**parameters**](#cmem_client.models.workflow.Workflow.parameters) (<code>dict</code>) – Raw parameters as returned by the search endpoint. Excluded from
serialization; the variable inputs and outputs are read out of it.

**Functions:**

- [**execute**](#cmem_client.models.workflow.Workflow.execute) – Execute the workflow
- [**execute_wait_for_completion**](#cmem_client.models.workflow.Workflow.execute_wait_for_completion) – Execute the workflow waiting for completion
- [**get_id**](#cmem_client.models.workflow.Workflow.get_id) – Get the workflow ID
- [**get_status**](#cmem_client.models.workflow.Workflow.get_status) – Get the status of the workflow execution.
- [**set_client**](#cmem_client.models.workflow.Workflow.set_client) – Set the client for this workflow

### `execute` {#cmem_client.models.workflow.Workflow.execute}

```python
execute(activity_name='ExecuteDefaultWorkflow')
```

Execute the workflow

### `execute_wait_for_completion` {#cmem_client.models.workflow.Workflow.execute_wait_for_completion}

```python
execute_wait_for_completion(activity_name='ExecuteDefaultWorkflow', sleep_time=1)
```

Execute the workflow waiting for completion

### `get_id` {#cmem_client.models.workflow.Workflow.get_id}

```python
get_id()
```

Get the workflow ID

### `get_status` {#cmem_client.models.workflow.Workflow.get_status}

```python
get_status(activity_name='ExecuteDefaultWorkflow')
```

Get the status of the workflow execution.

### `id` {#cmem_client.models.workflow.Workflow.id}

```python
id: str
```

### `label` {#cmem_client.models.workflow.Workflow.label}

```python
label: str
```

### `model_config` {#cmem_client.models.workflow.Workflow.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `parameters` {#cmem_client.models.workflow.Workflow.parameters}

```python
parameters: dict = Field(default_factory=dict, exclude=True)
```

### `project_id` {#cmem_client.models.workflow.Workflow.project_id}

```python
project_id: str = Field(alias='projectId')
```

### `project_label` {#cmem_client.models.workflow.Workflow.project_label}

```python
project_label: str = Field(alias='projectLabel', default='')
```

### `set_client` {#cmem_client.models.workflow.Workflow.set_client}

```python
set_client(client)
```

Set the client for this workflow

### `tags` {#cmem_client.models.workflow.Workflow.tags}

```python
tags: list[Tag] = Field(default_factory=list)
```

### `variable_inputs` {#cmem_client.models.workflow.Workflow.variable_inputs}

```python
variable_inputs: list[str] = Field(alias='variableInputs', default_factory=list)
```

### `variable_outputs` {#cmem_client.models.workflow.Workflow.variable_outputs}

```python
variable_outputs: list[str] = Field(alias='variableOutputs', default_factory=list)
```

### `warnings` {#cmem_client.models.workflow.Workflow.warnings}

```python
warnings: list[str] = Field(default_factory=list)
```

## `WorkflowSearchResultSet` {#cmem_client.models.workflow.WorkflowSearchResultSet}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Wrapper for the search API response envelope.

**Attributes:**

- [**results**](#cmem_client.models.workflow.WorkflowSearchResultSet.results) (<code>list[[Workflow](#cmem_client.models.workflow.Workflow)]</code>) – The workflows the search returned.

### `model_config` {#cmem_client.models.workflow.WorkflowSearchResultSet.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `results` {#cmem_client.models.workflow.WorkflowSearchResultSet.results}

```python
results: list[Workflow]
```

## `WorkflowStatus` {#cmem_client.models.workflow.WorkflowStatus}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Workflow execution status

**Attributes:**

- [**status_name**](#cmem_client.models.workflow.WorkflowStatus.status_name) (<code>str</code>) – Coarse state of the execution, e.g. ``Idle``, ``Running`` or
``Finished``.
- [**concrete_status**](#cmem_client.models.workflow.WorkflowStatus.concrete_status) (<code>str</code>) – What the state amounts to, e.g. ``Successful``, ``Failed`` or
``Cancelled``. This is the field to check once an execution finished.
- [**progress**](#cmem_client.models.workflow.WorkflowStatus.progress) (<code>float | None</code>) – How far the execution got, in percent, or ``None`` if the workflow
does not report progress.
- [**failed**](#cmem_client.models.workflow.WorkflowStatus.failed) (<code>bool</code>) – Whether the execution failed.
- [**message**](#cmem_client.models.workflow.WorkflowStatus.message) (<code>str</code>) – Human readable status message.
- [**last_update_time**](#cmem_client.models.workflow.WorkflowStatus.last_update_time) (<code>int</code>) – When the status was last updated, as a Unix timestamp in
milliseconds.
- [**project**](#cmem_client.models.workflow.WorkflowStatus.project) (<code>str</code>) – ID of the project holding the workflow.
- [**task**](#cmem_client.models.workflow.WorkflowStatus.task) (<code>str</code>) – ID of the workflow task.
- [**activity**](#cmem_client.models.workflow.WorkflowStatus.activity) (<code>str</code>) – Name of the activity which runs the workflow.
- [**activity_label**](#cmem_client.models.workflow.WorkflowStatus.activity_label) (<code>str</code>) – Human readable name of that activity.
- [**queue_time**](#cmem_client.models.workflow.WorkflowStatus.queue_time) (<code>datetime | None</code>) – When the execution was queued.
- [**start_time**](#cmem_client.models.workflow.WorkflowStatus.start_time) (<code>datetime | None</code>) – When the execution actually started.
- [**is_running**](#cmem_client.models.workflow.WorkflowStatus.is_running) (<code>bool</code>) – Whether the execution is still going. Poll this to wait for a
workflow, or let ``execute_wait_for_completion()`` do it.
- [**runtime**](#cmem_client.models.workflow.WorkflowStatus.runtime) (<code>int | None</code>) – How long the execution took, in milliseconds.
- [**cancelled**](#cmem_client.models.workflow.WorkflowStatus.cancelled) (<code>bool | None</code>) – Whether the execution was cancelled.
- [**exception_message**](#cmem_client.models.workflow.WorkflowStatus.exception_message) (<code>str | None</code>) – Message of the exception which ended the execution, if one
did.

### `activity` {#cmem_client.models.workflow.WorkflowStatus.activity}

```python
activity: str
```

### `activity_label` {#cmem_client.models.workflow.WorkflowStatus.activity_label}

```python
activity_label: str = Field(alias='activityLabel')
```

### `cancelled` {#cmem_client.models.workflow.WorkflowStatus.cancelled}

```python
cancelled: bool | None = None
```

### `concrete_status` {#cmem_client.models.workflow.WorkflowStatus.concrete_status}

```python
concrete_status: str = Field(alias='concreteStatus')
```

### `exception_message` {#cmem_client.models.workflow.WorkflowStatus.exception_message}

```python
exception_message: str | None = Field(default=None, alias='exceptionMessage')
```

### `failed` {#cmem_client.models.workflow.WorkflowStatus.failed}

```python
failed: bool
```

### `is_running` {#cmem_client.models.workflow.WorkflowStatus.is_running}

```python
is_running: bool = Field(alias='isRunning')
```

### `last_update_time` {#cmem_client.models.workflow.WorkflowStatus.last_update_time}

```python
last_update_time: int = Field(alias='lastUpdateTime')
```

### `message` {#cmem_client.models.workflow.WorkflowStatus.message}

```python
message: str
```

### `model_config` {#cmem_client.models.workflow.WorkflowStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `progress` {#cmem_client.models.workflow.WorkflowStatus.progress}

```python
progress: float | None
```

### `project` {#cmem_client.models.workflow.WorkflowStatus.project}

```python
project: str
```

### `queue_time` {#cmem_client.models.workflow.WorkflowStatus.queue_time}

```python
queue_time: datetime | None = Field(default=None, alias='queueTime')
```

### `runtime` {#cmem_client.models.workflow.WorkflowStatus.runtime}

```python
runtime: int | None = None
```

### `start_time` {#cmem_client.models.workflow.WorkflowStatus.start_time}

```python
start_time: datetime | None = Field(default=None, alias='startTime')
```

### `status_name` {#cmem_client.models.workflow.WorkflowStatus.status_name}

```python
status_name: str = Field(alias='statusName')
```

### `task` {#cmem_client.models.workflow.WorkflowStatus.task}

```python
task: str
```

