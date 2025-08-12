---
title: "Start Workflow per Entity"
description: "Loop over the output of a task and start a sub-workflow for each entity."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Start Workflow per Entity
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

This workflow task operates on a list of incoming entities
and sequentially starts a single "inner" workflow for each entity.
In case one "inner" workflow fails, the execution is stopped with an error.
In this case the error message can be seen in the Activities view
(see `Execute with payload of [inner workflow name]`).

The started workflow needs to have a replaceable JSON dataset as input.

Current notes and limitations:

- The entities which are the input of the "inner" workflow can not be hierarchic.
- The replaceable dataset of the "inner" workflow needs to be a JSON dataset.
- There is no check for circles implemented!


## Parameter

### Workflow

Which workflow do you want to start per entity.

- Datatype: `string`
- Default Value: `None`



### How many workflow jobs should run in parallel?



- Datatype: `Long`
- Default Value: `1`



### Forward incoming entities to the output port?



- Datatype: `boolean`
- Default Value: `false`



### Mime-type for file by file processing (beta)

When working with file entities, setting this to a proper value will send the file to the workflow instead of the meta-data. Examples are: 'application/x-plugin-binaryFile', 'application/json', 'application/xml', 'text/csv', 'application/octet-stream' or 'application/x-plugin-excel'.

- Datatype: `string`
- Default Value: `None`



