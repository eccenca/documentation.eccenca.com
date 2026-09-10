---
title: "Set execution variable"
description: "Sets an execution variable to the first value of the (single) input and passes the input through unchanged. The variable is written to the 'execution' scope and can be read downstream as 'execution.<name>'. Only works while running inside a workflow execution."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Set execution variable

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Sets a single **execution-scope** template variable from this operator's input and passes the input through
unchanged, so it can be inserted anywhere in a workflow chain.

The variable is written to the `execution` scope. A value set by this operator replaces an execution variable
of the same name that was defined as a default on the workflow or provided when the run was started. This
operator only takes effect while running inside a workflow execution, where all nodes share one
execution-variable holder.

Any downstream node can read the variable as `{{execution.<name>}}`. Referencing an execution variable that
has not been set fails.

It is the workflow-operator counterpart of the **Set execution variable** transformer (`setExecutionVariable`):
use this operator to pass a value between workflow nodes without embedding a transform.

## Behaviour

- Reads a value from the **first entity** of the input: the first value of **Source path**, or the entity's
  first value when no source path is given. Later entities are not consulted.
- Writes it to the execution scope under `variableName`. If the input is empty or the first entity has no such
  value, the variable is left unchanged (a default or run-start override stays in place).
- Forwards the input entities unchanged (connect the output to keep the chain going, or leave it unconnected to
  use this purely as a side-effecting node).


## Parameter

### Variable name

Name of the execution variable to set. It is written to the 'execution' scope and addressed downstream as 'execution.<name>'.

- ID: `variableName`
- Datatype: `string`
- Default Value: `myVariable`



### Source path

Optional path/attribute of the input that supplies the value. If left empty, the first value of the input is used.

- ID: `sourcePath`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
