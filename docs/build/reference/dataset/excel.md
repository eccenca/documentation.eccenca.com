---
title: "Excel"
description: "Read from or write to an Excel workbook in Open XML format (XLSX)."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Excel
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read from or write to an Excel workbook in Open XML format (XLSX).


## Parameter

### File

File name inside the resources directory.

- Datatype: `resource`
- Default Value: `None`



### Streaming

Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption.

- Datatype: `boolean`
- Default Value: `true`



### Lines to skip

The number of lines to skip in the beginning when reading files.

- Datatype: `int`
- Default Value: `0`



### Has header

If true, the first line will be read as the table header, which defines the column names. If false, the first line will be read as data. In that case, the columns need to be adressed using #A, #B, etc.

- Datatype: `boolean`
- Default Value: `true`



### Output object values

Output results from object rules (URIs).

- Datatype: `boolean`
- Default Value: `true`



