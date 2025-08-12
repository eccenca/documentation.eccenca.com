---
title: "Extract physical quantity"
description: "Extracts physical quantities, such as length or weight values. Values are expected of the form '{Number}{UnitPrefix}{Symbol}' and are converted to the base unit. Example: - Given a value '10km, 3mg'. - If the symbol parameter is set to 'm', the extracted value is 10000. - If the symbol parameter is set to 'g', the extracted value is 0.001."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Extract physical quantity
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Extracts physical quantities, such as length or weight values. Values are expected of the form '{Number}{UnitPrefix}{Symbol}' and are converted to the base unit. Example: - Given a value '10km, 3mg'. - If the symbol parameter is set to 'm', the extracted value is 10000. - If the symbol parameter is set to 'g', the extracted value is 0.001.

## Parameter

### Symbol

The symbol of the dimension, e.g., 'm' for meter.

- Datatype: `string`
- Default Value: `None`



### Number format

The IETF BCP 47 language tag, e.g. 'en'.

- Datatype: `string`
- Default Value: `en`



### Filter

Only extracts from values that contain the given regex (case-insensitive).

- Datatype: `string`
- Default Value: `None`



### Index

If there are multiple matches, retrieve the value with the given index (zero-based).

- Datatype: `int`
- Default Value: `0`



