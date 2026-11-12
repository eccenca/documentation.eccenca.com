---
title: "Get Catalog Query"
description: "Emit one entity describing a query stored in a query catalog."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Get Catalog Query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task looks a query up in a query catalog and emits one entity describing it,
without running it.

The entity carries the catalog graph, the query IRI, its label and description, its
type, its query text as stored, and the names of the placeholders that text contains.
The query text is emitted unfilled, with its placeholders intact, which is what makes
it useful to a task that wants to inspect or transform a query rather than execute one.

With a query chosen on the task, it emits exactly one entity and takes no input. With
the query left empty, the queries to look up arrive on an input port instead, as a
catalog graph and a query IRI per entity, and one entity is emitted for each. An
incoming entity that leaves the catalog graph empty falls back to the catalog chosen
on the task, so a list of query IRIs from one catalog needs no constant column.

It emits exactly what **List Catalog Queries** emits, in the same order, and the
first two values it emits are what it accepts on its own input port - so the two tasks
chain directly. **Execute Catalog Query** is the one that runs a query.

A query IRI that the named catalog does not hold fails the task rather than being
skipped, because a workflow asking for a specific query and silently receiving nothing
is the harder failure to notice.


## Parameter

### Catalog Graph

The graph the query is read from. The list offers the query catalogs first, then the shape catalogs, then any other graph that holds queries, with the number of read and write queries each one contains.

- ID: `catalog_graph`
- Datatype: `string`
- Default Value: `None`



### Query Kind

Which half of the catalog the query list offers.

- ID: `query_kind`
- Datatype: `string`
- Default Value: `all`



### Query

The query to use, picked by its label. Choose the catalog graph and the query kind first; changing either of them clears this field.

- ID: `query`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
