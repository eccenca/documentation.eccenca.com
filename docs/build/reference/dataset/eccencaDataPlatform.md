---
title: "Knowledge Graph"
description: "Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Knowledge Graph
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The Knowledge Graph plugin is a dataset for reading and writing RDF to a knowledge graph embedded in Corporate Memory.

## Description

The Knowledge Graph plugin has the technical ID `eccencaDataPlatform`. This ID contains a reference to
[**eccenca Explore**](https://documentation.eccenca.com/latest/explore-and-author/), also known as `DataPlatform`.

Conceptually, the main responsibility of this plugin is to be a **RDF dataset** for reading and writing RDF statements
into or from a **knowledge graph**. This knowledge graph is _embedded_ within eccenca Corporate Memory (CMEM),
specifically within the already mentioned `DataPlatform`, known as **eccenca Explore**.

The plugin itself is part of [**eccenca Build**](https://documentation.eccenca.com/latest/build/)
(internally known as `DataIntegration`). In a nutshell, the relevant difference between Build and Explore is the
following aspect (see the [Getting Started](https://documentation.eccenca.com/latest/getting-started/) and the remaining
documentation for further details):

* **Explore** is for browsing and exploring knowledge graphs
* **Build** is for creating and integrating knowledge graphs

This plugin, i.e. `eccencaDataPlatform`, is thus responsible for _creating_ and _integrating_ knowledge graphs within
eccenca Build. The knowledge graph itself is part of `DataPlatform`, which can be
[explored](https://documentation.eccenca.com/latest/explore-and-author/graph-exploration/) in the UI of eccenca CMEM
under the Explore module.

## Example usage

The usage of this plugin is showcased, for example, in
[these](https://documentation.eccenca.com/latest/build/lift-data-from-tabular-data-such-as-csv-xslx-or-database-tables/#6-build-the-knowledge-graph)
[three](https://documentation.eccenca.com/latest/build/lift-data-from-json-and-xml-sources/#6-build-the-knowledge-graph)
[tutorials](https://documentation.eccenca.com/latest/build/extracting-data-from-a-web-api/#4-create-a-knowledge-graph),
where the knowledge graph is used as a _sink_ dataset. The creation of the knowledge graph is handled implicitly.

Another tutorial showcasing how to _consume_ the knowledge graph, i.e. how to use it as a _source_ of information rather
than as a _sink_, is [this example](https://documentation.eccenca.com/latest/consume/consuming-graphs-with-sql-databases/)
with a SQL database as a source dataset.

## Related plugins

Other types of RDF datasets are the **in-memory dataset** and the **RDF dataset**. These are worth considering if the
information is short-lived or the dataset is small. A more durable and resilient solution is to use an Enterprise
**Knowledge Graph**, which is exactly what this plugin does.

Next to the knowledge graph embedded within eccenca CMEM, there is the possibility to use an external
**SPARQL endpoint**. The _embedded_ knowledge graph of CMEM is an essential component of CMEM as
_semantic data management software_. The additional possibility of integrating with _external_ knowledge graphs via
the SPARQL endpoint is merely a small part of the possibilities to
[consume](https://documentation.eccenca.com/latest/consume/) data within CMEM.

## Parameter

### Graph

The URI of the named graph.

* ID: `graph`
* Datatype: `graph uri`
* Default Value: `None`

### Clear graph before workflow execution

If set to `true`, this will clear the specified graph before executing a workflow that writes to it. Note that this will always use the configured graph and ignore any overwritten values from the config port.

* ID: `clearGraphBeforeExecution`
* Datatype: `boolean`
* Default Value: `false`

### SPARQL query timeout (ms)

SPARQL query timeout in milliseconds. By default, a value of zero is used. This zero value has a symbolic character: it means that the timeout of SPARQL select and update queries is configured via the properties `silk.remoteSparqlEndpoint.defaults.connection.timeout.ms and`silk.remoteSparqlEndpoint.defaults.read.timeout.ms` for the default connection and read timeouts. To overwrite these configured values, specify a (common) timeout greater than zero milliseconds.

* ID: `sparqlTimeout`
* Datatype: `int`
* Default Value: `0`

### Optimized entity retrieval

Optimized retrieval method to remove load from the underlying triple store. Query parallelism is limited and cheaper queries are executed against the backend. By putting the main work on DataIntegration side, the RDF backend is kept responsive.

* ID: `optimizedRetrieve`
* Datatype: `boolean`
* Default Value: `true`

## Advanced Parameter

### Endpoint

The named endpoint within eccenca DataPlatform.

* ID: `endpoint`
* Datatype: `string`
* Default Value: `default`

### Page size

The number of entities to be retrieved per SPARQL query. This is the page size used when paging.

* ID: `pageSize`
* Datatype: `int`
* Default Value: `100000`

### Pause time

The number of milliseconds to wait between subsequent query

* ID: `pauseTime`
* Datatype: `int`
* Default Value: `0`

### Retry count

The number of retries if a query fails

* ID: `retryCount`
* Datatype: `int`
* Default Value: `3`

### Retry pause

The number of milliseconds to wait until a failed query is retried.

* ID: `retryPause`
* Datatype: `int`
* Default Value: `1000`

### Strategy

The strategy for retrieving entities. There are three options: `simple` retrieves all entities using a single query; `subQuery` also uses a single query, which is optimized for Virtuoso; `parallel` executes multiple queries in parallel, one for each entity property.

* ID: `strategy`
* Datatype: `enumeration`
* Default Value: `parallel`

### Entity list

A list of entities to be retrieved. If not given, all entities will be retrieved. Multiple entities are separated by whitespace.

* ID: `entityList`
* Datatype: `multiline string`
* Default Value: `None`
