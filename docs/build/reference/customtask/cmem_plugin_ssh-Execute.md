---
title: "Execute commands via SSH"
description: "Execute a command on an SSH server."
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


Runs a command on an SSH server and collects what it produces.

The input and output methods decide the shape of the task. With file input, an input
port accepts file entities and the command runs once per incoming file, with the
content of that file on its standard input; without it, the command runs exactly once.
What leaves the task is either one entity per run, carrying the exit code, the standard
output and the standard error, or one file per run holding the raw standard output, or
nothing at all, in which case the task ends the branch of the workflow it sits in.

**Upload SSH files** and **Download SSH files** move the files a command works on, so a
common chain is to upload files, run a command over them and download the result.

## Caveats

- The exit code is never inspected. A failing command leaves the task successful and
the workflow running, and the failure shows up only in the emitted exit code and
standard error. With file output, both are dropped and the standard output is kept
alone.
- The command is sent as it is written and interpreted by the login shell of the
account, without any escaping or checking, and it runs with every right that account
has.
- The command runs in whatever directory the account lands in on login. The configured
directory is not entered.
- With file input, each incoming file is read into memory as a whole before it is sent.
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

Remote directory, kept with the task but not entered before the command runs. Autocompletion starts in the home directory of the account, use '..' for the parent directory or '/' for the root directory.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Input method

Whether incoming files are fed to the command, which also decides whether the task has an input port.

- ID: `input_method`
- Datatype: `string`
- Default Value: `None`



### Output method

What the task emits for each run of the command, which also decides whether the task has an output port.

- ID: `output_method`
- Datatype: `string`
- Default Value: `None`



### Command

Command line executed on the server.

- ID: `command`
- Datatype: `string`
- Default Value: `ls`



### Timeout

Seconds the task waits for the command to send data before it gives up and fails. Zero waits for as long as the command takes.

- ID: `timeout`
- Datatype: `Long`
- Default Value: `0`

## Advanced Parameter

`None`
