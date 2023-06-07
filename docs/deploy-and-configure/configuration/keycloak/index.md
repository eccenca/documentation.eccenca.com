---
tags:
    - Configuration
    - Security
    - Keycloak
---
# Keycloak

## Introduction

This page documents important steps in order to configure Keycloak as an authentication backend for Corporate Memory.
The screenshots displayed in this documentation were taken from Keycloak v20 using the `keycloak.v2` theme.


!!! info

    You do not need these instruction in case you followed the documentation on [Scenario: Local Installation](./../../installation/scenario-local-installation/index.md) or [Scenario: Single Node Cloud Installation](./../../installation/scenario-single-node-cloud-installation/index.md) (in this case, everything was done automatically).
    However, in case you need to integrate Corporate Memory with an existing Keycloak, this page may help you.
    Please also have the [Keycloak - Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/) ready :smile:

## Realm configuration

!!! warning

    A realm can be im-/exported.
    However, exported realms will not contain user credentials.
    So be aware not losing data.

To create a realm, use the drop down menu for choosing a realm on the left side.

  -  Create a realm `cmem`
    - Select **Realm settings**
      - **General** tab:
      - Change HTML Display name to `<span class="ecc-logo"></span>Corporate Memory`
    - **Themes** tab
      - Switch realm's login theme to `eccenca`
      - Switch realm's account theme to `eccenca`

## Client configuration

Clients are used to link users and groups managed in keycloak to Corporate Memory. There are two (three) different kinds of clients used by Corporate Memory:

- One client is used by DM/DP/DI to authenticate a user for using the UI (usually named `cmem`).
- The other client is for using the command line client as a technical user (usually named `cmem-service-account`).
  Depending on the environment, there might be an other use case when running background schedules, then a third client, also as technical user, might be useful.

### Explaining client roles and groups

Corporate Memory can set up access conditions for users or groups which is described at [Access Conditions](./../access-conditions/index.md). To map users or groups from keycloak into Corporate Memory ACLs. These clients needs to have mappers attached to each client.

- For in the first kind of client (`cmem` here), the groups a user belongs to needs to get attached by the client. This is done by a **Group Membership** mapper (described below). Here we attach  each group a user is assigned in keycloak to its authentication process so Corporate Memory is aware of the same user and group name for setting up the ACLs.

- Keycloak does not allow us to add groups for the second kind (technical accounts as `cmem-service-account`) so we are using **ROLES** for this. By creating a mapper from roles to groups we can allow Corporate Memory to read roles as groups attached to these clients tokens as well.

