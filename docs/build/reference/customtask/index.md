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
 | [Combine CSV files](combine-csv.md) | Combine CSV files with the same structure to one dataset. |
 | [Concatenate to file](ConcatenateToFile.md) | Concatenates values into a file. |
 | [Create Embeddings](cmem_plugin_llm-CreateEmbeddings.md) | Fetch and output LLM created embeddings from input entities. |
 | [Create/Update Salesforce Objects](cmem_plugin_salesforce-workflow-operations-SobjectCreate.md) | Manipulate data in your organization's Salesforce account. |
 | [Delete project files](deleteProjectFiles.md) | Removes file resources from the project based on a regular expression. |
 | [Distinct by](DistinctBy.md) | Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities. |
 | [Download file](downloadFile.md) | Downloads a file from a given URL. |
 | [Download Nextcloud files](cmem_plugin_nextcloud-Download.md) | Download files from a given Nextcloud instance. |
 | [Download Office 365 Files](cmem_plugin_office365-Download.md) | Download files from Microsoft OneDrive or Sites |
 | [Download SSH files](cmem_plugin_ssh-Download.md) | Download files from a given SSH instance |
 | [Evaluate template](Template.md) | Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel. |
 | [Execute a command in a kubernetes pod](cmem_plugin_kubernetes-Execute.md) | Connect to a cluster, execute a command and gather the output. |
 | [Execute commands via SSH](cmem_plugin_ssh-Execute.md) | Execute commands on a given SSH instance. |
 | [Execute Instructions](cmem_plugin_llm-ExecuteInstructions.md) | Send instructions (prompt) to an LLM and process the result. |
 | [Execute REST requests](eccencaRestOperator.md) | REST operator that fetches and optionally merges data from a REST endpoint. It supports executing multiple requests either via input entities that each overwrite config parameters or via paging. If you only need to download a single file, the "Download file" operator might be the better option. Most features are currently only supported for JSON REST APIs. From multiple requests the REST operator can produce a merged JSON result, i.e. for JSON it will concatenate all results in a JSON array. Alternatively multiple results can be written directly to file (of a JSON dataset), either as a merged JSON file or one file per request inside a ZIP file. By default the output of this operator is an entity with a single property 'result', which is the (concatenated) JSON string. |
 | [Execute Spark function](SparkFunction.md) | Applies a specified Scala function to a specified field. |
 | [Extract from PDF files](cmem_plugin_pdf_extract-pdf_extract-PdfExtract.md) | Extract text and tables from PDF files |
 | [Generate base36 IRDIs](cmem_plugin_irdi-workflow-irdi_plugin-IrdiPlugin.md) | Create unique ECLASS IRDIs. |
 | [Generate SHACL shapes from data](cmem_plugin_shapes-plugin_shapes-ShapesPlugin.md) | Generate SHACL node and property shapes from a data graph |
 | [Get project files](getProjectFiles.md) | Get file resources from the project. |
 | [Get workflow report](cmem_plugin_wfreports_get_report.md) | Output the last report of a workflow as a JSON file. |
 | [GraphQL query](cmem_plugin_graphql-workflow-graphql-GraphQLPlugin.md) | Executes a custom GraphQL query to a GraphQL endpoint and saves result to a JSON dataset. |
 | [Join tables](Merge.md) | Joins a set of inputs into a single table. Expects a list of entity tables and links. All entity tables are joined into the first entity table using the provided links. |
 | [jq](cmem-plugin-jq-workflow.md) | Process a JSON document with a jq filter / program. |
 | [JQL query](cmem_plugin_jira-JqlQuery.md) | Search and retrieve JIRA issues. |
 | [Kafka Consumer (Receive Messages)](cmem_plugin_kafka-ReceiveMessages.md) | Reads messages from a Kafka topic and saves it to a messages dataset (Consumer). |
 | [Kafka Producer (Send Messages)](cmem_plugin_kafka-SendMessages.md) | Reads a messages dataset and sends records to a Kafka topic (Producer). |
 | [List Nextcloud files](cmem_plugin_nextcloud-List.md) | List directories and files from a given Nextcloud folder. |
 | [List Office 365 Files](cmem_plugin_office365-List.md) | List files from OneDrive or Sites |
 | [List project files](cmem_plugin_project_resources-List.md) | List file resources from the project. |
 | [List SSH files](cmem_plugin_ssh-List.md) | List files from a given SSH instance. |
 | [Merge tables](MultiTableMerge.md) | Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links. |
 | [Normalize units of measurement](ucumNormalizationTask.md) | Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation. |
 | [OAuth2 Authentication](cmem_plugin_auth-workflow-auth-OAuth2.md) | Provide an OAuth2 access token for other tasks (via config port). |
 | [Office 365 Upload Files](cmem_plugin_office365-Upload.md) | Upload files to OneDrive or a site Sharepoint |
 | [Parse JSON](JsonParserOperator.md) | Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed. |
 | [Parse XML](XmlParserOperator.md) | Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities. |
 | [Parse YAML](cmem_plugin_yaml-parse.md) | Parses files, source code or input values as YAML documents. |
 | [Pivot](Pivot.md) | The pivot operator takes data in separate rows, aggregates it and converts it into columns. |
 | [Request RDF triples](tripleRequestOperator.md) | A task that requests all triples from an RDF dataset. |
 | [Scheduler](Scheduler.md) | Executes a workflow at specified intervals. |
 | [Search addresses](SearchAddresses.md) | Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF. |
 | [Search Vector Embeddings](cmem_plugin_pgvector-Search.md) | Search for top-k metadata stored in Postgres Vector Store (PGVector). |
 | [Send email](SendEMail.md) | Sends an email using an SMTP server. |
 | [Send Mattermost messages](cmem_plugin_mattermost.md) | Send messages to Mattermost channels and/or users. |
 | [Set or Overwrite parameters](cmem_plugin_parameters-ParametersPlugin.md) | Connect this task to a config port of another task in order to set or overwrite the parameter values of this task. |
 | [Set parameters](setParameters.md) | Set and overwrite parameters of a task. |
 | [SHACL validation with pySHACL](shacl-pyshacl.md) | Performs SHACL validation with pySHACL. |
 | [SOQL query (Salesforce)](cmem_plugin_salesforce-SoqlQuery.md) | Executes a custom Salesforce Object Query (SOQL) to return sets of data your organization's Salesforce account. |
 | [Spark SQL query](CustomSQLExecution.md) | Executes a custom SQL query on the first input Spark dataframe and returns the result as its output. |
 | [SPARQL Construct query](sparqlCopyOperator.md) | A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable. |
 | [SPARQL Select query](sparqlSelectOperator.md) | A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected. |
 | [SPARQL Update query](sparqlUpdateOperator.md) | A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written. |
 | [Split file](cmem_plugin_splitfile-plugin_splitfile-SplitFilePlugin.md) | Split a file into multiple parts with a specified size. |
 | [SQL Update query](sqlUpdateQueryOperator.md) | A task that outputs SQL queries. The output of this operator should be connected to a remote SQL endpoint on which queries should be executed. |
 | [Start Workflow per Entity](cmem_plugin_loopwf-task-StartWorkflow.md) | Loop over the output of a task and start a sub-workflow for each entity. |
 | [Store Vector Embeddings](cmem_plugin_pgvector-Store.md) | Store embeddings into Postgres Vector Store (PGVector). |
 | [Unpivot](Unpivot.md) | Given a list of table columns, transforms those columns into attribute-value pairs. |
 | [Update Graph Insights Snapshots](cmem_plugin_graph_insights-Update.md) | Update one or more snapshots, optionally selected by affected graph. |
 | [Upload File to Knowledge Graph](eccencaDataPlatformGraphStoreFileUploadOperator.md) | Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset. |
 | [Upload files to Nextcloud](cmem_plugin_nextcloud-Upload.md) | Upload files to a given Nextcloud instance. |
 | [Upload local files](cmem_plugin_project_resources-UploadLocalFiles.md) | Replace a file dataset resource with a local file or upload multiple local files to a project. |
 | [Upload SSH files](cmem_plugin_ssh-Upload.md) | Upload files to a given SSH instance. |
 | [Validate Entities](cmem_plugin_validation-validate-ValidateEntities.md) | Use a JSON schema to validate entities or a JSON dataset. |
 | [Validate Knowledge Graph](cmem_plugin_validation-validate-ValidateGraph.md) | Use SHACL shapes to validate resources in a Knowledge Graph. |
 | [Validate XML](validateXsdOperator.md) | Validates an XML dataset against a provided XML schema (XSD) file. Any errors are written to the output. Can be used in conjunction with the `Cancel Workflow` operator in order to stop the workflow if errors have been found. |
 | [XSLT](xsltOperator.md) | A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource. |
