---
title: "Levenshtein distance"
description: "Levenshtein distance. Returns a distance value between zero and the size of the string."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Levenshtein distance
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Levenshtein distance. Returns a distance value between zero and the size of the string.

### Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for equal strings:**

* Input values:
    - Source: `[John]`
    - Target: `[John]`

* Returns: `0.0`


---
**Returns 1 for strings that differ by one edit operation:**

* Input values:
    - Source: `[John]`
    - Target: `[Jxhn]`

* Returns: `1.0`


---
**Returns 3 for strings that differ by three edit operations:**

* Input values:
    - Source: `[Saturday]`
    - Target: `[Sunday]`

* Returns: `3.0`




## Parameter

`None`

## Advanced Parameter

### Q-grams size

The size of the q-grams to be indexed. Setting this to zero will disable indexing.

- ID: `qGramsSize`
- Datatype: `int`
- Default Value: `2`



### Min char

The minimum character that is used for indexing

- ID: `minChar`
- Datatype: `char`
- Default Value: `0`



### Max char

The maximum character that is used for indexing

- ID: `maxChar`
- Datatype: `char`
- Default Value: `z`



