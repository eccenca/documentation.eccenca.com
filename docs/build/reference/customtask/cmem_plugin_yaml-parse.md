---
title: "Parse YAML"
description: "Parses files, source code or input values as YAML documents."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Parse YAML
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

This workflow task is basically a yaml2json command.

## Parameter

### Source / Input Mode



- Datatype: `string`
- Default Value: `code`



### Target / Output Mode



- Datatype: `string`
- Default Value: `entities`



### YAML Source Code (when using the *code* input)



- Datatype: `code-yaml`
- Default Value: `# Add your YAML code here (and select 'code' as input mode).`



### YAML File (when using the *file* input)

Which YAML file do you want to load into a JSON dataset? The dropdown shows file resources from the current project.

- Datatype: `string`
- Default Value: `None`



### Target Dataset

Where do you want to save the result of the conversion? The dropdown shows JSON datasets from the current project.

- Datatype: `string`
- Default Value: `None`



### Input Schema Type / Class

In case of source mode 'entities', you can specify the requested input type.

- Datatype: `string`
- Default Value: `urn:x-eccenca:yaml-document`



### Input Schema Path / Property

In case of source mode 'entities', you can specify the requested input path.

- Datatype: `string`
- Default Value: `text`



