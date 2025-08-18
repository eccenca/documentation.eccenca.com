---
title: "Validate Knowledge Graph"
description: "Use SHACL shapes to validate resources in a Knowledge Graph."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Validate Knowledge Graph
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Start a graph validation process which verifies, that resources in a specific graph are valid
according to the node shapes in a shape catalog graph.


## Parameter

### Context Graph

This graph holds the resources you want to validate.

- Datatype: `string`
- Default Value: `None`



### Shape graph

This graph holds the shapes you want to use for validation.

- Datatype: `string`
- Default Value: `https://vocab.eccenca.com/shacl/`



### Result graph

In this graph, the validation results are materialized. If left empty, results are not materialized.

- Datatype: `string`
- Default Value: `None`



### Clear result graph before validation



- Datatype: `boolean`
- Default Value: `false`



### Fail workflow on violations



- Datatype: `boolean`
- Default Value: `false`



### Output violations as entities



- Datatype: `boolean`
- Default Value: `true`



### Resource Selection Query

The query to select the resources to validate. Use {{context_graph}} as a placeholder for the select context graph for validation.

- Datatype: `code-sparql`
- Default Value:
``` sparql
SELECT DISTINCT ?resource
FROM <{{context_graph}}>
WHERE { ?resource a ?class . FILTER isIRI(?resource) }

```



