---
title: "Distinct by"
description: "Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities. Since this operator accepts a flexible input schema, it can only be connected to operators that provide a non-flexible output schema. A typical way to achieve this is to place a transform operator before it, which produces a fixed output schema."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Distinct by
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities.

Since this operator accepts a flexible input schema, it can only be connected to operators that provide a non-flexible output schema.
A typical way to achieve this is to place a transform operator before it, which produces a fixed output schema.


## Parameter

### Distinct path

Entities that share this path will be deduplicated.

- ID: `distinctPath`
- Datatype: `string`
- Default Value: `None`



### Resolve duplicates

Strategy to resolve duplicates.

- ID: `resolveDuplicates`
- Datatype: `enumeration`
- Default Value: `keepLast`





## Advanced Parameter

`None`