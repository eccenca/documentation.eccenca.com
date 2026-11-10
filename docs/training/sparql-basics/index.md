---
title: "Training: SPARQL Basics"
hide:
  - toc
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
    The **Try it** boxes run the queries of the slides directly in the browser, against the data shown in the box, without a Corporate Memory instance.

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

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix rov:  <http://www.w3.org/ns/regorg#> .
    @prefix org:  <http://www.w3.org/ns/org#> .
    @prefix comp: <http://example.org/company/> .
    @prefix site: <http://example.org/site/> .

    comp:A rov:legalName "Niké" ;
           org:hasRegisteredSite site:1234 .
    comp:B rov:legalName "BARCO" .
    ```

    ```sparql { .try-query }
    PREFIX rov: <http://www.w3.org/ns/regorg#>

    SELECT ?name
    WHERE {
      ?x rov:legalName ?name .
    }
    ```

    <div class="try-result" markdown>

    2 rows

    | name |
    | --- |
    | `"BARCO"` |
    | `"Niké"` |

    </div>

## Basic graph patterns { #basic-graph-patterns }

A set of triple patterns is a basic graph pattern.
The triple store searches for all ways to replace the variables with terms from the graph so that every pattern becomes a triple in the graph.
Each such replacement is one solution, and each solution becomes one row of the result.

In the example, the variable `?car` occurs in all three patterns.
This joins them: the three triples must share the same subject.
Only `ex:E63_AMG` satisfies all three, and the query returns its model and class.

Patterns that share no variable are not joined, and the result is the cross product of their solutions.
An unintended cross product is a frequent cause of slow queries with huge results.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .

    ex:E63_AMG ex:producedBy <http://mercedes-benz.de/> ;
               ex:model "E63 AMG" ;
               ex:class "E-Klasse" .
    ex:C200    ex:producedBy <http://mercedes-benz.de/> ;
               ex:model "C 200" .
    ex:M3      ex:producedBy <http://bmw.de/> ;
               ex:model "M3" ;
               ex:class "3er" .
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?model ?class
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      ?car ex:model ?model .
      ?car ex:class ?class .
    }
    ```

    <div class="try-result" markdown>

    1 row

    | model | class |
    | --- | --- |
    | `"E63 AMG"` | `"E-Klasse"` |

    </div>

    The second query uses two variables, `?car` and `?other`, so its patterns are not joined.
    Each of the two Mercedes-Benz cars combines with each of the three models:

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?car ?model
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      ?other ex:model ?model .
    }
    ```

    <div class="try-result" markdown>

    6 rows

    | car | model |
    | --- | --- |
    | `ex:E63_AMG` | `"M3"` |
    | `ex:C200` | `"M3"` |
    | `ex:E63_AMG` | `"C 200"` |
    | `ex:C200` | `"C 200"` |
    | `ex:E63_AMG` | `"E63 AMG"` |
    | `ex:C200` | `"E63 AMG"` |

    </div>

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

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex:  <http://example.org/> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    ex:bsp1 ex:p "test" .
    ex:bsp2 ex:p "test"^^xsd:string .
    ex:bsp3 ex:p "test"@de .
    ex:bsp4 ex:p "42"^^xsd:integer .
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?subject
    WHERE {
      ?subject ex:p "test" .
    }
    ```

    <div class="try-result" markdown>

    2 rows

    | subject |
    | --- |
    | `ex:bsp2` |
    | `ex:bsp1` |

    </div>

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?subject ?o
    WHERE {
      ?subject ex:p ?o .
      FILTER (STR(?o) = "test")
    }
    ```

    <div class="try-result" markdown>

    3 rows

    | subject | o |
    | --- | --- |
    | `ex:bsp3` | `"test"@de` |
    | `ex:bsp2` | `"test"` |
    | `ex:bsp1` | `"test"` |

    </div>

## OPTIONAL and UNION { #optional-and-union }

Braces group patterns.
Two keywords combine groups.

**`OPTIONAL { … }`** adds information when it exists, without discarding solutions when it does not.
In the customer example, every customer appears, and the variables `?phone` and `?email` stay unbound where the data has no value.
Without `OPTIONAL`, Schmidt, who has neither, would disappear from the result, and so would Meyer and Schulze.

**`{ … } UNION { … }`** accepts solutions from either of two patterns.
The union is not exclusive: Mueller, who has a phone number and an email address, appears twice, once for each.
Binding both alternatives to the same variable `?contactData` puts phone numbers and email addresses into one column.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix : <http://example.org/customers/> .

    :c1 :hasName "Mueller" ;
        :hasPhoneNumber "03414483711" ;
        :hasEmail "mueller@example.org" .
    :c2 :hasName "Meyer" ;
        :hasEmail "meyer@example.org" .
    :c3 :hasName "Schulze" ;
        :hasPhoneNumber "0308473625" .
    :c4 :hasName "Schmidt" .
    ```

    ```sparql { .try-query }
    PREFIX : <http://example.org/customers/>

    SELECT ?customer ?phone ?email
    WHERE {
      ?customerID :hasName ?customer .
      OPTIONAL { ?customerID :hasPhoneNumber ?phone . }
      OPTIONAL { ?customerID :hasEmail ?email . }
    }
    ```

    <div class="try-result" markdown>

    4 rows

    | customer | phone | email |
    | --- | --- | --- |
    | `"Schmidt"` |  |  |
    | `"Schulze"` | `"0308473625"` |  |
    | `"Meyer"` |  | `"meyer@example.org"` |
    | `"Mueller"` | `"03414483711"` | `"mueller@example.org"` |

    </div>

    ```sparql { .try-query }
    PREFIX : <http://example.org/customers/>

    SELECT ?contactData ?customer
    WHERE {
      ?customerID :hasName ?customer .
      { ?customerID :hasPhoneNumber ?contactData . }
      UNION
      { ?customerID :hasEmail ?contactData . }
    }
    ```

    <div class="try-result" markdown>

    4 rows

    | contactData | customer |
    | --- | --- |
    | `"0308473625"` | `"Schulze"` |
    | `"meyer@example.org"` | `"Meyer"` |
    | `"03414483711"` | `"Mueller"` |
    | `"mueller@example.org"` | `"Mueller"` |

    </div>

