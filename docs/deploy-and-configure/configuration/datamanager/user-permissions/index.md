# User permissions

*Configuration property: `userPermissions`*

DataManager provides the option to define user rights on the Workspace page.

-   js.config.userPermissions
    -   [allowCreateWorkspace](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/user-permissions#id-.Userpermissionsv20.06-js.config.userPermissions.allowCreateWorkspace)
    -   [allowSelectWorkspace](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/user-permissions#id-.Userpermissionsv20.06-js.config.userPermissions.allowSelectWorkspace)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.userPermissions.allowCreateWorkspace | true | no | none | boolean |

When this property is set to `true` the user has the right to manually create new workspaces on the Workspace page.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.userPermissions.allowSelectWorkspace | true | no | none | boolean |

When this property is set to `true` the user has the right to manually select an existing workspace. This property can only be used when the [`js.config.userPermissions.allowCreateWorkspace`](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/user-permissions#id-.Userpermissionsv20.06-js.config.userPermissions.allowCreateWorkspace) property is set `true`.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/user-permissions#id-.Userpermissionsv20.06-Configurationexample)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.userPermissions:
  allowCreateWorkspace: true
  allowSelectWorkspace: true
```