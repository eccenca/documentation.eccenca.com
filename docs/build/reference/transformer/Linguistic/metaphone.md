---
title: "Metaphone"
description: "Metaphone phonetic encoding."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Metaphone

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



This transformer plugin implements the **Metaphone** phonetic algorithm for indexing words according to English.

## Description

[Metaphone](https://en.wikipedia.org/wiki/Metaphone) is an algorithm which encodes words according to their English
pronunciation. This is also what other _phonetic algorithms_ such as Soundex do. Compared to Soundex, Metaphone's
algorithm contains a richer description of English spelling, leading to a better phonetic encoding of the input.

A description of the procedure can be found in the corresponding
[Wikipedia page](https://en.wikipedia.org/wiki/Metaphone#Procedure).

## Examples

We can get an idea of the output of the Metaphone algorithm using an online version of it such as the
[Metaphone Generator](https://en.toolpage.org/tool/metaphone).

Illustrative examples:

* `knuth` leads to the encoding `n0`.
* `school` is encoded as `skhl`.
* `encyclopedia` is encoded as `ensklpt`.
* `accuracy` is encoded as `akkrs`.
* `eccenca` is encoded as `eksnk`.


## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

* **soundex** — The Metaphone plugin returns a phonetic encoding whose length depends on the input. The Soundex plugin returns a fixed four-character code, so it forces a much coarser normalization. This is not a similarity score; it is an encoding step.
* **NYSIIS** — The Metaphone plugin and the NYSIIS plugin both produce phonetic encodings, but they do so under different encoding rules. The NYSIIS plugin also exposes a refined versus non-refined mode, while the Metaphone plugin has a single fixed encoding path.
