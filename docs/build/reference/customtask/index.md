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

|                                                    Name |                                                Category                                                 | Description              |
|--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:-------------------------|
 | [Add project files](addProjectFiles.md) | None | Adds file resources to the project that are piped into the input port. |
 | [Cancel Workflow](CancelWorkflow.md) | None | Cancels a workflow if a specified condition is fulfilled. |
 | [Combine CSV files](combine-csv.md) | None | Combine CSV files with the same structure to one dataset. |
 | [Concatenate to file](ConcatenateToFile.md) | None | Concatenates values into a file. |
 | [Create Embeddings](cmem_plugin_llm-CreateEmbeddings.md) | None | Fetch and output LLM created embeddings from input entities. |
 | [Create/Update Salesforce Objects](cmem_plugin_salesforce-workflow-operations-SobjectCreate.md) | None | Manipulate data in your organization’s Salesforce account. |
 | [Delete project files](deleteProjectFiles.md) | None | Removes file resources from the project based on a regular expression. |
 | [Distinct by](DistinctBy.md) | None | Removes duplicated entities based on a user-defined path. Note that this operator does not retain the order of the entities. |
 | [Download file](downloadFile.md) | None | Downloads a file from a given URL. |
 | [Download Nextcloud files](cmem_plugin_nextcloud-Download.md) | None | Download files from a given Nextcloud instance. |
 | [Download Office 365 Files](cmem_plugin_office365-Download.md) | None | Download files from Microsoft OneDrive or Sites |
 | [Download SSH files](cmem_plugin_ssh-Download.md) | None | Download files from a given SSH instance |
 | [Evaluate template](Template.md) | None | Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel. |
 | [Execute commands via SSH](cmem_plugin_ssh-Execute.md) | None | Execute commands on a given SSH instance. |
 | [Execute Instructions](cmem_plugin_llm-ExecuteInstructions.md) | None | Send instructions (prompt) to an LLM and process the result. |
 | [Execute REST requests](eccencaRestOperator.md) | None | REST operator that fetches and optionally merges data from a REST endpoint. It supports executing multiple requests either via input entities that each overwrite config parameters or via paging. If you only need to download a single file, the "Download file" operator might be the better option. Most features are currently only supported for JSON REST APIs. From multiple requests the REST operator can produce a merged JSON result, i.e. for JSON it will concatenate all results in a JSON array. Alternatively multiple results can be written directly to file (of a JSON dataset), either as a merged JSON file or one file per request inside a ZIP file. By default the output of this operator is an entity with a single property 'result', which is the (concatenated) JSON string. |
 | [Execute Spark function](SparkFunction.md) | None | Applies a specified Scala function to a specified field. |
 | [Extract from PDF files](cmem_plugin_pdf_extract-pdf_extract-PdfExtract.md) | None | Extract text and tables from PDF files |
 | [Generate base36 IRDIs](cmem_plugin_irdi-workflow-irdi_plugin-IrdiPlugin.md) | None | Create unique ECLASS IRDIs. |
 | [Generate SHACL shapes from data](cmem_plugin_shapes-plugin_shapes-ShapesPlugin.md) | None | Generate SHACL node and property shapes from a data graph |
 | [Get project files](getProjectFiles.md) | None | Get file resources from the project. |
 | [GraphQL query](cmem_plugin_graphql-workflow-graphql-GraphQLPlugin.md) | None | Executes a custom GraphQL query to a GraphQL endpoint and saves result to a JSON dataset. |
 | [Join tables](Merge.md) | None | Joins a set of inputs into a single table. Expects a list of entity tables and links. All entity tables are joined into the first entity table using the provided links. |
 | [jq](cmem-plugin-jq-workflow.md) | None | Process a JSON document with a jq filter / program. |
 | [JQL query](cmem_plugin_jira-JqlQuery.md) | None | Search and retrieve JIRA issues. |
 | [Kafka Consumer (Receive Messages)](cmem_plugin_kafka-ReceiveMessages.md) | None | Reads messages from a Kafka topic and saves it to a messages dataset (Consumer). |
 | [Kafka Producer (Send Messages)](cmem_plugin_kafka-SendMessages.md) | None | Reads a messages dataset and sends records to a Kafka topic (Producer). |
 | [List Nextcloud files](cmem_plugin_nextcloud-List.md) | None | List directories and files from a given Nextcloud folder. |
 | [List Office 365 Files](cmem_plugin_office365-List.md) | None | List files from OneDrive or Sites |
 | [List project files](cmem_plugin_project_resources-List.md) | None | List file resources from the project. |
 | [List SSH files](cmem_plugin_ssh-List.md) | None | List files from a given SSH instance. |
 | [Merge tables](MultiTableMerge.md) | None | Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links. |
 | [Normalize units of measurement](ucumNormalizationTask.md) | None | Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation. |
 | [OAuth2 Authentication](cmem_plugin_auth-workflow-auth-OAuth2.md) | None | Provide an OAuth2 access token for other tasks (via config port). |
 | [Office 365 Upload Files](cmem_plugin_office365-Upload.md) | None | Upload files to OneDrive or a site Sharepoint |
 | [Parse JSON](JsonParserOperator.md) | None | Parses an incoming entity as a JSON dataset. Typically, it is used before a transformation task. Takes exactly one input of which only the first entity is processed. |
 | [Parse XML](XmlParserOperator.md) | None | Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities. |
 | [Parse YAML](cmem_plugin_yaml-parse.md) | None | Parses files, source code or input values as YAML documents. |
 | [Pivot](Pivot.md) | None | The pivot operator takes data in separate rows, aggregates it and converts it into columns. |
 | [Request RDF triples](tripleRequestOperator.md) | None | A task that requests all triples from an RDF dataset. |
 | [Scheduler](Scheduler.md) | None | Executes a workflow at specified intervals. |
 | [Search addresses](SearchAddresses.md) | None | Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF. |
 | [Search Vector Embeddings](cmem_plugin_pgvector-Search.md) | None | Search for top-k metadata stored in Postgres Vector Store (PGVector). |
 | [Send eMail](SendEMail.md) | None | Sends an eMail using an SMTP server. If connected to a dataset that is based on a file in a workflow, it will send that file whenever the workflow is executed It can be used to send the result of a workflow via Mail. |
 | [Send Mattermost messages](cmem_plugin_mattermost.md) | None | Send messages to Mattermost channels and/or users. |
 | [Set or Overwrite parameters](cmem_plugin_parameters-ParametersPlugin.md) | None | Connect this task to a config port of another task in order to set or overwrite the parameter values of this task. |
 | [SHACL validation with pySHACL](shacl-pyshacl.md) | None | Performs SHACL validation with pySHACL. |
 | [SOQL query (Salesforce)](cmem_plugin_salesforce-SoqlQuery.md) | None | Executes a custom Salesforce Object Query (SOQL) to return sets of data your organization’s Salesforce account. |
 | [SPARQL Construct query](sparqlCopyOperator.md) | None | A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable. |
 | [SPARQL Select query](sparqlSelectOperator.md) | None | A task that executes a SPARQL Select query on a SPARQL enabled data source and outputs the SPARQL result. If the SPARQL source is defined on a specific graph, a FROM clause will be added to the query at execution time, except when there already exists a GRAPH or FROM clause in the query. FROM NAMED clauses are not injected. |
 | [SPARQL Update query](sparqlUpdateOperator.md) | None | A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written. In contrast to the SPARQL select operator, no FROM clause gets injected into the query. |
 | [Split file](cmem_plugin_splitfile-plugin_splitfile-SplitFilePlugin.md) | None | Split a file into multiple parts with a specified size. |
 | [SQL query](CustomSQLExecution.md) | None | Executes a custom SQL query on the first input dataset and returns the result as its output. |
 | [Start Workflow per Entity](cmem_plugin_loopwf-task-StartWorkflow.md) | None | Loop over the output of a task and start a sub-workflow for each entity. |
 | [Store Vector Embeddings](cmem_plugin_pgvector-Store.md) | None | Store embeddings into Postgres Vector Store (PGVector). |
 | [Unpivot](Unpivot.md) | None | Given a list of table columns, transforms those columns into attribute-value pairs. |
 | [Update SemSpect](cmem_plugin_semspect-task-Update.md) | None | Tell SemSpect to prepare a Knowledge Graph for visualization. |
 | [Upload File to Knowledge Graph](eccencaDataPlatformGraphStoreFileUploadOperator.md) | None | Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset. |
 | [Upload files to Nextcloud](cmem_plugin_nextcloud-Upload.md) | None | Upload files to a given Nextcloud instance. |
 | [Upload local files](cmem_plugin_project_resources-UploadLocalFiles.md) | None | Replace a file dataset resource with a local file or upload multiple local files to a project. |
 | [Upload SSH files](cmem_plugin_ssh-Upload.md) | None | Upload files to a given SSH instance. |
 | [Validate Entities](cmem_plugin_validation-validate-ValidateEntities.md) | None | Use a JSON schema to validate entities or a JSON dataset. |
 | [Validate Knowledge Graph](cmem_plugin_validation-validate-ValidateGraph.md) | None | Use SHACL shapes to validate resources in a Knowledge Graph. |
 | [Validate XML](validateXsdOperator.md) | None | Validates an XML dataset against a provided XML schema (XSD) file. Any errors are written to the output. Can be used in conjunction with the `Cancel Workflow` operator in order to stop the workflow if errors have been found. |
 | [XSLT](xsltOperator.md) | None | A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource. |
