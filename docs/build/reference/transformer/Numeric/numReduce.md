---
title: "Numeric reduce"
description: "Strip all non-numeric characters from a string."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Numeric reduce
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Strip all non-numeric characters from a string.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * keepPunctuation: `false`

* Input values:
    1. `[some1.2Value]`

* Returns: `[12]`

---
**Example 2:**

* Parameters
    * keepPunctuation: `true`

* Input values:
    1. `[some1.2Value]`

* Returns: `[1.2]`

## Parameter

### Keep punctuation

No description

* ID: `keepPunctuation`
* Datatype: `boolean`
* Default Value: `true`

## Advanced Parameter

`None`
