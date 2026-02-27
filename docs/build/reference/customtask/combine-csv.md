---
title: "Combine CSV files"
description: "Combine CSV files with the same structure to one dataset."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Combine CSV files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Combines CSV files with the same structure to one dataset.
                     Files are identified by specifying a regex filter.

## Parameter

### File name regex filter

Regular expression for filtering resources of the project.

- ID: `regex`
- Datatype: `string`
- Default Value: `None`

### Delimiter

Delimiter in the input CSV files.

- ID: `delimiter`
- Datatype: `string`
- Default Value: `,`

### Quotechar

Quotechar in the input CSV files.

- ID: `quotechar`
- Datatype: `string`
- Default Value: `"`

### Skip rows

The number of rows to skip before the header row.

- ID: `skip_lines`
- Datatype: `Long`
- Default Value: `0`

### Stop workflow if result is empty

Stop the workflow if no input files are found or all input files are empty.

- ID: `stop`
- Datatype: `boolean`
- Default Value: `true`

## Advanced Parameter

`None`
