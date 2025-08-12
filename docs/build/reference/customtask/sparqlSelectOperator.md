---
title: "SPARQL Select query"
description: "A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# SPARQL Select query
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected.

## Parameter

### Select query

A SPARQL 1.1 select query

- Datatype: `code-sparql`
- Default Value: `None`



### Result limit

If set to a positive integer, the number of results is limited

- Datatype: `string`
- Default Value: `None`



### Optional SPARQL dataset

An optional SPARQL dataset that can be used for example data, so e.g. the transformation editor shows mapping examples.

- Datatype: `SPARQL endpoint`
- Default Value: `None`



### SPARQL query timeout (ms)

SPARQL query timeout (select/update) in milliseconds. A value of zero means that there is no timeout set explicitly. If a value greater zero is specified this overwrites possible default timeouts.

- Datatype: `int`
- Default Value: `0`



