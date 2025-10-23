---
title: "Geometric mean"
description: "Compute the (weighted) geometric mean."
icon: octicons/cross-reference-24
tags: 
---
# Geometric mean
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Compute the (weighted) geometric mean.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Weights: `[1, 2, 1]`
* Input values: `[0.0, 0.0, 0.0]`
* Returns: `0.0`


---
**Example 2:**

* Weights: `[1, 2, 1]`
* Input values: `[1.0, 1.0, 1.0]`
* Returns: `1.0`


---
**Example 3:**

* Weights: `[2, 1]`
* Input values: `[0.5, 1.0]`
* Returns: `0.629961`


---
**Example 4:**

* Weights: `[2, 1, 5]`
* Input values: `[0.5, 1.0, 0.7]`
* Returns: `0.672866`


---
**Example 5:**

* Weights: `[10, 2, 3]`
* Input values: `[0.1, 0.9, 0.2]`
* Returns: `0.153971`


---
**Missing scores always lead to an output of none:**

* Input values: `[-1.0, null, 1.0]`
* Returns: `null`




## Parameter

`None`

## Advanced Parameter

`None`