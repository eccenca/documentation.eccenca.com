---
title: "Regex replace"
description: "Replace all occurrences of a regular expression in a string. If no replacement is given, the occurrences of the regular expression will be deleted."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Regex replace
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Description

The `regexReplace` plugin replaces all occurrences of a regular expression.

This plugin is a _replace_ transformer plugin. This means that if the regular expression does _not_ match the input
value, it will be replaced with an empty string, i.e. deleted.

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

Additionally to the `regexReplace` plugin, there are related plugins such as `validateRegex`, `ifMatchesRegex` and
`regexExtract`.

The distinctive feature of each of these plugins lies in what happens whenever the regular expression
matches the input value(s): the `regexReplace` plugin is used for _replacing_ the input, `validateRegex` is useful for
_validating_ the input, `ifMatchesRegex` _conditionally distinguishes_ which input to take, and `regexExtract`
_extracts_ all occurrences of the matching.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Removes all digits by replacing them with an empty string:**

* Parameters
    * regex: `[^0-9]*`

* Input values:
    1. `[a0b1c2]`

* Returns: `[012]`


---
**Removes all letters by replacing them with an empty string:**

* Parameters
    * regex: `[a-z]*`

* Input values:
    1. `[abcdef1]`

* Returns: `[1]`


---
**Removes all vowels by replacing them with an empty string:**

* Parameters
    * regex: `[aeyiuoAEYIUO]*`

* Input values:
    1. `[Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, Bombur, Thorin]`

* Returns: `[Dwln, Bln, Kl, Fl, Dr, Nr, r, n, Gln, Bfr, Bfr, Bmbr, Thrn]`


---
**Removes all consonants by replacing them with an empty string:**

* Parameters
    * regex: `[^aeyiuoAEYIUO]*`

* Input values:
    1. `[Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, Bombur, Thorin]`

* Returns: `[ai, ai, ii, ii, oi, oi, Oi, Oi, oi, iu, ou, ou, oi]`


---
**Replaces all vowels with a common vowel:**

* Parameters
    * regex: `[aeyiuoAEYIUO]{1}`
    * replace: `a`

* Input values:
    1. `[Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, Bombur, Thorin]`

* Returns: `[Dwalan, Balan, Kala, Fala, Dara, Nara, ara, aan, Glaan, Bafar, Bafar, Bambar, Tharan]`


---
**Replaces all vowels with a common double vowel:**

* Parameters
    * regex: `[aeyiuoAEYIUO]{1}`
    * replace: `aa`

* Input values:
    1. `[Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, Bombur, Thorin]`

* Returns: `[Dwaalaan, Baalaan, Kaalaa, Faalaa, Daaraa, Naaraa, aaraa, aaaan, Glaaaan, Baafaar, Baafaar, Baambaar, Thaaraan]`




## Parameter

### Regex

The regular expression to match

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### Replace

The replacement of each match

- ID: `replace`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`