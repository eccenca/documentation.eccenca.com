---
title: "Tokenize"
description: "Tokenizes all input values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Tokenize

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Tokenizes all input values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**By default, splits values at whitespaces:**

* Input values:
    1. `[Hello World]`

* Returns: `[Hello, World]`

---
**Optionally, splits values at the provided regex:**

* Parameters
    * regex: `,`

* Input values:
    1. `[.175,.050]`

* Returns: `[.175, .050]`

## Parameter

### Regex

The regular expression used to split values.

* ID: `regex`
* Datatype: `string`
* Default Value: `\s`

## Advanced Parameter

`None`
