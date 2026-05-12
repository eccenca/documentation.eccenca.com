---
title: "Remove empty values"
description: "Removes empty values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Remove empty values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes empty values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[value1, , value2]`

* Returns: `[value1, value2]`


---
**Example 2:**

* Input values:
    1. `[, ]`

* Returns: `[]`




## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

* **removeValues** — Remove empty values removes only empty strings and has no parameters. Remove values is the configurable alternative, filtering out values that match words from a user-supplied blacklist.
* **emptyValue** — Empty value produces what Remove empty values removes: an empty sequence. Remove empty values is selective; Empty value is unconditional.
