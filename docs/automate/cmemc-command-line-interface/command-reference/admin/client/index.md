---
title: "cmemc: Command Group - admin client"
description: "List client accounts, get or generate client account secrets."
icon: material/account-cog
tags:
  - Keycloak
  - Security
  - cmemc
---
# admin client Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List client accounts, get or generate client account secrets.

This command group is an opinionated interface to the Keycloak realm of your Corporate Memory instance. In order to be able to use the commands in this group, the configured cmemc connection account needs to be equipped with the `manage-clients` role in the used realm.

Client accounts are identified by a client ID which is unique in the scope of the used realm.

In case your Corporate Memory deployment does not use the default deployment layout, the following additional config variables can be used in your connection configuration: ``KEYCLOAK_BASE_URI`` defaults to `{`CMEM_BASE_URI`}/auth` and locates your Keycloak deployment; ``KEYCLOAK_REALM_ID`` defaults to `cmem` and identifies the used realm.


## admin client list

List client accounts.

```shell-session title="Usage"
$ cmemc admin client list [OPTIONS]
```




Outputs a list of client accounts, which can be used to get an overview as well as a reference for the other commands of the `admin client` command group.

!!! note
    The list command only outputs clients which have a client secret.




??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    --id-only   Lists only Client ID. This is useful for piping the IDs into
                other commands.
    ```

## admin client secret

Get or generate a new secret for a client account.

```shell-session title="Usage"
$ cmemc admin client secret [OPTIONS] CLIENT_ID
```




This command retrieves or generates a new secret for a client account from a realm.



??? info "Options"
    ```text

    --generate  Generate a new secret
    --output    Display client secret
    ```

## admin client open

Open clients in the browser.

```shell-session title="Usage"
$ cmemc admin client open [CLIENT_IDS]...
```




With this command, you can open a client in the keycloak web interface in your browser.

The command accepts multiple client IDs which results in opening multiple browser tabs.



