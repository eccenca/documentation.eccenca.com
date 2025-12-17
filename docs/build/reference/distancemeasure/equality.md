---
title: "String equality"
description: "Checks for equality of the string representation of the given values. Returns success if string values are equal, failure otherwise. For a numeric comparison of values use the 'Numeric Equality' comparator."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# String equality

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Checks for equality of the string representation of the given values. Returns success if string values are equal, failure otherwise. For a numeric comparison of values use the 'Numeric Equality' comparator.

## Characteristics

This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns distance 0, if at least one value matches:**

* Input values:
    * Source: `[max, helmut]`
    * Target: `[max]`

* Returns: `0.0`

---
**Returns distance 1, if no value matches:**

* Input values:
    * Source: `[max, helmut]`
    * Target: `[john]`

* Returns: `1.0`

## Parameter

`None`

## Advanced Parameter

`None`
