---
tags:
    - Configuration
    - Security
    - Keycloak
---
# Configure Corporate Memory with an external Keycloak

## Introduction

Maybe you already operate a central Keycloak deployment in your infrastructure or you want to deploy multiple stages of Corporate Memory with a single Keycloak.
Very often this results in a Keycloak which is deployed in a different domain than your Corporate Memory (such as Corporate Memory is available on `https://cmem.example.com` and Keycloak is available on `https://keycloak.example.com`).
For this scenario, this page provides additional configuration requirements.

## Configuration

### Infrastructure

Depending on your infrastructure around Corporate Memory, you need to change some provisioned HTTP header on the following services:

- Headers for Keycloak URLs:
    - `Access-Control-Allow-Origin: https://cmem.example.com`
- Headers for Corporate Memory URLs:
    - `Access-Control-Allow-Origin: *`

For example, if you are using our helm charts, adapt the followin ingress annotations:

``` yaml
  # KEYCLOAK ingress
  nginx.ingress.kubernetes.io/enable-cors: "true"
  nginx.ingress.kubernetes.io/cors-allow-origin: "https://cmem.example.com"
```

``` yaml
  # Corporate Memory ingress
  nginx.ingress.kubernetes.io/enable-cors: "true"
  nginx.ingress.kubernetes.io/cors-allow-origin: "*"
```

### Keycloak

You have to allow the Corporate Memory domain in the Keycloak settings.

In your realm, in **Clients** go to i.e. `cmem` client and add `https://cmem.example.com/*` to **Valid redirect URIs**:

![Client redirect URI](client-redirect-uri.png){ class="bordered" }

### Corporate Memory

When running the Corporate Memory docker orchestration, you can configure the Keycloak through editing `environments/config.env`.
Then just add the variables below.
You can get those from the `.well-known` url from your instance, e.g. `https://keycloak.example.com/auth/realms/cmem/.well-known/openid-configuration`:

``` bash
OAUTH_AUTHORIZATION_URL=${EXTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/auth
OAUTH_TOKEN_URL=${EXTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/token
OAUTH_JWK_SET_URL=${EXTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/certs
OAUTH_USERINFO_URL=${EXTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/userinfo
OAUTH_LOGOUT_REDIRECT_URL=${EXTERNAL_BASE_URL}/auth/realms/cmem/protocol/openid-connect/logout?redirect_uri=${EXTERNAL_BASE_URL}
OAUTH_CLIENT_ID=cmem
```

![well-known configuration](well-known-config.png){ class="bordered" }

By using variables in the Build (DataIntegration) configuration file `dataintegration.conf`, this environment is used automatically in the docker orchestration:

``` bash
oauth.clientId = ${OAUTH_CLIENT_ID}
oauth.authorizationUrl = ${OAUTH_AUTHORIZATION_URL}
oauth.tokenUrl = ${OAUTH_TOKEN_URL}
oauth.logoutRedirectUrl = ${OAUTH_LOGOUT_REDIRECT_URL}
```

By using variables in the Explore backend (DataPlatform) configuration file `application.yml`, this environment is used automatically in the docker orchestration:

``` yaml
spring.security.oauth2:
  resourceserver:
    anonymous: "${DATAPLATFORM_ANONYMOUS}"
    jwt:
      jwk-set-uri: "${OAUTH_JWK_SET_URL}"
  client:
    registration:
      keycloak:
        client-id: "${OAUTH_CLIENT_ID}"
        authorization-grant-type: "authorization_code"
        client-authentication-method: "basic"
        redirectUri: "${DEPLOY_BASE_URL: 'http://localhost' }/dataplatform/login/oauth2/code/{registrationId}"
        scope: # openid is mandatory as spring somehow does not add it to the userinfo request
          - openid
          - profile
          - email
    provider:
      keycloak:
        jwk-set-uri: "${OAUTH_JWK_SET_URL}"
        authorization-uri: "${OAUTH_AUTHORIZATION_URL}"
        token-uri: "${OAUTH_TOKEN_URL}"
        user-info-uri: "${OAUTH_USERINFO_URL}"
        user-name-attribute: "preferred_username"
```

### cmemc

In cmemc you need to change the Keycloak endpoint, which is used for authentication before connecting to Corporate Memory:

``` ini
KEYCLOAK_BASE_URI=https://keycloak.example.com/
KEYCLOAK_REALM_ID=cmem
```

### Helm charts

In the helm charts, we assumed you deploy Keycloak by using the official charts, either via operator, or via helm charts.
In either way you can configure the base realm path in the global value section:

``` yaml
  # keycloak base url (e.g. https://cmem.example.com/auth)
  keycloakBaseUrl: https://keycloak.example.com/auth/
  # keycloak cmem realm url (e.g. https://cmem.example.com/auth/realms/cmem)
  keycloakIssuerUrl: https://keycloak.example.com/auth/realms/cmem
  # keycloak oauth client id (used for DataPlatform connection and DataIntegration cmem service client)
  oauthClientId: cmem
```
