---
title: "Strip non-alphabetic characters"
description: "Strips all non-alphabetic characters from a string. Spaces are retained."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Strip non-alphabetic characters

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Strips all non-alphabetic characters from a string. Spaces are retained.


## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

- **removeSpecialChars** — Strip non-alphabetic characters removes digits along with punctuation. Remove special chars keeps digits but does not preserve spaces. When numeric content in the string needs to survive, Remove special chars is the applicable plugin.
- **normalizeChars** — Strip non-alphabetic characters removes digits and punctuation but does not normalize the letters it keeps; a diacritical letter in the input is a diacritical letter in the output. Normalize chars addresses that: it converts diacritical characters to ASCII equivalents, though it does not strip any content.
