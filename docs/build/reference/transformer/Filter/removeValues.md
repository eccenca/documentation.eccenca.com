---
title: "Remove values"
description: "Removes values that contain words from a blacklist. The blacklist values are separated with commas."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Remove values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes values that contain words from a blacklist. The blacklist values are separated with commas.


## Parameter

### Blacklist

No description

- ID: `blacklist`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

- **removeEmptyValues** — Remove values works from a blacklist: any value matching a word in that list is dropped. Remove empty values has no such list; it removes only empty strings.
- **removeDuplicates** — The two plugins filter on different grounds. Remove values drops a value because of what it is; Remove duplicates drops a value because it already appeared earlier in the sequence.
