---
title: "cmemc: Command Group - admin acl"
description: "List, create, delete and modify and review access conditions."
icon: material/server-security
tags:
  - Security
  - cmemc
---
# admin acl Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, create, delete and modify and review access conditions.

With this command group, you can manage and inspect access conditions in eccenca Corporate Memory. Access conditions are identified by a URL. They grant access to knowledge graphs or actions to user or groups.


## admin acl list

List access conditions.

```shell-session title="Usage"
$ cmemc admin acl list [OPTIONS]
```




This command retrieves and lists all access conditions, which are manageable by the current account.



??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    --id-only   Lists only URIs. This is useful for piping the IDs into other
                commands.
    ```

## admin acl inspect

Inspect an access condition.

```shell-session title="Usage"
$ cmemc admin acl inspect [OPTIONS] ACCESS_CONDITION_ID
```




!!! note
    access conditions can be listed by using the `acl list` command.




??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## admin acl create

Create an access condition.

```shell-session title="Usage"
$ cmemc admin acl create [OPTIONS]
```





??? info "Options"
    ```text

    --name TEXT         A short name or label.
    --id TEXT           An optional ID (will be an UUID otherwise).
    --description TEXT  An optional description.
    --user TEXT         A specific user account required by the access
                        condition.
    --group TEXT        A membership in a user group required by the access
                        condition
    --read-graph TEXT   Grants read access to a graph.
    --write-graph TEXT  Grants write access to a graph (includes read access).
    --action TEXT       Grants usage permissions to an action / functionality.
    ```

## admin acl update

Update an access condition.

```shell-session title="Usage"
$ cmemc admin acl update [OPTIONS] ACCESS_CONDITION_ID
```




Given an access condition URL, you can change specific options to new values.



??? info "Options"
    ```text

    --name TEXT         A short name or label.
    --description TEXT  An optional description.
    --user TEXT         A specific user account required by the access
                        condition.
    --group TEXT        A membership in a user group required by the access
                        condition
    --read-graph TEXT   Grants read access to a graph.
    --write-graph TEXT  Grants write access to a graph (includes read access).
    --action TEXT       Grants usage permissions to an action / functionality.
    ```

## admin acl delete

Delete access conditions.

```shell-session title="Usage"
$ cmemc admin acl delete [OPTIONS] [ACCESS_CONDITION_IDS]...
```




This command deletes existing access conditions from the account.

!!! note
    Access conditions can be listed by using the `cmemc admin acs list` command.




??? info "Options"
    ```text

    -a, --all   Delete all access conditions. This is a dangerous option, so use
                it with care.
    ```

## admin acl review

Review grants for a given account.

```shell-session title="Usage"
$ cmemc admin acl review [OPTIONS] USER
```




This command has two working modes: (1) You can review the access conditions of an actual account - this needs access to keycloak and the access condition API, (2) You can review the access conditions of an imaginary account with a set of freely added groups (what-if-scenario) - this only needs access to the access condition API.

The output of the command is a list of grants the account has based on your input and all access conditions loaded in the store. In addition to that, some metadata of the account is shown.



??? info "Options"
    ```text

    --raw         Outputs raw JSON.
    --group TEXT  Add groups to the review request (what-if-scenario).
    ```

