---
icon: simple/apachespark
tags:
    - Introduction
    - Explainer
---
# Apache Spark within CMEM BUILD

## Introduction

This documentation provides a detailed explanation of Apache Spark and its integration within eccenca’s Corporate Memory (CMEM) BUILD platform. The goal is to provide a conceptual understanding of Spark, its purpose in BUILD, and how workflows leverage Spark-aware datasets for efficient, distributed data processing.

The documentation is structured in three parts:

1. What Apache Spark is
2. How Apache Spark works
3. How Apache Spark is used in CMEM

## What is Apache Spark?

[Apache Spark](https://spark.apache.org/) is a unified **computing engine** and set of libraries for **distributed data processing** at scale. It is specifically used in the domains of data engineering, data science, and machine learning.

The main data processing use-cases of Apache Spark are:

* data loading
* SQL queries
* machine learning
* streaming
* graph processing
* etc. (functionalities stemming from hundreds of plugins)

By itself, Apache Spark is detached from any data and Input/Output (IO) operations. More formally: Apache Spark requires a [cluster manager](https://en.wikipedia.org/wiki/Cluster_manager "Cluster manager") and a [distributed storage system](https://en.wikipedia.org/wiki/Clustered_file_system "Clustered file system"). One possible realization of these requirements, for the distributed storage part, is to combine Apache Spark with [Apache Hive](https://hive.apache.org/) ―a distributed data warehouse―. For the cluster management part, there are also several possibilities, as can be explored in the [cluster mode overview documentation](https://spark.apache.org/docs/latest/cluster-overview.html). One such possibility ―and the one we recommend― is to use [Apache Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html). YARN handles the resource management and the _job scheduling_ within the cluster. The connection point between YARN and Spark can be explored [here](https://spark.apache.org/docs/latest/running-on-yarn.html) further. More specifically, within eccenca's Corporate Memory (CMEM) environment, the relevant configuration is documented in the [Spark configuration](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/dataintegration/#spark-configuration) of eccenca BUILD.

## How does Spark work?

### Spark's Architecture

There are ―in general terms― _three_ different layers or levels of abstraction within Spark:

* the **low-level APIs**: RDDs (resilient distributed datasets), shared variables
* the **high-level APIs**: DataFrames, Datasets, SparkSQL
* the **application level**: (Structured) Streaming, MLib, GraphX, etc.

#### Low-level API

At the lowest abstraction level, Spark provides the abstraction of a **resilient distributed dataset**, an [RDD](https://spark.apache.org/docs/latest/rdd-programming-guide.html). As stated, Spark is detached from any data and IO operations, and the abstraction of the RDD embodies this exact principle. In practice, the most common physical source of data for an RDD is a file in a Hadoop file system, the [HDFS](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs) (Hadoop Distributed File System).

Conceptually, it is important to be aware of the following distinction: Apache Spark does in-memory computations. Hadoop handles the distributed files, and Spark the distributed processing. Spark, YARN and HDFS have therefore orthogonal but cohesive concerns: computation, scheduling, persistence.

Additionally to the in-memory aspect of computations with RDDs, the RDD itself is **immutable**. This is an established practice in functional programming ―which inspired the core processing functionalities and mechanisms of systems such as Spark and Hadoop―, especially in the context of parallel processing and distributed computing. Immutability does _not_ imply that the processing of data structures is inefficient compared to working with mutable data, since [persistent data structures](https://en.wikipedia.org/wiki/Persistent_data_structure) are used. That said, evidently each type of datastructure has its use-cases and trade-offs.

Spark can be seen as bridging distributed computing paradigms. [Hadoop](https://hadoop.apache.org/) and its MapReduce operate on disk-based storage, processing data in batches. Spark shifts computation into memory and treats data as immutable, enabling stateless transformations across partitions. [Flink](https://flink.apache.org/) goes further by supporting stateful, continuously updated computations, suited for complex streaming workloads.

#### High-level API

The basis for in-memory computations in Spark is, thus, the RDD. As such, the RDD is the central abstraction in Spark for the concept of _distributed data_. The chronological development of Spark's APIs also reflects this: The RDD was introduced in 2011, then in 2013 and 2015 two higher-level abstractions were introduced, each building upon the previous. These two abstractions are the DataFrame (2013) and the Dataset (2015). The main difference is the following:

* A **Dataset** is a _strongly-typed_ distributed collection of data.
* A **DataFrame** is a _weakly-typed_ distributed collection of data.

Technically speaking, a DataFrame is nothing else than a **dataset of rows**. Here, a row is to be understood in the same sense as in the rows of a relational database table. Conceptually, the main difference is that a Dataset "knows" which types of objects it stores or contains, whereas a DataFrame doesn't.

In our case, the relevant abstractions are the RDD and the DataFrame. In a general, domain-agnostic data integration system such as eccenca CMEM, there is no use-case for a strongly-typed version of a distributed collection of data (that would require knowledge of the application and business domains, integrated into CMEM itself). In other words: The usage of DataFrames aligns perfectly with the general, flexible and dynamic data integration tasks of CMEM and the corresponding workflow execution, of which Spark is an optional but optimal part.

##### DataFrames

###### What a DataFrame Really Is

A DataFrame is a high-level abstraction over an RDD, combining a distributed dataset with a **schema**. The schema defines column names, data types, and the structure of fields. Notice that a schema is applied to DataFrames, not to rows; each row is itself untyped.

###### How DataFrames Work

A DataFrame combines a schema (structure) with a distributed dataset (content). It is **immutable**: transformations always produce new DataFrames without changing the original. Spark tracks lineage, the history of transformations, which allows lost partitions to be recomputed safely. DataFrames are partitioned across the cluster, enabling parallel processing. Together, these properties make DataFrames reliable and efficient for data integration workflows in CMEM.

###### Computing DataFrames

Operations on DataFrames are **lazy**. Transformations define what to do; computation happens only when an action (e.g., collect, write) is triggered. This ensures efficient computation, preserves immutability, and keeps integration workflows flexible.

###### Data Sources

DataFrames can be created from files (CSV, JSON, Parquet, ORC), databases (via JDBC), or existing RDDs with an applied schema. Schemas can be provided or inferred dynamically. Writing supports multiple modes (overwrite, append), enabling consistent handling of distributed datasets in CMEM Build.

#### Application level

At the application level, Apache Spark provides further abstractions and functionalities such as structured streaming, machine learning and (in-memory) graph processing with GraphX. These are interesting to know about, but they are not relevant for the integration of Apache Spark within eccenca CMEM.

In other words, and metaphorically speaking: The application level is CMEM itself, which makes use of Spark. This brings us to the follow-up questions regarding the usage of Spark _within_ Corporate Memory, which are described further below.

### Anatomy of a Spark job

A Spark job consists of stages, tasks, shuffles, and the DAG. These elements define how computations are divided and executed across the cluster.

* A **job** consists of stages, each containing multiple tasks, which are the units of computation executed per partition.
* A **stage** represents a set of computations that can run without shuffling data across nodes.
* A **shuffle** is the exchange of data between nodes, required when a stage depends on data from another stage.
* The **DAG** (directed acyclic graph) captures all dependencies between RDDs, allowing Spark to plan and optimize execution efficiently.

This structure — jobs divided into stages and tasks, connected through the DAG and occasionally requiring shuffles — allows Spark to schedule work efficiently, parallelize computation across the cluster, and recover lost partitions if a node fails. Spark’s DAG-based planning also enables optimizations, such as minimizing data movement, which improves performance in workflows that combine multiple transformations and actions.

## Apache Spark within CMEM BUILD

### Why is Apache Spark used by eccenca’s CMEM?

Apache Spark is integrated into CMEM to enable scalable, distributed execution of data integration workflows within its BUILD component. While CMEM’s overall architecture already consists of multiple distributed services (e.g. BUILD for data integration, EXPLORE for knowledge graph management), the execution of workflows in BUILD is typically centralized. Spark adds a **parallel, fault-tolerant computation layer** that becomes especially valuable when workflows process large, complex, or computation-heavy datasets.

In practical terms, Spark is used only in BUILD — not in EXPLORE or other components. Its purpose is to accelerate workflow execution for the so-called **Spark-aware datasets**, which include file formats and storage systems such as Avro, Parquet, ORC, Hive, and HDFS. These formats map naturally to Spark’s distributed processing model and benefit from in-memory execution and partition-based parallelism.

For other dataset types (e.g. smaller relational sources or local files), Spark execution provides no significant advantage and is not typically used. In such cases, BUILD’s standard local execution engine is sufficient. Spark thus acts as an optional, performance-oriented backend, not as a replacement for the standard workflow engine.

The rationale behind using Spark in BUILD aligns with its general strengths:

- **Parallelization and scalability** for high-volume transformations and joins.
- **Fault tolerance** through resilient distributed datasets (RDDs).
- **Optimization** via Spark’s DAG-based execution planner, minimizing data movement.
- **Interoperability** with widely used big data formats (Parquet, ORC, Avro).

By leveraging Spark, CMEM can handle data integration workflows that would otherwise be constrained by single-node processing limits, while maintaining compatibility with its semantic and knowledge-graph-oriented ecosystem. However, since Spark support is optional, its usage depends on specific deployment needs and data volumes.

### How and where is Apache Spark used by BUILD?

Within the BUILD stage, Apache Spark is used exclusively for executing workflows that involve Spark-optimized datasets. These workflows connect datasets, apply transformations, and produce outputs, with Spark providing a distributed, in-memory execution engine that handles large volumes of data and complex computations efficiently.

The Spark-optimized datasets — such as Avro datasets, Parquet datasets, ORC datasets, and Hive tables — are designed to leverage Spark’s architecture. When included in a workflow, Spark performs transformations in parallel across partitions and keeps data in memory whenever possible. Other datasets can participate in workflows but typically do not benefit from Spark’s parallel execution optimizations.

Optionally, for more technical context: each Spark-optimized dataset corresponds to an executor-aware entity. During workflow execution, BUILD translates the workflow graph into Spark jobs, where datasets become RDDs or DataFrames, transformations become stages, and Spark orchestrates execution across the cluster. The results are then materialized or written back into CMEM’s storage layer, ready for subsequent workflow steps or integration into the knowledge graph. Users do not need to manage executors or partitions manually.

### What are the Spark-optimized datasets?

In BUILD, Spark-optimized datasets are those data sources designed to fully leverage Spark’s distributed, in-memory execution engine. These datasets are structured to enable parallelized transformations, efficient partitioning, and integration into workflows without requiring manual management of computation or storage.

The main types of Spark-optimized datasets include:

- Avro datasets — columnar, self-describing file format optimized for Spark’s in-memory processing.
- Parquet datasets — highly efficient columnar storage format that supports predicate pushdown and column pruning.
- ORC datasets — optimized row-columnar format commonly used in Hadoop ecosystems, enabling fast scans and compression.
- Hive tables — structured tables stored in Hadoop-compatible formats, which can be queried and transformed via Spark seamlessly.
- HDFS datasets — file-based, row-oriented datasets stored in Hadoop Distributed File System, optimized for partitioned, parallel processing.
- JSON datasets — semi-structured, Spark-aware datasets enabling flexible schema inference and in-memory transformations.
- JDBC / relational datasets — external relational sources exposed to Spark via JDBC, queryable and transformable as DataFrames.
- Embedded SQL Endpoint — workflow results published as virtual SQL tables, queryable via JDBC/ODBC without persistent storage, optionally cached in memory.

When a workflow includes any of these datasets, Spark executes transformations in parallel across partitions and keeps intermediate results in memory whenever possible, accelerating performance for complex or large-scale data integration tasks.

Other datasets in BUILD (e.g., relational sources, local files, or non-Spark-aware formats) can participate in workflows, but they do not benefit from Spark’s parallel execution. Spark execution remains optional, used only when performance gains are meaningful or when workflow complexity demands distributed processing.

### What is the relation between BUILD’s Spark-aware workflows and the Knowledge Graph?

BUILD’s Spark-aware workflows operate on datasets within BUILD, executing transformations and producing outputs in a distributed, in-memory manner. The Knowledge Graph, managed by EXPLORE, serves as the persistent semantic storage layer, but Spark itself does not directly interact with the graph. Instead, the **workflow execution engine** orchestrates the movement of data between Spark-aware datasets and the Knowledge Graph, ensuring that transformations are applied in the correct sequence and that results are persisted appropriately.

This separation of concerns allows Spark to focus on high-performance computation without being constrained by the architecture or APIs of the Knowledge Graph, or the rest of CMEM's architecture around it. Data can flow into workflows from various sources and ultimately be integrated into the graph, but the execution engine mediates this process, handling dependencies, scheduling, and parallelism. Users benefit from the efficiency of Spark while maintaining the integrity and consistency of the graph as the central repository of integrated knowledge.

From a conceptual perspective, the relation is therefore indirect but essential: Spark-aware workflows accelerate the processing of large or complex datasets, while the Knowledge Graph ensures that the processed data is semantically harmonized and persistently stored. Together, they enable CMEM to combine flexible, distributed computation with knowledge-centric integration, supporting a wide range of enterprise data integration use cases without requiring users to manage low-level execution details.

### What is the relation between Spark-aware dataset plugins and other BUILD plugins?

Spark-aware dataset plugins are a specialized subset of dataset plugins that integrate seamlessly into BUILD workflows. They implement the same source-and-sink interfaces as all other plugins, allowing workflows to connect Spark-aware datasets, traditional datasets, and transformations without additional configuration.

These plugins include not only the core Spark-optimized datasets (Avro, Parquet, ORC, Hive, HDFS) but also other Spark-aware plugins such as JSON and JDBC sources, providing consistent behavior and integration across a wide range of data types and endpoints. Spark-aware plugins can be combined with any other plugin in a workflow, with the execution engine automatically leveraging Spark where beneficial, so users do not need to manage parallelism or execution details themselves.

The execution engine coordinates all plugins, orchestrating Spark-based processing where appropriate while ensuring overall workflow consistency and integration with CMEM’s storage layer. Certain optimizations, like lazy evaluation and optional caching, exist internally to improve performance, though users interact with the workflows in the same unified interface as with other datasets.
