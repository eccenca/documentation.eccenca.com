---
title: "Combined input hash"
description: "Calculates a single hash value covering all input values combined, across all input ports. Values are fed into the hash function in port order without any separator between them."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Combined input hash

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The **Combined input hash** operator produces exactly one hash value covering all input values combined, across all connected input ports. However many values arrive and however many ports are connected, the output is always a single string.

## How combining works

All values from all input ports are fed sequentially into a single hash function — port 1 first, then port 2, and so on. Within each port, values are processed in the order they arrive. No separator is inserted between values or between ports. The hash covers the concatenated byte content of all values in that traversal order.

This means the result depends on both the content and the order of values. The same set of values in a different order produces a different hash. Connecting one port with values `["apple", "banana"]` produces the same hash as connecting two ports with `["apple"]` and `["banana"]` respectively, because the bytes are fed in the same sequence either way.

## Output

The output is a single lowercase hexadecimal string. The length depends on the algorithm: 64 characters for SHA-256, 32 for MD5, 40 for SHA-1, 96 for SHA-384, 128 for SHA-512. If the input is empty, the output is the hash of an empty message.

Values are encoded as UTF-8 before hashing.

## Algorithm parameter

The algorithm parameter selects the hash function. The default is SHA-256. The following algorithms from the [SPARQL 1.1 specification](https://www.w3.org/TR/sparql11-query/#func-hash) are supported:

| SPARQL name | Java name | Notes |
|-------------|-----------|-------|
| MD5 | MD5 | Weak — vulnerable to collision attacks. Avoid for security-sensitive use. |
| SHA1 | SHA-1 | Weak — deprecated for most security purposes. |
| SHA256 | SHA-256 | Recommended default. |
| SHA384 | SHA-384 | Stronger than SHA-256. |
| SHA512 | SHA-512 | Strongest in the SPARQL set. |

Additional algorithms available on the JVM (such as SHA-512/256 and SHA-3 variants) are also accepted. The full list is JVM-dependent and visible in the algorithm parameter dropdown.

Note that the Java names use hyphens (SHA-256, SHA-1) where SPARQL uses none (SHA256, SHA1). Both forms are accepted by this operator.

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
**Reversing the value order produces a different hash, confirming order-sensitivity:**

* Input values:
    1. `[banana, apple]`

* Returns: `[d4183362b538440bb9a5f82359791c647280e6b657a1812f16f7bcc2b8f141ca]`


---
**Values from multiple ports are combined in port order, producing the same hash as the equivalent single-port sequence:**

* Input values:
    1. `[apple]`
    2. `[banana]`

* Returns: `[5b692305517af54eb5ae12b9ff89eaf89e31f6a6ee208365886a18b81a2fc2f8]`


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

## Advanced Parameter

`None`

## Related Plugins

* [perValueHash](perValueHash.md) — The Per-value hash plugin hashes each input value independently and returns one hash per value, preserving cardinality. The Combined input hash plugin instead feeds all values into a single hash function, producing one combined hash regardless of input size.
* [mapWithDefaultInput](../Replace/mapWithDefaultInput.md) — One hash value is produced for the entire set of inputs by the Combined input hash plugin. The Map with default plugin instead keeps a value sequence and rewrites it position by position through the mapping, falling back to the second input where no mapping entry is found.
