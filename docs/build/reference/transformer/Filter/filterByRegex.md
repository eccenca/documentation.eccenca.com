---
title: "Filter by regex"
description: "Removes all strings that do NOT match a regex. If 'negate' is true, only strings will be removed that match the regex."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Filter by regex

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Removes all strings that do NOT match a regex. If 'negate' is true, only strings will be removed that match the regex.


## Parameter

### Regex

No description

- ID: `regex`
- Datatype: `string`
- Default Value: `None`



### Negate

No description

- ID: `negate`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`

## Related Plugins

- **regexSelect** — Filter by regex keeps or drops values from the input sequence based on full-string matching. Regex selection keeps the checked value out of the output and instead returns a pattern-list-shaped result filled with the provided output value where a pattern matches.
