---
title: "Regex extract"
description: "Extracts occurrences of a regex 'regex' in a string. If there is at least one capture group, it will return the string of the first capture group instead."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Regex extract
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Extracts occurrences of a regex "regex" in a string. If there is at least one capture group, it will return the string of the first capture group instead.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
#### returns the first match:

* Parameters
  * *regex*: `[a-z]{2,4}123`

* Input values:
  1. `[afe123_abc123]`

* Returns:

  → `[afe123]`


---
#### returns all matches, if extractAll = true:

* Parameters
  * *regex*: `[a-z]{2,4}123`
  * *extractAll*: `true`

* Input values:
  1. `[afe123_abc123]`

* Returns:

  → `[afe123, abc123]`


---
#### returns an empty list if nothing matches:

* Parameters
  * *regex*: `^[a-z]{2,4}123`

* Input values:
  1. `[abcdef123]`

* Returns:

  → `[]`


---
#### returns the match of the first capture group that matches:

* Parameters
  * *regex*: `^([a-z]{2,4})123([a-z]+)`

* Input values:
  1. `[abcd123xyz]`

* Returns:

  → `[abcd]`


---
#### Example 5:

* Parameters
  * *regex*: `"bedeutungen"\s*:\s*\[\s*(?:"([^"]*)"(?:\s*,\s*"([^"]*)")*)*\s*\]`

* Input values:
  1. `["bedeutungen" : [ ]]`

* Returns:

  → `[]`




## Parameter

### Regex

Regular expression

- Datatype: `string`
- Default Value: `None`



### Extract all

If true, all matches are extracted. If false, only the first match is extracted.

- Datatype: `boolean`
- Default Value: `false`



