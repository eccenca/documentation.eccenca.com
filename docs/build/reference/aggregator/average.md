---
title: "Average"
description: "Computes the weighted average."
icon: octicons/cross-reference-24
tags: 
---
# Average
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Computes the weighted average.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Computes the arithmetic mean of all similarity scores:**

* Input values: `[0.4, 0.5, 0.9]`
* Returns: `0.6`


---
**Multiplies individual similarity scores with their weight before averaging:**

* Weights: `[1, 1, 2]`
* Input values: `[0.3, 0.5, 0.6]`
* Returns: `0.5`


---
**Missing scores always lead to an output of none:**

* Input values: `[-1.0, null, 1.0]`
* Returns: `null`




## Parameter

`None`

## Advanced Parameter

`None`