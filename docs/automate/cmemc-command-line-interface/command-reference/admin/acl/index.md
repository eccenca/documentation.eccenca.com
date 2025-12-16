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
cmemc admin acl list [OPTIONS]
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
cmemc admin acl inspect [OPTIONS] ACCESS_CONDITION_ID
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
cmemc admin acl create [OPTIONS]
```

With this command, new access conditions can be created.

An access condition captures information about WHO gets access to WHAT. In order to specify WHO gets access, use the ``--user`` and / or ``--group`` options. In order to specify WHAT an account get access to, use the ``--read-graph``, ``--write-graph`` and ``--action`` options.`

In addition to that, you can specify a name, a description and an ID (all optional).

A special case are dynamic access conditions, based on a SPARQL query: Here you have to provide a query with the projection variables `user`, `group` `readGraph` and `writeGraph` to create multiple grants at once. You can either provide a query file or a query URL from the query catalog.

!!! note
    Queries for dynamic access conditions are copied into the ACL, so changing the query in the query catalog does not change it in the access condition.

```shell-session title="Example"
cmemc admin acl create --group local-users --write-graph https://example.org/
```

??? info "Options"
    ```text

    --user TEXT                 A specific user account required by the access
                                condition.
    --group TEXT                A membership in a user group required by the
                                access condition.
    --read-graph TEXT           Grants read access to a graph.
    --write-graph TEXT          Grants write access to a graph (includes read
                                access).
    --action TEXT               Grants usage permissions to an action /
                                functionality.
    --read-graph-pattern TEXT   Grants management of conditions granting read
                                access on graphs matching the defined pattern. A
                                pattern consists of a constant string and a
                                wildcard ('*') at the end of the pattern or the
                                wildcard alone.
    --write-graph-pattern TEXT  Grants management of conditions granting write
                                access on graphs matching the defined pattern. A
                                pattern consists of a constant string and a
                                wildcard ('*') at the end of the pattern or the
                                wildcard alone.
    --action-pattern TEXT       Grants management of conditions granting action
                                allowance for actions matching the defined
                                pattern. A pattern consists of a constant string
                                and a wildcard ('*') at the end of the pattern
                                or the wildcard alone.
    --query TEXT                Dynamic access condition query (file or the
                                query catalog IRI).
    --id TEXT                   An optional ID (will be an UUID otherwise).
    --name TEXT                 A optional name.
    --description TEXT          An optional description.
    --replace                   Replace (overwrite) existing access condition,
                                if present. Can be used only in combination with
                                '--id'.
    ```

## admin acl update

Update an access condition.

```shell-session title="Usage"
cmemc admin acl update [OPTIONS] ACCESS_CONDITION_ID
```

Given an access condition URL, you can change specific options to new values.

??? info "Options"
    ```text

    --name TEXT                 A optional name.
    --description TEXT          An optional description.
    --user TEXT                 A specific user account required by the access
                                condition.
    --group TEXT                A membership in a user group required by the
                                access condition.
    --read-graph TEXT           Grants read access to a graph.
    --write-graph TEXT          Grants write access to a graph (includes read
                                access).
    --action TEXT               Grants usage permissions to an action /
                                functionality.
    --read-graph-pattern TEXT   Grants management of conditions granting read
                                access on graphs matching the defined pattern. A
                                pattern consists of a constant string and a
                                wildcard ('*') at the end of the pattern or the
                                wildcard alone.
    --write-graph-pattern TEXT  Grants management of conditions granting write
                                access on graphs matching the defined pattern. A
                                pattern consists of a constant string and a
                                wildcard ('*') at the end of the pattern or the
                                wildcard alone.
    --action-pattern TEXT       Grants management of conditions granting action
                                allowance for actions matching the defined
                                pattern. A pattern consists of a constant string
                                and a wildcard ('*') at the end of the pattern
                                or the wildcard alone.
    --query TEXT                Dynamic access condition query (file or the
                                query catalog IRI).
    ```

## admin acl delete

Delete access conditions.

```shell-session title="Usage"
cmemc admin acl delete [OPTIONS] [ACCESS_CONDITION_IDS]...
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
cmemc admin acl review [OPTIONS] USER
```

This command has two working modes: (1) You can review the access conditions of an actual account, (2) You can review the access conditions of an imaginary account with a set of freely added groups (what-if-scenario).

The output of the command is a list of grants the account has based on your input and all access conditions loaded in the store. In addition to that, some metadata of the account is shown.

??? info "Options"
    ```text

    --raw         Outputs raw JSON.
    --group TEXT  Add groups to the review request (what-if-scenario).
    ```
