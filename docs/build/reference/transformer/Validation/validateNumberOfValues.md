---
title: "Validate number of values"
description: "Validates that the number of values lies in a specified range."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Validate number of values
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Validates that the number of values lies in a specified range.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * min: `0`
    * max: `1`

* Input values:
    1. `[value1]`

* Returns: `[value1]`


---
**Example 2:**

* Parameters
    * min: `0`
    * max: `1`

* Input values:
    1. `[value1, value2]`

* Returns: `[]`
* **Throws error:** `ValidationException`




## Parameter

### Min

Minimum allowed number of values

- ID: `min`
- Datatype: `int`
- Default Value: `0`



### Max

Maximum allowed number of values

- ID: `max`
- Datatype: `int`
- Default Value: `1`





## Advanced Parameter

`None`