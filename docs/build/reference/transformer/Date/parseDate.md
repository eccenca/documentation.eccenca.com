---
title: "Parse date pattern"
description: "Parses a date based on a specified pattern, returning an xsd:date."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Parse date pattern
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Parses a date based on a specified pattern, returning an xsd:date.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * format: `dd.MM.yyyy`

* Input values:
    1. `[03.04.2015]`

* Returns: `[2015-04-03]`

---
**Example 2:**

* Parameters
    * format: `dd.MM.yyyy`

* Input values:
    1. `[3.4.2015]`

* Returns: `[2015-04-03]`

---
**Example 3:**

* Parameters
    * format: `yyyyMMdd`

* Input values:
    1. `[20150403]`

* Returns: `[2015-04-03]`

---
**Example 4:**

* Parameters
    * format: `MMM yyyy`
    * locale: `en`

* Input values:
    1. `[May 2024]`

* Returns: `[2024-05-01]`

---
**Example 5:**

* Parameters
    * format: `MMM yyyy`
    * locale: `de`

* Input values:
    1. `[Mai 2024]`

* Returns: `[2024-05-01]`

---
**Example 6:**

* Parameters
    * format: `MMM yyyy`
    * locale: `de`

* Input values:
    1. `[May 2024]`

* Returns: `[]`
* **Throws error:** `ValidationException`

---
**Example 7:**

* Parameters
    * format: `yyyyMMdd`
    * lenient: `false`

* Input values:
    1. `[20150000]`

* Returns: `[]`
* **Throws error:** `ValidationException`

## Parameter

### Format

The date pattern used to parse the input values

* ID: `format`
* Datatype: `string`
* Default Value: `dd-MM-yyyy`

### Lenient

If set to true, the parser tries to use heuristics to parse dates with invalid fields (such as a day of zero).

* ID: `lenient`
* Datatype: `boolean`
* Default Value: `false`

### Locale

Optional locale for the date format. If not set the system's locale will be used.

* ID: `locale`
* Datatype: `option[locale]`
* Default Value: `None`

## Advanced Parameter

`None`
