---
title: "Validate date after"
description: "Validates if the first input date is after the second input date. Outputs the first input if the validation is successful."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Validate date after
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Validates if the first input date is after the second input date. Outputs the first input if the validation is successful.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[2015-04-02]`
    2. `[2015-04-03]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Example 2:**

* Input values:
    1. `[2015-04-04]`
    2. `[2015-04-03]`

* Returns: `[2015-04-04]`


---
**Example 3:**

* Parameters
    * allowEqual: `true`

* Input values:
    1. `[2015-04-03]`
    2. `[2015-04-03]`

* Returns: `[2015-04-03]`


---
**Example 4:**

* Parameters
    * allowEqual: `false`

* Input values:
    1. `[2015-04-03]`
    2. `[2015-04-03]`

* Returns: `[]`
* **Throws error:** `ValidationException`




## Parameter

### Allow equal

Allow both dates to be equal.

- ID: `allowEqual`
- Datatype: `boolean`
- Default Value: `false`





## Advanced Parameter

`None`