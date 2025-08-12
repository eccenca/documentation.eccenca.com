---
title: "ULID"
description: "Generate ULID strings - Universally Unique Lexicographically Sortable Identifiers."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
    - PythonPlugin
---
# ULID
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).


ULID is a proposed identifier scheme, which produces time-based, random
and sortable strings. The following features are highlighted
[in the specification](https://github.com/ulid/spec):

- 128-bit compatibility with UUID
- 1.21e+24 unique ULIDs per millisecond
- Lexicographically sortable!
- Canonically encoded as a 26 character string, as opposed to the 36 character UUID
- Uses Crockford's base32 for better efficiency and readability (5 bits per character)
- Case insensitive
- No special characters (URL safe)
- Monotonic sort order (correctly detects and handles the same millisecond)

This transform plugin allows for creation of ULID based identifiers (plain or URN).
It does not support any input entities.


## Parameter

### Number of Values

Number of values to generate per entity.

- Datatype: `Long`
- Default Value: `1`



### Generate URNs

Generate 'urn:x-ulid:*' strings.

- Datatype: `boolean`
- Default Value: `false`



