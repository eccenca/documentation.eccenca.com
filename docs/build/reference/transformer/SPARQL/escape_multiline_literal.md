---
title: "Escape SPARQL multiline literal"
description: "Escapes a value so it can be safely used inside a SPARQL triple-quoted string literal (`'''...'''` or `'''...'''`). Escapes backslashes and breaks any run of three or more consecutive single or double quotes. Individual quotes and newlines are preserved. The returned value does not include enclosing quotation marks."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Escape SPARQL multiline literal

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Escapes a value so it can be safely used inside a SPARQL triple-quoted string literal (`"""..."""` or `'''...'''`). Escapes backslashes and breaks any run of three or more consecutive single or double quotes. Individual quotes and newlines are preserved. The returned value does not include enclosing quotation marks.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1.
    ```text
    [simple
    value]
    ```

* Returns:
    ```text
    [simple
    value]
    ```


---
**Example 2:**

* Input values:
    1. `[with "quote"]`

* Returns: `[with "quote"]`


---
**Example 3:**

* Input values:
    1. `[back\slash]`

* Returns: `[back\\slash]`


---
**Example 4:**

* Input values:
    1. `[triple """ quotes]`

* Returns: `[triple \"\"\" quotes]`


---
**Example 5:**

* Input values:
    1. `[triple ''' quotes]`

* Returns: `[triple \'\'\' quotes]`




## Parameter

`None`

## Advanced Parameter

`None`
