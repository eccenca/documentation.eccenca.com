---
title: "Lower than"
description: "Checks if the source value is lower than the target value."
icon: octicons/cross-reference-24
tags: 
    - DistanceMeasure
---
# Lower than
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->




### Characteristics
This is a boolean distance measure, i.e., all distances are either 0 or 1.

Compares single values (as opposed to sequences of values). If multiple values are provided, all values are compared and the lowest distance is returned.

## Parameter

### Or equal

Accept equal values

- Datatype: `boolean`
- Default Value: `false`



### Order

Per default, if both strings are numbers, numerical order is used for comparison. Otherwise, alphanumerical order is used. Choose a more specific order for improved performance.

- Datatype: `enumeration`
- Default Value: `Autodetect`



### Reverse

Reverse source and target inputs

- Datatype: `boolean`
- Default Value: `false`



