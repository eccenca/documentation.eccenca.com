---
title: "Jaro distance"
description: "Matches strings based on the Jaro distance metric."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Jaro distance
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The Jaro distance measure calculates the similarity between two strings based on the number and order of common characters, the number of transpositions, and the length of the strings. The Jaro distance is 0 for a perfect match and 1 if there is no similarity between the given strings. 

For more information, please refer to: [https://en.wikipedia.org/wiki/Jaro–Winkler_distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance).

## Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

`None`

## Advanced Parameter

`None`