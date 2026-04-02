---
title: "Remove default stop words"
description: "Removes stop words based on a default stop word list."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Remove default stop words
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Description

The Remove default stop words plugin removes stop words from text using a built-in default stop word list.

Conceptually, it works like a standard stop word filter: the input is split into word tokens, each token is checked against the default list, and all tokens that appear in the list are removed. The remaining tokens are kept and returned as the filtered text.

Stop word removal is case-insensitive. For example, `The` and `the` are treated as the same stop word. In the case of German words, notice that the upper-case letter of the lower-case `ß` is `ẞ`, not `SS`.

If a different stop word list is needed, the Remove stop words plugin supports providing a stop word list as a resource, and the Remove remote stop words plugin supports fetching the stop word list from a remote URL.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[To be or not to be, that is the question]`

* Returns: `[To, question]`


---
**Example 2:**

* Input values:
    1. `[It always seems impossible, until it's done]`

* Returns: `[It impossible, ]`




## Parameter

`None`

## Advanced Parameter

`None`