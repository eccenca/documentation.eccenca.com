# Workspaces Authorization

DataManager provides several types of authorization.

-   js.config.workspaces
    -   id
        -   authorization
            -   type
            -   oauth2
                -   grantType
                -   authorizeUrl
                -   clientId
                -   tokenUrl
                -   clientSecret

If you want to use OAuth2, you need to define `authorization.type` to `oauth2` as well as specify further configuration parameters within the `oauth2` parameter:

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.oauth2.grantType | none | yes, if authorization.type is `oauth2` | none | `implicit` or `authorization_code` |

Use this property to define the OAuth2 workflow. Depending on what value you choose you have to configure different properties:

-   `implicit` : `authorizeURL` and `clientId`
-   `authorization_code` : `authorizeUrl` , `clientId` , `tokenUrl` , and as optional property `clientSecret`

Note: It is recommended to use the implicit workflow, as DataManager is a client application.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.oauth2.authorizeUrl | none | yes, if `authorization.type` is `oauth2` | none | string (URL) |

Use this property to define the authorization endpoint URL of the OAuth2 authorization server.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.oauth2.clientId | none | yes, if `authorization.type` is `oauth2` | none | string |

Use this property to define the client identifier issued by the OAuth2 authorization server.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.oauth2.tokenUrl | none | yes, if` authorization.oauth2.grantType` is '*authorization_code*' | none | string (URL) |

Use this property to define the authorization token endpoint URL of the OAuth2 authorization server.

Note: This property is only needed for `js.config.workspaces[id].authorization.oauth2.grantType=authorization_code`.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.oauth2.clientSecret | none | yes, if `authorization.oauth2.grantType` is '*authorization_code*' | none | string |

Use this property to define a passphrase for OAuth2 client authorization. Usually, this property is not required. It must only be set if the authorization server expects a client secret.

## Configuration example

The two examples below show how a backend configuration can look like as for example for an eccenca DataPlatform using different authorization options.

DataPlatform configuration with anonymous access:

``` yaml
js.config.workspaces:
  default:
    name: 'Default Workspace (anonymous)'
    authorization:
      type: 'anonymous'
    backend:
      type: 'dataplatform'
      url: 'https://<dataplatform_uri>'
      endpointId: 'default'
```

DataPlatform configuration with implicit OAuth2 workflow:

``` yaml
js.config.workspaces:
  default:
    name: 'Default endpoint (oauth-implicit)'
    authorization:
      type: 'oauth2'
      oauth2:
        clientId: 'eldsClient'
        grantType: 'implicit'
        authorizeUrl: 'https://<dataplatform_uri>/oauth/authorize'
    backend:
      type: 'dataplatform'
      url: 'https://<dataplatform_uri>'
      endpointId: 'default'
```

DataPlatform with authorization code OAuth2 workflow:

``` yaml
js.config.workspaces:
  default:
    name: 'Default endpoint (oauth-implicit)'
    authorization:
      type: 'oauth2'
      oauth2:
        clientId: 'eldsClient'
        grantType: 'authorization_code'
        authorizeUrl: 'https://<dataplatform_uri>/oauth/authorize'
        tokenUrl: 'https://<dataplatform_uri>/oauth/token'
        clientSecret: 'secret'
    backend:
      type: 'dataplatform'
      url: 'https://<dataplatform_uri>'
      endpointId: 'default'
```