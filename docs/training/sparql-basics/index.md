---
title: "Training: SPARQL Basics"
icon: material/presentation
tags:
  - BeginnersTutorial
  - SPARQL
---
# SPARQL Basics

<div class="training-deck">
<iframe src="slides.html" title="Slides: SPARQL Basics" allow="fullscreen"></iframe>
</div>

!!! abstract "About this module"

    This module teaches how to query RDF graphs with SPARQL, from the first triple pattern to aggregation and updates, and ends with exercises on the product Knowledge Graph.
    It builds on [RDF and Linked Data Foundations](../rdf-and-linked-data/index.md) and is part of the [Corporate Memory training](../index.md).

    Use **Show slide** next to a heading to bring the matching slide into view, or **Read the explanation** under the slides to jump to the text for the current slide.
    All queries run in the [Query module](../../explore-and-author/query-module/index.md) of eccenca Corporate Memory.

## Why a query language for RDF { #why-a-query-language }

An RDF graph answers questions only when there is a way to ask them.
Typical questions combine several statements:

- Which German-language strings occur in the data? – a condition on literals.
- Which relations hold between two given entities? – a variable in the predicate position.
- Which pairs of persons share a parent? – a pattern that joins two statements on a common node.

A query language for RDF has to express such graph patterns in a readable way, cover schema and instance data alike, and return results in formats that other tools consume.
SPARQL is that language.

## SPARQL { #sparql }

SPARQL is a recursive acronym for *SPARQL Protocol and RDF Query Language*.
Version 1.0 became a W3C Recommendation in 2008, version 1.1 in 2013, and 1.1 is what triple stores implement today.

SPARQL is a family of standards:

- the **query language**, to read from a graph,
- the **update language**, to change a graph,
- the **protocol**, which defines how a client sends queries to a SPARQL endpoint over HTTP,
- **result formats** in JSON, XML, CSV and TSV.

In Corporate Memory, SPARQL is everywhere.
The Query module edits and runs queries, the query catalog stores them for reuse, cmemc runs them from the command line, and SHACL forms, charts and custom APIs are driven by queries from the catalog.

## Structure of a query { #structure-of-a-query }

A SPARQL query has three parts:

1. **Prefix declarations** – like `@prefix` in Turtle, but written `PREFIX` and without the closing dot.
2. **The query form and its variables** – `SELECT ?name` returns a table with one column `name`.
3. **The graph pattern** in the `WHERE` block – the conditions a solution has to meet.

A graph pattern is written like Turtle, with variables in place of some terms.
A variable starts with `?` (or `$`), carries a freely chosen name and may stand in any position: subject, predicate or object.

The example uses the Registered Organization Vocabulary, whose property `rov:legalName` holds the official name of an organization.
The query reads: *find every `?x` with a legal name, and return the name*.

## Basic graph patterns { #basic-graph-patterns }

A set of triple patterns is a basic graph pattern.
The triple store searches for all ways to replace the variables with terms from the graph so that every pattern becomes a triple in the graph.
Each such replacement is one solution, and each solution becomes one row of the result.

In the example, the variable `?car` occurs in all three patterns.
This joins them: the three triples must share the same subject.
Only `ex:E63_AMG` satisfies all three, and the query returns its model and class.

Patterns that share no variable are not joined, and the result is the cross product of their solutions.
An unintended cross product is a frequent cause of slow queries with huge results.

## Matching literals { #matching-literals }

A literal in a pattern matches only the identical term.
The data contains four literals with the text `test`, but they are not the same term:

- `"test"` and `"test"^^xsd:string` are the same term in RDF 1.1, because a literal without a datatype is an `xsd:string`.
  The query returns both `ex:bsp1` and `ex:bsp2`.
- `"test"@de` is a language-tagged string, a different term.
- `"42"^^xsd:integer` is a number.

!!! note "Changed since RDF 1.0"

    Older slide versions show only `ex:bsp1` in the result.
    That was the behavior under RDF 1.0, where plain literals and `xsd:string` literals were different terms.

To find a text regardless of its language tag or datatype, compare its string value in a filter: `FILTER (STR(?o) = "test")`.

## OPTIONAL and UNION { #optional-and-union }

Braces group patterns.
Two keywords combine groups.

**`OPTIONAL { … }`** adds information when it exists, without discarding solutions when it does not.
In the customer example, every customer appears, and the variables `?phone` and `?email` stay unbound where the data has no value.
Without `OPTIONAL`, Schmidt, who has neither, would disappear from the result, and so would Meyer and Schulze.

**`{ … } UNION { … }`** accepts solutions from either of two patterns.
The union is not exclusive: Mueller, who has a phone number and an email address, appears twice, once for each.
Binding both alternatives to the same variable `?contactData` puts phone numbers and email addresses into one column.

