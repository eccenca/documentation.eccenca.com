---
title: "Merge tables"
description: "Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Merge tables
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links.


## Parameter

### Multi table output

test

- ID: `multiTableOutput`
- Datatype: `boolean`
- Default Value: `true`



### Pivot table name

Name of the pivot table.

- ID: `pivotTableName`
- Datatype: `string`
- Default Value: `None`



### Mapping names

Name of the mapping tables. Comma separated list.

- ID: `mappingNames`
- Datatype: `string`
- Default Value: `None`



### Instance set names

Name of the tables joined to the pivot. Comma separated list.

- ID: `instanceSetNames`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`