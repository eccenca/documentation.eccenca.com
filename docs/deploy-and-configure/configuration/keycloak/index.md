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

!!! NOTE: A realm can be im-/exported. However exports will not contain user credentials. So be aware not losing data.

To create a realm use the drop down menu for choosing a realm on the left side.

  -  Create a realm `cmem`
    - Select "Realm settings"
      - "General" tab:
      - Change HTML Display name to `<span class="ecc-logo"></span>Corporate Memory`
    - "Themes" tab
      - Switch realm's login theme to `eccenca`
      - Switch realm's account theme to `eccenca`

## Client configuration

There are two (three) different kinds of clients used by Corporate Memory. One client is used by DM/DP/DI to authenticate a user for using the UI. The other client is for using the command line client as technical user. Depending on the environment there might be an other use case when running background schedules, then a third client, also as technical user, might be useful.

### Add a client by importing

Add a client called `cmem` by select clients, then create client. The client described below can also be imported. Please download file below, then select "Import client". For `cmem-service-account` you have to edit the file an replace the secret or regenerate the secret in keycloak after the import. Files:

  - [client configuration for using the ui](cmem.json)
  - [client configuration with credentials for technical account](cmem-service-account.json)


![Dialog import cmem client](import-client-cmem.png)

### Add a client manually (Login into UI)

This client is intended for usage by DataManager/Dataplatform and DataIntegration (user login):

![Dialog create cmem client](createClient_1.png)

  - Client type: OpenID Connect
  - Client ID: i.e. `cmem`, you need to remember this and use this later
  - Name and Description: fill as you like
  - Select 'Next'
  - Client authentication: Off
  - Authorization: Off
  - until v22.2:
    - Enable `Standard Flow Enabled` (enables OAuth 2.0 Authorization Code Flow)
    - Enable `Implicit Flow Enabled`
  - from v23.1:
    - Enable `Standard Flow Enabled` (enables OAuth 2.0 Authorization Code Flow)
  - Save

![Dialog create cmem client](createClient_2.png)

The dialog above closes and you land on the configuration sections of this client:

  - Valid redirect URIs: Add the adequate URL pattern (wildcard `http://example.org/*` works) to `Valid Redirect URIs` (`*` for testing purposes is acceptable)
  - Switch the Tabs to 'Client scopes' and select the first scope (i.e.: cmem-service-account-dedicated)

![Dialog select cmem-service-account-dedicated](createClient_11.png)
![Dialog create mapper](createClient_4.png)
![Dialog create mapper](createClient_5.png)

  - `Configure a new mapper`
  - select Mapper Type `User Client Role`
    - Name `groups`
    - Token Claim Name `groups`
    - Disable `Full group path`
    - Disable `Add to ID token`
    - Enable `Add to access token`
    - Enable `Add to user info`
  - Save

![Dialog create mapper](createClient_6.png)


  - In Corporate Memory configuration until v22.2:
    - Configure this client ID under `js.config.workspaces.default.authorization.oauth2.clientId` in DataManager's configuration file (Datamanager needs implicit flow)
    - Configure  this client ID under `oauth.clientId = "cmem"` in DataManager's configuration file (Dataintegration needs standard flow)
  - In Corporate Memory configuration from v23.1:
    - Configure this client ID in the environments with the name `OAUTH_CLIENT_ID` in `/environments/config.env`


### Add a client manually (Technical Account)

This client is intended for internal use by DataIntegration (scheduler super-user) and data import purposes ([cmemc](https://documentation.eccenca.com/latest/automate/cmemc-command-line-interface))


  - Client type: OpenID Connect
  - Client ID: i.e. `cmem-service-account`, you need to remember this and use this later
  - Name and Description: fill as you like
  - Select 'Next'
  - Client authentication: On
  - Authorization: Off
  - Authentication flow: enable `Service accounts roles`
  - Save

  - Go to `Credentials` and configure `Client Id and Secret`, copy the client secret for later usage
![Dialog create role](createClient_7.png)
![Dialog create role](createClient_8.png)

  - Go to `Roles` and add the `elds-admins` role
  - Select `Action` and `Add associated roles`
  - Select `Filter by client` then 
![Dialog create role](createClient_9.png)
![Dialog create role](createClient_10.png)

  - Go to `Service Account Roles -> Client Roles (cmem-service-account)` and add the `elds-admins` role to `Assigned Roles`

![Dialog select cmem-dedicated](createClient_3.png)
![Dialog create mapper](createClient_13.png)

  - `Configure a new mapper`
  - select Mapper Type `User Client Role`
    - Name `roles`
    - Token Claim Name `groups`
    - Enable `Add to ID token`
    - Enable `Add to access token`
    - Enable `Add to user info`
  - Save

![Dialog create mapper](createClient_14.png)

  - Go to tab `Service account roles` 
  - select the link in the center `To manage detail and group mappings, click on the username service-account-YOUR_CLIENT_ID`

![Dialog add role to client](createClient_15.png)

  - Go to tab `Role mapping` and select `Assign role`
  - Change the filter to `Filter by clients` and select the new Client ID, i.e `cmem-service-account`

![Dialog add role to client](createClient_16.png)
![Dialog add role to client](createClient_17.png)

  - In Corporate Memory configuration:
    - If DataIntegration schedulers are required, configure this client id and secret under the properties`workbench.superuser.client` and `workbench.superuser.clientSecret` in DataIntegration's configuration file or
    - in docker-compose-orchestration you can edit this in the environment as:
        - CMEM_SERVICE_ACCOUNT_CLIENT_ID=cmem-service-account
        - CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=YourSecret
        - DATAINTEGRATION_CMEM_SERVICE_CLIENT=cmem-service-account
        - DATAINTEGRATION_CMEM_SERVICE_CLIENT_SECRET=YourSecret
    - in helm this value is defined by: 
        - DATAINTEGRATION_CMEM_SERVICE_CLIENT_SECRET: `{{ .Values.global.cmemClientSecret }}`
        - DATAINTEGRATION_CMEM_SERVICE_CLIENT: `{{ .Values.global.cmemClientId }}`
    - For cmemc you can your this with `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`

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
        - groups: `local-users`
      - `admin:admin`
        - groups: `local-admin`
