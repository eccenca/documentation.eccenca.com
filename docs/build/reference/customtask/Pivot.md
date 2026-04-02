---
title: "Pivot"
description: "The pivot operator takes data in separate rows, aggregates it and converts it into columns."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Pivot

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## 1. Introduction

### 1.1 What is Pivot?

The **Pivot** operator aggregates data from multiple rows and converts it into **columns**.

It takes:

- one or several contiguous **group columns** (e.g. `product`),
- a **pivot column** (e.g. `year`),
- a **value column** (e.g. `count`),

and produces a table where:

- each **group** (e.g. each product) becomes **one row**,
- each distinct value of the **pivot column** (e.g. `2014`, `2015`, `2016`) becomes a **separate column**,
- the **value column** is **aggregated** into those pivot cells (sum, average, min, max, first).

In other words:
> Pivot takes “tall” data (many rows per entity) and produces a “wide” summary table (one row per group, one column per pivot value).

### 1.2 When to use Pivot

Pivot is useful when:

- the input contains **multiple rows per entity** (e.g. one row per product per year),
- a **summary table** is needed with:
    - one row per group (product, product+region, …),
    - one column per value of a chosen dimension (years, categories, …),
- the values in one column should be **aggregated** into those summary cells.

The operator works on a **flat input schema** and creates a **flat output schema**.

---

## 2. Conceptual Overview

### 2.1 Tall → Wide

Input (tall):

| product_id      | product | year | count |
|-----------------|---------|------|-------|
| product1/2014   | Car     | 2014 | 100   |
| product1/2015a  | Car     | 2015 | 200   |
| product1/2015b  | Car     | 2015 | 300   |
| product1/2016   | Car     | 2016 | 300   |
| product2/2015   | Beer    | 2015 | 200   |
| product2/2016   | Beer    | 2016 | 300   |

Output (wide, with sum aggregation):

| product_id | product | 2014  | 2015  | 2016  |
|------------|---------|-------|-------|-------|
| product1   | Car     | 100.0 | 500.0 | 300.0 |
| product2   | Beer    |       | 200.0 | 300.0 |

- **Before**: many rows per product and year.
- **After**: one row per product, one column per year.

### 2.2 Group, Pivot, Value Columns

- **Group columns**:
    - define which rows belong to the same **group** (e.g. all rows for the same product),
    - all rows with identical group column values are aggregated into one output row.

- **Pivot column**:
    - determines **which columns** are created in the output,
    - each distinct value of the pivot column (e.g. `2014`, `2015`, `2016`) becomes one output column.

- **Value column**:
    - contains the values to be **aggregated** into the pivot cells (e.g. counts, measures, totals).

Regarding the group columns, notice the following: The default is only one group column.
Multi-column grouping is possible in the form of a single contiguous range of group properties.
In a similar fashion, there is only one value column.

### 2.3 Aggregation

Within each group and pivot value:

- all value-column entries are collected, then
- an **aggregation function** is applied:

    - `first` – first value (works with numbers and strings),
    - `min` – smallest value (works with numbers and strings),
    - `max` – largest value (works with numbers and strings),
    - `sum` – sum of all values (numbers only),
    - `average` – arithmetic mean (numbers only).

In the example above, for product1, year 2015:

- values: `200`, `300`
- aggregation `sum` → `500.0`

If there is **no input row** for a particular (group, pivot) combination:

- the corresponding cell in the output table is **empty**.

---

## 3. Parameters

### 3.1 `pivotProperty` (required)

**Description**  
Property/path of the **pivot column** in the input data.

**Semantics**

- Distinct values in this column become **pivoted output columns**.
- Typical examples: `year`, `category`, `metric`.
- Only one column can function as a pivot.

**Example**

```text
pivotProperty = "year"
```

---

### 3.2 `firstGroupProperty` (required)

**Description**  
Name/path of the **first group column** in the range.

**Semantics**

- Defines the **start** of the **group column range**.
- All columns from `firstGroupProperty` up to `lastGroupProperty` (inclusive) are used as **grouping keys**. This is a single contiguous range of columns.
- If `lastGroupProperty` is empty, **only this column** is used for grouping.

**Example**

```text
firstGroupProperty = "product"
```

---

### 3.3 `lastGroupProperty` (optional)

