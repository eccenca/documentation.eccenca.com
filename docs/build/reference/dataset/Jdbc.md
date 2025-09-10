---
title: "JDBC endpoint"
description: "Connect to an existing JDBC endpoint."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# JDBC endpoint
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



## General usage

The JDBC dataset supports connections to Hive, Microsoft SQL Server, MySQL, MariaDB, SnowFlake, Oracle Database, DB2 and PostgreSQL databases.
A login, password and JDBC URL need to be provided.
This dataset supports queries or simply schema and table names to define what to retrieve from a source DB.
When the dataset is used as a sink, queries are ignored and only schema and table parameters are used.
If the dataset is used as a sink for a hierarchical mapping, it behaves similarly to the SqlEndpoint: One table is created per entity type.

The names of the written tables are generated as follows:

- The table name of the root mapping is defined by the table parameter of the dataset.
  If the table name is empty, a name is generated from the first type of the mapping.
  Special characters are removed and the name is truncated to a maximum of 128 characters.
- For each object mapping, the table name is generated from its type.

## JDBC Connection Strings/URLs

Most of the dataset parameters are passed directly to the driver.
Please make sure that you use the correct syntax for each DBMS, otherwise you may get unintuitive errors.

Here are templates for supported database systems:
```
oracle (external driver needed): 
jdbc:oracle:thin:@{host}[:{port}]/{database}

postgres (integrated): 
jdbc:postgresql://{host}[:{port}]/[{database}]

MySQL/MariaDB (integrated): 
jdbc:{mariadb}://{host}[:{port}]/[{database}]

SnowSQL (external driver needed): 
jdbc:snowflake://{AWSAccount}.{AWS region}.snowflakecomputing.com?db={database}&schema={schema}

MSSqlServer (integrated): 
jdbc:sqlserver://{host}[:{port}];databaseName={database}

DB2 (external driver needed):
jdbc:db2//{host}[:{port}]/{database}

Trino (external driver needed)
jdbc:trino//{host}:8080/catalog/schema
```

## Read and write strategies

There are multiple read and write strategies which can be selected depending on the purpose of the dataset in a workflow.

Read strategies decide how the database is queried:

- **full-table**: Queries or wraps a complete table.
  Only the DB schema and table name need to be set.
- **query**: The given source query is passed to the database.
  The table name is not necessary in this case but a valid query in the SQL-dialect of the source database system must be provided.

Write strategies decide how a new table is written:

- **default**: An error will occur if the table exists.
  If not a new one will be created.
- **overwrite**: The old table will be removed and a new one will be created.
- **append**: Data will be appended to the existing table.
  The schema of the data written has to be the same as the existing table schema.

## Optimized Writing

Usually specific database systems have custom commands for loading large amounts of data, e.g. from a CSV file into a database table.
For some DBMS and specific JDBC dataset configurations we support these optimized methods of loading data.

Supported DBMS:

- MySQL and MariaDB (full support for versions 8.0.19+ and 10.4+, resp.):
  - if older DBMS versions are used some dataset options like 'groupBy' might not be supported but equivalent queries will
  - the same is true when older driver jars then the one provided by eccenca are used
  - both use the MariaDB JDBC driver
  - uses `LOAD DATA LOCAL INFILE` internally
  - only applies when appending data to an existing table and having `Force Spark Execution` disabled
  - Both the server parameter `local_infile` and the client parameter `allowLoadLocalInfile` must be enabled, e.g. by adding `allowLoadLocalInfile=true` to the JDBC URL.
    For MySQL starting with version 8 the `local_infile` parameter is by default disabled!
  - If during writing to a MySQL/MariaDB a `[…] You have an error in your SQL syntax […]` error is encountered make sure ANSIquotes are used.
    `sql_mode=ANSI_QUOTES` can be set via a URL parameter to the JDBC connection string like:

    ```sh
    # MySQL
    jdbc:mysql://<host>:<port, eg. 3306>/<database>?sessionVariables=sql_mode=ANSI_QUOTES

    # MariaDB
    jdbc:mariadb://<host>:<port, eg. 3306>/<database>?sessionVariables=sql_mode=ANSI_QUOTES
    ```

## Registering JDBC drivers

More 3rd party databases are supported via adding their JDBC drivers to the classpath of Data Integration.
Drivers are usually provided by the database manufactures.
If 32 bit and 64 bit versions are provided the latter is usually needed and should aways equal the bit-level of the JVM.
To make sure that the drivers are loaded correctly, their class name (in case are jar contains multiple drivers) and location in the file system can be set with the `spark.sql.options.jdbc` option in the `dataintegration.conf` configuration file.

An example for adding both the DB2 and MySQL drivers to the Data Integration configuration file `spark.sql.options.*` section:

```raml
spark.sql.options {
  …

  # List of database identifiers to specify user provided JDBC drivers. The second part of the protocol of a JDBC URI (e.g. db2 from
  # jdbc:db2://host:port)  is used to specify the driver. For each protocol on the list a jar classname and optional download
  # location can be provided.
  jdbc.drivers = "db2,mysql"
  
  # Some database systems use licenses that are to loose or restrictive for us to ship the drivers. Therefore a path
  # to a jar file containing the driver and the name of driver can be specified here.
  jdbc.db2.jar = "/home/user/Jars/db2jcc-db2jcc4.jar"
  jdbc.mysql.jar = "/home/user/drivers/mysql.jar"

  # Name of the actual driver class for each db
  jdbc.db2.name = "com.ibm.db2.jcc.DB2Driver"
  jdbc.mysql.name = "com.mysql.jdbc.Driver"
}
```

