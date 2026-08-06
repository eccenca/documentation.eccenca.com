---
title: "Escape SPARQL plain literal"
description: "Escapes a value so it can be safely used inside a SPARQL short-form string literal. Escapes backslashes, quotes, newlines, carriage returns and tabs. The returned value does not include enclosing quotation marks."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Escape SPARQL plain literal

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Escapes a value so it can be safely used inside a SPARQL short-form string literal. Escapes backslashes, quotes, newlines, carriage returns and tabs. The returned value does not include enclosing quotation marks.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[simple value]`

* Returns: `[simple value]`


---
**Example 2:**

* Input values:
    1. `[with "quotes"]`

* Returns: `[with \"quotes\"]`


---
**Example 3:**

* Input values:
    1. `[back\slash]`

* Returns: `[back\\slash]`


---
**Example 4:**

* Input values:
    1.
    ```text
    [line1
    line2]
    ```

* Returns: `[line1\nline2]`




## Parameter

`None`

## Advanced Parameter

`None`
