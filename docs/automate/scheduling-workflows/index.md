---
icon: material/clock-start
tags:
    - Workflow
    - Automate
    - Video
---
# Scheduling Workflows

## Introduction

For a time-based execution of a workflow, Corporate Memory provides the Scheduler operator. Please note that, in case you want to schedule workflows externally, [cmemc can be used for that](../cmemc-command-line-interface/workflow-execution-and-orchestration/index.md).

## Create a scheduler

1. Navigate to **Build → Projects** section in the workspace and Click **Create**.
1. Select the Item type **Scheduler**.
1. Click Add - then the **Create new item of type Scheduler** dialog box appears.
1. Set the properties of the Scheduler:
    1. Select the target project.
    1. Define the label of your scheduler
    1. Specify the workflow (task) to be executed.
    1. Define the interval for the scheduler to be executed again.
        Example: `PT15MD` (Every 15 minutes)
    1. Define the start time for the scheduler to be executed for the first time.
    1. Click Enable to enable the scheduler.
    1. Click Stop on error to stop the scheduler on after a failed run.

Once you are ready with the configurations, click **Create** button. Now, the scheduler will be executed with the given settings.

![Create a Scheduler](22-1-CreateScheduler.gif "Create a Scheduler")


## Modify, enable or disable a scheduler

1. Navigate to **Build → Projects** section in the workspace.
1. Search the scheduler you want to modify.
1. Select it or click on **Open Details Page** in the context menu.
1. Click on the **Configure** button in the **Configuration** section.
1. Change the values according to your needs.

## Time Interval Specification

The scheduler interval is represented an [ISO-8601 time duration string](https://en.wikipedia.org/wiki/ISO_8601#Durations) .

The following values are possible:

- `P` is the duration designator (referred to as "period"), and is always placed at the beginning of the duration.
- `Y` for defining the number of years.
- `M` for defining the number of months.
- `W` for defining the number of weeks.
- `D` for defining the number of days.
- `T` is the time designator that precedes the time components.
- `H` for defining the number of hours.
- `M` for defining the number of minutes.
- `S` for defining the number of seconds.

A duration with all values being used: `P2Y6M4DT12H30M10S` (defines a a period of 2 years, 6 months, 4 days, 12 hours, 30 minutes and 10 seconds).

More common examples:

- `PT30M` - every half hour
- `PT1H` - every hour
- `P1D` - every day

