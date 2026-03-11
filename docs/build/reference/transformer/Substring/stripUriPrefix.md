---
title: "Strip URI prefix"
description: "Strips the URI prefix and decodes the remainder based on UTF-8 URL decoding (using java.net.URLDecoder). Leaves values unchanged which are not a valid URI."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Strip URI prefix

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Strips the URI prefix and decodes the remainder based on UTF-8 URL decoding (using java.net.URLDecoder). Leaves values unchanged which are not a valid URI.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[http://example.org/some/path/to/value]`

* Returns: `[value]`

---
**Example 2:**

* Input values:
    1. `[urn:scheme:value]`

* Returns: `[value]`

---
**Example 3:**

* Input values:
    1. `[http://example.org/some/path/to/encoded%20v%C3%A4lue]`

* Returns: `[encoded välue]`

---
**Example 4:**

* Input values:
    1. `[value]`

* Returns: `[value]`

---
**Example 5:**

* Input values:
    1. `[urn:scheme:Two_words]`

* Returns: `[Two words]`

---
**Example 6:**

* Parameters
    * decodeUnderscoresToSpaces: `false`

* Input values:
    1. `[urn:scheme:Two_words]`

* Returns: `[Two_words]`

## Parameter

### Decode underscores to spaces

If true, underscores will be decoded to spaces.

* ID: `decodeUnderscoresToSpaces`
* Datatype: `boolean`
* Default Value: `true`

## Advanced Parameter

`None`
