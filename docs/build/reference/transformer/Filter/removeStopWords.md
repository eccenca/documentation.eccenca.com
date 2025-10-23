---
title: "Remove stop words"
description: "Removes stop words based on a stop word list resource."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Remove stop words
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The stop word list is specified as a resource, e.g. a file identical to
[this German stop word list](https://raw.githubusercontent.com/stopwords-iso/stopwords-de/refs/heads/master/stopwords-de.txt).

Such a stop word list resource is useful, for instance, to specify the stop words of a specific language or
application domain.

Regardless of the stop word list used, the following comments apply:

* Each line in the stop word list should contain a single stop word.
* The removal of stop words is case-insensitive. For example, 'The' and 'the' are considered the same.
* In the case of German words, notice that the upper-case letter of the lower-case 'ß' is 'ẞ', not 'SS'.
* The separator defines a regular expression (regex) that is used for detecting words.
* By default, the separator is a regular expression for non-whitespace characters.

Additionally, notice the simpler filter 'removeDefaultStopWords', which uses a default stop word list.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[To be or not to be, that is the question]`

* Returns: `[, question]`


---
**Example 2:**

* Input values:
    1. `[It always seems impossible, until it's done]`

* Returns: `[impossible, ]`




## Parameter

### Stop word list

Resource for the stop word list

- ID: `stopWordList`
- Datatype: `resource`
- Default Value: `None`



### Separator

RegEx for detecting words

- ID: `separator`
- Datatype: `string`
- Default Value: `[\s-]+`





## Advanced Parameter

`None`