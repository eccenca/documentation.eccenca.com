---
title: "UUID"
description: "Generates UUIDs. If no input value is provided, a random UUID (type 4) is generated using a cryptographically strong pseudo random number generator. If input values are provided, a name-based UUID (type 3) is generated for each input value. Each input value will generate a separate UUID. For building a UUID from multiple inputs, the Concatenate operator can be used."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# UUID
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



 Generates UUIDs.
If no input value is provided, a random UUID (type 4) is generated using a cryptographically strong pseudo random number generator.
If input values are provided, a name-based UUID (type 3) is generated for each input value.
Each input value will generate a separate UUID. For building a UUID from multiple inputs, the Concatenate operator can be used.


## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[input value]`

* Returns: `[cee963a2-8f70-3e97-b51a-85ef732e66dd]`


---
**Example 2:**

* Input values:
    1. `[üöä!, êéè]`

* Returns: `[690802dd-a317-335f-807c-e4e1e32b7b5b, 925cbd7f-377b-3fbd-8f4c-ca41529b74ad]`




## Parameter

`None`

## Advanced Parameter

`None`