---
title: "Contains any of"
description: "Accepts two inputs. If the first input contains any of the second input values it returns 'true', else 'false' is returned."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Contains any of
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Accepts two inputs. If the first input contains any of the second input values it returns 'true', else 'false' is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[A, B, C]`
    2. `[A, B]`

* Returns: `[true]`


---
**Example 2:**

* Input values:
    1. `[A, B, C]`
    2. `[A, D]`

* Returns: `[true]`


---
**Example 3:**

* Input values:
    1. `[A, B, C]`
    2. `[D]`

* Returns: `[false]`


---
**Example 4:**

* Input values:
    1. `[A, B, C]`
    2. `[A, B, C]`

* Returns: `[true]`


---
**Example 5:**

* Input values:
    1. `[A, B, C]`
    2. `[]`

* Returns: `[]`
* **Throws error:** `IllegalArgumentException`


---
**Example 6:**

* Input values:
    1. `[A]`
    2. `[A]`
    3. `[A]`

* Returns: `[]`
* **Throws error:** `IllegalArgumentException`


---
**Example 7:**

* Input values:
    1. `[A]`

* Returns: `[]`
* **Throws error:** `IllegalArgumentException`




## Parameter

`None`

## Advanced Parameter

`None`