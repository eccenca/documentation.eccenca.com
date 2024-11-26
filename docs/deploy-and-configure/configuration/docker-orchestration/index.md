---
tags:
    - Configuration
    - Docker
---
# Docker Orchestration

## Introduction

This page describes the configuration for the `docker compose` based orchestration.

The Docker Orchestration (hereafter simply orchestration) is configured via environment files.
In this document we provide an overview on how the environment files are loaded, how to modify the configuration inside those files and available configuration parameters.

## Environment Files: Loading Sequence

The environment files are supplied in the CONFIGFILE environment variable to the make targets inside the orchestration.
For example, in [Scenario: Single Node Cloud Installation](../../installation/scenario-single-node-cloud-installation/index.md) we have created a `prod.env` environment file and created the Corporate Memory instance using `prod.env` configuration:

``` shell-session
$ CONFIGFILE=environments/prod.env make clean-pull-start-bootstrap
```

When you run `make clean-pull-start-bootstrap` target, the Makefile will evaluate and export the environment variables from the `environments/default.env`, your `${CONFIGFILE}` or `environments/config.env` and `environments/scripted-env.mk`:

``` shell-session
$ cat Makefile
...
include ${CONFIGFILE_BASE_DIRECTORY}/default.env
include ${CONFIGFILE}
include ${CONFIGFILE_BASE_DIRECTORY}/scripted-env.mk
export
...
```

The files are loaded exactly in this order and the later env files will overwrite the environment variables from the former env files.
In other words, your `${CONFIGFILE}` will have precedence over `environments/default.env`.
While `environments/scripted-env.mk` has precedence over both `environments/default.env` and your `${CONFIGFILE}`.

## Configuring Docker Orchestration

To configure the orchestration according to your requirements, you need simply to create a file inside `environments/` directory and set the necessary variables there.
For example, to replicate the minimum configuration from `config.env`, you can do the following:

``` shell-session
$ echo "create empty environments/prod.env file"
$ touch environments/prod.env
$ echo "inject necessary variables into the prod.env"
$ echo "CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a" >> environments/prod.env
$ echo "STARDOG_PASSWORD=admin" >> environments/prod.env
$ echo "TRUSTSTOREPASS=Aimeik5Ocho5riuC" >> environments/prod.env
```

This configuration will be sufficient to run the orchestration locally as described in [Scenario: Local Installation](../../installation/scenario-local-installation/index.md):

``` shell-session
$ CONFIGFILE=environments/prod.env make clean-pull-start-bootstrap
```

## Available Configuration Variables

All available configuration environment variables are listed in `environments/default.env` file. In this section we describe the default value and purpose of each of those variables.

### Docker Settings

| Variable | Default Value | Description |
| -------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Docker | | |
| DOCKER_CMD_ADD | (optional) | Additional command line arguments to be supplied to `docker compose` such as `--tlscacert`, `--tlscert`, `--tlskey` or `--tlsverify` |
| ECC_HOST | (internal) | |

### Deployment Settings

| Variable | Default Value | Description |
| ------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| DEPLOYPROTOCOL | http | Deploy protocol: http or https |
| DEPLOYHOST | docker.localhost | Deploy host such as docker.localhost or corporate-memory.example.com |
| PORT | 80 | Port for apache2 to listen on, for SSL configuration see section below. |
| DEST | $(dir $(abspath Makefile))              | Directory where the orchestration is located (by default resolves to the directory where this Makefile is located) |
| APACHE_BASE_FILE          | docker-compose.apache2-exposed.yml      | `docker compose` extension file for apache2, see SSL configuration section below for an example                      |
| APACHE_CONFIG             | default.conf                            | Apache2 virtual host configuration                                                                                 |
| SSLCONF                   | ssl.default.conf                        | Apache2 virtual host configuration for SSL setup                                                                   |
| HTTP_PORT                 | 80                                      | APACHE_HTTP_PORT is used as a standard port 80 in SSL setup                                                        |
| LETSENCRYPT_MAIL          | administration@eccenca.com            | email to be used when requesting letsencrypt certificates                                                          |
| DATAINTEGRATION_BASE_FILE | docker-compose.dataintegration-base.yml | `docker compose` extension file for DataIntegration, see SSL configuration section below for an example              |
| TRUSTSTOREPASS            | (empty)                                 | Truststore password, see self-signed certificates configuration section below for an example                       |

