---
title: "cmemc: Environment-based Configuration"
subtitle: Configuration
icon: material/cog-outline
tags:
  - cmemc
---
# Environment-based Configuration

## Introduction

In addition to using configuration files, cmemc can also be widely configured and parameterized with environment variables.

Typical use cases for when you may want to do this include:

- set a default connection (see below)
- enable session-wide debugging output
- control cmemc with variables from a calling process
- avoid having client and user credentials lying around in a file

There are two major categories of environment variables you can use.

## Environment variables for configuration

For these variables the rules are simple: You can use any variable from the [config file](../file-based-configuration/index.md) in the same way as an environment variable.

The following commands provide the same result as given in the [basic example for a config file](../file-based-configuration/index.md):

``` shell-session
export CMEM_BASE_URI=http://localhost/
export OAUTH_GRANT_TYPE=client_credentials
export OAUTH_CLIENT_ID=cmem-service-account
export OAUTH_CLIENT_SECRET=...
```

!!! info

    File-based and environment-based configuration interact in both directions:
    an environment variable overrides a value from the `[DEFAULT]` section, while a named connection section (`-c my-connection`) overrides the environment.
    See [Configuration value resolution order](../index.md) for the complete set of rules.

## Environment variables for parameters or options

The general pattern for parameter and option settings via environment variables is:

- all variables start with the prefix `CMEMC_`
- command group and command follow the prefix in uppercase and separated by `_`
- the option is in uppercase at the end.
- The naming scheme is: `CMEMC[_<COMMAND-GROUP>_<COMMAND>][_<OPTION>]`

The next sections demonstrate this pattern with examples.

### Example: Set a default connection

We first run a cmemc command via command line parameter:

``` shell-session
$ cmemc --config-file cmemc.ini --connection mycmem graph list --raw
[
  {
    "iri": "https://ns.eccenca.com/data/userinfo/",
... more JSON output ...
```

As a next step, we replace all connection parameters with environment variables:

``` shell-session
export CMEMC_CONFIG_FILE=cmemc.ini
export CMEMC_CONNECTION=mycmem
```

This alone allows us to save a lot of typing for a series of commands on the same Corporate Memory instance.

``` shell-session
$ cmemc graph list --raw
[... same output as above ...]
```

However, you can also pre-define command options in the same way:

``` shell-session
export CMEMC_GRAPH_LIST_RAW=true
```

Again, the same command but `--raw` is set per default.

``` shell-session
$ cmemc graph list
[... same output as above ...]
```

### Example: enable session wide debugging output

Since there is a top level `--debug` option, the corresponding variable name is `CMEMC_DEBUG`:

``` shell-session
export CMEMC_DEBUG=true
```

The same works for the other top level options, which is useful to set them once for a whole terminal session:

| Variable | Option | Description |
| -------- | ------ | ----------- |
| `CMEMC_CONNECTION` | `--connection` / `-c` | Use a specific connection from the config file. |
| `CMEMC_CONFIG_FILE` | `--config-file` | Use this config file instead of the default one. |
| `CMEMC_QUIET` | `--quiet` / `-q` | Suppress any non-error info messages. |
| `CMEMC_DEBUG` | `--debug` / `-d` | Output debug messages and stack traces after errors. |
| `CMEMC_LOG_LEVEL` | `--log-level` | Set the log level when `--debug` is enabled (defaults to `debug`). |
| `CMEMC_EXTERNAL_HTTP_TIMEOUT` | `--external-http-timeout` | Timeout in seconds for external HTTP requests (defaults to `10`). |

In addition to that, `CMEMC_CONSOLE_WIDTH` sets a fixed width for the rendered tables and other console output.
This has no corresponding command line option and is mainly useful to get reproducible output in scripts and pipelines.

## Configuration environment export from the config file

cmemc can export a configuration environment from a configuration file to set up an environment for later use with the `config eval` command.

``` shell-session
$ cmemc -c my-cmem.example.org config eval
export CMEM_BASE_URI="https://my-cmem.example.org"
export DI_API_ENDPOINT="https://my-cmem.example.org/dataintegration"
export DP_API_ENDPOINT="https://my-cmem.example.org/dataplatform"
export KEYCLOAK_BASE_URI="https://my-cmem.example.org/auth"
export KEYCLOAK_REALM_ID="cmem"
unset OAUTH_ACCESS_TOKEN
export OAUTH_CLIENT_ID="cmem-service-account"
export OAUTH_CLIENT_SECRET="..."
export OAUTH_GRANT_TYPE="client_credentials"
unset OAUTH_PASSWORD
export OAUTH_TOKEN_URI="https://my-cmem.example.org/auth/realms/cmem/protocol/openid-connect/token"
unset OAUTH_USER
export REQUESTS_CA_BUNDLE=".../certifi/cacert.pem"
export SSL_VERIFY="True"
```

This can be used to export a full `config.env` or to `eval` it in an environment for other processes:

``` shell-session
cmemc -c my-cmem.example.org config eval > config.env
eval $(cmemc -c my-cmem.example.org config eval)
```

Please note that the following command has the same effect but needs the `cmemc.ini` for evaluating the `config` values for the config section `my-cmem.example.org`:

``` shell-session
export CMEMC_CONNECTION="my-cmem.example.org"
```
