---
title: "Numeric operation"
description: "Applies one of the four basic arithmetic operators to the sequence of input values."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Numeric operation
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The `numOperation` plugin applies one of the four basic arithmetic operators to the sequence of input values.
These are the fundamental operations of **addition** (`+`), **subtraction** (`-`), **multiplication** (`*`)
and **division** (`/`).

Notice that the symbol `÷` can't be used for the 'division' operator, and remember that one
should never divide by null. Doing so will result in `Infinity`.

The computations are done with
[double-precision floating-point numbers](https://en.wikipedia.org/wiki/Double-precision_floating-point_format).
This means that e.g. integers such as `1` or `2` will be converted to `1.0` and `2.0`.
This also regards the _output_ of the operation, as in `1 + 1` leading to `2.0` rather than the integer `2`.

_**Only** the four basic arithmetic operations are allowed_ (and understood) by this numeric transformer plugin. If an
_invalid operation_ is given, an error or exception will occur. In the same manner, if the _values_ aren't (valid)
numbers, a validation exception will be raised.

## Examples

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


---
**Example 8:**

* Parameters
    * operator: `/`

* Input values:
    1. `[1]`
    2. `[0]`

* Returns: `[Infinity]`




## Parameter

### Operator

The operator to be applied to all values. One of `+`, `-`, `*`, `/`

- ID: `operator`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`