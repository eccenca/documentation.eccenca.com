---
title: "Office 365 Upload Files"
description: "Upload files to OneDrive or a site Sharepoint"
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Office 365 Upload Files
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow task upload files to specified Office 365 instance.
For this to work a registered app in Microsoft's Entra ID space is necessary.
Further information can be found [here](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

After registering an application, it needs to be granted application wide API permissions:
- Files.Read.All, Files.Write.All
- Sites.Read.All, Sites.Write.All

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

- ID: `tenant_id`
- Datatype: `string`
- Default Value: `None`



### Client ID

Client ID of your registered application.

- ID: `client_id`
- Datatype: `string`
- Default Value: `None`



### Client secret

Client secret created withing your registered application.

- ID: `client_secret`
- Datatype: `password`
- Default Value: `None`



### Type resource

The type of resource you want the data to be extracted from. This can either be a site or a users share

- ID: `type_resource`
- Datatype: `string`
- Default Value: `None`



### Target resource

Target resource which files will be listed from. This can either be a specific users share address or a microsoft site URL.

- ID: `target_resource`
- Datatype: `string`
- Default Value: `None`



### Drives

A list of drives from the selected target resource.

- ID: `drives`
- Datatype: `string`
- Default Value: `None`



### Directory path

The path of a directory that needs to be transformed. Includes all subdirectories by default

- ID: `path`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

### Maximum amount of workers

Specifies the maximum number of threads used for parallel execution of the workflow. The default is 32, and the valid range is 1 to 32. Note: Due to known throttling limits imposed by Microsoft, running with high parallelism may cause errors. If you encounter issues, try reducing the number of threads to 1.

- ID: `max_workers`
- Datatype: `Long`
- Default Value: `32`



