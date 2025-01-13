# Admin module

*Configuration property: `modules.administration` | Scope: app-wide and per workspace*

The Admin module of DataManager is used to manage user access rights.

-   js.config.modules.administration
    -   enable
    -   accessConditions
        -   graph

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.administration.enable | true | no | none | boolean |

Set this property to true to enable the Admin module of DataManager.

!!! info

    If this property is set to `false`, all other settings of `modules.administration` are skipped.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.administration.accessConditions.graph | none | yes | none | string (URI) |

Set this property to define the graph of saved access conditions.

## Configuration example

``` yaml
js.config.modules:
  administration:
    enable: true
    accessConditions:
      graph: "https://ns.eccenca.com/data/ac/"
```
