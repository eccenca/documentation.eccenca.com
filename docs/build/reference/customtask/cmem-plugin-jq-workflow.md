---
title: "jq"
description: "Process a JSON document with a jq filter / program."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# jq

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task applies a jq filter to a JSON file and writes the transformed
result to a new JSON file.

Both the input and the output port carry a single file per entity. The input
file is read as JSON, transparently decompressing it first if it is
gzip-compressed. The output file is always plain (uncompressed) JSON, encoded
as UTF-8 and pretty-printed with two-space indentation.

The task is typically placed between two file-based tasks, for example
reading from a **JSON dataset** and writing to another one, so that the
filter output becomes the next task's input.

If the filter produces exactly one JSON value for a file, that value becomes
the file's entire content. If it produces zero or several values, the output
file instead contains a JSON array of all of them - so the shape of the
output can change from a single object to an array depending on how many
values the filter happens to emit. The whole input file is read into memory
before the filter runs, so very large files are not streamed. Cancelling the
containing workflow only takes effect between files, not while a file is
being transformed.

> [jq](https://jqlang.org/) is like sed for JSON data - you can use it to
> slice and filter and map and transform structured data with the same ease that sed, awk,
> grep and friends let you play with text.

In order to test jq expressions, you can use [play.jqlang.org](https://play.jqlang.org/).

## Basic concepts

- Filters separated by a comma will produce multiple independent outputs: `,`
- Will ignores error if the type is unexpected: `?`
- Array construction: `[]`
- Object construction: `{}`
- Concatenate or Add: `+`
- Difference of sets or Substract: `-`
- Size of selected element: `length`
- Pipes are used to chain commands in a similar fashion than bash: `|`

## Dealing with JSON objects

- Display all keys: `keys`
- Adds + 1 to all items: `map_values(.+1)`
- Delete a key: `del(.foo)`
- Convert an object to array:  `to_entries | map([.key, .value])`

## Dealing with fields

- Concatenate two fields: `fieldNew=.field1+' '+.field2`

## Dealing with arrays: Slicing and Filtering

- All: `.[]`
- First: `.[0]`
- Range: `.[2:4]`
- First 3: `.[:3]`
- Last 2: `.[-2:]`
- Before Last: `.[-2]`
- Select array of int by value: `map(select(. >= 2))`
- Select array of objects by value: `.[] &#124; select(.id == "second")`
- Select by type: `.[] | numbers`

Types can be `arrays`, `objects`, `iterables`, `booleans`, `numbers`, `normals`,
 `finites`, `strings`, `nulls`, `values` and `scalars`.

## Dealing with arrays: Mapping and Transforming

- Add + 1 to all items: `map(.+1)`
- Delete 2 items: `del(.[1, 2])`
- Concatenate arrays: `add`
- Flatten an array: `flatten`
- Create a range of numbers: `[range(2;4)]`
- Display the type of each item: `map(type)`
- Sort an array of basic type: `sort`
- Sort an array of objects: `sort_by(.foo)`
- Group by a key - opposite to flatten: `group_by(.foo)`
- Minimum value of an array: `min` (see also  `max`, `min_by(path_exp)`, `max_by(path_exp)`)
- Remove duplicates: `unique` or `unique_by(.foo)` or `unique_by(length)`
- Reverse an array: `reverse`



## Parameter

### jq Expression

The jq program to apply to the input JSON string.

- ID: `jq_expression`
- Datatype: `string`
- Default Value: `.`

## Advanced Parameter

### Validation source

Example JSON used by the Validate expression action to preview the filter's output before running the task. Leave empty to skip the preview.

- ID: `validation_source`
- Datatype: `code-json`
- Default Value: `None`
