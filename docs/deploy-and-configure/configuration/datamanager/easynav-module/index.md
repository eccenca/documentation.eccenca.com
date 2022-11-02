# EasyNav module

*Configuration property: `modules.easynav` | Scope: app-wide and per workspace*

The EasyNav module of DataManager is used for visual graph data exploration.

-   js.config.modules.easynav
    -   enable
    -   startWith

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.easynav.enable | false | no | none | boolean |

Use this property to enable the EasyNav module of DataManager.

!!! info

    If this property is set to `false` , all other settings of `modules.easynav` are skipped.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.easynav.startWith | false | no | none | boolean |

Use this property to load the EasyNav module as after login.

!!! info

    If more than one module has defined `startWith: true` the top most module in the navigation bar will be set as default.
