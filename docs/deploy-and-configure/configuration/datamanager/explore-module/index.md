# Explore module

*Configuration property: `modules.explore` | Scope: app-wide and per workspace*

The Explore module of DataManager is used for graph data exploration.

-   js.config.modules.explore
    -   enable
    -   startWith
    -   overallSearchQuery
    -   mapServer
        -   url
        -   ext
    -   graphlist
        -   defaultGraph
        -   hideSearch
        -   whiteList
    -   navigation
        -   defaultClass
        -   topQuery
        -   subQuery
        -   searchQuery
        -   listQuery
        -   itemsPerPage
    -   details
        -   properties
            -   enable
        -   usage
            -   enable
        -   references
            -   enable
        -   turtle
            -   enable
        -   history

        -   enable

        -   statistics
            -   enable
            -   sunburst
                -   enable
    -   visualization
        -   enable
        -   webvowlConfig
            -   filter
                -   literals
                -   relations
                -   solitarySubclasses
                -   classDisjointness
                -   setOperators
                -   degreeOfCollapsing
            -   mode
                -   dynamicLabelWidth
                -   pickAndPin
                -   nodeScaling
                -   compactNotation
                -   colorExternals
            -   export
                -   json
                -   svg
            -   gravity
                -   classDistance
                -   dataTypeDistance
            -   reset
            -   pause
            -   search
    -   externalTools
        -   toolX
            -   enable
            -   tabname
            -   iframeUrlTemplate

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.enable | true | no | none | boolean |

Use this property to enable the Explore module of DataManager.

!!! info

    If this property is set to `false` , all other settings of `modules.explore` are skipped.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.startWith | false | no | none | boolean |

Use this property to load the Explore module as the default one after login.

