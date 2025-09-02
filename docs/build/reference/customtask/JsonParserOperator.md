---
title: "Parse JSON"
description: "Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Parse JSON
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed.


## Parameter

### Input path

The Silk path expression of the input entity that contains the JSON document. If not set, the value of the first defined property will be taken.

- ID: `inputPath`
- Datatype: `string`
- Default Value: `None`



### Base path

The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read.

- ID: `basePath`
- Datatype: `string`
- Default Value: `None`



### URI suffix pattern

A URI pattern that is relative to the base URI of the input entity, e.g., /{ID}, where {path} may contain relative paths to elements. This relative part is appended to the input entity URI to construct the full URI pattern.

- ID: `uriSuffixPattern`
- Datatype: `string`
- Default Value: `None`



### Navigate into arrays

Navigate into arrays automatically. If set to false, the `#array` path operator must be used to navigate into arrays.

- ID: `navigateIntoArrays`
- Datatype: `boolean`
- Default Value: `true`





## Advanced Parameter

`None`