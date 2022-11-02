
## Configuration for connecting to Stardog backend

Configuration example:

This example configures a connection with HTTPS to a remote stardog store (https://remote:5820). All SPARQL updates have a 
timout of 5 minutes configured.

```yaml
store:
  type: stardog
  owlImportsResolution: true
  authorization: REWRITE_FROM
  stardog:
    host: "remote"
    port: 5820
    ssl-enabled: true
    repository: "stardog"
    username: "admin"
    password: "admin"
    updateTimeoutInMilliseconds: 300000
```


***Property: store.type***

The type of the store must be set to "stardog"

| Category | Value |
|--- | ---: |
| Default | stardog |
| Required | true |
| Valid values | STARDOG |
| Environment | STORE_TYPE |

Specific settings for Stardog

***Property: store.stardog.host***

The host of the Stardog database

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_STARDOG_HOST |

***Property: store.stardog.port***

The port of the Stardog database

| Category | Value |
|--- | ---: |
| Default | 5820 |
| Required | false |
| Valid values | integer |
| Environment | STORE_STARDOG_PORT |

***Property: store.stardog.ssl-enabled***

Whether SSL is enabled or not (http vs. https)

| Category | Value |
|--- | ---: |
| Default | false |
| Required | false |
| Valid values | boolean |
| Environment | STORE_STARDOG_SSL_ENABLED |

***Property: store.stardog.repository***

The name of the repository to connect to

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_STARDOG_REPOSITORY |

The user name to connect with

***Property: store.stardog.password***

The credentials of the given user

| Category | Value |
|--- | ---: |
| Default | *none* |
| Required | false |
| Valid values | string |
| Environment | STORE_STARDOG_PASSWORD |

***Property: store.stardog.updateTimeoutInMilliseconds***

Use this property to set the upper bound for update operation execution time. If an update request consists of multiple update operations, the timeout applies to each update operation individually. To support this, the Stardog server must be properly configured.

| Category | Value |
|--- | ---: |
| Default | 3600000 |
| Required | false |
| Valid values | string |
| Environment | STORE_STARDOG_UPDATETIMEOUTINMILLISECONDS |

