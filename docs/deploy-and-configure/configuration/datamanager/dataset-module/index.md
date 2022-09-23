# Dataset module

*Configuration property: `modules.datasets` | Scope: app-wide and per workspace*

The Dataset module of DataManager is used to manage datasets and their attached resources.

-   js.config.modules.datasets
    -   [enable](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/dataset-module#id-.Datasetmodulev20.06-js.config.modules.datasets.enable)
    -   [startWith](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/dataset-module#id-.Datasetmodulev20.06-js.config.modules.datasets.startWith)
    -   [graphUrl](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/dataset-module#id-.Datasetmodulev20.06-js.config.modules.datasets.graphUrl)
    -   dataintegration
        -   [url](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/dataset-module#id-.Datasetmodulev20.06-js.config.modules.datasets.dataintegration.url)
        -   [project](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/dataset-module#id-.Datasetmodulev20.06-js.config.modules.datasets.dataintegration.project)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.datasets.enable | false | no | none | boolean |

Set this property to `true` to enable the Dataset module of DataManager.

Note: If this property is set to `false` , all other settings of `modules.datasets` are skipped. To use the module you also need to have read access to the graphs specified in `js.config.modules.vocabulary.graphUrl `and `js.config.shacl.shapesGraph` as well as the access control action `urn:eccenca:di`.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.datasets.startWith | false | no | none | boolean |

Set this property to `true` to load this module as default one after login.

Note: If more than one module has defined` startWith: true` the most left module in Module bar will be set as default.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.datasets.graphUrl | none | yes | none | string (URI) |

Use this property to define the target graph for read and write operations.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.datasets.dataintegration.url | none | yes | none | string (URL) |

Use this property to define the URL of DataIntegration that is needed for dataset workflows.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.datasets.dataintegration.project | none | yes | none | string |

Use this property to define the name of the DataIntegration project.

## Configuration example

``` yaml
js.config.modules:
  datasets:
    enable: true
    startWith: false
    graphUrl: https://example.com/example/datasets/
    dataintegration:
      url: https://example.com/dataintegration/
      project: your_project_name
```