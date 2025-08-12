---
title: "Or"
description: "At least one input score must be within the threshold. Selects the maximum score."
icon: octicons/cross-reference-24
tags: 
---
# Or
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### Selects the maximum similarity score:

* Input values: [0.5, 0.0]
* Returns: `0.5`


---
#### Selects the maximum similarity score:

* Input values: [-1.0, -0.5, -0.3]
* Returns: `-0.3`


---
#### Missing scores default to a similarity score of -1:

* Input values: [(none)]
* Returns: `-1.0`


---
#### Weights are ignored:

* Weights: [1000, 0]
* Input values: [1.0, 0.0]
* Returns: `1.0`




## Parameter

`None`