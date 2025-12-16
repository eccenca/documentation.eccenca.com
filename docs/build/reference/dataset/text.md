---
title: "Text"
description: "Reads and writes plain text files."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Text
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Reads and writes plain text files.

## Writing

All values of each entity will be written as plain text. Multiple values per entity are separated by spaces. Each entity will be written to a new line.

## Reading

The entire text will be read as a single entity with a single property. Note that even if multiple entities have been written to this dataset before, those would still be read back as a single entity. The default type is `document`, the default path is `text`. Both values can be configured in the advanced section.

## Parameter

### File

The plain text file. May also be a zip archive containing multiple text files.

- ID: `file`
- Datatype: `resource`
- Default Value: `None`

### Charset

The file encoding, e.g., UTF-8, UTF-8-BOM, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`

## Advanced Parameter

### Type name

A type name that represents this file.

- ID: `typeName`
- Datatype: `string`
- Default Value: `document`

### Property

The single property that holds the text.

- ID: `property`
- Datatype: `string`
- Default Value: `text`

### ZIP file regex

If the input resource is a ZIP file, files inside the file are filtered via this regex.

- ID: `zipFileRegex`
- Datatype: `string`
- Default Value: `.*`
