---
title: "cmemc: Environment-based Configuration"
subtitle: Configuration
icon: material/cog-outline
tags:
  - cmemc
---
# Environment-based Configuration

## Introduction

In addition to using configuration files, cmemc can be widely configured and parameterised with environment variables.

Typical use cases why you could want this include:

- set a default connection (see below),
- enable session wide debugging output,
- control cmemc with variables from a calling process,
- avoid having client and user credentials laying around in a file,
- ...

There are two major categories of environment variables you can use.

## Environment variables for configuration

For these variables the rules are simple: You can use any variable from the [config file](../file-based-configuration/index.md) in the same way also as an environment variable.

The following commands provide the same result as given in the [basic example for a config file](../file-based-configuration/index.md):

``` shell-session
$ export CMEM_BASE_URI=http://localhost/
$ export OAUTH_GRANT_TYPE=client_credentials
$ export OAUTH_CLIENT_ID=cmem-service-account
$ export OAUTH_CLIENT_SECRET=...
```

!!! info

    When you combine file based and environment based configuration, the config file always overwrites the environment.

## Environment variables for parameters or options

The general pattern for parameter and option settings via environment variables is:

- all variables start with the prefix `CMEMC_` ,
- command group and command follow the prefix uppercased and separated by `_` ,
- finally, the option is uppercased at the end.
- The naming scheme is: `CMEM[_<COMMAND-GROUP>_<COMMAND>][_<OPTION>]`

The next sections demonstrate this pattern with examples.

### Example: Set a default connection

To give an example, we first run a cmemc command via command line parameter:

``` shell-session
$ cmemc --config-file cmemc.ini --connection mycmem graph list --raw
[
  {
    "iri": "urn:elds-backend-access-conditions-graph",
... more JSON output ...
```

As a next step, we exchange all connection parameters with environment variables:

``` shell-session
$ export CMEMC_CONFIG_FILE=cmemc.ini
$ export CMEMC_CONNECTION=mycmem
```

This alone allows us to save a lot of typing for a series of commands on the same Corporate Memory instance.

``` shell-session
$ cmemc graph list --raw
[... same output as above ...]
```

But you also can pre-define command options in the same way:

``` shell-session
$ export CMEMC_GRAPH_LIST_RAW=true
```

Again, the same command but --raw is set default.

``` shell-session
$ cmemc graph list
[... same output as above ...]
```

### Example: enable session wide debugging output

Since there is a top level `--debug` option, the corresponding variable name is `CMEMC_DEBUG`:

``` shell-session
$ export CMEMC_DEBUG=true
```

## Configuration environment export from the config file

Beginning with v21.11, cmemc can export a configuration environment from a configuration file to setup an environment for later use with the `config eval` command.

``` shell-session
$ cmemc -c my-cmem.example.org config eval
export CMEM_BASE_URI="https://my-cmem.example.org"
export DI_API_ENDPOINT="https://my-cmem.example.org/dataintegration"
export DP_API_ENDPOINT="https://my-cmem.example.org/dataplatform"
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

This can be used to export a full config.env or to eval it in an environment for other processes:

``` shell-session
$ cmemc -c my-cmem.example.org config eval > config.env
$ eval $(cmemc -c my-cmem.example.org config eval)
```

Please note that the following command has the same effect but needs the cmemc.ini for evaluating the config values for the config section my-cmem.example.org:

``` shell-session
$ export CMEMC_CONNECTION="my-cmem.example.org"
```
