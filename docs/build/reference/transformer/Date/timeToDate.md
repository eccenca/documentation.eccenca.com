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

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**By default, a milliseconds timestamp is converted to a full xsd:dateTime in UTC:**

* Input values:
    1. `[1499117572000]`

* Returns: `[2017-07-03T21:32:52Z]`


---
**A custom date format returns only the requested fields:**

* Parameters
    * format: `yyyy-MM-dd`

* Input values:
    1. `[1499040000000]`

* Returns: `[2017-07-03]`


---
**The 'unit' parameter interprets the input as seconds instead of milliseconds:**

* Parameters
    * format: `yyyy-MM-dd`
    * unit: `seconds`

* Input values:
    1. `[1499040000]`

* Returns: `[2017-07-03]`


---
**Custom formats are rendered in UTC, independently of the server timezone:**

* Parameters
    * format: `yyyy-MM-dd HH:mm`

* Input values:
    1. `[0]`

* Returns: `[1970-01-01 00:00]`




## Parameter

### Format

Custom output format (e.g., 'yyyy-MM-dd'), rendered in UTC. If left empty, a full xsd:dateTime (UTC) is returned.

* ID: `format`
* Datatype: `string`
* Default Value: `None`



### Unit

No description

* ID: `unit`
* Datatype: `enumeration`
* Default Value: `milliseconds`

## Advanced Parameter

`None`

## Related Plugins

* [datetoTimestamp](datetoTimestamp.md) — Timestamp to date converts a Unix integer to a date string; Date to timestamp is the reverse of that, converting a date string back to a Unix integer.
