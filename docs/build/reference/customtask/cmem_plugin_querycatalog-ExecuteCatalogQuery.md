---
title: "Execute Catalog Query"
description: "Run a query stored in a query catalog and hand on its result."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Execute Catalog Query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task runs a query that is stored in a query catalog, so a workflow references the
stored definition instead of carrying a second copy of it.

## What flows through the ports

What leaves the task follows the type of the query. A SELECT query produces one entity
per result row with one value per projected variable, and a variable the query left
unbound produces no value rather than an empty string. An ASK query produces a single
entity carrying `true` or `false`. A CONSTRUCT or DESCRIBE query produces its
statements as quad entities with no graph set, ready for any task that consumes quads.
An update query produces nothing at all: the task is a terminal step and hands nothing
on.

A query that contains placeholders turns their names into input fields, so the
preceding task can be mapped onto them, and the query is then run once per incoming
entity with the results of all of them arriving together. A query without placeholders
has no input and runs on its own.

## Where the task sits

**Get Catalog Query** and **List Catalog Queries** describe queries without running
them, and are the way to find the query this task should be pointed at.

## Caveats

- **The stored query is read again on every execution.** Editing it in the query
  catalog changes what runs next time, which is the point of the task - but it also
  means a query that gained a placeholder since the workflow was wired fails, naming
  what changed, rather than running with a hole in it.
- **The query kind is a safety gate, not only a filter.** A query that has become an
  update is refused while the task is set to read queries, so editing the catalog
  cannot turn a reading step into a writing one.
- **The whole result is held in memory.** The store sends it in one response, so a
  query returning very many rows is limited by what the DataIntegration process can
  hold.
- **Continuing past a failed input entity can leave a write half applied.** Entities
  are run one after another against the store and nothing rolls an earlier one back.


## Parameter

### Catalog Graph

The graph the query is read from. The list offers the query catalogs first, then the shape catalogs, then any other graph that holds queries, with the number of read and write queries each one contains.

- ID: `catalog_graph`
- Datatype: `string`
- Default Value: `None`



### Query Kind

Which half of the catalog the query list offers. It also decides what this task is allowed to run: a query that has become an update since the task was configured is refused while this is set to read queries.

- ID: `query_kind`
- Datatype: `string`
- Default Value: `read`



### Query

The query to use, picked by its label. Choose the catalog graph and the query kind first; changing either of them clears this field.

- ID: `query`
- Datatype: `string`
- Default Value: `None`



### Context



- ID: `context`
- Datatype: `PluginContext`
- Default Value: `None`

## Advanced Parameter

### Timeout

How many milliseconds the store may spend on one execution before it is aborted. Zero leaves the decision to the store, which is the right choice unless a query has been seen to run away.

- ID: `timeout`
- Datatype: `Long`
- Default Value: `0`



### On error

What happens when the query fails for a single input entity. Either way the workflow ends in an error. Note that continuing through a write query can leave part of its changes applied: the entities are run one after another and nothing rolls them back.

- ID: `on_error`
- Datatype: `string`
- Default Value: `stop`
