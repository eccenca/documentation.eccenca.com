---
title: "Remove default stop words"
description: "Removes stop words based on a default stop word list."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Remove default stop words
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



This stop word list filter uses the following
[list of English stop words](https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt)
as a default.

The removal of stop words is case-insensitive. For example, 'The' and 'the' are considered the same.

In the case of German words, notice that the upper-case letter of the lower-case 'ß' is 'ẞ', not 'SS'.

Should you want to provide your own stop word list, either as a resource (e.g. a file) or a remote URL, see the filters
'removeStopWords' and 'removeRemoteStopWords'.

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