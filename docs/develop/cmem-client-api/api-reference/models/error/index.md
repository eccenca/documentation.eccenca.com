---
title: "cmem-client: models.error module"
description: "Error response models for Corporate Memory API error handling."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.error` {#cmem_client.models.error}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Error response models for Corporate Memory API error handling.

This module defines models for parsing and handling error responses from
both the DataIntegration (build) and DataPlatform (explore) APIs. Different
API endpoints return different error response formats, and these models
provide a unified way to handle them.

The Problem model handles DataPlatform API errors, while ErrorResult handles
DataIntegration API errors. Both include methods for generating human-readable
error messages for debugging and user feedback.

**Classes:**

- [**ErrorResult**](#cmem_client.models.error.ErrorResult) – An error result, communicated by the server
- [**ErrorResultIssue**](#cmem_client.models.error.ErrorResultIssue) – An issue listed with an ErrorResult
- [**Problem**](#cmem_client.models.error.Problem) – A problem, communicated by the server
- [**Violation**](#cmem_client.models.error.Violation) – A data violation, communicated with a problem

## `ErrorResult` {#cmem_client.models.error.ErrorResult}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

An error result, communicated by the server

returned by the build APIs (DataIntegration)

**Attributes:**

- [**title**](#cmem_client.models.error.ErrorResult.title) (<code>str</code>) – Short summary of the error.
- [**detail**](#cmem_client.models.error.ErrorResult.detail) (<code>str</code>) – Longer explanation of this particular occurrence.
- [**issues**](#cmem_client.models.error.ErrorResult.issues) (<code>list[[ErrorResultIssue](#cmem_client.models.error.ErrorResultIssue)] | None</code>) – The single issues behind the error, if the endpoint reports them. An
import which failed on several tasks lists one issue per task.

### `detail` {#cmem_client.models.error.ErrorResult.detail}

```python
detail: str
```

### `issues` {#cmem_client.models.error.ErrorResult.issues}

```python
issues: list[ErrorResultIssue] | None = None
```

### `model_config` {#cmem_client.models.error.ErrorResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `title` {#cmem_client.models.error.ErrorResult.title}

```python
title: str
```

## `ErrorResultIssue` {#cmem_client.models.error.ErrorResultIssue}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

An issue listed with an ErrorResult

**Attributes:**

- [**type**](#cmem_client.models.error.ErrorResultIssue.type) (<code>Literal['Error', 'Warning', 'Info']</code>) – Severity of the issue. Only ``Error`` means the operation failed.
- [**message**](#cmem_client.models.error.ErrorResultIssue.message) (<code>str</code>) – What the issue is.
- [**id**](#cmem_client.models.error.ErrorResultIssue.id) (<code>str</code>) – ID of the task or item the issue belongs to.

### `id` {#cmem_client.models.error.ErrorResultIssue.id}

```python
id: str
```

### `message` {#cmem_client.models.error.ErrorResultIssue.message}

```python
message: str
```

### `model_config` {#cmem_client.models.error.ErrorResultIssue.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `type` {#cmem_client.models.error.ErrorResultIssue.type}

```python
type: Literal['Error', 'Warning', 'Info']
```

## `Problem` {#cmem_client.models.error.Problem}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A problem, communicated by the server

This type of response is returned by the explore APIs (DataPlatform)

**Attributes:**

- [**type**](#cmem_client.models.error.Problem.type) (<code>str</code>) – URI identifying the kind of problem.
- [**title**](#cmem_client.models.error.Problem.title) (<code>str</code>) – Short summary of the problem.
- [**status**](#cmem_client.models.error.Problem.status) (<code>int</code>) – HTTP status code the response carried.
- [**details**](#cmem_client.models.error.Problem.details) (<code>str</code>) – Longer explanation of this particular occurrence.
- [**violations**](#cmem_client.models.error.Problem.violations) (<code>list[[Violation](#cmem_client.models.error.Violation)]</code>) – The rejected fields, for a problem caused by invalid input.

**Functions:**

- [**get_exception_message**](#cmem_client.models.error.Problem.get_exception_message) – Get error message

### `details` {#cmem_client.models.error.Problem.details}

```python
details: str = Field(default='')
```

### `get_exception_message` {#cmem_client.models.error.Problem.get_exception_message}

```python
get_exception_message()
```

Get error message

### `model_config` {#cmem_client.models.error.Problem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `status` {#cmem_client.models.error.Problem.status}

```python
status: int
```

### `title` {#cmem_client.models.error.Problem.title}

```python
title: str
```

### `type` {#cmem_client.models.error.Problem.type}

```python
type: str
```

### `violations` {#cmem_client.models.error.Problem.violations}

```python
violations: list[Violation] = Field(default=[])
```

## `Violation` {#cmem_client.models.error.Violation}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A data violation, communicated with a problem

**Attributes:**

- [**field**](#cmem_client.models.error.Violation.field) (<code>str</code>) – Name of the field which was rejected.
- [**message**](#cmem_client.models.error.Violation.message) (<code>str</code>) – What is wrong with it.

### `field` {#cmem_client.models.error.Violation.field}

```python
field: str
```

### `message` {#cmem_client.models.error.Violation.message}

```python
message: str
```

### `model_config` {#cmem_client.models.error.Violation.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

