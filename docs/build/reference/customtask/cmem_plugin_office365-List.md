---
title: "List Office 365 Files"
description: "List files from OneDrive or Sites"
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# List Office 365 Files
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task creates a structured output from a specified Office 365 instance.
For this to work a registered app in Microsoft's Entra ID space is necessary.
Further information can be found [here](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

After registering an application, it needs to be granted application wide API permissions:
- Files.Read.All
- Sites.Read.All

Admin consent is required to activate these permissions.
With this setup, anyone with the secret can access all users' OneDrives and all Sharepoint/Team
sites.

#### Important
Make sure only trusted admins can create or manage secrets!
Whoever holds the secrets has all the access to granted resources so best not to distribute
recklessly.
    

## Parameter

### Tenant ID

ID of your tenant. Can be seen within your registered application

- Datatype: `string`
- Default Value: `None`



### Client ID

Client ID of your registered application.

- Datatype: `string`
- Default Value: `None`



### Client secret

Client secret created withing your registered application.

- Datatype: `password`
- Default Value: `None`



### Type resource

The type of resource you want the data to be extracted from. This can either be a site or a users share

- Datatype: `string`
- Default Value: `None`



### Target resource

Target resource which files will be listed from. This can either be a specific users share address or a microsoft site URL.

- Datatype: `string`
- Default Value: `None`



### Drives

A list of drives from the selected target resource.

- Datatype: `string`
- Default Value: `None`



### Maximum amount of workers

Specifies the maximum number of threads used for parallel execution of the workflow. The default is 32, and the valid range is 1 to 32. Note: Due to known throttling limits imposed by Microsoft, running with high parallelism may cause errors. If you encounter issues, try reducing the number of threads to 1.

- Datatype: `Long`
- Default Value: `32`



### Directory path

The path of a directory that needs to be transformed. Includes all subdirectories by default

- Datatype: `string`
- Default Value: `None`



### Regular expression

A regular expression performed on all the files within the selected path

- Datatype: `string`
- Default Value: `^.*$`



### Exclude files in subfolders

A flag indicating if files should only be listed from subfolders or not.

- Datatype: `boolean`
- Default Value: `false`



