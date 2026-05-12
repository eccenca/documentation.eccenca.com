---
title: "Remove special chars"
description: "Remove special characters (including punctuation) from a string."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Remove special chars

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Remove special characters (including punctuation) from a string.


## Parameter

`None`

## Advanced Parameter

`None`

## Related Plugins

- **normalizeChars** — Remove special chars keeps diacritical characters intact: because they qualify as Unicode letters, they are neither removed nor modified. Normalize chars is the right choice when diacritics need to be converted to their ASCII base forms rather than preserved as-is.
- **alphaReduce** — The two plugins differ on digits and spaces: Remove special chars keeps digits and removes spaces; Strip non-alphabetic characters removes digits and keeps spaces. Strip non-alphabetic characters is the right tool when word spacing matters and digits do not belong in the output.
