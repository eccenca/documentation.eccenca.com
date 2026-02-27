---
title: "And"
description: "All input scores must be within the threshold. Selects the minimum score."
icon: octicons/cross-reference-24
tags:
---

# And

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

All input scores must be within the threshold. Selects the minimum score.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Selects the minimum similarity score:**

* Input values: `[1.0, 0.0]`
* Returns: `0.0`

---
**Selects the minimum similarity score:**

* Input values: `[-1.0, 0.0, 0.5, 1.0]`
* Returns: `-1.0`

---
**Missing scores default to a similarity score of -1:**

* Input values: `[1.0, null, -0.5]`
* Returns: `-1.0`

---
**Weights are ignored:**

* Weights: `[1000, 0]`
* Input values: `[1.0, 0.0]`
* Returns: `0.0`

## Parameter

`None`

## Advanced Parameter

`None`