**Description**  
Name/path of the **last group column** in the range.

**Usage**

- If **empty**, only `firstGroupProperty` is used as group column.
- If **set**, all columns between `firstGroupProperty` and `lastGroupProperty` (inclusive), following schema order, are used as group columns.

**Examples**

```text
lastGroupProperty = "product"   # group by product only
lastGroupProperty = ""          # same effect: only first group column
lastGroupProperty = "region"    # group by product, ..., region (range)
```

---

### 3.4 `valueProperty` (required)

**Description**  
Property/path that contains the **values to be aggregated**.

**Semantics**

- All values in this column, for each (group, pivot) combination, are aggregated using `aggregationFunction`.
- Typical examples: `count`, `amount`, `measure`.

**Example**

```text
valueProperty = "count"
```

---

### 3.5 `aggregationFunction` (optional)

**Description**  
Aggregation function applied to the values in `valueProperty` for each (group, pivot) combination.

**Default**

```text
aggregationFunction = sum
```

**Available functions**

- `first` – first value (works with numbers and strings)
- `min` – lowest value (numbers or strings, according to ordering)
- `max` – highest value (numbers or strings, according to ordering)
- `sum` – sum of values (numbers only)
- `average` – average of values (numbers only)

---

### 3.6 `uriPrefix` (optional)

**Description**  
According to the plugin parameter description, this is a **prefix to prepend to all generated pivot columns**.

**Semantics visible in the code shown**

- The `LocalPivotOperatorExecutor` adjusts property URIs by removing an internal `GENERATED_FIELD_PREFIX` used by Spark, but does not reference `uriPrefix` directly.
- The concrete way in which `uriPrefix` is applied is handled in the Spark-based executor (`SparkPivotOperatorExecutor`), which is not included in the code snippets here.

---

## 4. Behaviour in Detail

### 4.1 Input Assumptions

- Exactly **one input table** is expected.
- The input schema is **flat** (no nested paths).
- The operator effectively behaves as:
    - group-by over the group columns, then
    - pivot on `pivotProperty` values, aggregating `valueProperty`.

### 4.2 Group Column Selection

Group columns are determined as follows:

1. Locate `firstGroupProperty` in the input schema.
2. If `lastGroupProperty` is **empty**:
    - use only `firstGroupProperty` as group column.
3. If `lastGroupProperty` is **set**:
    - locate `lastGroupProperty` in the schema,
    - use the **inclusive range** of columns from `firstGroupProperty` to `lastGroupProperty`.

All these columns together define the group key.

### 4.3 Pivot Column Creation

For each distinct value of `pivotProperty` in the input:

- a pivot column is created in the output schema.
- The order of pivot columns is determined by the underlying Spark executor.

New pivot columns:

- are added **after** the group columns,
- have property URIs supplied by the Spark-based executor.
- The local executor removes an internal generated-field prefix from these URIs before returning the result.

### 4.4 Output Schema Structure

The output schema is flat and structured as:

```text
[ group columns …, pivotValue1, pivotValue2, pivotValue3, … ]
```

Example matching the test:

- group columns: `product`
- pivot values: `2014`, `2015`, `2016`
- output columns: `product`, `2014`, `2015`, `2016`

### 4.5 Row Aggregation and Cell Filling

For each combination of:

- group key (values of the group columns), and
- pivot value (value of `pivotProperty`),

the operator:

1. collects all rows that share this (group, pivot) pair,
2. extracts the values from `valueProperty`,
3. applies `aggregationFunction`,
4. writes the result into the corresponding pivot cell.

If no row exists for a particular (group, pivot) combination:

- the corresponding cell in the output row remains **empty**.

Example (from the test):

- Input rows for product1, year 2015 have counts `200` and `300`.
- With `sum`:
    - output cell at (product1, column `2015`) = `500.0`.
- There is no row for product2, year 2014:
    - output cell at (product2, column `2014`) is empty.

### 4.6 Output URIs

Output entity URIs typically represent the **group** (e.g. product), not individual input rows.

In the example:

- input URIs: `product1/2014`, `product1/2015a`, `product1/2015b`, …
- output URIs: `product1`, `product2`.

The pivot operation thus collapses multiple input URIs into one output URI per group.

---

