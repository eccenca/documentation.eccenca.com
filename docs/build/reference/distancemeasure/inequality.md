---
title: "Inequality"
description: "Returns success if values are not equal, failure otherwise."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Inequality
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Returns success if values are not equal, failure otherwise.

## Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns distance 0, if the values are different:**

* Input values:
    - Source: `[max]`
    - Target: `[john]`

* Returns: `0.0`


---
**Returns distance 1, if the values are equal:**

* Input values:
    - Source: `[max]`
    - Target: `[max]`

* Returns: `1.0`


---
**If multiple values are provided, returns 0, if at least one value does not match:**

* Input values:
    - Source: `[max, helmut]`
    - Target: `[max]`

* Returns: `0.0`


---
**If multiple values are provided, returns 1, if all value match:**

* Input values:
    - Source: `[max, max]`
    - Target: `[max, max]`

* Returns: `1.0`




## Parameter

`None`

## Advanced Parameter

`None`