---
title: "Numeric reduce"
description: "Strips all non-numeric characters from a string."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Numeric reduce

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Strips all non-numeric characters from a string.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Parameters
    * keepPunctuation: `false`

* Input values:
    1. `[some1.2Value]`

* Returns: `[12]`


---
**Example 2:**

* Parameters
    * keepPunctuation: `true`

* Input values:
    1. `[some1.2Value]`

* Returns: `[1.2]`




## Parameter

### Keep punctuation

No description

* ID: `keepPunctuation`
* Datatype: `boolean`
* Default Value: `true`

## Advanced Parameter

`None`

## Related Plugins

* **regexReplace** — Numeric reduce is a zero-configuration specialization of Regex replace using a non-digit stripping pattern. Regex replace is the choice when the stripping rule is not strictly numeric.
* **aggregateNumbers** — Numeric reduce strips non-numeric characters from each value. Aggregate numbers silently discards any value it cannot parse as a number, so values with embedded non-numeric characters are lost to the aggregation without this step.
* **numOperation** — Numeric reduce strips non-numeric characters from each value, making each one parseable as a number. Numeric operation throws a validation exception on any input that cannot be parsed, rather than discarding it silently.
