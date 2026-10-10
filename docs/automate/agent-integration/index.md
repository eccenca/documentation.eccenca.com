---
title: "Agent Integration: Automate Corporate Memory with AI Agents"
icon: material/robot-outline
status: new
tags:
  - Automate
  - Integration
  - Security
---
# Agent Integration

## Introduction

This page describes how to let an AI agent, such as a coding agent in a terminal, work with eccenca Corporate Memory.
It compares the three mechanisms an agent can use to control Corporate Memory and gives configuration recipes for concrete agent products.

The recipes use `https://your-cmem.example.org` as the base URL.
Replace it with the base URL of the Corporate Memory deployment.

## Choose a control mechanism

An agent can control Corporate Memory through the Model Context Protocol (MCP) servers, through the REST APIs and through the command line client cmemc.

| | MCP | API | cmemc |
| --- | --- | --- | --- |
| What the agent uses | Tools that the server advertises | HTTP endpoints described by an OpenAPI specification | Shell commands |
| Discovery | The agent lists the available tools and their parameters | The agent or developer reads the specification | The agent reads `cmemc --help` and `cmemc <group> --help`, or the whole manual from `cmemc manual --format markdown-single-page` |
| Authentication | OAuth sign-in as a user, or a bearer token | Bearer token | A cmemc connection |
| Requires | An agent that supports MCP | Code that sends HTTP requests | An agent that can run shell commands |
| Fits | Interactive exploration and authoring | Custom integrations and services | Repeatable scripts, bulk operations, backups and pipelines |

### MCP

An MCP client lists the tools of a server and calls them on request of the model.
No glue code is needed, and the tool descriptions come from the server.
Corporate Memory exposes three MCP servers:

| Server | Component | Endpoint | Purpose |
| --- | --- | --- | --- |
| `cmem-build` | Build (DataIntegration) | `/dataintegration/mcp` | Inspect, author and run projects, datasets, transformations and workflows |
| `cmem-explore` | Explore (DataPlatform) | `/dataplatform/mcp/streamable` | Work with the Knowledge Graph |
| `cmem-marketplace` | eccenca Marketplace | `/marketplace/mcp` | Find, inspect and install packages, and validate package manifests |

The names of the servers are free to choose.
The Build MCP server is part of Build (DataIntegration) since v26.2.
It inspects the workspace, describes plugins and task types, previews data and, when changes are allowed, creates and runs tasks.
The Marketplace MCP server is part of [eccenca Marketplace](../../distribution/marketplace/index.md) since v26.2.8, and is reachable where that component is deployed, under the root path of its deployment.

