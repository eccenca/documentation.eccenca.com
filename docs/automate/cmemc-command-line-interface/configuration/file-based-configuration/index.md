---
title: "cmemc: File-based Configuration"
subtitle: Configuration
icon: material/file-cog-outline
tags:
  - cmemc
---
# File-based Configuration

## Introduction

This page documents how to configure cmemc via configuration files.

cmemc looks for a default configuration file in a location depending on your operating system:

- For Linux, this is `$HOME/.config/cmemc/config.ini`[^1].
- For Windows, this is `%APPDATA%\cmemc\config.ini`.
- For MacOS, this is `$HOME/Library/Application Support/cmemc/config.ini`.

[^1]: More precisely, it is `$XDG_CONFIG_HOME/cmemc/config.ini`, see also the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

If you need to change this location and want to use another config file, you have two options:

- run cmemc with the `--config-file path/to/your/config.ini` option
- set a new config file with the environment variable `CMEMC_CONFIG_FILE`

However, once you start cmemc the first time without any command or option, it will create an empty configuration file at this location and will output a general introduction.


??? example "First cmemc run ..."
    ``` shell-session
    $ cmemc
    Empty config created: /home/user/.config/cmemc/config.ini
    Usage: cmemc [OPTIONS] COMMAND [ARGS]...

      eccenca Corporate Memory Control (cmemc).

      cmemc is the eccenca Corporate Memory Command Line Interface (CLI).

      Available commands are grouped by affecting resource type (such as graph,
      project and query). Each command and group has a separate --help screen
      for detailed documentation. In order to see possible commands in a group,
      simply execute the group command without further parameter (e.g. cmemc
      project).

      If your terminal supports colors, these coloring rules are applied: Groups
      are colored in white; Commands which change data are colored in red; all
      other commands as well as options are colored in green.

      Please also have a look at the cmemc online documentation:

                          https://eccenca.com/go/cmemc

      cmemc is © 2023 eccenca GmbH, licensed under the Apache License 2.0.

    Options:
      -c, --connection TEXT  Use a specific connection from the config file.
      --config-file FILE     Use this config file instead of the default one.
                             [default: /Users/seebi/Library/Application
                             Support/cmemc/config.ini]

      -q, --quiet            Suppress any non-error info messages.
      -d, --debug            Output debug messages and stack traces after errors.
      --version              Show the version and exit.
      -h, --help             Show this message and exit.

    Commands:
      admin       Import bootstrap data, backup/restore workspace or get status.
      config      List and edit configs as well as get config values.
      dataset     List, create, delete, inspect, up-/download or open datasets.
      graph       List, import, export, delete, count, tree or open graphs.
      project     List, import, export, create, delete or open projects.
      query       List, execute, get status or open SPARQL queries.
      vocabulary  List, (un-)install, import or open vocabs / manage cache.
      workflow    List, execute, status or open (io) workflows.
    ```

