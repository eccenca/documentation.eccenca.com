---
title: "UUID1"
description: "Generate a UUIDv1 from a host ID, sequence number, and the current time"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID1
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).


UUIDv1 is generated from a host ID, sequence number, and the current
time.



## Parameter

### Node (default: hardware address)

Node value in the form "01:23:45:67:89:AB", 01-23-45-67-89-AB", or "0123456789AB". If not given, it is attempted to obtain the hardware address. If this is unsuccessful, a random 48-bit number is chosen.

- Datatype: `string`
- Default Value: `None`



### Clock sequence (default: random)

If clock sequence is given, it is used as the sequence number. Otherwise a random 14-bit sequence number is chosen.

- Datatype: `string`
- Default Value: `None`



