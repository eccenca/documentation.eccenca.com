---
title: "DateTime"
description: "Distance between two date time values (xsd:dateTime format) in seconds."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# DateTime

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Distance between two date time values (xsd:dateTime format) in seconds.

## Characteristics

This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for equal date times:**

- Input values:
    - Source: `[2010-09-24T05:00:00]`
    - Target: `[2010-09-24T05:00:00]`

- Returns: `0.0`


---
**Returns the distance in seconds:**

- Input values:
    - Source: `[2001-10-26T21:32:10]`
    - Target: `[2001-10-26T21:32:40]`

- Returns: `30.0`


---
**Date times crossing a month boundary are one day (86400 seconds) apart:**

- Input values:
    - Source: `[2020-01-31T00:00:00]`
    - Target: `[2020-02-01T00:00:00]`

- Returns: `86400.0`


---
**Explicit timezone offsets are taken into account:**

- Input values:
    - Source: `[2020-01-01T00:00:00Z]`
    - Target: `[2020-01-01T02:00:00+02:00]`

- Returns: `0.0`


---
**Invalid date times do not match:**

- Input values:
    - Source: `[2020-01-01T00:00:00]`
    - Target: `[not a date]`

- Returns: `Infinity`




## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

- [date](date.md) — Where the date time metric plugin demands full datetime values and measures in seconds, the date metric plugin works at day granularity and accepts year-only or year-month dates.
