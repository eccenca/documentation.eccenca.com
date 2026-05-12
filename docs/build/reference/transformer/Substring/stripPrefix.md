---
title: "Strip prefix"
description: "Strips a prefix of a string."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Strip prefix

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Strips a prefix of a string.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * prefix: `prefix`

* Input values:
    1. `[prefixValue]`

* Returns: `[Value]`


---
**Example 2:**

* Parameters
    * prefix: `prefix`

* Input values:
    1. `[ValueWithoutPrefix]`

* Returns: `[ValueWithoutPrefix]`




## Parameter

### Prefix

No description

* ID: `prefix`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

* **stripPostfix** — Strip prefix removes a configured string from the start of the value, leaving it unchanged if the string is not found there. Strip postfix is the complement: it checks and removes from the end.
* **substring** — Strip prefix removes a configured string from the start only if it is actually present. Substring removes by position: it skips the first N characters regardless of their content, so it will cut into the value even if the expected prefix is absent.
