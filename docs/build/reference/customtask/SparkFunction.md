---
title: "Execute Spark function"
description: "Applies a specified Scala function to a specified field."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Execute Spark function

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Applies a specified Scala function to a specified field.
Example: Let the input field be `"name"`, the inputFunction `"""any => "Arrrrgh!"""`, and the alias `xxx`.
In this example, a Spark query corresponding to `SELECT existingField1, existingField2, ... "Arrrrgh!" as "xxx"` will be generated.
If the `alias` parameter is empty, the input field will be overwritten.
Otherwise, a new field will be added and the rest of the schema stays the same.

## Parameter

### Function

Scala function expression.

- ID: `function`
- Datatype: `multiline string`
- Default Value: `None`

### Input field

Input field.

- ID: `inputField`
- Datatype: `string`
- Default Value: `None`

### Alias

Alias.

- ID: `alias`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
