---
title: "Per-value hash"
description: "Hashes each input value independently and returns one hash per value. Accepts exactly one input port."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Per-value hash

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The **Per-value hash** operator hashes each input value independently and returns one hash per value. The output count always equals the input count — cardinality is preserved.

## SPARQL alignment

This operator produces the same output as the SPARQL 1.1 hash functions applied per value. For a single input value, `SHA256(?x)` in SPARQL returns the same result as this operator with the default SHA256 algorithm.

## Single-input constraint

The operator accepts exactly one input port. Connecting more than one port throws an `IllegalArgumentException`. This constraint exists because per-value hashing is defined relative to a single value sequence — combining values across ports would require choosing a port-merging strategy, which is the behaviour of the **Combined input hash** operator instead.

## Output

Each input value produces one lowercase hexadecimal hash string. The output order matches the input order. If the input is empty, the output is empty — no hash is produced.

Values are encoded as UTF-8 before hashing.

## Algorithm parameter

The algorithm parameter selects the hash function. The default is SHA-256. The five algorithms from the [SPARQL 1.1 specification](https://www.w3.org/TR/sparql11-query/#func-hash) are supported:

| SPARQL name | Java name | Notes |
|-------------|-----------|-------|
| MD5 | MD5 | Weak — vulnerable to collision attacks. Avoid for security-sensitive use. |
| SHA1 | SHA-1 | Weak — deprecated for most security purposes. |
| SHA256 | SHA-256 | Recommended default. |
| SHA384 | SHA-384 | Stronger than SHA-256. |
| SHA512 | SHA-512 | Strongest in the SPARQL set. |

Additional algorithms available on the JVM are also accepted. The full list is JVM-dependent and visible in the algorithm parameter dropdown.

Note that the Java names use hyphens (SHA-256, SHA-1) where SPARQL uses none (SHA256, SHA1). Both forms are accepted by this operator.

## Contrast with Combined input hash

The **Combined input hash** operator feeds all values from all ports into a single hash function and returns one hash regardless of input size. Use it when you need a single fingerprint for a set of values taken together.

Use **Per-value hash** when each value needs its own hash — for example, to hash a column of URIs independently, or to replicate `SHA256(?x)` in SPARQL.

## Examples

**Notation:** List of values are represented via square brackets. Example: `[first, second]` represents a list of two values "first" and "second".

---
**Single value produces one SHA-256 hash:**

* Input values:
    1. `[input value]`

* Returns: `[f708c2afff0ed197e8551c4dd549ee5b848e0b407106cbdb8e451c8cd1479362]`


---
**Two values in, two independent hashes out — one per value, not a combined hash:**

* Input values:
    1. `[apple, banana]`

* Returns: `[3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b, b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e]`


---
**The algorithm parameter selects the hash function (MD5), single value:**

* Parameters
    * algorithm: `MD5`

* Input values:
    1. `[apple]`

* Returns: `[1f3870be274f6c49b3e31a0c6728957f]`


---
**The algorithm parameter selects the hash function (MD5), multiple values:**

* Parameters
    * algorithm: `MD5`

* Input values:
    1. `[apple, banana]`

* Returns: `[1f3870be274f6c49b3e31a0c6728957f, 72b302bf297a228a75730123efef7c41]`


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
**Empty input produces empty output:**

* Input values:
    1. `[]`

* Returns: `[]`


---
**Two input ports causes IllegalArgumentException:**

* Input values:
    1. `[foo]`
    2. `[bar]`

* Returns: `[]`
* **Throws error:** `IllegalArgumentException`


---
**Invalid algorithm name causes NoSuchAlgorithmException:**

* Parameters
    * algorithm: `NONEXISTENT`

* Input values:
    1. `[foo]`

* Returns: `[]`
* **Throws error:** `NoSuchAlgorithmException`


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

* [inputHash](inputHash.md) — The Combined input hash plugin produces one combined hash for all input values. The Per-value hash plugin instead hashes each value independently, preserving cardinality.
