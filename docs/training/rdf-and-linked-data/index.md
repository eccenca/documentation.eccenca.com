---
title: "Training: RDF and Linked Data Foundations"
icon: material/presentation
tags:
  - BeginnersTutorial
  - KnowledgeGraph
---
# RDF and Linked Data Foundations

<div class="training-deck">
<iframe src="slides.html" title="Slides: RDF and Linked Data Foundations" allow="fullscreen"></iframe>
</div>

!!! abstract "About this module"

    This module introduces the ideas behind the Semantic Web and the RDF data model that every Knowledge Graph in eccenca Corporate Memory is built on.
    It is the first module of the [Corporate Memory training](../index.md) and needs no previous knowledge.

    The slides are the material trainers present in class.
    The sections below explain each slide in the detail a trainer gives orally, so the module also works for self-study.
    Use **Show slide** next to a heading to bring the matching slide into view, or **Read the explanation** under the slides to jump to the text for the current slide.

## Syntax and semantics { #syntax-and-semantics }

Every language, natural or formal, has two sides.
Its syntax defines which expressions are well-formed, and its semantics defines what a well-formed expression means.

The arithmetic examples on the slide separate the two.
`4+)2=(` is not even a valid expression.
`4+2=10` is valid but false, and `4+2` and `2+4` look different and mean the same.

Computers handle syntax well: a parser rejects `4+)2=(` without understanding anything about numbers.
Meaning is harder.
The technologies in this training exist to write meaning down in a form that a machine can process, compare and combine.

## Implicit and contextual meaning { #implicit-and-contextual-meaning }

Much of what people understand is never stated.
Implicit meaning is knowledge that follows from what is said together with background knowledge.
*Emil is a bear* says nothing about mammals, yet everyone concludes that Emil is a mammal, because bears are mammals.

Contextual meaning depends on the surroundings of an expression.
In *the fisherman went to the bank*, the word *bank* is ambiguous, and the fisherman makes the river bank more likely than the financial institution.

A machine has neither the background knowledge nor the context.
An ontology supplies the first: it states that every bear is a mammal, so a reasoner derives the conclusion a person draws without thinking.
Unique identifiers remove the second problem: a resource named by an IRI means one thing only, whatever the surrounding text.

## Why the Web needs semantics { #why-the-web-needs-semantics }

The Web holds an enormous amount of information, transferred in standardized syntax.
It is, however, written for people.
A search engine matches words, it does not combine facts.

Questions such as *ERP service providers with offices in Vienna and Berlin* need facts from several sources joined together: who provides ERP services, where each provider has offices, and that Vienna and Berlin are cities.
Each fact may well be on the Web.
The answer is not, because no single document states it.

Three things are needed to close that gap:

- structure, so that facts can be found rather than words,
- shared standards, so that facts from different sources can be integrated,
- a formal representation of meaning, so that a machine can derive what is only implied.

The same gap exists inside every larger organization, where the sources are databases, spreadsheets and documents instead of web sites.

## The semantic approach { #the-semantic-approach }

Different people and systems name the same thing differently.
One system stores *Plane*, another *Airplane*, a third *Aeroplane*.
Integrating their data starts with agreeing that these are one concept, with one identifier and one definition: a vehicle that generates lift, has wings and transports people or goods.

This shared concept is the knowledge anchor of the slide.
Two kinds of benefit follow from it:

- **Integrate knowledge.**
  An ontology defines the concept and its relations, for example that a plane has wings.
  A controlled vocabulary records that *Plane*, *Airplane* and *Aeroplane* are names for the same concept, so data from systems A, B and C lands on one node.
- **Enrich knowledge.**
  Once the Airbus A320 is known to be a plane, a reasoner concludes that it has wings, although no source states it.
  Such explicit, traceable knowledge is also what makes the answers of AI models and LLMs explainable.

## The Semantic Web { #the-semantic-web }

