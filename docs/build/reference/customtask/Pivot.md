---
title: "Pivot"
description: "The pivot operator takes data in separate rows, aggregates it and converts it into columns."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Pivot

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The pivot operator takes data in separate rows, aggregates it and converts it into columns.

The operator works on a flat input schema only and creates a flat output schema.

A pivot table is a data summarization that is used to automatically sort, count, total,
or average data in a dataset.
It allows you to view the data from a different perspective.

The following aggregation (summary) functions are available:

- **first** -  Shows the first value (works with numbers and strings)
- **min** - Shows the lowest value (works with numbers and strings)
- **max** - Shows the highest value (works with numbers and strings)
- **sum** - Adds up the values (works with numbers only)
- **average** - Finds the average of the values (works with numbers only)

## Parameter

### Pivot property

The pivot column refers to the column in the input data that is used to organize the data along the horizontal axis of the pivot table.

- ID: `pivotProperty`
- Datatype: `string`
- Default Value: `None`

### First group property

The name of the first group column in the range. All columns starting with this will be grouped.

- ID: `firstGroupProperty`
- Datatype: `string`
- Default Value: `None`

### Last group property

The name of the last group column in the range. If left empty, only the first column is grouped.

- ID: `lastGroupProperty`
- Datatype: `string`
- Default Value: `None`

### Value property

The property that contains the grouped values that will be aggregated.

- ID: `valueProperty`
- Datatype: `string`
- Default Value: `None`

### Aggregation function

The aggregation function used to aggregate values.

- ID: `aggregationFunction`
- Datatype: `enumeration`
- Default Value: `sum`

### URI prefix

Prefix to prepend to all generated pivot columns.

- ID: `uriPrefix`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
