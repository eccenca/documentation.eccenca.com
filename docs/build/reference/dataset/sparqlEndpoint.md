---
title: "SPARQL endpoint"
description: "Connects to an existing SPARQL endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# SPARQL endpoint
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The SPARQL endpoint plugin is a dataset for connecting to an existing, remote SPARQL endpoint.

## Description

The `sparqlEndpoint` plugin is an example of a _RDF dataset_. A **dataset** is a collection of data to be read from or
written into, both a _source_ and a _sink_ of information. A **RDF dataset** is a dataset that can deal with RDF data.
There are _several_ plugins for dealing with RDF datasets in the BUILD stage, depending on where the RDF dataset is
located and how it is being accessed. In this case, the `sparqlEndpoint` dataset is a plugin that can access a _remote_
SPARQL endpoint such as one of those [listed by the W3C](https://www.w3.org/wiki/SparqlEndpoints), e.g. Wikidata or
DBpedia.

The **SPARQL dataset** (this plugin) is an instance of a **RDF dataset**. All RDF datasets provide the abstraction and
functionality of a **SPARQL endpoint**. The SPARQL endpoint used in this plugin is a **remote** SPARQL endpoint. It can
handle and execute SPARQL [SELECT](https://www.w3.org/TR/rdf-sparql-query/#select),
[ASK](https://www.w3.org/TR/rdf-sparql-query/#ask) and [CONSTRUCT](https://www.w3.org/TR/rdf-sparql-query/#construct)
queries. Additionally, it can execute [updates](https://www.w3.org/TR/2013/REC-sparql11-update-20130321/#updateLanguage).

## Example usage

A very simple example showcasing the usage of this plugin is the following idea: Use an online SPARQL Query Editor such
as <https://dbpedia.org/sparql>, with a simple SPARQL query like `select distinct ?Concept where {[] a ?Concept} LIMIT 10`
or similar. Use this plugin as a **source** dataset, and transform or transfer the SPARQL query results into a sink
dataset such as a **CSV file**. A similar or related showcase example involves considering other output datasets such as
an **in-memory dataset** or a **Knowledge Graph** such as the one handled by the `eccencaDataPlatform` plugin, which is
the flagship RDF dataset of
[Corporate Memory](https://eccenca.com/products/enterprise-knowledge-graph-platform-corporate-memory).

## Related plugins

Other types of RDF datasets are the **in-memory dataset**, the **RDF dataset**. These are worth considering if the
information is short-lived or the dataset is small. A more durable and resilient solution is to use a proper
**Knowledge Graph**.

The SPARQL dataset plugin can be used in conjunction with the **task** plugins for SPARQL `SELECT` and `CONSTRUCT`
queries, i.e. the plugins `sparqlSelectOperator` and `sparqlCopyOperator`.

## Parameter

### Endpoint URI

The URI of the SPARQL endpoint, e.g. `http://dbpedia.org/sparql`

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

The URI of a named graph. If set, the SPARQL endpoint will only retrieve entities from that specific graph.

- ID: `graph`
- Datatype: `string`
- Default Value: `None`

### Strategy

The strategy for retrieving entities. There are three options: `simple` retrieves all entities using a single query; `subQuery` also uses a single query, which is optimized for Virtuoso; `parallel` executes multiple queries in parallel, one for each entity property.

- ID: `strategy`
- Datatype: `enumeration`
- Default Value: `parallel`

### Use order by

Enforces the correct ordering of values, if set to `true` (default).

- ID: `useOrderBy`
- Datatype: `boolean`
- Default Value: `true`

### Clear graph before workflow execution

If set to `true`, this will clear the specified graph before executing a workflow that writes into it.

- ID: `clearGraphBeforeExecution`
- Datatype: `boolean`
- Default Value: `false`

### SPARQL query timeout (ms)

SPARQL query timeout in milliseconds. By default, a value of zero is used. This zero value has a symbolic character: it means that the timeout of SPARQL select and update queries is configured via the properties `silk.remoteSparqlEndpoint.defaults.connection.timeout.ms and`silk.remoteSparqlEndpoint.defaults.read.timeout.ms` for the default connection and read timeouts. To overwrite these configured values, specify a (common) timeout greater than zero milliseconds.

- ID: `sparqlTimeout`
- Datatype: `int`
- Default Value: `0`

## Advanced Parameter

### Page size

The number of entities to be retrieved per SPARQL query. This is the page size used when paging.

- ID: `pageSize`
- Datatype: `int`
- Default Value: `1000`

### Entity list

An optional list of entities to be retrieved. If not specified, all entities will be retrieved. Multiple entities need to be separated by whitespace.

- ID: `entityList`
- Datatype: `multiline string`
- Default Value: `None`

### Pause time

The number of milliseconds to wait between subsequent queries

- ID: `pauseTime`
- Datatype: `int`
- Default Value: `0`

### Retry count

The total number of retries to execute a (repeatedly) failing query

- ID: `retryCount`
- Datatype: `int`
- Default Value: `3`

### Retry pause

The number of milliseconds to wait until a previously failed query is executed again

- ID: `retryPause`
- Datatype: `int`
- Default Value: `1000`

### Query parameters

Additional parameters to be appended to every query, e.g. `&soft-limit=1`

- ID: `queryParameters`
- Datatype: `string`
- Default Value: `None`
