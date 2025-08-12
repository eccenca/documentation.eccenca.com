---
title: "Add project files"
description: "Adds file resources to the project that are piped into the input port."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Add project files
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Adds file resources to the project that are piped into the input port.


## Parameter

### File name

File name of the uploaded file(s). If multiple files are uploaded, an index will be appended to the file name. If left empty, the existing file names will be used.

- Datatype: `string`
- Default Value: `None`



### Directory

Directory to which the files should be written. If left empty, the files will be uploaded to the project root directory. Note that all files will be written to this directory even if they have been read from a different project directory initially.

- Datatype: `string`
- Default Value: `None`



### Overwrite strategy

The strategy to use if a file with the same name already exists.

- Datatype: `enumeration`
- Default Value: `fail`



