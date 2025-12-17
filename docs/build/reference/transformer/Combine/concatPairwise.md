---
title: "Concatenate pairwise"
description: "Concatenates the values of multiple inputs pairwise."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Concatenate pairwise

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Concatenates the values of multiple inputs pairwise.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Values of two inputs are concatenated pairwise:**

* Input values:
    1. `[a, b, c]`
    2. `[1, 2, 3]`

* Returns: `[a1, b2, c3]`

---
**More than two inputs are supported as well:**

* Input values:
    1. `[a, b, c]`
    2. `[1, 2, 3]`
    3. `[x, y, z]`

* Returns: `[a1x, b2y, c3z]`

---
**If one of the inputs has more values than the other, its remaining values are ignored:**

* Input values:
    1. `[a, b, c]`
    2. `[1, 2]`

* Returns: `[a1, b2]`

---
**Empty input leads to empty output:**

* Returns: `[]`

---
**A single input is just forwarded:**

* Input values:
    1. `[a]`

* Returns: `[a]`

## Parameter

### Glue

Separator to be inserted between two concatenated strings. The text can contain escaped characters \n, \t and \\ that are replaced by a newline, tab or backslash respectively.

* ID: `glue`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`
