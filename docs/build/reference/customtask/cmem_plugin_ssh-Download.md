---
title: "Download SSH files"
description: "Download files from an SSH server."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Download SSH files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Downloads files from an SSH server into the workflow.

What is downloaded depends on the input port. When nothing is connected, the task lists
the configured directory itself and downloads the files matching the regular
expression. When a file listing is connected, it downloads exactly the paths carried in
the `file_name` value of the incoming entities, and the directory, regular expression
and subfolder settings are then without effect. Either way the files leave the output
port as file entities, stored in a temporary directory on the eccenca Corporate Memory
host from where the following tasks read them.

**List SSH files** produces the listing this task accepts, so a workflow can list
first, narrow the result down and download only what is left. **Upload SSH files**
covers the other direction.

The **Preview results** action lists the first ten files that a run without input would
download, without running the workflow.

## Caveats

- Only the plain file name of a remote file is kept. Downloaded files of the same name
coming from different folders overwrite each other, and just one of them reaches the
output port.
- A file that cannot be read is dropped from the output silently with both Ignore and
Warning. The warning names the unreadable files seen while listing, which is not

necessarily the same set of files.

- A folder that cannot be read is skipped silently unless the error handling is set to
Error, and the files below it are then never downloaded.
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

Remote directory the files are downloaded from, and ignored when a file listing arrives on the input port. Autocompletion starts in the home directory of the account, use '..' for the parent directory or '/' for the root directory.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Error handling

How the task reacts to files and folders the account cannot read.

- ID: `error_handling`
- Datatype: `string`
- Default Value: `error`



### No subfolder

If enabled, only the given directory is searched and its subfolders are left out.

- ID: `no_subfolder`
- Datatype: `boolean`
- Default Value: `false`



### Regular expression

Regular expression a file name has to match completely to be downloaded. It is matched against the plain file name, not against the path.

- ID: `regex`
- Datatype: `string`
- Default Value: `^.*$`

## Advanced Parameter

### Maximum number of workers

Number of threads the Preview results action uses to list subfolders in parallel, from 1 to 32. A workflow run always lists with a single thread. Too many parallel channels make some servers refuse them with a ChannelException.

- ID: `max_workers`
- Datatype: `Long`
- Default Value: `1`
