---
title: "Download SSH files"
description: "Download files from a given SSH instance"
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


This workflow task downloads files from a specified SSH instance.

By providing the hostname, username, port and authentication method, you can specify the
folder from which the data should be extracted.

You can also define a regular expression to include or exclude specific files.

There is also an option to prevent files in subfolders from being included.

#### Authentication Methods:
* **Password:** Only the password will be used for authentication. The private key field is
ignored, even if filled.
* **Key:** The private key will be used for authentication. If the key is encrypted, the password
will be used to decrypt it.

#### Error handling modes:
* **Ignore:** Ignores the permission rights of files and lists downloads all files it has access to.
Skips folders and files when there is no correct permission.
* **Warning:** Warns the user about files that the user has no permission rights to. Downloads
all other files and skips files folder when there is no correct permission.
* **Error:** Throws an error when there is a single file or folder with incorrect permission rights.

#### Note:
* If a connection cannot be established within 20 seconds, a timeout occurs.
* Currently supported key types are: RSA, DSS, ECDSA, Ed25519.
* Setting the maximum amount of workers to more than 1 may cause a Channel Exception when
the amount of files is too large
    

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



### Error handling for missing permissions.

A choice on how to handle errors concerning the permissions rights.When choosing 'ignore' all files get skipped if the current user has correct permission rights.When choosing 'warning' all files get downloaded however there will be a mention that some of the files are not under the users permissionsif there are any and these get skipped.When choosing 'error' the files will not get downloaded if thereis even a single file the user has no access to.

- Datatype: `string`
- Default Value: `error`



### No subfolder

When this flag is set, only files from the current directory will be downloaded.

- Datatype: `boolean`
- Default Value: `false`



### Regular expression

A regular expression used to define which files will get downloaded.

- Datatype: `string`
- Default Value: `^.*$`



### Maximum amount of workers.

Determines the amount of workers used for concurrent thread execution of the task. Default is 1, maximum is 32. Note that too many workers can cause a ChannelException.

- Datatype: `Long`
- Default Value: `1`



