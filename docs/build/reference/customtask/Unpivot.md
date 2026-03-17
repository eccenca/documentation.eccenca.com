---
title: "Unpivot"
description: "Given a list of table columns, transforms those columns into attribute-value pairs."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Unpivot

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Given a list of table columns, transforms those columns into attribute-value pairs.

## Parameter

### First pivot property

The name of the first pivot column in the range.

- ID: `firstPivotProperty`
- Datatype: `string`
- Default Value: `None`

### Last pivot property

the name of the last pivot column in the range. If left empty, all columns starting with the first pivot column are used.

- ID: `lastPivotProperty`
- Datatype: `string`
- Default Value: `None`

### Attribute property

The URI of the output column used to hold the attribute.

- ID: `attributeProperty`
- Datatype: `string`
- Default Value: `attribute`

### Value property

The URI of the output column used to hold the value.

- ID: `valueProperty`
- Datatype: `string`
- Default Value: `value`

### Pivot columns

Comma separated list of pivot column names. This property will override all inferred columns of the first two arguments.

- ID: `pivotColumns`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
