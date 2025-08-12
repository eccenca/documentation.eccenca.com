---
title: "Cancel Workflow"
description: "Cancels a workflow if a specified condition is fulfilled."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Cancel Workflow
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Cancels a workflow if a specified condition is fulfilled.

## Parameter

### Type URI

The entity type to check the condition on.

- Datatype: `uri`
- Default Value: `None`



### Condition

The cancellation condition

- Datatype: `enumeration`
- Default Value: `empty`



### Invert condition

If true, the specified condition will be inverted, i.e., the workflow execution will be cancelled if the condition is not fulfilled.

- Datatype: `boolean`
- Default Value: `false`



### Fail workflow

If true, the workflow execution will fail if the condition is met. If false, the workflow execution would be stopped, but shown as successfull.

- Datatype: `boolean`
- Default Value: `false`



