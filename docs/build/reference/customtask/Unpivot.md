---
title: "Unpivot"
description: "Given a list of table columns, transforms those columns into attribute-value pairs."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Unpivot
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## 1. Introduction

### 1.1 What is Unpivot?

The **Unpivot** operator transforms a single, wide table into a **long, attribute–value table**.

It takes several **pivot columns** (e.g. `2014`, `2015`, `2016`) and converts them into **multiple rows**, each row containing:

- the original **non-pivot** columns (e.g. `product`),
- an **attribute** column indicating *which* pivot column the value came from,
- a **value** column containing the cell value itself.

In other words:
> Per input row, Unpivot takes the “list” of values in the pivot columns and turns it into a **series of key–value entries**, one per output row.

### 1.2 When to use Unpivot

Unpivot is useful when:

- there are many **similar columns** (e.g. one column per year, month, category, metric variant),
- a uniform, long table is preferred, where each row is **(dimension, value)** instead of “one row with many semi-redundant columns”,
- all such columns should be processed in the same way downstream and a single attribute/value pair is preferable to many separate columns.

---

## 2. Conceptual Overview

### 2.1 Wide → Long

Input (wide):

| product | 2014 | 2015 | 2016 |
|---------|------|------|------|
| Car     | 100  | 200  | 300  |

Output (long):

| product | attribute | value |
|---------|----------|-------|
| Car     | 2014     | 100   |
| Car     | 2015     | 200   |
| Car     | 2016     | 300   |

- **Before**: 1 row with 3 pivot columns.
- **After**: 3 rows, each with `attribute` and `value`.

### 2.2 Pivot vs Non-pivot Columns

- **Pivot columns**: the columns to unpivot (e.g. `2014`, `2015`, `2016`).
- **Non-pivot columns**: all other columns (e.g. `product`) that are carried over and repeated in each unpivoted row.

### 2.3 Row Explosion

For each input row:

- the operator iterates over all **pivot columns**,
- for each pivot column:
    - it looks at the values in that cell (possibly multiple),
    - for each value, it generates **one output row**.

Thus:

> **Number of output rows per input row**  
> = sum over all pivot columns of (number of values in that cell).

Empty cells for a pivot column produce **no output row** for that column.

### 2.4 List → Map Mental Model

Per input row:

- the values in the pivot columns form a conceptual **map**:

  ```text
  2014 → 100
  2015 → 200
  2016 → 300
  ```

- Unpivot turns this map into a **sequence of key–value entries**, stored as **multiple rows**:

  ```text
  (attribute = 2014, value = 100)
  (attribute = 2015, value = 200)
  (attribute = 2016, value = 300)
  ```

The “map” is not stored as a single field; it is represented by these separate rows.

---

## 3. Parameters

### 3.1 `firstPivotProperty` (required)

**Description**  
The path/name of the **first pivot column** in the range.

**Usage**

- Used when `pivotColumns` is **empty**.
- Defines the **start** index of the pivot range in the input schema.

**Example**

```text
firstPivotProperty = "2014"
```

---

### 3.2 `lastPivotProperty` (optional)

**Description**  
The path/name of the **last pivot column** in the range.

**Usage**

- If left **empty**, all columns from `firstPivotProperty` to the **last column in the schema** are used as pivots.
- If set, the pivot range is **inclusive** from `firstPivotProperty` to `lastPivotProperty`.

**Examples**

```text
lastPivotProperty = "2016"  # Use 2014, 2015, 2016
lastPivotProperty = ""      # Use 2014 up to the last column in the schema
```

---

### 3.3 `pivotColumns` (optional)

**Description**  
A **comma-separated list** of pivot column names/paths.

**Usage**

- If non-empty, this list **overrides** the automatic range defined by `firstPivotProperty` and `lastPivotProperty`.
- Suitable when:
    - pivot columns are not contiguous in the schema, or
    - full control over which columns are used and in which order is desired.

**Example**

```text
pivotColumns = "2014,2015,2016"
```

**Precedence**

- If `pivotColumns` is non-empty → the operator uses this list and **ignores** the first/last range for pivot selection.
- If `pivotColumns` is empty → the operator uses the **range** defined by `firstPivotProperty` / `lastPivotProperty`.

