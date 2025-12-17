---
title: "Normalized Levenshtein distance"
description: "Normalized Levenshtein distance. Divides the edit distance by the length of the longer string."
icon: octicons/cross-reference-24
tags:
    - DistanceMeasure
---

# Normalized Levenshtein distance

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Normalized Levenshtein distance. Divides the edit distance by the length of the longer string.

## Characteristics

This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for equal strings:**

* Input values:
    * Source: `[John]`
    * Target: `[John]`

* Returns: `0.0`

---
**Returns 1/4 if two strings of length 4 differ by one edit operation:**

* Input values:
    * Source: `[John]`
    * Target: `[Jxhn]`

* Returns: `0.25`

---
**Normalizes the edit distance by the length of the longer string:**

* Input values:
    * Source: `[John]`
    * Target: `[Jhn]`

* Returns: `0.25`

---
**Returns the maximum distance of 1 for completely different strings:**

* Input values:
    * Source: `[John]`
    * Target: `[Clara]`

* Returns: `1.0`

## Parameter

`None`

## Advanced Parameter

### Q-grams size

The size of the q-grams to be indexed. Setting this to zero will disable indexing.

* ID: `qGramsSize`
* Datatype: `int`
* Default Value: `2`

### Min char

The minimum character that is used for indexing

* ID: `minChar`
* Datatype: `char`
* Default Value: `0`

### Max char

The maximum character that is used for indexing

* ID: `maxChar`
* Datatype: `char`
* Default Value: `z`
