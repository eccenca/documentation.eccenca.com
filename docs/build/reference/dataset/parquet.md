---
title: "Parquet"
description: "Read from or write to an Apache Parquet file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Parquet
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read from or write to an Apache Parquet file.


## Parameter

### File

Path (e.g. relative like 'path/filename.orc' or absolute 'hdfs:///path/filename.parquet').

- Datatype: `resource`
- Default Value: `None`



### Uri pattern

A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property.

- Datatype: `string`
- Default Value: `None`



### Properties

Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line.

- Datatype: `string`
- Default Value: `None`



### Partition

Optional specification of the attribute for output partitioning

- Datatype: `string`
- Default Value: `None`



### Compression

Optional compression algorithm (e.g. snappy, zlib)

- Datatype: `string`
- Default Value: `None`



### Charset

The file encoding, e.g., UTF8, ISO-8859-1

- Datatype: `string`
- Default Value: `UTF-8`



