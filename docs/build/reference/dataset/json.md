---
title: "JSON"
description: "Read from or write to a JSON or JSON Lines file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# JSON
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Typically, this dataset is used to transform an JSON file to another format, e.g., to RDF.

### Reading

In addition to plain JSON files, *JSON Lines* files can also be read.

For reading, the JSON dataset supports a number of special paths:
- `#id` Is a special syntax for generating an id for a selected element. It can be used in URI patterns for entities which do not provide an identifier. Examples: `http://example.org/{#id}` or `http://example.org/{/pathToEntity/#id}`.
- `#text` retrieves the text of the selected node.
- The backslash can be used to navigate to the parent JSON node, e.g., `\parent/key`. The name of the backslash key (here `parent`) is ignored.

### Writing

When writing JSON, all entities need to possess a unique URI. Writing multiple root entities with the same URI will result in multiple entries in the generated JSON. If multiple nested entities with the same URI are written, only the last entity with a given URI will be written.


## Parameter

### File

JSON file. This may also be a zip archive of multiple JSON files that share the same schema.

- Datatype: `resource`
- Default Value: `None`



### Template

Template for writing JSON. The term {{output}} will be replaced by the written JSON.

- Datatype: `code-json`
- Default Value: `{{output}}`



### Navigate into arrays

Navigate into arrays automatically. If set to false, the `#array` path operator must be used to navigate into arrays.

- Datatype: `boolean`
- Default Value: `true`



### Base path

The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read.

- Datatype: `string`
- Default Value: `None`



### URI pattern (deprecated)

A URI pattern, e.g., http://namespace.org/{ID}, where {path} may contain relative paths to elements

- Datatype: `string`
- Default Value: `None`



### Max depth

Maximum depth of written JSON. This acts as a safe guard if a recursive structure is written.

- Datatype: `int`
- Default Value: `15`



### Streaming

Streaming allows for reading large JSON files. If streaming is enabled, backward paths are not supported.

- Datatype: `boolean`
- Default Value: `true`



### ZIP file regex

If the input resource is a ZIP file, files inside the file are filtered via this regex.

- Datatype: `string`
- Default Value: `^(?!.*[\/\\]\..*$|^\..*$).*\.jsonl?$`



