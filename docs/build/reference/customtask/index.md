---
title: "Custom Workflow Tasks"
icon: octicons/cross-reference-24
tags:
    - Build
    - Reference
---
# Custom Workflow Tasks
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

A custom workflow task is an operator that can be used in a workflow.

**:octicons-people-24: Intended audience:** Linked Data Experts and Domain Experts

|         Name | Description              |
|-------------:|:-------------------------|
 | [Add project files](addProjectFiles.md) | Adds file resources to the project that are piped into the input port. |
 | [Cancel Workflow](CancelWorkflow.md) | Cancels a workflow if a specified condition is fulfilled. A typical use case for this operator is to cancel the workflow execution if the input data is empty. |
 | [Concatenate to file](ConcatenateToFile.md) | Concatenates values into a file. |
 | [Delete project files](deleteProjectFiles.md) | Removes file resources from the project based on a regular expression. |
 | [Distinct by](DistinctBy.md) | Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities. |
 | [Download file](downloadFile.md) | Downloads a file from a given URL. |
 | [Evaluate template](Template.md) | Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel. |
 | [Execute REST requests](eccencaRestOperator.md) | REST operator that fetches and optionally merges data from a REST endpoint. It supports executing multiple requests either via input entities that each overwrite config parameters or via paging. If you only need to download a single file, the "Download file" operator might be the better option. Most features are currently only supported for JSON REST APIs. From multiple requests the REST operator can produce a merged JSON result, i.e. for JSON it will concatenate all results in a JSON array. Alternatively multiple results can be written directly to file (of a JSON dataset), either as a merged JSON file or one file per request inside a ZIP file. By default the output of this operator is an entity with a single property 'result', which is the (concatenated) JSON string. |
 | [Execute Spark function](SparkFunction.md) | Applies a specified Scala function to a specified field. |
 | [Get project files](getProjectFiles.md) | Get file resources from the project. |
 | [Join tables](Merge.md) | Joins a set of inputs into a single table. Expects a list of entity tables and links. All entity tables are joined into the first entity table using the provided links. |
 | [Merge tables](MultiTableMerge.md) | Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links. |
 | [Normalize units of measurement](ucumNormalizationTask.md) | Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation. |
 | [Parse JSON](JsonParserOperator.md) | Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed. |
 | [Parse XML](XmlParserOperator.md) | Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities. |
 | [Pivot](Pivot.md) | The pivot operator takes data in separate rows, aggregates it and converts it into columns. |
 | [Request RDF triples](tripleRequestOperator.md) | A task that requests all triples from an RDF dataset. |
 | [Scheduler](Scheduler.md) | Executes a workflow at specified intervals. |
 | [Search addresses](SearchAddresses.md) | Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF. |
 | [Send email](SendEMail.md) | Sends an email using an SMTP server. |
 | [SPARQL Construct query](sparqlCopyOperator.md) | A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable. |
 | [SPARQL Select query](sparqlSelectOperator.md) | A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected. |
 | [SPARQL Update query](sparqlUpdateOperator.md) | A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written. In contrast to the SPARQL select operator, no FROM clause gets injected into the query. |
 | [SQL query](CustomSQLExecution.md) | Executes a custom SQL query on the first input dataset and returns the result as its output. |
 | [Unpivot](Unpivot.md) | Given a list of table columns, transforms those columns into attribute-value pairs. |
 | [Upload File to Knowledge Graph](eccencaDataPlatformGraphStoreFileUploadOperator.md) | Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset. |
 | [Validate XML](validateXsdOperator.md) | Validates an XML dataset against a provided XML schema (XSD) file. Any errors are written to the output. Can be used in conjunction with the `Cancel Workflow` operator in order to stop the workflow if errors have been found. |
 | [XSLT](xsltOperator.md) | A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource. |
