---
title: "Date"
description: "The distance in days between two dates ('YYYY-MM-DD' format)."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Date
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The distance in days between two dates ('YYYY-MM-DD' format).

## Characteristics
This distance measure is not normalized, i.e., all distances start at 0 (exact match) and increase the more different the values are.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.
## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Returns 0 if both dates are equal:**

* Input values:
    - Source: `[2003-03-01]`
    - Target: `[2003-03-01]`

* Returns: `0.0`


---
**Returns 1 if both dates are one day apart:**

* Input values:
    - Source: `[2003-03-01]`
    - Target: `[2003-03-02]`

* Returns: `1.0`


---
**Returns the number of days if both dates are one month apart:**

* Input values:
    - Source: `[2003-03-01]`
    - Target: `[2003-04-01]`

* Returns: `31.0`


---
**Returns the number of days if both dates are one year apart:**

* Input values:
    - Source: `[2018-03-01]`
    - Target: `[2019-03-01]`

* Returns: `365.0`


---
**Time of day is ignored:**

* Input values:
    - Source: `[2003-03-01]`
    - Target: `[2003-03-01T06:00:00]`

* Returns: `0.0`


---
**Missing days are set to 1 by default:**

* Input values:
    - Source: `[2003-01]`
    - Target: `[2003-01-01]`

* Returns: `0.0`


---
**Missing months are set to 1 by default:**

* Input values:
    - Source: `[2003]`
    - Target: `[2003-01-01]`

* Returns: `0.0`


---
**Missing months and days are set to 1 by default:**

* Input values:
    - Source: `[2018]`
    - Target: `[2019]`

* Returns: `365.0`


---
**If 'requireMonthAndDay' is set, dates without a day and month will not match:**

* Parameters
    * requireMonthAndDay: `true`

* Input values:
    - Source: `[2003]`
    - Target: `[2003-03-01]`

* Returns: `Infinity`


---
**If 'requireMonthAndDay' is set, dates without a day will not match:**

* Parameters
    * requireMonthAndDay: `true`

* Input values:
    - Source: `[2003-12]`
    - Target: `[2003-03-01]`

* Returns: `Infinity`




## Parameter

### Require month and day

If true, no distance value will be generated if months or days are missing (e.g., 2019-11). If false, missing month or day fields will default to 1.

- ID: `requireMonthAndDay`
- Datatype: `boolean`
- Default Value: `false`





## Advanced Parameter

`None`