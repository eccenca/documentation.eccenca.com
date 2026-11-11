---
tags:
    - Configuration
---
# Quad Store Configuration

## Virtuoso setup

This section only covers setup options that have a direct impact on the interoperability between Explore and Virtuoso.
There are far more options which can significantly improve the overall performance.
For an overview of all configuration files and options of Virtuoso refer to the [OpenLink Virtuoso Universal Server Documentation](https://docs.openlinksw.com/virtuoso/).
Ensure to add the suggested parameters to the corresponding subsections of the configuration file before starting the server.

### Compatibility

- **Virtuoso 7.2.4.2** - Explore is compatible with [Virtuoso 7.2.4.2](https://github.com/openlink/virtuoso-opensource/releases/tag/v7.2.4.2). Compatibility with other versions is not guaranteed.

### Configuration

The following options apply to the Virtuoso configuration file `virtuoso.ini`. Check these options before starting Explore and adjust them if necessary.

#### SSL support

Mandatory configuration if `sparqlEndpoints.virtuoso[i].sslEnabled=true`. The server must have a valid certificate, which must be trusted by the system where Explore backend (DataPlatform) runs. In this case, the `sparqlEndpoints.virtuoso[i].port` property must point to the `SSLServerPort`.

```conf
[Parameters]
SSLServerPort      = 2111
;; Make sure that <PATH_TO_CERTS_DIR> is contained by DirsAllowed
SSLCertificate     = <PATH_TO_CERTS_DIR>/public-cert.pem
SSLPrivateKey      = <PATH_TO_CERTS_DIR>/private-key.pem
```

#### Transaction size limit (optional)

This option has impact on the maximum file size which can be uploaded using the SPARQL Graph Store endpoint and executing update queries.\
The maximum value you can set for this option is `2147483000` bytes.

```conf
[Parameters]
TransactionAfterImageLimit = <size_limit_in_bytes> # default 50000000
```

#### Database buffers

These options determine the amount of RAM used by Virtuoso to cache database files. To choose the appropriate values consult the `virtuoso.ini` file.

```conf
[Parameters]
NumberOfBuffers          = <size>
MaxDirtyBuffers          = <size>
```

#### ResultSet max rows

This setting is used to limit the number of rows in a result. The effective limit is the lowest value of this setting and the SPARQL query `LIMIT` clause value (if present). The exact value is situation-related and depends on the size of the datasets and the consequential number of returned rows. We recommend to set this option to `0` to disable the limitation.

```turtle
[SPARQL]
ResultSetMaxRows = 0 # default 10000
```

## GraphDB setup

This section covers only limitations and options which have a direct impact on the interoperability between Explore and GraphDB. For an overview of all configuration options of GraphDB refer to the official [GraphDB documentation](http://graphdb.ontotext.com/documentation/).

### Compatibility  <!-- graphdb setup -->

- GraphDB 9.2.0 - Explore is compatible with [GraphDB version 9.2.0](http://graphdb.ontotext.com/documentation/standard/release-notes.html#graphdb-9-2-0). Compatibility with newer versions is not guaranteed.

### Configuration  <!-- graphdb setup -->

No specific configuration changes are needed in order to run with GraphDB.
