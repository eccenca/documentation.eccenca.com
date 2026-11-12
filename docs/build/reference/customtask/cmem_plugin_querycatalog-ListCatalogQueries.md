---
title: "List Catalog Queries"
description: "Emit one entity per query stored in a query catalog."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# List Catalog Queries

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task reads a query catalog and emits one entity for each query it holds,
describing the query rather than running it.

Each entity carries the catalog graph, the query IRI, its label and description, its
type, its query text as stored, and the names of the placeholders that text contains.
The query text is emitted unfilled, with its placeholders intact. The task takes no
input, so it can open a workflow.

It emits exactly what **Get Catalog Query** emits, in the same order, so one can
replace the other without rewiring whatever consumes it. Use this task to take stock of
a catalog, to drive a loop over its queries, or to find the query IRI that
**Execute Catalog Query** should be pointed at.

A catalog holding no query of the selected kind yields no entities and no error, which
is a legitimate answer about an empty catalog rather than a failure.


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

## Advanced Parameter

`None`
