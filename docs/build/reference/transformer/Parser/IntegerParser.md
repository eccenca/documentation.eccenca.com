---
title: "Parse integer"
description: "Parses integer values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Parse integer

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Parses integer values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * commaAsDecimalPoint: `true`
    * thousandSeparator: `false`

* Input values:
    1. `[1000,00]`

* Returns: `[1000]`

---
**Example 2:**

* Parameters
    * commaAsDecimalPoint: `true`
    * thousandSeparator: `true`

* Input values:
    1. `[1.000,00]`

* Returns: `[1000]`

---
**Example 3:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `false`

* Input values:
    1. `[1000.00]`

* Returns: `[1000]`

---
**Example 4:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `true`

* Input values:
    1. `[1,000.00]`

* Returns: `[1000]`

## Parameter

### Comma as decimal point

Use comma or point (default) as a decimal separator.

* ID: `commaAsDecimalPoint`
* Datatype: `boolean`
* Default Value: `false`

### Thousand separator

Presence of a thousands separator (default: absence), compatible with the chosen decimal separator.

* ID: `thousandSeparator`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`
