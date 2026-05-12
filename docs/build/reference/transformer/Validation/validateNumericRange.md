---
title: "Validate numeric range"
description: "Validates if a number is within a specified range."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Validate numeric range

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Validates if a number is within a specified range.


## Parameter

### Min

Minimum allowed number

- ID: `min`
- Datatype: `double`
- Default Value: `None`



### Max

Maximum allowed number

- ID: `max`
- Datatype: `double`
- Default Value: `None`

## Advanced Parameter

`None`

## Related Plugins

- **compareNumbers** — Validate numeric range either passes a number through or throws, producing no output on violation. Compare numbers always produces a 1 or 0 regardless of which side is larger, so the downstream pipeline continues in either case.
