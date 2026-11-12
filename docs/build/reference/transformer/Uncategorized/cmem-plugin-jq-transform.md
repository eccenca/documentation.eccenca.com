---
title: "jq"
description: "Process a JSON path with a jq filter / program."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
    - PythonPlugin
---

# jq

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This operator applies a jq filter to each value of a single input path and
emits the filter's result as the value on the operator's output path.

Exactly one input is required - the operator fails if it is connected to no
input path or to more than one. Each value of that path is passed to the
filter independently, so a multi-valued path produces one filter run, and one
output value, per input value.

A filter run can emit zero, one or several JSON values. If it emits exactly
one and **Output list with one item as string** is enabled (the default),
that single value is converted with Python's `str()`. For a plain JSON
string this yields the text unchanged, but for any other JSON type - numbers,
booleans, `null`, objects, arrays - it yields Python's own literal syntax
instead of JSON, for example `true` becomes `True` and `null` becomes `None`.
The same applies, regardless of the option, whenever a run emits zero or
several values: the operator then outputs the Python `str()` of the whole
result list. Filters that are expected to always return a single JSON string
are unaffected; filters that can return other types or a variable number of
results will need their output parsed back from this Python-literal form
downstream.

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

### Output list with one item as string

If enabled, a filter result of exactly one value is written as that value's Python string representation instead of as a one-element list. If disabled, or if the filter returns zero or several values, the whole result list is written the same way.

- ID: `single_item_as_string`
- Datatype: `boolean`
- Default Value: `true`
