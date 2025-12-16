---
title: "UUID5"
description: "Generate a UUIDv5"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID5
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

UUID5 is based on the SHA1 hash of a namespace identifier (which
    is a UUID) and a name (which is a string).

## Parameter

### Namespace

If 'namespace' is not given, the input string is used.

- ID: `namespace`
- Datatype: `string`
- Default Value: `None`

### Namespace as UUID

Applies only if none of the pre-defined namespaces is selected. If enabled, the namespace string needs to be a valid UUID. Otherwise, the namespace UUID is a UUIDv1 derived from the SHA1 hash of the namespace string.

- ID: `namespace_as_uuid`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
