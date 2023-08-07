---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 23.2

Corporate Memory 23.2 is the second major release in 2023.

... images ...

The highlights of this release are:

-   Build:
    -   Support for user managed **project variables** in dataset and task parameters.
-   Explore:
    -   ...
-   Automate:
    -   New **`admin client` command group** for managing client accounts in the Keycloak CMEM realm.

This release delivers the following component versions:

-   eccenca DataPlatform v23.2
-   eccenca DataIntegration v23.2
-   eccenca DataIntegration Python Plugins v4.1.0
-   eccenca DataManager v23.2
-   eccenca Corporate Memory Control (cmemc) v23.2

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v23.2

...

## eccenca DataIntegration Python Plugins v4.1.0

Corporate Memory v23.2 includes the DataIntegration Python Plugins support in version 4.1.0.

v4.1.0 of eccenca DataIntegration Python Plugins adds the following new features:

-   use `post_resource` api in `write_to_dataset` function to update dataset file resource
-   use cmempy 23.2
-   upgrade dependencies
-   enforce usage of Python 3.11

## eccenca DataManager v23.2

...

## eccenca DataPlatform v23.2

...

## eccenca Corporate Memory Control (cmemc) v23.2

v23.2 of eccenca Corporate Memory Control adds the following new features:

-   `admin user password` command
    -   option `--request-change` added, to send a email to user to reset the password
-   `dataset create` command
    -   add `readOnly` and `uriProperty` keys for the `-p/--parameter` option
-   `admin client` command group
    -   `list` command - list client accounts
    -   `open` command - Open clients in the browser
    -   `secret` command - Get or generate a new secret for a client account
-   `project create` command
    -   new option `--from-transformation` to create a mapping suggestion project

### Changed

-   `dataset upload` command
    -   use new endpoint which is aware of read-only datasets
-   `workflow io` command
    -   use of extended io endpoint
    -   allows for uploading bigger files
    -   allows for more input and output mimetypes
    -   change default output to JSON

## Migration Notes

...
