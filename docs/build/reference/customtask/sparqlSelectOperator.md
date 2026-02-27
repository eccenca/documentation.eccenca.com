---
title: "SPARQL Select query"
description: "A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# SPARQL Select query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The SPARQL SELECT plugin is a task for executing SPARQL SELECT queries on the input RDF data source.

## Description

The `sparqlSelectOperator` plugin is an example of a _RDF task_ or _operator_. Such a task can be used in a workflow,
connecting an input to an output. In this specific case, the _input_ is — in essence — a _SPARQL endpoint_ and the
_output_ is the entity table containing the _SPARQL results_ of the SPARQL SELECT query execution.

In general terms, a [SPARQL 1.1 SELECT](https://www.w3.org/TR/sparql11-query/#select) query is supported. One of the
simplest examples is `SELECT * WHERE { ?s ?p ?o }`.

The [result limit](https://www.w3.org/TR/sparql11-query/#modResultLimit) can be specified for the SPARQL SELECT plugin
itself, with the parameter `limit`. Additionally, a timeout can be specified with the parameter `sparqlTimeout`.

As usual, the SPARQL results contain both "variables" and "bindings", such as in
[this example](https://www.w3.org/TR/sparql11-results-json/#json-result-object).
This tabular raw form is transformed into an _entity table_.

### Internal Specifics

If the SPARQL source is defined on a specific graph, a `FROM` clause will be added to the query at execution time,
except when there already exists a `GRAPH` or `FROM` clause in the query. `FROM NAMED` clauses are not injected.

## Related plugins

Other types of RDF tasks are the `sparqlCopyOperator` for executing SPARQL CONSTRUCT queries, and the
`sparqlUpdateOperator` for building SPARQL UPDATE queries from a templating engine.

Regarding the input dataset, any RDF dataset is acceptable. For further details on the RDF datasets, see for example the
documentation of the `sparqlEndpoint` plugin.

## Parameter

### Select query

A SPARQL 1.1 select query

- ID: `selectQuery`
- Datatype: `code-sparql`
- Default Value: `None`

### Result limit

If set to a positive integer, the number of results is limited

- ID: `limit`
- Datatype: `string`
- Default Value: `None`

### Optional SPARQL dataset

An optional SPARQL dataset that can be used for example data, so e.g. the transformation editor shows mapping examples.

- ID: `optionalInputDataset`
- Datatype: `SPARQL endpoint`
- Default Value: `None`

### SPARQL query timeout (ms)

SPARQL query timeout (select/update) in milliseconds. A value of zero means that there is no timeout set explicitly. If a value greater zero is specified this overwrites possible default timeouts.

- ID: `sparqlTimeout`
- Datatype: `int`
- Default Value: `0`

## Advanced Parameter

`None`
