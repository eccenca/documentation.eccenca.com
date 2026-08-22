---
title: "Concatenate multiple values"
description: "Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Concatenate multiple values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Concatenates multiple values received for an input. If applied to multiple inputs, yields at most one value per input. Optionally removes duplicate values.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Without input values, no output is generated:**

* Returns: `[]`


---
**A single value is returned unchanged:**

* Input values:
    1. `[a]`

* Returns: `[a]`


---
**All values of an input are concatenated into one value. The default glue is the empty string:**

* Input values:
    1. `[a, b]`

* Returns: `[ab]`


---
**The glue string is inserted between the values:**

* Parameters
    * glue: `x`

* Input values:
    1. `[a, b]`

* Returns: `[axb]`


---
**Each input is concatenated separately, yielding one value per input:**

* Input values:
    1. `[a, b]`
    2. `[1, 2]`

* Returns: `[ab, 12]`


---
**Escaped character sequences in the glue are replaced by the actual characters (newline, tab, backslash):**

* Parameters
    * glue: `\n\t\\`

* Input values:
    1.
    ```text
    [a
    	\b, c]
    ```

* Returns:
    ```text
    [a
    	\b
    	\c]
    ```


---
**Duplicates are removed, also when they span multiple values:**

* Parameters
    * glue: ``
    * removeDuplicates: `true`

* Input values:
    1. `[Albert, Einstein, Albert Einstein]`

* Returns: `[Albert Einstein]`


---
**With an empty glue, only whole duplicate values are removed:**

* Parameters
    * removeDuplicates: `true`

* Input values:
    1. `[a, b, a]`

* Returns: `[ab]`


---
**Values consisting only of the glue collapse to an empty string:**

* Parameters
    * glue: `x`
    * removeDuplicates: `true`

* Input values:
    1. `[x, x]`

* Returns: `[]`




## Parameter

### Glue

No description

* ID: `glue`
* Datatype: `string`
* Default Value: `None`



### Remove duplicates

No description

* ID: `removeDuplicates`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`

## Related Plugins

* [concat](concat.md) — Concatenate multiple values collapses all values within each input into one string, preserving the boundary between inputs. Concatenate crosses that boundary — it takes one value from each input and produces all combinations, so the output grows with the number of inputs and values.
