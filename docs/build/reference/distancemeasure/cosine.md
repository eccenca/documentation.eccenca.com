---
title: "Cosine"
description: "Cosine Distance Measure."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Cosine

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Cosine Distance Measure.

## Characteristics

This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for identical unit vectors:**

- Input values:
    - Source: `[a 1.0]`
    - Target: `[a 1.0]`

- Returns: `0.0`


---
**Returns 1 minus the dot product of the two vectors:**

- Input values:
    - Source: `[a 0.8;b 0.6]`
    - Target: `[a 0.5]`

- Returns: `0.6`


---
**Returns 1 for vectors that share no terms:**

- Input values:
    - Source: `[a 1.0]`
    - Target: `[b 1.0]`

- Returns: `1.0`


---
**Values that are not shaped as 'term score' do not match, instead of failing the linking execution:**

- Input values:
    - Source: `[not a vector]`
    - Target: `[a 1.0]`

- Returns: `1.0`


---
**Terms with a non-finite score are ignored:**

- Input values:
    - Source: `[a NaN]`
    - Target: `[a 1.0]`

- Returns: `1.0`




## Parameter

### K

No description

- ID: `k`
- Datatype: `int`
- Default Value: `3`

## Advanced Parameter

`None`
