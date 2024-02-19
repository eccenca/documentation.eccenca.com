---
tags:
    - Configuration
---

## Configuration for connecting to Virtuoso backend

Configuration example:

This example configures a connection with HTTPS to a remote Virtuoso store (https://remote:8080).

```yaml
store:
  type: virtuoso
  authorization: REWRITE_FROM
  virtuoso:
    host: "remote"
    ssl-enabled: true
    port: 8080
    username: "admin"
    password: "admin"
    databasePort: 1111
```


***Property: store.type***

The type of the store must be set to "virtuoso"

| Category | Value |
|--- | ---: |
| Default | virtuoso |
| Required | true |
| Valid values | VIRTUOSO |
| Environment | STORE_TYPE |

Specific settings for Virtuoso

***Property: store.virtuoso.host***

The host of the Virtuoso server

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_VIRTUOSO_HOST |

***Property: store.virtuoso.port***

The HTTP port of the Virtuoso server

| Category | Value |
|--- | ---: |
| Default | 8080 |
| Required | false |
| Valid values | integer |
| Environment | STORE_VIRTUOSO_PORT |

***Property: store.virtuoso.databasePort***

The database port of the Virtuoso server for direct access to the JDBC database

| Category | Value |
|--- | ---: |
| Default | 1111 |
| Required | false |
| Valid values | integer |
| Environment | STORE_VIRTUOSO_DATABASEPORT |

***Property: store.virtuoso.ssl-enabled***

Whether SSL is enabled or not (http vs. https)

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | string |
| Environment | STORE_VIRTUOSO_SSL_ENABLED |

***Property: store.virtuoso.username***

The user name to connect with

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_VIRTUOSO_USERNAME |

***Property: store.virtuoso.password***

The credentials of the given user

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_VIRTUOSO_PASSWORD |