The Semantic Web is the vision of a Web of data that machines can interpret, developed under the W3C since the late 1990s.
It rests on two ingredients: open standards for writing down information and its meaning, and methods for deriving further information from such descriptions.

Ontologies are the core of the second ingredient.
They provide a shared reference frame that disambiguates terms and links meaning across sources, and they carry the background knowledge from which implicit facts are derived.
Because their semantics is formally defined, any compliant reasoner draws the same conclusions.
Published on the Web, an ontology becomes a shared resource that independent parties reuse.

Enterprise Knowledge Graphs apply the same standards inside an organization, without publishing the data.

## Semantic Web standards { #semantic-web-standards }

The "layer cake" shows how the W3C standards build on each other.

| Layer | Standard | Purpose |
| --- | --- | --- |
| Identifiers | URI, IRI, Unicode | name every resource globally and unambiguously |
| Data | RDF | represent data as a graph of statements |
| Schema | RDF Schema | describe classes, properties and their hierarchies |
| Ontology | OWL | describe concepts with richer logic, such as equivalence and cardinality |
| Rules | RIF | exchange rules between rule systems |
| Query | SPARQL | query and update RDF data |
| Validation | SHACL (2017, not in the original diagram) | describe the expected shape of data and validate against it |

The upper layers – unifying logic, proof and trust – describe research goals rather than finished standards.
The XML layer is historical: RDF is serialized in Turtle or JSON-LD far more often than in XML today.

Corporate Memory implements the layers that matter in practice: RDF for all data, RDF Schema and OWL for vocabularies, SPARQL for queries, and SHACL for forms and validation.

## Linked Data principles { #linked-data-principles }

In 2006, Tim Berners-Lee, the inventor of the World Wide Web, summarized in a design note how to publish data on the Web so that it links up:

1. Use URIs as names for things.
2. Use HTTP URIs, so that people can look up those names.
3. When someone looks up a URI, provide useful information, using the standards RDF and SPARQL.
4. Include links to other URIs, so that they can discover more things.

Data published this way is called Linked Data, and Linked Open Data when it is published under an open license.
The Linked Open Data cloud shows how far the idea went: from a dozen datasets around DBpedia in 2007 to more than a thousand datasets ten years later, covering life sciences, government, publications, geography and media.

The same principles serve an enterprise.
When every product, department and employee has a stable HTTP IRI, links between data from different systems are just statements, and every IRI can resolve to a description of its resource.

## RDF { #rdf }

The Resource Description Framework is the data model of the Semantic Web.
It became a W3C Recommendation in 1999, and RDF 1.1 from 2014 is the version in use today.

RDF was first designed to describe web resources, for example the author and date of a document.
It was soon generalized to describe anything: products, people, places, concepts.
It is a universal exchange format: any structured data, from a spreadsheet row to a database table to an XML tree, can be expressed in RDF without loss.

SPARQL is the query language for RDF and the topic of the [SPARQL basics](../sparql-basics/index.md) module.

## Parts of an RDF graph { #parts-of-an-rdf-graph }

RDF data is a directed graph with labeled edges.
Three kinds of terms occur in it:

- **IRIs** name resources, both the nodes and the edges.
  An edge label is itself a resource, called a property, and can be described like any other.
- **Literals** are data values such as strings, numbers and dates.
  They are always end points of an edge.
- **Blank nodes** stand for a resource that has no global name.
  They state that something with certain properties exists, without naming it.

## A first graph { #a-first-graph }

The graph around Leipzig shows all three kinds of terms at work.
Leipzig, Saxony, Germany, Burkhard Jung and the Social Democratic Party are resources.
The coordinates, the area code and the date of birth are literals.

Two details are worth noting:

- The area code `0341` is a literal string, not a number, because the leading zero matters.
- `hasMayor` and `isMayorOf` are two different edges.
  RDF has no notion of an inverse edge, each direction is a statement of its own.
  OWL can declare one property the inverse of the other, so that a reasoner adds the missing direction.

