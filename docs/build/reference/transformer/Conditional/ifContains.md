---
title: "If contains"
description: "Accepts two or three inputs. If the first input contains the given value, the second input is forwarded. Otherwise, the third input is forwarded (if present)."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# If contains
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Accepts two or three inputs. If the first input contains the given value, the second input is forwarded. Otherwise, the third input is forwarded (if present).

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * search: `match`

* Input values:
    1. `[matching string]`
    2. `[this is a match]`

* Returns: `[this is a match]`


---
**Example 2:**

* Parameters
    * search: `match`

* Input values:
    1. `[different string]`
    2. `[this is a match]`

* Returns: `[]`


---
**Example 3:**

* Parameters
    * search: `match`

* Input values:
    1. `[different string]`
    2. `[this is a match]`
    3. `[this is no match]`

* Returns: `[this is no match]`




## Parameter

### Search

No description

- ID: `search`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`