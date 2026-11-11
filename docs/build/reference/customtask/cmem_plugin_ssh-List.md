---
title: "List SSH files"
description: "List the files of a directory on an SSH server, with their metadata."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# List SSH files

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


Lists the files of a directory on an SSH server, together with the metadata the
server reports for them.

The task takes no input. It emits one entity per file, holding the full remote path
in `file_name`, plus `size`, `uid`, `gid`, `mode`, `atime` and `mtime` exactly as the
server reports them: a byte count, numeric owner and group ids, numeric mode bits and
Unix timestamps. Folders are traversed but never emitted.

**Download SSH files** accepts these entities on its input port, so that listing and
downloading can be split into two steps, with transformations in between that narrow
down which of the listed files are fetched.

The **Preview results** action lists the first ten matches without running the
workflow. It stops after ten files, so it can miss the unreadable file that would make
a real run behave differently.

## Caveats

- Files the account cannot read are listed like every other file. The error handling
only decides whether they are reported on top of that, or the listing fails.
- A folder that cannot be read is skipped silently unless the error handling is set to
Error, and the files below it are then missing from the result without further notice.
- Every file is opened and one byte is read from it to find out whether it is readable,
which makes listing a large directory noticeably slower than a plain directory listing.
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

Remote directory the task works in. Autocompletion starts in the home directory of the account, use '..' for the parent directory or '/' for the root directory.

- ID: `path`
- Datatype: `string`
- Default Value: `None`



### Error handling

How the task reacts to files and folders the account cannot read.

- ID: `error_handling`
- Datatype: `string`
- Default Value: `error`



### No subfolder

If enabled, only the given directory is listed and its subfolders are left out.

- ID: `no_subfolder`
- Datatype: `boolean`
- Default Value: `false`



### Regular expression

Regular expression a file name has to match completely to be listed. It is matched against the plain file name, not against the path.

- ID: `regex`
- Datatype: `string`
- Default Value: `^.*$`

## Advanced Parameter

### Maximum number of workers

Number of threads that list subfolders in parallel, from 1 to 32. More threads speed up a deep folder tree, but too many parallel channels make some servers refuse them with a ChannelException.

- ID: `max_workers`
- Datatype: `Long`
- Default Value: `1`
