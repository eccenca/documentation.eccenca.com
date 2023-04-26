---
title: "cmemc: Command Group - admin"
description: "Import bootstrap data, backup/restore workspace or get status."
icon: material/key-link
tags:
  - cmemc
---
# admin Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Import bootstrap data, backup/restore workspace or get status.

This command group consists of commands for setting up and configuring eccenca Corporate Memory.


## admin status

Output health and version information.

```shell-session title="Usage"
$ cmemc admin status [OPTIONS]
```




This command outputs version and health information of the selected deployment. If the version information cannot be retrieved, UNKNOWN is shown.

Additionally, this command warns you if the target version of your cmemc client is newer than the version of your backend and if the ShapeCatalog has a different version than your DataPlatform component.

To get status information of all configured deployments use this command in combination with parallel.

```shell-session title="Example"
$ cmemc config list | parallel --ctag cmemc -c {} admin status
```




??? info "Options"
    ```text

    --key TEXT                     Get only specific key(s) from the status /
                                   info output. There are two special keys
                                   available: 'all' will list all available keys
                                   in the table, 'overall.healthy' with result
                                   in  UP in case all health flags are UP as
                                   well (otherwise DOWN).
  
    --exit-1 [never|error|always]  Specify, when this command returns with exit
                                   code 1. Available options are 'never' (exit 0
                                   on errors and warnings), 'error' (exit 1 on
                                   errors, exit 0 on warnings), 'always' (exit 1
                                   on errors and warnings).  [default: never]
  
    --enforce-table                A single value with --key will be returned as
                                   plain text instead of a table with one row
                                   and the header. This default behaviour allows
                                   for more easy integration with scripts. This
                                   flag enforces the use of tabular output, even
                                   for single row tables.
  
    --raw                          Outputs combined raw JSON output of the
                                   health/info endpoints.
    ```

## admin token

Fetch and output an access token.

```shell-session title="Usage"
$ cmemc admin token [OPTIONS]
```




This command can be used to check for correct authentication as well as to use the token with wget / curl or similar standard tools:

```shell-session title="Example"
$ curl -H "Authorization: Bearer $(cmemc -c my admin token)" $(cmemc -c my config get DP_API_ENDPOINT)/api/custom/slug
```


Please be aware that this command can reveal secrets which you might not want to be present in log files or on the screen.



??? info "Options"
    ```text

    --raw       Outputs raw JSON. Note that this option will always try to fetch
                a new JSON token response. In case you are working with
                OAUTH_GRANT_TYPE=prefetched_token, this may lead to an error.
  
    --decode    Decode the access token and outputs the raw JSON. Note that the
                access token is only decoded and esp. not validated.
    ```

