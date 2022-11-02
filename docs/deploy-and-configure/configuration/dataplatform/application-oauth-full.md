
### Authentication

Access to DataPlatform resources is restricted using OAuth 2.0.

#### Configuration example

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        anonymous: true
        jwt:
          issuerUri: http://keycloak/auth/realms/cmem
```


#### OAuth 2.0 Resource Server

In order to protect access to it’s resources, DataPlatform acts as an OAuth 2.0 resource server accepting and responding to a protected resource request using a JSON Web Token (JWT).

The OAuth 2.0 specification as well as the JSON Web Token specification don’t define any mandatory claims to be contained in a JWT access token. However, if the property spring.security.oauth2.resourceserver.jwt.issuer-uri is set, the iss (issuer) claim is required to be contained in the JWT. It’s value must be equal to the configured issuer URI. Additionally, in order to identify the requesting principal, either the username claim or the clientId claim must be contained in the JWT.


***Property: spring.security.oauth2.resourceserver.anonymous***

Use this property to allow anonymous access to protected resources.

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_ANONYMOUS |

***Property: spring.security.oauth2.resourceserver.jwt.issuerUri***

Use this property to specify the URI that an OpenID Connect Provider asserts as its Issuer Identifier if it supports OpenID Connect discovery.
If this property is set, the iss (issuer) claim is required to be contained in the JWT. The value of the claim has to be the same value as the configured issuer URI.

**Note:** If the authorization server is down when DataPlatform queries it (given appropriate timeouts), then startup will fail. Also, if the authorization server doesn’t support the Provider Configuration endpoint, or if DataPlatform must be able to start up independently from the authorization server, use the property jwk-set-uri instead.


| Category | Value |
|--- | ---: |
| Default | http://docker.localhost/auth/realms/cmem |
| Required | false |
| Valid values | URI to OpenID Connect Provider |
  | Conflicts with | spring.security.oauth2.resourceserver.jwt.jwkSetUri |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_ISSUERURI |

***Property: spring.security.oauth2.resourceserver.jwt.jwkSetUri***

Use this property to specify the JSON Web Key URI to use to verify the JWT token.

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | URI to OpenID Connect Provider |
  | Conflicts with | spring.security.oauth2.resourceserver.jwt.issuerUri |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_JWKSETURI |

Use the following configuration options to specify the claims conveyed by a JWT used to access protected resources of DataPlatform. If nothing is configured, a default configuration is provided with the following configuration

***Property: spring.security.oauth2.resourceserver.jwt.claims.username***

Use this property to specify the claim providing the account name of the user accessing a protected resource.

| Category | Value |
|--- | ---: |
| Default | preferred_username |
| Required | false |
| Valid values | string |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_USERNAME |

***Property: spring.security.oauth2.resourceserver.jwt.claims.groups***

Use this property to specify the claim identifying the roles (authorities) of the user accessing a protected resource.

| Category | Value |
|--- | ---: |
| Default | groups |
| Required | false |
| Valid values | string | list of strings |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_GROUPS |

***Property: spring.security.oauth2.resourceserver.jwt.claims.clientId***

Use this property to specify the claim providing the OAuth 2.0 client ID to which a token was issued.

| Category | Value |
|--- | ---: |
| Default | clientId |
| Required | false |
| Valid values | string |
| Environment | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_CLIENTID |

