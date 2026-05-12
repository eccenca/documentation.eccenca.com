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

* ID: `map`
* Datatype: `stringmap`
* Default Value: `None`



### Default

Default if the map defines no value

* ID: `default`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

* **mapWithDefaultInput** — The Map plugin returns a fixed default string — set as a parameter — for any value not found in the map. Map with default replaces that fixed fallback with a second connected input, so the fallback can differ per value.
* **replace** — The Map plugin matches the entire input value against a lookup table and substitutes the whole value on an exact match. Replace substitutes a search string wherever it appears within the value, without requiring the full value to match.
