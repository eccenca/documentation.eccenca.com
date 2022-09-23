# Shacl configuration

*Configuration property: `shacl`*

DataManager provides the option to configure shacl.

-   js.config.shacl
    -   [shapesGraph](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/shacl-configuration#id-.Shaclconfigurationv20.06-js.config.shacl.shapesGraph)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.shacl.shapesGraph | none | yes | none | string (URL) |

Define in which graph shacl shapes exists.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/shacl-configuration#id-.Shaclconfigurationv20.06-Configurationexample)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.shacl:
  shapesGraph: "https://vocab.eccenca.com/shacl/"
```