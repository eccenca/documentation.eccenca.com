---
title: "Hive database"
description: "Read from or write to an embedded Apache Hive endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Hive database
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## Hive Dataset

Within BUILD, several Spark-aware datasets exist — Avro, Parquet, ORC, HDFS, and Hive — each optimized to leverage Spark’s parallel, in-memory execution. Among these, Hive datasets provide **structured table-based storage**, complementing file-based formats with queryable relational tables. Hive tables enable BUILD to query and process large datasets while taking full advantage of Spark’s distributed, in-memory execution model.

The Hive dataset plugin in BUILD allows workflows to **read from and write to Hive tables** seamlessly. Conceptually, Hive represents the table-oriented, relational side of CMEM’s Spark-aware ecosystem, bridging raw storage formats and semantic integration into the Knowledge Graph. It is **table-based**, meaning that workflows can apply **SQL filtering and projection**, leverage **partitioning**, and construct **entity URIs** for downstream knowledge-graph alignment — all without manual management of Spark execution details. Hive thus complements other Spark-aware datasets, which are typically file-based (columnar or row-oriented), by providing **structured, queryable, relational entities**.

### Key Features

- **Database and table mapping** – Workflows target specific Hive databases and tables, with explicit schema definitions.
- **SQL query support** – Optional queries allow pre-filtering of rows and columns before processing.
- **Entity URI construction** – Configurable patterns enable semantic alignment with the Knowledge Graph.
- **Property handling** – Properties can be specified explicitly or inferred from table schema.
- **Partitioning** – Native Hive partitions are recognized and used by Spark for parallelized processing.
- **Encoding support** – Handles various source encodings for table content.
- **Parallelized, memory-efficient execution** – Spark manages intermediate data in-memory across partitions, while maintaining fault tolerance.

### Conceptual Usage in Workflows

Hive datasets are best understood **in the context of CMEM’s Spark-aware dataset ecosystem**:

- They allow **structured ingestion and transformation** of relational datasets.
- Filters or projections via SQL minimize unnecessary data movement.
- Entity URIs and property mapping ensure **semantic continuity** into the Knowledge Graph.
- Hive tables complement file-based datasets by offering **queryable, relational views**, which can be combined in workflows with Parquet, ORC, Avro, or HDFS sources.

In short, Hive tables are the **relational, table-oriented pillar** of Spark-aware datasets within BUILD. While Spark mechanics like lazy evaluation, DAG planning, and RDD lineage underpin all datasets, they **do not need to be repeated here** — Hive’s value lies in its **integration, structured storage, and semantic alignment**.

### Example: Ingesting a Hive Table into BUILD

A typical Hive dataset configuration might reference a structured table exposed in a Hive warehouse. For instance:

- **Schema:** `sales_data`
- **Table:** `monthly_transactions`
- **Query (optional):** `SELECT * FROM monthly_transactions WHERE year = 2024`
- **URI pattern:** `urn:transaction:{id}`
- **Properties:** (optional) auto-detected if not provided
- **Charset:** `UTF-8`

This configuration allows BUILD to load the table as a Spark DataFrame, apply transformations or entity extraction workflows, and integrate the resulting entities into the Knowledge Graph. Filtering via an optional SQL query supports focused processing without materializing the entire table.

### Comparison to Other Spark-Aware Datasets in CMEM

| Aspect | Hive | Other Spark-Aware Datasets (Avro, Parquet, ORC, HDFS) |
|--------|------|------------------------------------------------------|
| Storage model | Table-based, relational | File-based: columnar (Parquet, ORC) or row-oriented (Avro, HDFS) |
| Spark optimization | In-memory, partition-parallel execution | In-memory for columnar; row-oriented formats support streaming or batch processing |
| Schema | Explicit from Hive table | Columnar: explicit/inferred; row-oriented: schema required |
| Filtering / Projection | SQL queries, table partition pruning | Columnar: column pruning/predicate pushdown; row-based: limited |
| Partitioning | Native Hive partitions, used for parallelism | Optional file-level partitions or directory-based sharding |
| Compression | Configurable at table level | Columnar: Snappy/Gzip; row: Snappy/Deflate |
| Typical usage | Structured, large-scale tables integrated into CMEM pipelines | File-based analytics, ETL, streaming ingestion, or intermediate workflow steps |
| Semantic integration | Direct mapping to entity URIs and Knowledge Graph properties | Generally less semantic, focus on raw transformation or analytics |
| Best CMEM use case | Large, structured datasets requiring filtering, projections, and semantic KG alignment | Flexible ingestion and processing, format-specific performance optimization |


## Parameter

### Schema

Name of the hive schema or namespace.

- ID: `schema`
- Datatype: `string`
- Default Value: `None`



### Table

Name of the hive table.

- ID: `table`
- Datatype: `string`
- Default Value: `None`



### Query

Optional query for projection and selection, e.g. "SELECT * FROM table WHERE x = true".

- ID: `query`
- Datatype: `string`
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



### Charset

The source internal encoding, e.g., UTF8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`





## Advanced Parameter

`None`