---

### 3.4 `attributeProperty` (optional)

**Description**  
The path/name of the **output column** used to hold the **attribute**.

**Default**

```text
attributeProperty = "attribute"
```

**Semantics**

- Contains an **identifier of the pivot column** for this row.
- In the current implementation, this is the pivot column’s **property URI** as a string.

---

### 3.5 `valueProperty` (optional)

**Description**  
The path/name of the **output column** used to hold the **value**.

**Default**

```text
valueProperty = "value"
```

**Semantics**

- Contains the **cell value** from the pivot column for the entity.
- Stored as a **string** value.

---

### 3.6 Parameter Precedence Overview

- If `pivotColumns` is **non-empty**:
    - pivot columns are taken exactly from this list,
    - `firstPivotProperty` and `lastPivotProperty` are ignored for pivot selection.
- If `pivotColumns` is **empty**:
    - pivot columns are inferred from the range:
        - `firstPivotProperty` → start, and
        - `lastPivotProperty` → inclusive end, or last schema column if empty.

---

## 4. Behaviour in Detail

### 4.1 Pivot Column Selection Logic

Given the input schema:

1. If `pivotColumns` is **empty**:
    - find index of `firstPivotProperty` in the input schema,
    - if `lastPivotProperty` is **empty**:
        - pivot indices = from `firstPivotProperty` index to the **last** column index,
    - if `lastPivotProperty` is **set**:
        - find index of `lastPivotProperty`;
        - pivot indices = inclusive range from first to last.

2. If `pivotColumns` is **non-empty**:
    - split by comma, trim each entry,
    - for each name/path, look up its index in the input schema,
    - those indices become the **pivot columns**.

All remaining columns (not in `pivotIndices`) are the **non-pivot** columns.

---

### 4.2 Output Schema Construction

The output schema:

- keeps the same **type URI** as the input, and
- defines **columns** in this order:
    1. all **non-pivot columns**, in their original order, and
    2. one **attribute** column (`attributeProperty`, string), and
    3. one **value** column (`valueProperty`, string).

Thus the structure is:

```text
[ non-pivot columns …, attributeProperty, valueProperty ]
```

---

### 4.3 Entity / Row Transformation

For each input entity (row):

1. Iterate over each **pivot column index**.
2. For each pivot column:
    - evaluate the values in that cell (possibly multiple).
3. For each value:
    - create **one output entity** with:
        - non-pivot column values copied from the input,
        - `attributeProperty` = property URI of the pivot column (as string),
        - `valueProperty` = that cell value (as string).

If a pivot cell is **empty** (no value):

- no output entity is created for that (row, pivot) combination.

---

### 4.4 URI Rewriting

Each output entity gets a new **URI** that encodes the original entity plus the pivot column.

Conceptually:

```text
outputUri = originalUri + "/" + encoded(pivotColumnIdentifier)
```

Example:

- original URI: `product1`
- pivot column: `2014`
- output URI: `product1/2014`

This makes each unpivoted row identify the **original entity** and **which column** it came from.

---

### 4.5 Multi-valued Cells

If a pivot column can have **multiple values** for a given entity:

- each value becomes a **separate output row**.

Example (conceptual):

- input row: `product = Car`, `2015 = [200, 250]`
- output rows (for 2015):

  | product | attribute | value |
    |---------|----------|-------|
  | Car     | 2015     | 200   |
  | Car     | 2015     | 250   |

---

## 5. Examples

### 5.1 Simple Range-based Example

**Input schema**

Columns:

- `product`, `2014`, `2015`, `2016`

**Input data**

| uri      | product | 2014 | 2015 | 2016 |
|----------|---------|------|------|------|
| product1 | Car     | 100  | 200  | 300  |
| product2 | Beer    |      | 200  | 300  |

(Here `product2` has no value for `2014`.)

**Configuration**

```text
firstPivotProperty = "2014"
lastPivotProperty  = "2016"
pivotColumns       = ""         # use range
attributeProperty  = "attribute"
valueProperty      = "value"
```

**Output schema**

Columns:

- `product`, `attribute`, `value`

**Output data**

