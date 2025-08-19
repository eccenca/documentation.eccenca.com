---
title: "Multi CSV ZIP"
description: "Reads from or writes to multiple CSV files from/to a single ZIP file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Multi CSV ZIP
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Reads from or writes to multiple CSV files from/to a single ZIP file.


## Parameter

### File

Zip file name inside the resources directory/repository.

- ID: `file`
- Datatype: `resource`
- Default Value: `None`



### Separator

The character that is used to separate values. If not provided, defaults to ',', i.e., comma-separated values. "\t" for specifying tab-separated values, is also supported.

- ID: `separator`
- Datatype: `string`
- Default Value: `,`



### Array separator

The character that is used to separate the parts of array values. Write "\t" to specify the tab character.

- ID: `arraySeparator`
- Datatype: `string`
- Default Value: `None`



### Quote

Character used to quote values.

- ID: `quote`
- Datatype: `string`
- Default Value: `"`



### Charset

The file encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`



### Lines to skip

The number of lines to skip in the beginning, e.g. copyright, meta information etc.

- ID: `linesToSkip`
- Datatype: `int`
- Default Value: `0`



### Max chars per column

The maximum characters per column. If there are more characters found, the parser will fail.

- ID: `maxCharsPerColumn`
- Datatype: `int`
- Default Value: `128000`



### Ignore bad lines

If set to true then the parser will ignore lines that have syntax errors or do not have to correct number of fields according to the current config.

- ID: `ignoreBadLines`
- Datatype: `boolean`
- Default Value: `false`



### Quote escape character

Escape character to be used inside quotes, used to escape the quote character. It must also be used to escape itself, e.g. by doubling it, e.g. "". If left empty, it defaults to quote.

- ID: `quoteEscapeCharacter`
- Datatype: `string`
- Default Value: `"`



### Append files

If 'True' then files in the ZIP archive are only added or updated, all other files in the ZIP stay untouched. If 'False' then a new ZIP file will be created on every dataset write.

- ID: `append`
- Datatype: `boolean`
- Default Value: `true`





## Advanced Parameter

### ZIP file regex

Filter file paths inside the ZIP file via this regex. By default sub folders or files not ending with .csv are ignored.

- ID: `zipFileRegex`
- Datatype: `string`
- Default Value: `^[^/]*\.csv$`



### Delete file before workflow execution

If set to true this will clear the specified file before executing a workflow that writes to it.

- ID: `clearBeforeExecution`
- Datatype: `boolean`
- Default Value: `true`



### Optionally trim whitespace and non-printable characters.

If set to true, this will trim whitespace and non-printable characters from the contents of the CSV dataset.

- ID: `trimWhitespaceAndNonPrintableCharacters`
- Datatype: `boolean`
- Default Value: `false`