## Combining OPTIONAL and UNION { #combining-optional-and-union }

`OPTIONAL` and `UNION` bind equally strong and are left-associative: each applies to everything written to its left within the same group.

This matters in a query such as *for all books published by Springer, show the author or editor and, if available, the first name*.
Written without extra braces, the `OPTIONAL` attaches to the whole union, which is the intended reading.
A reader who expects it to apply only to the editor branch is surprised by the result.

Explicit braces make the intention visible and cost nothing.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex:   <http://example.org/> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .

    ex:book1 ex:publishedBy ex:Springer ;
             ex:author ex:alice .
    ex:book2 ex:publishedBy ex:Springer ;
             ex:editor ex:bob .
    ex:book3 ex:publishedBy ex:Springer ;
             ex:editor ex:carol .
    ex:book4 ex:publishedBy ex:Elsevier ;
             ex:author ex:dave .

    ex:alice foaf:firstName "Alice" .
    ex:bob   foaf:firstName "Bob" .
    ex:dave  foaf:firstName "Dave" .
    ```

    The `OPTIONAL` applies to the whole union, so authors and editors get their first name:

    ```sparql { .try-query }
    PREFIX ex:   <http://example.org/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?book ?person ?firstName
    WHERE {
      { ?book ex:publishedBy ex:Springer ; ex:author ?person . }
      UNION
      { ?book ex:publishedBy ex:Springer ; ex:editor ?person . }
      OPTIONAL { ?person foaf:firstName ?firstName . }
    }
    ```

    <div class="try-result" markdown>

    3 rows

    | book | person | firstName |
    | --- | --- | --- |
    | `ex:book1` | `ex:alice` | `"Alice"` |
    | `ex:book3` | `ex:carol` |  |
    | `ex:book2` | `ex:bob` | `"Bob"` |

    </div>

    Braces that move the `OPTIONAL` into the editor branch change the result, and the author loses the first name:

    ```sparql { .try-query }
    PREFIX ex:   <http://example.org/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?book ?person ?firstName
    WHERE {
      { ?book ex:publishedBy ex:Springer ; ex:author ?person . }
      UNION
      { ?book ex:publishedBy ex:Springer ; ex:editor ?person .
        OPTIONAL { ?person foaf:firstName ?firstName . } }
    }
    ```

    <div class="try-result" markdown>

    3 rows

    | book | person | firstName |
    | --- | --- | --- |
    | `ex:book1` | `ex:alice` |  |
    | `ex:book3` | `ex:carol` |  |
    | `ex:book2` | `ex:bob` | `"Bob"` |

    </div>

## FILTER { #filter }

Graph patterns select by structure.
Filters select by value: participants younger than 30, last names containing a hyphen, texts in German.

`FILTER (expression)` evaluates the expression for each solution and keeps only those for which it is true.
A solution is removed when the expression is false and also when it raises an error, for example a comparison between a number and a string.

A filter applies to the whole group it stands in, wherever in the group it is written.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .

    ex:E63_AMG ex:producedBy <http://mercedes-benz.de/> ;
               ex:model "E63 AMG" ;
               ex:price 115000 .
    ex:C200    ex:producedBy <http://mercedes-benz.de/> ;
               ex:model "C 200" ;
               ex:price 48500 .
    ex:A180    ex:producedBy <http://mercedes-benz.de/> ;
               ex:model "A 180" .
    ```

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?car
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      ?car ex:price ?price .
      FILTER (?price < 70000)
    }
    ```

    <div class="try-result" markdown>

    1 row

    | car |
    | --- |
    | `ex:C200` |

    </div>

## Operators { #operators }

**Comparison operators** – `<`, `=`, `>`, `<=`, `>=`, `!=` – compare literals by their natural order: numbers numerically, dates chronologically, strings alphabetically, and `false` before `true`.
IRIs and blank nodes support only `=` and `!=`.
Values of incompatible types, such as a string and an integer, cannot be compared, and the comparison is an error.

**Arithmetic operators** – `+`, `-`, `*`, `/` – work on numbers and combine values, as in `FILTER (?weight / (?length * ?height) >= 25)`.

**Logical operators** – `&&`, `||`, `!` – combine conditions.
SPARQL logic has three values: true, false and error.
`true || error` is true and `false && error` is false, because the other operand already decides the outcome; in every other case an error propagates.
At the end, the filter treats an error like false.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .

    ex:anna  ex:name "Anna Schmidt-Lehmann" ;
             ex:age 27 .
    ex:ben   ex:name "Ben Ott" ;
             ex:age 34 .
    ex:clara ex:name "Clara Weiss" ;
             ex:age "unknown" .
    ```

    Comparing the string `"unknown"` with a number is an error, so the filter removes Clara:

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?name ?age
    WHERE {
      ?person ex:name ?name ;
              ex:age ?age .
      FILTER (?age < 30)
    }
    ```

    <div class="try-result" markdown>

    1 row

    | name | age |
    | --- | --- |
    | `"Anna Schmidt-Lehmann"` | `"27"^^xsd:integer` |

    </div>

    With `||`, the error meets a true operand, and Clara is back:

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?name ?age
    WHERE {
      ?person ex:name ?name ;
              ex:age ?age .
      FILTER (?age < 30 || CONTAINS(?name, "Weiss"))
    }
    ```

    <div class="try-result" markdown>

    2 rows

    | name | age |
    | --- | --- |
    | `"Clara Weiss"` | `"unknown"` |
    | `"Anna Schmidt-Lehmann"` | `"27"^^xsd:integer` |

    </div>

