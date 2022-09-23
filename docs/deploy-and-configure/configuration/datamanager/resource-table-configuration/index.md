# Resource Table configuration

*Configuration property: `resourceTable`*

DataManager provides the option to configure the Resource Tables.

-   js.config.resourceTable
    -   [timeoutDownload](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/resource-table-configuration#id-.ResourceTableconfigurationv20.10-js.config.resourceTable.timeoutDownload)
    -   pagination
        -   [limit](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/resource-table-configuration#id-.ResourceTableconfigurationv20.10-js.config.resourceTable.pagination.limit)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.resourceTable.timeoutDownload | 600000 | no | none | number |

Set this property to limit the timeout (in milliseconds) requesting a file to download in the tables of Query Module.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.resourceTable.`pagination.limit` | 25 | no | none | number |

Set this property to limit the default pagination limit on any Resource Table.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/resource-table-configuration#id-.ResourceTableconfigurationv20.10-Configurationexample)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.shacl:
  shapesGraph: "https://vocab.eccenca.com/shacl/"
```