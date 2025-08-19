---
title: "SPARQL endpoint"
description: "Connect to an existing SPARQL endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# SPARQL endpoint
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Connect to an existing SPARQL endpoint.


## Parameter

### Endpoint URI

The URI of the SPARQL endpoint, e.g., http://dbpedia.org/sparql

- ID: `endpointURI`
- Datatype: `string`
- Default Value: `None`



### Login

Login required for authentication

- ID: `login`
- Datatype: `string`
- Default Value: `None`



### Password

Password required for authentication

- ID: `password`
- Datatype: `password`
- Default Value: `None`



### Graph

Only retrieve entities from a specific graph

- ID: `graph`
- Datatype: `string`
- Default Value: `None`



### Strategy

The strategy use for retrieving entities: simple: Retrieve all entities using a single query; subQuery: Use a single query, but wrap it for improving the performance on Virtuoso; parallel: Use a separate Query for each entity property.

- ID: `strategy`
- Datatype: `enumeration`
- Default Value: `parallel`



### Use order by

Include useOrderBy in queries to enforce correct order of values.

- ID: `useOrderBy`
- Datatype: `boolean`
- Default Value: `true`



### Clear graph before workflow execution

If set to true this will clear the specified graph before executing a workflow that writes to it.

- ID: `clearGraphBeforeExecution`
- Datatype: `boolean`
- Default Value: `false`



### SPARQL query timeout (ms)

SPARQL query timeout (select/update) in milliseconds. A value of zero means that the timeout configured via property is used (e.g. configured via silk.remoteSparqlEndpoint.defaults.read.timeout.ms). To overwrite the configured value specify a value greater than zero.

- ID: `sparqlTimeout`
- Datatype: `int`
- Default Value: `0`





## Advanced Parameter

### Page size

The number of solutions to be retrieved per SPARQL query.

- ID: `pageSize`
- Datatype: `int`
- Default Value: `1000`



### Entity list

A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace.

- ID: `entityList`
- Datatype: `multiline string`
- Default Value: `None`



### Pause time

The number of milliseconds to wait between subsequent query

- ID: `pauseTime`
- Datatype: `int`
- Default Value: `0`



### Retry count

The number of retries if a query fails

- ID: `retryCount`
- Datatype: `int`
- Default Value: `3`



### Retry pause

The number of milliseconds to wait until a failed query is retried.

- ID: `retryPause`
- Datatype: `int`
- Default Value: `1000`



### Query parameters

Additional parameters to be appended to every request e.g. &soft-limit=1

- ID: `queryParameters`
- Datatype: `string`
- Default Value: `None`



