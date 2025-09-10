---
title: "UUID Convert"
description: "Convert a UUID string representation"
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# UUID Convert
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

Convert a UUID string with 32 hexadecimal digits to a 16-byte
    string containing the six integer fields in big-endian byte order, a 16-byte string
    the six integer fields in little-endian byte order, a 32-character lowercase
    hexadecimal string, a 128-bit integer, or a URN. Strings in the correct format,
    however, the log will show a warning if the input does not comply with the standard
    specified in RFC 4122 and the proposed updates

## Parameter

### From

Input string format

- ID: `from_format`
- Datatype: `string`
- Default Value: `uuid_hex`



### To

Output string format

- ID: `to_format`
- Datatype: `string`
- Default Value: `hex`





## Advanced Parameter

`None`