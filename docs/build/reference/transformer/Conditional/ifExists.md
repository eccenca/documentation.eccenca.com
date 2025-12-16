---
title: "If exists"
description: "Accepts two or three inputs. If the first input provides a value, the second input is forwarded. Otherwise, the third input is forwarded (if present)."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# If exists
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Accepts two or three inputs. If the first input provides a value, the second input is forwarded. Otherwise, the third input is forwarded (if present).

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[value]`
    2. `[yes]`
    3. `[no]`

* Returns: `[yes]`

---
**Example 2:**

* Input values:
    1. `[]`
    2. `[yes]`
    3. `[no]`

* Returns: `[no]`

---
**Example 3:**

* Input values:
    1. `[value]`
    2. `[]`

* Returns: `[]`

## Parameter

`None`

## Advanced Parameter

`None`
