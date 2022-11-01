---
hide:
  - toc
---

| Property | Environment | Default | Required | Valid values|
| --- | --- | --- | --- | --- |
| spring.security.oauth2.resourceserver.anonymous | SPRING_SECURITY_OAUTH2_RESOURCESERVER_ANONYMOUS  | false| false | boolean |
| spring.security.oauth2.resourceserver.jwt.issuerUri | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_ISSUERURI  | <http://docker.localhost/auth/realms/cmem>| false | URI to OpenID Connect Provider |
| spring.security.oauth2.resourceserver.jwt.jwkSetUri | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_JWKSETURI  | *none*| false | URI to OpenID Connect Provider |
| spring.security.oauth2.resourceserver.jwt.claims.username | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_USERNAME  | preferred_username| false | string |
| spring.security.oauth2.resourceserver.jwt.claims.groups | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_GROUPS  | groups| false | string | list of strings |
| spring.security.oauth2.resourceserver.jwt.claims.clientId | SPRING_SECURITY_OAUTH2_RESOURCESERVER_JWT_CLAIMS_CLIENTID  | clientId| false | string |
