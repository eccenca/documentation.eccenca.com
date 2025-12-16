---
title: "Scheduler"
description: "Executes a workflow at specified intervals."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Scheduler
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The eccenca Build plugin `Scheduler` executes a given workflow at specified intervals.

## Description

The `Scheduler` executes an existing workflow periodically. The workflow is specified via its _name_ in the `task`
parameter, and the period is set with the `interval` (number of minutes). The workflow will then be scheduled for a
_periodic execution **without termination**_, i.e. it will run _until cancelled_ or until an otherwise erroneous event
occurs. In order to cancel a workflow, consider using the `CancelWorkflow` plugin.

Additionally to the _period_ or interval of execution, we can also control the _starting time_ with the parameter
`startTime`. The required format for this starting time is the international standard
[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).
In a nutshell, the relevant formatting for us is `PnDTnHnMn.nS`, where `P` indicates the **p**eriod, `nD` stands for the
**n**umber of **d**ays, and `nH`, `nM` and `nS` are, respectively, the **n**umber of **h**ours, **m**inutes and
**s**econds. Similarly to the `P`, the `T` introduces the **t**ime component, i.e. that part of the chronological
information related to a given day in the sense of 24 hours.

Notice that the _full_ ISO-8601 format is `PnYnMnWnDTnHnMnS`, which includes the portion `"nYnMnW"` for the number of
**y**ears, **m**onths and **w**eeks. In the case of this plugin, such long time periods should be avoided. That's why
we restrict ourselves to the (sub)format `PnDTnHnMn.nS`.

The scheduler can be disabled with the parameter `enabled`. It can also be made to stop after the first encountered
error within a given execution of the specified workflow. This short-circuiting behavior may be useful in certain
circumstances, so as to avoid the accumulation of errors (snowball effect).

### Special considerations

The `Scheduler` will execute the given workflow _periodically_, regardless of the position in time of the _start time_.
In other words: If the start time lies in the _past_, then the workflow _will_ be executed (periodically) once the
_next_ period occurs. If the start time lies in the _future_, then this is simply a _delay_.

## Relation to other plugins

As mentioned, the `CancelWorkflow` plugin can be used on par in order to _cancel_ the otherwise never-ending execution
of a workflow.

## Parameter

### Workflow

The name of the workflow to be executed

- ID: `task`
- Datatype: `task`
- Default Value: `None`

### Interval

The interval at which the scheduler should run the referenced task. It must be in ISO-8601 duration format PnDTnHnMn.nS.

- ID: `interval`
- Datatype: `duration`
- Default Value: `PT15M`

### Start time

The time when the scheduled task is run for the first time, e.g., 2017-12-03T10:15:30. If no start time is set, midnight on the day the scheduler is started is assumed.

- ID: `startTime`
- Datatype: `string`
- Default Value: `None`

### Enabled

Enables or disables the scheduler. It's enabled by default.

- ID: `enabled`
- Datatype: `boolean`
- Default Value: `true`

### Stop on error

If set to true, this will stop the scheduler, so the failed task is not scheduled again for execution.

- ID: `stopOnError`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
