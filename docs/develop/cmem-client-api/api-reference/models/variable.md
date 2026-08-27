---
title: "cmem-client: variable module"
description: "Corporate Memory project variable models for data integration."
tags:
  - API
  - Python
  - cmem-client
---

# `variable` {#cmem_client.models.variable}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory project variable models for data integration.

This module defines models for representing project variables within Corporate Memory
DataIntegration projects. Variables can hold static values or Jinja2 template strings
that reference other variables, and are used to parameterize datasets and tasks.

**Classes:**

- [**Variable**](#cmem_client.models.variable.Variable) – A project variable in Corporate Memory DataIntegration.

## `Variable` {#cmem_client.models.variable.Variable}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A project variable in Corporate Memory DataIntegration.

**Attributes:**

- [**name**](#cmem_client.models.variable.Variable.name) (<code>str</code>) – Name of the variable, unique within its project. This is what a template
refers to.
- [**project_id**](#cmem_client.models.variable.Variable.project_id) (<code>str</code>) – ID of the project the variable belongs to.
- [**value**](#cmem_client.models.variable.Variable.value) (<code>str</code>) – Resolved value of the variable. For a templated variable this is the
rendered result, so it is read-only.
- [**template**](#cmem_client.models.variable.Variable.template) (<code>str</code>) – Jinja2 template the value is rendered from. Empty for a variable
which holds a static value.
- [**description**](#cmem_client.models.variable.Variable.description) (<code>str</code>) – Description of the variable as maintained in the project.
- [**is_sensitive**](#cmem_client.models.variable.Variable.is_sensitive) (<code>bool</code>) – Whether the value is treated as a secret. Sensitive values are
masked by the user interface.
- [**scope**](#cmem_client.models.variable.Variable.scope) (<code>str</code>) – Scope the variable is defined in, ``project`` for a project variable.

**Functions:**

- [**get_id**](#cmem_client.models.variable.Variable.get_id) – Get the combined ID of the variable in the form ``project_id:name``.

### `description` {#cmem_client.models.variable.Variable.description}

```python
description: str = ''
```

### `get_id` {#cmem_client.models.variable.Variable.get_id}

```python
get_id()
```

Get the combined ID of the variable in the form ``project_id:name``.

### `is_sensitive` {#cmem_client.models.variable.Variable.is_sensitive}

```python
is_sensitive: bool = Field(alias='isSensitive', default=False)
```

### `model_config` {#cmem_client.models.variable.Variable.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.variable.Variable.name}

```python
name: str
```

### `project_id` {#cmem_client.models.variable.Variable.project_id}

```python
project_id: str = Field(alias='project')
```

### `scope` {#cmem_client.models.variable.Variable.scope}

```python
scope: str = 'project'
```

### `template` {#cmem_client.models.variable.Variable.template}

```python
template: str = ''
```

### `value` {#cmem_client.models.variable.Variable.value}

```python
value: str = ''
```

