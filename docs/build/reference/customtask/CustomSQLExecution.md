---
title: "Spark SQL query"
description: "Executes a Spark SQL query on the input entities and returns the result as its output."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
---

# Spark SQL query

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The Spark SQL query operator runs a [Spark SQL](https://spark.apache.org/docs/latest/sql-ref.html) query against the
entities of its single input and passes the query result to the next workflow task.

The operator requires the Spark execution backend (`execution.manager.plugin = SparkExecutionManager`). In local
workflow execution the task fails because no executor is available for it.

## Command

<a id="parameter_doc_command"></a>
The **Command** parameter holds the SQL query. The input entities are made available as a table named `dataset`,
regardless of which task is connected to the input. Each column holds all values of its path as an array of strings,
since an entity can have several values per path. Use `try_element_at(column, 1)` to read the first value, which
returns NULL if the entity has no value, and cast it to compare it as a number. For example, this query keeps the
entities whose first `age` value is above 30 and returns two of their columns:

```sql
SELECT try_element_at(name, 1) AS name, try_element_at(age, 1) AS age
FROM dataset
WHERE try_cast(try_element_at(age, 1) AS INT) > 30
```

The columns hold plain strings instead of arrays if the configuration option `spark.interpreter.options.columnType`
is set to any value other than `sequence`.

The columns of the `dataset` table are named after the paths of the input schema: the column headers of a CSV file or
the full property URIs of RDF data. Enclose a column name in backticks when it contains characters that are not valid
in an SQL identifier, such as a URI:

```sql
SELECT `http://xmlns.com/foaf/0.1/name` AS name FROM dataset
```

The entity URIs of the input are not part of the table and cannot be referenced in the query.

The table name is applied by a case-sensitive text replacement: every occurrence of the character sequence `dataset` in
the query is replaced with the internal name of the input table, also inside longer names such as `my_dataset` or inside
a URI, while `DATASET` or `Dataset` is left unchanged. Write the table name in lower case and make sure that column names,
aliases and string literals in the query do not contain `dataset`.

## Output

The columns of the query result become the paths of the output schema, in the order the query returns them. A column
name that is not valid in a URI, e.g. an alias containing spaces, is URL-encoded in the path, so prefer plain
alphanumeric aliases. The output schema declares all result values as strings and keeps the type of the input entities.
Connect a dataset or another operator to the output to use the result.



## Parameter

### Command

SQL command. The name of the table in the statement must be 'dataset', regardless of the input.

- ID: `command`
- Datatype: `code-sql`
- Default Value: `None`

## Advanced Parameter

`None`
