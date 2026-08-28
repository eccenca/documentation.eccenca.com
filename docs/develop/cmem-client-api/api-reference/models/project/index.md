---
title: "cmem-client: models.project module"
description: "Corporate Memory project models and metadata."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.project` {#cmem_client.models.project}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory project models and metadata.

This module defines models for representing Corporate Memory DataIntegration
projects, including their metadata such as labels, descriptions, and tags.

Projects are the primary organizational unit in Corporate Memory's build
environment, containing datasets, transformations, and other integration
components. The Project model provides validation and serialization for
project data exchanged with the DataIntegration API.

**Classes:**

- [**FailedTasksReport**](#cmem_client.models.project.FailedTasksReport) – The failed tasks report
- [**Project**](#cmem_client.models.project.Project) – A Build (DataIntegration) Project
- [**ProjectMetaData**](#cmem_client.models.project.ProjectMetaData) – Project Meta Data

**Functions:**

- [**default_metadata**](#cmem_client.models.project.default_metadata) – Get the current UTC datetime

## `FailedTasksReport` {#cmem_client.models.project.FailedTasksReport}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The failed tasks report

**Attributes:**

- [**task_id**](#cmem_client.models.project.FailedTasksReport.task_id) (<code>str | None</code>) – ID of the task which failed to load.
- [**error_summary**](#cmem_client.models.project.FailedTasksReport.error_summary) (<code>str | None</code>) – Short summary of what went wrong.
- [**task_label**](#cmem_client.models.project.FailedTasksReport.task_label) (<code>str | None</code>) – Human readable name of the task.
- [**task_description**](#cmem_client.models.project.FailedTasksReport.task_description) (<code>str | None</code>) – Description of the task.
- [**error_message**](#cmem_client.models.project.FailedTasksReport.error_message) (<code>str | None</code>) – Full error message.
- [**project_id**](#cmem_client.models.project.FailedTasksReport.project_id) (<code>str | None</code>) – ID of the project holding the task.
- [**stack_trace**](#cmem_client.models.project.FailedTasksReport.stack_trace) (<code>dict[str, Any] | None</code>) – Stack trace of the error, as reported by DataIntegration.

### `error_message` {#cmem_client.models.project.FailedTasksReport.error_message}

```python
error_message: str | None = Field(alias='errorMessage', default=None)
```

### `error_summary` {#cmem_client.models.project.FailedTasksReport.error_summary}

```python
error_summary: str | None = Field(alias='errorSummary', default=None)
```

### `model_config` {#cmem_client.models.project.FailedTasksReport.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_id` {#cmem_client.models.project.FailedTasksReport.project_id}

```python
project_id: str | None = Field(alias='projectId', default=None)
```

### `stack_trace` {#cmem_client.models.project.FailedTasksReport.stack_trace}

```python
stack_trace: dict[str, Any] | None = Field(alias='stackTrace', default=None)
```

### `task_description` {#cmem_client.models.project.FailedTasksReport.task_description}

```python
task_description: str | None = Field(alias='taskDescription', default=None)
```

### `task_id` {#cmem_client.models.project.FailedTasksReport.task_id}

```python
task_id: str | None = Field(alias='taskId', default=None)
```

### `task_label` {#cmem_client.models.project.FailedTasksReport.task_label}

```python
task_label: str | None = Field(alias='taskLabel', default=None)
```

## `Project` {#cmem_client.models.project.Project}

Bases: <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A Build (DataIntegration) Project

**Attributes:**

- [**name**](#cmem_client.models.project.Project.name) (<code>str</code>) – ID of the project, unique within the deployment. This is the key of the
repository, and it is what the other repositories mean by ``project_id``.
- [**meta_data**](#cmem_client.models.project.Project.meta_data) (<code>[ProjectMetaData](#cmem_client.models.project.ProjectMetaData)</code>) – Label, description and tags of the project.

**Functions:**

- [**get_id**](#cmem_client.models.project.Project.get_id) – Get the ID of the project
- [**model_post_init**](#cmem_client.models.project.Project.model_post_init) – Set the label to the name if needed

### `get_id` {#cmem_client.models.project.Project.get_id}

```python
get_id()
```

Get the ID of the project

### `meta_data` {#cmem_client.models.project.Project.meta_data}

```python
meta_data: ProjectMetaData = Field(alias='metaData', default_factory=default_metadata)
```

### `model_config` {#cmem_client.models.project.Project.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `model_post_init` {#cmem_client.models.project.Project.model_post_init}

```python
model_post_init(context)
```

Set the label to the name if needed

### `name` {#cmem_client.models.project.Project.name}

```python
name: str
```

## `ProjectMetaData` {#cmem_client.models.project.ProjectMetaData}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Project Meta Data

**Attributes:**

- [**label**](#cmem_client.models.project.ProjectMetaData.label) (<code>str | None</code>) – Human readable name of the project. DataIntegration refuses an empty
one, so a project created without a label gets its ID instead.
- [**description**](#cmem_client.models.project.ProjectMetaData.description) (<code>str | None</code>) – Description of the project.
- [**tags**](#cmem_client.models.project.ProjectMetaData.tags) (<code>list[str] | None</code>) – Tags attached to the project.
- [**modified**](#cmem_client.models.project.ProjectMetaData.modified) (<code>str | None</code>) – When the project was last modified.
- [**last_modified_by_user**](#cmem_client.models.project.ProjectMetaData.last_modified_by_user) (<code>str | None</code>) – IRI of the account which modified it last.

### `description` {#cmem_client.models.project.ProjectMetaData.description}

```python
description: str | None = None
```

### `label` {#cmem_client.models.project.ProjectMetaData.label}

```python
label: str | None = None
```

### `last_modified_by_user` {#cmem_client.models.project.ProjectMetaData.last_modified_by_user}

```python
last_modified_by_user: str | None = Field(alias='lastModifiedByUser', default=None)
```

### `model_config` {#cmem_client.models.project.ProjectMetaData.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `modified` {#cmem_client.models.project.ProjectMetaData.modified}

```python
modified: str | None = None
```

### `tags` {#cmem_client.models.project.ProjectMetaData.tags}

```python
tags: list[str] | None = None
```

## `default_metadata` {#cmem_client.models.project.default_metadata}

```python
default_metadata()
```

Get the current UTC datetime

