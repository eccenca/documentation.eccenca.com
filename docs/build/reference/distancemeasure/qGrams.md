---
title: "qGrams"
description: "String similarity based on q-grams (by default q=2)."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# qGrams
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



String similarity based on q-grams (by default q=2).

### Characteristics
This distance measure is normalized, i.e., all distances are between 0 (exact match) and 1 (no similarity).

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0.0 if the input strings are equal:**

* Input values:
    - Source: `[abcd]`
    - Target: `[abcd]`

* Returns: `0.0`


---
**Returns 1.0 if the input strings do not share a single q-gram:**

* Input values:
    - Source: `[abcd]`
    - Target: `[dcba]`

* Returns: `1.0`


---
**Returns 1 minus the matching q-grams divided by the total number of q-grams. Generated q-grams in this example: (#a, ab, b#) and (#a, ac, c#):**

* Input values:
    - Source: `[ab]`
    - Target: `[ac]`

* Returns: `0.8`




## Parameter

### Q

No description

- ID: `q`
- Datatype: `int`
- Default Value: `2`





## Advanced Parameter

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