## RDF statements: triples { #triples }

Every edge of the graph is one statement, called a triple, written subject – predicate – object:

- The **subject** is the resource the statement is about: an IRI or a blank node.
- The **predicate** is the property, the label of the edge: always an IRI.
- The **object** is the value: an IRI, a blank node or a literal.

A graph is nothing more than the set of its triples.
Writing down the triples of the Leipzig graph and drawing them again gives back the same graph, because every node and every edge is identified unambiguously.

Merging two graphs is just the union of their triple sets.
When both use the same IRI for Leipzig, the statements about Leipzig join up without any further mapping.
This is what makes RDF suited for data integration.

## IRIs { #iris }

IRIs, Internationalized Resource Identifiers, are the Unicode-aware generalization of URIs, Uniform Resource Identifiers.
Both terms appear in practice, and RDF 1.1 uses IRIs.

An IRI is a globally unique name.
Anything with a clear identity can have one: a book, a city, an organization, a product, a concept.
The ISBN plays the same role for books, the IRI generalizes it to everything.

An IRI starts with a scheme such as `http`, `https`, `mailto` or `urn`, followed by a hierarchical part:

```text
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

An IRI is a name first.
It does not have to resolve to a document, although Linked Data recommends that it does.
To avoid collisions with names chosen by others, create IRIs in an HTTP namespace that the organization controls, such as `http://ld.company.org/prod-vocab/` in the hands-on exercises.

## Literals { #literals }

Literals represent data values.
A literal is a string, its lexical form, plus a datatype that says how to interpret it.

- Without an explicit datatype, a literal is an `xsd:string`.
- A string can carry a language tag such as `@en`, and is then of type `rdf:langString`.
- Literals appear only in the object position.
  A literal can be neither the subject of a statement nor the label of an edge.

## Datatypes { #datatypes }

The datatype determines how values compare and sort.
As plain strings, `"02" < "100" < "11" < "2"`, because strings are compared character by character.
As `xsd:integer` values, the order is numeric.

A typed literal is written `"value"^^datatype`, for example `"1958-03-07"^^xsd:date` or `"12.3833"^^xsd:decimal`.
RDF reuses the datatypes of XML Schema, under the namespace `http://www.w3.org/2001/XMLSchema#` with the usual prefix `xsd:`.
The most frequent are `xsd:string`, `xsd:integer`, `xsd:decimal`, `xsd:double`, `xsd:boolean`, `xsd:date` and `xsd:dateTime`.

The example uses the W3C geo vocabulary, whose properties for coordinates are `geo:lat` and `geo:long`.

## Labels and language tags { #labels-and-language-tags }

IRIs are made for machines.
For people, a resource gets a label with the property `rdfs:label`, whose values are literals.

One resource can have labels in several languages, each marked with a language tag.
Corporate Memory shows the label in the language the user prefers and falls back to other languages or to the IRI when no label exists.

Language tags follow BCP 47: `en`, `de`, `pt`, and region variants such as `en-GB`.
A language tag can be combined only with a string, not with another datatype.

## Serializations { #serializations }

An RDF graph is abstract, and several syntaxes write it down as text.
All of them describe the same triples, and tools convert between them without loss.

- **N-Triples** writes one complete triple per line with full IRIs.
  It is verbose but easy to split, stream and compare line by line.
- **Turtle**, the Terse RDF Triple Language, is compact and readable.
  It is the format used throughout this training.
- **JSON-LD** encodes RDF as JSON and fits web APIs.
- **RDF/XML** is the original syntax, still found in older vocabularies.
- **TriG** and **N-Quads** extend Turtle and N-Triples with named graphs, so that one file can hold several graphs.

Corporate Memory imports and exports these formats, for example with the cmemc commands `graph import` and `graph export`.

## Turtle { #turtle }

