# Vocabs module

*Configuration property: `modules.vocabulary` | Scope: app-wide and per workspace*

The Vocabs module of DataManager is used to manage available vocabularies.

-   js.config.modules.vocabulary
    -   enable
    -   startWith
    -   graphUrl

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.vocabulary.enable | false | no | none | boolean |

Set this property to true to enable the Vocabs module of DataManager.

Note: If this property is set to `false`, all other settings of `modules.vocabulary` are skipped. To use the module you also need to have read access to the graph specified in `js.config.modules.vocabulary.graphUrl` as well as the access control action `urn:eccenca:VocabularyUserInterface` .

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.vocabulary.startWith | false | no | none | boolean |

Set this property to true to load this module as default one after login.

Note: If more than one module has defined `startWith: true` the most left module in Module bar will be set as default.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.vocabulary.graphUrl | none | yes | none | string (URI) |

Use this property to define the target graph for read and write operations.

# Configuration example

``` yaml
js.config.modules:
  vocabulary:
    enable: true
    startWith: false
    graphUrl: https://example.com/example/vocabs/
```