### Project Settings

| Variable            | Default Value      | Description                                                                                                                                                    |
| ------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BOOTSTRAP           | false              | "false" or "true", indicates whether to load the Corporate Memory bootstrap data                                                                               |
| PROJECT_NAME_SUFFIX | (empty) (optional) | will append to the `docker compose` project environment variable [COMPOSE_PROJECT_NAME](https://docs.docker.com/compose/reference/envvars/#compose_project_name) |

### DataManager Settings

| Variable                                       | Default Value            | Description                               |
| ---------------------------------------------- | ------------------------ | ----------------------------------------- |
| DATAMANAGER_CONFIG_WORKSPACES_DEFAULT_NAME     | CMEM Orchestration       | Name of the default DataManager workspace |
| DATAMANAGER_CONFIG_APPPRESENTATION_HEADERNAME  | eccenca Corporate Memory | DataManager header name                   |
| DATAMANAGER_CONFIG_APPPRESENTATION_WINDOWTITLE | eccenca Corporate Memory | DataManager windows title                 |

### DataPlatform Settings

| Variable                       | Default Value         | Description                                                                                                                   |
| ------------------------------ | --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| AUTHORIZATION_ABOX_PREFIX      | <http://eccenca.com/> | ABox prefix defines a prefix for access control lists, changing this can break authorization in the Corporate Memory instance |
| AUTHORIZATION_ABOX_ADMINGROUP  | elds-admins           | Default admin group for the Corporate Memory users                                                                            |
| DATAPLATFORM_CONTEXTPATH       | /dataplatform         | Context path for the dataplatform, meaning that dataplatform will run under `http://dataplatform.host/dataplatform`           |
| DATAPLATFORM_JAVA_TOOL_OPTIONS | -Xms512m -Xmx2g       | Java options, modify to increase memory allocation                                                                            |

### DataIntegration Settings

| Variable                               | Default Value                                                                   | Description                                                                                                                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| DATAINTEGRATION_EXECUTOR               | LocalExecutionManager                                                           | DataIntegration execution.manager.plugin parameter, see [DataIntegration](../../configuration/dataintegration/index.md) manual for more details |
| INTERNAL_BASE_URL                      | ${DEPLOYPROTOCOL}://${DEPLOYHOST} | Used for DATAPLATFORM_URL and OAUTH_TOKEN_URL variables |
| DATAPLATFORM_URL | ${INTERNAL_BASE_URL}${DATAPLATFORM_CONTEXTPATH} | DataIntegration eccencaDataPlatform.url parameter, see [DataIntegration](../../configuration/dataintegration/index.md) manual for more details |
| OAUTH_AUTHORIZATION_URL | ${DEPLOY_BASE_URL}/auth/realms/cmem/protocol/openid-connect/auth | DataIntegration oauth.authorizationUrl parameter, see [DataIntegration](../../configuration/dataintegration/index.md) manual for more details |
| OAUTH_TOKEN_URL | ${INTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/token | DataIntegration oauth.tokenUrl parameter, see [DataIntegration](../../configuration/dataintegration/index.md) manual for more details |
| DATAINTEGRATION_PRODUCTION_CONFIG_FILE | /opt/cmem/eccenca-DataIntegration/dist/etc/dataintegration/conf/dataintegration.conf | Path to DataIntegration configuration file |
| DATAINTEGRATION_JAVA_TOOL_OPTIONS | -Xmx4g | Java options, modify to increase memory allocation |

### Keycloak Settings

| Variable | Default Value | Description |
| ------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| PROXY_ADDRESS_FORWARDING | false | Keycloak proxy forwarding, necessary for SSL configuration |
| KEYCLOAK_AUTH_URL_INTERNAL | `http://keycloak:8080/auth/realms/cmem/protocol/openid-connect/token` (internal) | used in scripts/utils.sh to restore DataIntegration projects |
| CMEM_SERVICE_ACCOUNT_CLIENT_ID | (internal) | used in scripts/utils.sh to restore DataIntegration projects |

### Stardog Settings

| Variable | Default Value | Description |
| -------------------------- | ---------------------------------------- | -------------------------------------------------- |
| STARDOG_SEARCHINDEX_ENABLE | true | Enable or disable stardog search index |
| STARDOG_SERVER_JAVA_ARGS | -Xms2g -Xmx2g -XX:MaxDirectMemorySize=1g | Java options, modify to increase memory allocation |

### Component Versions

| Variable | Default Value | Description |
| ---------------- | ------------- | ----------------------------------------------- |
| DI_VERSION | develop | DataIntegration docker image version to be used |
| DP_VERSION | develop | DataPlatform docker image version to be used |
| DM_VERSION | develop | DataManager docker image version to be used |
| APACHE2_VERSION | v2.6.0 | Apache2 docker image version to be used |
| KEYCLOAK_VERSION | v6.0.1-2 | Keycloak docker image version to be used |
| POSTGRES_VERSION | 11.5-alpine | Postgresql docker image version to be used |
| STARDOG_VERSION | v7.2.0-1 | Stardog docker image version to be used |

## SSL Configuration with Letsencrypt Example

A complete example on how to deploy the Corporate Memory instance on Hetzner with Letsencrypt certificates is described in [Scenario: Single Node Cloud Installation](../../installation/scenario-single-node-cloud-installation/index.md)

``` bash
#!/bin/bash

CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a
STARDOG_PASSWORD=admin
# change DEPLOYHOST to your own value! the one you have configured in your DNS
DEPLOYHOST=corporate-memory.eccenca.dev
PROXY_ADDRESS_FORWARDING=true
DATAINTEGRATION_JAVA_TOOL_OPTIONS=-Xmx4g
DATAPLATFORM_JAVA_TOOL_OPTIONS=-Xms2g -Xmx4g
STARDOG_SERVER_JAVA_ARGS=-Xms2g -Xmx2g -XX:MaxDirectMemorySize=4g

# letsencrypt:
SSLCONF=ssl.letsencrypt.conf
# change MAIL to your own value! use a common system administration mailbox here
LETSENCRYPT_MAIL=administration@eccenca.com

DI_VERSION=v20.03
DP_VERSION=v20.03
DM_VERSION=v20.03
APACHE2_VERSION=v2.6.0
KEYCLOAK_VERSION=v6.0.1-2
POSTGRES_VERSION=11.5-alpine
STARDOG_VERSION=v7.2.0-1

#################################
# Do NOT CHANGE these settings. #
# ###############################
# NOTE:
#  - these settings differ from http setup but should not be altered
#
DEPLOYPROTOCOL=https
PORT=443
APACHE_BASE_FILE=docker-compose.apache2-ssl.yml
APACHE_CONFIG=default.ssl.conf
PROXY_ADDRESS_FORWARDING=true
```

## SSL Configuration with Self-Signed Certificates Example

``` bash
#!/bin/bash

CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a
STARDOG_PASSWORD=admin
TRUSTSTOREPASS=Aimeik5Ocho5riuC

# Set this to your deployhost
DEPLOYHOST=corporate.memory
DATAINTEGRATION_BASE_FILE=docker-compose.dataintegration-ssl.yml

DI_VERSION=v20.03
DP_VERSION=v20.03
DM_VERSION=v20.03
APACHE2_VERSION=v2.6.0
KEYCLOAK_VERSION=v6.0.1-2
POSTGRES_VERSION=11.5-alpine
STARDOG_VERSION=v7.2.0-1

#################################
# Do NOT CHANGE these settings. #
# ###############################
# NOTE:
#  - these settings differ from http setup but should not be altered
#
DEPLOYPROTOCOL=https
PORT=443
APACHE_BASE_FILE=docker-compose.apache2-ssl.yml
APACHE_CONFIG=default.ssl.conf
PROXY_ADDRESS_FORWARDING=true
```
