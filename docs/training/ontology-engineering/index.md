---
title: "Training: Ontology Engineering"
icon: material/presentation
tags:
  - BeginnersTutorial
  - Vocabulary
---
# Ontology Engineering

<div class="training-deck">
<iframe src="slides.html" title="Slides: Ontology Engineering" allow="fullscreen"></iframe>
</div>

!!! abstract "About this module"

    This hands-on module shows how to develop an ontology for a domain, from the first requirements to a formal vocabulary in eccenca Corporate Memory.
    The example is the product domain whose data the [SPARQL exercises](../sparql-basics/index.md#exercises) query.
    It follows [Ontology Modeling](../ontology-modeling/index.md) and is part of the [Corporate Memory training](../index.md).

    Use **Show slide** next to a heading to bring the matching slide into view, or **Read the explanation** under the slides to jump to the text for the current slide.

## What an ontology is { #what-is-an-ontology }

An ontology is a shared, structured conceptualization of a domain.
Each of the three words carries part of the meaning:

- **Conceptualization** – an abstract, simplified view of the domain, made for a purpose.
  It captures the objects and concepts of the domain and the relations between them.
- **Structured** – written in a standard modeling language such as RDF Schema, OWL or SKOS, so that machines can process it.
- **Shared** – agreed on by the domain experts, so that it serves as a common, extensible standard for the data of the domain.

Domains range from the most basic things, such as persons, places and activities, to specialist areas such as supply chains or manufacturing.

## Methodology { #methodology }

There is no single correct way to engineer an ontology, and no single correct result.
The domain and the application decide.

A few principles hold in general.
The concepts of the ontology stay close to the physical or logical objects of the domain and the relations between them.
They are usually the nouns and verbs of sentences that describe the domain: nouns become classes, verbs become properties.
The intended use decides which of them the ontology needs.

Ontology engineering is iterative.
A first model is discussed with the domain experts, applied to real data, and refined, again and again.

## Scope and requirements { #scope-and-requirements }

The scope of an ontology depends on its domain, its application and its users.
A few questions clarify it at the start:

- Is there data already, or is the model built on a green field?
- If there is data, what is it used for?
- Is the goal a clearer, logical model of the domain, or compatibility with existing structures?
- How much metadata is needed?
- Which other data sources are relevant?
- Do ontologies for the domain exist already, see [Reuse existing vocabularies](../ontology-modeling/index.md#reuse)?

## Competency questions { #competency-questions }

Competency questions turn the requirements into a test.
They are the questions the ontology has to be able to answer, collected in a catalog at the start.

After each milestone, example data that follows the ontology is created, and the questions are answered by querying or browsing it.
A question that cannot be answered shows a gap in the model.

For the product domain, typical competency questions are:

- Which products is a department responsible for?
- Who manages a given product, and in which department does that person work?
- Who can take over a product when its manager leaves?

The [SPARQL exercises](../sparql-basics/index.md#exercises) answer exactly such questions on the product data.

## Source material { #source-material }

The knowledge for an ontology comes from many sources:
existing databases and spreadsheets, slide decks and training material, company taxonomies, product catalogs, books and standards, and interviews with domain experts.

In practice, it is usually a combination.
A project receives a spreadsheet and a slide deck, interviews a domain expert, drafts a first ontology, iterates it with the expert, and receives further material along the way.

## The domain { #the-domain }

The exercise models a short description of a product domain:
products and services, the product managers who manage them, the departments the managers work in, and the product categories in which the departments and managers have expertise.

The second paragraph of the description names concrete things: a product with its identifier and name, a product manager and a department.
These are the instances the model has to accommodate.

## Concepts, relationships, instances and attributes { #concepts-relationships-instances-and-attributes }

Reading the description four times, each time with a different question, structures the domain:

1. **Concepts** – what kinds of things are there?
   Products, services, product managers, departments, direct reports and categories.
2. **Relationships** – how are they connected?
   Products are *managed by* product managers, managers *have* direct reports, products are *structured into* categories, departments are *responsible* for products, and managers and departments *have expertise* in categories.
3. **Instances** – which concrete things are mentioned?
   P516-8211068, Film Multiplexer Rheostat Warp, Kristen Bauers and Procurement.
   In a real project, instances come from the data sources rather than from documentation.
4. **Attributes** – which values describe a thing?
   A product is *named*, so it has a name.

## Defining classes { #defining-classes }

Three strategies lead from the candidates to a class hierarchy:

- **Top-down** starts with the most general classes and specializes them.
- **Bottom-up** starts with the most specific classes and groups them into more general ones.
- **Middle-out** starts with the most important classes and generalizes and specializes from there.

In the product domain, middle-out works well.
*Product* is central, and *hardware* and *service* specialize it.
*Product manager* and *direct report* turn out not to be classes of their own: both are employees, distinguished only by their relations.
They become the class *Employee*, its subclass *Manager*, and the common superclass *Agent* for anyone who can be a member of a department.

A drawing helps at this stage: classes as boxes, relations as arrows between them.

## The model { #the-model }

The diagram shows the core of the products vocabulary as it is installed with the **Product Data Demo** package, version v1.2.0:

| Class | Meaning |
| --- | --- |
| `prod:Product` with `prod:Hardware` and `prod:Service` | what the company offers |
| `prod:Agent` with `prod:Employee` and `prod:Manager` | people who act in the company |
| `prod:Department` | an organizational unit |
| `prod:ProductCategory` | a category of products |

| Property | From | To |
| --- | --- | --- |
| `prod:hasProductManager` | Product | Employee |
| `prod:hasCategory` | Product | ProductCategory |
| `prod:areaOfExpertise` | Agent | ProductCategory |
| `prod:memberOf` | Agent | Department |
| `prod:responsibleFor` | Department | Product |
| `prod:hasManager` | Employee | Manager |
| `prod:eligibleFor` | Service | Product |

The relations of the description map onto these properties: *managed by* became `prod:hasProductManager`, *have expertise* became `prod:areaOfExpertise`.
The direct report relation is `prod:hasManager`, read from the other end, and `prod:hasDirectReport` exists as well.

The vocabulary has grown beyond the first draft of the exercise.
It adds suppliers, prices, bills of material and physical dimensions, and models addresses as simple attributes of an agent.

!!! note "Older vocabulary versions"

    Earlier versions of this exercise and of the build tutorials use the vocabulary version 0.0.1.
    It names the expertise property `prod:expertFor`, has a property `prod:managesProduct`, and models addresses as a class `prod:Address` of their own.

## Class or attribute? { #class-or-attribute }

A recurring modeling decision is whether something becomes a class with instances of its own, or remains an attribute value.

Take facilities and the cities they are in.
As long as the city is only a name, an attribute such as `cityName` with a string value is enough.
Once the data says something about the city itself, such as its location, the city has to become a resource: the facility is `locatedIn` a city, and the city has a label and a location.

Make something a class when

- it is a business object in its own right,
- there are, or will be, statements about it,
- other datasets describe the same things, so that links to them become possible.

Both options are valid, and the requirements decide.

## Formalize { #formalize }

The drawing is then written down as RDFS and OWL.
Each class and property gets a type, its place in the hierarchy, domain and range, a label, and a link to the ontology that defines it.

Any text editor can produce Turtle.
Ontology editors such as Protégé add forms, consistency checks and reasoning.
In Corporate Memory, the Business Knowledge Editor creates classes and properties visually, see [Visually Authoring Ontologies](../../explore-and-author/bke-module/visually-authoring-ontologies/index.md).

## Quality checks { #quality-checks }

An ontology is easier to use and maintain when it meets a few rules consistently:

- The ontology header names the version, the preferred namespace and the preferred prefix.
- Every class and property has an `rdf:type` and an `rdfs:isDefinedBy` pointing to the ontology.
- Every class and property has at least one `rdfs:label` and one `rdfs:comment`, without placeholders such as "todo".
- Labels differ from comments, and no two resources share a label or a comment.

Such rules can be checked automatically with SPARQL queries or SHACL shapes.
SHACL also checks the instance data against the model, and Corporate Memory can run these checks in workflows and in continuous integration pipelines, see [Continuous integration](../../automate/continuous-integration/index.md).

## Visualize and use { #visualize-and-use }

A diagram shows the structure of an ontology at a glance.
It helps domain experts, who often find a picture easier to follow than Turtle, and it reveals modeling errors such as missing relations.

Corporate Memory supports the whole cycle:

- the [Vocabulary Catalog](../../explore-and-author/vocabulary-catalog/index.md) installs and manages vocabularies,
- the [Business Knowledge Editor](../../explore-and-author/bke-module/index.md) explores and authors ontologies visually,
- the mapping editor transforms data from spreadsheets, databases and other sources into instances of the ontology, see [Lift data from tabular data](../../build/lift-data-from-tabular-data-such-as-csv-xslx-or-database-tables/index.md).

An ontology without data stays theory.
Mapping the sources onto it fills it with life.

## Exercise { #exercise }

Develop a small ontology, either for a domain from daily work or by extending the product domain, for example with suppliers:

1. Write five competency questions.
2. Describe the domain in a few sentences, and mark the concepts, relations, instances and attributes.
3. Draw the model.
4. Formalize it in Turtle, or create it in the Business Knowledge Editor.
5. Create a few instances, and answer the competency questions with SPARQL.

Compare the result with the products vocabulary of the Product Data Demo, which models suppliers with the class `prod:Supplier` and the property `prod:hasSupplier`.
