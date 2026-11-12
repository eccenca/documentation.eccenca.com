---
title: "Combined input hash"
description: "Calculates a single hash value covering all input values combined, across all input ports. Values are fed into the hash function in port order, with an optional separator (the glue parameter) inserted between them."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Combined input hash

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The **Combined input hash** operator produces exactly one hash value covering all input values combined, across all connected input ports, with an optional separator inserted between them.

## How combining works

All values from all input ports are fed sequentially into a single hash function, in port order; within each port, values are processed in the order they arrive. An optional separator, set with the glue parameter, can be inserted between every adjacent pair of values in that order — see the Glue parameter section below. The hash covers the concatenated byte content of all values in that order, together with any inserted separator.

Swapping two values, or changing a single character within one value, produces a different hash. Connecting one port with values `["apple", "banana"]` produces the same hash as connecting two ports with `["apple"]` and `["banana"]` respectively, because the bytes are fed in the same sequence either way.

## Output

The output is a single lowercase hexadecimal string whose length is fixed by the chosen algorithm: 64 characters for SHA-256, 32 for MD5, 40 for SHA-1, 96 for SHA-384, 128 for SHA-512. Connecting no values at all still produces a hash — the hash of the empty message, not an error.

Values are encoded as UTF-8 before hashing, so the same text produces the same bytes regardless of platform or locale.

## Algorithm parameter

