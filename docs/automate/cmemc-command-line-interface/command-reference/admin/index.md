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




This command outputs version and health information of the selected deployment. If the version information can not be retrieved, UNKNOWN shown.

In addition to that, this command warns you if the target version of your cmemc client is newer than the version of your backend and if the ShapeCatalog has a different version then your DataPlatform component.

To get status information of all configured deployments use this command in combination with parallel.

```shell-session title="Example"
$ cmemc config list | parallel --ctag cmemc -c {} admin status
```




??? info "Options"
    ```text

    --key TEXT       Get only specific key(s) from the status / info output.
                     There are two special keys available: 'all' will list all
                     available keys in the table, 'overall.healthy' with result
                     in  UP in case all health flags are UP as well (otherwise
                     DOWN).
  
    --enforce-table  A single value with --key will be returned as plain text
                     instead of a table with one row and the header. This
                     default behaviour allows for more easy integration with
                     scripts. This flag enforces the use of tabular output, even
                     for single row tables.
  
    --raw            Outputs combined raw JSON output of the health/info
                     endpoints.
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


Please be aware that this command can reveal secrets, which you do not want to have in log files or on the screen.



??? info "Options"
    ```text

    --raw       Outputs raw JSON. Note that this option will always try to fetch
                a new JSON token response. In case you are working with
                OAUTH_GRANT_TYPE=prefetched_token, this may lead to an error.
  
    --decode    Decode the access token and outputs the raw JSON. Note that the
                access token is only decoded and esp. not validated.
    ```

