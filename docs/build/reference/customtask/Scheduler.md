---
title: "Scheduler"
description: "Executes a workflow at specified intervals."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Scheduler
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Executes a workflow at specified intervals.


## Parameter

### Workflow

The name of the workflow to be executed

- Datatype: `task`
- Default Value: `None`



### Interval

The interval at which the scheduler should run the referenced task. Must be in ISO-8601 duration format PnDTnHnMn.nS

- Datatype: `duration`
- Default Value: `PT15M`



### Start time

The time when the scheduled task is run for the first time, e.g., 2017-12-03T10:15:30. If no start time is set, midnight on the day the scheduler is started is assumed.

- Datatype: `string`
- Default Value: `None`



### Enabled

Enables or disables the scheduler.

- Datatype: `boolean`
- Default Value: `true`



### Stop on error

If true, this will stop the scheduler, so the failed task is not scheduled again for execution.

- Datatype: `boolean`
- Default Value: `false`



