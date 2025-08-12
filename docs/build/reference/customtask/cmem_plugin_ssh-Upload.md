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

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).


This workflow task uploads files to a given SSH instance.

By providing the hostname, username, port and authentication method, you can specify the
folder the data should be uploaded to.

#### Authentication Methods:
* **Password:** Only the password will be used for authentication. The private key field is
ignored, even if filled.
* **Key:** The private key will be used for authentication. If the key is encrypted, the password
will be used to decrypt it.

#### Note:
* If a connection cannot be established within 20 seconds, a timeout occurs.
* Currently supported key types are: RSA, DSS, ECDSA, Ed25519.
    

## Parameter

### Hostname

Hostname to connect to. Usually in the form of an IP address

- Datatype: `string`
- Default Value: `None`



### Port

The port on which the connection will be tried on. Default is 22.

- Datatype: `Long`
- Default Value: `22`



### Username

The username of which a connection will be instantiated.

- Datatype: `string`
- Default Value: `None`



### Authentication method

The method that is used to connect to the SSH server.

- Datatype: `string`
- Default Value: `password`



### Private key

Your private key to connect via SSH.

- Datatype: `password`
- Default Value: `None`



### Password

Depending on your authentication method this will either be used toconnect via password to SSH or is used to decrypt the SSH private key

- Datatype: `password`
- Default Value: `None`



### Path

The currently selected path withing your SSH instance.

- Datatype: `string`
- Default Value: `None`



