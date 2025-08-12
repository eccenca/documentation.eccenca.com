---
title: "Distinct by"
description: "Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Distinct by
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities.


## Parameter

### Distinct path

Entities that share this path will be deduplicated.

- Datatype: `string`
- Default Value: `None`



### Resolve duplicates

Strategy to resolve duplicates.

- Datatype: `enumeration`
- Default Value: `keepLast`



