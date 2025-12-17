---
title: "Get value by index"
description: "Returns the value found at the specified index. Fails or returns an empty result depending on failIfNoFound is set or not. Please be aware that this will work only if the data source supports some kind of ordering like XML or JSON. This is probably not a good idea to do with RDF models. If emptyStringToEmptyResult is true then instead of a result with an empty String, an empty result is returned."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
---

# Get value by index

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Returns the value found at the specified index. Fails or returns an empty result depending on failIfNoFound is set or not.
       Please be aware that this will work only if the data source supports some kind of ordering like XML or JSON. This
       is probably not a good idea to do with RDF models.

       If emptyStringToEmptyResult is true then instead of a result with an empty String, an empty result is returned.

## Parameter

### Index

No description

- ID: `index`
- Datatype: `int`
- Default Value: `None`

### Fail if not found

No description

- ID: `failIfNotFound`
- Datatype: `boolean`
- Default Value: `false`

### Empty string to empty result

No description

- ID: `emptyStringToEmptyResult`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
