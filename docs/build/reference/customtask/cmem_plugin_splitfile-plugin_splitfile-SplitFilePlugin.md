---
title: "Split file"
description: "Split a file into multiple parts with a specified size."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Split file
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

A task splitting a text file into multiple parts with a specified size.

## Options

### Input filename

The input file to be split.  
_Example:_ An input file with the name _input.nt_ will be split into files with the names _input\_000000001.nt_,
_input\_000000002.nt_,   _input\_000000003.nt_, etc.  
⚠️ Existing files will be overwritten!

### Chunk size

The maximum size of the chunk files.

### Size unit

The unit of the size value: kilobyte (KB), megabyte (MB), gigabyte (GB), or number of lines (Lines).

### Delete input file

Delete the input file after splitting.

### Include header

Include the header in each split. The first line of the input file is treated as the header.

### Use internal projects directory

Use the internal projects directory of DataItegration to fetch and store files, instead of using the API.
If enabled, the "Internal projects directory" parameter has to be set.

### Internal projects directory

The path to the internal projects directory. If "Use internal projects directory" is disabled,
this parameter has no effect.


## Parameter

### Input filename

The input file to be split.

- Datatype: `string`
- Default Value: `None`



### Chunk size

The maximum size of the chunk files.

- Datatype: `double`
- Default Value: `None`



### Size unit

The unit of the size value: kilobyte (KB), megabyte (MB), gigabyte (GB), or number of lines (Lines).

- Datatype: `string`
- Default Value: `MB`



### Include header

Include the header in each split. The first line of the input file is treated as the header.

- Datatype: `boolean`
- Default Value: `false`



### Delete input file

Delete the input file after splitting.

- Datatype: `boolean`
- Default Value: `false`



### Use internal projects directory

Use the internal projects directory of DataIntegration to fetch and store files, instead of using the API. If enabled, the "Internal projects directory" parameter has to be set.

- Datatype: `boolean`
- Default Value: `false`



### Internal projects directory

The path to the internal projects directory. If "Use internal projects directory" is disabled, this parameter has no effect.

- Datatype: `string`
- Default Value: `/data/datalake`



