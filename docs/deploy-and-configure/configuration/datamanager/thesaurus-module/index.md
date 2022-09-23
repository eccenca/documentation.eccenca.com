# Thesaurus module

*Configuration property: `modules.thesaurus` | Scope: app-wide and per workspace*

The Thesaurus module of DataManager is used to manage thesauri or taxonomies with SKOS vocabularies.

-   js.config.modules.thesaurus
    -   [enable](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/thesaurus-module#id-.Thesaurusmodulev20.06-js.config.modules.thesaurus.enable)
    -   [startWith](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/thesaurus-module#id-.Thesaurusmodulev20.06-js.config.modules.thesaurus.startWith)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.thesaurus.enable | false | no | none | boolean |

Set this property to true to enable the Thesaurus module of DataManager.

Note: If this property is set to `false`, all other settings of `modules.thesaurus` are skipped. To use the module you also need to have read access to the graph `js.config.shacl.shapesGraph` as well as the access control action `urn:eccenca:ThesaurusUserInterface` .

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.thesaurus.startWith | false | no | none | boolean |

Set this property to true to load this module as default one after login.

Note: If more than one module has defined `startWith: true` the most left module in Module bar will be set as default.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/thesaurus-module#id-.Thesaurusmodulev20.06-Configurationexample)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.modules:
  thesaurus:
    enable: true
    startWith: false
```