You can now edit your configuration file and add credentials and URL parameters for your Corporate Memory deployment.
You either search for the configuration manually in your home directory or you can use the `config edit` command, which opens the configuration file in your default text editor (specified by the [`EDITOR` variable](https://wiki.archlinux.org/title/environment_variables#Default_programs)).

``` shell-session
$ cmemc config edit
Open editor for config file /home/user/.config/cmemc/config.ini
```

The rules for the configuration file are similar to a Windows INI file and are explained in detail at [docs.python.org](https://docs.python.org/3/library/configparser.html).

## Examples

Below is a minimal example using the `client_credentials` grant type.

!!! example

    ``` ini
    [my-local]
    CMEM_BASE_URI=http://localhost/
    OAUTH_GRANT_TYPE=client_credentials
    OAUTH_CLIENT_ID=cmem-service-account
    OAUTH_CLIENT_SECRET=...
    ```

This creates a named section (connection identifier) `my-local` which is a connection to a Corporate Memory deployment on `http://localhost/`.
In order to use this connection, you need to use the `--connection / -c` option with this identifier or [set the default connection](../environment-based-configuration/index.md#example-set-a-default-connection) to this configuration.
The authorization will be done with a system account `cmem-service-account` and the given client secret.
Using this combination of configuration parameters is based on a typical installation where all components are available under the same host name.

Another example using `password` grant type.

!!! example

    ``` ini
    [my-local]
    CMEM_BASE_URI=http://localhost/
    OAUTH_GRANT_TYPE=password
    OAUTH_CLIENT_ID=cmemc
    OAUTH_USER=user
    OAUTH_PASSWORD=...
    ```

This creates a named section `my-local`, which is a connection to a Corporate Memory deployment on `http://localhost/`.
The authorization will be done with the given `OAUTH_USER` and `OAUTH_PASSWORD`.

!!! info

    The OAuth 2.0 token endpoint location ([`OAUTH_TOKEN_URI`](#oauth_token_uri)) defaults to `$KEYCLOAK_BASE_URI/realms/$KEYCLOAK_REALM_ID/protocol/openid-connect/token`.
    If Keycloak is exposed to a different domain than Corporate Memory, make sure the variables [`KEYCLOAK_BASE_URI`](#keycloak_base_uri) and [`KEYCLOAK_REALM_ID`](#keycloak_realm_id) are configured correctly.
    Please refer to [Configure Corporate Memory with an external Keycloak](../../../../deploy-and-configure/configuration/keycloak/using-external-keycloak/index.md) for more information.

## Configuration Variables

The above example provides access to an installation where all components (including Keycloak) are deployed with the default URL base.
However, if you need to fine-tune all locations or want to use special functionality, the following configuration parameters can be used.

### Location related

The following configuration variables specify where cmemc can find the relevant HTTP endpoints.
Most of them are optional.

#### CMEM_BASE_URI

This is the base location (HTTP(S) URL) of your eccenca Corporate Memory deployment.

You **always** have to set this configuration variable.

This variable defaults to `http://docker.localhost/`.

#### DI_API_ENDPOINT

This is the base location (HTTP(S) URL) of all Data Integration APIs.

This variable defaults to `$CMEM_BASE_URI/dataintegration/` and usually does **not** need to be set.

#### DP_API_ENDPOINT

This is the base location (HTTP(S) URL) of all Data Platform APIs.

This variable defaults to `$CMEM_BASE_URI/dataplatform/` and usually does **not** need to be set.

#### KEYCLOAK_BASE_URI

This is the base location (HTTP(S) URL) of all Keycloak APIs.

This variable defaults to `$CMEM_BASE_URI/auth/` and usually does **not** need to be set.

#### KEYCLOAK_REALM_ID

This is the identifier of your  Keycloak Realm.

This variable defaults to `cmem` and usually does **not** need to be set.

#### OAUTH_TOKEN_URI

This is the [OpenID Connect (OIDC)](https://en.wikipedia.org/wiki/OpenID#OpenID_Connect_(OIDC)) OAuth 2.0 token endpoint location (HTTP(S) URL).

This variable defaults to `$KEYCLOAK_BASE_URI/realms/$KEYCLOAK_REALM_ID/protocol/openid-connect/token` and usually does **not** need to be set.

### Authentication related

The following configuration variables specify how cmemc can fetch a token to authenticate on the endpoints.

#### OAUTH_GRANT_TYPE

This configures the [OAuth Grant Type](https://oauth.net/2/grant-types/) used to specify how cmemc is able to get a valid token for accessing the Corporate Memory APIs.

Depending on the value of this variable, other authentication-related variables will become mandatory or obsolete.
The following values can be used:

- `client_credentials` - this refers to the [OAuth 2.0 Client Credentials Grant Type](https://oauth.net/2/grant-types/client-credentials/). Mandatory variables for this grant type are `OAUTH_CLIENT_ID`, `OAUTH_CLIENT_SECRET` **or** `OAUTH_CLIENT_SECRET_PROCESS`.
- `password` - this refers to the [OAuth 2.0 Password Grant Type](https://oauth.net/2/grant-types/password/). Mandatory variables for this grant type are `OAUTH_CLIENT_ID`, `OAUTH_USER`, `OAUTH_PASSWORD` **or** `OAUTH_PASSWORD_PROCESS`.
- `prefetched_token` - this value can be used in case you can provide a token that was fetched outside of cmemc. Mandatory variables for this grant type are `OAUTH_ACCESS_TOKEN` **or** `OAUTH_ACCESS_TOKEN_PROCESS`.

This variable defaults to `client_credentials`.

#### OAUTH_CLIENT_ID

This configures the used client ID.
Usually, the following cmemc related clients are configured in the standard Corporate Memory realm:

- `cmem-service-account` is the client which is configured to be used with the `client_credentials` grant type.
- `cmemc` is the client which is configured to be used with the `password` grant type.

You **usually** have to set this configuration variable (exception: you use the `prefetched_token` grant type).

This variable defaults to `cmem-service-account`.

#### OAUTH_USER

This variable specifies your user account.

You **only** need to set this configuration variable if you use the `password` grant type.

This variable defaults to `admin`.

#### OAUTH_PASSWORD

This variable specifies your user password.

You **only** need to set this configuration variable if you use the `password` grant type.

#### OAUTH_CLIENT_SECRET

This variable specifies your client secret (password).

You **only** need to set this configuration variable if you use the `client_credentials` grant type.

#### OAUTH_ACCESS_TOKEN

This variable specifies a pre-fetched access token.

You **only** need to set this configuration variable if you use the `prefetched_token` grant type.

#### OAUTH_PASSWORD_PROCESS

In order to avoid saving credentials in configuration files you can use this optional configuration variable **instead** of the `OAUTH_PASSWORD` variable.

Please refer to [Getting Credentials from external Processes](../getting-credentials-from-external-processes/index.md) for more information.

This variable defaults to `none`.

#### OAUTH_CLIENT_SECRET_PROCESS

In order to avoid saving credentials in configuration files you can use this optional configuration variable **instead** of the `OAUTH_CLIENT_SECRET` variable.

Please refer to [Getting Credentials from external Processes](../getting-credentials-from-external-processes/index.md) for more information.

This variable defaults to `none`.

#### OAUTH_ACCESS_TOKEN_PROCESS

In order to avoid saving credentials in configuration files you can use this optional configuration variable **instead** of the `OAUTH_ACCESS_TOKEN` variable.

Please refer to [Getting Credentials from external Processes](../getting-credentials-from-external-processes/index.md) for more information.

This variable defaults to `none`.

### Network related

#### SSL_VERIFY

Setting this to `false` will disable certification verification (not recommended).

Please refer to [Certificate handling and SSL verification](../certificate-handling-and-ssl-verification/index.md) for more information.

This variable defaults to `true`.

#### REQUESTS_CA_BUNDLE

Setting this to a PEM file allows for using private Certificate Authorities for certificate validation.

Please refer to [Certificate handling and SSL verification](../certificate-handling-and-ssl-verification/index.md) for more information.

This variable defaults to `$PYTHON_HOME/site-packages/certifi/cacert.pem`.

