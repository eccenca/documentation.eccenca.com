# Shacl configuration

*Configuration property: `shacl`*

DataManager provides the option to configure shacl.

-   js.config.shacl
    -   [shapesGraph](#shacl-configuration)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.shacl.shapesGraph | none | yes | none | string (URL) |

Define in which graph shacl shapes exists.

# Configuration example

``` yaml
js.config.shacl:
  shapesGraph: "https://vocab.eccenca.com/shacl/"
```