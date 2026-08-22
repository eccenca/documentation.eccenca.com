---
title: "Select random entities"
description: "Select X random entities from an input dataset."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Select random entities

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task selects X random entities from an input dataset
using the standard pseudo-random generator (reservoir sampling).

The task supports only flat entities. Hierarchical entities are ignored.


## Parameter

### Number of Entities

How many entities should be selected.

- ID: `number_of_entities`
- Datatype: `Long`
- Default Value: `10`

## Advanced Parameter

`None`
