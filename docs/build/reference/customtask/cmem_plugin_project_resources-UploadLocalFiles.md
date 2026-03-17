---
title: "Upload local files"
description: "Replace a file dataset resource with a local file or upload multiple local files to a project."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Upload local files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This plugin allows you to upload multiple local files to the next workflow task.

Be aware that only file based datasets can handle file entities (e.g. JSON, CSV).

As an advanced option, you can change the working mode to UPLOAD_TO_PROJECT, which
allows for blindly adding files to the project space (with a consuming workflow task).
Make sure to use always use the preview function to avoid overloading you project.

## Parameter

### Directory

The local directory where the files are located.

- ID: `directory`
- Datatype: `string`
- Default Value: `None`

### File matching regex

The regex for filtering the file names. The regex needs to fully match the local name without directory.

- ID: `regex_string`
- Datatype: `string`
- Default Value: `.*`

## Advanced Parameter

### Working mode

Which activity should be done with the selected local files.

- ID: `working_mode`
- Datatype: `enumeration`
- Default Value: `SEND_TO_TASK`

