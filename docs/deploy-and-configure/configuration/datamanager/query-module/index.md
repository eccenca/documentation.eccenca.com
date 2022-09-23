# Query module

*Configuration property: `modules.query` | Scope: app-wide and per workspace*

The Query module of DataManager is used to query rdf data directly from store.

-   js.config.modules.query
    -   [enable](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/query-module#id-.Querymodulev20.06-js.config.modules.query.enable)
    -   [graph](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/query-module#id-.Querymodulev20.06-js.config.modules.query.graph)
    -   [startWith](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/query-module#id-.Querymodulev20.06-js.config.modules.query.startWith)
    -   [timeout](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/query-module#id-.Querymodulev20.06-js.config.modules.query.timeout)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.query.enable | true | no | none | boolean |

Set this property to `true` to enable the Query module of DataManager.

Note: If this property is set to `false`, all other settings of modules.query are skipped. To use the module you also need to have read access to the graphs specified in `js.config.modules.vocabulary.graph` and `js.config.shacl.shapesGraph` as well as the access control action `urn:eccenca:QueryUserInterface` .

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.query.graph | none | yes | none | string (URI) |

Use this property to define the target graph for read and write operations.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.query.startWith | false | no | none | boolean |

Set this property to true to load this module as default one after login.

Note: If more than one module has defined `startWith: true` the most left module in Module bar will be set as default.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.query.timeout | 600000 | no | none | number |

Set this property to limit the timeout (in milliseconds) requesting manual queries in Query Module.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/query-module#id-.Querymodulev20.06-Configurationexample)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.modules:
  query:
    enable: true
    startWith: false
    graph: "https://ns.eccenca.com/data/queries/"
    timeout: 600000
```