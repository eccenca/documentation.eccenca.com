---
title: "Embedded Spark SQL view"
description: "Deprecated: Use the embedded SQL endpoint dataset instead."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Embedded Spark SQL view
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Deprecated: Use the embedded SQL endpoint dataset instead.

## Parameter

### View name

The name of the view. This specifies the table that can be queried by another virtual dataset or via JDBC (the 'default' schema is used for all virtual datasets).

- ID: `viewName`
- Datatype: `string`
- Default Value: `None`

### Query

Optional SQL query on the selected table. Has no effect when used as an output dataset.

- ID: `query`
- Datatype: `string`
- Default Value: `None`

### Cache

Optional boolean option that selects if the table should be cached by Spark or not (default = true).

- ID: `cache`
- Datatype: `boolean`
- Default Value: `true`

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

The source internal encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`

### Array separator

The character that is used to separate the parts of array values. Write "back slash t" to specify the tab character.

- ID: `arraySeparator`
- Datatype: `string`
- Default Value: `|`

### Compatibility

If true, basic types will be used for types that otherwise would result in client errors. This mainly that arrays will be stored as Strings separated by the separator defined above. If the view is only for use within a SparkContext, this can be set to false.

- ID: `useCompatibleTypes`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

`None`
