---
tags:
    - Configuration
    - JDBC
---
# Setup and use of JDBC Drivers

Corporate Memory allows to use JDBC to connect to Database Management Systems (DBMS).
We ship some drivers as part of our platform.
Custom drivers can be added and used, too.

!!! info "References"

    For more technical details also check the following reference pages:

    -   [Remote SQL endpoint](../../../../build/reference/dataset/Jdbc.md) and
    -   [Snowflake SQL endpoint](../../../../build/reference/dataset/SnowflakeJdbc.md).

## Embedded JDBC Driver

Our platform contains and ship the following JDBC drivers:

-   PostgreSQL (`postgresql v42.7.10`)
-   MariaDB (includes support for MySQL, `mariadb-java-client v3.5.7`)
-   Microsoft SQL Server (`mssql-jdbc v13.2.1.jre11`)
-   Snowflake (`snowflake-jdbc v3.28.0`)

## Custom JDBC Driver

In addition to the shipped default JDBC drivers custom JDBC drivers can be registered.
The following steps describe how they are configured.

### Download Custom JDBC Driver

Download the respective JDBC driver for the Database Management Systems that need to be connected.
[Integrations](../../../../build/integrations/index.md) provides links for well know system and at the same time lists those that are in active use with Corporate Memory.

### Provide a Custom JDBC Driver

Consult your solutions manager or DevOps specialist for options how to copy / inject additional files, namely the JDBC driver `jar`, into a Corporate Memory deployment.
Depending on the specific deployment model used the suitable options differ, some possibilities:

-   the docker compose package `cmem-orchestration` mounts the folder `./conf/dataintegration/plugin/` into the DataIntegration container (this location is assumed in the configuration snippets below and mapped to the container internal path `/opt/cmem/eccenca-DataIntegration/dist/etc/dataintegration/conf/plugin/`),
-   a dedicated Build project into which the driver jar files are uploaded as project (file) resources,
-   dedicated file or resource mounts in a docker compose or helm/kubernets configuration.

## Driver Registration

A custom JDBC driver needs to be registered in the DataIntegration configuration file, `dataintegration.conf`, `spark.sql.options` section.
The following example demonstrates how to register the custom JDBC driver for the Databricks data lakehouse:

```conf
…
spark.sql.options {
  …
  # driver name
  jdbc.drivers = "databricks"
  # path to the jar in the docker container
  jdbc.databricks.jar =  "/opt/cmem/eccenca-DataIntegration/dist/etc/dataintegration/conf/plugin/DatabricksJDBC.jar"
  # class name
  jdbc.databricks.name = "com.databricks.client.jdbc.Driver"
  …
}
…
```

## Use the driver

JDBC drivers are used via the **Remote SQL endpoint** (or **Snowflake SQL endpoint**) dataset type.

![](jdbc-dataset.png){ class="bordered" width="85%" }

They can be configured in the configuration dialog of the dataset, consult the documentation of your DBMS / JDBC driver for details about the [JDBC connection string](https://www.baeldung.com/java-jdbc-url-format).

![](jdbc-config-databricks.png){ class="bordered" width="100%" }
