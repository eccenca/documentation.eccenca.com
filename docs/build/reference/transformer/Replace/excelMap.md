---
title: "Excel map"
description: "Replaces values based on a map of values read from a file in Open XML format (XLSX). The XLSX file may contain several sheets of the form: mapFrom,mapTo <source string>,<target string> ... and more An empty string can be created in Excel and alternatives by inserting ='' in the input line of a cell. If there are multiple values for a single key, all values will be returned for the given key. Note that the mapping table will be cached in memory. If the Excel file is updated (even while transforming), the map will be reloaded within seconds."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# Excel map
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Replaces values based on a map of values read from a file in Open XML format (XLSX).
The XLSX file may contain several sheets of the form:

mapFrom,mapTo
<source string>,<target string>
... and more

An empty string can be created in Excel and alternatives by inserting ="" in the input line of a cell.

If there are multiple values for a single key, all values will be returned for the given key.

Note that the mapping table will be cached in memory. If the Excel file is updated (even while transforming), the map will be reloaded within seconds.
    


## Parameter

### Excel file

Excel file inside the resources directory containing one or more sheets with mapping tables.

- Datatype: `resource`
- Default Value: `None`



### Sheet name

The sheet that contains the mapping table or empty if the first sheet should be taken.

- Datatype: `string`
- Default Value: `None`



### Skip lines

How many rows to skip before reading the mapping table. By default the expected header row is skipped.

- Datatype: `int`
- Default Value: `1`



### Strict

If set to true, the operator throws validation errors for values it cannot map. If set to false, the chosen conflict strategy will be applied for missing values.

- Datatype: `boolean`
- Default Value: `true`



### Conflict strategy

Determines how values that cannot be found in the mapping table are treated. Only has an effect if 'strict' is set to false. If 'retain' is chosen, the original value will be forwarded. If 'remove' is chosen, no value will be output.

- Datatype: `enumeration`
- Default Value: `retain`



