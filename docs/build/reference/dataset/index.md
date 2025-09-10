---
title: "Datasets"
icon: octicons/cross-reference-24
tags:
    - Build
    - Reference
---
# Datasets
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Datasets are collections of data that can be read or written.

**:octicons-people-24: Intended audience:** Linked Data Experts and Domain Experts

|         Name | Description              |
|-------------:|:-------------------------|
 | [Alignment](alignment.md) | Writes the alignment format specified at http://alignapi.gforge.inria.fr/format.html. |
 | [Avro](avro.md) | Read from or write to an Apache Avro file. |
 | [Binary file](binaryFile.md) | Reads and writes binary files. A typical use-case for this dataset is to process PDF documents or images. |
 | [CSV](csv.md) | Read from or write to an CSV file. |
 | [Excel](excel.md) | Read from or write to an Excel workbook in Open XML format (XLSX). The sheet is selected by specifying it as type in the subsequent workflow operator. |
 | [Excel (Google Drive)](googlespreadsheet.md) | Read data from a remote Google Spreadsheet. |
 | [Excel (OneDrive, Office365)](office365preadsheet.md) | Read data from a remote onedrive or Office365 Spreadsheet. |
 | [Hive database](Hive.md) | Read from or write to an embedded Apache Hive endpoint. |
 | [In-memory dataset](inMemory.md) | A Dataset that holds all data in-memory. |
 | [Internal dataset](internal.md) | Dataset for storing entities between workflow steps. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters. |
 | [Internal dataset (single graph)](LocalInternalDataset.md) | Dataset for storing entities between workflow steps. This variant does use the same graph for all internal datasets in a workflow. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters. |
 | [JDBC endpoint](Jdbc.md) | Connect to an existing JDBC endpoint. |
 | [JSON](json.md) | Read from or write to a JSON or JSON Lines file. |
 | [Knowledge Graph](eccencaDataPlatform.md) | Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory. |
 | [Multi CSV ZIP](multiCsv.md) | Reads from or writes to multiple CSV files from/to a single ZIP file. |
 | [Neo4j](neo4j.md) | Neo4j graph |
 | [ORC](orc.md) | Read from or write to an Apache ORC file. |
 | [Parquet](parquet.md) | Read from or write to an Apache Parquet file. |
 | [RDF file](file.md) | Dataset which retrieves and writes all entities from/to an RDF file. For reading, the dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead. |
 | [Snowflake JDBC endpoint](SnowflakeJdbc.md) | Connect to Snowflake JDBC endpoint. |
 | [SparkSQL view](sparkView.md) | Use the SQL endpoint dataset instead. |
 | [SPARQL endpoint](sparqlEndpoint.md) | Connects to an existing SPARQL endpoint. |
 | [SQL endpoint](sqlEndpoint.md) | Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL. |
 | [Text](text.md) | Reads and writes plain text files. |
 | [XML](xml.md) | Read from or write to an XML file. |
