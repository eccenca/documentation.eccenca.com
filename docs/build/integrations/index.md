---
title: "Integrations"
icon: octicons/cross-reference-24
hide:
    - toc
tags:
    - Build
    - Reference
---
# Integrations
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The following services and applications can be easily integrated in Corporate Memory workflows:

<div class="grid cards" markdown>

- :simple-anthropic:{ .lg .middle } Anthropic / Claude

    ---

    Use the [Execute Instructions](../../build/reference/customtask/cmem_plugin_llm-ExecuteInstructions.md) or [Create Embeddings](../../build/reference/customtask/cmem_plugin_llm-CreateEmbeddings.md) task
to interact with any
[Anthropic / Claude provided Large Language Models](https://docs.claude.com/en/docs/about-claude/models/overview)
(LLMs).

- :other-apacheavro:{ .lg .middle } Avro

    ---

    Use the [Avro](../../build/reference/dataset/avro.md) dataset to read and write files in the [Avro format](https://avro.apache.org/).

- :material-microsoft-azure:{ .lg .middle } Azure AI Foundry

    ---

    Use the [Execute Instructions](../../build/reference/customtask/cmem_plugin_llm-ExecuteInstructions.md) or [Create Embeddings](../../build/reference/customtask/cmem_plugin_llm-CreateEmbeddings.md) task
to interact with any [Azure AI Foundry provided Large Language Models](https://ai.azure.com/catalog) (LLMs).

- :fontawesome-solid-file-csv:{ .lg .middle } CSV

    ---

    Comma-separated values (CSV) is a text data format which can be processed
(read and write) with the [CSV Dataset](../../build/reference/dataset/csv.md).

- :material-email-outline:{ .lg .middle } eMail / SMTP

    ---

    Send plain text or HTML formatted [eMail messages](../../build/reference/customtask/SendEMail.md) using an SMTP server.

- :material-file-excel:{ .lg .middle } Excel

    ---

    Use the [Excel](../../build/reference/dataset/excel.md) task to read and write to Excel workbooks in the Open XML format (XLSX).

- :material-google-drive:{ .lg .middle } Google Drive

    ---

    Use the [Excel (Google Drive)](../../build/reference/dataset/googlespreadsheet.md) to read and write to Excel workbooks in Google Drive.

- :other-graphdb:{ .lg .middle } GraphDB

    ---

    Load and write Knowledge Graphs to an external GraphDB store by using the [SPARQL endpoint](../../build/reference/dataset/sparqlEndpoint.md) dataset.
Query data from GraphDB by using the SPARQL
[Construct](../../build/reference/customtask/sparqlCopyOperator.md),
[Select](../../build/reference/customtask/sparqlSelectOperator.md) and
[Update](../../build/reference/customtask/sparqlUpdateOperator.md) tasks.
GraphDB can be used as the integrated Quad Store as well.

- :simple-graphql:{ .lg .middle } GraphQL

    ---

    You can execute a [GraphQL query](../../build/reference/customtask/cmem_plugin_graphql-workflow-graphql-GraphQLPlugin.md) and process the result in a workflow.

- :simple-apachehive:{ .lg .middle } Hive

    ---

    Read from or write to an embedded Apache [Hive database](../../build/reference/dataset/Hive.md) endpoint.

- :simple-jira:{ .lg .middle } Jira

    ---

    Execute a [JQL query](../../build/reference/customtask/cmem_plugin_jira-JqlQuery.md) on a Jira instance to fetch and integrate issue data.

- :material-code-json:{ .lg .middle } JSON

    ---

    Use the [JSON](../../build/reference/dataset/json.md) dataset to read and write JSON files (JavaScript Object Notation).

- :material-code-json:{ .lg .middle } JSON Lines

    ---

    Use the [JSON](../../build/reference/dataset/json.md) dataset to read and write files in the [JSON Lines](https://jsonlines.org/) text file format.

- :simple-apachekafka:{ .lg .middle } Kafka

    ---

    You can [send](../../build/reference/customtask/cmem_plugin_kafka-SendMessages.md) and
[receive messages](../../build/reference/customtask/cmem_plugin_kafka-ReceiveMessages.md) to and from a Kafka topic.

- :simple-kubernetes:{ .lg .middle } Kubernetes

    ---

    You can [Execute a command in a kubernetes pod](../../build/reference/customtask/cmem_plugin_kubernetes-Execute.md) and captures its output to process it.

- :simple-mariadb:{ .lg .middle } MariaDB

    ---

    MariaDB can be accessed with the [Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/org.mariadb.jdbc/mariadb-java-client/overview).

- :simple-mattermost:{ .lg .middle } Mattermost

    ---

    Send workflow reports or any other message to user and groups in you Mattermost with
the [Send Mattermost messages](../../build/reference/customtask/cmem_plugin_mattermost.md) task.

- :material-microsoft:{ .lg .middle } Microsoft SQL

    ---

    The Microsoft SQL Server can be accessed with the [Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/com.microsoft.sqlserver/mssql-jdbc).

- :simple-mysql:{ .lg .middle } MySQL

    ---

    MySQL can be accessed with the [Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/org.mariadb.jdbc/mariadb-java-client/overview).

- :simple-neo4j:{ .lg .middle } Neo4J

    ---

    Use the [Neo4j](../../build/reference/dataset/neo4j.md) dataset for reading and writing [Neo4j graphs](https://neo4j.com/).

- :other-neptune:{ .lg .middle } Neptune

    ---

    Load and write Knowledge Graphs to Amazon Neptune by using the [SPARQL endpoint](../../build/reference/dataset/sparqlEndpoint.md) dataset.
Query data from Amazon Neptune by using the SPARQL
[Construct](../../build/reference/customtask/sparqlCopyOperator.md),
[Select](../../build/reference/customtask/sparqlSelectOperator.md) and
[Update](../../build/reference/customtask/sparqlUpdateOperator.md) tasks.
Amazon Neptune can be used as the integrated Quad Store as well (beta).

- :simple-nextcloud:{ .lg .middle } Nextcloud

    ---

    Use a Nextcloud instance to [download files](../../build/reference/customtask/cmem_plugin_nextcloud-Download.md) to process
them or [upload files](../../build/reference/customtask/cmem_plugin_nextcloud-Upload.md) you created with Corporate Memory.

- :material-microsoft-office:{ .lg .middle } Office 365

    ---

    Use the [Excel (OneDrive, Office365)](../../build/reference/dataset/office365preadsheet.md) to read and write to Excel workbooks in Office 365.

- :simple-ollama:{ .lg .middle } Ollama

    ---

    Use the [Execute Instructions](../../build/reference/customtask/cmem_plugin_llm-ExecuteInstructions.md) or [Create Embeddings](../../build/reference/customtask/cmem_plugin_llm-CreateEmbeddings.md) task
to interact with Ollama provided Large Language Models (LLMs).

- :simple-openai:{ .lg .middle } OpenAI

    ---

    Use the [Execute Instructions](../../build/reference/customtask/cmem_plugin_llm-ExecuteInstructions.md) or [Create Embeddings](../../build/reference/customtask/cmem_plugin_llm-CreateEmbeddings.md) task
to interact with any [OpenAI provided Large Language Models](https://platform.openai.com/docs/models) (LLMs).

- :octicons-ai-model-24:{ .lg .middle } OpenRouter

    ---

    Use the [Execute Instructions](../../build/reference/customtask/cmem_plugin_llm-ExecuteInstructions.md) or [Create Embeddings](../../build/reference/customtask/cmem_plugin_llm-CreateEmbeddings.md) task
to interact with any [OpenRouter provided Large Language Models](https://openrouter.ai/models) (LLMs).

- :other-apacheorc:{ .lg .middle } ORC

    ---

    Use the [ORC](../../build/reference/dataset/orc.md) dataset to read and write files in the [ORC](https://orc.apache.org/) format.

- :simple-apacheparquet:{ .lg .middle } Parquet

    ---

    Use the [Parquet](../../build/reference/dataset/parquet.md) dataset to read and write files in the [Parquet](https://parquet.apache.org/) format.

- :black_large_square:{ .lg .middle } pgvector

    ---

    Store vector embeddings into [pgvector](https://github.com/pgvector/pgvector)
using the [Search Vector Embeddings](../../build/reference/customtask/cmem_plugin_pgvector-Search.md).

- :simple-postgresql:{ .lg .middle } PostgreSQL

    ---

    PostgreSQL can be accessed with the [Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/org.postgresql/postgresql/versions).

- :other-powerbi:{ .lg .middle } PowerBI

    ---

    Leverage your Knowledge Graphs in PowerBI by using our
[Corporate Memory Power-BI-Connector](../../consume/consuming-graphs-in-power-bi/index.md).

- :other-qlever:{ .lg .middle } Qlever

    ---

    Load and write Knowledge Graphs to an external Qlever store by using the [SPARQL endpoint](../../build/reference/dataset/sparqlEndpoint.md) dataset.
Query data from Qlever by using the SPARQL
[Construct](../../build/reference/customtask/sparqlCopyOperator.md),
[Select](../../build/reference/customtask/sparqlSelectOperator.md) and
[Update](../../build/reference/customtask/sparqlUpdateOperator.md) tasks.
Qlever can be used as the integrated Quad Store as well (beta).

- :simple-semanticweb:{ .lg .middle } RDF

    ---

    Use the [RDF file](../../build/reference/dataset/file.md) dataset to read and write files in the RDF formats
([N-Quads](https://www.w3.org/TR/n-quads/), [N-Triples](https://www.w3.org/TR/n-triples/),
[Turtle](https://www.w3.org/TR/turtle/), [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/) or
[RDF/JSON](https://www.w3.org/TR/rdf-json/)).

- :other-redash:{ .lg .middle } Redash

    ---

    Leverage your Knowledge Graphs in Redash using the integrated
[Corporate Memory Redash-Connector](../../consume/consuming-graphs-with-redash/index.md).

- :material-application-braces-outline:{ .lg .middle } REST

    ---

    Execute REST requests using [Execute REST requests](../../build/reference/customtask/eccencaRestOperator.md).

- :fontawesome-brands-salesforce:{ .lg .middle } Salesforce

    ---

    Interact with your Salesforce data, such as [Create/Update Salesforce Objects](../../build/reference/customtask/cmem_plugin_salesforce-workflow-operations-SobjectCreate.md) or
execute a [SOQL query (Salesforce)](../../build/reference/customtask/cmem_plugin_salesforce-SoqlQuery.md).

- :simple-snowflake:{ .lg .middle } Snowflake

    ---

    Snowflake can be accessed with the [Snowflake SQL endpoint](../../build/reference/dataset/SnowflakeJdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/net.snowflake/snowflake-jdbc).

- :simple-apachespark:{ .lg .middle } Spark

    ---

    Apply a [Spark](https://spark.apache.org/) function to a specified field using [Execute Spark function](../../build/reference/customtask/SparkFunction.md).

- :simple-sqlite:{ .lg .middle } SQLite

    ---

    SQLite can be accessed with the [Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a
[JDBC driver](https://central.sonatype.com/artifact/org.xerial/sqlite-jdbc).

- :material-ssh:{ .lg .middle } SSH

    ---

    Interact with SSH servers to [Download SSH files](../../build/reference/customtask/cmem_plugin_ssh-Download.md) or [Execute commands via SSH](../../build/reference/customtask/cmem_plugin_ssh-Execute.md).

- :other-tentris:{ .lg .middle } Tentris

    ---

    Load and write Knowledge Graphs to an external Tentris store by using the [SPARQL endpoint](../../build/reference/dataset/sparqlEndpoint.md) dataset.
Query data from Tentris by using the SPARQL
[Construct](../../build/reference/customtask/sparqlCopyOperator.md),
[Select](../../build/reference/customtask/sparqlSelectOperator.md) and
[Update](../../build/reference/customtask/sparqlUpdateOperator.md) tasks.
Tentris can be used as the integrated Quad Store as well (beta).

- :simple-trino:{ .lg .middle } Trino

    ---

    [Trino](https://github.com/trinodb/trino) can be access with the
[Remote SQL endpoint](../../build/reference/dataset/Jdbc.md) dataset and a [JDBC driver](https://trino.io/docs/current/client/jdbc.html).

- :black_large_square:{ .lg .middle } Virtuoso

    ---

    Load and write Knowledge Graphs to an external Openlink Virtuoso store by using the [SPARQL endpoint](../../build/reference/dataset/sparqlEndpoint.md) dataset.
Query data from Virtuoso by using the SPARQL
[Construct](../../build/reference/customtask/sparqlCopyOperator.md),
[Select](../../build/reference/customtask/sparqlSelectOperator.md) and
[Update](../../build/reference/customtask/sparqlUpdateOperator.md) tasks.
Virtuoso can be used as the integrated Quad Store as well (beta).

- :material-xml:{ .lg .middle } XML

    ---

    Load and write data to XML files with the [XML](../../build/reference/dataset/xml.md) dataset as well as
[Parse XML](../../build/reference/customtask/XmlParserOperator.md) from external services.

- :simple-yaml:{ .lg .middle } YAML

    ---

    Load and integrate data from YAML files with the [Parse YAML](../../build/reference/customtask/cmem_plugin_yaml-parse.md) task.

- :material-code-json:{ .lg .middle } Zipped JSON

    ---

    Use the [JSON](../../build/reference/dataset/json.md) dataset to read and write JSON files in a ZIP Archive.

</div>
