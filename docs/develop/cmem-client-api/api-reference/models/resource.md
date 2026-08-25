---
title: "resource"
tags:
  - API
  - Python
  - cmem-client
---

# `resource` {#cmem_client.models.resource}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

A file resource model

A resource is a file inside a DataIntegration project, such as the CSV a dataset reads
from. The files of all projects are the items of ``client.files``, keyed by
``{project_id}:{file_id}``.

**Classes:**

- [**Resource**](#cmem_client.models.resource.Resource) – A file resource.
- [**ResourceMetadata**](#cmem_client.models.resource.ResourceMetadata) – Resource metadata
- [**ResourceResponse**](#cmem_client.models.resource.ResourceResponse) – API response model for a file resource
- [**ResourceUsage**](#cmem_client.models.resource.ResourceUsage) – Resource usage

## `Resource` {#cmem_client.models.resource.Resource}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A file resource.

**Attributes:**

- [**file_id**](#cmem_client.models.resource.Resource.file_id) (<code>str</code>) – ID of the file, unique within its project.
- [**project_id**](#cmem_client.models.resource.Resource.project_id) (<code>str</code>) – ID of the project holding the file.
- [**name**](#cmem_client.models.resource.Resource.name) (<code>str | None</code>) – Name of the file, or ``None`` if the deployment did not report it.
- [**full_path**](#cmem_client.models.resource.Resource.full_path) (<code>str | None</code>) – Path of the file inside the project.
- [**modified**](#cmem_client.models.resource.Resource.modified) (<code>str | None</code>) – When the file was last modified.
- [**size**](#cmem_client.models.resource.Resource.size) (<code>int | None</code>) – Size of the file in bytes.

**Functions:**

- [**get_id**](#cmem_client.models.resource.Resource.get_id) – Get the resource ID in format 'project_id:file_id'

### `file_id` {#cmem_client.models.resource.Resource.file_id}

```python
file_id: str
```

### `full_path` {#cmem_client.models.resource.Resource.full_path}

```python
full_path: str | None = Field(alias='fullPath', default=None)
```

### `get_id` {#cmem_client.models.resource.Resource.get_id}

```python
get_id()
```

Get the resource ID in format 'project_id:file_id'

### `model_config` {#cmem_client.models.resource.Resource.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `modified` {#cmem_client.models.resource.Resource.modified}

```python
modified: str | None = None
```

### `name` {#cmem_client.models.resource.Resource.name}

```python
name: str | None = None
```

### `project_id` {#cmem_client.models.resource.Resource.project_id}

```python
project_id: str
```

### `size` {#cmem_client.models.resource.Resource.size}

```python
size: int | None = None
```

## `ResourceMetadata` {#cmem_client.models.resource.ResourceMetadata}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Resource metadata

**Attributes:**

- [**name**](#cmem_client.models.resource.ResourceMetadata.name) (<code>str</code>) – Name of the file.
- [**relative_path**](#cmem_client.models.resource.ResourceMetadata.relative_path) (<code>str</code>) – Path of the file relative to the project.
- [**absolute_path**](#cmem_client.models.resource.ResourceMetadata.absolute_path) (<code>str</code>) – Path of the file on the deployment.
- [**size**](#cmem_client.models.resource.ResourceMetadata.size) (<code>int</code>) – Size of the file in bytes.
- [**modified**](#cmem_client.models.resource.ResourceMetadata.modified) (<code>str</code>) – When the file was last modified.

### `absolute_path` {#cmem_client.models.resource.ResourceMetadata.absolute_path}

```python
absolute_path: str = Field(alias='absolutePath')
```

### `model_config` {#cmem_client.models.resource.ResourceMetadata.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `modified` {#cmem_client.models.resource.ResourceMetadata.modified}

```python
modified: str
```

### `name` {#cmem_client.models.resource.ResourceMetadata.name}

```python
name: str
```

### `relative_path` {#cmem_client.models.resource.ResourceMetadata.relative_path}

```python
relative_path: str = Field(alias='relativePath')
```

### `size` {#cmem_client.models.resource.ResourceMetadata.size}

```python
size: int
```

## `ResourceResponse` {#cmem_client.models.resource.ResourceResponse}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

API response model for a file resource

**Attributes:**

- [**name**](#cmem_client.models.resource.ResourceResponse.name) (<code>str</code>) – Name of the file.
- [**full_path**](#cmem_client.models.resource.ResourceResponse.full_path) (<code>str</code>) – Path of the file inside the project.
- [**modified**](#cmem_client.models.resource.ResourceResponse.modified) (<code>str</code>) – When the file was last modified.
- [**size**](#cmem_client.models.resource.ResourceResponse.size) (<code>int</code>) – Size of the file in bytes.

### `full_path` {#cmem_client.models.resource.ResourceResponse.full_path}

```python
full_path: str = Field(alias='fullPath')
```

### `model_config` {#cmem_client.models.resource.ResourceResponse.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `modified` {#cmem_client.models.resource.ResourceResponse.modified}

```python
modified: str
```

### `name` {#cmem_client.models.resource.ResourceResponse.name}

```python
name: str
```

### `size` {#cmem_client.models.resource.ResourceResponse.size}

```python
size: int
```

## `ResourceUsage` {#cmem_client.models.resource.ResourceUsage}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Resource usage

**Attributes:**

- [**id**](#cmem_client.models.resource.ResourceUsage.id) (<code>str</code>) – ID of the task using the file.
- [**label**](#cmem_client.models.resource.ResourceUsage.label) (<code>str</code>) – Human readable name of that task.
- [**task_type**](#cmem_client.models.resource.ResourceUsage.task_type) (<code>str</code>) – Kind of task using the file, e.g. ``Dataset``.

### `id` {#cmem_client.models.resource.ResourceUsage.id}

```python
id: str
```

### `label` {#cmem_client.models.resource.ResourceUsage.label}

```python
label: str
```

### `model_config` {#cmem_client.models.resource.ResourceUsage.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `task_type` {#cmem_client.models.resource.ResourceUsage.task_type}

```python
task_type: str = Field(alias='taskType')
```

