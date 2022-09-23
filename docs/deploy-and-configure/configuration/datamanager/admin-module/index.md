# Admin module

*Configuration property: `modules.administration` | Scope: app-wide and per workspace*

The Admin module of DataManager is used to manage user access rights.

-   js.config.modules.administration
    -   [enable](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/admin-module#id-.Adminmodulev20.06-js.config.modules.administration.enable)
    -   accessConditions
        -   [graph](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/admin-module#id-.Adminmodulev20.06-js.config.modules.administration.accessConditions.graph)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.administration.enable | true | no | none | boolean |

Set this property to true to enable the Admin module of DataManager.

Note: If this property is set to `false`, all other settings of `modules.administration` are skipped.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.administration.accessConditions.graph | none | yes | none | string (URI) |

Set this property to define the graph of saved access conditions.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/admin-module#id-.Adminmodulev20.06-Configurationexample)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.modules:
  administration:
    enable: true
    accessConditions:
      graph: "urn:elds-backend-access-conditions-graph"
```