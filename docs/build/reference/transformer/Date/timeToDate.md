---
title: "Timestamp to date"
description: "Convert a timestamp to xsd:date format. Expects an integer that denotes the passed time since the Unix Epoch (1970-01-01)"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Timestamp to date
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Convert a timestamp to xsd:date format. Expects an integer that denotes the passed time since the Unix Epoch (1970-01-01)

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[1499117572000]`

* Returns: `[2017-07-03T21:32:52Z]`


---
**Example 2:**

* Parameters
    * format: `yyyy-MM-dd`

* Input values:
    1. `[1499040000000]`

* Returns: `[2017-07-03]`


---
**Example 3:**

* Parameters
    * format: `yyyy-MM-dd`
    * unit: `seconds`

* Input values:
    1. `[1499040000]`

* Returns: `[2017-07-03]`




## Parameter

### Format

Custom output format (e.g., 'yyyy-MM-dd'). If left empty, a full xsd:dateTime (UTC) is returned.

- ID: `format`
- Datatype: `string`
- Default Value: `None`



### Unit

No description

- ID: `unit`
- Datatype: `enumeration`
- Default Value: `milliseconds`





## Advanced Parameter

`None`