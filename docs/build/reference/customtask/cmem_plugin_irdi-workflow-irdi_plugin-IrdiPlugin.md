---
title: "Generate base36 IRDIs"
description: "Create unique ECLASS IRDIs."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Generate base36 IRDIs
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Create unique
[ECLASS](https://eclass.eu/support/technical-specification/structure-and-elements/irdi) IRDIs.

IRDIs are unique for each combination of (non-advanced) parameters.
If no input path is configured, values are read from the URIs of the input (Transformation Input).

- All fields of the IRDI are configurable, except `Item Code`, which is created by the plugin.
    - Created IRDIs are unique per configuration.
- Specify a graph that stores the state of Item Codes.
- Input and output paths are configurable.
    - if no input path is configured, values are read from the URIs of the input
    (transformation input).

## Parameter

### Counter graph

Graph in which the Item Code (IC) counter is stored

- ID: `graph`
- Datatype: `string`
- Default Value: `None`

### International Code Designator (ICD): Numeric, 4 characters

- ID: `icd`
- Datatype: `string`
- Default Value: `None`

### Organization Identifier (OI): Numeric, 4 characters

- ID: `oi`
- Datatype: `string`
- Default Value: `None`

### Organization Part Identifier (OPI): Alphanumeric, up to 35 characters (base36)

- ID: `opi`
- Datatype: `string`
- Default Value: `None`

### OPI Source Indicator (OPIS): Numeric, 1 character

- ID: `opis`
- Datatype: `string`
- Default Value: `None`

### Additional information (AI): Numeric, 4 characters

- ID: `ai`
- Datatype: `string`
- Default Value: `None`

### Code-space identifier (CSI): Alphanumeric, 2 character (base36)

- ID: `csi`
- Datatype: `string`
- Default Value: `None`

### Output path / property

Path or property that will connect input values and their generated IRDIs

- ID: `output_schema_path`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Counted object

The class of objects that are counted. (IRI)

- ID: `counted_object`
- Datatype: `string`
- Default Value: `None`

### Input Schema Path / Property

Path from which input values are taken. If empty, values are read from the URIs of the input

- ID: `input_schema_path`
- Datatype: `string`
- Default Value: `None`
