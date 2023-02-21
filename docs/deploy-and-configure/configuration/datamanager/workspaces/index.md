# Workspaces

*Configuration property: `workspaces` | Scope: app-wide only*

DataManager provides the option to define pre-configured workspaces a user can select for login.

-   js.config.workspaces
    -   id
        -   name
        -   authorization

            -   type
            -   logoutRedirectUrl
        -   backend
            -   type
            -   url
            -   endpointId
        -   DIWorkspace
            -   enable
            -   url

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].name | none | yes | none | string |

Use this property to define a descriptive name for the workspace that the user sees when selecting a workspace.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.type | none | yes | none | string |

Use this property to define the type of authorization.

!!! info

    Currently, possible values are anonymous and oauth2 . If oauth2 is selected, you need to configure more options as described in section *Authorization*.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].authorization.logoutRedirectUrl | none | no | none | string (URL) |

Use this property to define a page other than the DataManager page that a user is redirected to after logout.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].backend.type | none | yes | none | string |

Use this property to define the type of the data backend.

!!! info

    Currently, the only possible value is `dataplatform`.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].backend.url | none | yes | none | string (URL) |

Use this property to define the base URL of the data backend.

!!! info

    For `js.config.workspaces[id].backend.type: dataplatform` the base URL must not contain "`/`" at the end.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].backend.endpointId | none | yes | none | string |

Use this property to define the identifier of a specific SPARQL endpoint at the data backend.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].DIWorkspace.enable | none | yes | none | true / false |

Use this property to enable/disable the Data Integration menu item in the navigation menu.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.workspaces[id].DIWorkspace.url | none | yes | none | string |

Use this property to define the url where Data Integration is accessible.

## Configuration example

``` yaml
js.config.workspaces:
  # definition for workspace 1
  default:
    name: 'Default Workspace'
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
    DIWorkspace:
      enable: true
      url: /dataintegration/workspace-beta

  # definition for workspace 2
  otherSpace:
    name: 'Another Workspace'
    authorization:
      type: 'anonymous'
    backend:
      type: 'dataplatform'
      url: '<dataplatform_uri>'
      endpointId: 'default'
    DIWorkspace:
      enable: true
      url: /dataintegration/workspace-beta

```

Most configuration options that are applied application-wide can be overruled by specific workspace configurations. To overrule an app-wide configuration include the specific configuration option in the workspace definition as shown in the example below:

``` yaml
js.config.workspaces:
  # definition for workspace 1
  default:
    name: 'Default Workspace'
    authorization:
      type: 'anonymous'
    backend:
      type: 'dataplatform'
      url: 'https://<dataplatform_uri>'
      endpointId: 'default'
    # overwrites app-wide appPresentation configuration for this workspace refer to chapter App presentation
    appPresentation:
      windowTitle: 'Example Name'

js.config.appPresentation:
  faviconUrl: https://example.com/example/favicon.png
  windowTitle: DataManager
  logoUrl: https://example.com/example/logo.png
  headerName: Datamanager
```

In the example above, the properties `js.config.workspaces and js.config.appPresentation` are configured. The property `js.config.appPresentation.windowTitle` in `js.config.workspaces` changes the title of DataManager from '*DataManager*' to '*Example Name*' for this specific workspace. Users logged in to this workspace see *Example Name* as the window title, because the workspace configuration overrules the app-wide configuration.