## Combining OPTIONAL and UNION { #combining-optional-and-union }

`OPTIONAL` and `UNION` bind equally strong and are left-associative: each applies to everything written to its left within the same group.

This matters in a query such as *for all books published by Springer, show the author or editor and, if available, the first name*.
Written without extra braces, the `OPTIONAL` attaches to the whole union, which is the intended reading.
A reader who expects it to apply only to the editor branch is surprised by the result.

Explicit braces make the intention visible and cost nothing.

## FILTER { #filter }

Graph patterns select by structure.
Filters select by value: participants younger than 30, last names containing a hyphen, texts in German.

`FILTER (expression)` evaluates the expression for each solution and keeps only those for which it is true.
A solution is removed when the expression is false and also when it raises an error, for example a comparison between a number and a string.

A filter applies to the whole group it stands in, wherever in the group it is written.

## Operators { #operators }

**Comparison operators** – `<`, `=`, `>`, `<=`, `>=`, `!=` – compare literals by their natural order: numbers numerically, dates chronologically, strings alphabetically, and `false` before `true`.
IRIs and blank nodes support only `=` and `!=`.
Values of incompatible types, such as a string and an integer, cannot be compared, and the comparison is an error.

**Arithmetic operators** – `+`, `-`, `*`, `/` – work on numbers and combine values, as in `FILTER (?weight / (?length * ?height) >= 25)`.

**Logical operators** – `&&`, `||`, `!` – combine conditions.
SPARQL logic has three values: true, false and error.
`true || error` is true and `false && error` is false, because the other operand already decides the outcome; in every other case an error propagates.
At the end, the filter treats an error like false.

## Functions for RDF terms { #rdf-functions }

SPARQL provides functions that inspect RDF terms:

- `BOUND(?x)` tests whether a variable has a value, typically after `OPTIONAL`.
- `isIRI`, `isBLANK` and `isLITERAL` test the kind of term.
- `STR` returns the lexical form of a literal or IRI, `LANG` its language tag, `DATATYPE` its datatype IRI.
- `langMatches(LANG(?label), "de")` tests a language tag against a language range, so that `de` also matches `de-CH`.
- `REGEX(?text, "pattern", "i")` tests a string against a regular expression, here ignoring case.

SPARQL 1.1 adds string functions such as `CONTAINS`, `STRSTARTS`, `LCASE`, `CONCAT` and `REPLACE`, which are faster and easier to read than a regular expression for simple cases.

## Negation { #negation }

*Show all cars without a price* asks for something that is not in the data.
`FILTER NOT EXISTS { … }` keeps a solution only if the enclosed pattern has no match for it.

`MINUS { … }` removes the solutions that are compatible with the enclosed pattern.
The two give the same result in most queries, and differ when the patterns share no variable.
`FILTER NOT EXISTS` is the safer default.

The older idiom `OPTIONAL { … } FILTER (!BOUND(?x))` achieves the same and appears in many existing queries.

## Solution modifiers { #solution-modifiers }

Solution modifiers shape the result table after the pattern has been matched:

- `ORDER BY` sorts the rows.
  `ASC()` is the default, `DESC()` reverses, and several keys sort hierarchically.
- `DISTINCT` removes duplicate rows.
- `OFFSET n` skips the first n rows.
- `LIMIT n` returns at most n rows.

The modifiers apply in this order: sort, remove duplicates, skip, cut.
Without `ORDER BY`, the order of the rows is undefined, and `LIMIT` and `OFFSET` return arbitrary rows.
Combine them with `ORDER BY` to page through a result reliably.

## Query forms { #query-forms }

SPARQL has four query forms, which differ in what they return:

- `SELECT` returns a table of variable bindings, the most common form.
- `ASK` returns true or false, depending on whether the pattern matches at all.
  In the example, BARCO has no registered site, so the answer is `false`.
- `DESCRIBE` returns an RDF graph with information about the resources found.
  The standard leaves open which triples belong to the description.
  Most stores return the triples with the resource as subject, the Concise Bounded Description.
- `CONSTRUCT` returns an RDF graph built from a template.

The examples use two W3C vocabularies: `rov:` for the Registered Organization Vocabulary and `org:` for the Organization Ontology.

## CONSTRUCT { #construct }

`CONSTRUCT` turns query results into new triples.
The template after `CONSTRUCT` is a set of triple patterns, and the triple store fills in the variables for every solution of the `WHERE` block.

The example derives an `rdfs:label` from each legal name.
Typical uses are mapping data from one vocabulary to another, deriving shortcuts over long paths, and extracting a subgraph for export.
In Corporate Memory, a `CONSTRUCT` query in a workflow writes its result into a graph, which makes it a building block for data transformation.

