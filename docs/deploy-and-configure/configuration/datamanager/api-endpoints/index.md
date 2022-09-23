# Api endpoints

*Configuration property: `api` | Scope: app-wide and per workspace*

DataManager provides the option to define which endpoints should be used for SPARQL and SPARQL Update requests.

-   js.config.api
    -   [sparql](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/api-endpoints#id-.Apiendpointsv20.06-js.config.api.sparql)
    -   [sparqlUpdate](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/api-endpoints#id-.Apiendpointsv20.06-js.config.api.sparqlUpdate)
    -   [defaultTimeout](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/api-endpoints#id-.Apiendpointsv20.06-js.config.api.defaultTimeout)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.sparql | '/proxy/:endpointId/sparql' | yes | none | string |

Use this property to define the default endpoint for all SPARQL requests.

Note: When a relative path is set the base url will be added automatically. The placeholder `:endpointId` will be set according to the used workspace defined at [`js.config.workspaces[id].backend.endpointId`](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/workspaces#id-.Workspacesv20.10-js.config.workspaces[id].backend.endpointId).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.sparqlUpdate | '/proxy/:endpointId/update' | yes | none | string |

Use this property to define the default endpoint for all SPARQL Update requests.

Note: When a relative path is set the base url will be added automatically. The placeholder `:endpointId` will be set according to the used workspace defined at [`js.config.workspaces[id].backend.endpointId`](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/workspaces#id-.Workspacesv20.10-js.config.workspaces[id].backend.endpointId).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.api.defaultTimeout | 60000 | no | none | number |

Set this property to limit the timeout (in milliseconds) requesting data in the tables of DataManager.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/api-endpoints#id-.Apiendpointsv20.06-Configurationexample)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.api:
  sparql: /proxy/:endpointId/sparql
  sparqlUpdate: /proxy/:endpointId/update
  defaultTimeout: 60000
```