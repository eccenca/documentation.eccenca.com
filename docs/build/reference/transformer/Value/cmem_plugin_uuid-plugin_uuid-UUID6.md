---
title: "UUID6"
description: "Generate a UUIDv6 from a host ID, sequence number, and the current time"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID6
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


UUIDv6 is generated from a host ID, sequence number, and the current
time.

UUIDv6 is a field-compatible version of UUIDv1, reordered for
improved DB locality. It is expected that UUIDv6 will primarily be
used in contexts where there are existing v1 UUIDs. Systems that do
not involve legacy UUIDv1 SHOULD consider using UUIDv7 instead.


## Parameter

### Node (default: hardware address)

Node value in the form "01:23:45:67:89:AB", 01-23-45-67-89-AB", or "0123456789AB". If not given, a random 48-bit number is chosen.

- ID: `node`
- Datatype: `string`
- Default Value: `None`



### Clock sequence (default: random)

If clock sequence is given, it is used as the sequence number. Otherwise a random 14-bit number is chosen.

- ID: `clock_seq`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

`None`