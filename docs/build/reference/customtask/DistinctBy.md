---
title: "Distinct by"
description: "Removes duplicated entities based on user-defined paths. Duplicates can be resolved by keeping the first or last entity, or by keeping the entity with the minimum or maximum value of a compare path."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Distinct by

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## 1. Introduction

The **Distinct by** operator removes duplicated entities based on one or more user-defined paths.

All entities that share the same values at all **distinct paths** (one path per line) are considered duplicates of each other,
and exactly one of them is kept according to the chosen **duplicate resolution strategy**.

Note that this operator does not retain the order of the entities.

## 2. Duplicate Resolution Strategies

- **Keep first duplicate** – keeps the first entity encountered in the input.
- **Keep last duplicate** – keeps the last entity encountered in the input.
- **Keep duplicate with minimum value** – keeps the entity with the lowest value at the **compare path**.
- **Keep duplicate with maximum value** – keeps the entity with the highest value at the **compare path**.

The first and last strategies depend on the order of the input entities.
The minimum and maximum strategies are independent of the input order and follow these rules:

- Entities that have a value at the compare path win over entities that do not have one.
- If an entity has multiple values at the compare path, its lowest (minimum strategy) or highest (maximum strategy) value is used for comparison.
- On ties, the first encountered entity is kept.

## 3. Compare Order

The order used to compare values for the *Keep duplicate with minimum/maximum value* strategies can be configured:

- `Autodetect` (default) – if both values are numbers, numerical order is used; otherwise, alphabetical order is used.
- `Alphabetical` – values are always compared as strings.
- `Numerical` – values are compared as decimal numbers; values that cannot be parsed never win a comparison.
- `Integer` – values are compared as integers; values that cannot be parsed never win a comparison.

## 4. Example

Input:

| key | value |
|-----|-------|
| A   | 2     |
| A   | 1     |
| B   | 2     |
| A   | 3     |
| B   | 1     |

Configuration:

| Parameter          | Value                             |
|--------------------|-----------------------------------|
| Distinct paths     | `key`                             |
| Resolve duplicates | Keep duplicate with minimum value |
| Compare path       | `value`                           |
| Compare order      | Autodetect (default)              |

Output:

| key | value |
|-----|-------|
| A   | 1     |
| B   | 1     |

For each distinct `key`, only the entity with the lowest `value` is kept.

## 5. Connecting the Operator

Since this operator accepts a flexible input schema, it can only be connected to operators that provide a
non-flexible output schema or an explicit schema, such as CSV datasets, which can be connected directly.
For other inputs, a typical way to achieve this is to place a transform operator before it,
which produces a fixed output schema.

## 6. Technical Notes

- Entities are buffered in a temporary disk-based store, so the operator also works on datasets that do not fit into memory.


## Parameter

### Distinct paths

Entities that share the values of all these paths will be deduplicated. One path per line.

- ID: `distinctPath`
- Datatype: `multiline string`
- Default Value: `None`



### Resolve duplicates

Strategy to resolve duplicates.

- ID: `resolveDuplicates`
- Datatype: `enumeration`
- Default Value: `keepLast`



### Compare path

Path whose value decides which duplicate is kept for the 'Keep duplicate with minimum/maximum value' strategies. Ignored otherwise.

- ID: `comparePath`
- Datatype: `string`
- Default Value: `None`



### Compare order

Order used to compare values for the 'Keep duplicate with minimum/maximum value' strategies. Per default, if both values are numbers, numerical order is used for comparison. Otherwise, alphabetical order is used. Ignored for other strategies.

- ID: `order`
- Datatype: `enumeration`
- Default Value: `Autodetect`

## Advanced Parameter

`None`
