# Default Configuration

The following configuration shows the default configuration of DataManager.

``` yaml
js.config.workspaces:
  default:
    name: Eccenca Vocabulary Service
    authorization:
      type: anonymous
    backend:
      type: dataplatform
      url: https://vocab.eccenca.com/
      endpointId: default

js.config.appPresentation:
  windowTitle: eccenca DataManager
  headerName: DataManager

js.config.shacl:
  shapesGraph: https://vocab.eccenca.com/shacl/

js.config.resourceTable:
  timeoutDownload: 600000

js.config.api:
  sparql: /proxy/:endpointId/sparql
  sparqlQueryBase64Encoded: false
  sparqlUpdate: /proxy/:endpointId/update
  defaultTimeout: 60000

js.config.errorPages:
  graphAccess:
    title: Unauthorized User
    message: You are not authorized to use this workspace.
  moduleAccess:
    title: No module accessible
    message: You have no access to any module.
  workspaceAccess:
    title: Workspace access problem
    message: You are logged in successfully but you do not have enough permissions. Please contact your administrator.

js.config.titleHelper:
  properties:
    - http://www.w3.org/ns/shacl#name
    - http://www.w3.org/2004/02/skos/core#prefLabel
    - http://xmlns.com/foaf/0.1/name
    - http://purl.org/dc/elements/1.1/title
    - http://purl.org/dc/terms/title
    - http://www.w3.org/2000/01/rdf-schema#label
  languages:
    - en
    - ''

js.config.userPermissions:
  allowCreateWorkspace: true
  allowSelectWorkspace: true

js.config.modules.task:
  enable: true

js.config.modules.administration:
  enable: true
  accessConditions:
    graph: https://ns.eccenca.com/data/ac/

js.config.modules.datasets:
  enable: false

js.config.modules.explore:
  enable: true
  shacl:
    allowCopy: false
    showGraphInfo: false
    useSaveApi: false
  graphlist:
    defaultGraph: ''
    hideSearch: false
  navigation:
    defaultClass: ''
    itemsPerPage: 10
    topQuery: |
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>

      SELECT ?resource ?hasChildren
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
      }
    subQuery: |
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
    searchQuery: |
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

      SELECT ?resource ?hasChildren
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
          regex(str(?resource),"{{QUERY}}","i") ||
          regex(str(?label1),"{{QUERY}}","i") ||
          regex(str(?label2),"{{QUERY}}","i")
        )

      }
    listQuery: |
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

  overallSearchQuery: |
    SELECT ?resource
    {{FROM}}
    WHERE {
      ?resource ?p0 ?label.
      FILTER (!isBLANK(?resource)).
      FILTER (contains (lcase(str(?label)), lcase("{{QUERY}}"))).
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

js.config.modules.thesaurus:
  enable: true

js.config.modules.query:
  enable: true
  graph: https://ns.eccenca.com/data/queries/
  timeout: 600000

js.config.modules.vocabulary:
  enable: false

js.config.modules.gdprsearch:
  enable: false

js.config.modules.linkrules:
  enable: false

js.config.modules.annotation:
  enable: false

js.config.modules.search:
  enable: false

js.config.modules.tracking:
  enable: false

js.config.modules.reports:
  enable: false
```
