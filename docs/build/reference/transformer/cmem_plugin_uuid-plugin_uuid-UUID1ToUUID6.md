---
title: "UUID1 to UUID6"
description: "Generate UUIDv6 from a UUIDv1."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID1 to UUID6
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).


UUIDv6 is a field-compatible version of UUIDv1, reordered for
improved DB locality. It is expected that UUIDv6 will primarily be
used in contexts where there are existing v1 UUIDs. Systems that do
not involve legacy UUIDv1 SHOULD consider using UUIDv7 instead.


## Parameter

`None`