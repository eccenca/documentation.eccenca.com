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

|                                                    Name |                                                Category                                                 | Description              |
|--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------:|:-------------------------|
 | [Alignment](alignment.md) | None | Writes the alignment format specified at http://alignapi.gforge.inria.fr/format.html. |
 | [Avro](avro.md) | None | Read from or write to an Apache Avro file. |
 | [Binary file](binaryFile.md) | None | Reads and writes binary files. A typical use-case for this dataset is to process PDF documents or images. |
 | [CSV](csv.md) | None | Read from or write to an CSV file. |
 | [Excel](excel.md) | None | Read from or write to an Excel workbook in Open XML format (XLSX). |
 | [Excel (Google Drive)](googlespreadsheet.md) | None | Read data from a remote Google Spreadsheet. |
 | [Excel (OneDrive, Office365)](office365preadsheet.md) | None | Read data from a remote onedrive or Office365 Spreadsheet. |
 | [Hive database](Hive.md) | None | Read from or write to an embedded Apache Hive endpoint. |
 | [In-memory dataset](inMemory.md) | None | A Dataset that holds all data in-memory. |
 | [Internal dataset](internal.md) | None | Dataset for storing entities between workflow steps. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters. |
 | [Internal dataset (single graph)](LocalInternalDataset.md) | None | Dataset for storing entities between workflow steps. This variant does use the same graph for all internal datasets in a workflow. The underlying dataset type can be configured using the `dataset.internal.*` configuration parameters. |
 | [JDBC endpoint](Jdbc.md) | None | Connect to an existing JDBC endpoint. |
 | [JSON](json.md) | None | Read from or write to a JSON or JSON Lines file. |
 | [Knowledge Graph](eccencaDataPlatform.md) | None | Read RDF from or write RDF to a Knowledge Graph embedded in Corporate Memory. |
 | [Multi CSV ZIP](multiCsv.md) | None | Reads from or writes to multiple CSV files from/to a single ZIP file. |
 | [Neo4j](neo4j.md) | None | Neo4j graph |
 | [ORC](orc.md) | None | Read from or write to an Apache ORC file. |
 | [Parquet](parquet.md) | None | Read from or write to an Apache Parquet file. |
 | [RDF](file.md) | None | Dataset which retrieves and writes all entities from/to an RDF file. For reading, the dataset is loaded in-memory and thus the size is restricted by the available memory. Large datasets should be loaded into an external RDF store and retrieved using the SPARQL dataset instead. |
 | [Snowflake JDBC endpoint](SnowflakeJdbc.md) | None | Connect to Snowflake JDBC endpoint. |
 | [SparkSQL view](sparkView.md) | None | Use the SQL endpoint dataset instead. |
 | [SPARQL endpoint](sparqlEndpoint.md) | None | Connect to an existing SPARQL endpoint. |
 | [SQL endpoint](sqlEndpoint.md) | None | Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL. |
 | [Text](text.md) | None | Reads and writes plain text files. |
 | [XML](xml.md) | None | Read from or write to an XML file. |
