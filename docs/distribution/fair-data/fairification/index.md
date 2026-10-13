---
status: new
title: "FAIRify a Knowledge Graph"
icon: material/transit-connection-variant
tags:
    - KnowledgeGraph
    - BestPractice
---

# FAIRify a Knowledge Graph

Data does not become Findable, Accessible, Interoperable and Reusable (FAIR) by declaration.
It becomes FAIR through a sequence of steps that attach the missing context to it - identifier, description, semantics, origin and rules of use.
This sequence is called FAIRification.

The six steps below describe that sequence for a Knowledge Graph in eccenca Corporate Memory.
Each step links to the page that documents the mechanism in detail.

!!! tip "Start early"

    Origin, semantics and responsibility are expensive to reconstruct once a graph exists, and sometimes impossible.
    Carry out steps 1 to 4 while the graph is being built rather than after it has been published.

## 1. Identify the data

Create the graph and decide on its identifier before loading data into it.
In **:eccenca-application-explore: Knowledge Graphs**, click **:eccenca-item-add-artefact: Add new graph** and select the graph type.
The **Graph URI** is generated from the label by a selectable template - **Hostname + provided label**, **Selected graph + provided label**, **UUID** or **Custom**.

The identifiers of the resources inside the graph are determined by the mapping rules that produce them.
[Cool IRIs](../../../build/cool-iris/index.md) describes how to design them so that they stay stable, and [Define Prefixes / Namespaces](../../../build/define-prefixes-namespaces/index.md) how to register the namespace.

## 2. Describe the data

Fill in the metadata form that follows the graph type.
The metadata is stored as RDF about the graph IRI itself and is available to search, to queries and to any client reading the graph.

Agree on a minimum set of fields that every graph in the organization carries, and enforce it with a shape catalog as described in step 6.
Without such an agreement the metadata differs from graph to graph, and principle F2 is satisfied for some graphs only.

## 3. Place the data semantically

Install the vocabularies and ontologies the domain already has instead of inventing terms.

=== "Corporate Memory"

    Open the [Marketplace](../../marketplace/index.md), filter the package list by the **Vocabulary** package type, and click **Install** on the package.

=== "cmemc"

    ``` bash
    cmemc package search VOCABULARY
    cmemc package install PACKAGE_ID
    ```

Record the dependency with `owl:imports`, so that the graph states which vocabularies it relies on, see [graph imports](../../../automate/cmemc-command-line-interface/command-reference/graph/imports/index.md).
Where no suitable vocabulary exists, author one in the [Business knowledge editor](../../../explore-and-author/bke-module/index.md) and publish it as a package of its own.

## 4. Add provenance

Make the origin of the data readable without asking the person who built it.

- Enable [Versioning of Graph Changes](../../../explore-and-author/graph-exploration/versioning-of-graph-changes/index.md) on the graph to record editing activities in a Versioning Graph.
- Set up [Statement Annotations](../../../explore-and-author/graph-exploration/statement-annotations/index.md) where the origin or the temporal validity of individual statements matters.
- Keep the [Workflow](../../../build/workflows/index.md) that produces the graph as the record of how it was derived from its sources.

## 5. Attach the rules of use

Decide who reaches the graph and under which conditions, and record the decision where it is enforced rather than in a separate document.
[Access Conditions](../../../deploy-and-configure/configuration/access-conditions/index.md) grant access per graph, per action and through dynamic conditions.

State the license under which the content may be reused.
For content distributed as a Marketplace Package, the license is an [SPDX identifier](https://spdx.org/licenses/) in the manifest, and publication without it is rejected, see [Metadata](../../../develop/packages/development/index.md#metadata).

## 6. Publish and check

Expose the graph over the standard endpoints and verify that it holds what the shape catalog requires.

=== "Corporate Memory"

    Open **:eccenca-application-explore: Knowledge Graphs** and check the resources against the node shapes of the shape catalog graph.

=== "cmemc"

    ``` bash
    cmemc graph validation execute https://ns.eccenca.com/example/data
    cmemc graph validation inspect <ID>
    ```

Bundle the result for reuse elsewhere.
[Marketplace Packages: Development and Publication](../../../develop/packages/development/index.md) describes how graphs, projects and queries are packaged into a single versioned artifact, and [Marketplace](../../marketplace/index.md) how such a package is installed into another instance.

!!! info "Related sections"

    - [The FAIR principles in Corporate Memory](../principles/index.md) lists which principle each of these steps serves.
