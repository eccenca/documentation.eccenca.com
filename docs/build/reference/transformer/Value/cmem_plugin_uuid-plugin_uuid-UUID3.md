---
title: "UUID3"
description: "Generate a UUIDv3"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID3
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

UUID3 is based on the MD5 hash of a namespace identifier (which
    is a UUID) and a name (which is a string).

## Parameter

### Namespace

The namespace.

- ID: `namespace`
- Datatype: `string`
- Default Value: `None`

### Namespace as UUID

Applies only if none of the pre-defined namespaces is selected. If enabled, the namespace string needs to be a valid UUID. Otherwise, the namespace UUID is a UUIDv1 derived from the MD5 hash of the namespace string.

- ID: `namespace_as_uuid`
- Datatype: `boolean`
- Default Value: `false`

## Advanced Parameter

`None`
