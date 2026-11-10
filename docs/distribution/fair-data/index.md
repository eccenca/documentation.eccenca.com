---
status: new
title: "FAIR Data with Corporate Memory"
icon: material/star-four-points-outline
tags:
    - KnowledgeGraph
    - BestPractice
---

# FAIR data with Corporate Memory

!!! abstract

    The Findable, Accessible, Interoperable and Reusable (FAIR) principles describe the conditions under which data can be located, retrieved, understood and reused - by people as well as by machines.
    This section maps each principle to the mechanism in eccenca Corporate Memory that implements it, and names the points where a principle asks for an organizational decision rather than for a feature.

## What FAIR means

FAIR stands for Findable, Accessible, Interoperable and Reusable.
The four dimensions are published as fifteen principles by the [GO FAIR Foundation](https://www.gofair.foundation/fair-principles).
Each dimension answers one question about a dataset:

| Dimension | Question it answers |
| --- | --- |
| Findable | Is it known that the data exists, and can it be located? |
| Accessible | Can the data be retrieved, under defined conditions? |
| Interoperable | Do sender and receiver interpret the data the same way? |
| Reusable | Can the fitness of the data for a new purpose be judged? |

The principles address metadata as much as data.
A dataset becomes FAIR through the context that travels with it: its identifier, its description, the vocabularies it uses, its origin and the rules for its use.

!!! note "Accessible does not mean open"

    Principle A1.2 requires the access protocol to support authentication and authorization where necessary.
    Restricted data can be FAIR data.
    In Corporate Memory, [Access Conditions](../../deploy-and-configure/configuration/access-conditions/index.md) determine which user group reaches which graph and which action, without affecting the findability or the description of the data.

## How Corporate Memory covers the four dimensions

| Dimension | Building blocks in Corporate Memory |
| --- | --- |
| Findable | IRIs for every resource and every graph, graph metadata, graph and full-text search, the Query catalog, the Marketplace |
| Accessible | SPARQL endpoint, Graph Store API, RDF resource and JSON-LD Frame APIs, Keycloak, Access Conditions |
| Interoperable | RDF throughout, RDFS and OWL ontologies, SKOS thesauri, SHACL shapes, vocabularies installed as Marketplace Packages |
| Reusable | Shape catalogs and validation, SPDX licenses on packages, Versioning Graphs, Statement Annotations, Build workflows |

[The FAIR principles in Corporate Memory](principles/index.md) resolves this overview into one entry per principle.

<div class="grid cards" markdown>

- :material-format-list-checks: [The FAIR principles in Corporate Memory](principles/index.md)

    ---

    All fifteen principles in the wording of the GO FAIR Foundation, each with the Corporate Memory mechanism that implements it and the page that documents it.

- :material-transit-connection-variant: [FAIRify a Knowledge Graph](fairification/index.md)

    ---

    The six steps that turn an existing Knowledge Graph into a FAIR one, from the identifier to the published package.

</div>

## What FAIR does not cover

The FAIR principles describe whether data can be used.
They do not describe whether data should be used for a particular purpose.
A dataset can satisfy all fifteen principles and still be unsuitable for training a model, because its coverage is skewed, its annotations are unreliable, or the exact state used in an earlier run cannot be reconstructed.
Fitness for purpose, bias and coverage, and the reproducibility of a given state are separate questions.
They build on FAIR data rather than following from it.

!!! info "Related sections"

    - [Marketplace](../marketplace/index.md) describes how ready-made vocabularies, ontologies and projects are installed as versioned packages.
    - [Marketplace Packages: Development and Publication](../../develop/packages/development/index.md) describes the manifest in which name, description, license and dependencies of a package are declared.
    - [Access Conditions](../../deploy-and-configure/configuration/access-conditions/index.md) describes how access to graphs and actions is granted.
