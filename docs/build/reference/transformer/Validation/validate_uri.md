---
title: "Validate URI"
description: "Validates that the input is a valid absolute IRI and returns it unchanged. Throws a validation error if the input is not a valid IRI."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Validate URI

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Validates that the input is a valid absolute IRI and returns it unchanged. Throws a validation error if the input is not a valid IRI.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[http://example.org/entity1]`

* Returns: `[http://example.org/entity1]`


---
**Example 2:**

* Input values:
    1. `[urn:example:1]`

* Returns: `[urn:example:1]`


---
**Example 3:**

* Input values:
    1. `[not a uri]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Example 4:**

* Input values:
    1. `[]`

* Returns: `[]`
* **Throws error:** `ValidationException`




## Parameter

`None`

## Advanced Parameter

`None`