| uri           | product | attribute | value |
|---------------|---------|----------|-------|
| product1/2014 | Car     | 2014     | 100   |
| product1/2015 | Car     | 2015     | 200   |
| product1/2016 | Car     | 2016     | 300   |
| product2/2015 | Beer    | 2015     | 200   |
| product2/2016 | Beer    | 2016     | 300   |

Notes:

- `product2/2014` is **missing**, because the `2014` cell for `product2` was empty.
- Non-pivot column `product` is copied into every output row.
- `attribute` holds the pivot column identifier, `value` holds the cell value.

---

### 5.2 Open-ended Last Pivot

Same input as above.

**Configuration**

```text
firstPivotProperty = "2014"
lastPivotProperty  = ""         # empty → to last schema column
pivotColumns       = ""
```

Since `lastPivotProperty` is empty:

- the pivot range becomes `2014` → last column (`2016`),
- the result is identical to the previous example.

---

### 5.3 Explicit `pivotColumns` List

Same input as above.

**Configuration**

```text
firstPivotProperty = "2014"                  # ignored for pivot selection
lastPivotProperty  = "2016"                  # ignored if pivotColumns is set
pivotColumns       = "2014,2015,2016"
attributeProperty  = "attribute"
valueProperty      = "value"
```

Since `pivotColumns` is non-empty:

- the operator uses exactly `2014`, `2015`, `2016` as pivots,
- the output is again identical to the range-based examples.

This shows the three configurations are equivalent for this simple case.

---

## 6. Usage Patterns & Recommendations

### 6.1 Range vs Explicit List

- Use **range (`firstPivotProperty` / `lastPivotProperty`)** when:
    - pivot columns form a **contiguous block** in the schema,
    - “from here to there” behaviour is desired,
    - or “from here to the last column” is desired by leaving `lastPivotProperty` empty.

- Use **`pivotColumns`** when:
    - pivot columns are **not contiguous**,
    - a **subset** of them should be used, or
    - explicit control over **which columns and in which order** is needed.

### 6.2 Naming `attributeProperty` and `valueProperty`

- Domain-specific names for these columns can often improve clarity, such as:
    - `year` / `amount`,
    - `dimension` / `measure`,
    - `metric` / `value`.
- The defaults `attribute` / `value` are generic and suitable where no specific naming is required.

### 6.3 Things to Watch Out For

- If `firstPivotProperty` or `lastPivotProperty` do not match schema columns, no pivots will be found.
- If `pivotColumns` is set incorrectly (typos, wrong names), the corresponding columns will not be unpivoted.
- Empty cells in pivot columns **do not** produce rows: no value implies no key–value pair.
- The attribute column stores the pivot column’s **property URI**, not an arbitrary, independent label.

---

## 7. Technical Notes (for Power Users)

- The **attribute column** stores the pivot column’s **property URI** as a string.
- The **value column** is typed as **string**, regardless of the original type; downstream components may need to re-interpret or cast values.
- Output URIs follow the pattern:

  ```text
  <original URI>/<pivot-column-identifier>
  ```

  (internally URL-encoded where needed).

This makes it easy to trace each unpivoted row back to:

- the original entity, and
- the pivot column it came from.

---

## 8. One-Paragraph Mental Model

> **Unpivot** is a single-input operator that takes a group of “pivot” columns in a wide table and converts them into an attribute–value representation. For each input row and each selected pivot column (and each value in that cell), it creates one output row: non-pivot columns are copied, an attribute column records which pivot column this row represents (via its property URI), and a value column stores the cell’s value. URIs are rewritten to reflect the original entity plus the pivot column, and pivot columns can be defined either by a range (first/last) or by an explicit list.

---

## 9. Relation to the Pivot Operator

The **Pivot** and **Unpivot** operators are structurally complementary:

- **Unpivot** takes a **wide** table with many pivot columns and turns it into a **long** table with attribute–value pairs (one row per (original row, pivot column, value)).
- **Pivot** takes a **tall** table with group columns, a pivot column, and a value column and produces a **wide** summary table (one row per group, one column per pivot value, aggregated).

They are often used together in ETL pipelines:

- Unpivot a wide table to normalize structure,
- transform or filter the attribute–value data,
- optionally pivot the result back into a wide summary form using aggregation.


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