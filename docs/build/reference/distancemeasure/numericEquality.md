---
title: "Numeric equality"
description: "Compares values numerically instead of their string representation as the 'String Equality' operator does. Allows to set the needed precision of the comparison. A value of 0.0 means that the values must represent exactly the same (floating point) value, values higher than that allow for a margin of tolerance."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Numeric equality
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Compares values numerically instead of their string representation as the 'String Equality' operator does.
Allows to set the needed precision of the comparison. A value of 0.0 means that the values must represent exactly the same
(floating point) value, values higher than that allow for a margin of tolerance.

### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 for equal numbers:**

* Input values:
    - Source: `[4.2]`
    - Target: `[4.2]`

* Returns: `0.0`


---
**Returns 1 if at least one value is not a number:**

* Input values:
    - Source: `[1]`
    - Target: `[one]`

* Returns: `1.0`


---
**Returns 0 for numbers within the configured precision:**

* Parameters
    * precision: `0.1`

* Input values:
    - Source: `[1.3]`
    - Target: `[1.35]`

* Returns: `0.0`


---
**Returns 1 for numbers outside the configured precision:**

* Parameters
    * precision: `0.1`

* Input values:
    - Source: `[1.3]`
    - Target: `[1.5]`

* Returns: `1.0`




## Parameter

### Precision

The range of tolerance in floating point number comparisons. Must be 0 or a non-negative number smaller than 1.

- Datatype: `double`
- Default Value: `0.0`



