---
title: "SPARQL Update query"
description: "A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# SPARQL Update query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The SPARQL UPDATE query plugin is a task for outputting SPARQL UPDATE queries from the input RDF data source.

## Description

The `sparqlUpdateOperator` plugin is an example of a _task_. Notice well that this plugin is **neither** a _RDF task_
nor a _RDF dataset_. This is in contrast to e.g. the `sparqlSelectOperator` and the `sparqlEndpoint`, respectively.

More specifically, this means the following: This plugin does not execute SPARQL queries of any sort, but _generates_
them. It generates [SPARQL Update](https://www.w3.org/TR/sparql11-update/) queries from a templating engine. In order to
_execute_ these queries, we need to connect this task from an input into an output RDF dataset.

## Templating

The `sparqlUpdateOperator` plugin uses a **template** in order to construct and output SPARQL update queries.
There are two possible template engines supported by this plugin: a `Simple` engine and
[`Velocity Engine`](https://velocity.apache.org/engine/2.4.1/user-guide.html).
Each of these engines supports a different set of templating features, such as for example _variable interpolation_ with
the dollar sign (`$`), i.e. filling in input values via placeholders in the template.

### Example of the `Simple` mode

```text
  DELETE DATA { ${<PROP_FROM_ENTITY_SCHEMA1>} rdf:label ${"PROP_FROM_ENTITY_SCHEMA2"} }
  INSERT DATA { ${<PROP_FROM_ENTITY_SCHEMA1>} rdf:label ${"PROP_FROM_ENTITY_SCHEMA3"} }
```

This will insert the URI serialization of the property value `PROP_FROM_ENTITY_SCHEMA1` for the
`${<PROP_FROM_ENTITY_SCHEMA1>}` expression.
Furthermore, it will insert a plain literal serialization for the property values `PROP_FROM_ENTITY_SCHEMA2` and
`PROP_FROM_ENTITY_SCHEMA3` for the template literal expressions.

It is also possible to write something like `${"PROP"}^^<http://someDatatype>`  or `${"PROP"}@en`. In other words, we
can combine variable substitutions with fixed expressions to construct semi-flexible expressions within the template.

### Example of the `Velocity Engine` mode

```text
  DELETE DATA { $row.uri("PROP_FROM_ENTITY_SCHEMA1") rdf:label $row.plainLiteral("PROP_FROM_ENTITY_SCHEMA2") }
  #if ( $row.exists("PROP_FROM_ENTITY_SCHEMA1") )
    INSERT DATA { $row.uri("PROP_FROM_ENTITY_SCHEMA1") rdf:label $row.plainLiteral("PROP_FROM_ENTITY_SCHEMA3") }
  #end
```

Input values are accessible via various methods of the `row` variable (used with `$row`):

- `$row.uri(inputPath: String)`: Renders an input value as **URI**. Throws an exception if the value isn't a valid URI.
- `$row.plainLiteral(inputPath: String)`: Renders an input value as **plain literal**, i.e. it escapes problematic characters, etc.
- `$row.rawUnsafe(inputPath: String)`: Renders an input value as is, i.e. **no escaping** is done. This should **only** be used if the input values can be trusted.
- `$row.exists(inputPath: String)`: Returns `true` if a value for the input path **exists**, else `false`.

The methods `uri`, `plainLiteral` and `rawUnsafe` throw an exception if no input value is available for the given input path.

In addition to input values, properties of the input and output tasks can be accessed via the `inputProperties` and
`outputProperties` objects in the same way as the `row` object. For example with `$inputProperties.uri("graph")`.

For more information about the Velocity Engine, visit <http://velocity.apache.org>.

### Internal Specifics

In contrast to the SPARQL select operator, no `FROM` clause gets injected into the query.

## Related plugins

As mentioned, this plugin is neither a RDF task nor a RDF dataset. Those two categories of plugins are, nevertheless,
related. Specifically, the RDF dataset plugins such as the `sparqlEndpoint` can be used as data input. Similarly,
possible output datasets could be an **in-memory dataset** or a **Knowledge Graph** such as the one handled by the
`eccencaDataPlatform` plugin, which is the flagship RDF dataset of
[Corporate Memory](https://eccenca.com/products/enterprise-knowledge-graph-platform-corporate-memory).

## Parameter

### SPARQL update query

The SPARQL UPDATE template for constructing SPARQL UPDATE queries for every entity from the input. The possible values for the template engine are `Simple` and `Velocity Engine`. See the general documentation of this plugin for further details on the features of each template engine.

- ID: `sparqlUpdateTemplate`
- Datatype: `code-sparql`
- Default Value: `None`

### Batch size

How many entities should be handled in a single update request.

- ID: `batchSize`
- Datatype: `int`
- Default Value: `1`

### Templating mode

The templating mode for the template engine. The possible values are `Simple` and `Velocity Engine`. See the general documentation of this plugin for further details on the features of each template engine.

- ID: `templatingMode`
- Datatype: `enumeration`
- Default Value: `simple`

## Advanced Parameter

`None`
