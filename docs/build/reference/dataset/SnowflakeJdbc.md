---
title: "Snowflake JDBC endpoint"
description: "Connect to Snowflake JDBC endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Snowflake JDBC endpoint
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



This dataset supports connections to the Snowflake JDBC endpoint.

#### <a id="parameter_doc_connection-host">Account URL hostname</a>

The supplied account URL hostname needs to contain the account identifier. Refer to the Snowflake documentation on [account identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier) for details.

#### Reading

Either a table or a queries can be specified to retrieve data from Snowflake.

Read strategies decide how the database is queried:

- **full-table**: Queries or wraps a complete table.
  Only the table name need to be set.
- **query**: The given source query is passed to the database.
  The table name is not necessary in this case but a valid query must be provided.

#### Writing

When the dataset is used as a sink, queries are ignored and only schema and table parameters are used.
If the dataset is used as a sink for a hierarchical mapping, one table is created per entity type.

Write strategies decide how a new table is written:

- **default**: An error will occur if the table exists.
  If not a new one will be created.
- **overwrite**: The old table will be removed and a new one will be created.
- **append**: Data will be appended to the existing table.
  The schema of the data written has to be the same as the existing table schema.

The names of the written tables are generated as follows:

- The table name of the root mapping is defined by the table parameter of the dataset.
  If the table name is empty, a name is generated from the first type of the mapping.
  Special characters are removed and the name is truncated to a maximum of 128 characters.
- For each object mapping, the table name is generated from its type.


## Parameter

### Connection

Connection parameters

- Datatype: `objectParameter`
- Default Value: `{'parameters': {'database': '', 'privateKeyPassword': '', 'host': '<orgname>-<account_name>.snowflakecomputing.com', 'privateKey': '', 'user': '', 'schema': '', 'port': '443', 'warehouse': '', 'table': '', 'password': '', 'additionalParameters': ''}}`


#### Account URL hostname

The hostname which is used for the connection. Usually, this is something like '<orgname>-<account_name>.snowflakecomputing.com'

- Datatype: `string`
- Default Value: `<orgname>-<account_name>.snowflakecomputing.com`


#### Port

HTTP port

- Datatype: `int`
- Default Value: `443`


#### User

Username

- Datatype: `string`
- Default Value: `None`


#### Password

Password for basic authentication. Leave empty if key-pair authentication should be used.

- Datatype: `password`
- Default Value: `None`


#### Private key

The private key for the specified user. Leave empty if basic password authentication should be used.

- Datatype: `password`
- Default Value: `None`


#### Private key password

Password for encrypted private keys. Can be left empty if using an unencrypted key.

- Datatype: `password`
- Default Value: `None`


#### Additional parameters

Additional JDBC connection parameters. A map of the form 'Key1:Value1,Key2:Value2, where keys and values are URL encoded.

- Datatype: `stringmap`
- Default Value: `None`


#### Warehouse

Warehouse

- Datatype: `string`
- Default Value: `None`


#### Database

Database

- Datatype: `string`
- Default Value: `None`


#### Schema

Schema

- Datatype: `string`
- Default Value: `None`


#### Table

Table name. Can be empty if the read-strategy is not set to read the full table.

- Datatype: `string`
- Default Value: `None`



### Read

Parameters related to reading from the database.

- Datatype: `objectParameter`
- Default Value: `{'parameters': {'queryStrategy': 'access-complete-table', 'restriction': '', 'groupBy': '', 'orderBy': '', 'sourceQuery': '', 'limit': '10'}}`


#### Source query

Source query (e.g. 'SELECT TOP 10 * FROM table WHERE x = true'. Can be left empty when full tables are loaded. Note: Even if columns with spaces/special characters are named in the query, they need to be referred to URL-encoded in subsequent transformations.

- Datatype: `code-sql`
- Default Value: `None`


#### Group by

Comma separated list of attributes appearing in the outer SELECT clause that should be grouped by. The attributes are matched case-insensitive. All other attributes will be grouped via an aggregation function that depends on the supported DBMS, e.g. (JSON) array aggregation.

- Datatype: `string`
- Default Value: `None`


#### Order by

Optional column to sort the result set.

- Datatype: `string`
- Default Value: `None`


#### Limit

Optional limit of returned records. This limit should be pushed to the source. No value implies that no limit will be applied.

- Datatype: `option[int]`
- Default Value: `10`


#### Query strategy

The strategy decides how the source system is queried.

- Datatype: `enumeration`
- Default Value: `access-complete-table`


#### Restriction

An SQL WHERE clause to filter the records to be retrieved.

- Datatype: `string`
- Default Value: `None`



### Write

Parameters related to writing to the database.

- Datatype: `objectParameter`
- Default Value: `{'parameters': {'writeStrategy': 'default', 'multipleValuesStrategy': 'concatenateValuesStrategy'}}`


#### Write strategy

If this dataset is written to, it can be selected if data is overwritten or appended.'

- Datatype: `enumeration`
- Default Value: `default`


#### Multiple values strategy

How multiple values per entity property are written.

- Datatype: `enumeration`
- Default Value: `concatenateValuesStrategy`



### Query execution

Query execution parameters.

- Datatype: `objectParameter`
- Default Value: `{'parameters': {'retries': '0', 'pause': '2000'}}`


#### Retries

Optional number of retries per query

- Datatype: `int`
- Default Value: `0`


#### Pause

Optional pause between queries in ms.

- Datatype: `int`
- Default Value: `2000`



