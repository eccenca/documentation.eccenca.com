---
title: "Knowledge Graph"
description: "Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Knowledge Graph
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory.

## Parameter

### Endpoint

The named endpoint within the eccenca DataPlatform.

- Datatype: `string`
- Default Value: `default`



### Graph

The URI of the named graph.

- Datatype: `graph uri`
- Default Value: `None`



### Page size

The number of solutions to be retrieved per SPARQL query.

- Datatype: `int`
- Default Value: `100000`



### Pause time

The number of milliseconds to wait between subsequent query

- Datatype: `int`
- Default Value: `0`



### Retry count

The number of retries if a query fails

- Datatype: `int`
- Default Value: `3`



### Retry pause

The number of milliseconds to wait until a failed query is retried.

- Datatype: `int`
- Default Value: `1000`



### Strategy

The strategy use for retrieving entities: simple: Retrieve all entities using a single query; subQuery: Use a single query, but wrap it for improving the performance on Virtuoso; parallel: Use a separate Query for each entity property.

- Datatype: `enumeration`
- Default Value: `parallel`



### Clear graph before workflow execution

If set to true this will clear the specified graph before executing a workflow that writes to it. Note that this will always use the configured graph and ignore any overwritten values from the config port.

- Datatype: `boolean`
- Default Value: `false`



### Entity list

A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace.

- Datatype: `multiline string`
- Default Value: `None`



### SPARQL query timeout (ms)

SPARQL query timeout (select/update) in milliseconds. A value of zero means that there is no timeout. If a value greater zero is specified this overwrites possible default timeouts. This timeout is also propagated to DataPlatform and may overwrite default timeouts there.

- Datatype: `int`
- Default Value: `0`



### Optimized entity retrieval

Optimized retrieval method to remove load from the underlying triple store. Query parallelism is limited and cheaper queries are executed against the backend. By putting the main work on DataIntegration side, the RDF backend is kept responsive.

- Datatype: `boolean`
- Default Value: `true`



