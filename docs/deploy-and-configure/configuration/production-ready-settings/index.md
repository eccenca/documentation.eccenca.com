---
tags:
    - Configuration
    - Security
---
# Production-ready settings

If you plan to deploy Corporate Memory in an public available environment you should take care about a few issues.

## Changing keycloak client settings

<https://www.keycloak.org/docs/latest/server_admin/index.html#unspecific-redirect-uris_server_administration_guide>

Corporate Memory uses some clients to authenticate against keycloak. For each client you have to adjust the referrer uri. These clients you need to take care of:

- datamanager
- dataintegration

Go to `Cmem-Realm` → `Clients` → `datamanger / dataintegration` and enter your deploy URI like <https://cmem.example.net/>*

![changing-keycloak-client-settings](22-1-keycloak-client-settings.png)

## Password policies

If you create users in Keycloak, make sure users have strong passwords, for this setting up password policies will help. You can take a look here: <https://www.keycloak.org/docs/latest/server_admin/index.html#_password-policies>

## Change Keycloak cookie settings

In Keycloak you should enforce secure flag for keycloak cookies. Go to `Cmem-Realm → Realm Settings → Login` and change Require SSL to "all requests". If you are running without SSL you will no longer be able to login into Corporate Memory.

Once this is done, make sure Dataplatform and Dataintegration uses `HTTPS` to connect to Keycloak. See the usage of `DATAPLATFORM_AUTH_URL, OAUTH_AUTHORIZATION_URL, OAUTH_TOKEN_URL`

![changing-keycloak-cookie-settings](22-1-changing-keycloak-cookie-settings.png)

## Dataplatform CORS settings

Corporate Memors Dataplatform uses `http.cors.allowedOrigins *` as default setting. It is recommended to correctly set the values for the following headers:

- `Access-Control-Allow-Origin`:  specifies which domains can access a site's resources. For example, if ABC Corp. has domains `ABC.com` and `XYZ.com`, then its developers can use this header to securely grant `XYZ.com` access to ABC.com's resources.
- `Access-Control-Allow-Methods`: specifies which HTTP request methods (GET, PUT, DELETE, etc.) can be used to access resources. This header lets developers further enhance security by specifying what methods are valid when XYZ accesses ABC's resources.

Detailed configuration options can be found [here](./../dataplatform/index.md).

This is an example section in dataplatforms application.yml

application.yml

```yaml
## Cross-Origin Resource Sharing (CORS) settings
http:
  cors:
    allowedOrigins:
      - "http://example.org"
    allowedMethods:
      - "OPTIONS"
   - "HEAD"
      - "GET"
      - "POST"
      - "PUT"
      - "DELETE"
      - "PATCH"
```

## DataIntegration CORS settings

DataIntegration uses `cors.config.allowOrigins *` as default setting. 
It is recommended to correctly set the value for the `Access-Control-Allow-Origin` header.
It specifies which domains can access a site's resources.
For example, if ABC Corp. has the domains `ABC.com` and `XYZ.com`, then you can use this header to securely grant `XYZ.com` access to `ABC.com`'s resources.
Detailed configuration options can be found [here](./../dataintegration/index.md).

This is an example section in DataIntegration's `dataintegration.conf`:

```
## Cross-Origin Resource Sharing (CORS) settings
# CORS configuration ###
cors.enabled = true
# List of domains that are allowed to do requests. Wildcard '*' means "All domains".
cors.config.allowOrigins = "*"
# Support cookies, auth etc. for the configured domain under allowOrigins. If set to true, allowOrigins must not have '*' configured.
cors.config.allowCredentials = false
```
