---
title: "Format number"
description: "Formats a number according to a user-defined pattern. The pattern syntax is documented at: https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Format number
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




  Formats a number according to a user-defined pattern.
  The pattern syntax is documented at:
  https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html


## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * pattern: `000`

* Input values:
    1. `[1]`

* Returns: `[001]`


---
**Example 2:**

* Parameters
    * pattern: `000000.000`

* Input values:
    1. `[123.78]`

* Returns: `[000123.780]`


---
**Example 3:**

* Parameters
    * pattern: `###,###.###`

* Input values:
    1. `[123456.789]`

* Returns: `[123,456.789]`


---
**Example 4:**

* Parameters
    * pattern: `###.###,###`
    * locale: `de`

* Input values:
    1. `[123456.789]`

* Returns: `[123.456,789]`


---
**Example 5:**

* Parameters
    * pattern: `# apples`

* Input values:
    1. `[10]`

* Returns: `[10 apples]`


---
**Example 6:**

* Parameters
    * pattern: `000'0'`

* Input values:
    1. `[1]`

* Returns: `[0010]`


---
**Example 7:**

* Parameters
    * pattern: `0`

* Input values:
    1. `[1.0]`

* Returns: `[1]`


---
**Example 8:**

* Parameters
    * pattern: `0.0`

* Input values:
    1. `[0000123.4]`

* Returns: `[123.4]`




## Parameter

### Pattern

No description

- ID: `pattern`
- Datatype: `string`
- Default Value: `None`



### Locale

No description

- ID: `locale`
- Datatype: `string`
- Default Value: `en`





## Advanced Parameter

`None`