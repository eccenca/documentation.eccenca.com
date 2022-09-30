# Statement Annotations

## Introduction
Statement Annotations provide a way to express knowledge about statements. Typical use cases for Statement Annotations include:

-   the temporal validity of information,
-   the origin of information, or
-   just a way to annotate a specific statement with a human readable comment.

## Usage

If enabled on a specific type of statement or type of resource, you see a Statement Annotation text bubble beside every annotatable statement:

![](https://documentation.eccenca.com/files/latest/15111467/15111513/1/1660790841511/statementannotationoveriew.png)

This bubble has different statuses:

-   A **empty text bubble** indicates, that there is no annotation on the statement, but the annotation feature is enabled for this statement.
-   A **filled text bubble** indicates, that there is at least one annotation on the statement.
-   **No bubble** indicates, that the annotation feature is NOT enabled on this type of statement.

Clicking on one of the flags opens the Statement Annotation dialog for this specific statement:

![](https://documentation.eccenca.com/files/latest/15111467/15111516/1/1660791382334/createstatementannotations.png)

In the Statement Annotation dialog, you can select the Statement Annotation Template and click Create.

![](https://documentation.eccenca.com/files/latest/15111467/15111517/1/1660793124265/statementedit.png)

Setup

In order to have a working Statement Annotation setup, the following steps need to be done:

1

**Create a Statement Annotation Graph**

Create a new Graph, edit its metadata and change the type to Statement Annotation Graph.

![](https://documentation.eccenca.com/files/latest/15111467/15111503/1/1660540483533/statementannotation.png)

2

**Setup and import the Statement Annotation Graph in your data graph**

In your data graph, where the resources exist which you want to annotate, import the Statement Annotation Graph and select it as an Annotation Graph.

![](https://documentation.eccenca.com/files/latest/15111467/15111519/1/1660850424332/annotations.png)

3

**Create a shaped form which will be used to annotate statements\
**

In your Shape Catalog, select a Node Shape (or create one) which you want to use for statement annotations, and Enable Statement Annotation to true.

![](https://documentation.eccenca.com/files/latest/15111467/15111520/1/1660850653440/setannotations.png)

4

**Allow statement annotations in your shaped forms on specific Classes or Properties**

Finally, select the Node Shape or Property Shape from your Shape Catalog, and enable annotations by setting the Enable option in the Statement Annotations group to true.

![](https://documentation.eccenca.com/files/latest/15111467/15111520/1/1660850653440/setannotations.png)

This will enable the feature on the statements of all resources shown with this Node Shape or on all statements shown with this Property Shape.

## Technical Background

From the technical point of view, the Statement Annotation feature uses RDF Reification to annotate Statements (Triples) with additional background information. Statement resources can be annotated with custom Annotation Resources. These Annotation Resources are based on specific Shapes which are enabled as Statement Annotation shapes. Reification Resources as well as Annotation Resources are managed in a Statement Annotation Graph, which need to be configured on a Graph as well as imported to this Graph. The following illustration depicts this schema with boxes and arrows:

![](https://documentation.eccenca.com/files/latest/15111467/15111475/1/1656609203458/20-10-StatementAnnotationSchema.png)

Some notes on this:

-   There is one Statement Reification Resource per Statement Annotation.
-   Removing the Statement Annotation also removes the Statement Reification Resource.
-   All annotation triples (8 triples in the image) are created in the Statement Annotation Graph, so Step 2 of the setup procedure is important.

### Querying Statement Annotations

In order to automate access to Statement Annotations, you can query them with SPARQL e.g. via [cmemc](https://documentation.eccenca.com/latest/automate/cmemc-command-line-interface) or the API endpoint.

Here is a query example to start with:

``` s
# Request SPO of all Statement Annotations which annotate a triple of my ResourceIRI (parameter)

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT DISTINCT ?StatementAnnotationGraph ?AnnotationResource ?p ?o
WHERE {
  GRAPH ?StatementAnnotationGraph {
    ?StatementResource a rdf:Statement .
    ?StatementResource rdf:subject|rdf:predicate|rdf:object <{{ResourceIRI}}> .
    ?StatementResource rdf:value ?AnnotationResource .
    ?AnnotationResource ?p ?o
  }
}
```