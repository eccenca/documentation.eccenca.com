---
title: "Parquet"
description: "Read from or write to an Apache Parquet file."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Parquet
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Parquet Dataset

The Parquet dataset plugin in BUILD provides the ability to read from or write to Apache Parquet files. It is a **Spark-optimized dataset**, designed to leverage Spark’s in-memory, parallel execution model and take advantage of Parquet-specific optimizations.

Parquet supports optimizations such as **column pruning** and **predicate pushdown**, which enable Spark to read only the required columns or rows. This makes Parquet particularly effective for workflows where selective access to data is needed, improving performance for large-scale transformations.
### Key Features

- **Columnar storage format**: Parquet stores data in a column-oriented manner, enabling efficient compression and retrieval of individual columns.
- **Partitioning**: Optional support for partitioned outputs, allowing Spark to parallelize data processing effectively.
- **Compression**: Supports multiple compression algorithms, e.g., Snappy, Gzip, or LZO, reducing storage footprint and improving I/O performance.
- **Schema handling**: Supports explicit or inferred schemas, with the schema applied to the dataset as a whole, not individual rows.
### Example

A Parquet dataset in CMEM Build might look conceptually like this:

| transaction_id | customer_id | amount | timestamp          |
|----------------|-------------|--------|------------------|
| 1              | 1001        | 150.00 | 2025-11-01 08:15 |
| 2              | 1002        | 200.50 | 2025-11-01 09:30 |
| 3              | 1003        | 75.25  | 2025-11-01 11:20 |

This dataset could be stored in a file `transactions.parquet` and used in workflows where only certain columns or filtered rows are needed. Spark can read only the relevant columns or rows matching a condition, thanks to Parquet’s **column pruning** and **predicate pushdown** optimizations, making transformations efficient even at large scale.
### Reference

For more information on the Parquet format and its optimizations, see the [Apache Parquet project page](https://parquet.apache.org/).

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

Path (e.g. relative like 'path/filename.orc' or absolute 'hdfs:///path/filename.parquet').

- ID: `file`
- Datatype: `resource`
- Default Value: `None`



### Uri pattern

A pattern used to construct the entity URI. If not provided the prefix + the line number is used. An example of such a pattern is 'urn:zyx:{id}' where *id* is a name of a property.

- ID: `uriPattern`
- Datatype: `string`
- Default Value: `None`



### Properties

Comma-separated list of URL-encoded properties. If not provided, the list of properties is read from the first line.

- ID: `properties`
- Datatype: `string`
- Default Value: `None`



### Partition

Optional specification of the attribute for output partitioning

- ID: `partition`
- Datatype: `string`
- Default Value: `None`



### Compression

Optional compression algorithm (e.g. snappy, zlib)

- ID: `compression`
- Datatype: `string`
- Default Value: `None`



### Charset

The file encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`





## Advanced Parameter

`None`