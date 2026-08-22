---
title: "Scheduler"
description: "Executes a workflow at specified intervals."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Scheduler

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The Scheduler plugin executes a given workflow at specified intervals.

## Description

The Scheduler executes an existing workflow periodically. The workflow is specified via its _name_ in the `task`
parameter, and the period is set with the `interval` parameter. The workflow will then be scheduled for a
_periodic execution **without termination**_, i.e. it will run _until cancelled_ or until an otherwise erroneous event
occurs. In order to cancel a workflow, consider using the Cancel Workflow plugin.

The required format for the `interval` is the duration format of the international standard
[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).
In a nutshell, the relevant formatting for us is `PnDTnHnMn.nS`, where `P` indicates the **p**eriod, `nD` stands for the
**n**umber of **d**ays, and `nH`, `nM` and `nS` are, respectively, the **n**umber of **h**ours, **m**inutes and
**s**econds. Similarly to the `P`, the `T` introduces the **t**ime component, i.e. that part of the chronological
information related to a given day in the sense of 24 hours.

Notice that the _full_ ISO-8601 format is `PnYnMnWnDTnHnMnS`, which includes the portion `"nYnMnW"` for the number of
**y**ears, **m**onths and **w**eeks. These units are not supported by this plugin: only the (sub)format `PnDTnHnMn.nS`
is accepted. The interval must be at least one millisecond.

Additionally to the _period_ or interval of execution, we can also control the _starting time_ with the parameter
`startTime`. It is an ISO-8601 date and time, e.g. `2017-12-03T10:15:30`, and is interpreted as **UTC**, independently
of the timezone the server is configured with. Alternatively, an explicit UTC offset in the form `+01:00` or `Z` can
be appended, e.g. `2017-12-03T10:15:30+01:00`. If no start time is set, midnight UTC on the day the scheduler is
started is assumed.

The scheduler can be disabled with the parameter `enabled`. It can also be made to stop after the first encountered
error within a given execution of the specified workflow. This short-circuiting behavior may be useful in certain
circumstances, so as to avoid the accumulation of errors (snowball effect).

A scheduled execution is skipped if an execution of the same workflow is still running, e.g. one that has been started
manually or one that was left running when the scheduler was restarted. The skipped execution is not caught up on
later. The scheduler itself never runs the same workflow twice in parallel, since the interval is counted from the end
of the previous execution.

### Special considerations

The Scheduler will execute the given workflow _periodically_, regardless of the position in time of the _start time_.
In other words: If the start time lies in the _past_, then the workflow _will_ be executed (periodically) once the
_next_ period occurs. If the start time lies in the _future_, then this is simply a _delay_.


## Parameter

### Workflow

The name of the workflow to be executed

- ID: `task`
- Datatype: `task`
- Default Value: `None`



### Interval

The interval at which the scheduler should run the referenced task. It must be in ISO-8601 duration format PnDTnHnMn.nS and at least one millisecond.

- ID: `interval`
- Datatype: `duration`
- Default Value: `PT15M`



### Start time

The time when the scheduled task is run for the first time, in ISO-8601 format, e.g., 2017-12-03T10:15:30. The time is interpreted as UTC, independently of the server timezone; alternatively an explicit UTC offset in the form +01:00 or Z can be appended (e.g., 2017-12-03T10:15:30+01:00). If no start time is set, midnight UTC on the day the scheduler is started is assumed.

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
