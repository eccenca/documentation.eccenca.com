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

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

Combines CSV files with the same structure to one dataset.
                     Files are identified by specifying a regex filter.

## Parameter

### File name regex filter

Regular expression for filtering resources of the project.

- Datatype: `string`
- Default Value: `None`



### Delimiter

Delimiter in the input CSV files.

- Datatype: `string`
- Default Value: `,`



### Quotechar

Quotechar in the input CSV files.

- Datatype: `string`
- Default Value: `"`



### Skip rows

The number of rows to skip before the header row.

- Datatype: `Long`
- Default Value: `0`



### Stop workflow if result is empty

Stop the workflow if no input files are found or all input files are empty.

- Datatype: `boolean`
- Default Value: `true`



