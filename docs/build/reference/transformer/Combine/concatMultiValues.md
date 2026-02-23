---
title: "Concatenate multiple values"
description: "Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Concatenate multiple values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Returns: `[]`

---
**Example 2:**

* Input values:
    1. `[a]`

* Returns: `[a]`

---
**Example 3:**

* Input values:
    1. `[a, b]`

* Returns: `[ab]`

---
**Example 4:**

* Parameters
    * glue: `x`

* Input values:
    1. `[a, b]`

* Returns: `[axb]`

---
**Example 5:**

* Input values:
    1. `[a, b]`
    2. `[1, 2]`

* Returns: `[ab, 12]`

---
**Example 6:**

* Parameters
    * glue: `\n\t\\`

* Input values:
    1.
    ```text
    [a
    	\b, c]
    ```

* Returns:
    ```text
    [a
    	\b
    	\c]
    ```

## Parameter

### Glue

No description

* ID: `glue`
* Datatype: `string`
* Default Value: `None`

### Remove duplicates

No description

* ID: `removeDuplicates`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`