## Functions for RDF terms { #rdf-functions }

SPARQL provides functions that inspect RDF terms:

- `BOUND(?x)` tests whether a variable has a value, typically after `OPTIONAL`.
- `isIRI`, `isBLANK` and `isLITERAL` test the kind of term.
- `STR` returns the lexical form of a literal or IRI, `LANG` its language tag, `DATATYPE` its datatype IRI.
- `langMatches(LANG(?label), "de")` tests a language tag against a language range, so that `de` also matches `de-CH`.
- `REGEX(?text, "pattern", "i")` tests a string against a regular expression, here ignoring case.

SPARQL 1.1 adds string functions such as `CONTAINS`, `STRSTARTS`, `LCASE`, `CONCAT` and `REPLACE`, which are faster and easier to read than a regular expression for simple cases.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex:   <http://example.org/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

    ex:zurich rdfs:label "Zürich"@de-CH , "Zurich"@en .
    ex:munich rdfs:label "München"@de , "Munich"@en .
    ex:paris  rdfs:label "Paris" .
    ```

    ```sparql { .try-query }
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?city ?label (LANG(?label) AS ?lang) (DATATYPE(?label) AS ?datatype)
    WHERE {
      ?city rdfs:label ?label .
      FILTER langMatches(LANG(?label), "de")
    }
    ```

    <div class="try-result" markdown>

    2 rows

    | city | label | lang | datatype |
    | --- | --- | --- | --- |
    | `ex:munich` | `"München"@de` | `"de"` | `rdf:langString` |
    | `ex:zurich` | `"Zürich"@de-ch` | `"de-ch"` | `rdf:langString` |

    </div>

    ```sparql { .try-query }
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?city ?label
    WHERE {
      ?city rdfs:label ?label .
      FILTER REGEX(?label, "^mu", "i")
    }
    ```

    <div class="try-result" markdown>

    1 row

    | city | label |
    | --- | --- |
    | `ex:munich` | `"Munich"@en` |

    </div>

## Negation { #negation }

*Show all cars without a price* asks for something that is not in the data.
`FILTER NOT EXISTS { … }` keeps a solution only if the enclosed pattern has no match for it.

`MINUS { … }` removes the solutions that are compatible with the enclosed pattern.
The two give the same result in most queries, and differ when the patterns share no variable.
`FILTER NOT EXISTS` is the safer default.

The older idiom `OPTIONAL { … } FILTER (!BOUND(?x))` achieves the same and appears in many existing queries.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix ex: <http://example.org/> .

    ex:E63_AMG ex:producedBy <http://mercedes-benz.de/> ;
               ex:price 115000 .
    ex:C200    ex:producedBy <http://mercedes-benz.de/> ;
               ex:price 48500 .
    ex:A180    ex:producedBy <http://mercedes-benz.de/> .
    ```

    The three queries express the same question in the three ways:

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?car
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      FILTER NOT EXISTS { ?car ex:price ?price . }
    }
    ```

    <div class="try-result" markdown>

    1 row

    | car |
    | --- |
    | `ex:A180` |

    </div>

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?car
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      MINUS { ?car ex:price ?price . }
    }
    ```

    <div class="try-result" markdown>

    1 row

    | car |
    | --- |
    | `ex:A180` |

    </div>

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT ?car
    WHERE {
      ?car ex:producedBy <http://mercedes-benz.de/> .
      OPTIONAL { ?car ex:price ?price . }
      FILTER (!BOUND(?price))
    }
    ```

    <div class="try-result" markdown>

    1 row

    | car |
    | --- |
    | `ex:A180` |

    </div>

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

??? example try-sparql "Try it"

    Data: [thirty books with a price](data/books.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX ex: <http://example.org/>

    SELECT DISTINCT ?book ?price
    WHERE {
      ?book ex:price ?price .
    }
    ORDER BY DESC(?price) ?book
    LIMIT 5
    OFFSET 25
    ```

    <div class="try-result" markdown>

    5 rows

    | book | price |
    | --- | --- |
    | `ex:book13` | `"8.5"^^xsd:decimal` |
    | `ex:book28` | `"8.2"^^xsd:decimal` |
    | `ex:book20` | `"7.99"^^xsd:decimal` |
    | `ex:book27` | `"7.5"^^xsd:decimal` |
    | `ex:book26` | `"6.9"^^xsd:decimal` |

    </div>

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

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix rov:  <http://www.w3.org/ns/regorg#> .
    @prefix org:  <http://www.w3.org/ns/org#> .
    @prefix comp: <http://example.org/company/> .
    @prefix site: <http://example.org/site/> .

    comp:A rov:legalName "Niké" ;
           org:hasRegisteredSite site:1234 .
    comp:B rov:legalName "BARCO" .
    ```

    ```sparql { .try-query }
    PREFIX org:  <http://www.w3.org/ns/org#>
    PREFIX comp: <http://example.org/company/>

    ASK { comp:B org:hasRegisteredSite ?site . }
    ```

    <div class="try-result" markdown>

    Answer: false

    </div>

    ```sparql { .try-query }
    PREFIX org:  <http://www.w3.org/ns/org#>
    PREFIX site: <http://example.org/site/>

    DESCRIBE ?org
    WHERE { ?org org:hasRegisteredSite site:1234 . }
    ```

    <div class="try-result" markdown>

    2 triples

    | subject | predicate | object |
    | --- | --- | --- |
    | `comp:A` | `org:hasRegisteredSite` | `site:1234` |
    | `comp:A` | `rov:legalName` | `"Niké"` |

    </div>

## CONSTRUCT { #construct }

`CONSTRUCT` turns query results into new triples.
The template after `CONSTRUCT` is a set of triple patterns, and the triple store fills in the variables for every solution of the `WHERE` block.

The example derives an `rdfs:label` from each legal name.
Typical uses are mapping data from one vocabulary to another, deriving shortcuts over long paths, and extracting a subgraph for export.
In Corporate Memory, a `CONSTRUCT` query in a workflow writes its result into a graph, which makes it a building block for data transformation.

??? example try-sparql "Try it"

    ```turtle { .try-data }
    @prefix rov:  <http://www.w3.org/ns/regorg#> .
    @prefix org:  <http://www.w3.org/ns/org#> .
    @prefix comp: <http://example.org/company/> .
    @prefix site: <http://example.org/site/> .

    comp:A rov:legalName "Niké" ;
           org:hasRegisteredSite site:1234 .
    comp:B rov:legalName "BARCO" .
    ```

    ```sparql { .try-query }
    PREFIX rov:  <http://www.w3.org/ns/regorg#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    CONSTRUCT { ?comp rdfs:label ?name . }
    WHERE     { ?comp rov:legalName ?name . }
    ```

    <div class="try-result" markdown>

    2 triples

    | subject | predicate | object |
    | --- | --- | --- |
    | `comp:B` | `rdfs:label` | `"BARCO"` |
    | `comp:A` | `rdfs:label` | `"Niké"` |

    </div>

## Aggregation and more { #aggregation }

SPARQL 1.1 added the features that make it a complete analysis language:

- **Aggregates** – `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `SAMPLE`, `GROUP_CONCAT` – summarize the rows of each group formed by `GROUP BY`.
  The example counts the products per product manager.
