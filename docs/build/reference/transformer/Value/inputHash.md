---
title: "Input hash"
description: "Calculates the hash sum of the input values. Generates a single hash sum for all input values combined."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Input hash
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Calculates the hash sum of the input values. Generates a single hash sum for all input values combined.
This operator supports using different hash algorithms from the [Secure Hash Algorithms family](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (SHA, e.g. SHA256) and two algorithms from the [Message-Digest Algorithm family](https://en.wikipedia.org/wiki/MD5) (MD2 / MD5). Please be aware that some of these algorithms are not secure due the possibility of collision attacks and other attacks.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Example 1:**

* Input values:
    1. `[input value]`

* Returns: `[f708c2afff0ed197e8551c4dd549ee5b848e0b407106cbdb8e451c8cd1479362]`

## Parameter

### Algorithm

The hash algorithm to be used.

* ID: `algorithm`
* Datatype: `string`
* Default Value: `SHA256`

## Advanced Parameter

`None`
