---
title: "Parse integer"
description: "Parses integer values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Parse integer

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Parses integer values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * commaAsDecimalPoint: `true`
    * thousandSeparator: `false`

* Input values:
    1. `[1000,00]`

* Returns: `[1000]`


---
**Example 2:**

* Parameters
    * commaAsDecimalPoint: `true`
    * thousandSeparator: `true`

* Input values:
    1. `[1.000,00]`

* Returns: `[1000]`


---
**Example 3:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `false`

* Input values:
    1. `[1000.00]`

* Returns: `[1000]`


---
**Example 4:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `true`

* Input values:
    1. `[1,000.00]`

* Returns: `[1000]`


---
**Large integers are parsed exactly, without floating point precision loss:**

* Input values:
    1. `[1234567890123456789]`

* Returns: `[1234567890123456789]`


---
**An explicit plus sign is accepted:**

* Input values:
    1. `[+42]`

* Returns: `[42]`


---
**Integers outside the 64-bit range are rejected instead of silently corrupted:**

* Input values:
    1. `[99999999999999999999]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Values with unparsed characters are rejected, e.g. a thousands separator although it is disabled:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `false`

* Input values:
    1. `[1,000.00]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Values whose separators do not form valid thousands groups are rejected, e.g. a two-digit group:**

* Parameters
    * commaAsDecimalPoint: `false`
    * thousandSeparator: `true`

* Input values:
    1. `[1,00]`

* Returns: `[]`
* **Throws error:** `ValidationException`


---
**Values that are not plain numbers are rejected, e.g. "NaN":**

* Input values:
    1. `[NaN]`

* Returns: `[]`
* **Throws error:** `ValidationException`




## Parameter

### Comma as decimal point

Use comma or point (default) as a decimal separator.

* ID: `commaAsDecimalPoint`
* Datatype: `boolean`
* Default Value: `false`



### Thousand separator

Presence of a thousands separator (default: absence), compatible with the chosen decimal separator.

* ID: `thousandSeparator`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`
