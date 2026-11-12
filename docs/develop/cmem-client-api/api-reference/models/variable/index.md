---
title: "cmem-client: models.variable module"
description: "Corporate Memory variable models for data integration."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.variable` {#cmem_client.models.variable}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory variable models for data integration.

This module defines models for representing the variables of Corporate Memory
DataIntegration projects. Variables can hold static values or Jinja2 template strings
that reference other variables, and are used to parameterize datasets and tasks.

A project variable belongs to a project. An execution variable is declared on a single
task of a project, e.g. a workflow or a dataset. A global variable is defined in the
configuration of DataIntegration, so it belongs to no project and is read-only.

**Classes:**

- [**AllVariablesResponse**](#cmem_client.models.variable.AllVariablesResponse) – The response of the endpoint which lists the global variables and those of all projects.
- [**DependentTask**](#cmem_client.models.variable.DependentTask) – A task which uses a variable, e.g. in a parameter template or an execution variable.
- [**GlobalVariables**](#cmem_client.models.variable.GlobalVariables) – The global variables, which are defined in the configuration of DataIntegration.
- [**ProjectVariables**](#cmem_client.models.variable.ProjectVariables) – A project together with its project variables and the variables of its tasks.
- [**TaskVariables**](#cmem_client.models.variable.TaskVariables) – A task of a project together with its execution variables.
- [**Variable**](#cmem_client.models.variable.Variable) – A project, execution or global variable in Corporate Memory DataIntegration.
- [**VariableDependents**](#cmem_client.models.variable.VariableDependents) – What still uses a variable, so that it cannot be deleted.
- [**VariableError**](#cmem_client.models.variable.VariableError) – An error the server reports for a single variable, e.g. a template it can not resolve.
- [**WorkflowExecutionVariable**](#cmem_client.models.variable.WorkflowExecutionVariable) – An execution variable a workflow run needs.

## `AllVariablesResponse` {#cmem_client.models.variable.AllVariablesResponse}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The response of the endpoint which lists the global variables and those of all projects.

The variables in it carry neither their project nor their task ID, these are given
by the project and task they are listed under.

**Attributes:**

- [**global_variables**](#cmem_client.models.variable.AllVariablesResponse.global_variables) (<code>[GlobalVariables](#cmem_client.models.variable.GlobalVariables)</code>) – The global variables.
- [**projects**](#cmem_client.models.variable.AllVariablesResponse.projects) (<code>list[[ProjectVariables](#cmem_client.models.variable.ProjectVariables)]</code>) – The projects the user has access to, with their variables.

### `global_variables` {#cmem_client.models.variable.AllVariablesResponse.global_variables}

```python
global_variables: GlobalVariables = Field(alias='global', default_factory=GlobalVariables)
```

### `model_config` {#cmem_client.models.variable.AllVariablesResponse.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `projects` {#cmem_client.models.variable.AllVariablesResponse.projects}

```python
projects: list[ProjectVariables] = Field(default_factory=list)
```

## `DependentTask` {#cmem_client.models.variable.DependentTask}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A task which uses a variable, e.g. in a parameter template or an execution variable.

**Attributes:**

- [**id**](#cmem_client.models.variable.DependentTask.id) (<code>str</code>) – ID of the task.
- [**label**](#cmem_client.models.variable.DependentTask.label) (<code>str</code>) – Label of the task.
- [**task_type**](#cmem_client.models.variable.DependentTask.task_type) (<code>str</code>) – Type of the task, e.g. ``dataset``, ``transform`` or ``workflow``.
Empty where the server does not report it.

### `id` {#cmem_client.models.variable.DependentTask.id}

```python
id: str
```

### `label` {#cmem_client.models.variable.DependentTask.label}

```python
label: str = ''
```

### `model_config` {#cmem_client.models.variable.DependentTask.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `task_type` {#cmem_client.models.variable.DependentTask.task_type}

```python
task_type: str = Field(alias='taskType', default='')
```

## `GlobalVariables` {#cmem_client.models.variable.GlobalVariables}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The global variables, which are defined in the configuration of DataIntegration.

**Attributes:**

- [**variables**](#cmem_client.models.variable.GlobalVariables.variables) (<code>list[[Variable](#cmem_client.models.variable.Variable)]</code>) – The global variables.

### `model_config` {#cmem_client.models.variable.GlobalVariables.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `variables` {#cmem_client.models.variable.GlobalVariables.variables}

```python
variables: list[Variable] = Field(default_factory=list)
```

## `ProjectVariables` {#cmem_client.models.variable.ProjectVariables}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A project together with its project variables and the variables of its tasks.

**Attributes:**

- [**id**](#cmem_client.models.variable.ProjectVariables.id) (<code>str</code>) – ID of the project.
- [**label**](#cmem_client.models.variable.ProjectVariables.label) (<code>str</code>) – Label of the project.
- [**variables**](#cmem_client.models.variable.ProjectVariables.variables) (<code>list[[Variable](#cmem_client.models.variable.Variable)]</code>) – The project variables.
- [**errors**](#cmem_client.models.variable.ProjectVariables.errors) (<code>list[[VariableError](#cmem_client.models.variable.VariableError)]</code>) – Errors of single project variables.
- [**tasks**](#cmem_client.models.variable.ProjectVariables.tasks) (<code>list[[TaskVariables](#cmem_client.models.variable.TaskVariables)]</code>) – All tasks of the project, including tasks without execution variables.

### `errors` {#cmem_client.models.variable.ProjectVariables.errors}

```python
errors: list[VariableError] = Field(default_factory=list)
```

### `id` {#cmem_client.models.variable.ProjectVariables.id}

```python
id: str
```

### `label` {#cmem_client.models.variable.ProjectVariables.label}

```python
label: str = ''
```

### `model_config` {#cmem_client.models.variable.ProjectVariables.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `tasks` {#cmem_client.models.variable.ProjectVariables.tasks}

```python
tasks: list[TaskVariables] = Field(default_factory=list)
```

### `variables` {#cmem_client.models.variable.ProjectVariables.variables}

```python
variables: list[Variable] = Field(default_factory=list)
```

## `TaskVariables` {#cmem_client.models.variable.TaskVariables}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A task of a project together with its execution variables.

**Attributes:**

- [**id**](#cmem_client.models.variable.TaskVariables.id) (<code>str</code>) – ID of the task.
- [**label**](#cmem_client.models.variable.TaskVariables.label) (<code>str</code>) – Label of the task.
- [**variables**](#cmem_client.models.variable.TaskVariables.variables) (<code>list[[Variable](#cmem_client.models.variable.Variable)]</code>) – The execution variables declared on the task.
- [**errors**](#cmem_client.models.variable.TaskVariables.errors) (<code>list[[VariableError](#cmem_client.models.variable.VariableError)]</code>) – Errors of single execution variables of the task.

### `errors` {#cmem_client.models.variable.TaskVariables.errors}

```python
errors: list[VariableError] = Field(default_factory=list)
```

### `id` {#cmem_client.models.variable.TaskVariables.id}

```python
id: str
```

### `label` {#cmem_client.models.variable.TaskVariables.label}

```python
label: str = ''
```

### `model_config` {#cmem_client.models.variable.TaskVariables.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `variables` {#cmem_client.models.variable.TaskVariables.variables}

```python
variables: list[Variable] = Field(default_factory=list)
```

## `Variable` {#cmem_client.models.variable.Variable}

Bases: <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A project, execution or global variable in Corporate Memory DataIntegration.

**Attributes:**

- [**name**](#cmem_client.models.variable.Variable.name) (<code>str</code>) – Name of the variable, unique within its project or task. This is what a
template refers to.
- [**project_id**](#cmem_client.models.variable.Variable.project_id) (<code>str</code>) – ID of the project the variable belongs to. Together with ``name``,
and ``task_id`` for an execution variable, it forms the key of the repository.
Empty for a global variable.
- [**task_id**](#cmem_client.models.variable.Variable.task_id) (<code>str | None</code>) – ID of the task an execution variable is declared on. ``None`` for a
project variable.
- [**value**](#cmem_client.models.variable.Variable.value) (<code>str</code>) – Resolved value of the variable. For a templated variable this is the
rendered result, so it is read-only. Empty where the server masks the value,
which it does for sensitive variables when listing all variables.
- [**template**](#cmem_client.models.variable.Variable.template) (<code>str</code>) – Jinja2 template the value is rendered from. Empty for a variable
which holds a static value.
- [**description**](#cmem_client.models.variable.Variable.description) (<code>str</code>) – Description of the variable as maintained in the project.
- [**is_sensitive**](#cmem_client.models.variable.Variable.is_sensitive) (<code>bool</code>) – Whether the value is treated as a secret. Sensitive values are
masked by the user interface.
- [**scope**](#cmem_client.models.variable.Variable.scope) (<code>str</code>) – Scope the variable is defined in, ``project`` for a project variable,
``execution`` for an execution variable and ``global`` for a global variable.

**Functions:**

- [**get_id**](#cmem_client.models.variable.Variable.get_id) – Get the combined ID of the variable.

### `description` {#cmem_client.models.variable.Variable.description}

```python
description: str = ''
```

### `get_id` {#cmem_client.models.variable.Variable.get_id}

```python
get_id()
```

Get the combined ID of the variable.

**Returns:**

- <code>str</code> – ``project_id:name`` for a project variable, ``project_id:task_id:name``
- <code>str</code> – for an execution variable and ``name`` for a global variable.

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
project_id: str = Field(alias='project', default='')
```

