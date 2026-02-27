---
title: "Starts with"
description: "Returns success if the first string starts with the second string, failure otherwise."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Starts with

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Returns success if the first string starts with the second string, failure otherwise.

## Characteristics

This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

### Reverse

Reverse source and target values

- ID: `reverse`
- Datatype: `boolean`
- Default Value: `false`

### Min length

The minimum length of the string being contained.

- ID: `minLength`
- Datatype: `int`
- Default Value: `2`

### Max length

The potential maximum length of the strings that must match. If the max length is greater than the length of the string to match, the full string must match.

- ID: `maxLength`
- Datatype: `int`
- Default Value: `2147483647`

## Advanced Parameter

`None`
