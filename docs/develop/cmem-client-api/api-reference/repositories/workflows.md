---
title: "cmem-client: workflows module"
tags:
  - API
  - Python
  - cmem-client
---

# `workflows` {#cmem_client.repositories.workflows}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the workflows of DataIntegration projects.

Provides WorkflowsRepository for listing workflows and for starting them, polling
their execution status and running them with input or output payloads.

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

**Classes:**

- [**WorkflowsRepository**](#cmem_client.repositories.workflows.WorkflowsRepository) – Repository for managing workflows in Corporate Memory.

## `WorkflowsRepository` {#cmem_client.repositories.workflows.WorkflowsRepository}

Bases: <code>[TaskSearchRepository](../repositories/base/task_search.md#cmem_client.repositories.base.task_search.TaskSearchRepository)</code>

Repository for managing workflows in Corporate Memory.

The dict (keys, values, items) is populated via the task search API which returns
workflows with io info (variableInputs/variableOutputs) and tags in a single call.
Operational methods (execute, get_status, execute_io, etc.) are independent of
the dict and hit dedicated activity/result endpoints.

**Functions:**

- [**execute**](#cmem_client.repositories.workflows.WorkflowsRepository.execute) – Execute the workflow without waiting for completion.
- [**execute_io**](#cmem_client.repositories.workflows.WorkflowsRepository.execute_io) – Execute a workflow with variable input/output as a streaming context manager.
- [**execute_wait_for_completion**](#cmem_client.repositories.workflows.WorkflowsRepository.execute_wait_for_completion) – Execute the workflow and block until it finishes.
- [**fetch_data**](#cmem_client.repositories.workflows.WorkflowsRepository.fetch_data) – Fetch a list from the DI task search endpoint via a type adapter.
- [**get_all_statuses**](#cmem_client.repositories.workflows.WorkflowsRepository.get_all_statuses) – Get status information for multiple workflow activities.
- [**get_status**](#cmem_client.repositories.workflows.WorkflowsRepository.get_status) – Get the current status of a workflow activity.
- [**get_task**](#cmem_client.repositories.workflows.WorkflowsRepository.get_task) – Get full task details from the API.
- [**get_workflow_editor_url**](#cmem_client.repositories.workflows.WorkflowsRepository.get_workflow_editor_url) – Get the URL to open a workflow in the workbench editor.
- [**items**](#cmem_client.repositories.workflows.WorkflowsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.workflows.WorkflowsRepository.keys) – Get the keys of the repository
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
- **activity_name** (<code>[ACTIVITY_NAME](../models/workflow.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Name of the activity

**Raises:**

- <code>[WorkflowExecutionError](../exceptions.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the workflow execution failed.

### `execute_io` {#cmem_client.repositories.workflows.WorkflowsRepository.execute_io}

```python
execute_io(workflow_id, input_file=None, input_mime_type='application/xml', output_mime_type='application/xml', auto_config=False)
```

Execute a workflow with variable input/output as a streaming context manager.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:task_id'.
- **input_file** (<code>str | None</code>) – Optional path to the input file.
- **input_mime_type** (<code>str</code>) – MIME type of the input file.
- **output_mime_type** (<code>str</code>) – MIME type expected for the output.
- **auto_config** (<code>bool</code>) – Whether to enable auto-configuration of input datasets.

**Yields:**

- <code>Generator[Response]</code> – httpx.Response: Streaming response from the workflow execution.

**Raises:**

- <code>[WorkflowExecutionError](../exceptions.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If the request fails.

### `execute_wait_for_completion` {#cmem_client.repositories.workflows.WorkflowsRepository.execute_wait_for_completion}

```python
execute_wait_for_completion(workflow_id, activity_name='ExecuteDefaultWorkflow', sleep_time=1)
```

Execute the workflow and block until it finishes.

**Parameters:**

- **workflow_id** (<code>str</code>) – The workflow to execute (in the form of 'project_id:workflow_id')
- **activity_name** (<code>[ACTIVITY_NAME](../models/workflow.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Activity name. Defaults to "ExecuteDefaultWorkflow".
- **sleep_time** (<code>int</code>) – Seconds to sleep between status polls. Defaults to 1.

**Raises:**

- <code>[WorkflowExecutionError](../exceptions.md#cmem_client.exceptions.WorkflowExecutionError)</code> – If workflow execution failed.

### `fetch_data` {#cmem_client.repositories.workflows.WorkflowsRepository.fetch_data}

```python
fetch_data()
```

Fetch a list from the DI task search endpoint via a type adapter.

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

- <code>list[[WorkflowStatus](../models/workflow.md#cmem_client.models.workflow.WorkflowStatus)]</code> – List of WorkflowStatus objects.

**Raises:**

- <code>[WorkflowReadError](../exceptions.md#cmem_client.exceptions.WorkflowReadError)</code> – If the status fetch request fails.

### `get_status` {#cmem_client.repositories.workflows.WorkflowsRepository.get_status}

```python
get_status(workflow_id, activity_name='ExecuteDefaultWorkflow')
```

Get the current status of a workflow activity.

**Parameters:**

- **workflow_id** (<code>str</code>) – Workflow ID in the form 'project_id:workflow_id'.
- **activity_name** (<code>[ACTIVITY_NAME](../models/workflow.md#cmem_client.models.workflow.ACTIVITY_NAME)</code>) – Activity to check. Defaults to "ExecuteDefaultWorkflow".

**Returns:**

- <code>[WorkflowStatus](../models/workflow.md#cmem_client.models.workflow.WorkflowStatus)</code> – WorkflowStatus with current state, progress, and message.

**Raises:**

- <code>[WorkflowReadError](../exceptions.md#cmem_client.exceptions.WorkflowReadError)</code> – If the status fetch request fails.

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

- <code>[TaskResponse](../models/task.md#cmem_client.models.task.TaskResponse)</code> – The full task details as a TaskResponse model.

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

### `logger` {#cmem_client.repositories.workflows.WorkflowsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.workflows.WorkflowsRepository.values}

```python
values()
```

Get the values of the repository

