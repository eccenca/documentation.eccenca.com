---
title: "Avro"
description: "Read from or write to an Apache Avro file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Avro
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read from or write to an Apache Avro file. 


## Parameter

### File

Path (e.g. relative like 'path/filename.avro' or absolute 'hdfs:///path/filename.avro').

- ID: `file`
- Datatype: `resource`
- Default Value: `None`



### Uri pattern

A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property.

- ID: `uriPattern`
- Datatype: `string`
- Default Value: `None`



### Properties

Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line.

- ID: `properties`
- Datatype: `string`
- Default Value: `None`



### Charset

The file encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`





## Advanced Parameter

`None`