---
icon: simple/apachespark
tags:
    - Introduction
    - Explainer
---
# Apache Spark within Corporate Memory Build

## Introduction

This documentation provides an overview of Apache Spark and its integration within Corporate Memory’s Build component.
The goal is to provide a conceptual understanding of Spark, its purpose in Build, and how workflows leverage Spark-aware datasets for efficient, distributed data processing.

The documentation is structured in two parts:

1. What is Apache Spark?
2. Apache Spark within Build

## What is Apache Spark?

The main data processing use-cases of Apache Spark are:

* data loading,
* SQL queries,
* machine learning,
* streaming,
* graph processing.

Additionally, there are other functionalities stemming from hundreds of plugins.

By itself, Apache Spark is detached from any data and Input/Output (IO) operations.
Within Corporate Memory, the relevant configuration is documented in the [Spark configuration](../../deploy-and-configure/configuration/dataintegration/index.md#spark-configuration).

## Apache Spark within Build

### Why is Apache Spark used in Corporate Memory?

Apache Spark is integrated into Corporate Memory to enable scalable, distributed execution of data integration workflows within its Build component.
While Corporate Memory’s overall architecture already consists of multiple distributed services (e.g. Build for data integration, Explore for knowledge graph management), the execution of workflows in Build is typically centralized.
Spark adds a **parallel, fault-tolerant computation layer** that becomes especially valuable when workflows process large, complex, or computation-heavy datasets.

The rationale behind using Spark aligns with its general strengths:

- **Parallelization and scalability** for high-volume transformations and joins.
- **Fault tolerance** through resilient distributed datasets (RDDs).
- **Optimization** via Spark’s DAG-based execution planner, minimizing data movement.
- **Interoperability** with widely used big data formats (Parquet, ORC, Avro).

By leveraging Spark, Corporate Memory can handle data integration workflows that would otherwise be constrained by processing limits, while maintaining compatibility with its semantic and knowledge-graph-oriented ecosystem.
However, since Spark support is optional, its usage depends on specific deployment needs and data volumes.

### How and where is Apache Spark used by Build?

Within the Build component, Apache Spark is used exclusively for executing workflows that involve **Spark-aware datasets**.
These workflows connect datasets, apply transformations, and produce outputs, with Spark that handles large volumes of data and complex computations efficiently.

For other dataset types (e.g. smaller relational sources or local files), Spark execution provides no significant advantage and is not typically used.
In such cases, Build’s standard local execution engine is sufficient.
Spark thus acts as an optional, performance-oriented backend, not as a replacement for the standard workflow engine.

Each Spark-aware dataset corresponds to an **executor-aware entity**.
During workflow execution, Build translates the **workflow graph** into Spark jobs, where datasets become RDDs or DataFrames, transformations become stages, and Spark orchestrates execution across the cluster.
The results are then materialized or written back into Corporate Memory’s storage layer, ready for subsequent workflow steps or integration into the knowledge graph.

### Types of Spark-aware datasets

The main types of Spark-aware datasets include:

- **Avro datasets** — columnar, self-describing file format optimized for Spark’s in-memory processing.
- **Parquet datasets** — highly efficient columnar storage format that supports predicate pushdown and column pruning.
- **ORC datasets** — optimized row-columnar format commonly used in Hadoop ecosystems, enabling fast scans and compression.
- **Hive tables** — structured tables stored in Hadoop-compatible formats, which can be queried and transformed via Spark seamlessly.
- **HDFS datasets** — file-based, row-oriented datasets stored in Hadoop Distributed File System, optimized for partitioned, parallel processing.
- **JSON datasets** — semi-structured, Spark-aware datasets enabling flexible schema inference and in-memory transformations.
- **JDBC datasets** — external relational sources exposed to Spark via JDBC, queryable and transformable as DataFrames.
- **Embedded SQL Endpoint** — workflow results published as virtual SQL tables, queryable via JDBC or ODBC without persistent storage, optionally cached in memory.

### What is the relation between Build’s Spark-aware workflows and the Knowledge Graph?

The Spark-aware workflows operate on datasets within Build, executing transformations and producing outputs.
The Knowledge Graph, managed by Explore, serves as the persistent semantic storage layer, but Spark itself does not directly interact with the graph.
Instead, the **workflow execution engine** orchestrates the movement of data between Spark-aware datasets and the Knowledge Graph, ensuring that transformations are applied in the correct sequence and that results are persisted appropriately.

This separation of concerns allows Spark to focus on high-performance computation without being constrained by the architecture or APIs of the Knowledge Graph, or the rest of Corporate Memory’s architecture around it.
Data can flow into workflows from various sources and ultimately be integrated into the graph, while the execution engine mediates this process, handling dependencies, scheduling, and parallelism.

### What is the relation between Spark-aware dataset plugins and other Build plugins?

Spark-aware dataset plugins are a specialized subset of dataset plugins that integrate seamlessly into Build workflows.
They implement the same source-and-sink interfaces as all other plugins, allowing workflows to connect Spark-aware datasets, traditional datasets, and transformations.

These plugins also cover JSON and JDBC sources, providing consistent behavior and integration across a wide range of data types and endpoints.
Spark-aware plugins can be combined with any other plugin in a workflow, with the execution engine automatically leveraging Spark where beneficial.
