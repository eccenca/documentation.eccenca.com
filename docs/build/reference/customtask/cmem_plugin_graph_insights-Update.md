---
title: "Create or Update Graph Insights Snapshots"
description: "Create a snapshot for a graph that has none, or update it if one already exists."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Create or Update Graph Insights Snapshots

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task creates or updates [Graph Insights](https://go.eccenca.com/feature/explore-graph-insights?lang=en&origin=cmem-plugin-graph-insights)
    snapshots for a specified graph in your system.

## Behavior

- **No graph selected**: All snapshots in the system are updated
- **Graph selected**: Every snapshot associated with the selected graph (including
  ones where it is only an imported sub-graph) is updated. If the selected graph
  does not have a dedicated snapshot of its own yet, one is also created for it.

## Usage

1. Add this task to your workflow.
2. Optionally select a specific graph to create or update its snapshot.
3. Use the "Preview Snapshots" action to see which snapshots will be affected,
   and whether a new one will be created, before execution.
4. Run the workflow to create or update the snapshots.

## Prerequisites

- Graph Insights must be active in your system
- User must have permissions to access Graph Insights
- The plugin will skip execution with a warning if these conditions are not met


## Parameter

### Selected Graph

Graph to create or update a snapshot for. Leave empty to update every existing snapshot instead.

- ID: `selected_graph`
- Datatype: `scheme:string`
- Default Value: `None`

## Advanced Parameter

### Timeout

Timeout in seconds for Graph Insights API.

- ID: `timeout`
- Datatype: `double`
- Default Value: `100`