- **Projection of expressions** – `(COUNT(?product) AS ?products)` or `BIND (… AS ?x)` assign a computed value to a new variable.
- **Subqueries** nest a complete `SELECT` inside a pattern.
- **`VALUES`** provides a fixed list of bindings, for example a list of IRIs to look up.
- **Property paths** follow chains and repetitions of properties: `prod:memberOf/rdfs:label` reaches the label of the department, `rdfs:subClassOf*` walks a class hierarchy to any depth.

??? example try-sparql "Try it"

    Data: [product data](data/product-data.ttl){ .try-data }, the graphs of the [exercises](#exercises)

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>

    SELECT ?manager (COUNT(?product) AS ?products)
    WHERE {
      ?product prod:hasProductManager ?manager .
    }
    GROUP BY ?manager
    ORDER BY DESC(?products)
    ```

    <div class="try-result" markdown>

    56 rows, the first 10 shown

    | manager | products |
    | --- | --- |
    | `pi:empl-Wolfgang.Martin%40company.org` | `"28"^^xsd:integer` |
    | `pi:empl-Bert.Blumstein%40company.org` | `"26"^^xsd:integer` |
    | `pi:empl-Franziska.Acker%40company.org` | `"26"^^xsd:integer` |
    | `pi:empl-Gretel.Roth%40company.org` | `"25"^^xsd:integer` |
    | `pi:empl-Manfred.Foth%40company.org` | `"25"^^xsd:integer` |
    | `pi:empl-Berlin.Schulz%40company.org` | `"24"^^xsd:integer` |
    | `pi:empl-Thomas.Mueller%40company.org` | `"24"^^xsd:integer` |
    | `pi:empl-Elisabeth.Harman%40company.org` | `"24"^^xsd:integer` |
    | `pi:empl-Kevin.Feigenbaum%40company.org` | `"24"^^xsd:integer` |
    | `pi:empl-Corinna.Ludwig%40company.org` | `"22"^^xsd:integer` |

    </div>

    A property path reaches the department of the product manager in one step:

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?department (COUNT(DISTINCT ?product) AS ?products)
    WHERE {
      ?product prod:hasProductManager/prod:memberOf/rdfs:label ?department .
    }
    GROUP BY ?department
    ORDER BY DESC(?products)
    ```

    <div class="try-result" markdown>

    6 rows

    | department | products |
    | --- | --- |
    | `"Product Management"` | `"238"^^xsd:integer` |
    | `"Marketing"` | `"183"^^xsd:integer` |
    | `"Data Services"` | `"179"^^xsd:integer` |
    | `"Procurement"` | `"152"^^xsd:integer` |
    | `"Engineering"` | `"125"^^xsd:integer` |
    | `"Production"` | `"83"^^xsd:integer` |

    </div>

## SPARQL Update { #sparql-update }

SPARQL 1.1 Update changes graphs:

- `INSERT DATA { … }` and `DELETE DATA { … }` add or remove the given triples.
- `DELETE { … } INSERT { … } WHERE { … }` computes the changes from a pattern, for example to rename a property throughout a graph.
- `CLEAR GRAPH`, `DROP GRAPH`, `LOAD` and `COPY` work on whole graphs.

`GRAPH <iri> { … }` selects the named graph to change.
In Corporate Memory, every graph is a named graph, and write access is controlled per graph by access conditions.

??? example try-sparql "Try it"

    The store of this box starts empty.
    Run the four steps in order: insert, look, rename, drop.

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    INSERT DATA {
      GRAPH <http://ld.company.org/training/> {
        <http://ld.company.org/prod-instances/empl-Jane.Doe%40company.org>
            a prod:Employee ;
            rdfs:label "Jane Doe" .
      }
    }
    ```

    <div class="try-result" markdown>

    Update done (+2), the store holds 2 triples.

    </div>

    ```sparql { .try-query }
    SELECT ?s ?p ?o
    WHERE {
      GRAPH <http://ld.company.org/training/> { ?s ?p ?o . }
    }
    ```

    <div class="try-result" markdown>

    2 rows

    | s | p | o |
    | --- | --- | --- |
    | `<http://ld.company.org/prod-instances/empl-Jane.Doe%40company.org>` | `rdfs:label` | `"Jane Doe"` |
    | `<http://ld.company.org/prod-instances/empl-Jane.Doe%40company.org>` | `rdf:type` | `<http://ld.company.org/prod-vocab/Employee>` |

    </div>

    ```sparql { .try-query }
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    DELETE { GRAPH ?g { ?s rdfs:label ?label . } }
    INSERT { GRAPH ?g { ?s skos:prefLabel ?label . } }
    WHERE  { GRAPH ?g { ?s rdfs:label ?label . } }
    ```

    <div class="try-result" markdown>

    Update done, the store holds 2 triples.

    </div>

    ```sparql { .try-query }
    DROP GRAPH <http://ld.company.org/training/>
    ```

    <div class="try-result" markdown>

    Update done (-2), the store holds 0 triples.

    </div>

