---
title: "Filter by regex"
description: "This transformer filters values by a regular expression: values matching the regex are kept, unless 'negate' is set, which keeps only the values that don't. By default the regex must match a value in full; setting 'contains' relaxes that so any value containing a match is kept instead."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Filter by regex

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Description

The Filter by regex plugin keeps or drops values based on a regular expression. By default, a value is kept only if it matches the regex in full; setting `contains` relaxes that to keep any value the regex matches anywhere within. Setting `negate` inverts whichever of those two decisions is in effect.

## Notes on regular expressions

Attention: regex metacharacters in the pattern have to be escaped to be matched literally, e.g. a literal dot needs `\.`, not `.`, which otherwise means "any character."

A pattern that can match an empty string, such as `a*`, matches every value under `contains`, since an empty match always "occurs somewhere" in any string.

A regex that fails to compile throws a `PatternSyntaxException` rather than silently doing nothing.

Attention: This happens during _execution_.
In other words: It's technically possible to save _invalid_ regular expressions.

### Note for advanced users

A compilation of the available constructs for building regular expressions is available in the
[API of the Java `Pattern`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/regex/Pattern.html).

## Missing or empty input

If no input is connected to this transformer, it throws a `ValidationException`. If an input is connected but carries no values, the transformer returns nothing for that entity — this is not an error.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Keeps only values that fully match the regex:**

* Parameters
    * regex: `abc`

* Input values:
    1. `[abc, xabcx, xyz]`

* Returns: `[abc]`


---
**Keeps only values consisting of exactly three word characters:**

* Parameters
    * regex: `\w\w\w`

* Input values:
    1. `[abc, ab, abcd, a-x]`

* Returns: `[abc]`


---
**Excludes values that fully match the regex, keeping the rest:**

* Parameters
    * regex: `abc`
    * negate: `true`

* Input values:
    1. `[abc, xabcx, xyz]`

* Returns: `[xabcx, xyz]`


---
**Keeps values that contain a match anywhere, not just full matches:**

* Parameters
    * regex: `abc`
    * contains: `true`

* Input values:
    1. `[abc, xabcx, xyz]`

* Returns: `[abc, xabcx]`


---
**Excludes values that contain a match anywhere, keeping the rest:**

* Parameters
    * regex: `abc`
    * negate: `true`
    * contains: `true`

* Input values:
    1. `[abc, xabcx, xyz]`

* Returns: `[xyz]`


---
**A pattern matching zero characters finds a match in any value, so 'contains' keeps everything:**

* Parameters
    * regex: `a*`
    * contains: `true`

* Input values:
    1. `[xyz, aaa, ]`

* Returns: `[xyz, aaa, ]`


---
**An anchored pattern still only matches at the anchored position, even with 'contains' set:**

* Parameters
    * regex: `^abc`
    * contains: `true`

* Input values:
    1. `[abcxyz, xabcx, xyz]`

* Returns: `[abcxyz]`


---
**Throws when the regex fails to compile:**

* Parameters
    * regex: `(`

* Input values:
    1. `[abc]`

* Returns: `[]`
* **Throws error:** `PatternSyntaxException`


---
**A backslash-escaped metacharacter in the regex is matched literally:**

* Parameters
    * regex: `a\.b`

* Input values:
    1. `[a.b, aXb]`

* Returns: `[a.b]`


---
**A whitespace-only value matches a whitespace pattern:**

* Parameters
    * regex: `\s+`

* Input values:
    1. `[   , abc]`

* Returns: `[   ]`


---
**A Unicode value matches a literal pattern correctly:**

* Parameters
    * regex: `café`

* Input values:
    1. `[café, cafe]`

* Returns: `[café]`


---
**Returns nothing when the connected input carries no values:**

* Parameters
    * regex: `abc`

* Input values:
    1. `[]`

* Returns: `[]`


---
**Throws when no input is connected:**

* Parameters
    * regex: `abc`

* Returns: `[]`
* **Throws error:** `ValidationException`




## Parameter

### Regex

The regular expression to test each value against.

* ID: `regex`
* Datatype: `string`
* Default Value: `None`



### Negate

If true, keeps values that do not match instead of values that do.

* ID: `negate`
* Datatype: `boolean`
* Default Value: `false`



### Contains

If true, the pattern only needs to occur somewhere in the value.

* ID: `contains`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`

## Related Plugins

* [regexSelect](../Selection/regexSelect.md) — Filter by regex keeps or drops values from the input sequence based on regex matching. Regex selection keeps the checked value out of the output and instead returns a pattern-list-shaped result filled with the provided output value where a pattern matches.
* [validateRegex](../Validation/validateRegex.md) — Validate regex throws on the first non-matching value, failing the whole operation. Filter by regex just drops it and keeps the rest.
* [regexReplace](../Replace/regexReplace.md) — Filter by regex is a structural filter: it never changes a value's content, only whether that value appears in the output. Regex replace works the other way: it changes what's inside each value, but every value that goes in still comes out.
* [regexExtract](../Extract/regexExtract.md) — Regex extract never returns the original value — only part of the match itself, a substring or a capturing group. By contrast, Filter by regex returns only the original value, unmodified, or nothing at all.
* [ifMatchesRegex](../Conditional/ifMatchesRegex.md) — If matches regex checks one sequence for a match, then returns one of two candidate sequences, completely unchanged. Each value in a single sequence is tested on its own under Filter by regex, kept or dropped to build the output.
* [filterByLength](filterByLength.md) — Filter by length only checks length, bounded by a minimum and a maximum. Length is irrelevant to Filter by regex; only the pattern matters.
* [removeValues](removeValues.md) — Remove values checks each value against a fixed, comma-separated blacklist — an exact, case-insensitive match, nothing computed. Filter by regex checks each value against a regular expression instead, which can be a single word or a broad, open-ended pattern.
