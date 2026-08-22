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

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns the substring between 'beginIndex' (inclusive) and 'endIndex' (exclusive). Indices are zero-based:**

* Parameters
    * beginIndex: `0`
    * endIndex: `1`

* Input values:
    1. `[abc]`

* Returns: `[a]`


---
**Extracts a single character if 'endIndex' is 'beginIndex' plus one:**

* Parameters
    * beginIndex: `2`
    * endIndex: `3`

* Input values:
    1. `[abc]`

* Returns: `[c]`


---
**Equal indices yield an empty string:**

* Parameters
    * beginIndex: `3`
    * endIndex: `3`

* Input values:
    1. `[abc]`

* Returns: `[]`


---
**Indices that are out of range for the value are rejected by default:**

* Parameters
    * beginIndex: `2`
    * endIndex: `4`

* Input values:
    1. `[abc]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**If 'stringMustBeInRange' is false, out-of-range indices are clipped to the length of the value:**

* Parameters
    * beginIndex: `2`
    * endIndex: `4`
    * stringMustBeInRange: `false`

* Input values:
    1. `[abc]`

* Returns: `[c]`


---
**Clipping yields an empty string if the whole range lies outside the value:**

* Parameters
    * beginIndex: `10`
    * endIndex: `20`
    * stringMustBeInRange: `false`

* Input values:
    1. `[abc]`

* Returns: `[]`


---
**A negative 'endIndex' removes that many characters from the end:**

* Parameters
    * beginIndex: `0`
    * endIndex: `-1`

* Input values:
    1. `[abc]`

* Returns: `[ab]`


---
**An 'endIndex' of 0 returns the entire remaining string starting at 'beginIndex':**

* Parameters
    * beginIndex: `1`
    * endIndex: `0`

* Input values:
    1. `[abc]`

* Returns: `[bc]`


---
**Values shorter than the number of characters to remove from the end are rejected:**

* Parameters
    * beginIndex: `0`
    * endIndex: `-3`

* Input values:
    1. `[ab]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**If 'stringMustBeInRange' is false, values shorter than the number of characters to remove yield an empty string:**

* Parameters
    * beginIndex: `0`
    * endIndex: `-3`
    * stringMustBeInRange: `false`

* Input values:
    1. `[ab]`

* Returns: `[]`


---
**A begin index that exceeds the end index is rejected:**

* Parameters
    * beginIndex: `2`
    * endIndex: `1`

* Input values:
    1. `[abc]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**If 'stringMustBeInRange' is false, a begin index that exceeds the end index yields an empty string:**

* Parameters
    * beginIndex: `2`
    * endIndex: `1`
    * stringMustBeInRange: `false`

* Input values:
    1. `[abc]`

* Returns: `[]`




## Parameter

### Begin index

The beginning index, inclusive.

* ID: `beginIndex`
* Datatype: `int`
* Default Value: `0`



### End index

The end index, exclusive. Ignored if set to 0, i.e., the entire remaining string starting with 'beginIndex' is returned. If negative, -endIndex characters are removed from the end.

* ID: `endIndex`
* Datatype: `int`
* Default Value: `0`



### String must be in range

If true, only strings will be accepted that are within the start and end indices, throwing a validating error if an index is out of range.

* ID: `stringMustBeInRange`
* Datatype: `boolean`
* Default Value: `true`

## Advanced Parameter

`None`

## Related Plugins

* [stripPrefix](stripPrefix.md) — Substring removes a fixed number of characters from the start regardless of their content. Strip prefix is more selective: it only removes from the start if the configured string is actually found there.
* [stripPostfix](stripPostfix.md) — Substring works by index: it removes a fixed count of trailing characters regardless of their content. Strip postfix is the alternative when the trailing portion is a known string; it checks for it and leaves the value unchanged if not found.
* [untilCharacter](untilCharacter.md) — Substring extracts by position: the start and end indices are fixed and apply to every input value regardless of its content. Until character extracts up to a specific character.
