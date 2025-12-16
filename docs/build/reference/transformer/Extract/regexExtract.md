---
title: "Regex extract"
description: "Extracts one or all matches of a regular expression within the input. If the regular expression contains one or more capturing groups, only the first group will be considered."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Regex extract
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

## Description

The `regexExtract` plugin extracts one or all matches of a regular expression within the input.

This plugin is an _extraction_ transformer plugin. It is configured with the parameters `regex` and `extractAll`. The
regular expression `regex` is simply the pattern used in the matching. With `extractAll`, we tell the `regexExtract`
plugin whether to extract _all_ values (with `extractAll = true`) or only the _first_ occurrence of the matching
(with `extractAll = false`, which is the default).

Additionally to normal regular expressions, we can also use _capturing groups_ such as in `(A)(B)(C)` instead of just
`ABC`. If capturing groups are used in a regular expression, only the _first_ capturing group will be considered. This
does _not_ mean the first matching group, but the first capturing group in the regex.

### Notes on regular expressions

The most commonly used examples of regular expressions are `"\\s*"` for representing whitespace characters, `[^0-9]*`
for numbers, and `[a-z]*` for the usual English characters between `a` and `z`. The star (`*`) represents an arbitrary
number of occurrences (zero included), whereas the plus sign (`+`) indicates a strictly positive number of occurrences
(zero excluded).

An uppercase version of the predefined character classes means _negation_, such as `"\\S*"` for _non_-whitespace
characters, or `"\\D*"` for _non_-digits.
Similarly, the hat sign `^` can be used for negating (arbitrary) character classes, such as `[^xyz]` for any character
except `x`, `y` or `z`.

**Attention**: Slashes in regular expressions have to be _escaped_, e.g. instead of `\s` we need to escape it as `\\s`.

### Note for advanced users

A compilation of the available constructs for building regular expressions is available in the
[API of the Java `Pattern`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html#sum).

## Relation to other plugins

Additionally to the `regexExtract` plugin, there are related plugins such as `validateRegex`, `ifMatchesRegex` and
`regexReplace`.

The distinctive feature of each of these plugins lies in what happens whenever the regular expression
matches the input value(s): the `regexExtract` plugin is used for _extracting_ matches from the input, `validateRegex`
is useful for _validating_ the input, `ifMatchesRegex` _conditionally distinguishes_ which input to take, and
`regexReplace` _replaces_ all occurrences of the matching.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**returns only the first match, when extractAll = false (default):**

* Parameters
    * regex: `[a-z]{2,4}123`

* Input values:
    1. `[afe123_abcd23]`

* Returns: `[afe123]`

---
**returns all matches, when extractAll = true:**

* Parameters
    * regex: `[a-z]{2,4}123`
    * extractAll: `true`

* Input values:
    1. `[afe123_abcd123]`

* Returns: `[afe123, abcd123]`

---
**returns an empty list if nothing matches:**

* Parameters
    * regex: `^[a-z]{2,4}123`

* Input values:
    1. `[abcde123]`

* Returns: `[]`

---
**returns the match of the first capturing group, which includes two to four letters:**

* Parameters
    * regex: `^([a-z]{2,4})123([a-z]+)`

* Input values:
    1. `[abcd123xyz]`

* Returns: `[abcd]`

---
**returns the match of the first capturing group, which includes at least one letter:**

* Parameters
    * regex: `^([a-z]+)123([a-z]{2,4})`

* Input values:
    1. `[pqrstuvwxyz123abcd]`

* Returns: `[pqrstuvwxyz]`

---
**returns an empty string, because the first capturing group includes the possibility of no letters:**

* Parameters
    * regex: `^([a-z]*)123([a-z]{2,4})`

* Input values:
    1. `[123abcd]`

* Returns: `[]`

---
**returns an empty list, because the first capturing group excludes the possibility of no letters:**

* Parameters
    * regex: `^([a-z]+)123([a-z]{2,4})`

* Input values:
    1. `[123abcd]`

* Returns: `[]`

---
**Example 8:**

* Parameters
    * regex: `"bedeutungen"\s*:\s*\[\s*(?:"([^"]*)"(?:\s*,\s*"([^"]*)")*)*\s*\]`

* Input values:
    1. `["bedeutungen" : [ ]]`

* Returns: `[]`

## Parameter

### Regex

Regular expression

* ID: `regex`
* Datatype: `string`
* Default Value: `None`

### Extract all

If true, all matches are extracted. If false, only the first match is extracted (default).

* ID: `extractAll`
* Datatype: `boolean`
* Default Value: `false`

## Advanced Parameter

`None`
