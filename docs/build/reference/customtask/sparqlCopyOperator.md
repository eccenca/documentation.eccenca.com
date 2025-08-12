---
title: "SPARQL Construct query"
description: "A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# SPARQL Construct query
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable.


## Parameter

### Construct query

A SPARQL 1.1 construct query

- Datatype: `code-sparql`
- Default Value: `None`



### Use temporary file

When copying directly to the same SPARQL Endpoint or when copying large amounts of triples, set to True by default

- Datatype: `boolean`
- Default Value: `true`



