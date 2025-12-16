---
title: "Cancel Workflow"
description: "Cancels a workflow if a specified condition is fulfilled. A typical use case for this operator is to cancel the workflow execution if the input data is empty."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Cancel Workflow
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Cancels a workflow if a specified condition is fulfilled. A typical use case for this operator is to cancel the workflow execution if the input data is empty.

## Parameter

### Type URI

The entity type to check the condition on.

- ID: `typeUri`
- Datatype: `uri`
- Default Value: `None`

### Condition

The cancellation condition

- ID: `condition`
- Datatype: `enumeration`
- Default Value: `empty`

### Invert condition

If true, the specified condition will be inverted, i.e., the workflow execution will be cancelled if the condition is not fulfilled.

- ID: `invertCondition`
- Datatype: `boolean`
- Default Value: `false`

### Fail workflow

If true, the workflow execution will fail if the condition is met. If false, the workflow execution would be stopped, but shown as successfull.

- ID: `failWorkflow`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