!!! info

    The Build and Marketplace MCP servers are enabled by default and offer only read-only tools.
    `com.eccenca.di.assistant.McpConfig.readOnly` controls this for Build, and `ECC_MARKETPLACE_MCP_READ_ONLY` for Marketplace, where it decides whether the tools that install and uninstall packages are registered at all.
    The default does not apply to the API or cmemc: an agent that uses them is limited only by the permissions of its account.
    See [Allow changes through the Build MCP server](#allow-changes-through-the-build-mcp-server).

### API

The [Build (DataIntegration) APIs](../../develop/dataintegration-apis/index.md) and the [Explore backend APIs](../../develop/dataplatform-apis/index.md) publish an OpenAPI specification.
An agent that writes or runs its own HTTP client uses them directly.
The API gives the most control, but the agent has to know the endpoints and handle authentication itself.
It is the only mechanism in which the agent handles the token value itself, see [Protect the token](#protect-the-token).

### cmemc

An agent with shell access can run [cmemc](../cmemc-command-line-interface/index.md).
Commands are grouped by resource type and each command documents itself with `--help`.
`cmemc manual --format markdown-single-page` writes the complete command reference to standard output, which gives an agent the whole command surface in one step.
Options such as `--id-only` and `--raw` produce output that is suited for further processing, see [Scripting with cmemc](../cmemc-command-line-interface/scripting-with-cmemc/index.md).
The agent works with the permissions of the configured cmemc connection.

## Authentication and credentials

### Choose a method

The available methods depend on the mechanism.
The MCP servers accept an OAuth sign-in or a bearer token, and the API accepts a bearer token.
cmemc resolves the credential of its [connection](../cmemc-command-line-interface/configuration/file-based-configuration/index.md) itself, so the agent never handles the token value.

The two token methods work as follows:

- **OAuth sign-in:** The agent opens a browser window and the user signs in to Keycloak.
  The agent receives an access token and refreshes it without further interaction.
  This method needs an agent that supports OAuth for MCP servers.
- **Bearer token:** The agent sends a fixed token in the `Authorization` header.
  This method works with any agent that supports custom headers, but the token expires.

The OAuth sign-in uses the `cmem` Keycloak client, which is a public client with the standard flow enabled.
The recipes name its client ID, because Keycloak rejects the dynamic client registration that an agent attempts when no client ID is given.
Depending on the agent, the client ID is a command line option or an entry in its configuration file.
In a deployment that does not use the shipped `cmem` client, use the ID of the client that the web interface uses.

### Protect the token

A token from `cmemc admin token` expires after the access token lifetime of the realm, which is 10 minutes by default.
After that, Corporate Memory rejects the requests and the agent needs a fresh token.
`cmemc admin token --ttl` outputs the remaining lifetime of the token.

For an agent that depends on a bearer token, create a dedicated Keycloak client instead of reusing the account of a person:

1. Create a client as described in [Add the `cmem-service-account` client](../../deploy-and-configure/configuration/keycloak/index.md#add-the-cmem-service-account-client), with a different name such as `cmem-agent`.
2. Give the client only the roles and [access conditions](../../deploy-and-configure/configuration/access-conditions/index.md) that the agent needs.
3. Set a longer access token lifespan in the advanced settings of the client.
4. Create a cmemc connection for the client with `OAUTH_GRANT_TYPE=client_credentials`, and fetch the token with `cmemc -c cmem-agent admin token`.

!!! warning

    A token in a configuration file, such as `mcp_config.json`, is stored in plain text, and a longer lifetime extends the time in which a leaked token is usable.
    An agent that writes a token into a request or a script sends that token to its model provider with the rest of the conversation.
    Keep the token lifespan as short as the use case allows and restrict the client to the permissions the agent needs.
    Pass the token to generated code through an environment variable instead of embedding the value, and keep it out of committed files.

## Recipes

=== "Claude Code"

    Claude Code discovers the OAuth configuration of the server and supports the sign-in directly.

    1. Register the two MCP servers for the current user:

        ``` shell-session
        $ claude mcp add --scope user --transport http --client-id cmem cmem-explore https://your-cmem.example.org/dataplatform/mcp/streamable
        $ claude mcp add --scope user --transport http --client-id cmem cmem-build https://your-cmem.example.org/dataintegration/mcp
        ```

    2. Start `claude` and enter `/mcp`.
    3. Select a server and start the authentication.
    4. Sign in to Corporate Memory in the browser window that opens.

    The `--scope` option controls where Claude Code stores the registration:

    - `user`: for all projects of the current user
    - `local`: for the current project and the current user (default)
    - `project`: in a `.mcp.json` file in the project directory, which can be committed

    With `--scope project`, the registration for the Build server looks like this:

    ``` json title=".mcp.json"
    {
      "mcpServers": {
        "cmem-build": {
          "type": "http",
          "url": "https://your-cmem.example.org/dataintegration/mcp",
          "oauth": {
            "clientId": "cmem"
          }
        }
      }
    }
    ```

=== "Codex"

    Codex registers the server first and signs in with a separate command.

    1. Register the two MCP servers:

        ``` shell-session
        $ codex mcp add cmem-explore --oauth-client-id cmem --url https://your-cmem.example.org/dataplatform/mcp/streamable
        $ codex mcp add cmem-build --oauth-client-id cmem --url https://your-cmem.example.org/dataintegration/mcp
        ```

    2. Sign in to each server:

        ``` shell-session
        $ codex mcp login cmem-explore
        $ codex mcp login cmem-build
        ```

        On a machine without a browser, add `--no-browser`.
        The command prints the authorization URL and accepts the callback URL.

    The registration is stored in `~/.codex/config.toml`:

    ``` toml title="~/.codex/config.toml"
    [mcp_servers.cmem-build]
    url = "https://your-cmem.example.org/dataintegration/mcp"

    [mcp_servers.cmem-build.oauth]
    client_id = "cmem"
    callback_url = "http://127.0.0.1/callback/<random-path>"
    ```

    Codex can also read a bearer token from an environment variable, which keeps the token out of the configuration file:

    ``` shell-session
    $ codex mcp add cmem-build --bearer-token-env-var CMEM_TOKEN --url https://your-cmem.example.org/dataintegration/mcp
    $ export CMEM_TOKEN=$(cmemc -c your-config admin token)
    ```

    The variable has to be set again after the token expires, see [Protect the token](#protect-the-token).

=== "Antigravity CLI"

    The [Antigravity CLI](https://antigravity.google/docs/cli) (`agy`) does not discover the OAuth configuration of the server.
    Pass a bearer token in a header instead.

    1. Fetch an access token with cmemc:

        ``` bash
        TOKEN=$(cmemc -c your-config admin token)
        ```

    2. Register the server with the token:

        ``` shell-session
        $ agy mcp add --header "Authorization: Bearer $TOKEN" --type http cmem-build https://your-cmem.example.org/dataintegration/mcp
        ```

        Flags must come before the server name.

    The registration, including the token, is stored in `~/.gemini/config/mcp_config.json`:

    ``` json title="~/.gemini/config/mcp_config.json"
    {
      "mcpServers": {
        "cmem-build": {
          "disabled": false,
          "headers": {
            "Authorization": "Bearer <token>"
          },
          "serverUrl": "https://your-cmem.example.org/dataintegration/mcp"
        }
      }
    }
    ```

    The token expires, see [Protect the token](#protect-the-token).

=== "Mistral Vibe"

    Vibe reads the OAuth configuration of the server, but it takes the client ID from its configuration file instead of a command line option.

    1. Register the two MCP servers without signing in:

        ``` shell-session
        $ vibe mcp add cmem-explore --no-login --url https://your-cmem.example.org/dataplatform/mcp/streamable
        $ vibe mcp add cmem-build --no-login --url https://your-cmem.example.org/dataintegration/mcp
        ```

    2. Add `client_id` to the `auth` table of each server in `~/.vibe/config.toml`:

        ``` toml title="~/.vibe/config.toml"
        [[mcp_servers]]
        url = "https://your-cmem.example.org/dataintegration/mcp"
        name = "cmem-build"
        transport = "streamable-http"

        [mcp_servers.auth]
        type = "oauth"
        scopes = []
        client_id = "cmem"
        ```

    3. Start `vibe` and enter `/mcp login cmem-build`.
    4. Sign in to Corporate Memory in the browser window that opens.

    Without `client_id`, Vibe registers a client dynamically, and Keycloak rejects the request with `Policy 'Trusted Hosts' rejected request to client-registration service`.

    Vibe can also read a bearer token from an environment variable:

    ``` shell-session
    $ vibe mcp add cmem-build --api-key-env CMEM_TOKEN --url https://your-cmem.example.org/dataintegration/mcp
    $ export CMEM_TOKEN=$(cmemc -c your-config admin token)
    ```

    The variable has to be set again after the token expires, see [Protect the token](#protect-the-token).

=== "cmemc"

    Any agent that can run shell commands needs no MCP registration to use cmemc.
    Configure a [cmemc connection](../cmemc-command-line-interface/configuration/file-based-configuration/index.md) and name it in the instructions of the agent, see [Instructions for the agent](#instructions-for-the-agent).

## Instructions for the agent

A registration connects an agent to Corporate Memory, but it does not tell the agent how to use it.
An instruction file in the project does:

``` text title="AGENTS.md"
Use `cmemc -c your-config` to work with Corporate Memory.
Run `cmemc --help` and `cmemc <group> --help` to discover commands.
Use `--id-only` and `--raw` for machine-readable output.
```

The file name depends on the agent, for example `CLAUDE.md` for Claude Code or `AGENTS.md` for Codex.

The [cmem-package-template](https://github.com/eccenca/cmem-package-template) goes further than a single file.
Package repositories generated from it ship agent rules and authoring skills for Marketplace packages, which read the manifest format from the Marketplace MCP server.

## Permissions of the agent

An agent acts with the permissions of the account that signs in, of the account that owns the bearer token, or of the configured cmemc connection.
A dedicated account or client with limited permissions therefore bounds what an agent can do, whichever mechanism it uses.

### Allow changes through the Build MCP server

The Build MCP server offers only read-only tools: it inspects the workspace but does not create, change, delete or execute anything.
The authoring, deletion and execution tools are exposed after setting `com.eccenca.di.assistant.McpConfig.readOnly = false` in the Build configuration.
`com.eccenca.di.assistant.McpConfig.enabled = false` disables the server, and requests then return 404.

!!! warning

    With the read-only mode off, an agent can delete projects and run workflows with the permissions of the authenticated account.
    Use a dedicated account or client with limited permissions, and review the actions of the agent.
