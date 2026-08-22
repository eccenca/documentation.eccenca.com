---
title: "Generate random values"
description: "Generates entities with random values."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Generate random values

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task generates entities with random values.

The plugin generates X entities with Y values, each value has a length of Z.

All parameters can be configured with the parameters.

Warning: Please note that high numbers in any of the parameters will result in more
computational time as well as disk usage to save the entities.
For example, while a configuration of 100 entities with 100 values / 100 characters
results in a 1.4 MB CSV file (which is generated in milliseconds),
a configuration of 1000 entities with 1000 values / 1000 characters will result
already in a 1.3 GB CSV file.


## Parameter

### Number of Entities (Rows)

How many rows will be created per run. Depending on your output dataset, this will result in different number of resources (Knowledge Graph),rows (CSV) or objects (JSON).

- ID: `number_of_entities`
- Datatype: `Long`
- Default Value: `10`



### Number of Values (Columns)

How many values are created per entity / row. Depending on your output dataset, this will result in different number of datatype properties (Knowledge Graph), columns (CSV) or attributes (JSON).

- ID: `number_of_values`
- Datatype: `Long`
- Default Value: `5`



### String Length

How long (in characters) should each value be.

- ID: `string_length`
- Datatype: `Long`
- Default Value: `16`

## Advanced Parameter

### Random Function



- ID: `random_function`
- Datatype: `string`
- Default Value: `token_urlsafe`



### Property Namespace

Output properties will have this namespace (following a number).

- ID: `property_namespace`
- Datatype: `string`
- Default Value: `https://example.org/vocab/RandomValuePath`



### Type Identifier

Output entities will have this type identifier (IRI).

- ID: `type_id`
- Datatype: `string`
- Default Value: `https://example.org/vocab/RandomValueRow`