## Exercises { #exercises }

The exercises query the product data of the **Product Data Demo** package, ID `ecc-product-data-project`.
The [sandbox](../../getting-started/with-your-sandbox/index.md) comes with it installed, on another instance it is installed from the [Marketplace](../../distribution/marketplace/index.md).
The package contains the build project *Product Data Integration Demo* and the graphs it generates, among them hardware, services and the organization map, plus the integration graph *Products - Integration* (`http://ld.company.org/prod-inst/`), which imports all of them.

The vocabulary uses the prefix `prod:` for `http://ld.company.org/prod-vocab/`.
Run the queries in the Query module, or with **Run** on this page against a copy of the graphs in [product-data.ttl](data/product-data.ttl).

!!! tip "No inference"

    The data types products as `prod:Hardware` or `prod:Service`, and the vocabulary declares both as subclasses of `prod:Product`.
    The triple store does not infer `prod:Product` from that, so `?product a prod:Product` finds nothing.
    The property path `a/rdfs:subClassOf*` follows the class hierarchy in the query itself, and the solutions below use it wherever a superclass is meant.

??? example try-sparql "1. Find all products"

    Data: [product data](data/product-data.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?product ?label
    WHERE {
      ?product a/rdfs:subClassOf* prod:Product .
      OPTIONAL { ?product rdfs:label ?label . }
    }
    ORDER BY ?label
    ```

    <div class="try-result" markdown>

    1009 rows, the first 10 shown

    | product | label |
    | --- | --- |
    | `pi:hw-A145-1240844` | `"A145-1240844 - Bipolar-junction Coil Compensator Transducer"` |
    | `pi:hw-A166-3766336` | `"A166-3766336 - Aluminum LCD Driver Gauge"` |
    | `pi:hw-A181-1118563` | `"A181-1118563 - Compensator Switch"` |
    | `pi:hw-A225-1988393` | `"A225-1988393 - Field-effect Dipole Gauge"` |
    | `pi:hw-A243-3332548` | `"A243-3332548 - Bipolar-junction Crystal Meter"` |
    | `pi:hw-A315-1730287` | `"A315-1730287 - Network Dipole"` |
    | `pi:hw-A360-3041803` | `"A360-3041803 - Inductor Transformer Warp"` |
    | `pi:hw-A391-9508821` | `"A391-9508821 - Oscillator Compensator"` |
    | `pi:hw-A403-4549719` | `"A403-4549719 - Flow Gauge Transformer"` |
    | `pi:hw-A464-7310986` | `"A464-7310986 - Network Driver"` |

    </div>

    The result has 1009 rows: 1000 hardware products and 9 services.

??? example try-sparql "2. Find hardware products lighter than 10 g"

    Data: [product data](data/product-data.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?product ?label ?weight
    WHERE {
      ?product a prod:Hardware ;
               rdfs:label ?label ;
               prod:weight_g ?weight .
      FILTER (?weight < 10)
    }
    ORDER BY ?weight ?label
    ```

    <div class="try-result" markdown>

    478 rows, the first 10 shown

    | product | label | weight |
    | --- | --- | --- |
    | `pi:hw-A998-9941987` | `"A998-9941987 - Flow Compensator"` | `"1"^^xsd:integer` |
    | `pi:hw-C213-4995667` | `"C213-4995667 - Potentiometer Crystal Encoder"` | `"1"^^xsd:integer` |
    | `pi:hw-C770-9751514` | `"C770-9751514 - Transistor Resonator Breaker"` | `"1"^^xsd:integer` |
    | `pi:hw-D483-7794770` | `"D483-7794770 - Memristor Gauge"` | `"1"^^xsd:integer` |
    | `pi:hw-D516-5106885` | `"D516-5106885 - Driver Rheostat Capacitor"` | `"1"^^xsd:integer` |
    | `pi:hw-D915-4717890` | `"D915-4717890 - Oscillator Switch"` | `"1"^^xsd:integer` |
    | `pi:hw-E405-1045893` | `"E405-1045893 - Polymer Sensor"` | `"1"^^xsd:integer` |
    | `pi:hw-E424-4700158` | `"E424-4700158 - Rheostat Compensator Meter"` | `"1"^^xsd:integer` |
    | `pi:hw-E502-4333702` | `"E502-4333702 - Heisenberg Resistor Gauge Dipole"` | `"1"^^xsd:integer` |
    | `pi:hw-E660-5579477` | `"E660-5579477 - Film Oscillator Transistor Capacitor"` | `"1"^^xsd:integer` |

    </div>

    `prod:weight_g` holds the weight in grams.
    478 of the 1000 hardware products weigh less than 10 g.

??? example try-sparql "3. Find products whose product manager is not in the organization map"

    Data: [product data](data/product-data.ttl){ .try-data }

    Every product in the data has a product manager, so a query for products *without* one returns no rows.
    A more revealing question is whether the product manager is a known employee:

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?item ?label ?manager
    WHERE {
      ?item a/rdfs:subClassOf* prod:Product ;
            rdfs:label ?label ;
            prod:hasProductManager ?manager .
      FILTER NOT EXISTS { ?manager a/rdfs:subClassOf* prod:Employee . }
    }
    ORDER BY ?manager ?label
    ```

    <div class="try-result" markdown>

    49 rows, the first 10 shown

    | item | label | manager |
    | --- | --- | --- |
    | `pi:hw-A509-5571891` | `"A509-5571891 - Multiplexer Inductor"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-A595-2446575` | `"A595-2446575 - Sensor Driver Capacitor"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-C605-1105328` | `"C605-1105328 - Log-periodic Gauge Compensator Meter"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-C799-8367143` | `"C799-8367143 - Coil Strain Meter"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-E267-7496794` | `"E267-7496794 - Crystal Rheostat"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-E395-9906117` | `"E395-9906117 - Flow Inductor Crystal Encoder"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-E952-1325145` | `"E952-1325145 - Driver Gauge"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-H609-2196524` | `"H609-2196524 - Planck Potentiometer Transformer"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-M645-5460777` | `"M645-5460777 - Log-periodic Multiplexer Rheostat"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |
    | `pi:hw-R231-2442628` | `"R231-2442628 - Transformer Transducer"` | `pi:empl-Frau.Irmalinda%E2%80%9A%C3%84%C3%B2.Becker%40company.org` |

    </div>

    49 products refer to 3 product managers that the organization map does not contain.
    Without the property path, managers typed only as `prod:Manager` would show up as well.

??? example try-sparql "4. Find products without a responsible department"

    Data: [product data](data/product-data.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?item ?label
    WHERE {
      ?item a/rdfs:subClassOf* prod:Product ;
            rdfs:label ?label .
      FILTER NOT EXISTS { ?department prod:responsibleFor ?item . }
    }
    ORDER BY ?label
    ```

    <div class="try-result" markdown>

    951 rows, the first 10 shown

    | item | label |
    | --- | --- |
    | `pi:hw-A166-3766336` | `"A166-3766336 - Aluminum LCD Driver Gauge"` |
    | `pi:hw-A181-1118563` | `"A181-1118563 - Compensator Switch"` |
    | `pi:hw-A225-1988393` | `"A225-1988393 - Field-effect Dipole Gauge"` |
    | `pi:hw-A243-3332548` | `"A243-3332548 - Bipolar-junction Crystal Meter"` |
    | `pi:hw-A315-1730287` | `"A315-1730287 - Network Dipole"` |
    | `pi:hw-A360-3041803` | `"A360-3041803 - Inductor Transformer Warp"` |
    | `pi:hw-A391-9508821` | `"A391-9508821 - Oscillator Compensator"` |
    | `pi:hw-A403-4549719` | `"A403-4549719 - Flow Gauge Transformer"` |
    | `pi:hw-A464-7310986` | `"A464-7310986 - Network Driver"` |
    | `pi:hw-A509-5571891` | `"A509-5571891 - Multiplexer Inductor"` |

    </div>

    Departments are responsible for 58 products, so 951 products have no responsible department.

??? example try-sparql "5. Find alternative experts for a product"

    Data: [product data](data/product-data.ttl){ .try-data }

    An employee's `prod:areaOfExpertise` names product categories.
    Employees who share a category with the product manager can take over responsibility:

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?productLabel ?managerLabel
           (GROUP_CONCAT(DISTINCT ?alternativeLabel; separator=", ") AS ?alternatives)
    WHERE {
      VALUES ?product { <http://ld.company.org/prod-instances/hw-N573-1498086> }
      ?product rdfs:label ?productLabel ;
               prod:hasProductManager ?manager .
      ?manager rdfs:label ?managerLabel ;
               prod:areaOfExpertise ?category .
      ?alternative prod:areaOfExpertise ?category ;
                   rdfs:label ?alternativeLabel .
      FILTER (?alternative != ?manager)
    }
    GROUP BY ?productLabel ?managerLabel
    ```

    <div class="try-result" markdown>

    1 row

    | productLabel | managerLabel | alternatives |
    | --- | --- | --- |
    | `"N573-1498086 - Dipole Transformer"` | `"Ratt Hartmann"` | `"Valda Everhart, Siglind Brinkerhoff, Kevin Feigenbaum, Anamchara Foerstner, Xochitl Aue, Frauke Faerber, Wanja Hoffmann, Sabrina Geiger, Minnie Kuehn, Lili Geier, Herr Burgh Eichel, Bert Blumstein, Arnelle Gerber, Arendt Beitel"` |

    </div>

    For the Dipole Transformer, managed by Ratt Hartmann, the query lists 14 colleagues.
    Remove the `VALUES` line to get the alternatives for every product.

??? example try-sparql "6. Count the products per manager and department"

    Data: [product data](data/product-data.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?departmentLabel ?managerLabel (COUNT(DISTINCT ?product) AS ?products)
    WHERE {
      ?product prod:hasProductManager ?manager .
      ?manager rdfs:label ?managerLabel ;
               prod:memberOf ?department .
      ?department rdfs:label ?departmentLabel .
    }
    GROUP BY ?departmentLabel ?managerLabel
    ORDER BY ?departmentLabel DESC(?products)
    ```

    <div class="try-result" markdown>

    53 rows, the first 10 shown

    | departmentLabel | managerLabel | products |
    | --- | --- | --- |
    | `"Data Services"` | `"Wolfgang Martin"` | `"28"^^xsd:integer` |
    | `"Data Services"` | `"Gretel Roth"` | `"25"^^xsd:integer` |
    | `"Data Services"` | `"Nadia Schubert"` | `"20"^^xsd:integer` |
    | `"Data Services"` | `"Elena Herzog"` | `"18"^^xsd:integer` |
    | `"Data Services"` | `"Anamchara Foerstner"` | `"17"^^xsd:integer` |
    | `"Data Services"` | `"Ratt Hartmann"` | `"16"^^xsd:integer` |
    | `"Data Services"` | `"Arnelle Gerber"` | `"15"^^xsd:integer` |
    | `"Data Services"` | `"Siglind Brinkerhoff"` | `"15"^^xsd:integer` |
    | `"Data Services"` | `"Sylvester Brant"` | `"13"^^xsd:integer` |
    | `"Data Services"` | `"Rebecca Hall"` | `"12"^^xsd:integer` |

    </div>

    Save this query in the query catalog.
    The charts and custom API exercises reuse it.

??? example try-sparql "7. Add an employee"

    Data: [product data](data/product-data.ttl){ .try-data }

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    INSERT DATA {
      GRAPH <http://ld.company.org/training/> {
        <http://ld.company.org/prod-instances/empl-Jane.Doe%40company.org> a prod:Employee ;
            rdfs:label "Jane Doe" ;
            prod:email "Jane.Doe@company.org" ;
            prod:memberOf <http://ld.company.org/prod-instances/dept-73191> .
      }
    }
    ```

    <div class="try-result" markdown>

    Update done (+4), the store holds 23601 triples.

    </div>

    Replace the name and email address with personal values.
    The statements go into a graph of their own, which leaves the package data untouched and is removed again with `DROP GRAPH <http://ld.company.org/training/>`.
    Because the new employee links to an existing department, the employee appears in the department's data in queries over all graphs:

    ```sparql { .try-query }
    PREFIX prod: <http://ld.company.org/prod-vocab/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?member ?label
    WHERE {
      ?member prod:memberOf <http://ld.company.org/prod-instances/dept-73191> ;
              rdfs:label ?label .
    }
    ORDER BY ?label
    ```

    <div class="try-result" markdown>

    7 rows

    | member | label |
    | --- | --- |
    | `pi:empl-Corinna.Ludwig%40company.org` | `"Corinna Ludwig"` |
    | `pi:empl-Herr.Haan.Bader%40company.org` | `"Herr Haan Bader"` |
    | `pi:empl-Jane.Doe%40company.org` | `"Jane Doe"` |
    | `pi:empl-Karch.Moeller%40company.org` | `"Karch Moeller"` |
    | `pi:empl-Karen.Brant%40company.org` | `"Karen Brant"` |
    | `pi:empl-Manfred.Foth%40company.org` | `"Manfred Foth"` |
    | `pi:empl-Thomas.Mueller%40company.org` | `"Thomas Mueller"` |

    </div>

    ```sparql { .try-query }
    DROP GRAPH <http://ld.company.org/training/>
    ```

    <div class="try-result" markdown>

    Update done (-4), the store holds 23597 triples.

    </div>

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
