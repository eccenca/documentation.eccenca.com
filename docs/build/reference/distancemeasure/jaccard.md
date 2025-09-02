---
title: "Jaccard"
description: "Jaccard similarity coefficient. Divides the matching tokens by the number of distinct tokens from both inputs."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Jaccard
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Jaccard similarity coefficient. Divides the matching tokens by the number of distinct tokens from both inputs.

### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares sets of multiple values.Typically, incoming values are tokenized before being fed into this measure.
### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for equal sets of values:**

* Input values:
    - Source: `[A, B, C]`
    - Target: `[B, C, A]`

* Returns: `0.0`


---
**Returns 1 if there is no overlap between both sets of tokens:**

* Input values:
    - Source: `[A, B, C]`
    - Target: `[D, E, F]`

* Returns: `1.0`


---
**Returns 0.5 if half of all unique tokens overlap:**

* Input values:
    - Source: `[A, B, C]`
    - Target: `[A, B, D]`

* Returns: `0.5`


---
**Returns 2/3 if one third of all unique tokens overlap:**

* Input values:
    - Source: `[John, Jane]`
    - Target: `[John, Max]`

* Returns: `0.6666666666666666`




## Parameter

`None`

## Advanced Parameter

`None`