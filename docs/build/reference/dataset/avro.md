---
title: "Avro"
description: "Read from or write to an Apache Avro file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Avro
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Avro Dataset

The Avro dataset plugin in BUILD provides the ability to read from or write to Apache Avro files. It is a **Spark-optimized dataset**, designed to leverage Spark’s in-memory, parallel execution model and take advantage of Avro-specific optimizations.

Avro supports **schema evolution** and **efficient serialization**, enabling Spark to process structured data reliably across workflow changes. While columnar optimizations like Parquet or ORC are not applicable, Avro provides **fast row-based access** and compact storage, making it suitable for workloads where the data structure may change over time or full-row access is common.
### Key Features

- **Row-based storage format**: Avro stores data row-wise, enabling efficient serialization and deserialization for distributed processing.
- **Schema support**: Explicit schemas are stored with the dataset, ensuring compatibility and supporting schema evolution.
- **Compression**: Supports multiple compression algorithms, e.g., Snappy or Deflate, reducing storage footprint and improving I/O performance.
- **Interoperability**: Avro is widely supported across big data tools, making it easy to exchange data between systems.

### Example

An Avro dataset in CMEM Build might look conceptually like this:

| transaction_id | customer_id | amount | timestamp          |
|----------------|-------------|--------|------------------|
| 1              | 1001        | 150.00 | 2025-11-01 08:15 |
| 2              | 1002        | 200.50 | 2025-11-01 09:30 |
| 3              | 1003        | 75.25  | 2025-11-01 11:20 |

This dataset could be stored in a file `transactions.avro` and used in workflows where row-oriented access or schema evolution is needed. Spark reads the data efficiently, and the explicit schema ensures correct mapping of fields across transformations.

### Reference

For more information on the Avro format and its optimizations, see the [Apache Avro project page](https://avro.apache.org/).

---
### Comparison of Spark-optimized datasets

The following table summarizes the key differences and typical use cases of the main Spark-optimized datasets supported in CMEM BUILD. It provides a quick reference for understanding the optimizations, storage formats, and workflow suitability for ORC, Parquet, and Avro datasets.

| Aspect                          | ORC                                                                                                            | Parquet                                                                                                          | Avro                                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Spark optimization              | Yes – in-memory, columnar, leverages column pruning & predicate pushdown                                       | Yes – in-memory, columnar, leverages column pruning & predicate pushdown                                         | Yes – row-based, less efficient for selective column access, better for streaming or row-oriented data      |
| Storage format                  | Columnar                                                                                                       | Columnar                                                                                                         | Row-oriented                                                                                                |
| Column pruning                  | Supported                                                                                                      | Supported                                                                                                        | Not supported efficiently                                                                                   |
| Predicate pushdown              | Supported                                                                                                      | Supported                                                                                                        | Limited / not native                                                                                        |
| Partitioning support            | Optional                                                                                                       | Optional                                                                                                         | Optional, typically less impactful                                                                          |
| Compression                     | Snappy, Zlib, etc.                                                                                             | Snappy, Gzip, etc.                                                                                               | Snappy, Deflate, etc.                                                                                       |
| Schema handling                 | Explicit or inferred, applied to dataset                                                                       | Explicit or inferred, applied to dataset                                                                         | Schema required, applied to rows                                                                            |
| Typical usage                   | Workflows needing efficient column-based access and filtered rows                                              | Similar to ORC, widely used in Hadoop ecosystems, columnar analytics                                             | Workflows needing row-wise access, streaming ingestion, or evolving schema                                  |
| Best use case in CMEM workflows | Workflows where only subsets of columns or filtered rows are processed frequently, large-scale transformations | General-purpose analytics and ETL tasks where columnar processing improves performance, medium-to-large datasets | Ingesting external row-oriented sources, streaming integration, or datasets with frequently evolving schema |


## Parameter

### File

Path (e.g. relative like `path/filename.avro` or absolute `hdfs:///path/filename.avro`).

- ID: `file`
- Datatype: `resource`
- Default Value: `None`



### Uri pattern

A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is `urn:zyx:{id}` where `*id*` is a name of a property.

- ID: `uriPattern`
- Datatype: `string`
- Default Value: `None`



### Properties

Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line.

- ID: `properties`
- Datatype: `string`
- Default Value: `None`



### Charset

The file encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`





## Advanced Parameter

`None`