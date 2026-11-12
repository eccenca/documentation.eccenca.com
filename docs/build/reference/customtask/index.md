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
 | [Build Packages](cmem_plugin_packages-BuildPackages.md) | Build package archives from a CPA manifest, using graphs, projects and files from this instance. |
 | [Bump Version in Package Manifest](cmem_plugin_packages-BumpVersions.md) | Raise the version of a CPA manifest, by semantic level or to the current date. |
 | [Cancel Workflow](CancelWorkflow.md) | Cancels a workflow if a specified condition is fulfilled. A typical use case for this operator is to cancel the workflow execution if the input data is empty. |
 | [Clear dataset](clearDataset.md) | Clears the dataset that is connected to the output of this operator. |
 | [Combine CSV files](combine-csv.md) | Combine CSV files with the same structure to one dataset. |
 | [Concatenate to file](ConcatenateToFile.md) | Concatenates values into a file. |
 | [Create Embeddings](cmem_plugin_llm-CreateEmbeddings.md) | Turn the text of each entity into a vector embedding and add it to the entity. |
 | [Create or Update Graph Insights Snapshots](cmem_plugin_graph_insights-Update.md) | Create a snapshot for a graph that has none, or update it if one already exists. |
 | [Create/Update Salesforce Objects](cmem_plugin_salesforce-workflow-operations-SobjectCreate.md) | Manipulate data in your organization's Salesforce account. |
 | [Delete project files](deleteProjectFiles.md) | Removes file resources from the project based on a regular expression. |
 | [Distinct by](DistinctBy.md) | Removes duplicated entities based on user-defined paths. Duplicates can be resolved by keeping the first or last entity, or by keeping the entity with the minimum or maximum value of a compare path. |
 | [Download CKAN files](cmem_plugin_ckan-Download.md) | Download the files of a dataset from a CKAN service. |
 | [Download file](downloadFile.md) | Downloads a file from a given URL. |
 | [Download Git files](cmem_plugin_git-Download.md) | Download files from a git repository and hand them to the next task. |
 | [Download Nextcloud files](cmem_plugin_nextcloud-Download.md) | Download files from a given Nextcloud instance. |
 | [Download Office 365 Files](cmem_plugin_office365-Download.md) | Download files from Microsoft OneDrive or Sites |
 | [Download S3 objects](cmem_plugin_s3-Download.md) | Download objects from a bucket in S3 or S3-compatible object storage. |
 | [Download SSH files](cmem_plugin_ssh-Download.md) | Download files from an SSH server. |
 | [Evaluate template](Template.md) | Evaluates a template on a sequence of entities. Can be used after a transformation or directly after datasets that output a single table, such as CSV or Excel. A template that uses no input variables can be evaluated without an input. |
 | [Execute a command in a kubernetes pod](cmem_plugin_kubernetes-Execute.md) | Connect to a cluster, execute a command and gather the output. |
 | [Execute Catalog Query](cmem_plugin_querycatalog-ExecuteCatalogQuery.md) | Run a query stored in a query catalog and hand on its result. |
 | [Execute commands via SSH](cmem_plugin_ssh-Execute.md) | Execute a command on an SSH server. |
 | [Execute Instructions](cmem_plugin_llm-ExecuteInstructions.md) | Prompt a large language model once per entity and add the answer to the entity. |
 | [Execute REST requests](eccencaRestOperator.md) | REST operator that fetches and optionally merges data from a REST endpoint. It supports executing multiple requests either via input entities that each overwrite config parameters or via paging. If you only need to download a single file, the "Download file" operator might be the better option. Most features are currently only supported for JSON REST APIs. By default the output of this operator is one entity per response with a single property 'result' that holds the response body. Responses of multiple requests are merged into a single JSON array if the 'Parse JSON' operator is connected or the Accept header starts with 'application/json'. Alternatively the response/s can be written to the file of a connected file-based dataset, either as a merged JSON file (JSON dataset) or, if the dataset file ends in '.zip', one file per response inside a ZIP file. |
 | [Execute Spark function](SparkFunction.md) | Applies a specified Scala function to a specified field. |
 | [Extract from PDF files](cmem_plugin_pdf_extract-pdf_extract-PdfExtract.md) | Extract text and tables from PDF files |
 | [Generate base36 IRDIs](cmem_plugin_irdi-workflow-irdi_plugin-IrdiPlugin.md) | Create unique ECLASS IRDIs. |
 | [Generate random values](cmem_plugin_random-GenerateEntities.md) | Generates entities with random values. |
 | [Generate SHACL shapes from data](cmem_plugin_shapes-plugin_shapes-ShapesPlugin.md) | Generate SHACL node and property shapes from a data graph |
 | [Get Catalog Query](cmem_plugin_querycatalog-GetCatalogQuery.md) | Emit one entity describing a query stored in a query catalog. |
 | [Get emails](cmem-plugin-email-GetEmails.md) | Search IMAP mailbox and get email metadata or file attachments. |
 | [Get ntfy attachments](cmem_plugin_ntfy-GetAttachments.md) | Download the attachments of a topic's messages from an ntfy server. |
 | [Get ntfy messages](cmem_plugin_ntfy-GetMessages.md) | Read the messages of a topic from an ntfy server. |
 | [Get project files](getProjectFiles.md) | Get file resources from the project. |
 | [Get workflow report](cmem_plugin_wfreports_get_report.md) | Output a workflow execution report as a JSON file. |
 | [GraphQL query](cmem_plugin_graphql-Query.md) | Sends a GraphQL query or mutation to an endpoint and returns the result as entities. |
 | [Hetzner Cloud: List Resources](cmem_plugin_hetzner-ListResources.md) | Inventory all existing resources of a Hetzner Cloud project (servers, volumes, networks, load balancers, IPs, firewalls, SSH keys, snapshots, …), one entity per resource in a single union schema. |
 | [Hetzner Cloud: List Server Types](cmem_plugin_hetzner-ListServerTypes.md) | List all available Hetzner Cloud server (VM) types, one entity per server type and location, including specs and per-location pricing. |
 | [Install Packages](cmem_plugin_packages-InstallPackages.md) | Install packages and their dependencies from a marketplace service or from package archives. |
 | [Join tables](Merge.md) | Joins a set of inputs into a single table. Expects a list of entity tables and links. All entity tables are joined into the first entity table using the provided links. |
 | [jq](cmem-plugin-jq-workflow.md) | Process a JSON document with a jq filter / program. |
 | [JQL query](cmem_plugin_jira-JqlQuery.md) | Search and retrieve Jira issues. |
 | [JSON to File](jsonToFile.md) | Writes a JSON string held in a field on each valid incoming entity to a file. Depending on the output mode, it produces one file per entity, packs all entities into a single ZIP archive, or merges them into a single JSON array file. Produces a file entity downstream, suitable for wiring into a file-backed dataset or any operator that consumes file entities. |
 | [Kafka Consumer (Receive Messages)](cmem_plugin_kafka-ReceiveMessages.md) | Reads messages from a Kafka topic as entities, or saves them to a dataset (Consumer). |
 | [Kafka Producer (Send Messages)](cmem_plugin_kafka-SendMessages.md) | Sends entities, or messages from a dataset, to a Kafka topic (Producer). |
 | [List Catalog Queries](cmem_plugin_querycatalog-ListCatalogQueries.md) | Emit one entity per query stored in a query catalog. |
 | [List Git files](cmem_plugin_git-List.md) | List the files of a git repository, without transferring their content. |
 | [List Nextcloud files](cmem_plugin_nextcloud-List.md) | List directories and files from a given Nextcloud folder. |
 | [List Office 365 Files](cmem_plugin_office365-List.md) | List files from OneDrive or Sites |
 | [List project files](cmem_plugin_project_resources-List.md) | List file resources from the project. |
 | [List S3 objects](cmem_plugin_s3-List.md) | List the objects of a bucket in S3 or S3-compatible object storage. |
 | [List SSH files](cmem_plugin_ssh-List.md) | List the files of a directory on an SSH server, with their metadata. |
 | [Merge tables](MultiTableMerge.md) | Stores sets of instance and mapping inputs as relational tables with the mapping as an n:m relation. Expects a list of entity tables and links. All entity tables have a relation to the first entity table using the provided links. |
 | [Normalize units of measurement](ucumNormalizationTask.md) | Custom task that will substitute numeric values and pertaining unit symbols with a SI-system-unit normalized representation. |
 | [OAuth2 Authentication](cmem_plugin_auth-workflow-auth-OAuth2.md) | Provide an OAuth2 access token for other tasks (via config port). |
 | [Office 365 Upload Files](cmem_plugin_office365-Upload.md) | Upload files to OneDrive or a site Sharepoint |
 | [Parse JSON](JsonParserOperator.md) | Parses a JSON string held in a field on each incoming entity. Typically used before a transformation task. Takes exactly one input. |
 | [Parse XML](XmlParserOperator.md) | Takes exactly one input and reads either the defined inputPath or the first value of the first entity as XML document. Then executes the given output entity schema similar to the XML dataset to construct the result entities. |
 | [Parse YAML](cmem_plugin_yaml-parse.md) | Parses YAML documents from a code field, entities or files and converts them to JSON. |
 | [Pivot](Pivot.md) | The pivot operator takes data in separate rows, aggregates it and converts it into columns. |
 | [Publish Packages](cmem_plugin_packages-PublishPackages.md) | Publish package archives to a marketplace service. |
 | [Reason](cmem_plugin_reason-plugin_reason-ReasonPlugin.md) | Performs OWL reasoning. |
 | [Request RDF triples](tripleRequestOperator.md) | A task that requests all triples from an RDF dataset. |
 | [Run Apify actor](cmem_plugin_apify-RunActor.md) | Run an Apify actor and deliver its dataset as a file. |
 | [Scheduler](Scheduler.md) | Executes a workflow at specified intervals. |
 | [Search addresses](SearchAddresses.md) | Looks up locations from textual descriptions using the configured geocoding API. Outputs results as RDF. |
 | [Search for Logs](cmem_plugin_logpoint-search_logs_task-RetrieveLogs.md) | Search and retrieve logs from a Logpoint SIEM system with flexible schema output. |
 | [Search LDAP directory](cmem_plugin_ldap-Search.md) | Query LDAP directory services such as OpenLDAP or Active Directory. |
 | [Search Vector Embeddings](cmem_plugin_pgvector-Search.md) | Search for the top-k nearest matches to a query embedding in Postgres Vector Store (PGVector). |
 | [Select random entities](cmem_plugin_random-SelectEntities.md) | Select X random entities from an input dataset. |
 | [Send email](SendEMail.md) | Sends an email using an SMTP server. |
 | [Send Mattermost messages](cmem_plugin_mattermost.md) | Post messages to Mattermost users and channels through a bot account. |
 | [Send ntfy attachment](cmem_plugin_ntfy-SendAttachment.md) | Send a file as an attachment to a topic on an ntfy server. |
 | [Send ntfy message](cmem_plugin_ntfy-SendMessage.md) | Send a push notification to a topic on an ntfy server. |
 | [Set execution variable](setExecutionVariableOperator.md) | Sets an execution variable to the first value of the (single) input and passes the input through unchanged. The variable is written to the 'execution' scope and can be read downstream as 'execution.<name>'. Only works while running inside a workflow execution. |
 | [Set or Overwrite parameters](cmem_plugin_parameters-ParametersPlugin.md) | Connect this task to a config port of another task in order to set or overwrite the parameter values of this task. |
 | [Set parameters](setParameters.md) | Set and overwrite parameters of a task. |
 | [SHACL validation with pySHACL](shacl-pyshacl.md) | Performs SHACL validation with pySHACL. |
 | [SOQL query (Salesforce)](cmem_plugin_salesforce-SoqlQuery.md) | Executes a custom Salesforce Object Query (SOQL) to return sets of data your organization's Salesforce account. |
 | [Spark SQL query](CustomSQLExecution.md) | Executes a Spark SQL query on the input entities and returns the result as its output. |
 | [SPARQL Construct query](sparqlCopyOperator.md) | A task that executes a SPARQL Construct query on a SPARQL enabled data source and outputs the SPARQL result. If the result should be written to the same RDF store it is read from, the SPARQL Update operator is preferable. |
 | [SPARQL Select query](sparqlSelectOperator.md) | A task that executes a SPARQL Select query and outputs the SPARQL result. |
 | [SPARQL Update query](sparqlUpdateOperator.md) | A task that outputs SPARQL Update queries for every entity from the input based on a SPARQL Update template. The output of this operator should be connected to the SPARQL datasets to which the results should be written. |
 | [Split file](cmem_plugin_splitfile-plugin_splitfile-SplitFilePlugin.md) | Split a file into multiple parts with a specified size. |
 | [SQL Update query](sqlUpdateQueryOperator.md) | A task that outputs SQL queries. The output of this operator should be connected to a remote SQL endpoint on which queries should be executed. |
 | [Start Workflow per Entity](cmem_plugin_loopwf-task-StartWorkflow.md) | Loop over the output of a task and start a sub-workflow for each entity. |
 | [Store Vector Embeddings](cmem_plugin_pgvector-Store.md) | Store embeddings into Postgres Vector Store (PGVector). |
 | [Uninstall Packages](cmem_plugin_packages-UninstallPackages.md) | Uninstall packages and their unused dependencies from this instance. |
 | [Unpivot](Unpivot.md) | Given a list of table columns, transforms those columns into attribute-value pairs. |
 | [Upload File to Knowledge Graph](eccencaDataPlatformGraphStoreFileUploadOperator.md) | Uploads an N-Triples or Turtle (limited support) file from the file repository to a 'Knowledge Graph' dataset. The output of this operatorcan be the input of datasets that support graph store file upload, e.g. 'Knowledge Graph'. The file will be uploaded to the graph specified in that dataset. |
 | [Upload files to CKAN](cmem_plugin_ckan-Upload.md) | Publish files as the files of a dataset on a CKAN service. |
 | [Upload files to Nextcloud](cmem_plugin_nextcloud-Upload.md) | Upload files to a given Nextcloud instance. |
 | [Upload files to S3](cmem_plugin_s3-Upload.md) | Upload files to a bucket in S3 or S3-compatible object storage. |
 | [Upload Git files](cmem_plugin_git-Upload.md) | Commit the files of the preceding task into a git repository. |
 | [Upload local files](cmem_plugin_project_resources-UploadLocalFiles.md) | Replace a file dataset resource with a local file or upload multiple local files to a project. |
 | [Upload SSH files](cmem_plugin_ssh-Upload.md) | Upload files to an SSH server. |
 | [Validate Entities](cmem_plugin_validation-validate-ValidateEntities.md) | Use a JSON schema to validate entities or a JSON dataset. |
 | [Validate Knowledge Graph](cmem_plugin_validation-validate-ValidateGraph.md) | Use SHACL shapes to validate resources in a Knowledge Graph. |
 | [Validate OWL consistency](cmem_plugin_reason-plugin_validate-ValidatePlugin.md) | Validates the consistency of an OWL ontology. |
 | [Validate XML](validateXsdOperator.md) | Validates an XML dataset against a provided XML schema (XSD) file. Any errors are written to the output. Can be used in conjunction with the `Cancel Workflow` operator in order to stop the workflow if errors have been found. |
 | [XSLT](xsltOperator.md) | A task that converts an XML resource via an XSLT script and writes the transformed output into a file resource. |
