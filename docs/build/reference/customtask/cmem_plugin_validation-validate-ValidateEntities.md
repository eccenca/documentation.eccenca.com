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

## Input Modes

Entities arrive on the input port by default. Switching the input mode to a JSON dataset
removes the input port, and the resources to validate are instead read from a JSON dataset in
the project. A JSON array in that dataset has each of its objects validated individually; a
JSON object is validated directly.

### Output Modes

Valid JSON objects are sent to an output port by default, ready for further processing in the
workflow. Switching the output mode to a JSON dataset removes the output port, and the valid
JSON objects are instead saved to a JSON dataset in the project, replacing its existing content.

### Error Handling

Every entity or object is validated regardless of the outcome. The task can then either:

- Fail once validation completes if any entity has violations, halting the workflow.
- Report violations only as warnings, allowing follow-up tasks to run based on the
  validated data.

The error handling behavior is configurable through the **Fail on violations** parameter.


## Parameter

### Source / Input Mode

Selects where entities to validate come from: the input port or a JSON dataset.

- ID: `source_mode`
- Datatype: `string`
- Default Value: `entities`



### Target / Output Mode

Selects where valid JSON objects are written to: the output port or a JSON dataset.

- ID: `target_mode`
- Datatype: `string`
- Default Value: `entities`



### JSON Schema Dataset

This dataset holds the JSON schema to use for validation.

- ID: `json_schema_dataset`
- Datatype: `string`
- Default Value: `None`



### Fail on violations

If enabled, the workflow fails once validation completes if any entity has violations. All entities are validated either way; disabling this instead reports the violations as warnings.

- ID: `fail_on_violations`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Source JSON Dataset

This dataset holds the resources you want to validate. Required when Source / Input Mode is set to dataset; leave it empty when using entities.

- ID: `source_dataset`
- Datatype: `string`
- Default Value: `None`



### Target JSON Dataset

This dataset stores the valid JSON objects after validation, replacing any existing content. Required when Target / Output Mode is set to dataset; leave it empty when using entities.

- ID: `target_dataset`
- Datatype: `string`
- Default Value: `None`
