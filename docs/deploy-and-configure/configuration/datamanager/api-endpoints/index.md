# Api endpoints

*Configuration property: `api` | Scope: app-wide and per workspace*

DataManager provides the option to define which endpoints should be used for SPARQL and SPARQL Update requests.

-   js.config.api
    -   sparql
    -   sparqlUpdate
    -   defaultTimeout

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.sparql | '/proxy/:endpointId/sparql' | yes | none | string |

Use this property to define the default endpoint for all SPARQL requests.

!!! info

    When a relative path is set the base url will be added automatically. The placeholder `:endpointId` will be set according to the used workspace defined at [`js.config.workspaces[id].backend.endpointId`](../workspaces).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.sparqlUpdate | '/proxy/:endpointId/update' | yes | none | string |

Use this property to define the default endpoint for all SPARQL Update requests.

!!! info

    When a relative path is set the base url will be added automatically. The placeholder `:endpointId` will be set according to the used workspace defined at [`js.config.workspaces[id].backend.endpointId`](../workspaces).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.defaultTimeout | 60000 | no | none | number |

Set this property to limit the timeout (in milliseconds) requesting data in the tables of DataManager.

## Configuration example

``` yaml
js.config.api:
  sparql: /proxy/:endpointId/sparql
  sparqlUpdate: /proxy/:endpointId/update
  defaultTimeout: 60000
```
