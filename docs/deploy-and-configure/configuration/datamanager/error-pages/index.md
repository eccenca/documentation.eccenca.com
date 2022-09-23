# Error pages

*Configuration property: `errorPages` | Scope: app-wide and per workspace*

DataManager provides the option to customize special user errors.

-   js.config.errorPages
    -   graphAccess
        -   [title](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.graphAccess.title)
        -   [message](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.graphAccess.message)
    -   moduleAccess
        -   [title](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.moduleAccess.title)
        -   [message](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.moduleAccess.message)
    -   workspaceAccess
        -   [title](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.workspaceAccess.title)
        -   [message](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-js.config.errorPages.workspaceAccess.message)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.graphAccess.title | 'Unauthorized User' | no | none | string |

Use this property to define a custom title that is displayed if a user has no read access to any graph of the selected workspace.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.graphAccess.message | 'You are not authorized to use this workspace.' | no | none | string |

Use this property to define a custom message that is displayed if a user has no read access to any graph of the selected workspace.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.moduleAccess.title | 'No module accessible' | no | none | string |

Use this property to define a custom title that is displayed if a user has no permission to any module of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.moduleAccess.message | 'You have no access to any module.' | no | none | string |

Use this property to define a custom message that is displayed if a user has no permission to any module of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.workspaceAccess.title | 'Workspace access problem' | no | none | string |

Use this property to define a custom title that is displayed if the workspace is not accessible.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.errorPages.workspaceAccess.message | 'The configured workspace is not accessible.' | no | none | string |

Use this property to define a custom message that is displayed if the workspace is not accessible.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/error-pages#id-.Errorpagesv20.06-Configurationexample)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.errorPages:
  graphAccess:
    title: Unauthorized User
    message: You are not authorized to use this workspace.
  moduleAccess:
    title: No module accessible
    message: You have no access to any module.
  workspaceAccess:
    title: Workspace access problem
    message:: The configured workspace is not accessible.
```