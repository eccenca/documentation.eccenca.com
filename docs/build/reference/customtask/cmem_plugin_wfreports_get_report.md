---
title: "Get workflow report"
description: "Output a workflow execution report as a JSON file."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Get workflow report

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow operator retrieves one execution report of a workflow and outputs it as a JSON
file.

## Ports

The task has no input port; it queries the reports available for the selected workflow
directly. It outputs a single JSON file entity holding the report - the same JSON payload
returned for that execution, including its finish status and any warnings.

## Usage

With no input port, this operator is typically the first task in a workflow. Its output feeds
a downstream task that reads or forwards the JSON file, for example to inspect it, archive it,
or route on the presence of errors or warnings.

## Caveats

- If no report matches the selected mode - none currently carries warnings or errors, or the
  time period excludes every report - the output file contains an empty JSON object `{}`, not
  an error or any other indication that nothing was found.
- Finding the latest report with warnings or errors is checked from newest to oldest, and may
  fetch every report in scope individually before a match is found or the list is exhausted.


## Parameter

### Workflow

The workflow from which the reports get listed.

- ID: `workflow_id`
- Datatype: `string`
- Default Value: `None`



### Report

Selector for reports to be shown.

- ID: `report_selected`
- Datatype: `string`
- Default Value: `Latest Report`



### Time Period

The time period in hours of the workflow execution reports that can be listed. Allows only full hours. Defaults to 0, which lists every execution report.

- ID: `time_period`
- Datatype: `Long`
- Default Value: `0`

## Advanced Parameter

`None`
