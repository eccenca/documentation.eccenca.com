---
title: "Strip postfix"
description: "Strips a postfix of a string."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Strip postfix

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Strips a postfix of a string.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * postfix: `Postfix`

* Input values:
    1. `[valuePostfix]`

* Returns: `[value]`


---
**Example 2:**

* Parameters
    * postfix: `Postfix`

* Input values:
    1. `[Value]`

* Returns: `[Value]`




## Parameter

### Postfix

No description

* ID: `postfix`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

* **stripPrefix** — Strip postfix removes from the end; Strip prefix removes from the start. Both leave the value unchanged when the configured string is not found at the expected position.
* **substring** — Strip postfix checks for a specific string at the end before removing it. Substring does not check content: a negative end index removes a fixed character count from the end unconditionally.
