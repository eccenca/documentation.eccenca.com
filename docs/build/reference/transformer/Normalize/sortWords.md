---
title: "Sort words"
description: "Sorts all words in each value lexicographically."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Sort words
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Sorts all words in each value lexicographically.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Example 1:

* Input values:
  1. `[]`

* Returns:

  → `[]`


---
#### Example 2:

* Input values:
  1. `[c a b]`

* Returns:

  → `[a b c]`


---
#### Example 3:

* Input values:
  1. `[Hans Hansa    Hamburg, München Marburg]`

* Returns:

  → `[Hamburg Hans Hansa, Marburg München]`




## Parameter

### Split regex

The regular expression used to split values into words.

- Datatype: `string`
- Default Value: `\s+`



### Glue

Separator to be inserted between sorted words.

- Datatype: `string`
- Default Value: ` `



