---
title: "cmemc: Command Group - config"
description: "List and edit configs as well as get config values."
icon: material/cog-outline
tags:
  - Configuration
  - cmemc
---
# config Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

```text
List and edit configs as well as get config values.

    Configurations are identified by the section identifier in the
    config file. Each configuration represent a Corporate Memory deployment
    with its specific access method as well as credentials.

    A minimal configuration which uses client credentials has the following
    entries:

    
    [example.org]
    CMEM_BASE_URI=https://cmem.example.org/
    OAUTH_GRANT_TYPE=client_credentials
    OAUTH_CLIENT_ID=cmem-service-account
    OAUTH_CLIENT_SECRET=my-secret-account-pass

    Note that OAUTH_GRANT_TYPE can be either client_credentials, password or
    prefetched_token.

    In addition to that, the following config parameters can be used as well:

    
    SSL_VERIFY=False    - for ignoring certificate issues (not recommended)
    DP_API_ENDPOINT=URL - to point to a non-standard Explore backend (DataPlatform) location
    DI_API_ENDPOINT=URL - to point to a non-standard Build (DataIntegration) location
    OAUTH_TOKEN_URI=URL - to point to an external IdentityProvider location
    OAUTH_USER=username - only if OAUTH_GRANT_TYPE=password
    OAUTH_PASSWORD=password - only if OAUTH_GRANT_TYPE=password
    OAUTH_ACCESS_TOKEN=token - only if OAUTH_GRANT_TYPE=prefetched_token

    In order to get credential information from an external process, you can
    use the parameter OAUTH_PASSWORD_PROCESS, OAUTH_CLIENT_SECRET_PROCESS and
    OAUTH_ACCESS_TOKEN_PROCESS to set up an external executable.

    
    OAUTH_CLIENT_SECRET_PROCESS=/path/to/getpass.sh
    OAUTH_PASSWORD_PROCESS=["getpass.sh", "parameter1", "parameter2"]

    The credential executable can use the cmemc environment for fetching the
    credential (e.g. CMEM_BASE_URI and OAUTH_USER).
    If the credential executable is not given with a full path, cmemc
    will look into your environment PATH for something which can be executed.
    The configured process needs to return the credential on the first line
    of stdout. In addition to that, the process needs to exit with exit
    code 0 (without failure). There are examples available in the online
    manual.

```

## config list

List configured connections.

```shell-session title="Usage"
$ cmemc config list
```




This command lists all configured connections from the currently used config file.

The connection identifier can be used with the `--connection` option in order to use a specific Corporate Memory instance.

In order to apply commands on more than one instance, you need to use typical unix gear such as xargs or parallel.

```shell-session title="Example"
$ cmemc config list | xargs -I % sh -c 'cmemc -c % admin status'
```


```shell-session title="Example"
$ cmemc config list | parallel --jobs 5 cmemc -c {} admin status
```




## config edit

Edit the user-scope configuration file.

```shell-session title="Usage"
$ cmemc config edit
```





## config get

Get the value of a known cmemc configuration key.

```shell-session title="Usage"
$ cmemc config get {CMEM_BASE_URI|SSL_VERIFY|REQUESTS_CA_BUNDLE|DP_API_END
             POINT|DI_API_ENDPOINT|KEYCLOAK_BASE_URI|KEYCLOAK_REALM_ID|OAUTH_T
             OKEN_URI|OAUTH_GRANT_TYPE|OAUTH_USER|OAUTH_PASSWORD|OAUTH_CLIENT_
             ID|OAUTH_CLIENT_SECRET|OAUTH_ACCESS_TOKEN}
```




In order to automate processes such as fetching custom API data from multiple Corporate Memory instances, this command provides a way to get the value of a cmemc configuration key for the selected deployment.

```shell-session title="Example"
$ curl -H "Authorization: Bearer $(cmemc -c my admin token)" $(cmemc -c my config get DP_API_ENDPOINT)/api/custom/slug
```


The commands return with exit code 1 if the config key is not used in the current configuration.



## config eval

Export all configuration values of a configuration for evaluation.

```shell-session title="Usage"
$ cmemc config eval [OPTIONS]
```




The output of this command is suitable to be used by a shell's `eval` command. It will output the complete configuration as `export key="value"` statements, which allow for the preparation of a shell environment.

```shell-session title="Example"
$ eval $(cmemc -c my config eval)
```


!!! warning
    Please be aware that credential details are shown in cleartext with this command.




??? info "Options"
    ```text

    --unset     Instead of exporting all configuration keys, this option will
                unset all keys.
    ```

