---
title: "Execute commands via SSH"
description: "Execute commands on a given SSH instance."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Execute commands via SSH

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This workflow task executes commands on a given SSH instance.

By providing the hostname, username, port and authentication method, you can specify the
folder in which the command should be executed in.

## Input Methods

- **No input:** The command will be executed with no input attached to the plugin. Stdin
is non-existent in this case.
- **File input:** The command will be executed with the stdin being represented by the
files that are connected via the input port of the plugin. This also allows for looping
over multiple files executing the same command over them.

### Output Methods

- **Structured process output:** The output will produce entities with its own schema including
the stdout and stderr as well as the exit code to confirm the execution of the command.
- **File output:** The stdout will be converted into a file a be provided for further use.
- **No output:** The output port will be closed.

#### Authentication Methods

- **Password:** Only the password will be used for authentication. The private key field is
ignored, even if filled.
- **Key:** The private key will be used for authentication. If the key is encrypted, the password
will be used to decrypt it.

#### Note

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

### Input method

Parameter to decide whether files will be used as stdin or no input is needed. If 'File input' is chosen, the input port will open for all entities withthe FileEntitySchema.

- ID: `input_method`
- Datatype: `string`
- Default Value: `None`

### Output method

Parameter to decide which type of output the user wants. This can be either no output, a structured process output with its own schema, or a file based output

- ID: `output_method`
- Datatype: `string`
- Default Value: `None`

### Command

The command that will be executed on the SSH instance. When the inputmethod is set to 'File input', the command will be executed over these files.

- ID: `command`
- Datatype: `string`
- Default Value: `ls`

### Timeout

A timeout for the executed command.

- ID: `timeout`
- Datatype: `Long`
- Default Value: `0`

## Advanced Parameter

`None`