### `scope` {#cmem_client.models.variable.Variable.scope}

```python
scope: str = 'project'
```

### `task_id` {#cmem_client.models.variable.Variable.task_id}

```python
task_id: str | None = Field(alias='task', default=None)
```

### `template` {#cmem_client.models.variable.Variable.template}

```python
template: str = ''
```

### `value` {#cmem_client.models.variable.Variable.value}

```python
value: str = ''
```

## `VariableDependents` {#cmem_client.models.variable.VariableDependents}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

What still uses a variable, so that it cannot be deleted.

**Attributes:**

- [**variables**](#cmem_client.models.variable.VariableDependents.variables) (<code>list[str]</code>) – Names of the variables in the same scope whose templates use the
variable: project variables for a project variable, execution variables of
the same task for an execution variable.
- [**tasks**](#cmem_client.models.variable.VariableDependents.tasks) (<code>list[[DependentTask](#cmem_client.models.variable.DependentTask)]</code>) – Tasks which use the variable.

### `model_config` {#cmem_client.models.variable.VariableDependents.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `tasks` {#cmem_client.models.variable.VariableDependents.tasks}

```python
tasks: list[DependentTask] = Field(alias='dependentTasks', default_factory=list)
```

### `variables` {#cmem_client.models.variable.VariableDependents.variables}

```python
variables: list[str] = Field(alias='dependentVariables', default_factory=list)
```

## `VariableError` {#cmem_client.models.variable.VariableError}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

An error the server reports for a single variable, e.g. a template it can not resolve.

**Attributes:**

- [**variable_name**](#cmem_client.models.variable.VariableError.variable_name) (<code>str</code>) – Name of the variable the error belongs to.
- [**message**](#cmem_client.models.variable.VariableError.message) (<code>str</code>) – The error message.

### `message` {#cmem_client.models.variable.VariableError.message}

```python
message: str = ''
```

### `model_config` {#cmem_client.models.variable.VariableError.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `variable_name` {#cmem_client.models.variable.VariableError.variable_name}

```python
variable_name: str = Field(alias='variableName')
```

## `WorkflowExecutionVariable` {#cmem_client.models.variable.WorkflowExecutionVariable}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

An execution variable a workflow run needs.

**Attributes:**

- [**name**](#cmem_client.models.variable.WorkflowExecutionVariable.name) (<code>str</code>) – Name of the variable, referenced as ``{{execution.<name>}}``.
- [**required**](#cmem_client.models.variable.WorkflowExecutionVariable.required) (<code>bool</code>) – Whether the variable has to be provided when the run is started,
because it is used at execution time but neither defined on the workflow
nor set by a preceding node.
- [**default**](#cmem_client.models.variable.WorkflowExecutionVariable.default) (<code>[Variable](#cmem_client.models.variable.Variable) | None</code>) – The default defined on the workflow, if any. Only the defaults of the
executed workflow apply to a run, defaults of sub-tasks do not. The value
of a sensitive default is omitted by the server.
- [**referenced_by**](#cmem_client.models.variable.WorkflowExecutionVariable.referenced_by) (<code>list[[DependentTask](#cmem_client.models.variable.DependentTask)]</code>) – Tasks which use the variable at execution time.
- [**set_by**](#cmem_client.models.variable.WorkflowExecutionVariable.set_by) (<code>list[[DependentTask](#cmem_client.models.variable.DependentTask)]</code>) – Tasks which set the variable during the run.

### `default` {#cmem_client.models.variable.WorkflowExecutionVariable.default}

```python
default: Variable | None = None
```

### `model_config` {#cmem_client.models.variable.WorkflowExecutionVariable.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.variable.WorkflowExecutionVariable.name}

```python
name: str
```

### `referenced_by` {#cmem_client.models.variable.WorkflowExecutionVariable.referenced_by}

```python
referenced_by: list[DependentTask] = Field(alias='referencedBy', default_factory=list)
```

### `required` {#cmem_client.models.variable.WorkflowExecutionVariable.required}

```python
required: bool = False
```

### `set_by` {#cmem_client.models.variable.WorkflowExecutionVariable.set_by}

```python
set_by: list[DependentTask] = Field(alias='setBy', default_factory=list)
```

