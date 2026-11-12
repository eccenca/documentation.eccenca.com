---
title: "Training: Ontology Modeling"
hide:
  - toc
icon: material/presentation
tags:
  - BeginnersTutorial
  - Vocabulary
---
# Ontology Modeling

<div class="training-deck">
<iframe src="slides.html" title="Slides: Ontology Modeling" allow="fullscreen"></iframe>
</div>

!!! abstract "About this module"

    This module introduces RDF Schema and OWL, the two W3C languages for describing the classes and properties of a domain.
    It builds on [RDF and Linked Data Foundations](../rdf-and-linked-data/index.md) and [SPARQL Basics](../sparql-basics/index.md), and prepares the hands-on module [Ontology Engineering](../ontology-engineering/index.md).
    It is part of the [eccenca Corporate Memory training](../index.md).

    Use **Show slide** next to a heading to bring the matching slide into view, or **Read the explanation** under the slides to jump to the text for the current slide.

## Schema knowledge { #schema-knowledge }

RDF states facts about individual resources: Einstein discovered the theory of relativity.
It has no means of saying what kinds of things exist and how they relate in general.
That only persons discover things, or that every researcher is a person, is knowledge about the schema of the data, also called terminological knowledge.

Schema knowledge is what a vocabulary contains.
Written down in RDF Schema or OWL, it serves three purposes:
it documents the meaning of the data, it lets software such as the mapping and form editors of eccenca Corporate Memory propose suitable classes and properties, and it allows a reasoner to derive facts that are only implied.

## RDF Schema { #rdf-schema }

RDF Schema, RDFS for short, is part of the W3C RDF recommendations, and RDF Schema 1.1 from 2014 is the current version.
It provides a small set of terms for describing classes and properties.

RDFS is itself written in RDF: a schema is a set of triples, stored and queried like any other data.
Its terms are generic and fit any domain.
They live in the namespace `http://www.w3.org/2000/01/rdf-schema#`, usually abbreviated `rdfs:`.

## Classes and instances { #classes-and-instances }

A class is a set of things, and is named by an IRI.
Declaring a class means stating that its IRI is an `rdfs:Class`.
The property `rdf:type`, written `a` in Turtle, makes a resource an instance of a class, and a resource can be an instance of any number of classes.

Nothing in the syntax separates classes from instances: both are IRIs.
Only the statements about an IRI show whether it is used as a class, as an instance, or as both.

## Class hierarchies { #class-hierarchies }

`rdfs:subClassOf` arranges classes in a hierarchy.
`ex:Car rdfs:subClassOf ex:MotorVehicle` means that every car is a motor vehicle.
A class can have several superclasses, so the hierarchy is a directed graph rather than a strict tree.

The products vocabulary used in the exercises has two such hierarchies:
`prod:Hardware` and `prod:Service` are subclasses of `prod:Product`, and `prod:Manager` is a subclass of `prod:Employee`, which in turn is a subclass of `prod:Agent`.

## Inference { #inference }

Schema knowledge makes implicit facts derivable.
From *the blue VW Golf is a car* and *every car is a motor vehicle* it follows that the blue VW Golf is a motor vehicle.
The RDFS semantics defines a fixed set of such entailment rules.

`rdfs:subClassOf` is transitive: a car is a motor vehicle, a motor vehicle is a vehicle, so a car is a vehicle.
When two classes are each other's subclass, they have exactly the same instances and are therefore equivalent.

