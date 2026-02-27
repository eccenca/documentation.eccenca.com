---
title: "Date to timestamp"
description: "Convert an xsd:dateTime to a timestamp. Returns the passed time since the Unix Epoch (1970-01-01)."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Date to timestamp

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Convert an xsd:dateTime to a timestamp. Returns the passed time since the Unix Epoch (1970-01-01).

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[2017-07-03T21:32:52Z]`

* Returns: `[1499117572000]`

---
**Example 2:**

* Input values:
    1. `[2017-07-03T21:32:52+01:00]`

* Returns: `[1499113972000]`

---
**Example 3:**

* Parameters
    * unit: `seconds`

* Input values:
    1. `[2017-07-03T21:32:52+01:00]`

* Returns: `[1499113972]`

---
**Example 4:**

* Input values:
    1. `[2017-07-03]`

* Returns: `[1499040000000]`

## Parameter

### Unit

No description

* ID: `unit`
* Datatype: `enumeration`
* Default Value: `milliseconds`

## Advanced Parameter

`None`