In Turtle, a triple is written like a sentence: subject, predicate and object, separated by whitespace and terminated by a dot.
IRIs stand in angle brackets, literals in quotes.
Line breaks and indentation are free, and are used to make the structure visible.

Full IRIs make a file long and hard to read.
A prefix declaration binds a short name to a namespace, and `dbr:Leipzig` then stands for `http://dbpedia.org/resource/Leipzig`.
Prefixes are pure notation: the graph contains the full IRIs.

Two further abbreviations remove repetition:

- A semicolon `;` continues with a new predicate for the same subject.
- A comma `,` continues with a new object for the same subject and predicate.

The full example on the slide describes Leipzig, Saxony and Burkhard Jung in a few lines.
It also shows the typed date of birth and that `locatedIn` holds two values, Saxony and Germany.

## Classes { #classes }

Resources are grouped into classes.
A class is a set of things, and is itself named by an IRI, for example `ex:Car`.

The property `rdf:type` states that a resource is an instance of a class.
It is used so often that Turtle offers the keyword `a` as shorthand, and both lines on the slide are the same triple.
A resource can belong to any number of classes: the blue VW Golf is a car and a German product at the same time.

How classes form hierarchies, and how properties are tied to classes, is the subject of the ontology module.

## n-ary relations { #n-ary-relations }

An RDF statement connects exactly two things.
Some facts connect more: a recipe, an ingredient and its amount belong together.

The first attempt on the slide stores ingredient and amount in one string.
The facts are recorded, but a machine cannot find recipes that use green mango, because green mango is not a resource.

The second attempt attaches ingredients and amounts to the recipe separately.
Now the association is lost: nothing in the graph says that 450 g belongs to the mango and not to the pepper.

The solution is a helper node that represents the combination itself.
The recipe points to the helper node, and the helper node points to the ingredient and the amount.
This is the standard pattern for any relation with more than two participants, and also for relations that need attributes of their own, such as a validity period.

## Blank nodes { #blank-nodes }

A helper node rarely needs a global name.
A blank node is a node without an IRI: it states that there is something with the given properties.

In Turtle, a blank node is written with a label such as `_:id1`, which is valid only inside the file.
Square brackets are shorter and need no label: the brackets enclose the description of an anonymous resource.

Blank nodes have a price.
Because they have no global name, they cannot be referenced from outside the graph, and two graphs that describe the same blank node cannot be merged on it.
Many Knowledge Graph projects therefore give helper nodes generated IRIs instead, which the mapping tools of Corporate Memory create from a URI pattern.

## Lists { #lists }

RDF has two ways of writing lists, both built from ordinary triples.

**Containers** are open lists, to which more members can be added.
The container node has one of three types: `rdf:Bag` for an unordered set, `rdf:Seq` for an ordered sequence, and `rdf:Alt` for a set of alternatives of which usually one applies.
The members hang off the properties `rdf:_1`, `rdf:_2` and so on.

**Collections** are closed, ordered lists.
Turtle writes them in parentheses.
Internally each element is a node with `rdf:first`, pointing to the element, and `rdf:rest`, pointing to the remainder of the list, which ends with `rdf:nil`.
OWL uses collections to enumerate class members and to combine classes.

## Summary { #summary }

RDF is a widely supported standard for storing and exchanging data, and triple stores handle graphs with billions of statements.
Because every resource has a global name, data from many sources merges into one graph.

Plain RDF describes individuals, but it has little to say about their kinds.
That a car is a motor vehicle, or that only a person drives, is schema knowledge, described with RDF Schema and OWL.
Getting answers out of a graph needs a query language, SPARQL.

Continue with:

- the module [SPARQL basics](../sparql-basics/index.md),
- the tutorial [Lift data from tabular data](../../build/lift-data-from-tabular-data-such-as-csv-xslx-or-database-tables/index.md), which builds a Knowledge Graph from the data used in the hands-on exercises.
