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

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task parses YAML content from multiple sources and converts it to various output
formats.

**Input Sources:**

- **entities**: Parse YAML from input port entities in a workflow
- **code**: Parse YAML from directly entered source code
- **file**: Parse YAML from uploaded project file resources

**Output Formats:**

- **entities**: Convert parsed structure to entities for workflow processing
- **json_entities**: Output as single JSON entity to the output port
- **json_dataset**: Save parsed structure directly to a JSON dataset

The plugin provides flexible YAML-to-JSON conversion with configurable input schema
types and paths for entity-based processing. It includes comprehensive validation and
error handling for all supported modes.

## Parameter

### Source / Input Mode

- ID: `source_mode`
- Datatype: `string`
- Default Value: `code`

### Target / Output Mode

- ID: `target_mode`
- Datatype: `string`
- Default Value: `entities`

### YAML Source Code (when using the *code* input)

- ID: `source_code`
- Datatype: `code-yaml`
- Default Value: `# Add your YAML code here (and select 'code' as input mode).`

## Advanced Parameter

### YAML File (when using the *file* input)

Which YAML file do you want to load into a JSON dataset? The dropdown shows file resources from the current project.

- ID: `source_file`
- Datatype: `string`
- Default Value: `None`

### Target Dataset

Where do you want to save the result of the conversion? The dropdown shows JSON datasets from the current project.

- ID: `target_dataset`
- Datatype: `string`
- Default Value: `None`

### Input Schema Type / Class

In case of source mode 'entities', you can specify the requested input type.

- ID: `input_schema_type`
- Datatype: `string`
- Default Value: `urn:x-eccenca:yaml-document`

### Input Schema Path / Property

In case of source mode 'entities', you can specify the requested input path.

- ID: `input_schema_path`
- Datatype: `string`
- Default Value: `text`

