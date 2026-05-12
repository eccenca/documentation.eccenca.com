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

## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

- **date** — Where the date time metric plugin demands full datetime values and measures in seconds, the date metric plugin works at day granularity and accepts year-only or year-month dates.
