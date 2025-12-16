---
title: "Validate Entities"
description: "Use a JSON schema to validate entities or a JSON dataset."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Validate Entities
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

[JSON Schema](https://json-schema.org/) specifies a JSON-based format to
define the structure of JSON data for validation, documentation, and interaction control.
It provides a contract for the JSON data required by a given application.

This workflow task can validate incoming entities or a stand-alone JSON dataset by using a
JSON Schema specification.

The used JSON Schema needs to be provided as a JSON Dataset in the project.

### Input Modes

The plugin supports two input modes for validation:

1. **Validate Entities**: Validates entities received from the input port in the workflow.
2. **Validate JSON Dataset**: Validates a JSON dataset stored in the project.
   - If the JSON dataset is a JSON array, the schema will validate each object inside the array.
   - If the JSON dataset is a JSON object, it will be validated against the schema directly.

Validated data objects can be sent to an output port for further processing in the workflow
or saved in a JSON dataset in the project.

### Output Modes

1. **Valid JSON objects sent to Output Port**: Valid JSON objects can be sent as entities
   to the output port.
2. **Saved in JSON Dataset**: Valid JSON objects can be stored in a specified JSON dataset
   in the project.

### Error Handling

The task can either:

- Fail instantly if there is a data violation, halting the workflow.
- Provide warnings in the workflow report, allowing follow-up tasks to run based on the
  validated data.

The error handling behavior is configurable through the `Fail on violations` parameter.

## Parameter

### Source / Input Mode

- ID: `source_mode`
- Datatype: `string`
- Default Value: `entities`

### Target / Output Mode

- ID: `target_mode`
- Datatype: `string`
- Default Value: `entities`

### JSON Schema Dataset

This dataset holds the JSON schema to use for validation.

- ID: `json_schema_dataset`
- Datatype: `string`
- Default Value: `None`

### Fail on violations

If enabled, the task will fail on the first data violation.

- ID: `fail_on_violations`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Source JSON Dataset

This dataset holds the resources you want to validate.

- ID: `source_dataset`
- Datatype: `string`
- Default Value: `None`

### Target JSON Dataset

This dataset will be used to store the valid JSON objects after validation.

- ID: `target_dataset`
- Datatype: `string`
- Default Value: `None`