In our default setup in helm or docker-compose deployments we often refer to `elds-admins` role or group acting as default admin group. Every user in this group has all possible rights no matter which ACLs in Corporate Memory are set. This is by default configured in Dataplatform configuration or as environment variable `AUTHORIZATION_ABOX_ADMINGROUP=elds-admins`, also see [Dataplatform configuration authorization](./../dataplatform/application-full/#authorization).


### Add clients by importing the JSON exports

Add a client named `cmem` by select clients, then create client.
The client described below can also be imported.
Please download the file below, then select **Import client**.
For the `cmem-service-account` client you have to edit the file and replace the secret or regenerate the secret in keycloak after the import.

Available files:

  - [client configuration for using the ui (`cmem`)](cmem.json)
  - [client configuration with credentials for technical account (`cmem-service-account`)](cmem-service-account.json)

![Dialog import cmem client](import-client-cmem.png){ class="bordered" }

### Create client `cmem` manually (for web interface)

This client is intended for the usage with DataManager, Dataplatform and DataIntegration (user login):

![Dialog create cmem client](createClient_1.png){ class="bordered" }

  - **Client type**: OpenID Connect
  - **Client ID**: i.e. `cmem`, you need to remember this and use this later
  - **Name** and **Description**: fill as you like
  - Select **Next**
  - **Client authentication**: Off
  - **Authorization**: Off
  - Enable **Standard Flow Enabled** (enables OAuth 2.0 Authorization Code Flow)
  - Before v23.1:
    - Additionally enable **Implicit Flow Enabled**
  - **Save**

![Dialog create cmem client](createClient_2.png){ class="bordered" }

The dialog above closes and you land on the configuration page of this client:

  - **Valid redirect URIs**: Add the correct URL pattern (wildcard `http://example.org/*` works) to `Valid Redirect URIs` (`*` for testing purposes can be used as well)
  - Switch the Tabs to **Client scopes** and select the first scope (i.e.: `cmem-dedicated`)

![Dialog select cmem-service-account-dedicated](createClient_11.png){ class="bordered" }
![Dialog create mapper](createClient_4.png){ class="bordered" }
![Dialog create mapper](createClient_5.png){ class="bordered" }

  - Configure a new mapper (**Client** -> **Client Scopes** -> **Add / Select Client Scope** -> **Add Mapper**)
    - select Mapper Type **Group Membership**
    - **Name** `groups`
    - **Token Claim Name** `groups`
    - Disable **Full group path**
    - Disable **Add to ID token**
    - Enable **Add to access token**
    - Enable **Add to user info**
  - **Save**

![Dialog create mapper](createClient_6.png){ class="bordered" }

  - In Corporate Memory configuration until v22.2:
    - Configure this client ID under `js.config.workspaces.default.authorization.oauth2.clientId` in DataManager's configuration file (Datamanager needs implicit flow)
    - Configure  this client ID under `oauth.clientId = "cmem"` in DataManager's configuration file (Dataintegration needs standard flow)
  - In Corporate Memory configuration from v23.1:
    - Configure this client ID in the environments with the name `OAUTH_CLIENT_ID` in `/environments/config.env` (defaults to `cmem` if not set)


### Create a client manually (Technical Account)

This client is intended for internal use by DataIntegration (scheduler super-user) and data import purposes ([cmemc](https://documentation.eccenca.com/latest/automate/cmemc-command-line-interface)).

This descriptions can also be used to create clients with different permissions than admins. For this, just create a different role name later, and create an access condition with this groups name in Corporate Memory as it is described in [Access Conditions](./../access-conditions/index.md).

![Dialog create role](createClient_7_1.png){ class="bordered" }
![Dialog create role](createClient_7_2.png){ class="bordered" }
![Dialog create role](createClient_7_3.png){ class="bordered" }

  - **Client type**: OpenID Connect
  - **Client ID**: i.e. `cmem-service-account`, you need to remember this and use this later
  - **Name** and **Description**: fill as you like
  - Select **Next**
  - **Client authentication**: On
  - **Authorization**: Off
  - **Authentication flow**: only enable `Service accounts roles`, the rest can be disabled
  - **Save**

  - Go to **Credentials** and configure **Client Id and Secret**, copy the client secret for later usage

![Dialog create role](createClient_7_4.png){ class="bordered" }

  - Go to **Roles** and select **Create role** to create the `elds-admins` role

![Dialog create role](createClient_7.png){ class="bordered" }
![Dialog create role](createClient_8.png){ class="bordered" }
 
  - Select **Action** and **Add associated roles**

![Dialog create role](createClient_9.png){ class="bordered" }

  - Select **Filter by client** then

![Dialog create role](createClient_10.png){ class="bordered" }

  - In this dialog select the client by name which you are currently configuring ( here `cmem-service-account`) and then **Assign**

![Dialog create role](createClient_10_1.png){ class="bordered" }

  - Go back to **Client details** i.e. by using the top navigation
  - In the **Roles** tab you now see your created role here

![Dialog create role](createClient_10_2.png){ class="bordered" }

  - Switch the Tabs to **Client scopes** and select the first scope (i.e.: `cmem-service-account-dedicated`)

![Dialog create mapper](createClient_11.png){ class="bordered" }

  - select **Add mapper** -> **By configuration**

![Dialog create mapper](createClient_13_1.png){ class="bordered" }

  - select Mapper Type `User Client Role`
    - **Name** `roles`
    - **Token Claim Name** `groups`
    - Enable **Add to ID token**
    - Enable **Add to access token**
    - Enable **Add to user info**
  - **Save**

![Dialog create mapper](createClient_13.png){ class="bordered" }

![Dialog create mapper](createClient_14.png){ class="bordered" }

  - After **Save** go back to **Client details**
  - Go to tab **Service account roles** tab
  - Select the link in the center **To manage detail and group mappings, click on the username service-account-YOUR_CLIENT_ID**

![Dialog add role to client](createClient_15.png){ class="bordered" }

  - Go to tab **Role mapping** and select **Assign role**

![Dialog add role to client](createClient_16.png){ class="bordered" }

  - Change the filter to **Filter by clients** and select the new Client ID, i.e `cmem-service-account`

![Dialog add role to client](createClient_16_2.png){ class="bordered" }
![Dialog add role to client](createClient_16_1.png){ class="bordered" }


![Dialog add role to client](createClient_17.png){ class="bordered" }




### Corporate Memory configuration after setting up clients:
  - If **DataIntegration** schedulers are required, configure this client id and secret under the properties `workbench.superuser.client` and `workbench.superuser.clientSecret` in DataIntegration's configuration file or
  - in docker-compose-orchestration you can edit this in the environment as:
      ``` bash
        CMEM_SERVICE_ACCOUNT_CLIENT_ID=cmem-service-account
        CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=YourSecret
        DATAINTEGRATION_CMEM_SERVICE_CLIENT=cmem-service-account
        DATAINTEGRATION_CMEM_SERVICE_CLIENT_SECRET=YourSecret
      ```
  - in helm this value is defined by:
      ``` yaml
        DATAINTEGRATION_CMEM_SERVICE_CLIENT_SECRET: {{ .Values.global.cmemClientSecret }}
        DATAINTEGRATION_CMEM_SERVICE_CLIENT: {{ .Values.global.cmemClientId }}
      ```
  - For **cmemc** you can configure this with `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`.

## Groups configuration

- Go to **Groups** and add the following groups:
  - `elds-admins`
  - Any groups provided by your user management system (e.g. LDAP) that must be recognized/mapped by Keycloak
  - In Corporate Memory docker orchestration, `local-users`, `local-admins`

## Users configuration

- This applies to the [Docker Orchestration](./../docker-orchestration/index.md), for other setups consult the [Keycloak manual](https://www.keycloak.org/docs/latest/server_admin/).
- Go to `Users`
- Add the following users and assign their groups respectively (for each user go to credentials, add password and disable `Temporary`)
  - `user:user`
    - groups: `local-users`
  - `admin:admin`
    - groups: `local-admin`

