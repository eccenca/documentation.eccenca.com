---
title: "Upload SSH files"
description: "Upload files to an SSH server."
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


Uploads the files it receives to a directory on an SSH server.

Files arrive on the input port as file entities and are written into the configured
directory under their plain file name. The task has no output port: it ends the branch
of the workflow it sits in and hands nothing on to a following task.

**Download SSH files** covers the other direction, and **Execute commands via SSH**
runs a command on the uploaded files once they are in place.

## Caveats

- Content that is gzip compressed is unpacked before it is sent. Such a file arrives on
the server uncompressed, under an unchanged name that still ends in `.gz`.
- A file of the same name already on the server is overwritten without warning, and so
are files of the same name coming from different folders.
- The first failing upload aborts the task. Files uploaded before that stay on the
server, and nothing is rolled back.
- The target directory has to exist. It is not created.
- The task logs in with the configured credentials only, and offers no key of the
machine it runs on. The host key of the server in turn is accepted as presented and
never checked against a known hosts list.
- Establishing the connection fails after 20 seconds.


## Parameter

### Hostname

Host name or IP address of the SSH server.

- ID: `hostname`
- Datatype: `string`
- Default Value: `None`



### Port

TCP port the SSH server listens on.

- ID: `port`
- Datatype: `Long`
- Default Value: `22`



### Username

Account to log in as.

- ID: `username`
- Datatype: `string`
- Default Value: `None`



### Authentication method

How the task authenticates against the server.

- ID: `authentication_method`
- Datatype: `string`
- Default Value: `password`



### Private key

Private key in PEM format, used when the authentication method is Key. RSA, ECDSA and Ed25519 keys are supported.

- ID: `private_key`
- Datatype: `password`
- Default Value: `None`



### Password

Password of the account, or the passphrase of the private key when the authentication method is Key.

- ID: `password`
- Datatype: `password`
- Default Value: `None`



### Path

Remote directory the files are written to. Autocompletion starts in the home directory of the account, use '..' for the parent directory or '/' for the root directory.

- ID: `path`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

`None`
