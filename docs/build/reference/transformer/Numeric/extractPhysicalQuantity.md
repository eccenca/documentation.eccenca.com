---
title: "Extract physical quantity"
description: "Extracts physical quantities, such as length or weight values. Values are expected to be formatted as `{Number}{UnitPrefix}{Symbol}` and are converted to the base unit."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Extract physical quantity
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Extracts physical quantities, such as length or weight values.
Values are expected of the form `{Number}{UnitPrefix}{Symbol}` and are converted to the base unit.

Example: Let a value such as `"10km, 3mg"`, containing both a distance and a weight, be given. If the `symbol` parameter is set to `m`, then the extracted value will be `1000` (i.e. the distance). If, instead, the `symbol` parameter is set to `g`, then the extracted value will be `0.001` (i.e. the weight).


## Parameter

### Symbol

The symbol of the dimension, e.g., 'm' for meter.

- ID: `symbol`
- Datatype: `string`
- Default Value: `None`



### Number format

The IETF BCP 47 language tag, e.g. 'en'.

- ID: `numberFormat`
- Datatype: `string`
- Default Value: `en`



### Filter

Only extracts from values that contain the given regex (case-insensitive).

- ID: `filter`
- Datatype: `string`
- Default Value: `None`



### Index

If there are multiple matches, retrieve the value with the given index (zero-based).

- ID: `index`
- Datatype: `int`
- Default Value: `0`





## Advanced Parameter

`None`