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


Starts a graph validation process which verifies that resources in a specific graph are valid
according to the node shapes in a shape catalog graph. The task waits for the validation to
finish before completing.

The task has no input port. Violations found during validation are always summarized in the
workflow report, and can also be materialized into a result graph in the project. Sending each
violation as an entity to an output port is optional; when that is disabled, the task has no
output port either.

## Error Handling

Every resource is validated regardless of the outcome. The task can then either:

- Fail once validation completes if any resource has violations, halting the workflow.
- Report violations only as warnings, allowing follow-up tasks to run based on the results.

The error handling behavior is configurable through the **Fail workflow on violations**
parameter.


## Parameter

### Context Graph

This graph holds the resources you want to validate.

- ID: `context_graph`
- Datatype: `scheme:string`
- Default Value: `None`



### Shape graph

This graph holds the shapes you want to use for validation.

- ID: `shape_graph`
- Datatype: `scheme:string`
- Default Value: `https://vocab.eccenca.com/shacl/`



### Result graph

In this graph, the validation results are materialized. If left empty, results are not materialized.

- ID: `result_graph`
- Datatype: `scheme:string`
- Default Value: `None`



### Clear result graph before validation

If enabled, the existing content of the result graph is deleted before validation starts. Has no effect when Result graph is left empty.

- ID: `clear_result_graph`
- Datatype: `boolean`
- Default Value: `false`



### Fail workflow on violations

If enabled, the workflow fails once validation completes if any resource has violations. All resources are validated either way; disabling this instead reports the violations as warnings.

- ID: `fail_on_violations`
- Datatype: `boolean`
- Default Value: `false`



### Output violations as entities

If enabled, each violation is sent as an entity to an output port for further processing in the workflow. Disabling this removes the output port.

- ID: `output_results`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

### Resource Selection Query

The query to select the resources to validate. Use `{{context_graph}}` as a placeholder for the selected Context Graph.

- ID: `sparql_query`
- Datatype: `code-sparql`
- Default Value:

``` sparql
SELECT DISTINCT ?resource
FROM <{{context_graph}}>
WHERE { ?resource a ?class . FILTER isIRI(?resource) }

```
