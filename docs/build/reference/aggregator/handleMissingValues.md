---
title: "Handle missing values"
description: "Generates a default similarity score, if no similarity score is provided (e.g., due to missing values). Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation."
icon: octicons/cross-reference-24
tags: 
---
# Handle missing values
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Generates a default similarity score, if no similarity score is provided (e.g., due to missing values). Using this operator can have a performance impact, since it lowers the efficiency of the underlying computation.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Forwards input similarity scores:**

* Input values: `[0.1]`
* Returns: `0.1`


---
**Outputs the default score, if no input score is provided:**

* Parameters
    * defaultValue: `1.0`

* Input values: `[null]`
* Returns: `1.0`




## Parameter

### Default value

The default value to be generated, if no similarity score is provided. Must be a value between -1 (inclusive) and 1 (inclusive). '1' represents boolean true and '-1' represents boolean false.

- Datatype: `double`
- Default Value: `-1.0`



