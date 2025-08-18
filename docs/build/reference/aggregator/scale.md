---
title: "Scale"
description: "Scales a similarity score by a factor."
icon: octicons/cross-reference-24
tags: 
---
# Scale
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Scales a similarity score by a factor.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Scales similarity scores by the specified factor:**

* Parameters
    * factor: `0.5`

* Input values: `[1.0]`
* Returns: `0.5`


---
**Ignores missing values:**

* Input values: `[null]`
* Returns: `null`


---
**Throws a validation error if more than one input is provided:**

* Input values: `[0.1, 0.2]`
* Returns: `null`




## Parameter

### Factor

All input similarity values are multiplied with this factor.

- Datatype: `double`
- Default Value: `1.0`



