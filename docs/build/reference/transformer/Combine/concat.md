---
title: "Concatenate"
description: "Concatenates strings from multiple inputs."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Concatenate

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Concatenates strings from multiple inputs.

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
    1. `[a]`
    2. `[b]`

* Returns: `[ab]`

---
**Example 4:**

* Parameters
    * glue: `-`

* Input values:
    1. `[First]`
    2. `[Last]`

* Returns: `[First-Last]`

---
**Example 5:**

* Parameters
    * glue: `-`

* Input values:
    1. `[First]`
    2. `[Second, Third]`

* Returns: `[First-Second, First-Third]`

---
**Example 6:**

* Parameters
    * glue: `-`

* Input values:
    1. `[First]`
    2. `[]`
    3. `[Second]`

* Returns: `[First--Second]`

---
**Example 7:**

* Parameters
    * glue: `-`

* Input values:
    1. `[First]`
    2. `[]`
    3. `[Second]`

* Returns: `[]`

---
**Example 8:**

* Parameters
    * glue: `-`
    * missingValuesAsEmptyStrings: `true`

* Input values:
    1. `[First]`
    2. `[]`
    3. `[Second]`

* Returns: `[First--Second]`

---
**Example 9:**

* Parameters
    * glue: `\n`

* Input values:
    1. `[First]`
    2. `[Second]`

* Returns:
    ```text
    [First
    Second]
    ```

---
**Example 10:**

* Parameters
    * glue: `\t\\\a`

* Input values:
    1. `[First]`
    2. `[Second]`

* Returns: `[First    \\aSecond]`

## Parameter

### Glue

Separator to be inserted between two concatenated strings. The text can contain escaped characters \n, \t and \\ that are replaced by a newline, tab or backslash respectively.

* ID: `glue`
* Datatype: `string`
* Default Value: `None`

### Missing values as empty strings

Handle missing values as empty strings.

* ID: `missingValuesAsEmptyStrings`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`
