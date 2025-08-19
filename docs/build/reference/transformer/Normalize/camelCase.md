---
title: "Camel case"
description: "Converts a string to camel case. Upper camel case is the default, lower camel case can be chosen."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Camel case
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Converts a string to camel case. Upper camel case is the default, lower camel case can be chosen.

### Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**A sentence with several words is converted to a single word written in UpperCamelCase:**

* Parameters
    * isDromedary: `false`

* Input values:
    1. `[hello world]`

* Returns: `[HelloWorld]`


---
**A sentence with several words is converted to a single word written in lowerCamelCase:**

* Parameters
    * isDromedary: `true`

* Input values:
    1. `[hello world]`

* Returns: `[helloWorld]`


---
**A single lowercase letter is converted to UpperCamelCase, i.e. capitalized:**

* Parameters
    * isDromedary: `false`

* Input values:
    1. `[h]`

* Returns: `[H]`


---
**A single lowercase letter is converted to lowerCamelCase (aka. dromedary case), i.e. uncapitalized:**

* Parameters
    * isDromedary: `true`

* Input values:
    1. `[h]`

* Returns: `[h]`


---
**An empty space is removed. The dromedary/lower case is irrelevant here:**

* Parameters
    * isDromedary: `true`

* Input values:
    1. `[ ]`

* Returns: `[]`


---
**An empty space is removed. The upper case is irrelevant here:**

* Parameters
    * isDromedary: `false`

* Input values:
    1. `[ ]`

* Returns: `[]`




## Parameter

### Dromedary case

If true, lower camel case (aka. dromedary case) is used, otherwise upper camel case is used.

- ID: `isDromedary`
- Datatype: `boolean`
- Default Value: `false`





## Advanced Parameter

`None`