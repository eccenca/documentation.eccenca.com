---
title: "Parse XML"
description: "Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Parse XML
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities.


## Parameter

### Input path

The Silk path expression of the input entity that contains the XML document. If not set, the value of the first defined property will be taken.

- Datatype: `string`
- Default Value: `None`



### Base path

The path to the elements to be read, starting from the root element, e.g., '/Persons/Person'. If left empty, all direct children of the root element will be read.

- Datatype: `string`
- Default Value: `None`



### URI suffix pattern

A URI pattern that is relative to the base URI of the input entity, e.g., /{ID}, where {path} may contain relative paths to elements. This relative part is appended to the input entity URI to construct the full URI pattern.

- Datatype: `string`
- Default Value: `None`



