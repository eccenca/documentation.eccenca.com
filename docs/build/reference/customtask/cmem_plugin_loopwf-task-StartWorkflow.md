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

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Run another workflow once per incoming entity.

## Overview

- **Per-entity execution**: For every entity on the input port, this task starts one selected
  sub-workflow.
- **Execution modes**: Runs sequentially by default or in parallel with a configurable
  concurrency.
- **Input handover**: Each entity is converted to a JSON object and provided to the sub-workflow
  via its single replaceable (variable) input dataset.
- **Optional pass-through**: Optionally forwards the original input entities to the output port;
  it never returns results produced by the sub-workflow.
- **File support (beta)**: When processing file entities and a `input_mime_type` is set, the file
  content is sent to the sub-workflow instead of the file metadata.

## How It Works

1. Read entities from the single input port (flexible schema).
2. Convert each entity to a flat JSON object using the entity schema (one value per path required).
3. Start the chosen sub-workflow once per entity, supplying the JSON as the replaceable
   input dataset.
4. Run up to `parallel_execution` workflow instances at the same time.
5. Stop with an error if any sub-workflow fails; see details in Activities.

Example entity mapping (illustrative):
Input schema paths: `label`, `id`  → JSON payload: `{ "label": "Example", "id": "123" }`

## Requirements

- The selected workflow must be in the same project as this task.
- The selected workflow must have exactly one replaceable input dataset.
- The input entities must be flat: each schema path may have at most one value per entity.

## Limitations

- Nested or multi-valued entities are not supported; multiple values per path raise an error.
- The replaceable dataset of the sub-workflow must be a JSON dataset.
- No circular dependency detection is performed.
- File processing is beta; correct `input_mime_type` and a file-accepting dataset in the
  sub-workflow are required.

## Troubleshooting

- "Need a connected input task": Connect one upstream task to provide entities.
- "Can process a single input only": Only one input port is supported.
- "Multiple values for entity path": Ensure each path has at most one value.
- "Workflow ... does not exist ... or is missing a single replaceable input dataset": Select
  a workflow in the same project with exactly one variable input.

## Typical Use Cases

- Per-record processing pipelines (e.g., validation, enrichment, export).
- Batch operations that require complex per-entity logic encapsulated in a workflow.
- Quality checks where each entity must pass through a dedicated validation workflow.

## Parameter

### Workflow

Which workflow do you want to start per entity.

- ID: `workflow`
- Datatype: `string`
- Default Value: `None`

### How many workflow jobs should run in parallel?

- ID: `parallel_execution`
- Datatype: `Long`
- Default Value: `1`

### Forward incoming entities to the output port?

- ID: `forward_entities`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

### Mime-type for file by file processing (beta)

When working with file entities, setting this to a proper value will send the file to the workflow instead of the meta-data. Examples are: 'application/x-plugin-binaryFile', 'application/json', 'application/xml', 'text/csv', 'application/octet-stream' or 'application/x-plugin-excel'.

- ID: `input_mime_type`
- Datatype: `string`
- Default Value: `None`
