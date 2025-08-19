---
title: "Numeric operation"
description: "Applies a numeric operation to the values of multiple input operators. Uses double-precision floating-point numbers for computation."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Numeric operation
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Applies a numeric operation to the values of multiple input operators. Uses double-precision floating-point numbers for computation.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1]`
    2. `[1]`

* Returns: `[2.0]`


---
**Example 2:**

* Parameters
    * operator: `-`

* Input values:
    1. `[1]`
    2. `[1]`

* Returns: `[0.0]`


---
**Example 3:**

* Parameters
    * operator: `*`

* Input values:
    1. `[5]`
    2. `[6]`

* Returns: `[30.0]`


---
**Example 4:**

* Parameters
    * operator: `/`

* Input values:
    1. `[5]`
    2. `[2]`

* Returns: `[2.5]`


---
**Example 5:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1]`
    2. `[no number]`

* Returns: `[]`


---
**Example 6:**

* Parameters
    * operator: `*`

* Input values:
    1. `[1]`
    2. `[]`

* Returns: `[1.0]`


---
**Example 7:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1, 1]`
    2. `[1]`

* Returns: `[3.0]`




## Parameter

### Operator

The operator to be applied to all values. One of '+', '-', '*', '/'

- ID: `operator`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`