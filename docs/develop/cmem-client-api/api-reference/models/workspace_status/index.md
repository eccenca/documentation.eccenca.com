---
title: "cmem-client: models.workspace_status module"
description: "Corporate Memory DataIntegration workspace status models."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.workspace_status` {#cmem_client.models.workspace_status}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory DataIntegration workspace status models.

Models for the aggregated workspace status endpoint
(`GET /dataintegration/api/workspace/status`), which reports task loading
errors for all projects of the build (DataIntegration) workspace in a single
response. Only projects that have at least one failed task are listed.

**Classes:**

- [**ProjectStatus**](#cmem_client.models.workspace_status.ProjectStatus) – Loading status of a single project with failed tasks.
- [**WorkspaceStatus**](#cmem_client.models.workspace_status.WorkspaceStatus) – Aggregated loading status of the whole build (DataIntegration) workspace.

## `ProjectStatus` {#cmem_client.models.workspace_status.ProjectStatus}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Loading status of a single project with failed tasks.

The per-task objects share the shape of the per-project
``failedTasksReport`` endpoint, so the same model is reused.

**Attributes:**

- [**project_id**](#cmem_client.models.workspace_status.ProjectStatus.project_id) (<code>str</code>) – ID of the project.
- [**project_label**](#cmem_client.models.workspace_status.ProjectStatus.project_label) (<code>str | None</code>) – Human readable name of the project, if one is set.
- [**failed_task_count**](#cmem_client.models.workspace_status.ProjectStatus.failed_task_count) (<code>int</code>) – How many tasks of the project failed to load.
- [**failed_tasks**](#cmem_client.models.workspace_status.ProjectStatus.failed_tasks) (<code>list[[FailedTasksReport](../../models/project/index.md#cmem_client.models.project.FailedTasksReport)]</code>) – The failed tasks themselves, with the error of each.

### `failed_task_count` {#cmem_client.models.workspace_status.ProjectStatus.failed_task_count}

```python
failed_task_count: int = Field(alias='failedTaskCount', default=0)
```

### `failed_tasks` {#cmem_client.models.workspace_status.ProjectStatus.failed_tasks}

```python
failed_tasks: list[FailedTasksReport] = Field(alias='failedTasks', default_factory=list)
```

### `model_config` {#cmem_client.models.workspace_status.ProjectStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_id` {#cmem_client.models.workspace_status.ProjectStatus.project_id}

```python
project_id: str = Field(alias='projectId')
```

### `project_label` {#cmem_client.models.workspace_status.ProjectStatus.project_label}

```python
project_label: str | None = Field(alias='projectLabel', default=None)
```

## `WorkspaceStatus` {#cmem_client.models.workspace_status.WorkspaceStatus}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Aggregated loading status of the whole build (DataIntegration) workspace.

**Attributes:**

- [**project_count**](#cmem_client.models.workspace_status.WorkspaceStatus.project_count) (<code>int</code>) – How many projects the workspace holds in total.
- [**failed_project_count**](#cmem_client.models.workspace_status.WorkspaceStatus.failed_project_count) (<code>int</code>) – How many of them have at least one failed task.
- [**failed_task_count**](#cmem_client.models.workspace_status.WorkspaceStatus.failed_task_count) (<code>int</code>) – How many tasks failed to load across all projects.
- [**projects**](#cmem_client.models.workspace_status.WorkspaceStatus.projects) (<code>list[[ProjectStatus](#cmem_client.models.workspace_status.ProjectStatus)]</code>) – The projects with failed tasks. Projects which loaded cleanly are not
listed, so this is empty on a healthy workspace.

### `failed_project_count` {#cmem_client.models.workspace_status.WorkspaceStatus.failed_project_count}

```python
failed_project_count: int = Field(alias='failedProjectCount', default=0)
```

### `failed_task_count` {#cmem_client.models.workspace_status.WorkspaceStatus.failed_task_count}

```python
failed_task_count: int = Field(alias='failedTaskCount', default=0)
```

### `model_config` {#cmem_client.models.workspace_status.WorkspaceStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_count` {#cmem_client.models.workspace_status.WorkspaceStatus.project_count}

```python
project_count: int = Field(alias='projectCount', default=0)
```

### `projects` {#cmem_client.models.workspace_status.WorkspaceStatus.projects}

```python
projects: list[ProjectStatus] = Field(default_factory=list)
```

