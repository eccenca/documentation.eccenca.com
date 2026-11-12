---
title: "cmem-client: repositories.workflows module"
description: "Repository for the workflows of DataIntegration projects."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.workflows` {#cmem_client.repositories.workflows}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the workflows of DataIntegration projects.

Provides WorkflowsRepository for listing workflows and for starting them, polling
their execution status, running them with input or output payloads and reading their
execution reports.

**Examples:**

List the workflows of the deployment:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for workflow_id in client.workflows:
...     print(workflow_id, client.workflows[workflow_id].label)
```

Start a workflow and wait until it finished:

```pycon
>>> client.workflows.execute("my-project:my-workflow")
>>> client.workflows.get_status("my-project:my-workflow")
>>> client.workflows.execute_wait_for_completion("my-project:my-workflow")
```

Look at the status of every workflow currently known:

```pycon
>>> client.workflows.get_all_statuses()
```

List the execution reports of a workflow and fetch the latest one:

```pycon
>>> reports = client.workflows.list_reports("my-project:my-workflow")
>>> client.workflows.get_report("my-project:my-workflow", reports[0].time)
```

**Classes:**

- [**WorkflowsRepository**](#cmem_client.repositories.workflows.WorkflowsRepository) – Repository for managing workflows in Corporate Memory.

## `WorkflowsRepository` {#cmem_client.repositories.workflows.WorkflowsRepository}

Bases: <code>[TaskSearchRepository](../../repositories/base/task_search/index.md#cmem_client.repositories.base.task_search.TaskSearchRepository)</code>

Repository for managing workflows in Corporate Memory.

The dict (keys, values, items) is populated via the task search API, which returns
the workflows with their tags in a single call, and the workflow info API, which
resolves their variable inputs and outputs (variableInputs/variableOutputs).
Operational methods (execute, get_status, execute_io, etc.) are independent of
the dict and hit dedicated activity/result endpoints.

**Functions:**

- [**execute**](#cmem_client.repositories.workflows.WorkflowsRepository.execute) – Execute the workflow without waiting for completion.
- [**execute_io**](#cmem_client.repositories.workflows.WorkflowsRepository.execute_io) – Execute a workflow with variable input/output as a streaming context manager.
- [**execute_wait_for_completion**](#cmem_client.repositories.workflows.WorkflowsRepository.execute_wait_for_completion) – Execute the workflow and block until it finishes.
- [**execute_with_variables**](#cmem_client.repositories.workflows.WorkflowsRepository.execute_with_variables) – Execute the workflow once with overridden execution variables.
- [**fetch_data**](#cmem_client.repositories.workflows.WorkflowsRepository.fetch_data) – Fetch the workflows and complete their variable inputs and outputs.
- [**get_all_statuses**](#cmem_client.repositories.workflows.WorkflowsRepository.get_all_statuses) – Get status information for multiple workflow activities.
- [**get_execution_variables**](#cmem_client.repositories.workflows.WorkflowsRepository.get_execution_variables) – Get the execution variables a run of the workflow needs.
- [**get_report**](#cmem_client.repositories.workflows.WorkflowsRepository.get_report) – Get one execution report of a workflow.
- [**get_status**](#cmem_client.repositories.workflows.WorkflowsRepository.get_status) – Get the current status of a workflow activity.
- [**get_task**](#cmem_client.repositories.workflows.WorkflowsRepository.get_task) – Get full task details from the API.
- [**get_workflow_editor_url**](#cmem_client.repositories.workflows.WorkflowsRepository.get_workflow_editor_url) – Get the URL to open a workflow in the workbench editor.
- [**items**](#cmem_client.repositories.workflows.WorkflowsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.workflows.WorkflowsRepository.keys) – Get the keys of the repository
- [**list_reports**](#cmem_client.repositories.workflows.WorkflowsRepository.list_reports) – List the execution reports available for a workflow.
- [**remove_execution**](#cmem_client.repositories.workflows.WorkflowsRepository.remove_execution) – Remove a finished run started with ``execute_with_variables()``.
- [**values**](#cmem_client.repositories.workflows.WorkflowsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.workflows.WorkflowsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `execute` {#cmem_client.repositories.workflows.WorkflowsRepository.execute}

```python
execute(workflow_id, activity_name='ExecuteDefaultWorkflow')
```

Execute the workflow without waiting for completion.

**Parameters:**

- **workflow_id** (<code>str</code>) – The workflow to execute (in the form of 'project_id:workflow_id')
- **activity_name** (<code>[ACTIVITY_NAME](../../models/workflow/index.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Name of the activity

**Raises:**

- <code>[WorkflowExecutionError](../../exceptions/index.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the workflow execution failed.

### `execute_io` {#cmem_client.repositories.workflows.WorkflowsRepository.execute_io}

```python
execute_io(workflow_id, input_file=None, input_mime_type='application/xml', output_mime_type='application/xml', auto_config=False, execution_variables=None)
```

Execute a workflow with variable input/output as a streaming context manager.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:task_id'.
- **input_file** (<code>str | None</code>) – Optional path to the input file.
- **input_mime_type** (<code>str</code>) – MIME type of the input file.
- **output_mime_type** (<code>str</code>) – MIME type expected for the output.
- **auto_config** (<code>bool</code>) – Whether to enable auto-configuration of input datasets.
- **execution_variables** (<code>dict[str, str] | None</code>) – Values by variable name, overriding the defaults of the
workflow's execution variables for this run only. They are never part
of the input entity.

**Yields:**

- <code>Generator[Response]</code> – httpx.Response: Streaming response from the workflow execution.

**Raises:**

- <code>[WorkflowExecutionError](../../exceptions/index.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the request fails.

### `execute_wait_for_completion` {#cmem_client.repositories.workflows.WorkflowsRepository.execute_wait_for_completion}

```python
execute_wait_for_completion(workflow_id, activity_name='ExecuteDefaultWorkflow', sleep_time=1)
```

Execute the workflow and block until it finishes.

**Parameters:**

- **workflow_id** (<code>str</code>) – The workflow to execute (in the form of 'project_id:workflow_id')
- **activity_name** (<code>[ACTIVITY_NAME](../../models/workflow/index.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Activity name. Defaults to "ExecuteDefaultWorkflow".
- **sleep_time** (<code>int</code>) – Seconds to sleep between status polls. Defaults to 1.

**Raises:**

- <code>[WorkflowExecutionError](../../exceptions/index.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If workflow execution failed.

### `execute_with_variables` {#cmem_client.repositories.workflows.WorkflowsRepository.execute_with_variables}

```python
execute_with_variables(workflow_id, execution_variables)
```

Execute the workflow once with overridden execution variables.

The given values replace the defaults of the workflow's execution variables for
this run only, the stored defaults stay unchanged. The run is started as an
instance of the ``ExecuteWorkflowWithPayload`` activity, so poll its status with
``get_status()`` and that activity name and instance ID. The server keeps a
limited number of these instances per workflow, so remove a finished one with
``remove_execution()``.

The server neither rejects names which the workflow does not use nor checks
for missing required variables, so compare the values with
``get_execution_variables()`` beforehand if needed.

**Parameters:**

- **workflow_id** (<code>str</code>) – The workflow to execute (in the form of 'project_id:workflow_id')
- **execution_variables** (<code>dict[str, str]</code>) – Values by variable name, overriding the defaults.

**Returns:**

- <code>str</code> – The ID of the started activity instance.

**Raises:**

- <code>[WorkflowExecutionError](../../exceptions/index.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the workflow could not be started.

### `fetch_data` {#cmem_client.repositories.workflows.WorkflowsRepository.fetch_data}

```python
fetch_data()
```

Fetch the workflows and complete their variable inputs and outputs.

The task search only carries the replaceable datasets marked on a workflow
itself, so a workflow of workflows whose variable input or output sits in a
nested workflow would report none. The workflow info endpoint resolves nested
workflows as well, so its answer replaces the io information of every workflow.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the workflow info request fails.

### `get_all_statuses` {#cmem_client.repositories.workflows.WorkflowsRepository.get_all_statuses}

```python
get_all_statuses(project_id=None, status_filter=None, activity_type=None)
```

Get status information for multiple workflow activities.

**Parameters:**

- **project_id** (<code>str | None</code>) – Optional project ID to filter by.
- **status_filter** (<code>str | None</code>) – Optional status filter (e.g. "Finished", "Running").
- **activity_type** (<code>str | None</code>) – Optional activity type to filter by (e.g. "ExecuteDefaultWorkflow").

**Returns:**

- <code>list[[WorkflowStatus](../../models/workflow/index.md#cmem_client.models.workflow.WorkflowStatus)]</code> – List of WorkflowStatus objects.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the status fetch request fails.

### `get_execution_variables` {#cmem_client.repositories.workflows.WorkflowsRepository.get_execution_variables}

```python
get_execution_variables(workflow_id)
```

Get the execution variables a run of the workflow needs.

This covers the variables used at execution time by the workflow's tasks and
sub-workflows, recursively, and the variables defined on the workflow itself.
Only the defaults defined on the workflow apply to a run, so a variable which is
used but neither has such a default nor is set by a preceding node is marked as
required.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:workflow_id'.

**Returns:**

- <code>list[[WorkflowExecutionVariable](../../models/variable/index.md#cmem_client.models.variable.WorkflowExecutionVariable)]</code> – The execution variables, sorted by name.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the workflow does not exist or the request fails.

### `get_report` {#cmem_client.repositories.workflows.WorkflowsRepository.get_report}

```python
get_report(workflow_id, time)
```

Get one execution report of a workflow.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:task_id'.
- **time** (<code>datetime</code>) – Timestamp of the report, as returned by
[list_reports](#cmem_client.repositories.workflows.WorkflowsRepository.list_reports).

**Returns:**

- <code>[WorkflowReport](../../models/workflow/index.md#cmem_client.models.workflow.WorkflowReport)</code> – The execution report.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the report could not be fetched.

### `get_status` {#cmem_client.repositories.workflows.WorkflowsRepository.get_status}

```python
get_status(workflow_id, activity_name='ExecuteDefaultWorkflow', instance_id=None)
```

Get the current status of a workflow activity.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:workflow_id'.
- **activity_name** (<code>[ACTIVITY_NAME](../../models/workflow/index.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Activity to check. Defaults to "ExecuteDefaultWorkflow".
- **instance_id** (<code>str | None</code>) – Activity instance to check, e.g. the one returned by
``execute_with_variables()``. Defaults to the main instance.

**Returns:**

- <code>[WorkflowStatus](../../models/workflow/index.md#cmem_client.models.workflow.WorkflowStatus)</code> – WorkflowStatus with current state, progress, and message.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the status fetch request fails.

### `get_task` {#cmem_client.repositories.workflows.WorkflowsRepository.get_task}

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

### `get_workflow_editor_url` {#cmem_client.repositories.workflows.WorkflowsRepository.get_workflow_editor_url}

```python
get_workflow_editor_url(workflow_id)
```

Get the URL to open a workflow in the workbench editor.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:task_id'.

**Returns:**

- <code>str</code> – URL string for the workflow editor.

### `items` {#cmem_client.repositories.workflows.WorkflowsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.workflows.WorkflowsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `list_reports` {#cmem_client.repositories.workflows.WorkflowsRepository.list_reports}

```python
list_reports(workflow_id)
```

List the execution reports available for a workflow.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:task_id'.

**Returns:**

- <code>list[[WorkflowReportInfo](../../models/workflow/index.md#cmem_client.models.workflow.WorkflowReportInfo)]</code> – The reports available for the workflow. Empty if it was never executed.

**Raises:**

- <code>[WorkflowReadError](../../exceptions/index.md#cmem_client.exceptions.WorkflowReadError)</code> – If the report list could not be fetched.

### `logger` {#cmem_client.repositories.workflows.WorkflowsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `remove_execution` {#cmem_client.repositories.workflows.WorkflowsRepository.remove_execution}

```python
remove_execution(workflow_id, instance_id)
```

Remove a finished run started with ``execute_with_variables()``.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:workflow_id'.
- **instance_id** (<code>str</code>) – The activity instance ID of the run.

**Raises:**

- <code>[WorkflowExecutionError](../../exceptions/index.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the request fails.

### `values` {#cmem_client.repositories.workflows.WorkflowsRepository.values}

```python
values()
```

Get the values of the repository