The algorithm parameter selects the hash function. The following algorithms from the [SPARQL 1.1 specification](https://www.w3.org/TR/sparql11-query/#func-hash) are supported:

| SPARQL name | Java name | Notes |
|-------------|-----------|-------|
| MD5 | MD5 | Has known collision vulnerabilities. |
| SHA1 | SHA-1 | Deprecated for most security purposes. |
| SHA256 | SHA-256 | Default. |
| SHA384 | SHA-384 | |
| SHA512 | SHA-512 | |

Additional algorithms available on the JVM (such as SHA-512/256 and SHA-3 variants) are also accepted. The full list is JVM-dependent and visible in the algorithm parameter dropdown.

The Java names use hyphens (SHA-256, SHA-1) where SPARQL uses none (SHA256, SHA1); both forms are accepted by this operator.

## Glue parameter

The glue parameter sets a separator string that is inserted between every adjacent pair of values in the traversal order described above, defaulting to an empty string. Its text can contain the escaped sequences `\n`, `\t`, and `\\`, which are converted to a newline, a tab, and a backslash respectively before hashing.

Connecting one port with values `["apple", "banana"]` and a glue of `-` produces the same hash as connecting two ports with `["apple"]` and `["banana"]` respectively, using the same glue, because the glue is inserted at the same point in the byte sequence either way.

An input port without a value is skipped, and the glue is only inserted between the values that exist. To insert the glue for such a port, the port can be connected through a Default Value operator with an empty value.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**A single input value produces one combined SHA-256 hash:**

* Input values:
    1. `[input value]`

* Returns: `[f708c2afff0ed197e8551c4dd549ee5b848e0b407106cbdb8e451c8cd1479362]`


---
**Multiple values on one input are combined into a single hash:**

* Input values:
    1. `[apple, banana]`

* Returns: `[5b692305517af54eb5ae12b9ff89eaf89e31f6a6ee208365886a18b81a2fc2f8]`


---
**The order in which values are combined affects the resulting hash:**

* Input values:
    1. `[banana, apple]`

* Returns: `[d4183362b538440bb9a5f82359791c647280e6b657a1812f16f7bcc2b8f141ca]`


---
**Values from multiple ports are combined in port order: port 1's values first, then port 2's:**

* Input values:
    1. `[apple]`
    2. `[banana]`

* Returns: `[5b692305517af54eb5ae12b9ff89eaf89e31f6a6ee208365886a18b81a2fc2f8]`


---
**The glue parameter inserts a separator between values:**

* Parameters
    * glue: `-`

* Input values:
    1. `[apple, banana]`

* Returns: `[d6300f978b8699862450cbabc35349239c09e95c356723c32fc1407ec8104c78]`


---
**Values from multiple ports are combined using the glue separator in port order: port 1's values first, then port 2's:**

* Parameters
    * glue: `-`

* Input values:
    1. `[apple]`
    2. `[banana]`

* Returns: `[d6300f978b8699862450cbabc35349239c09e95c356723c32fc1407ec8104c78]`


---
**The glue parameter accepts escaped characters, here a newline:**

* Parameters
    * glue: `\n`

* Input values:
    1. `[apple, banana]`

* Returns: `[5c573825e0a168e9e382f9b7e78e6603271634dceac792b9c92fa77a27d404f8]`


---
**Values containing non-ASCII characters are encoded as UTF-8 before being hashed:**

* Parameters
    * glue: `-`

* Input values:
    1. `[café, banana]`

* Returns: `[c17ffffc64b5ffd83dbc2a975134c65a7f7f457a898b6e1fc6d2db1217fa92ff]`


---
**The glue parameter accepts a separator longer than one character:**

* Parameters
    * glue: `::`

* Input values:
    1. `[apple, banana]`

* Returns: `[7f721cdbf970bad79a82e7d827e0e5eef3d8263610aa6f062427060f5d2379db]`


---
**The order of values combined with a glue separator affects the resulting hash:**

* Parameters
    * glue: `-`

* Input values:
    1. `[banana, apple]`

* Returns: `[4472ed905ebe09b0e7a37ffa5adc6b0b2f052a6d0045fc037e2e56cdb45fba0a]`


---
**The glue separator is never applied to a single value, since there is no adjacent value to separate it from:**

* Parameters
    * glue: `-`

* Input values:
    1. `[solo]`

* Returns: `[5364f2f2fc4f54e9d47ad29cfb08ef430c8153394bf2a0dff5cbe77a0ffef861]`


---
**An input port without a value is skipped, and no glue is inserted for it:**

* Parameters
    * glue: `-`

* Input values:
    1. `[]`
    2. `[solo]`

* Returns: `[5364f2f2fc4f54e9d47ad29cfb08ef430c8153394bf2a0dff5cbe77a0ffef861]`


---
**An empty port 2 is skipped in the same way, producing the same hash as an empty port 1:**

* Parameters
    * glue: `-`

* Input values:
    1. `[solo]`
    2. `[]`

* Returns: `[5364f2f2fc4f54e9d47ad29cfb08ef430c8153394bf2a0dff5cbe77a0ffef861]`


---
**Without any input values, the glue is not hashed on its own, producing the hash of an empty message:**

* Parameters
    * glue: `-`

* Input values:
    1. `[]`
    2. `[]`

* Returns: `[e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855]`


---
**With more than two values, the glue separator is inserted between every adjacent pair:**

* Parameters
    * glue: `-`

* Input values:
    1. `[a, b]`
    2. `[c]`

* Returns: `[cbd2be7b96f770a0326948ebd158cf539fab0627e8adbddc97f7a65c6a8ae59a]`


---
**Three values in one port produce a hash with the glue separator inserted between every pair:**

* Parameters
    * glue: `-`

* Input values:
    1. `[a, b, c]`

* Returns: `[cbd2be7b96f770a0326948ebd158cf539fab0627e8adbddc97f7a65c6a8ae59a]`


---
**A value that is identical to the glue string is hashed as ordinary byte content, with no special escaping:**

* Parameters
    * glue: `-`

* Input values:
    1. `[a, -, b]`

* Returns: `[1acd27f89b4f44ddaf3b81fadb5491ea61f9ae3981545cf62d3502a387bcf350]`


---
**Values from three ports are combined using the glue separator in port order: port 1's value, then port 2's, then port 3's:**

* Parameters
    * glue: `-`

* Input values:
    1. `[a]`
    2. `[b]`
    3. `[c]`

* Returns: `[cbd2be7b96f770a0326948ebd158cf539fab0627e8adbddc97f7a65c6a8ae59a]`


---
**The order in which values are combined affects the resulting hash, even with more than two values and a glue separator:**

* Parameters
    * glue: `-`

* Input values:
    1. `[c, b]`
    2. `[a]`

* Returns: `[8e599734c8f75bd7866757e5f9cd4ab3cc173d753fb858a85ae6efb817e3e200]`


---
**With more than two values, the SHA-1 algorithm still inserts the glue separator between every adjacent pair:**

* Parameters
    * algorithm: `SHA-1`
    * glue: `-`

* Input values:
    1. `[a, b]`
    2. `[c]`

* Returns: `[e088d9e3f737c091378fe8494936b16d51eb42ee]`


---
**With the SHA-512 algorithm selected, the glue separator is inserted between every adjacent pair of three values:**

* Parameters
    * algorithm: `SHA-512`
    * glue: `-`

* Input values:
    1. `[a, b]`
    2. `[c]`

* Returns: `[a271a54e93179f7dccb132a17c914e66e76a91ae3b7cb8b3abffa21a8ffb66b65a2883769bc4c6f95ab39fbd039cfe21046b485cef1588269d2605c7253f2b98]`


---
**With the MD5 algorithm selected, the glue parameter still inserts a separator between values:**

* Parameters
    * algorithm: `MD5`
    * glue: `-`

* Input values:
    1. `[apple, banana]`

* Returns: `[9b22c402a5166c71ebdf2d1b99f37727]`


---
**With the MD5 algorithm selected, escaped glue characters are still converted before being used as the separator:**

* Parameters
    * algorithm: `MD5`
    * glue: `\n`

* Input values:
    1. `[apple, banana]`

* Returns: `[cf0bf238cadd6688db6f8d2511a52ebf]`


---
**With the MD5 algorithm and a glue of '-', the hash equals the SPARQL expression MD5(CONCAT(?a, "-", ?b)):**

* Parameters
    * algorithm: `MD5`
    * glue: `-`

* Input values:
    1. `[a]`
    2. `[b]`

* Returns: `[8ca2ed590cf2ea2404f2e67641bcdf50]`


---
**The algorithm parameter selects the hash function (MD5):**

* Parameters
    * algorithm: `MD5`

* Input values:
    1. `[input value]`

* Returns: `[cee963a28f70ee97751a85ef732e66dd]`


---
**The algorithm parameter selects the hash function (SHA-1):**

* Parameters
    * algorithm: `SHA-1`

* Input values:
    1. `[apple]`

* Returns: `[d0be2dc421be4fcd0172e5afceea3970e2f3d940]`


---
**The algorithm parameter selects the hash function (SHA-384):**

* Parameters
    * algorithm: `SHA-384`

* Input values:
    1. `[apple]`

* Returns: `[3d8786fcb588c93348756c6429717dc6c374a14f7029362281a3b21dc10250ddf0d0578052749822eb08bc0dc1e68b0f]`


---
**The algorithm parameter selects the hash function (SHA-512):**

* Parameters
    * algorithm: `SHA-512`

* Input values:
    1. `[apple]`

* Returns: `[844d8779103b94c18f4aa4cc0c3b4474058580a991fba85d3ca698a0bc9e52c5940feb7a65a3a290e17e6b23ee943ecc4f73e7490327245b4fe5d5efb590feb2]`


---
**Empty input produces the hash of an empty message:**

* Input values:
    1. `[]`

* Returns: `[e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855]`


---
**Empty algorithm string causes IllegalArgumentException:**

* Parameters
    * algorithm: ``

* Input values:
    1. `[foo]`

* Returns: `[]`
* **Throws error:** `IllegalArgumentException`




## Parameter

### Algorithm

The hash algorithm to be used.

* ID: `algorithm`
* Datatype: `string`
* Default Value: `SHA256`



### Glue

Separator to be inserted between two concatenated strings. The text can contain escaped characters \n, \t and \\ that are replaced by a newline, tab or backslash respectively.

* ID: `glue`
* Datatype: `string`
* Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

* [perValueHash](perValueHash.md) — The Per-value hash plugin hashes each input value independently and returns one hash per value, preserving cardinality. The Combined input hash plugin instead feeds all values into a single hash function, producing one combined hash regardless of input size.
* [mapWithDefaultInput](../Replace/mapWithDefaultInput.md) — One hash value is produced for the entire set of inputs by the Combined input hash plugin. The Map with default plugin instead keeps a value sequence and rewrites it position by position through the mapping, falling back to the second input where no mapping entry is found.
* [concat](../Combine/concat.md) — Combined input hash always returns exactly one value, however many values or ports are connected. Concatenate instead produces every combination of connected values as a separate output, so more than one value on an input produces multiple outputs instead of one.
* [zip](../Combine/zip.md) — Combined input hash accepts any number of ports and always returns exactly one value. Zip instead requires exactly two inputs, pairs their values by position, and returns one output per position rather than one combined result.
* [concatMultiValues](../Combine/concatMultiValues.md) — Concatenate multiple values combines everything received on one port into a single string, but keeps each port's result separate; more ports still return separate results, one per port. Combined input hash instead crosses every port boundary, always returning one hash value overall.
