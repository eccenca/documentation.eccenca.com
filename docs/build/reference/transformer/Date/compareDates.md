---
title: "Compare dates"
description: "Compares two dates."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Compare dates
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Compares two dates.
Returns 1 if the comparison yields true and 0 otherwise.
If there are multiple dates in both sets, the comparator must be true for all dates.
For instance, {2014-08-02,2014-08-03} < {2014-08-03} yields 0 as not all dates in the first set are smaller than in the second.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * comparator: `<`

* Input values:
    1. `[2017-01-01]`
    2. `[2017-01-02]`

* Returns: `[1]`


---
**Example 2:**

* Parameters
    * comparator: `<`

* Input values:
    1. `[2017-01-02]`
    2. `[2017-01-01]`

* Returns: `[0]`


---
**Example 3:**

* Parameters
    * comparator: `>`

* Input values:
    1. `[2017-01-02]`
    2. `[2017-01-01]`

* Returns: `[1]`


---
**Example 4:**

* Parameters
    * comparator: `>`

* Input values:
    1. `[2017-01-01]`
    2. `[2017-01-02]`

* Returns: `[0]`


---
**Example 5:**

* Parameters
    * comparator: `=`

* Input values:
    1. `[2017-01-01]`
    2. `[2017-01-01]`

* Returns: `[1]`


---
**Example 6:**

* Parameters
    * comparator: `=`

* Input values:
    1. `[2017-01-02]`
    2. `[2017-01-01]`

* Returns: `[0]`




## Parameter

### Comparator

No description

- ID: `comparator`
- Datatype: `enumeration`
- Default Value: `<`





## Advanced Parameter

`None`