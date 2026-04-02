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


This workflow operator retrieves a specific execution report of a workflow and outputs it
as a JSON file.

The plugin queries the backend API to list all available reports for the given workflow and
allows you to select which report to retrieve:

- **Latest Report**: The most recent execution report
- **Latest Report with Errors**: The most recent failed execution report
- **Latest Report with Warning or Errors**: The most recent report with warnings (successful or not)

The report contains detailed information about the workflow execution, including task results,
execution times, and any errors or warnings.

## Output

The plugin outputs a single JSON file entity containing the complete workflow execution report.

## Usage

This operator is useful for:

- Monitoring workflow execution results and failures
- Debugging recent errors or warnings
- Creating audit trails of workflow runs
- Archiving execution reports for compliance purposes
- Feeding execution data into downstream analysis tasks


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

The time period in hours of the workflow execution reports that can be listed.Allows only full hours. Defaults to 0 for every execution report.

- ID: `time_period`
- Datatype: `Long`
- Default Value: `0`





## Advanced Parameter

`None`
