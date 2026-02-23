---
title: "Numeric similarity"
description: "Computes the numeric distance between two numbers."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Numeric similarity

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Computes the numeric distance between two numbers.

## Characteristics

This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

`None`

## Advanced Parameter

### Min index value

The minimum number that is used for indexing

- ID: `minValue`
- Datatype: `double`
- Default Value: `-Infinity`

### Max index value

The maximum number that is used for indexing

- ID: `maxValue`
- Datatype: `double`
- Default Value: `Infinity`