!!! info

    If more than one module has defined `startWith: true` the top most module in the navigation bar will be set as default.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.overallSearchQuery | see below | no | none | string (query |

Use this property to define a custom query for the search field provided in the Module bar.

```yaml
# default query
js.config.modules.explore.overallSearchQuery: |
  SELECT DISTINCT ?resource ?_resource
  {{FROM}}
  WHERE {
    ?resource ?p0 ?label.
    FILTER (!isBLANK(?resource)).
    BIND (?resource as ?_resource) .
    FILTER (contains (lcase(str(?label)), lcase("{{QUERY}}"))).
    }
```

!!! info

    The placeholder `{{QUERY}}` is replaced with the search string entered by the user. A placeholder `{{FROM}}` can be used to insert the currently selected graph URI.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
|`js.config.modules.explore.mapServer.url`| none | no | none | string (URI) |

Extension of the tiles as provided by OpenMapTiles Map Server

!!! info

    This works together with `js.config.modules.explore.mapServer.ext`, and only if it is set.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.mapServer.ext | none | no | none | string (URI) |

The service URL as provided by OpenMapTiles Map Server. If not defined, the wikimedia server is used.

!!! info

    It works together with `js.config.modules.explore.mapServer.url`, and only if it is set.

This is how `mapServer.ext` and `mapServer.url` are used in your configuration:

```yaml
js.config.modules.explore:
  mapServer:
    url: 'https://osm.your-host.com/styles/osm-bright'
    ext: 'png'
```

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.graphlist.defaultGraph | none | no | none | string (file extension) |

Use this property to define a graph URI the user is allowed to work on.

!!! info

    If the property is set the Graph box is hidden.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.graphlist.hideSearch | true | no | none | boolean |

Set this property to true to hide the Search field in the Graph box

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.graphlist.whiteList | none | no | none | list of strings (query) |

Use this property to specify a list of graphs the user can see.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.defaultClass | none | no | none | string (URI) |

Use this property to setup a default class.

!!! info

    This works together with `defaultGraph`, and only if it is set.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.topQuery | see below | no | none | string (query) |

Use this property to specify a custom query that defines which top level classes of a graph are displayed.

```yaml
# default query
js.config.modules.explore.navigation.topQuery: |
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  SELECT  ?resource ?hasChildren
  {{FROM}}
  WHERE {
    {
        ?resource rdfs:subClassOf owl:Thing .
    } UNION {
        ?r a ?resource .
        FILTER NOT EXISTS { ?resource rdfs:subClassOf ?super } .
    } UNION {
        ?resource a owl:Class
        FILTER NOT EXISTS { ?resource rdfs:subClassOf ?super } .
    }
    OPTIONAL{
        ?child rdfs:subClassOf ?resource .
        FILTER(isIRI(?child)) .
    }
    FILTER(isIRI(?resource)) .
    BIND(IF(BOUND(?child), "hasChildren", "noChildren") AS ?hasChildren)
    FILTER (!regex(
        STR(?resource),
        "^http://(www.w3.org/(2002/07/owl|2000/01/rdf-schema|1999/02/22-rdf-syntax-ns))#",
        "i"
    ))
  }
```

!!! info

    A placeholder `{{FROM}}` can be used to insert the currently selected graph URI. The `{{FROM}} `placeholder will be resolved to `FROM <graphUri>`.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.subQuery | see below | no | none | string (query) |

Use this property to specify a custom query that defines which subclasses of top level classes of a graph are displayed.

```yaml
# default query
js.config.modules.explore.navigation.subQuery: |
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  SELECT ?resource ?hasChildren
  {{FROM}}
  WHERE {
    ?resource rdfs:subClassOf {{RESOURCE}} .
    OPTIONAL{
        ?child rdfs:subClassOf ?resource .
        FILTER(isIRI(?child)) .
    }
    FILTER(isIRI(?resource)) .
    BIND(IF(BOUND(?child), "hasChildren", "noChildren") AS ?hasChildren)
  }

```

!!! info

    The placeholder `{{RESOURCE}}` is replaced with the selected parent class. A placeholder `{{FROM}}` can be used to insert the currently selected graph URI. The `{{FROM}}` placeholder will be resolved to `FROM <graphUri>`.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.searchQuery | see below | no | none | string (query) |

Use this property to specify a custom query that defines which classes of a graph are displayed when the user uses the Search field in the Navigation box.

```yaml
# default query
js.config.modules.explore.navigation.searchQuery: |
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
  SELECT  ?resource ?hasChildren
  {{FROM}}
  WHERE {
    {
        ?resource rdfs:subClassOf+ owl:Thing
    } UNION {
        ?r a ?resource .
    } UNION {
        ?resource a owl:Class
    }
    OPTIONAL{
        ?child rdfs:subClassOf ?resource .
        FILTER(isIRI(?child)) .
    }
    OPTIONAL {
        ?resource rdfs:label ?label1 .
    }
    OPTIONAL {
        ?resource skos:prefLabel ?label2 .
    }
    BIND(IF(BOUND(?child), "hasChildren", "noChildren") AS ?hasChildren)
    FILTER(isIRI(?resource)) .
    FILTER(
      regex(str(?resource),"{{QUERY}}","i") || regex(str(?label1),"{{QUERY}}","i") || regex(str(?label2),"{{QUERY}}","i")
    )
  }
```

!!! info

    The placeholder {{QUERY}} is replaced with the search string. A placeholder `{{GRAPH}}` can be used to insert the currently selected graph URI (will be resolved to `<graphUri>` ).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.listQuery | see below | no | none | string (query) |

Use this property to specify a custom query that defines which resources are displayed that are type of a selected class of a graph.

```yaml
# default query
js.config.modules.explore.navigation.listQuery: |
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  SELECT ?instance
  {{FROM}}
  WHERE {
    {
      ?instance a {{RESOURCE}} .
      FILTER isIRI(?instance) .
    } UNION {
      ?class rdfs:subClassOf+ {{RESOURCE}} .
      ?instance a ?class .
      FILTER isIRI(?instance).
    }
  }
```

!!! info

    The placeholder `{{RESOURCE}}` is replaced by the selected resource URI. A placeholder `{{GRAPH}}` can be used to insert the currently selected graph URI (will be resolved to `<graphUri>` ).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.navigation.itemsPerPage | 15 | no | none | number |

Use this property to specify the number of items shown per page of navigation.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.properties.enable | true | no | none | boolean |

Use this property to enable the `properties` tab of DataManager

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.usage.enable | true | no | none | boolean |

Use this property to enable the `usage` tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.references.enable | true | no | none | boolean |

Use this property to enable the `references` tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.turtle.enable | true | no | none | boolean |

Use this property to enable the `turtle` tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.history.enable | true | no | none | boolean |

Use this property to enable the History tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.statistics.enable | true | no | none | boolean |

Use this property to enable the `statistic` tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.statistics.sunburst.enable | true | no | none | boolean |

Sunburst is the visualization element in `statistic` tab.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.enable | true | no | none | boolean |

Use this property to enable the `visualization` tab of DataManager.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.literals | true | no | none | boolean |

Use this property to enable the literals filter in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.relations | true | no | none | boolean |

Use this property to enable the relations filter in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.solitarySubclasses | true | no | none | boolean |

Use this property to enable the solitary subclasses filter in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.classDisjointness | true | no | none | boolean |

Use this property to enable the class disjointness filter in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.setOperators | true | no | none | boolean |

Use this property to enable the set operators filter in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.filter.degreeOfCollapsing | true | no | none | boolean |

Use this property to enable the degree of the collapsing function in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.mode.dynamicLabelWidth | true | no | none | boolean |

Use this property to enable the dynamic label width mode in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.mode.pickAndPin | true | no | none | boolean |

Use this property to enable the pick and pin mode in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.mode.nodeScaling | true | no | none | boolean |

Use this property to enable the node scaling mode in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.mode.compactNotation | true | no | none | boolean |

Use this property to enable the compact notation mode in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.mode.colorExternals | true | no | none | boolean |

Use this property to enable the color externals mode in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.export.json | true | no | none | boolean |

Use this property to enable the feature export as JSON in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.export.svg | true | no | none | boolean |

Use this property to enable the feature export as SVG in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.gravity.classDistance | true | no | none | boolean |

Use this property to enable the class distance option in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.gravity.dataTypeDistance | true | no | none | boolean |

Use this property to enable the dataType distance option in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.reset | true | no | none | boolean |

Use this property to enable the reset function in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.pause | true | no | none | boolean |

Use this property to enable the pause function in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.details.visualization.webvowlConfig.search | true | no | none | boolean |

Use this property to enable the search function in the OWL viewer.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.externalTools.toolX.enable | false | no | none | boolean |

The `externTools` section can be used to configure one or more external tools which will be integrated as additional tabs in a resource detail view. The tool is then presented in the content of an iFrame. In addition to that, a JSON representation of the presented resource is sent via postmate to the running application inside of the iFrame.

Use this property to enable or disable one specific external tool configuration.

```yaml
js.config.modules.explore.externalTools.toolX.enable: true
```

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.externalTools.toolX.tabname | none | yes | none | string |

The `externTools` section can be used to configure one or more external tools which will be integrated as additional tabs in a resource detail view. The tool is then presented in the content of an iFrame. In addition to that, a JSON representation of the presented resource is sent via postmate to the running application inside of the iFrame.

Use this property to name the tab for the external tool.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.explore.externalTools.toolX.iframeUrlTemplate | none | yes | none | string (URL) |

The `externTools` section can be used to configure one or more external tools which will be integrated as additional tabs in a resource detail view. The tool is then presented in the content of an iFrame. In addition to that, a JSON representation of the presented resource is sent via postmate to the running application inside of the iFrame.

Use this property to specify the URL which will be loaded in the iFrame in the new application tab.

```yaml
js.config.modules.explore.externalTools.toolX.iframeUrlTemplate:
    "http://example.org/app/{{RESOURCE}}"
```

!!! info

    The placeholder `{{RESOURCE}}` is replaced with the selected resource URI. The placeholder `{{RESOURCELABEL}}` is replaced with the titleHelper generated label of the resource.

## Configuration example

```yaml
js.config.modules.explore:
  enable: true
  startWith: true
  overallSearchQuery: |
    SELECT DISTINCT ?resource ?_resource
    {{FROM}}
    WHERE {
      ?resource ?p0 ?label.
      FILTER (!isBLANK(?resource)).
      BIND (?resource as ?_resource) .
      FILTER (contains (lcase(str(?label)), lcase("{{QUERY}}"))).
    }
  graphlist:
    defaultGraph: ''
    hideSearch: true
  navigation:
    topQuery: |
      SELECT DISTINCT ?resource
      WHERE {
        ?r a ?resource .
        FILTER NOT EXISTS { ?resource rdfs:subClassOf ?super } .
      }
    subQuery: |
      SELECT DISTINCT ?resource
      WHERE {
        ?r a ?resource .
        ?resource rdfs:subClassOf {{RESOURCE}} .
      }
    searchQuery: |
      SELECT DISTINCT ?resource
      WHERE {
        ?r a ?resource .
        ?resource rdfs:label ?label .
        FILTER(contains(?label, "{{QUERY}}")) .
      }
    listQuery: |
      SELECT DISTINCT ?resource
      WHERE {
        {
          ?resource a {{RESOURCE}} .
        } UNION {
          ?class rdfs:subClassOf+ {{RESOURCE}} .
          ?resource a ?class .
        }
      }
  details:
    properties:
      enable: true
    usage:
      enable: true
    references:
      enable: true
    turtle:
      enable: true
    statistics:
      enable: true
      sunburst:
        enable: true
    visualization:
      enable: true
      webvowlConfig:
        filter:
          literals: true
          relations: true
          solitarySubclasses: true
          classDisjointness: true
          setOperators: true
          degreeOfCollapsing: true
        mode:
          dynamicLabelWidth: true
          pickAndPin: true
          nodeScaling: true
          compactNotation: true
          colorExternals: true
        export:
          json: true
          svg: true
        gravity:
          classDistance: true
          dataTypeDistance: true
        reset: true
        pause: true
        search: true

```
