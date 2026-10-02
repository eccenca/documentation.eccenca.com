---
status: new
title: "FAIR Principles in Corporate Memory"
icon: material/format-list-checks
tags:
    - KnowledgeGraph
    - BestPractice
---

# The FAIR principles in Corporate Memory

The fifteen Findable, Accessible, Interoperable and Reusable (FAIR) principles are quoted below in the wording of the [GO FAIR Foundation](https://www.gofair.foundation/fair-principles), retrieved on 2026-10-02.
For each principle, the table names the mechanism in eccenca Corporate Memory that implements it and links to the page documenting that mechanism.

A principle that depends on an organizational decision rather than on a product feature is called out below its table.

## Findable

| Code | Principle | In Corporate Memory |
| --- | --- | --- |
| F1 | "(meta)data are assigned a globally unique and persistent identifier" | Every resource and every graph is identified by an IRI. Graph IRIs are derived from a selectable generation template - hostname and label, selected graph and label, UUID or a custom value. See [Cool IRIs](../../../build/cool-iris/index.md), [Define Prefixes / Namespaces](../../../build/define-prefixes-namespaces/index.md) and [Adding a new graph](../../../explore-and-author/graph-exploration/index.md#adding-a-new-graph). |
| F2 | "data are described with rich metadata (defined by R1 below)" | Each graph type carries its own metadata form, shown on the Metadata view of the graph. The metadata is stored as RDF inside the graph and can be queried like any other data. See [Knowledge Graphs](../../../explore-and-author/graph-exploration/index.md#graphs). |
| F3 | "metadata clearly and explicitly include the identifier of the data they describe" | Graph metadata is recorded as statements about the graph IRI itself, so the description and the described graph share one identifier. See [Knowledge Graphs](../../../explore-and-author/graph-exploration/index.md#graphs). |
| F4 | "(meta)data are registered or indexed in a searchable resource" | The graph list, the navigation tree and the full-text search index the content of an instance. Queries are registered in the [Query module](../../../explore-and-author/query-module/index.md), distributable content in the [Marketplace](../../marketplace/index.md). See [Label Resolution and Full Text Search](../../../deploy-and-configure/configuration/label-resolution-and-full-text-search/index.md). |

!!! info "F4 beyond a single instance"

    A Marketplace Server indexes packages, not datasets.
    Discovery of datasets across organizations requires a catalog that is set up as part of the solution, for example as a graph following a catalog vocabulary.

## Accessible

| Code | Principle | In Corporate Memory |
| --- | --- | --- |
| A1 | "(meta)data are retrievable by their identifier using a standardised communications protocol" | The SPARQL endpoint, the Graph Store API, the RDF resource API, the JSON-LD Frame API and the SQL endpoint retrieve data by its identifier. See [Explore backend APIs](../../../develop/dataplatform-apis/index.md) and [Consume](../../../consume/index.md). |
| A1.1 | "the protocol is open, free, and universally implementable" | Access runs over SPARQL 1.1, the SPARQL Graph Store HTTP Protocol and HTTP content negotiation. These are W3C standards, so no proprietary client is required. See [Media Types](../../../develop/dataplatform-apis/index.md#media-types). |
| A1.2 | "the protocol allows for an authentication and authorisation procedure, where necessary" | Authentication runs over OAuth 2.0 and OpenID Connect through [Keycloak](../../../deploy-and-configure/configuration/keycloak/index.md). [Access Conditions](../../../deploy-and-configure/configuration/access-conditions/index.md) grant access per graph, per action and through dynamic conditions. [Project Access Control](../../../build/project-access-control/index.md) restricts a Build project to selected user groups. |
| A2 | "metadata are accessible, even when the data are no longer available" | Metadata is held in graphs and can be kept in a different graph from the data it describes, so removing the data graph leaves the description in place. This is a modelling decision taken when the solution is designed, not a setting. |

!!! info "A2 is a design decision"

    Corporate Memory does not retain the description of a graph automatically once the graph is removed.
    Keeping metadata separate from the data it describes - for example in a dedicated catalog graph - is what makes A2 hold.

## Interoperable

| Code | Principle | In Corporate Memory |
| --- | --- | --- |
| I1 | "(meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation" | Data and metadata are RDF throughout. Ontologies are authored in RDFS and OWL in the [Business knowledge editor](../../../explore-and-author/bke-module/index.md), see [Visually authoring ontologies](../../../explore-and-author/bke-module/visually-authoring-ontologies/index.md). Taxonomies follow SKOS, see [Thesauri](../../../explore-and-author/thesauri-management/index.md). |
| I2 | "(meta)data use vocabularies that follow FAIR principles" | Vocabularies and ontologies are installed as versioned [Marketplace Packages](../../marketplace/index.md) carrying a name, a description, an SPDX license, a version and their dependencies. `owl:imports` records which vocabularies a graph relies on, see [graph imports](../../../automate/cmemc-command-line-interface/command-reference/graph/imports/index.md). |
| I3 | "(meta)data include qualified references to other (meta)data" | [Link rules](../../../explore-and-author/link-rules/index.md) and [Active learning](../../../build/active-learning/index.md) produce typed links between datasets instead of untyped matches. [Statement Annotations](../../../explore-and-author/graph-exploration/statement-annotations/index.md) qualify an individual statement, for example with its temporal validity or its origin. |

## Reusable

| Code | Principle | In Corporate Memory |
| --- | --- | --- |
| R1 | "(meta)data are richly described with a plurality of accurate and relevant attributes" | SHACL shape catalogs define which attributes a resource carries, and drive both the editing forms and the validation. See [Building a customized user interface](../../../explore-and-author/graph-exploration/building-a-customized-user-interface/index.md) and [graph validation](../../../automate/cmemc-command-line-interface/command-reference/graph/validation/index.md). Shapes can be derived from an existing graph with [Generate SHACL shapes](../../../build/reference/customtask/cmem_plugin_shapes-plugin_shapes-ShapesPlugin.md). |
| R1.1 | "(meta)data are released with a clear and accessible data usage license" | A Marketplace Package declares an [SPDX license identifier](https://spdx.org/licenses/) in its manifest and cannot be published without one. The license is shown on the package card and on the details page, and packages can be filtered by it. See [Metadata](../../../develop/packages/development/index.md#metadata) and [License](../../marketplace/index.md#license). |
| R1.2 | "(meta)data are associated with detailed provenance" | [Versioning of Graph Changes](../../../explore-and-author/graph-exploration/versioning-of-graph-changes/index.md) records editing activities in a separate Versioning Graph. [Statement Annotations](../../../explore-and-author/graph-exploration/statement-annotations/index.md) hold the origin of an individual statement. [Workflows](../../../build/workflows/index.md) document how a graph was produced, and a package changelog records what changed between versions. |
| R1.3 | "(meta)data meet domain-relevant community standards" | Standard vocabularies are installed from the [Marketplace](../../marketplace/index.md). Conformance to the shapes of a standard is checked with [graph validation](../../../automate/cmemc-command-line-interface/command-reference/graph/validation/index.md) and with [Validate RDF triples](../../../build/reference/customtask/cmem_plugin_reason-plugin_validate-ValidatePlugin.md). |

!!! info "R1.1 applies to packages"

    The license mechanism described here belongs to Marketplace Packages.
    A license statement on a graph that is not distributed as a package is part of the metadata model of that graph and is defined with the solution.
