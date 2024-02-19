---
title: "cmemc: Command Group - admin user"
description: "List, create, delete and modify user accounts."
icon: material/account-cog
tags:
  - Keycloak
  - Security
  - cmemc
---
# admin user Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete and modify user accounts.

This command group is an opinionated interface to the Keycloak realm of your Corporate Memory instance. In order to be able to manage user data, the configured cmemc connection account needs to be equipped with the `manage-users` role in the used realm.

User accounts are identified by a username which unique in the scope of the used realm.

In case your Corporate Memory deployment does not use the default deployment layout, the following additional config variables can be used in your connection configuration: ``KEYCLOAK_BASE_URI`` defaults to `/auth` on ``CMEM_BASE_URI`` and locates your Keycloak deployment; ``KEYCLOAK_REALM_ID`` defaults to `cmem` and identifies the used realm.


## admin user list

List user accounts.

```shell-session title="Usage"
$ cmemc admin user list [OPTIONS]
```




Outputs a list of user accounts, which can be used to get an overview as well as a reference for the other commands of the `admin user` command group.



??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --filter <TEXT TEXT>...  Filter users by one of the following filter names
                             and a corresponding value: enabled, email,
                             username.
    --id-only                Lists only username. This is useful for piping the
                             IDs into other commands.
    ```

## admin user create

Create a user account.

```shell-session title="Usage"
$ cmemc admin user create USERNAME
```




This command creates a new user account.

!!! note
    The created user account has no metadata such as personal data or group assignments. In order to add these details to a user account, use the `admin user update` command.




## admin user update

Update a user account.

```shell-session title="Usage"
$ cmemc admin user update [OPTIONS] USERNAME
```




This command updates metadata and group assignments of a user account.

For each data value, a separate option needs to be used. All options can be combined in a single execution.

!!! note
    In order to assign a group to a user account, the group need to be added or imported to the realm upfront.




??? info "Options"
    ```text

    --first-name TEXT      Set a new first name.
    --last-name TEXT       Set a new last name.
    --email TEXT           Set a new email.
    --assign-group TEXT    Assign a group.
    --unassign-group TEXT  Unassign a group.
    ```

## admin user delete

Delete a user account.

```shell-session title="Usage"
$ cmemc admin user delete USERNAME
```




This command deletes a user account from a realm.

!!! note
    The deletion of a user account does not delete the assigned groups of this account, only the assignments to these groups.




## admin user password

Change the password of a user account.

```shell-session title="Usage"
$ cmemc admin user password [OPTIONS] USERNAME
```




With this command, the password of a user account can be changed. The default execution mode of this command is an interactive prompt which asks for the password (twice). In order automate password changes, you can use the ``--value`` option.

!!! warning
    Providing passwords on the command line can be dangerous (e.g. due to a potential exploitation in the shell history). A suggested more save way for automation is to provide the password in a variable first (e.g. with `NEW_PASS=$(pwgen -1 40)`) and use it afterward in the cmemc call: `cmemc admin user password max --value ${NEW_PASS}`.




??? info "Options"
    ```text

    --value TEXT      With this option, the new password can be set in a non-
                      interactive way.
    --temporary       If enabled, the user must change the password on next
                      login.
    --request-change  If enabled, will send a email to user to reset the
                      password.
    ```

## admin user open

Open user in the browser.

```shell-session title="Usage"
$ cmemc admin user open [USERNAMES]...
```




With this command, you can open a user in the keycloak console in your browser to change them.

The command accepts multiple usernames which results in opening multiple browser tabs.



