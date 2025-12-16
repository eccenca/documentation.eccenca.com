---
title: "File hash"
description: "Calculates the hash sum of a file. The hash sum is cached so that subsequent calls to this operator are fast. Note that initially and every time the specified resource has been updated, this operator might take a long time (depending on the file size). This operator supports using different hash algorithms from the [Secure Hash Algorithms family](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (SHA, e.g. SHA256) and two algorithms from the [Message-Digest Algorithm family](https://en.wikipedia.org/wiki/MD5) (MD2 / MD5). Please be aware that some of these algorithms are not secure regarding collision- and other attacks. Note: This transform operator ignores any inputs."
icon: octicons/cross-reference-24
tags: 
    - TransformOperator
---
# File hash
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Calculates the hash sum of a file. The hash sum is cached so that subsequent calls to this operator are fast.
Note that initially and every time the specified resource has been updated, this operator might take a long time (depending on the file size).
This operator supports using different hash algorithms from the [Secure Hash Algorithms family](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (SHA, e.g. SHA256) and two algorithms from the [Message-Digest Algorithm family](https://en.wikipedia.org/wiki/MD5) (MD2 / MD5). Please be aware that some of these algorithms are not secure regarding collision- and other attacks.
Note: This transform operator ignores any inputs.

## Parameter

### File

File for which the hash sum will be calculated. If left empty, the file of the input dataset is used.

- ID: `file`
- Datatype: `resource`
- Default Value: `None`

### Algorithm

The hash algorithm to be used.

- ID: `algorithm`
- Datatype: `string`
- Default Value: `SHA256`

## Advanced Parameter

`None`
