---
title: "Marketplace: Configuration"
tags:
    - Configuration
    - Marketplace
---
# Marketplace

## Introduction

This page describes how to configure eccenca Marketplace, the service behind the [Marketplace](../../../distribution/marketplace/index.md) module of eccenca Corporate Memory.
The service stores versioned [Marketplace Packages](../../../develop/marketplace-packages/index.md), serves their metadata and files, and installs or uninstalls them in a connected Corporate Memory deployment.

One process serves the web application, the REST API below `/api` with its interactive documentation at `/docs`, and the MCP endpoint for agents at `/mcp`, all below the configured [root path](#sub-path-deployment).

The same image runs in different roles, which the settings select:

| Role | Settings | Purpose |
| ---- | -------- | ------- |
| Registry | `ECC_MARKETPLACE_LOCAL_MARKETPLACE=true` (default) | Hosts its own packages: publish, list, download, delete. |
| Installer | `ECC_MARKETPLACE_CMEM_BASE_URL` set | Installs packages into Corporate Memory, from its own registry and from the Marketplace Servers in `ECC_MARKETPLACE_MARKETPLACE_URLS`. |
| Both | both of the above | A registry bound to one Corporate Memory deployment. |
| Central Marketplace Server | `ECC_MARKETPLACE_LICENSE_MODE=LICENSE_TOKEN` without a local license | A registry for many Corporate Memory deployments, each identified by the license it sends, such as `https://eccenca.market`. |

## Where the settings are set

The service reads its settings from environment variables with the prefix `ECC_MARKETPLACE_`.
It does not read a configuration file.
All effective settings are written to the log at startup, with secrets masked.

How the variables reach the container depends on the deployment:

- **Helm chart**: The chart derives the variables from the `marketplace.config.*`, `marketplace.service.contextPath`, `marketplace.persistence.*` and `global.marketplaceClientId` values.
    See [(Optional) Marketplace](../../installation/scenario-k8s-deployment/index.md#optional-marketplace) in the Kubernetes scenario.
- **Docker orchestration**: The `marketplace` service in `docker-compose.yml` maps the `MARKETPLACE_*` variables of the environment files to the `ECC_MARKETPLACE_*` variables.
    Override them in the environment file of the deployment, as described in [Docker Orchestration](../docker-orchestration/index.md).
- **Plain container**: Set the `ECC_MARKETPLACE_*` variables directly, as in the following example.

```yaml title="docker-compose.yml"
services:
  marketplace:
    image: "docker-registry.eccenca.com/eccenca-marketplace:v26.3.0"
    restart: "unless-stopped"
    environment:
      - "ECC_MARKETPLACE_DATA_DIR=/data"
      - "ECC_MARKETPLACE_ROOT_PATH=/marketplace"
      - "ECC_MARKETPLACE_KEYCLOAK_URL=https://cmem.example.org/auth/"
      - "ECC_MARKETPLACE_KEYCLOAK_REALM=cmem"
      - "ECC_MARKETPLACE_KEYCLOAK_ADMIN_GROUP=local-admins"
      - "ECC_MARKETPLACE_KEYCLOAK_CLIENT_ID=marketplace"
      - "ECC_MARKETPLACE_SESSION_SECRET=<random string>"
      - "ECC_MARKETPLACE_CMEM_BASE_URL=https://cmem.example.org/"
    volumes:
      - "./data/:/data"
    ports:
      - "5050:5050"
```

The container listens on port `5050` with plain HTTP and is meant to run behind a reverse proxy.

An empty value counts as not set for `ROOT_PATH`, `PUBLIC_URL`, `LICENSE_FILE`, `LICENSE_TEXT`, `BOOTSTRAP_DIR` and `LICENSING_PUBLIC_KEY`.
An unset `${VAR}` substitution in a Compose file is therefore harmless.

## Required settings

The service does not start without the following settings.
It also contacts Keycloak at startup and does not start when the realm configuration cannot be fetched.

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_KEYCLOAK_URL` | (required) | Base URL of Keycloak, for example `https://cmem.example.org/auth/`. |
| `ECC_MARKETPLACE_KEYCLOAK_REALM` | (required) | ID of the Keycloak realm, usually `cmem`. |
| `ECC_MARKETPLACE_KEYCLOAK_ADMIN_GROUP` | (required) | Keycloak group whose members publish and delete packages, see [Permissions](#permissions). Several groups are given as a comma-separated list, for example `local-admins,package-publishers`. |

## Login and Keycloak client

Browser users log in through Keycloak with the OpenID Connect authorization code flow and keep a session cookie.
API clients and agents send a bearer token of the same realm instead and need none of the following settings.

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_KEYCLOAK_CLIENT_ID` | (empty) | ID of the Keycloak client used for the login, usually `marketplace`. |
| `ECC_MARKETPLACE_KEYCLOAK_CLIENT_SECRET` | (empty) | Secret of that client. Leave it empty for a public client. |
| `ECC_MARKETPLACE_SESSION_SECRET` | random at every start | Key that signs the session cookie. |

The client needs the following properties in Keycloak:

- **Standard flow** enabled.
- A valid redirect URI of `<base URL><root path>/auth/callback`, for example `https://cmem.example.org/marketplace/auth/callback`.
- A group membership mapper that writes the group names into the `groups` claim of the access token.

The [Keycloak](../keycloak/index.md) page provides a `marketplace.json` client configuration for import, which defines a public client with these properties.
The Helm chart and the Docker orchestration use this public client and leave the secret empty.
Set `ECC_MARKETPLACE_KEYCLOAK_CLIENT_SECRET` only when the client is created as a confidential client.

!!! warning "Set a session secret"

    Without `ECC_MARKETPLACE_SESSION_SECRET` the service generates a new key at every start.
    Every restart then logs all users out, and several replicas do not accept the sessions of each other.

## Permissions

| Action | Required |
| ------ | -------- |
| Read the name and version (`GET /api/info`), the allowed licenses, the manifest schema and package badges | Nothing. |
| Check a manifest (`POST /api/manifest`) | Nothing. |
| List, inspect and download packages | A login in the realm. A central Marketplace Server accepts the license sent with the request instead. |
| Publish a package version, delete a package or a version | Membership in one of the groups named by `ECC_MARKETPLACE_KEYCLOAK_ADMIN_GROUP`. |
| Install and uninstall packages in Corporate Memory, list installed packages | A login in the realm. |

The service has no Corporate Memory account of its own.
It passes the token of the logged-in user on to Corporate Memory, so an installation runs with the rights of that user.
The service and the Corporate Memory deployment therefore use the same Keycloak realm, and the [access conditions](../access-conditions/index.md) of Corporate Memory decide what the user is allowed to change.

## Storage

Packages are stored as plain files, without a database.

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_DATA_DIR` | a temporary directory | Directory the packages are stored in. |
| `ECC_MARKETPLACE_LOCAL_MARKETPLACE` | `true` | Whether the instance hosts its own registry. With `false` the package routes are not available and the instance only installs from the Marketplace Servers in `ECC_MARKETPLACE_MARKETPLACE_URLS`. |
| `ECC_MARKETPLACE_BOOTSTRAP_DIR` | (unset) | Directory of `.cpa` package archives that are published into the registry at startup. |

!!! warning "Use a persistent data directory"

    The default data directory is created anew at every start.
    Without `ECC_MARKETPLACE_DATA_DIR` pointing to a persistent volume, the registry is empty after every restart.

The data directory has the following layout:

```text
<data-dir>/
  <package-id>.json                  package metadata
  <package-id>/
    <package-id>-v<version>.json     manifest of one version
    <package-id>-v<version>.zip      archive of one version
```

A copy of this directory is a complete backup.
The top-level `<package-id>.json` files are rebuilt from the latest manifest of each package at every start.

The bootstrap directory ships curated packages with an instance in an isolated environment.
A version that is already published is skipped, an archive that fails is written to the log and skipped, and a directory that does not exist is ignored.
The order of the file names does not matter: an archive whose dependency is published later is retried after the others.

## Sub-path deployment

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_ROOT_PATH` | `/` | Path the application is served under, for example `/marketplace`. |

With a root path of `/marketplace`, every route, the API documentation and the login routes live below this prefix, and requests without the prefix are answered with `404`.
The reverse proxy has to forward the prefix unchanged:

```apache
ProxyPass        /marketplace/ http://marketplace:5050/marketplace/
ProxyPassReverse /marketplace/ http://marketplace:5050/marketplace/
```

Do not strip or rewrite the prefix in the proxy.
The redirect URI of the Keycloak client moves with the prefix, see [Login and Keycloak client](#login-and-keycloak-client).

## User interface and Marketplace Servers

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_FRONTEND` | `true` | Whether the web application is served. With `false` a static home page is served instead. |
| `ECC_MARKETPLACE_TITLE` | `eccenca Corporate Memory Marketplace` | Name of the instance, shown in the API documentation and returned by `GET /api/info`. |
| `ECC_MARKETPLACE_DESCRIPTION` | (a short product text) | Description shown in the API documentation and on the static home page. |
| `ECC_MARKETPLACE_MARKETPLACE_URLS` | `https://eccenca.market` | Comma-separated list of the Marketplace Servers offered to users. |

`ECC_MARKETPLACE_MARKETPLACE_URLS` also restricts where packages are installed from: an installation from any other Marketplace Server is refused.
An empty value offers no remote Marketplace Server, which leaves only the own registry of the instance.

```bash
ECC_MARKETPLACE_MARKETPLACE_URLS=https://eccenca.market,https://marketplace.example.org
```

!!! info "Lists before v26.3.1"

    The comma-separated form of `ECC_MARKETPLACE_MARKETPLACE_URLS` and several groups in `ECC_MARKETPLACE_KEYCLOAK_ADMIN_GROUP` require Marketplace v26.3.1 or newer.
    Earlier versions accept one admin group, and the Marketplace Servers only as a JSON list, for example `["https://eccenca.market"]`.
    The JSON list is still accepted but deprecated.

## Corporate Memory integration

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_CMEM_BASE_URL` | (unset) | Base URL of the Corporate Memory deployment that packages are installed into. |
| `ECC_MARKETPLACE_CMEM_EXPLORE_ENDPOINT_URL` | `<base URL>/dataplatform/` | URL of the Explore (DataPlatform) API. |
| `ECC_MARKETPLACE_CMEM_BUILD_ENDPOINT_URL` | `<base URL>/dataintegration` | URL of the Build (DataIntegration) API. |
| `ECC_MARKETPLACE_PUBLIC_URL` | (unset) | URL under which the instance is reachable from the outside, including the root path. |

Setting `ECC_MARKETPLACE_CMEM_BASE_URL` enables installing, upgrading and uninstalling packages and the view of the installed packages.
Without it, the instance is a registry only.

`ECC_MARKETPLACE_PUBLIC_URL` is optional.
It is recorded as the origin of a package that is installed from the own registry of the instance, and it is the address under which the MCP endpoint is announced.

## MCP endpoint

The service provides a Model Context Protocol (MCP) endpoint at `<root path>/mcp`, see [Agent Integration](../../../automate/agent-integration/index.md).

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_MCP` | `true` | Whether the endpoint is served. |
| `ECC_MARKETPLACE_MCP_READ_ONLY` | `true` | Whether only the reading tools are offered. With `false` the tools that install and uninstall packages are offered as well. |

Every request needs a bearer token of the realm, and the tools act with the rights of that user.

## License enforcement

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_LICENSE_MODE` | `ANONYMOUS` | `ANONYMOUS` checks no license. `LICENSE_TOKEN` requires a valid eccenca license for the package routes and the Corporate Memory routes. |
| `ECC_MARKETPLACE_LICENSE_FILE` | (unset) | Path to the mounted license file (`license.asc`). |
| `ECC_MARKETPLACE_LICENSE_TEXT` | (unset) | The license itself: the content of the `.asc` file or a base64 encoding of it. Takes precedence over the file. |
| `ECC_MARKETPLACE_LICENSE_MODE_ALLOWED_LICENSES` | (empty) | Comma-separated list of license checksums that are allowed to use a central Marketplace Server. |
| `ECC_MARKETPLACE_LICENSE_HEADER` | `x-eccenca-auth` | Name of the header in which clients send their license. |
| `ECC_MARKETPLACE_LICENSING_PUBLIC_KEY` | the eccenca licensing key | Public key the licenses are verified against. |

In `LICENSE_TOKEN` mode the license comes from one of two sources:

- **A license configured on the instance**, with `LICENSE_FILE` or `LICENSE_TEXT`.
    This is the setup of an instance that belongs to a Corporate Memory deployment, and the default of the Helm chart and the Docker orchestration.
    The instance also sends this license, encrypted, to the Marketplace Servers in `ECC_MARKETPLACE_MARKETPLACE_URLS`.
    Without a configured license, packages of a Marketplace Server that enforces licenses cannot be listed or installed.
- **A license sent by the client with every request**, when neither of the two settings is set.
    This is the setup of a central Marketplace Server.
    `ECC_MARKETPLACE_LICENSE_MODE_ALLOWED_LICENSES` restricts it to an explicit list of licenses, each given as `checksum` or `checksum:label`.

Calculate the checksum of a license with the following command:

```bash
grep '^licenseSignature' license.asc | cut -d= -f2- | base64 -d | sha256sum
```

Treat `ECC_MARKETPLACE_LICENSE_TEXT` as a secret.
Change `ECC_MARKETPLACE_LICENSE_HEADER` and `ECC_MARKETPLACE_LICENSING_PUBLIC_KEY` only for testing: cmemc and the web application send the default header name.

## Outgoing TLS connections

The following settings apply to the requests the service sends to Keycloak, Corporate Memory and other Marketplace Servers.
They do not affect the certificate the service itself is served with.

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `ECC_MARKETPLACE_SSL_VERIFY` | `true` | Whether TLS certificates are verified. The variable is also read as `SSL_VERIFY`. |
| `ECC_MARKETPLACE_CUSTOM_CERTIFICATE_DIRECTORY` | (unset) | Directory of additional CA certificates (`*.crt`, `*.pem`) mounted into the container. |
| `ECC_MARKETPLACE_CERTIFICATE_DIRECTORY` | `/tmp/cacerts` | Writable directory for the merged CA bundle. |

For a private certificate authority, keep the verification enabled and mount the CA certificates.
At start, the container merges the certificates found in `ECC_MARKETPLACE_CUSTOM_CERTIFICATE_DIRECTORY` with the public certificate authorities and uses the result for all outgoing connections.
The step is skipped when the variable is unset or the directory is not mounted.

!!! warning "Do not disable the verification in production"

    `ECC_MARKETPLACE_SSL_VERIFY=false` accepts any certificate and is meant for development setups with self-signed certificates only.