## Driver Priority

In general it will not work to upgrade a JDBC driver by providing an external driver for a database that is already packaged with eccenca Dataintegration.

The driver delivered with eccenca Dataintegration will be prefered. Driver names (configured via e.g. `spark.sql.options.jdbc.drivers = "mssql"`) will be ignored if JDBC URLs starting with, in this example `jdbc:mssql...` , are already supported in the dataset.                   

_Recommended DBMS versions_

- **Microsoft SQL Server 2017**: Older versions might work, but do not support the `groupBy` parameter.
- **PostgreSQL 9.5**: The `groupBy` parameter needs at least version 8.4.
- **MySQL v8.0.19**: Older versions do not support the `groupBy` parameter.
- **DB2 v11.5.x**: The `groupBy` feature needs at least version 9.7 to function.
- **Oracle 12.2.x**: The `groupBy` feature does not work for versions prior to 11g Release 2.

These limitations are the same for JDBC drivers that are older than the fully supported databases.
Queries can achieve a similar outcome if `groupBy` is not supported.


## Parameter

### JDBC Driver Connection URL

JDBC URL, must contain the database as parameter, i.g. with ;database=DBNAME or /database depending on the vendor.

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Table

Table name. Can be empty if the read-strategy is not set to read the full table. If non-empty it has to contain at least an existing table.

- ID: `table`
- Datatype: `string`
- Default Value: `None`



### Source query

Source query (e.g. 'SELECT TOP 10 * FROM table WHERE x = true'. Warning: Uses Driver (mySql, HiveQL, MSSql, Postgres) specific syntax. Can be left empty when full tables are loaded. Note: Even if columns with spaces/special characters are named in the query, they need to be referred to URL-encoded in subsequent transformations.

- ID: `sourceQuery`
- Datatype: `code-sql`
- Default Value: `None`



### Group by

Comma separated list of attributes appearing in the outer SELECT clause that should be grouped by. The attributes are matched case-insensitive. All other attributes will be grouped via an aggregation function that depends on the supported DBMS, e.g. (JSON) array aggregation.

- ID: `groupBy`
- Datatype: `string`
- Default Value: `None`



### Order by

Optional column to sort the result set.

- ID: `orderBy`
- Datatype: `string`
- Default Value: `None`



### Limit

Optional limit of returned records. This limit should be pushed to the source. No value implies that no limit will be applied.

- ID: `limit`
- Datatype: `option[int]`
- Default Value: `10`



### Query strategy

The strategy decides how the source system is queried.

- ID: `queryStrategy`
- Datatype: `enumeration`
- Default Value: `access-complete-table`



### Write strategy

If this dataset is written to, it can be selected if data is overwritten or appended.'

- ID: `writeStrategy`
- Datatype: `enumeration`
- Default Value: `default`



### Multiple values strategy

How multiple values per entity property are written.

- ID: `multipleValuesStrategy`
- Datatype: `enumeration`
- Default Value: `concatenateValuesStrategy`



### Clear table before workflow execution

If set to true this will clear the specified table before executing a workflow that writes to it.

- ID: `clearTableBeforeExecution`
- Datatype: `boolean`
- Default Value: `false`



### User

Username. Must be empty in some cases e.g. if secret key and client id are used. If non-empty this will also overwrite any value set in the JDBC URL string.

- ID: `user`
- Datatype: `string`
- Default Value: `None`



### Password

Password. Can be empty in some cases e.g. secret key and client id are used or if it is just an empty string. The password must be set here and cannot be set in the JDBC URL connection string.

- ID: `password`
- Datatype: `password`
- Default Value: `None`



### Restriction

An SQL WHERE clause to filter the records to be retrieved.

- ID: `restriction`
- Datatype: `string`
- Default Value: `None`





## Advanced Parameter

### Token endpoint URL (Azure Active Directory)

URL for retrieving tokens, when using MS SQL Active Directory token based authentication. Can be found in the Azure AD Admin Center under OAuth2 endpoint or cab be constructed with the general endpoint URL combined with the tenant id and the suffix /outh/v2/authortized.

- ID: `tokenEndpoint`
- Datatype: `string`
- Default Value: `None`



### Service principal name (Azure Active Directory)

Service Principal Name identifying the resource. Usually a static URL like https://database.windows.net.

- ID: `spnName`
- Datatype: `string`
- Default Value: `None`



### Client id (Azure Active Directory)

Client id or application id. Client id used for MS SQL token based authentication. String seperated by - char.

- ID: `clientId`
- Datatype: `string`
- Default Value: `None`



### Client secret (Azure Active Directory)

Client secret. Client secret used for MS SQL token based authentication. Can be generated in Azure AD admin center.

- ID: `clientSecret`
- Datatype: `password`
- Default Value: `None`



### Retries

Optional number of retries per query

- ID: `retries`
- Datatype: `int`
- Default Value: `0`



### Pause

Optional pause between queries in ms.

- ID: `pause`
- Datatype: `int`
- Default Value: `2000`



### Charset

The source internal encoding, e.g., UTF-8, ISO-8859-1

- ID: `charset`
- Datatype: `string`
- Default Value: `UTF-8`



### Force spark execution

If set to true, Spark will be used for querying the database, even if the local execution manager is configured.

- ID: `forceSparkExecution`
- Datatype: `boolean`
- Default Value: `false`



