---
title: "UUIDv8"
description: "Generate a UUIDv8 from three custom data fields (RFC 9562 §5.8)."
icon: octicons/cross-reference-24
tags:
    - TransformOperator
    - PythonPlugin
---

# UUIDv8

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

UUIDv8 is a free-form / experimental UUID format defined in
RFC 9562 §5.8. The 122 bits available outside the version and variant fields
are split into three custom data fields: 'a' (48 bits, octets 0-5), 'b' (12
bits, octets 6-7), and 'c' (62 bits, octets 8-15). When a field is left
empty, a random value is used.


## Parameter

### Custom data 'a' (default: random)

First 48-bit chunk of the UUID (octets 0-5) as a positive integer. If not given, a random value is used.

- ID: `a`
- Datatype: `string`
- Default Value: `None`



### Custom data 'b' (default: random)

Middle 12-bit chunk of the UUID (octets 6-7) as a positive integer. If not given, a random value is used.

- ID: `b`
- Datatype: `string`
- Default Value: `None`



### Custom data 'c' (default: random)

Last 62-bit chunk of the UUID (octets 8-15) as a positive integer. If not given, a random value is used.

- ID: `c`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