!!! info "Inference in the triple store"

    Whether a query sees inferred triples depends on the triple store and its configuration.
    In the product data of the exercises, the store does not infer them: a query for `a prod:Product` finds no product, because the data only states `prod:Hardware` and `prod:Service`.
    The SPARQL property path `a/rdfs:subClassOf*` evaluates the class hierarchy inside the query instead, see the [SPARQL exercises](../sparql-basics/index.md#exercises).

## Built-in classes { #built-in-classes }

RDF and RDFS predefine a few classes:

- `rdfs:Resource` contains everything.
- `rdfs:Class` contains all classes, and is therefore an instance of itself.
- `rdf:Property` contains all properties.
- `rdfs:Literal` contains all literal values, `rdfs:Datatype` all datatypes, and `rdf:langString` all language-tagged strings.
- `rdf:Statement` contains reified statements, see [Statements about statements](#reification).
- `rdfs:Container` is the superclass of the container classes `rdf:Bag`, `rdf:Seq` and `rdf:Alt`.

## Properties and their hierarchies { #properties }

A property relates two things.
Mathematically, it is a set of pairs: the property *drives* is the set of all pairs of a driver and a vehicle.
A property is declared as an instance of `rdf:Property`.

`rdfs:subPropertyOf` arranges properties in a hierarchy, just like classes.
If driving is a way of controlling, then every pair in *drives* is also a pair in *controls*, and from *Max drives the Golf* follows *Max controls the Golf*.
A vocabulary is always an idealized model: in reality, not every driver is in control of the vehicle.

## Domain and range { #domain-and-range }

`rdfs:domain` states the class of the subjects of a property, `rdfs:range` the class or datatype of its objects.
For a property with a literal value, the range is a datatype such as `xsd:nonNegativeInteger`.

In RDFS, domain and range are inference rules.
When Max drives the Golf and the domain of *drives* is *Person*, a reasoner concludes that Max is a person.

Domain and range also serve as documentation.
They tell modelers and tools which properties fit a class.

## Domain and range are not constraints { #domain-and-range-are-not-constraints }

Because domain and range infer, they never reject data.
In the classic example, the range of *belongs to* is *Organization*.
The statement *five belongs to the primes* is then not an error, but turns the primes into an organization.

The product data shows the same effect.
The range of `prod:hasProductManager` is `prod:Employee`, yet 49 products name a product manager who does not appear in the organization map.
A reasoner would type these three managers as employees, and the gap in the data would be invisible.

Checking that data fits the schema is the task of SHACL, see [Open world](#open-world).

## Annotations { #annotations }

RDFS provides four properties that describe resources for people rather than for reasoners:

- `rdfs:label` gives a human-readable name, ideally one per language.
- `rdfs:comment` gives a longer description or definition.
- `rdfs:seeAlso` points to further information about the resource.
- `rdfs:isDefinedBy` points to the vocabulary that defines the resource.

Corporate Memory shows labels and comments wherever a class or property appears, in forms, mapping suggestions and the graph explorer.
Every class and property of a vocabulary should therefore have both.

## Statements about statements { #reification }

Sometimes a statement is itself the subject of a statement: a detective supposes that the butler killed the gardener, and this theory is unproven.
RDF reification describes a statement as a resource of type `rdf:Statement`, with the properties `rdf:subject`, `rdf:predicate` and `rdf:object`.

The described triple is not asserted.
The graph contains the information that someone supposes the butler killed the gardener, not that the butler did.

Reification is verbose, and querying it is cumbersome.
RDF 1.2 introduces triple terms as a compact alternative.
Corporate Memory supports annotations on statements, see [Statement annotations](../../explore-and-author/graph-exploration/statement-annotations/index.md).

## The limits of RDF Schema { #limits-of-rdf-schema }

RDFS has no negation, no cardinalities and no alternatives.
It cannot say that cats are not dogs, that a person has at most one spouse, or that the range of a property is a car or a ship.

Two range statements are a common pitfall.
`ex:drives rdfs:range ex:Car , ex:Ship` does not mean car or ship, it means that everything driven is a car and a ship at the same time.
In RDFS, the way out is a common superclass, such as *Vehicle*, used as the range.

RDFS also cannot state that two IRIs name the same individual, or that one property is the inverse of another.
These gaps are filled by OWL.

## OWL { #owl }

OWL, the Web Ontology Language, became a W3C Recommendation in 2004, and OWL 2 followed in 2009.
OWL extends RDFS with constructs from description logic, with a precisely defined semantics.

An OWL ontology is a set of axioms, and every axiom is written as RDF triples.
Like RDFS, OWL distinguishes individuals, the things of the domain, classes, the sets of things, and properties, the relations between things or between things and values.

Besides Turtle and RDF/XML, OWL has its own syntaxes: OWL/XML for XML tools, the Manchester syntax that ontology editors such as Protégé display, and the functional syntax that shows the formal structure.
In Corporate Memory, ontologies are graphs, imported and exported as Turtle or another RDF format.

## The ontology header { #ontology-header }

An ontology describes itself with a resource of type `owl:Ontology`, usually named by the namespace IRI.
The header holds the metadata of the ontology: label and description, creator and dates, the version, and the preferred prefix and namespace.

The products vocabulary declares `pv` as its preferred prefix.
This training writes `prod:`, which names the same namespace: a prefix is only an abbreviation.

`owl:imports` includes another ontology, so that its classes and properties are available together with the importing one.
Versioning properties such as `owl:versionInfo`, `owl:priorVersion` and `owl:deprecated` track how an ontology changes.

The [Vocabulary Catalog](../../explore-and-author/vocabulary-catalog/index.md) of Corporate Memory reads this header to list and manage the installed vocabularies.

## Classes and properties in OWL { #owl-classes-and-properties }

OWL declares classes with `owl:Class` and distinguishes two kinds of properties:

- An `owl:ObjectProperty` relates two resources, for example an employee to a department.
- An `owl:DatatypeProperty` relates a resource to a literal value, for example an employee to an email address.

The distinction matters when mapping data in Corporate Memory: a value mapping writes a datatype property, an object mapping an object property.

OWL predefines the classes `owl:Thing`, which contains every individual, and `owl:Nothing`, which contains none.

## Individuals { #individuals }

Individuals are typed with `rdf:type` as in RDFS, and properties can have any number of values: Einstein belongs to Princeton and to Bern.

`owl:sameAs` states that two IRIs name the same individual.
Everything said about one then holds for the other.
This is how OWL links records of the same entity from different sources.

OWL makes no unique name assumption: two different IRIs may name the same thing unless the data states otherwise.
`owl:differentFrom` and `owl:AllDifferent` state explicitly that individuals are distinct.

## Relations between classes { #class-relations }

Three axioms relate classes:

- `rdfs:subClassOf` – every member of A is a member of B.
- `owl:equivalentClass` – A and B have exactly the same members.
- `owl:disjointWith` – no individual belongs to both.

Disjointness is inherited.
If faculty staff and publications are disjoint, and professors are faculty staff and books are publications, then professors and books are disjoint as well.
An individual typed as both would make the ontology inconsistent, and a reasoner reports the contradiction.

## Building classes from classes { #class-constructors }

OWL builds new classes from existing ones:

- `owl:intersectionOf` – members of all listed classes: a moon of Mars is a moon and an object near Mars.
- `owl:unionOf` – members of at least one listed class: a person is an adult or a child.
- `owl:complementOf` – everything not in the class.
- `owl:oneOf` – exactly the listed individuals: the moons of Mars are Phobos and Deimos.
- `owl:disjointUnionOf` – a union whose parts do not overlap: every professor is either active or retired.

Such class expressions usually appear as anonymous classes in square brackets, combined with `owl:equivalentClass` or `rdfs:subClassOf`.
The lists are RDF collections, written in parentheses without commas.

## Property characteristics { #property-characteristics }

OWL describes properties in more detail than RDFS:

- `owl:inverseOf` – *has manager* and *has direct report* are inverse, so each statement implies the other in the opposite direction.
- `owl:TransitiveProperty` – a part of a part is a part.
- `owl:SymmetricProperty` – a marriage holds in both directions.
- `owl:FunctionalProperty` – a property with at most one value, such as a birth date.
- `owl:equivalentProperty` – two properties with the same pairs, typically from different vocabularies.

The products vocabulary defines `prod:hasManager` and `prod:hasDirectReport` but does not declare them inverse.
The example on the slide shows how it could.

## Property restrictions { #restrictions }

A restriction is an anonymous class defined by the values of a property:

- `owl:allValuesFrom` – all values come from a class: every examiner of an exam is a professor.
- `owl:someValuesFrom` – at least one value comes from a class: every exam has at least one examiner who is a person.
- `owl:hasValue` – a specific value is present.
- `owl:minCardinality`, `owl:maxCardinality`, `owl:cardinality` – the number of values: an exam has at most two examiners.

Stating that a class is a subclass of a restriction makes the restriction hold for all its members.

## Open world { #open-world }

OWL assumes an open world: what the data does not state may still be true.
If every exam must have an examiner and an exam in the data has none, OWL does not report an error.
It concludes that an examiner exists who has not been recorded.

For data quality this is rarely the desired behavior.
SHACL, the Shapes Constraint Language, assumes a closed world and checks the data as it is: the exam without examiner violates the shape.

Corporate Memory uses both: vocabularies in RDFS and OWL describe the meaning of the data, SHACL shapes drive the forms and validate the data, see [Building a customized user interface](../../explore-and-author/graph-exploration/building-a-customized-user-interface/index.md).

## Expressivity has a price { #expressivity }

Modeling languages range from simple taxonomies and thesauri over RDFS and OWL to first-order logic and natural language.
The more a language can express, the harder it is to reason with.

OWL 2 balances the two with several variants:

- **OWL 2 Full** allows any use of the constructs, but reasoning is undecidable.
- **OWL 2 DL** restricts the use so that reasoning is decidable; it corresponds to the description logic *SROIQ*.
- **OWL 2 EL, QL and RL** are profiles that give up expressivity for reasoning in polynomial time, tuned for large class hierarchies, query rewriting and rule engines respectively.

OWL 1 had the variants Lite, DL and Full, which older material still mentions.

Most enterprise vocabularies need little of this: classes, a hierarchy, object and datatype properties with domain and range, and good labels.

## Reuse existing vocabularies { #reuse }

Many concepts are already modeled in established vocabularies:

- **Dublin Core** for metadata such as title, creator and date,
- **FOAF** for people and their relations,
- **SKOS** for thesauri and taxonomies, used by the Corporate Memory [Thesauri management](../../explore-and-author/thesauri-management/index.md),
- the **Organization Ontology** for organizational structures,
- **PROV-O** for provenance,
- **schema.org** for structured data on the Web.

Reusing them saves modeling work, and makes the data understandable to others who know these vocabularies.
A domain vocabulary can extend them with its own subclasses and subproperties.
The [Vocabulary Catalog](../../explore-and-author/vocabulary-catalog/index.md) installs common vocabularies into Corporate Memory.

## Summary { #summary }

RDF Schema describes classes and properties, their hierarchies, domains and ranges, and annotates them for people.
It is enough for a lightweight ontology.
OWL adds equivalence, disjointness, inverse and other property characteristics, class constructors and restrictions.

Both infer rather than check.
For validating data, Corporate Memory uses SHACL.

A widely cited definition, by Studer, Benjamins and Fensel in 1998 after Thomas Gruber, sums up the goal: an ontology is a formal, explicit specification of a shared conceptualization.
How to arrive at such a specification is the topic of the hands-on module [Ontology Engineering](../ontology-engineering/index.md).
