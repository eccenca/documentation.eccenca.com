---
tags:
    - Configuration
    - Security
---
# Keycloak

## Introduction

This page documents important steps in order to configure Keycloak as an authentication backend for Corporate Memory.

!!! info
    You do not need these instruction in case you followed the documentation on [Scenario: Local Installation](./../../installation/scenario-local-installation/index.md) or [Scenario: Single Node Cloud Installation](./../../installation/scenario-single-node-cloud-installation/index.md) (in this case, everything was done automatically). However, in case you need to integrate Corporate Memory with an existing Keycloak, this page may help you. Please also have the [Keycloak - Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/) ready :smile:

## Realm configuration

In order to separate all configuration

- Add new realm `cmem`
      - Switch realm's login theme to `eccenca`
          - Change Display name to `CMEM`
          - Change HTML Display name to `<span class="ecc-logo"></span>Corporate Memory`

## Client configuration

- Add a client called `cmem-oauth2-client`

      - This client is intended for usage by DataManager and DataIntegration (user login)
      - Configure this client ID under `oauth.clientId` in DataIntegration's configuration file
      - Configure this client ID under `js.config.workspaces.default.authorization.oauth2.clientId` in DataManager's configuration file
      - Enable `Standard Flow Enabled` (enables OAuth 2.0 Authorization Code Flow)
      - Enable `Implicit Flow Enabled`
      - Add the adequate URL pattern (wildcard `http://example.org/*` works) to `Valid Redirect URIs` (`*` for testing purposes is acceptable)
      - Save
      - Go to `Mappers`
        - Click `Create`
            - Name `groups`
            - Mapper Type `Group Membership`
            - Token Claim Name `groups`
            - Disable `Full group path`
            - Disable `Add to ID token`
            - Enable `Add to access token`
        - (Only for DP < 19.10.1) Click `Create`
            - Name `DataPlatform audience`
            - Mapper Type `Audience`
            - Included Client Audience --> "Select One" (do not touch it)
            - Included Custom Audience `dataplatform`
            - Disable `Add to ID token`
            - Enable `Add to access token`

- Add client called `cmem-service-account`

      - This client is intended for internal use by DataIntegration (scheduler super-user) and data import purposes ([cmemc](https://documentation.eccenca.com/latest/automate/cmemc-command-line-interface))
      - Set the `Access Type` to `confidential`
      - Go to `Settings` and enable `Service Accounts Enabled` (enables OAuth 2.0 Client Credentials Flow)
      - Save
      - Go to `Credentials` and configure `Client Id and Secret`
      - If DataIntegration schedulers are required, configure this client id and secret under the properties`workbench.superuser.client` and `workbench.superuser.clientSecret` in DataIntegration's configuration file
      - For the importer add the client secret to `docker-compose.importer.yml`
      - Go to `Roles` and add the `elds-admins` role
      - Go to `Service Account Roles -> Client Roles (cmem-service-account)` and add the `elds-admins` role to `Assigned Roles`
      - Go to `Mappers`
          - Click `Create`
            - Name `roles`
            - Mapper Type `User Client Role`
            - Client ID `cmem-service-account`
            - Token Claim Name `groups`
            - Enable `Add to access token`
          - (Only for DP < 19.10.1) Click `Create`
            - Name `DataPlatform audience`
            - Mapper Type `Audience`
            - Included Client Audience --> "Select One" (do not touch it)
            - Included Custom Audience `dataplatform`
            - Disable `Add to ID token`
            - Enable `Add to access token`

## Groups configuration

- Go to `Groups`
      - Add the following groups:
        - `elds-admins`
        - Any groups provided by your user management system (e.g. LDAP) that must be recognized/mapped by Keycloak
              - In CHO, `local-users`, `local-admins`

## Users configuration

- This applies to the [Docker Orchestration](./../docker-orchestration/index.md), for other setups consult the [Keycloak manual](https://www.keycloak.org/docs/latest/server_admin/).
- Go to `Users`
- Add the following users and assign their groups respectively (for each user go to credentials, add password and disable `Temporary`)
      - `user:user`
      - groups: `local-users` and `group_user_a` (legacy group)
      - `admin:admin`
