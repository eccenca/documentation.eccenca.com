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
  <https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html>


## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**The digit '0' in the pattern pads the number with leading zeros:**

* Parameters
    * pattern: `000`

* Input values:
    1. `[1]`

* Returns: `[001]`


---
**Padding applies to the integer and the fraction part:**

* Parameters
    * pattern: `000000.000`

* Input values:
    1. `[123.78]`

* Returns: `[000123.780]`


---
**The placeholder '#' stands for an optional digit and ',' inserts a grouping separator:**

* Parameters
    * pattern: `###,###.###`

* Input values:
    1. `[123456.789]`

* Returns: `[123,456.789]`


---
**The pattern is interpreted in the configured locale, here German with '.' as grouping and ',' as decimal separator:**

* Parameters
    * pattern: `###.###,###`
    * locale: `de`

* Input values:
    1. `[123456.789]`

* Returns: `[123.456,789]`


---
**Literal text in the pattern is kept in the output:**

* Parameters
    * pattern: `# apples`

* Input values:
    1. `[10]`

* Returns: `[10 apples]`


---
**Quoted characters are copied to the output as-is, even if they are digits:**

* Parameters
    * pattern: `000'0'`

* Input values:
    1. `[1]`

* Returns: `[0010]`


---
**A pattern without fraction digits rounds to a whole number:**

* Parameters
    * pattern: `0`

* Input values:
    1. `[1.0]`

* Returns: `[1]`


---
**Leading zeros of the input are removed unless the pattern demands them:**

* Parameters
    * pattern: `0.0`

* Input values:
    1. `[0000123.4]`

* Returns: `[123.4]`




## Parameter

### Pattern

The number pattern, e.g., '###,###.###'.

* ID: `pattern`
* Datatype: `string`
* Default Value: `None`



### Locale

The locale in which the pattern is interpreted, given as an IETF BCP 47 language tag, e.g., 'en'.

* ID: `locale`
* Datatype: `string`
* Default Value: `en`

## Advanced Parameter

`None`

## Related Plugins

* [extractPhysicalQuantity](extractPhysicalQuantity.md) — Format number requires a numeric input. If the source data contains quantity strings with embedded unit symbols, Extract physical quantity parses those strings and returns the numeric value in the base unit — the form that Format number can then render according to a decimal pattern.
