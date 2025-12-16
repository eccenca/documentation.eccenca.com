---
title: "Encode URL"
description: "URL encodes the string."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Encode URL
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

URL encodes the string.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[ab]`

* Returns: `[ab]`

---
**Example 2:**

* Input values:
    1. `[a&b]`

* Returns: `[a%26b]`

---
**Example 3:**

* Input values:
    1. `[http://example.org/some/path]`

* Returns: `[http%3A%2F%2Fexample.org%2Fsome%2Fpath]`

## Parameter

`None`

## Advanced Parameter

### Encoding

The character encoding.

* ID: `encoding`
* Datatype: `string`
* Default Value: `UTF-8`
