---
title: "Substring"
description: "Returns a substring between 'beginIndex' (inclusive) and 'endIndex' (exclusive). If 'endIndex' is 0 (default), it is ignored and the entire remaining string starting with 'beginIndex' is returned. If 'endIndex' is negative, -endIndex characters are removed from the end."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Substring
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Returns a substring between 'beginIndex' (inclusive) and 'endIndex' (exclusive). If 'endIndex' is 0 (default), it is ignored and the entire remaining string starting with 'beginIndex' is returned. If 'endIndex' is negative, -endIndex characters are removed from the end.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * beginIndex: `0`
    * endIndex: `1`

* Input values:
    1. `[abc]`

* Returns: `[a]`


---
**Example 2:**

* Parameters
    * beginIndex: `2`
    * endIndex: `3`

* Input values:
    1. `[abc]`

* Returns: `[c]`


---
**Example 3:**

* Parameters
    * beginIndex: `3`
    * endIndex: `3`

* Input values:
    1. `[abc]`

* Returns: `[]`


---
**Example 4:**

* Parameters
    * beginIndex: `2`
    * endIndex: `4`

* Input values:
    1. `[abc]`

* Returns: `[c]`
* **Throws error:** `ValidationException`


---
**Example 5:**

* Parameters
    * beginIndex: `2`
    * endIndex: `4`
    * stringMustBeInRange: `false`

* Input values:
    1. `[abc]`

* Returns: `[c]`


---
**Example 6:**

* Parameters
    * beginIndex: `10`
    * endIndex: `20`
    * stringMustBeInRange: `false`

* Input values:
    1. `[abc]`

* Returns: `[]`


---
**Example 7:**

* Parameters
    * beginIndex: `0`
    * endIndex: `-1`

* Input values:
    1. `[abc]`

* Returns: `[ab]`


---
**Example 8:**

* Parameters
    * beginIndex: `1`
    * endIndex: `0`

* Input values:
    1. `[abc]`

* Returns: `[bc]`




## Parameter

### Begin index

The beginning index, inclusive.

- ID: `beginIndex`
- Datatype: `int`
- Default Value: `0`



### End index

The end index, exclusive. Ignored if set to 0, i.e., the entire remaining string starting with 'beginIndex' is returned. If negative, -endIndex characters are removed from the end

- ID: `endIndex`
- Datatype: `int`
- Default Value: `0`



### String must be in range

If true, only strings will be accepted that are within the start and end indices, throwing a validating error if an index is out of range.

- ID: `stringMustBeInRange`
- Datatype: `boolean`
- Default Value: `true`





## Advanced Parameter

`None`