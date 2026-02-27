---
title: "Zip"
description: "Concatenates the values of two inputs in pairs."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Zip

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Concatenates the values of two inputs in pairs.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Zipping two inputs of equal length:**

* Input values:
    1. `[a, b]`
    2. `[1, 2]`

* Returns: `[a1, b2]`

---
**Zipping two inputs of different lengths, using placeholders:**

* Parameters
    * firstPlaceholder: `_`
    * secondPlaceholder: `-`

* Input values:
    1. `[a, b, c]`
    2. `[1, 2]`

* Returns: `[a1, b2, c-]`

---
**Zipping two inputs using a glue string:**

* Parameters
    * glue: `-`

* Input values:
    1. `[a, b]`
    2. `[1, 2]`

* Returns: `[a-1, b-2]`

---
**Zipping two inputs using a glue string with escape characters:**

* Parameters
    * glue: `\n`

* Input values:
    1. `[a, b]`
    2. `[1, 2]`

* Returns:
    ```text
    [a
    1, b
    2]
    ```

## Parameter

### First placeholder

Placeholder to be used if the first input provides fewer values than the second one.

* ID: `firstPlaceholder`
* Datatype: `string`
* Default Value: `None`

### Second placeholder

Placeholder to be used if the second input provides fewer values than the first one.

* ID: `secondPlaceholder`
* Datatype: `string`
* Default Value: `None`

### Glue

Separator to be inserted between two concatenated strings. The text can contain escaped characters \n, \t and \\ that are replaced by a newline, tab or backslash respectively.

* ID: `glue`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`
