---
title: "Is substring"
description: "Checks if a source value is a substring of a target value."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Is substring

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Checks if a source value is a substring of a target value.

## Characteristics

This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

### Reverse

Reverse source and target inputs

- ID: `reverse`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`

## Related Plugins

- **startsWith** — The Starts With plugin tests a stricter condition: not only must the target appear in the source, but it must appear at the very start.
- **substringDistance** — Containment and similarity are not the same measure. Is substring checks whether the source string appears anywhere inside the target and returns a binary result; Substring comparison scores the overall similarity between the two strings.
