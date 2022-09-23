# Title helper

*Configuration property: `titleHelper` | Scope: app-wide and per workspace*

DataManager provides the option to define which labels of properties are displayed.

-   js.config.titleHelper
    -   [properties](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/title-helper#id-.Titlehelperv20.06-js.config.titleHelper.properties)
    -   [languages](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/title-helper#id-.Titlehelperv20.06-js.config.titleHelper.languages)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.titleHelper.properties | see below | yes, if `titleHelper.languages` is set | none | list of strings |

Use this property to define an array of properties used for getting titles. The default value is:

``` json
[
  'http://www.w3.org/2004/02/skos/core#prefLabel',
  'http://xmlns.com/foaf/0.1/name',
  'http://purl.org/dc/elements/1.1/title',
  'http://purl.org/dc/terms/title',
  'http://www.w3.org/2000/01/rdf-schema#label'
]
```

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.titleHelper.languages | ['en'] | no | none | list of strings |

Use this property to define an array of languages used for getting titles.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/title-helper#id-.Titlehelperv20.06-Configurationexample)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.titleHelper:
properties:
- "http://xmlns.com/foaf/0.1/name"
- "http://www.w3.org/2000/01/rdf-schema#label"
languages:
- en
- de
```

Note: The order how labels in different languages are displayed is determined by the rank of `properties` combined with all given `languages` , default language english (if not already set) and the path property without any language tag.

In this example ordering is set as following:

``` yaml
- http://xmlns.com/foaf/0.1/name@en
- http://xmlns.com/foaf/0.1/name@de
- http://xmlns.com/foaf/0.1/name
- http://www.w3.org/2000/01/rdf-schema#label@en
- http://www.w3.org/2000/01/rdf-schema#label@de
- http://www.w3.org/2000/01/rdf-schema#label.
```