## Aggregation and more { #aggregation }

SPARQL 1.1 added the features that make it a complete analysis language:

- **Aggregates** – `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `SAMPLE`, `GROUP_CONCAT` – summarize the rows of each group formed by `GROUP BY`.
  The example counts the products per product manager.
- **Projection of expressions** – `(COUNT(?product) AS ?products)` or `BIND (… AS ?x)` assign a computed value to a new variable.
- **Subqueries** nest a complete `SELECT` inside a pattern.
- **`VALUES`** provides a fixed list of bindings, for example a list of IRIs to look up.
- **Property paths** follow chains and repetitions of properties: `prod:memberOf/rdfs:label` reaches the label of the department, `rdfs:subClassOf*` walks a class hierarchy to any depth.

## SPARQL Update { #sparql-update }

SPARQL 1.1 Update changes graphs:

- `INSERT DATA { … }` and `DELETE DATA { … }` add or remove the given triples.
- `DELETE { … } INSERT { … } WHERE { … }` computes the changes from a pattern, for example to rename a property throughout a graph.
- `CLEAR GRAPH`, `DROP GRAPH`, `LOAD` and `COPY` work on whole graphs.

`GRAPH <iri> { … }` selects the named graph to change.
In Corporate Memory, every graph is a named graph, and write access is controlled per graph by access conditions.

## Exercises { #exercises }

The exercises use the product Knowledge Graph built in module 1, see [Lift data from tabular data](../../build/lift-data-from-tabular-data-such-as-csv-xslx-or-database-tables/index.md).
Its vocabulary uses the prefix `prod:` for `http://ld.company.org/prod-vocab/`.
Run the queries in the Query module, against the graph that contains the instance data.

??? example "1. Find all products"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?product ?label
    WHERE {
      ?product a prod:Product .
      OPTIONAL { ?product rdfs:label ?label . }
    }
    ORDER BY ?label
    ```

??? example "2. Find products lighter than 10"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?product ?weight
    WHERE {
      ?product a prod:Product ;
               prod:weight ?weight .
      FILTER (?weight < 10)
    }
    ```

    The products vocabulary defines no weight property.
    Use the property that the mapping of the `Weigth` column of `products.xlsx` writes to, `prod:weight` is an example.

??? example "3. Find products and services without a product manager"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?item
    WHERE {
      { ?item a prod:Product . } UNION { ?item a prod:Service . }
      FILTER NOT EXISTS { ?item prod:hasProductManager ?manager . }
    }
    ```

??? example "4. Find products without a responsible department"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?product
    WHERE {
      ?product a prod:Product .
      FILTER NOT EXISTS { ?department prod:responsibleFor ?product . }
    }
    ```

??? example "5. Find experts for the category of a product"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?product ?category ?expert
    WHERE {
      ?product prod:hasCategory ?category .
      ?expert prod:expertFor ?category .
    }
    ```

??? example "6. Count the products per manager and department"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?department ?manager (COUNT(DISTINCT ?product) AS ?products)
    WHERE {
      ?product prod:hasProductManager ?manager .
      OPTIONAL { ?manager prod:memberOf ?department . }
    }
    GROUP BY ?department ?manager
    ORDER BY ?department DESC(?products)
    ```

    Save this query in the query catalog.
    The charts and custom API exercises reuse it.

??? example "7. Insert yourself as an employee"

    ```sparql
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    INSERT DATA {
      GRAPH <http://ld.company.org/prod-instances/> {
        <http://ld.company.org/prod-inst/jane-doe> a prod:Employee ;
            rdfs:label "Jane Doe" ;
            prod:email "jane.doe@company.org" .
      }
    }
    ```

    Replace the IRI, label and email address with personal values, and the graph IRI with the instance graph of the project.

## Summary { #summary }

| Area | Elements |
| --- | --- |
| Basic structure | `PREFIX`, `WHERE { }` |
| Query forms | `SELECT`, `ASK`, `DESCRIBE`, `CONSTRUCT` |
| Graph patterns | basic graph patterns, `{ }`, `OPTIONAL`, `UNION`, `FILTER NOT EXISTS`, `MINUS` |
| Solution modifiers | `ORDER BY`, `DISTINCT`, `OFFSET`, `LIMIT` |
| Filter functions | `BOUND`, `isIRI`, `isBLANK`, `isLITERAL`, `STR`, `LANG`, `DATATYPE`, `sameTerm`, `langMatches`, `REGEX` |
| SPARQL 1.1 | aggregates, `GROUP BY`, `BIND`, `VALUES`, subqueries, property paths, update |

The full language is specified in the [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) recommendation.
