---
title: "Hive database"
description: "Read from or write to an embedded Apache Hive endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Hive database
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read from or write to an embedded Apache Hive endpoint.


## Parameter

### Schema

Name of the hive schema or namespace.

- Datatype: `string`
- Default Value: `None`



### Table

Name of the hive table.

- Datatype: `string`
- Default Value: `None`



### Query

Optional query for projection and selection (e.g. " SELECT * FROM table WHERE x = true".

- Datatype: `string`
- Default Value: `None`



### Uri pattern

A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property.

- Datatype: `string`
- Default Value: `None`



### Properties

Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line.

- Datatype: `string`
- Default Value: `None`



### Charset

The source internal encoding, e.g., UTF8, ISO-8859-1

- Datatype: `string`
- Default Value: `UTF-8`



