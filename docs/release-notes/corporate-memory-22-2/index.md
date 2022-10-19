---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 22.2

Corporate Memory 22.2 is the second release in 2022.

<!-- ![22.2: DataIntegration - Linking Editor](22-1-linking-editor.png "22.1: DataIntegration - Linking Editor") -->
<!-- ![22.2: DataManager - Workflow Execution](22-1-workflow-execution.png "22.1: DataManager - Workflow Execution") -->
![22.2: cmemc - Multiple Filter / Admin Status](22-2-cmemc-multiple-filter-and-admin-status.png "22.1: 22-2-cmemc-multiple-filter-and-admin-status.png")

The highlights of this release are:

-   Build:
    -   The all new **Active** (Link) **Learning UI**
    -   Extended **Python Plugin SDK**
-   Explore:
    -   New graph exploration module **EasyNav**
-   Consume:
        -   ... ?
-   Automate:
    -   ...

!!! warning

    With this release of Corporate Memory the DataPlatform configuration and behavior has changed and have to be adapted according to the migration notes below.

!!! warning

    With this release of Corporate Memory the (DataIntegration) Python plugin SDK added the `ExecutionContext` class. This results in a changed signature of the SDK API functions and thus in a breaking change. Your python SDK based plugins have to be adapted according to the migration notes below.

This release delivers the following component versions:

-   eccenca DataPlatform v22.2
-   eccenca DataIntegration v22.2
-   eccenca DataManager v22.2
-   eccenca Corporate Memory Control (cmemc) v22.2

More detailed release notes for these versions are listed below.

## eccenca DataIntegration v22.2

This version of eccenca DataIntegration adds the following new features:

-   ...

In addition to that, these changes are shipped:

-   ...

In addition to that, multiple performance and stability issues were solved.

## eccenca DataManager v22.2

This version of eccenca DataManager adds the following new features:

-   ...

In addition to that, these changes are shipped:

-   General
    -   ...
-   Shacl
    -   ...

In addition to that, multiple performance and stability issues were solved.

## eccenca DataPlatform v22.2

This version of eccenca DataPlatform ships the following new features:

-   ...

In addition to that, these changes and fixes are shipped:

-   ...

In addition to that, multiple performance and stability issues were solved.

## eccenca Corporate Memory Control (cmemc) v22.2

This version of cmemc adds the following new features:

-   `admin workspace python list-plugins` command
    -   New option `--package-id-only` to output only package IDs
-   `admin workspace python install` command completion
    -   now also provides plugin packages published on pypi.org
-   `query status` command
    -   New filter `query`:
        -   `graph` - List only queries which affected a certain graph (URL)
        -   `regex` - List only queries which query text matches a regular expression
        -   `trace-id` - List only queries which have the specified trace ID
        -   `user` - List only queries executed by the specified account (URL)
    -   New values for filter `status`:
        -   `cancelled`: List only queries which were cancelled
        -   `timeout`: List only queries which ran into a timeout
-   `query cancel` command
    -   cancel a running query - this stops the execution in the backend
    -   Depending on the backend store, this will result in a broken result stream (stardog, neptune and virtuoso) or a valid result stream with incomplete results (graphdb)
-   `dataset list`|`delete` commands
    -   New option `--filter` with the following concrete filter
        -   `project` - filter by project ID
        -   `regex` - filter by regular expression on the dataset label
        -   `tag` - filter by tag label
        -   `type` - filter by dataset type
-   `workflow list` command
    -   New option `--filter` with the following concrete filter
        -   `project` - filter by project ID
        -   `regex` - filter by regular expression on the dataset label
        -   `tag` - filter by tag label
        -   `io` - filter by io type
-   `admin status` command
    -   overall rewrite
    -   new table output
    -   new option `--raw` to output collected status / info values
    -   new option `--key` to output only specific values
    -   new option `--enforce-table` to enforce table output of `--key`
-   `vocabular import` command
    -   new option `--namespace`: In case the imported vocabulary file does not include a preferred namespace prefix, you can manually add a namespace prefix

In addition to that, these changes and fixes are shipped:

-   `admin workspace python list-plugins` command
    -   Additionally outputs the Package ID
-   `project import` command
    -   The project id is now optional when importing project files
-   `admin status` command
    -   new table output (similar to the other tables)
    -   `status` filter with `error` value
        -   only execution errors are listed
        -   this means esp. no cancelled and timeouted queries (they have there own status now)
-   Add pysocks dependency to cmempy
    -   This allows for using the `all_proxy` evironment variable
-   `dataset list --raw` output
    -   output was not a JSON array and not filtered correctly
-   cmempy get graph streames
    -   stream enabled
-   `admin status` command
    -   command will now always return, even if a component is down

The following commands are removed:

-   `admin bootstap` command
    -   was deprecated in 22.1, use `admin store bootstrap` command instead
-   `admin showcase` command
    -   was deprecated in 22.1, use `admin store showcase` command instead
-   `dataset list`|`delete` command
    -   `--project` option, use `--filter projext XXX` instead

In addition to that, multiple performance and stability issues were solved.

## Migration Notes

### DataIntegration

-   ...

### DataManager

-   ...

### DataPlatform

-   ...

### cmemc

-   `dataset list`|`delete command`
    -   option `--project` is removed
    -   Please use `--filter project XXX` instead
-   `admin status` command
    -   in case you piped the normal output of this command and reacted on that, you need to use the `--key` command now
