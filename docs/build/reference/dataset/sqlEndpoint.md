---
title: "Embedded SQL endpoint"
description: "Provides a JDBC endpoint that exposes workflow or transformation results as tables, which can be queried using SQL."
icon: octicons/cross-reference-24
tags:
    - Dataset
---

# Embedded SQL endpoint

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Embedded SQL Endpoint Dataset

Within BUILD, several Spark-aware datasets exist — Avro, Parquet, ORC, HDFS, Hive — each optimized to leverage Spark’s parallel, in-memory execution. Complementing these table-based and file-based datasets, the **Embedded SQL Endpoint** provides a **queryable, relational interface** to workflow results or transformations. Unlike file-based formats, this endpoint exposes results as **virtual tables**, accessible via **JDBC or other SQL clients**, enabling downstream queries, reporting, or integration without requiring persistent storage.

### Concept

The Embedded SQL Endpoint represents **workflow-generated tables**. It is **not a general-purpose query endpoint**; each table corresponds directly to workflow outputs and serves as a **source or sink** within the workflow, functioning as a **dataset** like other Spark-aware datasets and integrating with BUILD plugins in the usual way.

The endpoint allows workflows to **publish results as tables** in a format compatible with standard SQL tooling. Multiple tables can be exposed per workflow if complex mappings exist. Table names can be **customized using a prefix** or automatically generated for convenience. By caching tables in memory, Spark ensures that queries execute efficiently while maintaining fault tolerance and parallelism inherent in the Spark ecosystem.

Conceptually, these tables can be **consumed by other workflows or plugins** without needing to manage Spark execution details.

### Key Features

- **Virtual table exposure**: Any workflow or transformation result can be turned into a SQL-accessible table.
- **Multiple tables per workflow**: If the workflow produces multiple entity types, each type can become a separate table.
- **Table name customization**: `tableNamePrefix` allows semantic or organizational naming of tables.
- **In-memory caching**: Optional caching accelerates repeated queries while preserving fault tolerance.
- **Array and type compatibility**: Arrays can be serialized using a configurable separator (`arraySeparator`), and complex Spark types are converted to basic types for external clients (`useCompatibleTypes`).
- **Column mapping**: Optional aliasing of columns via `map` ensures semantic clarity and client compatibility.
- **Integration**: Fits seamlessly into BUILD workflows alongside other Spark-aware datasets.
- **Client independence**: External consumers do not need to manage partitions, caching, or Spark execution details.

### Activity Behavior

- The SQL endpoint **starts automatically** when used as a workflow sink and when BUILD is configured to make it remotely accessible.
- When running, the activity **returns the server status and JDBC URL**.
- **Stopping** the activity drops all generated views; it can be restarted by rerunning the workflow.

### Remote Client Access

- Access via **JDBC or ODBC** is possible when the `startThriftServer` option is enabled.
- Supported drivers:
    - JDBC compatible with **Hive 1.2.1** (`org.apache.hive.jdbc.HiveDriver`)
    - JDBC compatible with **Spark 2.3.3**
    - Hive ODBC driver for the client OS architecture
- Table and column names are sanitized for database compatibility:
    - Only `a-z`, `A-Z`, `0-9`, and `_` are allowed; other characters replaced with `_`.
    - Table names truncated to 128 characters; column names converted to lowercase.
- Any JDBC/ODBC client can connect; SparkSQL uses Hive-compatible query processing.
- [DBeaver](https://dbeaver.io/) connects out-of-the-box; see [Apache HiveServer2 Clients](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients) for additional tools.

### Conceptual Workflow Usage

- Transform data using Spark-optimized datasets (Hive, HDFS, Parquet, ORC, Avro).
- Publish intermediate or final results via the SQL endpoint.
- External consumers query the published tables without needing to manage Spark internals.
- Maintains semantic alignment with the Knowledge Graph indirectly, as table content can be structured according to workflow-derived entity URIs and properties.

### Comparison with Other Spark-aware Datasets

| Aspect                          | Embedded SQL Endpoint                                                                                 | Hive Dataset                                                        | HDFS Dataset (Sequence Files)                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Type                            | Virtual table / JDBC-accessible endpoint                                                              | Table-based, structured                                             | File-based, row-oriented                                                |
| Storage / persistence           | In-memory, transient                                                                                  | Hive tables (persistent, partitioned)                               | Hadoop sequence files (persistent, row-based)                           |
| Querying                        | SQL / JDBC queries                                                                                    | Optional SQL for filtering/projection                               | Handled via workflow transformations in Spark                           |
| Caching                         | Optional in-memory caching                                                                            | Handled by Spark                                                    | Handled by Spark                                                        |
| Integration with workflows      | Directly exposes workflow outputs                                                                     | Consumed as a Spark-optimized dataset                               | Consumed as a Spark-optimized dataset                                   |
| Best use case in CMEM workflows | Queryable exposure of workflow or transformation results for external clients or downstream workflows | Ingesting structured Hive tables with optional filtering/projection | Ingesting row-oriented sequence files, often for large-scale processing |


## Parameter

### Table name prefix

Prefix of the table that will be shared. In the case of complex mappings more than one table will be created. If one name is given it will be used as a prefix for table names. If left empty the table names will be generated from the user name and time stamps and start with 'root', 'object-mapping'

- ID: `tableNamePrefix`
- Datatype: `string`
- Default Value: `None`



### Cache

Optional boolean option that selects if the table should be cached by Spark or not (default = true).

- ID: `cache`
- Datatype: `boolean`
- Default Value: `true`



### Array separator

The character that is used to separate the parts of array values. Write \t to specify the tab character.

- ID: `arraySeparator`
- Datatype: `string`
- Default Value: `|`



### Compatibility

If true, basic types will be used for unusual data types that otherwise may result in client errors. Try switching this on, if a client has weird error messages. (Default = true)

- ID: `useCompatibleTypes`
- Datatype: `boolean`
- Default Value: `true`



### Map

Mapping of column names. Similar to aliases E.g. 'c1:c2' would rename column c1 into c2.

- ID: `map`
- Datatype: `stringmap`
- Default Value: `None`





## Advanced Parameter

`None`
