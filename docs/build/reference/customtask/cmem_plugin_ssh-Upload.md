---
title: "Upload SSH files"
description: "Upload files to a given SSH instance."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Upload SSH files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task uploads files to a given SSH instance.

By providing the hostname, username, port and authentication method, you can specify the
folder the data should be uploaded to.

## Authentication Methods

- **Password:** Only the password will be used for authentication. The private key field is
ignored, even if filled.
- **Key:** The private key will be used for authentication. If the key is encrypted, the password
will be used to decrypt it.

### Note

- If a connection cannot be established within 20 seconds, a timeout occurs.
- Currently supported key types are: RSA, DSS, ECDSA, Ed25519.

## Parameter

### Hostname

Hostname to connect to. Usually in the form of an IP address

- ID: `hostname`
- Datatype: `string`
- Default Value: `None`

### Port

The port on which the connection will be tried on. Default is 22.

- ID: `port`
- Datatype: `Long`
- Default Value: `22`

### Username

The username with which a connection will be instantiated.

- ID: `username`
- Datatype: `string`
- Default Value: `None`

### Authentication method

The method that is used to connect to the SSH server.

- ID: `authentication_method`
- Datatype: `string`
- Default Value: `password`

### Private key

Your private key to connect via SSH.

- ID: `private_key`
- Datatype: `password`
- Default Value: `None`

### Password

Depending on your authentication method this will either be used toconnect via password to SSH, or to decrypt the SSH private key

- ID: `password`
- Datatype: `password`
- Default Value: `None`

### Path

The currently selected path within your SSH instance. Auto-completion starts from user home folder, use '..' for parent directory or '/' for root directory.

- ID: `path`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
