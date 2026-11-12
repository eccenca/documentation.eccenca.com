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
- [**WorkflowReport**](#cmem_client.models.workflow.WorkflowReport) – One workflow execution report.
- [**WorkflowReportFinishStatus**](#cmem_client.models.workflow.WorkflowReportFinishStatus) – Final execution status recorded in a workflow report.
- [**WorkflowReportInfo**](#cmem_client.models.workflow.WorkflowReportInfo) – One entry of a workflow execution report list.
- [**WorkflowReportMetaData**](#cmem_client.models.workflow.WorkflowReportMetaData) – Metadata section of a workflow execution report.
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
- [**warnings**](#cmem_client.models.workflow.Workflow.warnings) (<code>list[str]</code>) – Warnings DataIntegration reported for the workflow. DataIntegration
reports them as plain strings or as objects with a ``message``.
- [**tags**](#cmem_client.models.workflow.Workflow.tags) (<code>list[[Tag](../../models/common/index.md#cmem_client.models.common.Tag)]</code>) – Tags attached to the workflow.
- [**parameters**](#cmem_client.models.workflow.Workflow.parameters) (<code>dict</code>) – Raw parameters as returned by the search endpoint. Excluded from
serialization.

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

## `WorkflowReport` {#cmem_client.models.workflow.WorkflowReport}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

One workflow execution report.

**Attributes:**

- [**meta_data**](#cmem_client.models.workflow.WorkflowReport.meta_data) (<code>[WorkflowReportMetaData](#cmem_client.models.workflow.WorkflowReportMetaData)</code>) – Timing and final status of the execution.
- [**value**](#cmem_client.models.workflow.WorkflowReport.value) (<code>dict[str, Any]</code>) – Report body describing the executed operation (warnings, error, entity
counts, and nested reports of sub-tasks). Kept as a plain dictionary
because its shape depends on the type of task that ran.

### `meta_data` {#cmem_client.models.workflow.WorkflowReport.meta_data}

```python
meta_data: WorkflowReportMetaData = Field(alias='metaData')
```

### `model_config` {#cmem_client.models.workflow.WorkflowReport.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `value` {#cmem_client.models.workflow.WorkflowReport.value}

```python
value: dict[str, Any] = Field(default_factory=dict)
```

## `WorkflowReportFinishStatus` {#cmem_client.models.workflow.WorkflowReportFinishStatus}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Final execution status recorded in a workflow report.

**Attributes:**

- [**status_name**](#cmem_client.models.workflow.WorkflowReportFinishStatus.status_name) (<code>str</code>) – Coarse state of the execution, e.g. ``Finished``.
- [**concrete_status**](#cmem_client.models.workflow.WorkflowReportFinishStatus.concrete_status) (<code>str</code>) – What the state amounts to, e.g. ``Successful``, ``Failed`` or
``Cancelled``.
- [**is_running**](#cmem_client.models.workflow.WorkflowReportFinishStatus.is_running) (<code>bool</code>) – Whether the execution was still going when the report was written.
Always ``False`` for a finished report.
- [**progress**](#cmem_client.models.workflow.WorkflowReportFinishStatus.progress) (<code>float | None</code>) – How far the execution got, in percent.
- [**message**](#cmem_client.models.workflow.WorkflowReportFinishStatus.message) (<code>str</code>) – Human readable status message.
- [**failed**](#cmem_client.models.workflow.WorkflowReportFinishStatus.failed) (<code>bool</code>) – Whether the execution failed.
- [**last_update_time**](#cmem_client.models.workflow.WorkflowReportFinishStatus.last_update_time) (<code>int</code>) – When the status was last updated, as a Unix timestamp in
milliseconds.
- [**runtime**](#cmem_client.models.workflow.WorkflowReportFinishStatus.runtime) (<code>int | None</code>) – How long the execution took, in milliseconds.
- [**cancelled**](#cmem_client.models.workflow.WorkflowReportFinishStatus.cancelled) (<code>bool | None</code>) – Whether the execution was cancelled.
- [**exception_message**](#cmem_client.models.workflow.WorkflowReportFinishStatus.exception_message) (<code>str | None</code>) – Message of the exception which ended the execution, if one
did.

### `cancelled` {#cmem_client.models.workflow.WorkflowReportFinishStatus.cancelled}

```python
cancelled: bool | None = None
```

### `concrete_status` {#cmem_client.models.workflow.WorkflowReportFinishStatus.concrete_status}

```python
concrete_status: str = Field(alias='concreteStatus')
```

### `exception_message` {#cmem_client.models.workflow.WorkflowReportFinishStatus.exception_message}

```python
exception_message: str | None = Field(default=None, alias='exceptionMessage')
```

### `failed` {#cmem_client.models.workflow.WorkflowReportFinishStatus.failed}

```python
failed: bool
```

### `is_running` {#cmem_client.models.workflow.WorkflowReportFinishStatus.is_running}

```python
is_running: bool = Field(alias='isRunning')
```

### `last_update_time` {#cmem_client.models.workflow.WorkflowReportFinishStatus.last_update_time}

```python
last_update_time: int = Field(alias='lastUpdateTime')
```

### `message` {#cmem_client.models.workflow.WorkflowReportFinishStatus.message}

```python
message: str
```

### `model_config` {#cmem_client.models.workflow.WorkflowReportFinishStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `progress` {#cmem_client.models.workflow.WorkflowReportFinishStatus.progress}

```python
progress: float | None = None
```

### `runtime` {#cmem_client.models.workflow.WorkflowReportFinishStatus.runtime}

```python
runtime: int | None = None
```

### `status_name` {#cmem_client.models.workflow.WorkflowReportFinishStatus.status_name}

```python
status_name: str = Field(alias='statusName')
```

## `WorkflowReportInfo` {#cmem_client.models.workflow.WorkflowReportInfo}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

One entry of a workflow execution report list.

**Attributes:**

- [**project**](#cmem_client.models.workflow.WorkflowReportInfo.project) (<code>str</code>) – ID of the project holding the workflow.
- [**task**](#cmem_client.models.workflow.WorkflowReportInfo.task) (<code>str</code>) – ID of the workflow task.
- [**time**](#cmem_client.models.workflow.WorkflowReportInfo.time) (<code>datetime</code>) – Timestamp identifying the report, passed to
[get_report](../../repositories/workflows/index.md#cmem_client.repositories.workflows.WorkflowsRepository.get_report)
to retrieve it.

### `model_config` {#cmem_client.models.workflow.WorkflowReportInfo.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project` {#cmem_client.models.workflow.WorkflowReportInfo.project}

```python
project: str
```

### `task` {#cmem_client.models.workflow.WorkflowReportInfo.task}

```python
task: str
```

### `time` {#cmem_client.models.workflow.WorkflowReportInfo.time}

```python
time: datetime
```

## `WorkflowReportMetaData` {#cmem_client.models.workflow.WorkflowReportMetaData}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Metadata section of a workflow execution report.

**Attributes:**

- [**started_by_user**](#cmem_client.models.workflow.WorkflowReportMetaData.started_by_user) (<code>str | None</code>) – Account name of the user who started the execution, if known.
- [**queued_at**](#cmem_client.models.workflow.WorkflowReportMetaData.queued_at) (<code>datetime | None</code>) – When the execution was queued.
- [**started_at**](#cmem_client.models.workflow.WorkflowReportMetaData.started_at) (<code>datetime | None</code>) – When the execution actually started.
- [**finished_at**](#cmem_client.models.workflow.WorkflowReportMetaData.finished_at) (<code>datetime | None</code>) – When the execution finished.
- [**cancelled_at**](#cmem_client.models.workflow.WorkflowReportMetaData.cancelled_at) (<code>datetime | None</code>) – When the execution was cancelled, if it was.
- [**cancelled_by**](#cmem_client.models.workflow.WorkflowReportMetaData.cancelled_by) (<code>str | None</code>) – Account name of the user who cancelled the execution, if it was.
- [**finish_status**](#cmem_client.models.workflow.WorkflowReportMetaData.finish_status) (<code>[WorkflowReportFinishStatus](#cmem_client.models.workflow.WorkflowReportFinishStatus)</code>) – The execution's final status.

### `cancelled_at` {#cmem_client.models.workflow.WorkflowReportMetaData.cancelled_at}

```python
cancelled_at: datetime | None = Field(default=None, alias='cancelledAt')
```

### `cancelled_by` {#cmem_client.models.workflow.WorkflowReportMetaData.cancelled_by}

```python
cancelled_by: str | None = Field(default=None, alias='cancelledBy')
```

### `finish_status` {#cmem_client.models.workflow.WorkflowReportMetaData.finish_status}

```python
finish_status: WorkflowReportFinishStatus = Field(alias='finishStatus')
```

### `finished_at` {#cmem_client.models.workflow.WorkflowReportMetaData.finished_at}

```python
finished_at: datetime | None = Field(default=None, alias='finishedAt')
```

### `model_config` {#cmem_client.models.workflow.WorkflowReportMetaData.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `queued_at` {#cmem_client.models.workflow.WorkflowReportMetaData.queued_at}

```python
queued_at: datetime | None = Field(default=None, alias='queuedAt')
```

### `started_at` {#cmem_client.models.workflow.WorkflowReportMetaData.started_at}

```python
started_at: datetime | None = Field(default=None, alias='startedAt')
```

### `started_by_user` {#cmem_client.models.workflow.WorkflowReportMetaData.started_by_user}

```python
started_by_user: str | None = Field(default=None, alias='startedByUser')
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

