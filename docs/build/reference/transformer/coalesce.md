---
title: "Coalesce (first non-empty input)"
description: "Forwards the first non-empty input, i.e. for which any value(s) exist. A single empty string is considered a value."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Coalesce (first non-empty input)
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Example 1:

* Input values:
  1. `[]`
  2. `[]`
  3. `[]`

* Returns:

  → `[]`


---
#### Example 2:

* Input values:
  1. `[]`
  2. `[]`

* Returns:

  → `[]`


---
#### Example 3:

* Returns:

  → `[]`


---
#### Example 4:

* Input values:
  1. `[]`
  2. `[first]`
  3. `[second]`

* Returns:

  → `[first]`


---
#### Example 5:

* Input values:
  1. `[]`
  2. `[first A, first B]`
  3. `[second]`

* Returns:

  → `[first A, first B]`


---
#### Example 6:

* Input values:
  1. `[first]`
  2. `[second]`

* Returns:

  → `[first]`




## Parameter

`None`