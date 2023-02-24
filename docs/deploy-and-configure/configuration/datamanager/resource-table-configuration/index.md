# Resource Table configuration

*Configuration property: `resourceTable`*

DataManager provides the option to configure the Resource Tables.

-   js.config.resourceTable
    -   timeoutDownload
    -   pagination
        -   limit

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.resourceTable.timeoutDownload | 600000 | no | none | number |

Set this property to limit the timeout (in milliseconds) for requesting a file to download in the tables of Query Module.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.resourceTable.`pagination.limit` | 25 | no | none | number |

Set this property to limit the default pagination limit for any Resource Table.

## Configuration example

``` yaml
js.config.shacl:
  shapesGraph: "https://vocab.eccenca.com/shacl/"
```
