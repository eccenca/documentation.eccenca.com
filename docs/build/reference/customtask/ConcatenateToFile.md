---
title: "Concatenate to file"
description: "Concatenates values into a file."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Concatenate to file
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Concatenates values into a file.


## Parameter

### Path

Values from this path will be concatenated.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Mime type

MIME type of the output file.

- ID: `mimeType`
- Datatype: `string`
- Default Value: `None`



### Prefix

Prefix to be written before the first value.

- ID: `prefix`
- Datatype: `multiline string`
- Default Value: `None`



### Glue

Separator to be inserted between concatenated values.

- ID: `glue`
- Datatype: `multiline string`
- Default Value: `None`



### Suffix

Suffix to be written after the last value.

- ID: `suffix`
- Datatype: `multiline string`
- Default Value: `None`





## Advanced Parameter

### Charset

The file encoding.

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`



### File extension

File extension of the output file.

- ID: `fileExtension`
- Datatype: `string`
- Default Value: `.tmp`



