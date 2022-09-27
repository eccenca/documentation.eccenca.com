---
tags:
    - API
---
# DataPlatform APIs

## Introduction

eccenca DataPlatform APIs can be used to import, export, query and extract information from graphs as well as to check access conditions.

This section describes common characteristics and features of all provided APIs.

### Media Types

The default [media type](https://en.wikipedia.org/wiki/Media_type) of most responses is `application/json`. Other possible response media types can be reached by changing the Accept header of the request. Alternatively, the desired response media type can be expressed in the request URI.

Possible values of this HTTP header field are API dependent and listed as part of the specific HTTP method.

Dependent on the specific API, eccenca DataPlatform works with the following application media types which correspond to the following specification documents:

| Media Type                                                        | Specification Document                                                                                                                                                  |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| application/x-www-form-urlencoded                                 | [HTML 4.01 Specification, Forms](https://www.w3.org/TR/html401/interact/forms.html)                                                                                     |
| application/json                                                  | [The JavaScript Object Notation (JSON) Data Interchange Format](https://tools.ietf.org/html/rfc8259)                                                                    |
| application/ld+json                                               | [JSON-LD 1.0](https://www.w3.org/TR/json-ld/)                                                                                                                           |
| text/turtle                                                       | [RDF 1.1 Turtle - Terse RDF Triple Language](https://www.w3.org/TR/turtle/)                                                                                             |
| application/n-triples                                             | [RDF 1.1 N-Triples - A line-based syntax for an RDF graph](https://www.w3.org/TR/n-triples/)                                                                            |
| application/rdf+xml                                               | [RDF 1.1 XML Syntax](http://www.w3.org/TR/rdf-syntax-grammar/)                                                                                                          |
| application/n-quads                                               | [RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/)                                                                                                                       |
| application/trig                                                  | [RDF 1.1 TriG](https://www.w3.org/TR/trig/)                                                                                                                             |
| application/sparql-query                                          | [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/#mediaType)                                                                                            |
| application/sparql-update                                         | [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/#mediaType)                                                                                                   |
| application/sparql-results+json                                   | [SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json)                                                                                     |
| application/sparql-results+xml                                    | [SPARQL Query Results XML Format (Second Edition)](https://www.w3.org/TR/rdf-sparql-XMLres)                                                                             |
| text/csv                                                          | [SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql11-results-csv-tsv/)                                                                         |
| text/tab-separated-values                                         | [SPARQL 1.1 Query Results CSV and TSV Formats](https://www.w3.org/TR/sparql11-results-csv-tsv/)                                                                         |
| application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | [Microsoft Office Excel (.xlsx) format](https://blogs.msdn.microsoft.com/vsofficedeveloper/2008/05/08/office-2007-file-format-mime-types-for-http-content-streaming-2/) |
| application/problem+json                                          | [Problem Details for HTTP APIs](https://tools.ietf.org/html/rfc7807)                                                                                                    |

#### Media type request by URI

The desired response media type can be requested by adding a format query parameter. The parameter value is interpreted as a media type abbreviation that is expanded to a proper media type string. eccenca DataPlatform maps the following abbreviations to media types it supports:

| Abbreviation | Media Type                      |
| ------------ | ------------------------------- |
| rdf          | application/rdf+xml             |
| ttl          | text/turtle                     |
| jsonld       | application/ld+json             |
| nt           | application/n-triples           |
| trig         | application/trig                |
| nq           | application/n-quads             |
| srj          | application/sparql-results+json |
| srx          | application/sparql-results+xml  |
| csv          | text/csv                        |
| tsv          | text/tab-separated-values       |

Thus, for example, a request to `/proxy/default/graph` with the Accept header value `text/turtle` and a request to `/proxy/default/graph?format=ttl` express the same intent for the media type of the response.

If both this format query parameter and an Accept header is present in a request, the parameter value takes precedence.

Usage of media type request by URI can be useful to create browser links that will express an intent for the media type of the response.

## Security Schemes

The default security scheme is OAuth 2.0.
However, this can be changed in the configuration.

## SPARQL result set streaming

The SPARQL proxy pipes the results of SPARQL queries directly from the underlying data endpoint to the request client. This however does not always apply for CONSTRUCT queries.

The result of a CONSTRUCT query is a set of statements. RDF graph serialization formats tend to group the information for compactness - e.g. in [Turtle](https://www.w3.org/TR/turtle/), all statements for a subject are written together - avoiding subject and subject-predicate repetition, for which it is necessary to have the complete result set at disposal.

Therefore, before sending the result to the request client, the complete result is loaded and then serialized. This creates a potential danger whenever a large result set is build and could lead to overload of the server.

There is however one serialization format (the [N-Triples format](https://www.w3.org/TR/n-triples/)) which is streaming friendly and that should always be used whenever large result sets are expected.

## SPARQL default graph & RDF dataset

### Default graph

The definition of the RDF dataset of a query in the [SPARQL 1.1 specification](https://www.w3.org/TR/sparql11-query/#rdfDataset) leads to problems regarding the default graph of a SPARQL service. On one hand it is defined that:

> A SPARQL query is executed against an RDF dataset which represents a collection of graphs. An RDF dataset comprises one graph, the default graph, which does not have a name, and zero or more named graphs, where each named graph is identified by an IRI.

Furthermore, it says:

> A SPARQL query may specify the dataset to be used for matching by using the FROM clause and the FROM NAMED clause to describe the RDF dataset. If a query provides such a dataset description, then it is used in place of any dataset that the query service would use if no dataset description is provided in a query. The RDF dataset may also be specified in a SPARQL protocol request, in which case the protocol description overrides any description in the query itself. A query service may refuse a query request if the dataset description is not acceptable to the service.
>
> The FROM and FROM NAMED keywords allow a query to specify an RDF dataset by reference; they indicate that the dataset should include graphs that are obtained from representations of the resources identified by the given IRIs (i.e. the absolute form of the given IRI references). The dataset resulting from a number of FROM and FROM NAMED clauses is:
>
> - a default graph consisting of the RDF merge of the graphs referred to in the FROM clauses, and
> - a set of (IRI, graph) pairs, one from each FROM NAMED clause.
>
> If there is no FROM clause, but there is one or more FROM NAMED clauses, then the dataset includes an empty graph for the default graph.

That means the default graph of a SPARQL service cannot be explicitly referenced in the RDF dataset of a SPARQL query using FROM / FROM NAMED.

For this reason, DataPlatform **does not allow the manipulation of the service's default graph.**

To enforce this policy, the following restriction applies to incoming [SPARQL 1.1](https://www.w3.org/TR/sparql11-update/) Update queries:

- Update queries (INSERT DATA, DELETE DATA and DELETE/INSERT) targeted against the service's default graph will not be accepted by returning an HTTP 400 Bad Request status code.

### Default RDF dataset

The interpretation of the RDF dataset of a query differs between various SPARQL service implementations (as shown [here](http://depressiverobot.com/2015/07/29/sparql-datasets.html)).

In the case a query declares no RDF dataset, DataPlatform uses the following default RDF dataset declaration to provide a uniform behavior for all supported SPARQL services:

- The default graph is the union ([RDF Merge graph](https://www.w3.org/TR/sparql11-query/#sparqlDataset)) of all named graphs the user is allowed to access.
- The set of named graphs contains all named graphs the user is allowed to access.

## (Open) API Reference

The latest Open API specification:
<!-- swagger collection -->
<swagger-ui src="https://releases.eccenca.com/OpenAPI/eccenca-DataPlatform-OpenAPI-Reference-v22.1.json"/>

> Alternatively, you can (re)view it [redoc web UI](https://redocly.github.io/redoc/?url=https://releases.eccenca.com/OpenAPI/eccenca-DataPlatform-OpenAPI-Reference-v22.1.json)
