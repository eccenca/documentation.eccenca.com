---
title: "Update Graph Insights Snapshots"
description: "Update one or more snapshots, optionally selected by affected graph."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Update Graph Insights Snapshots

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task updates [Graph Insights](https://go.eccenca.com/feature/explore-graph-exploration-graph-insights?lang=en&origin=cmem-plugin-graph-insights)
    snapshots for a specified graph in your system.

## Behavior

- **No graph selected**: All snapshots in the system are updated
- **Graph selected**: Only snapshots associated with the selected graph are updated

## Usage

1. Add this task to your workflow.
2. Optionally select a specific graph to limit which snapshots are updated.
3. Use the "Preview Snapshots" action to see which snapshots will be affected before execution.
4. Run the workflow to update the snapshots.

## Prerequisites

- Graph Insights must be active in your system
- User must have permissions to access Graph Insights
- The plugin will skip execution with a warning if these conditions are not met

## Parameter

### Selected Graph

Selected graph to update snapshots for. Leave empty for updating all snapshots.

- ID: `selected_graph`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Timeout

Timeout in seconds for Graph Insights API.

- ID: `timeout`
- Datatype: `double`
- Default Value: `100`