## 5. Example

### 5.1 Simple Example

**Input schema**

Columns:

- `product`, `year`, `count`

**Input data**

| product_id     | product | year | count |
| -------------- | ------- | ---- | ----- |
| product1/2014  | Car     | 2014 | 100   |
| product1/2015a | Car     | 2015 | 200   |
| product1/2015b | Car     | 2015 | 300   |
| product1/2016  | Car     | 2016 | 300   |
| product2/2015  | Beer    | 2015 | 200   |
| product2/2016  | Beer    | 2016 | 300   |

**Configuration**

```text
pivotProperty       = "year"
firstGroupProperty  = "product"
lastGroupProperty   = "product"  # group only by product
valueProperty       = "count"
aggregationFunction = sum        # default
uriPrefix           = ""         # default
```

**Output schema**

Columns:

- `product`, `2014`, `2015`, `2016`

**Output data**

| product_id | product | 2014  | 2015  | 2016  |
|------------|---------|-------|-------|-------|
| product1   | Car     | 100.0 | 500.0 | 300.0 |
| product2   | Beer    |       | 200.0 | 300.0 |

Notes:

- For product1, year 2015: `200 + 300 = 500.0`.
- For product2, year 2014: no rows → empty cell.
- Group column `product` is preserved in the output.
- One output row is created per distinct group value (`product1`, `product2`).

---

## 6. Usage Patterns & Recommendations

### 6.1 When to Use Pivot

Typical use cases:

- Undoing a previous **Unpivot** step, after aggregation or transformation.
- Building a compact **summary table** over time-series or categorical data.
- Converting tall, event-like data into a wide format required by downstream tools.

### 6.2 Choosing Group Columns

- Use **one group column** (only `firstGroupProperty`, `lastGroupProperty` empty or equal) when:
    - the grouping key is a single dimension (product, id, …).

- Use a **range of group columns** when:
    - the grouping key should be composite (e.g. product + region + category),
    - the schema places these grouping columns in a contiguous block.

### 6.3 Choosing the Aggregation Function

- `sum` / `average`:
    - for numeric metrics (counts, amounts).
- `min` / `max`:
    - for numeric ranges or ordered string values.
- `first`:
    - when a representative or deterministic first value should be selected.

Choosing a function that does not match the underlying data type (e.g. `sum` on non-numeric data) is not meaningful and should be avoided.

### 6.4 Handling Missing Data

- Missing combinations of (group, pivot) result in **empty** cells.
- This is useful to distinguish “no data” from “zero” in numeric cases.
- Downstream processing should take these empty cells into account (e.g. defaulting where appropriate).

---

## 7. Technical Notes (for Power Users)

- Pivot operates on **flat schemas** and produces a **flat schema** with additional columns.
- New pivot columns are generated by the Spark-based executor based on distinct values of `pivotProperty`; their property URIs may contain an internal generated-field prefix that is removed again in the local executor.
- The `uriPrefix` parameter is available for controlling the URIs of generated pivot columns, but its concrete effect is implemented in the Spark executor, which is not shown here.
- Column value types for pivoted columns are typically numeric for numeric aggregations, but may be represented as strings; downstream components may need to re-interpret or cast them.

---

## 8. Relation to the Unpivot Operator

The **Pivot** and **Unpivot** operators are structurally complementary:

- **Pivot** takes a **tall** table with group columns, a pivot column, and a value column, and produces a **wide** summary table with one row per group and one column per pivot value (aggregated).
- **Unpivot** takes a **wide** table with many pivot columns and turns it into a **long** attribute–value table, with one row per (original row, pivot column, value).

In practice, they are often used together:

- Pivoted data can be **unpivoted** for normalization and flexible processing;
- attribute–value data can be **pivoted** back into wide summaries once aggregation is needed.

---

## 9. One-Paragraph Mental Model

> **Pivot** is a single-input operator that takes tall data with group columns, a pivot column, and a value column, and produces a wide summary table. For each group (defined by a range of group columns) and each distinct pivot value, it aggregates all values in the value column using a chosen aggregation function and writes the result into a pivoted output column named after the pivot value. The result is a flat table with one row per group and one column per pivot value, suitable for further processing, reporting, or as the structural counterpart of an Unpivot step.


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
