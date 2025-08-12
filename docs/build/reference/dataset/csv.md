---
title: "CSV"
description: "Read from or write to an CSV file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# CSV
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Read from or write to an CSV file.

## Parameter

### File

The CSV file. This may also be a zip archive of multiple CSV files that share the same schema.

- Datatype: `resource`
- Default Value: `None`



### Properties

Comma-separated list of properties. If not provided, the list of properties is read from the first line. Properties that are no valid (relative or absolute) URIs will be encoded.

- Datatype: `string`
- Default Value: `None`



### Separator

The character that is used to separate values. If not provided, defaults to ',', i.e., comma-separated values. "\t" for specifying tab-separated values, is also supported.

- Datatype: `string`
- Default Value: `,`



### Array separator

The character that is used to separate the parts of array values. Write "\t" to specify the tab character.

- Datatype: `string`
- Default Value: `None`



### Quote

Character used to quote values.

- Datatype: `string`
- Default Value: `"`



### URI pattern

*Deprecated* A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property.

- Datatype: `string`
- Default Value: `None`



### Charset

The file encoding, e.g., UTF-8, UTF-8-BOM, ISO-8859-1

- Datatype: `string`
- Default Value: `UTF-8`



### Regex filter

A regex filter used to match rows from the CSV file. If not set all the rows are used.

- Datatype: `string`
- Default Value: `None`



### Lines to skip

The number of lines to skip in the beginning, e.g. copyright, meta information etc.

- Datatype: `int`
- Default Value: `0`



### Max chars per column

The maximum characters per column. *Warning*: System will request heap memory of that size (2 bytes per character) when reading the CSV. If there are more characters found, the parser will fail.

- Datatype: `int`
- Default Value: `128000`



### Ignore bad lines

If set to true then the parser will ignore lines that have syntax errors or do not have to correct number of fields according to the current config.

- Datatype: `boolean`
- Default Value: `false`



### Quote escape character

Escape character to be used inside quotes, used to escape the quote character. It must also be used to escape itself, e.g. by doubling it, e.g. "". If left empty, it defaults to quote.

- Datatype: `string`
- Default Value: `"`



### ZIP file regex

If the input resource is a ZIP file, files inside the file are filtered via this regex.

- Datatype: `string`
- Default Value: `^(?!.*[\/\\]\..*$|^\..*$).*\.csv`



### Delete file before workflow execution

If set to true this will clear the specified file before executing a workflow that writes to it.

- Datatype: `boolean`
- Default Value: `false`



### Trim whitespace and non-printable characters.

If set to true, this will trim whitespace and non-printable characters from the contents of the CSV dataset.

- Datatype: `boolean`
- Default Value: `false`



