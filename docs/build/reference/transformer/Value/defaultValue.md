---
title: "Default Value"
description: "Generates a default value, if the input values are empty. Forwards any non-empty values."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Default Value
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Generates a default value, if the input values are empty. Forwards any non-empty values.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Forwards input values:**

* Input values:
    1. `[input value]`

* Returns: `[input value]`


---
**Outputs the default value, if the inputs are empty:**

* Parameters
    * value: `default value`

* Input values:
    1. `[]`

* Returns: `[default value]`




## Parameter

### Value

The default value to be generated, if input values are empty

- ID: `value`
- Datatype: `string`
- Default Value: `default`





## Advanced Parameter

`None`