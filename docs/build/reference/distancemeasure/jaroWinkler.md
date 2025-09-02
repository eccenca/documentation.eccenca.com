---
title: "Jaro-Winkler distance"
description: "Matches strings based on the Jaro-Winkler distance measure."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Jaro-Winkler distance
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The Jaro-Winkler distance measure is a variation of the Jaro distance metric. It takes into account the prefixes of the strings being compared and assigns higher weights to matching prefixes.

For more information, please refer to: [https://en.wikipedia.org/wiki/Jaro–Winkler_distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance).

### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

`None`

## Advanced Parameter

`None`