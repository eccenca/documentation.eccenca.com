---
title: "SPARQL Construct query"
description: "A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# SPARQL Construct query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The SPARQL Construct query operator runs a [SPARQL 1.1 CONSTRUCT query](https://www.w3.org/TR/sparql11-query/#construct)
against a connected RDF dataset and passes the resulting RDF statements to the next workflow task.
Connect an RDF dataset as its input and an RDF output dataset as its output to write the result.
The operator itself does not write to a dataset.

## Construct query

<a id="parameter_doc_query"></a>
The **Construct query** parameter defines which RDF statements to produce. For example, this query copies names
from the source dataset into a different property in the output:

```sparql
PREFIX ex: <http://example.org/>

CONSTRUCT { ?person ex:displayName ?name }
WHERE { ?person ex:name ?name }
```

The query must be a valid CONSTRUCT query; other query forms such as SELECT and UPDATE are rejected when the task is
configured. The query is executed as written, without template variable substitution. Include any required `PREFIX`
declarations in the query.

The source dataset's **Graph** setting is not automatically added to this CONSTRUCT query. To read a particular named
graph, specify it in the query, for example:

```sparql
CONSTRUCT { ?s ?p ?o }
WHERE { GRAPH <http://example.org/source-graph> { ?s ?p ?o } }
```

Configure the destination graph on the connected output dataset if the result should be written to a named graph.

## Use temporary file

<a id="parameter_doc_tempFile"></a>
**Use temporary file** is enabled by default. The operator saves the complete CONSTRUCT result to a temporary file
before passing it to the output. This avoids reading from a store while the downstream task writes the result back
to that same store. It requires enough temporary disk space for the result; the file is removed after execution.

Disable this option to pass the result to the output without first saving it to a temporary file. This avoids the
intermediate file, but reading and writing may then overlap. The option controls this operator's intermediate file,
not how the source endpoint processes the query internally.

If the intention is to change data within the same RDF store, consider the **SPARQL Update query** operator instead.


## Parameter

### Construct query

A SPARQL 1.1 construct query

- ID: `query`
- Datatype: `code-sparql`
- Default Value: `None`



### Use temporary file

Save the complete CONSTRUCT result to a temporary file before passing it to the output. Useful when reading from and writing to the same store. Enabled by default.

- ID: `tempFile`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

`None`
