---
title: "Euclidian distance"
description: "Calculates the Euclidian distance."
icon: octicons/cross-reference-24
tags: 
---
# Euclidian distance
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Calculates the Euclidian distance.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Weights: `[1, 1, 1]`
* Input values: `[1.0, 1.0, 1.0]`
* Returns: `1.0`


---
**Example 2:**

* Weights: `[1, 1]`
* Input values: `[1.0, 0.0]`
* Returns: `0.707107`


---
**Example 3:**

* Weights: `[1, 1, 1]`
* Input values: `[0.4, 0.5, 0.6]`
* Returns: `0.506623`


---
**Example 4:**

* Weights: `[1, 1]`
* Input values: `[0.0, 0.0]`
* Returns: `0.0`


---
**Example 5:**

* Weights: `[2, 1, 1]`
* Input values: `[1.0, 0.0, 0.0]`
* Returns: `0.707107`


---
**Example 6:**

* Weights: `[1, 2, 3]`
* Input values: `[0.4, 0.5, 0.6]`
* Returns: `0.538516`


---
**Missing scores always lead to an output of none:**

* Input values: `[-1.0, null, 1.0]`
* Returns: `null`




## Parameter

`None`

## Advanced Parameter

`None`