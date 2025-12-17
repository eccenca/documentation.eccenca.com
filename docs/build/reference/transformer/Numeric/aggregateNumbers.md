---
title: "Aggregate numbers"
description: "Applies one of the aggregation operators (`+`, `*`, `min`, `max` or `average`) to the sequence of input values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Aggregate numbers

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The `aggregateNumbers` plugin applies an aggregation operator to the sequence of input values.
The allowed aggregation operators are **sum** (`+`), **product** (`*`), **minimum** (`min`), **maximum** (`max`)
and **average** (`average`).

Notice that the "number" `Infinity` is allowed as input and to be expected as possible output. For example, the
_minimum_ of `1` and `Infinity` is `1`, but its _maximum_, its _sum_, its _product_ and its _average_ are `Infinity`.

The **aggregation operations** of this plugin are exclusively _numerical_. They are exactly the expected operations upon
a list or sequence of numbers, in order to 'aggregate', 'reduce', 'sum' or
'[join](https://en.wikipedia.org/wiki/Fold_(higher-order_function))' them.

The computations are done with
[double-precision floating-point numbers](https://en.wikipedia.org/wiki/Double-precision_floating-point_format).
This means that e.g. integers such as `1` or `2` will be converted to `1.0` and `2.0`.
This also regards the _output_ of the operation, as in `1 + 1` leading to `2.0` rather than the integer `2`.

_**Only** the five listed aggregation operations are allowed_ (and understood) by this numeric transformer plugin. If an
_invalid operation_ is given, an error or exception will occur. On the other hand, if any _values_ aren't (valid)
numbers, they will be ignored.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1, 1, 1]`

* Returns: `[3.0]`

---
**Example 2:**

* Parameters
    * operator: `*`

* Input values:
    1. `[2, 2, 2]`

* Returns: `[8.0]`

---
**Example 3:**

* Parameters
    * operator: `min`

* Input values:
    1. `[1, 2, 3]`

* Returns: `[1.0]`

---
**Example 4:**

* Parameters
    * operator: `max`

* Input values:
    1. `[1, 2, 3]`

* Returns: `[3.0]`

---
**Example 5:**

* Parameters
    * operator: `average`

* Input values:
    1. `[1, 2, 3]`

* Returns: `[2.0]`

---
**Example 6:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1.0, Infinity]`

* Returns: `[Infinity]`

---
**Example 7:**

* Parameters
    * operator: `*`

* Input values:
    1. `[1.0, Infinity]`

* Returns: `[Infinity]`

---
**Example 8:**

* Parameters
    * operator: `min`

* Input values:
    1. `[1.0, Infinity]`

* Returns: `[1.0]`

---
**Example 9:**

* Parameters
    * operator: `max`

* Input values:
    1. `[1.0, Infinity]`

* Returns: `[Infinity]`

---
**Example 10:**

* Parameters
    * operator: `average`

* Input values:
    1. `[1.0, Infinity]`

* Returns: `[Infinity]`

---
**Example 11:**

* Parameters
    * operator: `+`

* Input values:
    1. `[1, Whatever]`

* Returns: `[1.0]`

---
**Example 12:**

* Parameters
    * operator: `*`

* Input values:
    1. `[1.0, Whatever]`

* Returns: `[1.0]`

---
**Example 13:**

* Parameters
    * operator: `min`

* Input values:
    1. `[1.0, Whatever]`

* Returns: `[1.0]`

---
**Example 14:**

* Parameters
    * operator: `max`

* Input values:
    1. `[1.0, Whatever]`

* Returns: `[1.0]`

---
**Example 15:**

* Parameters
    * operator: `average`

* Input values:
    1. `[1.0, Whatever]`

* Returns: `[1.0]`

---
**Example 16:**

* Parameters
    * operator: `notAnOperator`

* Input values:
    1. `[1.0, 2.0, 3.0]`

* Returns: `[]`

## Parameter

### Operator

The aggregation operation to be applied to all values. One of `+`, `*`, `min`, `max`, `average`.

* ID: `operator`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`
