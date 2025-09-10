---
title: "Map"
description: "Replaces values based on a map of values."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Map
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Replaces values based on a map of values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * map: `Key1:Value1,Key2:Value2`
    * default: `Undefined`

* Input values:
    1. `[Key1]`

* Returns: `[Value1]`


---
**Example 2:**

* Parameters
    * map: `Key1:Value1,Key2:Value2`
    * default: `Undefined`

* Input values:
    1. `[Key1X]`

* Returns: `[Undefined]`




## Parameter

### Map

A map of values

- ID: `map`
- Datatype: `stringmap`
- Default Value: `None`



### Default

Default if the map defines no value

- ID: `default`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`