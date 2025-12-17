---
title: "Get workflow report"
description: "Output the last report of a workflow as a JSON file."
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

This workflow operator retrieves the most recent execution report of a specified workflow
and outputs it as a JSON file.

The plugin queries the backend API to list all available reports for the given workflow,
sorts them by timestamp, and downloads the latest report. The report contains detailed information
about the workflow execution, including task results, execution times, and any errors or warnings.

## Output

The plugin outputs a single JSON file entity containing the complete workflow execution report.

## Usage

This operator is useful for:

- Monitoring workflow execution results
- Creating audit trails of workflow runs
- Archiving execution reports for compliance purposes
- Feeding execution data into downstream analysis tasks

## Parameter

### Workflow

- ID: `workflow_id`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
