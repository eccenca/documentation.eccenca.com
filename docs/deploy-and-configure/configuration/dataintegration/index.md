---
tags:
    - Configuration
---
# Build (DataIntegration)

This section is intended to be a reference for all available eccenca Build (DataIntegration) configuration options.
The configuration format is based on [HOCON](https://github.com/typesafehub/config).

The following sections introduce the most important configuration parameters.
The entire list of available configuration parameters can be found in the `dataintegration.conf` file found in the release package.

## OAuth

Authorization in eccenca Build (DataIntegration) is based on OAuth.
Typically, the eccenca Explore backend (DataPlatform) is used as an OAuth endpoint, but external endpoints can be used as well.
The Authorization Code Grant workflow is used for retrieving the OAuth token.
The default configuration is the following:

``` conf linenums="1"
# The URL of the eccenca DataPlatform.
eccencaDataPlatform.url = "http://localhost:9090"

# Use OAuth for authentification against DataPlatform
eccencaDataPlatform.oauth = false

# Enable if user information should be fetched via DP and OAuth. Only uncomment if OAuth is enabled and DP is configured.
user.manager.web.plugin = oauthUserManager

# The DataPlatform endpoint that is used for authentification
eccencaDataPlatform.endpointId = "default"

# Define the protocol used for accessing the workbench (http or https), defaults to http
workbench.protocol = "http"

# Optional parameter for specifying the host.
workbench.host = "localhost:9090"

# The URL to redirect to after logout.
# If not set, the user will be redirected to the internal logout page.
oauth.logoutRedirectUrl = "http://localhost:9090/loggedOut"

# The OAuth client that will be used to load the workspace initially and run the schedulers.
workbench.superuser.client = "elds"
workbench.superuser.clientSecret = "elds"

# Optional parameter for specifying an alternative OAuth authorization endpoint.
# If not specified, the default OAuth authorization endpoint of the specified eccenca Platform URL is used.
# Note that if the eccenca Platform URL is internal and not accessible for the user, a public authorization URL must be set here.
oauth.authorizationUrl = "http://localhost:9090/oauth/authorize"

# Optional parameter for specifying an alternative OAuth authorization endpoint.
oauth.tokenUrl = "http://localhost:9090/oauth/token"

# Optional parameter for specifying an alternative OAuth client ID.
oauth.clientId = "eldsClient"

# Optional parameter for specifying an alternative OAuth client secret.
oauth.clientSecret = "secret"

# Additional request parameters to append to all OAuth authentication requests.
# oauth.requestParameters = "&resource=value"
```

## Explore Configuration

eccenca Build (DataIntegration) can only be run by OAuth users that are granted the `https://vocab.eccenca.com/auth/Action/Build` action by the Explore component (aka DataPlatform/DataManager).
An example condition can be seen at [Access Conditions > Access to Build (DataIntegration)](../access-conditions/index.md#access-to-dataintegration)

In the shown example, the users also get access to all graphs in the RDF store.
This is not a requirement for working with Build (DataIntegration).
Access may also be restricted to graphs that the data integration users are allowed to work with.

In order to activate OAuth using the eccenca Explore (DataPlatform), the following minimal configuration is required:

``` conf linenums="1"
eccencaDataPlatform.url = "http://localhost:9090"
eccencaDataPlatform.oauth = true
oauth.clientId = "eldsClient"
oauth.clientSecret = "secret"
```

### Super User

By default, the workspace is loaded the first time a user opens eccenca Build (DataIntegration) in the browser using their credentials.
Any scheduler that is part of a project must be started manually.

By configuring a super user, the workspace will be loaded at startup.
After loading, all schedulers will be started using the credentials of the super user.

In addition to the configuration of eccenca Explore according to the previous section, a super user is configured by specifying the following two parameters:

``` bash linenums="1"
workbench.superuser.client = "superUserClient"
workbench.superuser.clientSecret = "superUserClientSecret"
```

??? note

    The client credentials grant type is used to retrieve a token for the super user.
    Note that the schedulers are only started automatically when running in production mode.

## Workspace Providers

The backend that holds the workspace can be configured using the `workspace.provider.plugin` parameter in `dataintegration.conf`

``` bash linenums="1"
workspace.provider.plugin = <workspace-provider-plugin-name>
```

The following sections describe the available workspace provider plugins and how they are configured.

### RDF-store Workspace - backend

When running in Corporate Memory, by default the workspace is held in the RDF store configured in the eccenca Explore.

The workspace is held using the eccenca Explore backend (DataPlatform), i.e., it requires the `eccencaDataPlatform.url` parameter to be configured.

This workspace can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| loadAllVocabularyPrefixes | boolean | Load prefixes defined by all known vocabularies. | false |
| loadInstalledVocabularyPrefixes | boolean | Load prefixes defined by vocabularies that are actually loaded in the RDF store. | true |
| vocabularyGraph | String | The graph that contains the vocabulary meta data. | <https://ns.eccenca.com/example/data/vocabs/> |
| cacheDir | String | Optional directory to persist caches between restarts. If empty, caches will be held in-memory and will be reloaded on each start. | `<empty>` |

By default, prefixes are loaded from all installed vocabularies. Only one of loadAllVocabularyPrefixes and loadInstalledVocabularyPrefixes can be set to true.

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf
eccencaDataPlatform.url = <DATAPLATFORM_URL>
...
workspace.provider.plugin = backend
...
workspace.provider.backend = {
  # Load prefixes defined by all known vocabularies.
  loadAllVocabularyPrefixes = false
  # Load prefixes defined by vocabularies that are actually loaded in the RDF store.
  loadInstalledVocabularyPrefixes = true
  # The graph that contains the vocabulary meta data.
  vocabularyGraph = "https://ns.eccenca.com/example/data/vocabs/"
  # Optional directory to persist caches between restarts. If empty, caches will be held in-memory and will be reloaded on each start.
  cacheDir = ""
}
```

### File-based Workspace - file

The workspace can also be held on the filesystem.

This workspace can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| dir | String | The directory to which the workspace is persisted. | no default |

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.provider.plugin = file
...
workspace.provider.file = {
  # The directory to which the workspace is persisted.
  dir = ${user.home}"/myWorkspace"
}
```

### Hybrid workspace - fileAndDataPlatform

The so called hybrid workspace holds the workspace in the filesystem and in eccenca Explore backend (DataPlatform) simultaneously. Each time a task is updated, it is written to both the filesystem and to the project RDF graph. In addition, on each (re)load of the Workspace, the contents of the file based workspace are pushed to the RDF store, to make sure that both workspace backends stay synchronized. Contents of the file system may be changed manually (reload the workspace afterwards). Contents of the RDF store are supposed to be read only and will be overwritten on reload.

The workspace is held using the eccenca Explore backend (DataPlatform), i.e., it requires the `eccencaDataPlatform.url` parameter to be configured.

This workspace can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| dir | String | The directory to which the workspace is persisted. | no default |
| loadAllVocabularyPrefixes | boolean | Load prefixes defined by all known vocabularies. | false |
| loadInstalledVocabularyPrefixes | boolean | Load prefixes defined by vocabularies that are actually loaded in the RDF store. | true |
| vocabularyGraph | String | The graph that contains the vocabulary meta data. | <https://ns.eccenca.com/example/data/vocabs/> |
| failOnDataPlatformError | boolean | If true, whenever an update is triggered that has been pushed to the xml backend, but failed to be pushed to the Explore backend (DataPlatform), the entire request fails. If false, an update error in the Explore backend (DataPlatform) will only log a warning. | false |

By default, prefixes are loaded from all installed vocabularies. Only one of loadAllVocabularyPrefixes and loadInstalledVocabularyPrefixes can be set to true.

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
eccencaDataPlatform.url = <DATAPLATFORM_URL>
...
workspace.provider.plugin = fileAndDataPlatform
...
workspace.provider.fileAndDataPlatform = {
  # The directory to which the workspace is persisted.
  dir = ${user.home}"/myWorkspace"
  # Load prefixes defined by all known vocabularies.
  loadAllVocabularyPrefixes = false
  # Load prefixes defined by vocabularies that are actually loaded in the RDF store.
  loadInstalledVocabularyPrefixes = true
  # The graph that contains the vocabulary meta data.
  vocabularyGraph = "https://ns.eccenca.com/example/data/vocabs/"
  # If true, whenever an update is triggered that has been pushed to the xml backend, but failed to be pushed to the DataPlatform, the entire request fails. If false, an update error in the DataPlatform will only log a warning.
  failOnDataPlatformError = false
}
```

### In-memory Workspace - inMemory

A workspace provider that holds all projects in memory. All contents will be gone on restart.

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.provider.plugin = inMemory
```

#### **In-memory RDF Workspace - inMemoryRdfWorkspace**

A workspace that is held in a in-memory RDF store and loses all its content on restart (mainly used for testing). Needed if operators are used that require an RDF store backend.

This workspace can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| loadAllVocabularyPrefixes | boolean | Load prefixes defined by all known vocabularies. | false |
| loadInstalledVocabularyPrefixes | boolean | Load prefixes defined by vocabularies that are actually loaded in the RDF store. | true |
| vocabularyGraph | String | The graph that contains the vocabulary meta data. | <https://ns.eccenca.com/example/data/vocabs/> |

By default, prefixes are loaded from all installed vocabularies. Only one of loadAllVocabularyPrefixes and loadInstalledVocabularyPrefixes can be set to true.

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.provider.plugin = inMemoryRdfWorkspace
...
workspace.provider.inMemoryRdfWorkspace = {
  # Load prefixes defined by all known vocabularies.
  loadAllVocabularyPrefixes = false
  # Load prefixes defined by vocabularies that are actually loaded in the RDF store.
  loadInstalledVocabularyPrefixes = true
  # The graph that contains the vocabulary meta data.
  vocabularyGraph = "https://ns.eccenca.com/example/data/vocabs/"
}
```

## Resource Repositories

Project resources are held by a resource repository which is configured using the `workspace.repository.plugin`  parameter in `dataintegration.conf`

```conf linenums="1"
workspace.repository.plugin = <resource-repository-plugin-name>
```

The following sections describe the available resource repository plugins and how they are configured.

### Project Specific Directories - projectFile

By default, resources are held in project specific directories.

This plugin can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| dir | String | The directory to which the resources are persisted. | no default |

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = projectFile
...
workspace.repository.projectFile = {
  dir = ${elds.home}"/var/dataintegration/workspace/"
}
```

### Shared Directory - file

Alternatively, all resources across all Build (DataIntegration) projects can be held in a single directory on the file system.

This plugin can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| dir | String | The directory to which the resources are persisted. | no default |

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = file
...
workspace.repository.file = {
  dir = ${elds.home}"/var/dataintegration/resources/"
}

```

### HDFS resources - hdfs

Holds all resources on the HDFS file system.

This plugin can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| path | String | The directory to which the resources are persisted. | no default |
| user | String | The hadoop user. | hadoopuser |

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = hdfs
...
workspace.repository.hdfs = {
  # The directory to which the resources are persisted.
  dir = "/data/hdfs-datalake/"
  # The hadoop user.
  user = "hadoopuser"
}
```

### S3 Bucket, Project Specific - projectS3

In addition to storing files in the local filesystem an AWS S3 bucket can be used as the resource repository backend.

To use resources stored on S3 the AWS `keyID` , `secretKey` need to be configured in the `dataintegration.conf`  file. This and the region are used to connect to S3. Further, one bucket name has to be given. This is analog to the root folder of filesystem based resource repositories.

This plugin can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| bucket | String | The S3 bucket name. | no default |
| accessKeyId | String | The S3 access key ID. | no default |
| secretKey | String | The S3 secret key. | no default |
| region | String | The AWS region the S3 bucket is located in. | no default |
| path | String | OPTIONAL. Path (absolute to the bucket (root)) that defines the folder that will be used to hold the workspace. | no default |

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = projectS3 # project individual resources
...
workspace.repository.projectS3 = {
  # The S3 bucket name.
  bucket = "your-bucket-name"
  # The S3 access key ID.
  accessKeyId = "BUCKET-ACCESS-KEY"
  # The S3 secret key.
  secretKey = "BUCKET-SECRET-KEY"
  # The AWS region the S3 bucket is located in.
  region = "eu-central-1"
  # OPTIONAL path in the bucket used to hold the DataIntegration workspace
  # /path/to/my-workspace/
}
```
For this S3 plugin make sure the account has at least these permissions attached:

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::<YOUR_BUCKET_NAME>"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::<YOUR_BUCKET_NAME>/*"
        }
    ]
}
```

### S3 Bucket, Shared Directory - s3

Holds all resources shared across all your Build (DataIntegration) projects in a single S3 bucket.

The available configuration options are the same as for `projectS3` .

The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = s3 # resources shared across projects
...
workspace.repository.s3 = {
  ... # same configuration as for projectS3
}
```

### In-Memory - inMemory

Resources can also be held in-memory. The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = inMemory
```

!!! note
    In-memory repositories will be emptied on restart.

#### No resources - empty

In case you do not want to allow to store file resources you can define an *empty* repository. The `empty` resource repository that does not allow storing any resources.

The resource repository can also be specified as empty. The corresponding configuration in your `dataintegration.conf` looks like the following:

```conf linenums="1"
workspace.repository.plugin = empty
```

## Execution Report Manager

The execution report manager is used to persist execution reports. It allows to retrieve previous reports. you can use it with file and in-memory models. In addition you can specify a retention time. Reports older than this time will be deleted, if a new report is added. The retention time is expressed as a Java `Duration` string, see <https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html#parse-java.lang.CharSequence-> for details.

### Disabled - None

Discards execution reports and does not persist them.

```conf linenums="1"
workspace.reportManager.plugin = none # Discards execution reports and does not persist them.

```

### In-Memory - inMemory

Holds the reports in memory.

```conf linenums="1"
workspace.reportManager.plugin = inMemory # Holds the reports in memory.

workspace.reportManager.inMemory = {
  retentionTime = "P30D" # duration how long to keep - default is 30 Days
}
```

### File based - file

Holds the reports in a specified directory on the filesystem.

```conf linenums="1"
workspace.reportManager.plugin = file # Holds the reports in a specified directory on the filesystem.

workspace.reportManager.file = {
  dir = "/data/reports" # directory where the reports will be stored
  retentionTime = "P30D" # duration how long to keep - default is 30 Days
}
```

## Internal Datasets

Internal datasets hold intermediate results during the execution of a Build (DataIntegration) Workflow. The type of internal dataset that is used can be configured. By default, an in memory dataset is used for storing data between tasks:

```conf linenums="1"
dataset.internal.plugin = inMemory
```

Alternatively, the internal data can also be held in the eccenca Explore backend (DataPlatform):

```conf linenums="1"
dataset.internal.plugin = eccencaDataPlatform
dataset.internal.eccencaDataPlatform = {
  graph = "https://ns.eccenca.com/dataintegration/internal"
}
```

If the eccenca Explore backend (DataPlatform) is not available, an external store may also be specified:

```conf linenums="1"
dataset.internal.plugin = sparqlEndpoint
dataset.internal.sparqlEndpoint = {
  endpointURI = "http://localhost:8890/sparql"
  graph = "https://ns.eccenca.com/dataintegration/internal"
}
```

!!! warning
    If an RDF store based internal dataset is used, all internal data is stored in the same graph. For this reason, multiple different internal datasets cannot be used safely in that case.

## Timeouts

Build (DataIntegration) has a number of timeouts to maintain operation while connection issues or problems in other applications occur. The following sections list the most important global timeouts.

??? note
    In addition to these global timeouts, many datasets, such as the Knowledge Graph dataset, do provide additional timeout parameters. Refer to the documentation of datasets for individual timeout mechanisms of different datasets.

!!! warning
    All timeouts set need to be lower than the gateway timeout in the network infrastructure.

### Request timeout

The request timeout specifies how long a HTTP(S) request may take until it times out and is closed:

```conf linenums="1"
play.server.akka.requestTimeout = 10m
```

This timeout mechanism can be disabled, by setting the timeout to `"infinite"`.

### Idle request timeout

The idle timeout specifies the maximum inactivity time of a HTTP(S) connection:

```conf linenums="1"
play.server.http.idleTimeout = 10m
```

The connection will be closed after it has been open for the configured idle timeout, without any request or response being written. This timeout mechanism can be disabled, by setting the timeout to `"infinite"`.

### Explore backend (DataPlatform) timeouts

As Build (DataIntegration) depends on the Explore backend (DataPlatform) for managing the Knowledge Graph, it will query the health of Explore backend (DataPlatform) as part of its own health check. The timeout to wait for Explore backend (DataPlatform)'s response to a health request can be configured:

```conf linenums="1"
healthCheck.dataplatform.timeout = 10000 # milliseconds
```

In addition, there is a timeout when requesting authorization information from the eccenca Explore backend (DataPlatform), which is fixed to 61 seconds.

### RDF store timeouts

When reading and writing RDF there are a number of timeouts applied, depending on whether the Graph Store protocol or the SPARQL endpoint are used.

For the Graph Store protocol, the following timeouts can be configured:

```conf linenums="1"
graphstore.default = {
  # Timeout in which a connection must be established
  connection.timeout.ms = 15000 # 15s
  # Timeout in which a response must be read
  read.timeout.ms = 150000 # 150s
  # Max request size of a single GraphStore request, larger data is split into multiple requests
  max.request.size = 300000000 # 300MB
  # Timeout in which a file upload of size max.request.size must be uploaded
  fileUpload.timeout.ms = 1800000 # half hour
}
```

For the SPARQL endpoint, the following parameters are applicable:

```conf linenums="1"
silk.remoteSparqlEndpoint.defaults = {
  connection.timeout.ms = 15000 # 15s
  read.timeout.ms = 180000 # 180s
}
```

!!! note
    The Knowledge Graph dataset provides additional timeout parameters for more fine-grained control.

### Linking execution timeout

When executing linking rules there are a number of timeouts to prevent possibly erroneous linkage rules from generating too many links or staling the execution:

```conf linenums="1"
linking.execution = {
  # The maximum amount of links that are generated in the linking execution/evaluation
  linkLimit = {
    # The default value a link spec is initialized with, this can be changed for each link spec.
    default = 1000000 # 1 million
    # The absolute maximum of links that can be generated. This is necessary since the links are kept in-memory.
    max = 10000000 # 10 million
  }
  # The maximum time the matching task is allowed to run, this does not limit the loading time.
  matching.timeout.seconds = 3600 # 1 hour
}
```

## Maximum Upload Size

By default, the size of uploaded resources is limited to 10 MB. The upload limit can be increased:

```conf linenums="1"
play.http.parser.maxDiskBuffer = 100MB
```

While uploading, resources are cached on the disk, i.e., the limit may exceed the size of the available memory.

## Provenance

By default, no provenance data is written to the RDF store. To enable writing provenance data to a named graph, a provenance plugin needs to be configured.

Provenance output can be configured using the following parameter:

| Parameter | Type | Description | Default |
|-|-|-|-|
| provenance.graph | String | Set the graph where generated provenance will be written to in the RDF workspace provider. | <https://ns.eccenca.com/example/data/dataset/> |
| provenance.persistWorkflowProvenancePlugin.plugin | String |Provenance plugin to set where provenance data should be written to. Possible options: - rdfWorkflowProvenance - writes provenance data to RDF backend - nopWorkflowProvenance - do NOT write provenance data (disable it) | nopWorkflowProvenance |

To enable provenance output, the following lines can be added to `dataintegration.conf`:

```conf linenums="1"
provenance.graph = https://ns.eccenca.com/example/data/dataset/
provenance.persistWorkflowProvenancePlugin.plugin = rdfWorkflowProvenance
```

## Logging

Logging for eccenca Build (DataIntegration) is based on the [Logback](https://logback.qos.ch/) logging framework. There are two ways to change the logging behavior from the default, the first is to provide a logback.xml file, the second is to set various logging properties in the `dataintegration.conf` file.

### Logback Configuration File

The `logback.xml` file can be added to the `${ELDS_HOME}/etc/dataintegration/conf/` folder, from where it is read on application start-up and replaces the default logging config.

#### Configuration Example

The following example `logback.xml` file defines a rolling file strategy where files are rotated on a time base (1 day) with a limit of 7 files, which means that the logging files contain a log history of a maximum of 1 week.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <appender name="TIME_BASED_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>/opt/elds/var/log/dataintegration.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <!-- daily rollover, history for 1 week -->
      <fileNamePattern>/opt/elds/var/log/dataintegration.%d{yyyy-MM-dd}.log</fileNamePattern>
      <maxHistory>7</maxHistory>
    </rollingPolicy>
    <encoder>
      <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>
  <logger name="com.eccenca" level="INFO">
    <appender-ref ref="TIME_BASED_FILE" />
  </logger>
</configuration>

```

### Logging Properties

For debugging purposes and smaller adaptions it is possible to change log levels for any logger in the Build (DataIntegration) config file. There are following possibilities:

```conf linenums="1"
# The following log level properties will overwrite the config from the logback.xml file

# Set the root logger level, valid values are: OFF, ERROR, WARN, INFO, DEBUG, TRACE, ALL.
# This affects any logger that is not explicitly defined in the logback.xml config file
logging.root.level = DEBUG

# Set the DI root log level. This affects all logger in DI packages that are not explicitly specified in the logback.xml
logging.di.level = TRACE

# Set the Silk root log level. This affects all logger in Silk packages that are not explicitly specified in the logback.xml
logging.silk.level = WARN

# Generic log level config: inside logging.level enter package path as key and log level as value.
# Valid values are: OFF, ERROR, WARN, INFO, DEBUG, TRACE, ALL
# This can be used to override any log level, also these defined in the logback.xml file.
logging.level {
  # Set log level of oauth package to TRACE, this overrides the config in the default logback config
  oauth=TRACE
}

```

## Plugin Configuration

The plugin architecture of eccenca Build (DataIntegration) allows to configure certain characteristics of the application, e.g. the persistence backend for the workspace.\
A full list over all plugins are given in the eccenca Build (DataIntegration) user manual in the sections *Plugin Reference* as well as *Activity Reference*.

### Blacklisting Plugins

In some cases the usage of specific plugins might pose a risk. In order to avoid to load a specific plugin, it can be blacklisted in the configuration file by setting the `pluginRegistry.plugins.{pluginID}.enabled`  config parameter to false. The parameter takes a comma-separated list of plugin IDs. The corresponding plugins will not be loaded into the plugin registry and can thus not be selected or executed anymore. The plugin ID for each plugin can be found in the *Plugin Reference* and *Activity Reference* section of the eccenca Build (DataIntegration) user manual.

Example config:

```conf linenums="1"
pluginRegistry {
  plugins {
    pluginToBeBlacklisted.enabled = false
  }
}
```

## Spark Configuration

The following chapters describe configuration options relevant for the execution of eccenca Build (DataIntegration) workflows on Spark. All options regarding the execution of Build (DataIntegration) on Spark are set in the `dataintegration.conf` file. The option to define SparkExecutor as the execution engine is `execution.manager.plugin` and needs to be changed from the default value:

```conf linenums="1"
execution.manager.plugin = LocalExecutionManager
```

To the value that specifies the use of the SparkExecutor:

```conf linenums="1"
execution.manager.plugin = SparkExecutionManager
```

### Execution in Spark client Mode

Spark provides a simple standalone cluster manager. You can launch a [standalone](http://spark.apache.org/docs/latest/spark-standalone.html) cluster either manually, by starting a master and workers by hand, or by using the provided launch scripts. Spark can still run alongside Hive, Hadoop and other services in this mode. But in general this mode is preferred if only Spark applications are running in a cluster. When multiple cluster applications are running in parallel (e.g. different databases, interpreters or any software running on top of Yarn) or more advanced monitoring is needed the execution with Yarn is often recommended.

For running Build (DataIntegration) in client mode the following configuration can be used

```conf linenums="1"
spark.interpreter.options = {
  # Specifies local or client-mode, required: local, cluster or client
  deploymentMode = "client"
  # URL of the Spark cluster master node
  sparkMaster = "spark://spark.master:7077"
  # The IP of the driver/client program machine in client-mode, required for client mode
  sparkLocalIP = "IP or hostname where DataIntegration runs"
  # Jars containing the dependencies, required only for client and cluster modes
  # In client mode the artifact 'eccenca-DataIntegration-assembly.jar' must be included
  sparkJars = "eccenca-DataIntegration-assembly.jar"
}
```

### Execution in cluster mode

#### Build (DataIntegration) application configuration

Cluster mode is supported with Apache Yarn only at the moment. To run Build (DataIntegration) in cluster mode the following configuration can be used:

```conf linenums="1"
spark.interpreter.options = {
  # Specifies local or client-mode, required: local, cluster or client
  deploymentMode = "cluster"
  # URL of the Spark cluster master node
  sparkMaster = "yarn-master-hostname"
  # The IP of the driver/client program machine in client-mode, required for client mode
  sparkLocalIP = "IP or hostname where DataIntegration runs"
  # Jars containing the dependencies, required only for client and cluster modes
  # In cluster mode the artifact 'eccenca-DataIntegration-assembly.jar' must be included
  sparkJars = "eccenca-DataIntegration-assembly.jar"
}
```

#### Build (DataIntegration) cluster deployment configuration

In cluster mode one should keep in mind that, normally, Build (DataIntegration) will generate a jar and a project export. These artifacts can be copied or send to a cluster and will be executed there via the `spark-submit` command. That means the data processing is running in its own remote process separate from the Build (DataIntegration) application.

An assembly jar and a workflow can be exported by an activity that belongs to each defined workflow. The activity can be configured in the `dataintegration.conf` . There are 3 phases of a deployment: staging, transform, loading and 3 types of artifact compositions as well as some other options deciding the target of the export. First the specified resource are copied to the configured resource folder of a project or a temp folder (staging) and then an action decides how the files are deployed.

*Artifacts (spark.deployment.options.artifact):*

- 'jar': The assembly jar is deployed
- 'project': The exported project zip file is deployed (e.g. if the assembly was already globally deployed)
- 'project-jar': The jar and the project zip are deployed

The artifacts are copied to the configured resource folder off the project the activity belongs to.

*Types (`spark.deployment.options.[phase].type, e.g. spark.deployment.options.staging.type="env-script"` ):*

- 'script' A shell script is called to copy the files to the cluster (can be user supplied, contain auth, prepare a DataFactory activity etc.)
- 'copy' The resource are copied to a specified folder
- 'hdfs' The resource is imported to HDFS
- 'env-script' A shell script is loaded from a environment variable
- 'var-script' A shell script is loaded from a configuration variable

*Other options:*

- `spark.deployment.options.[phase].[typeName]` Depending on the selected deployment type this contains one or more (separated by a comma) targeted local file system or HDFS paths or location of the scripts to run\
    e.g. `spark.deployment.options.staging.type ="script"` and `spark.deployment.options.staging.script="/scripts/script.sh"`
- `spark.deployment.options.overwriteExecution` Boolean value that decides if the ExecuteSparkWorkflow action is overwritten by the deployment action and will run this instead.

*Example:*

```conf linenums="1"
spark.deployment.options = {
  # Specifies artifacts: Stage the project export and the executable assembly jar
  artifact = "project-jar"
  # Type of the deployment: Copy project and jar to /data folder, then run a script to start processing the data
  staging.type = "copy"
  staging.copy = "/data"
  transform.type = "script"
  transform.script = "conf/runWorkflow.sh"
  # Bind the 2 actions to the "run workflow" button
  overwriteExecution = true
}
```

##### Activity parameters to skip deployment phases

In some scenarios (especially deployments where a jar has to be copied to a remote location) it is required that a deployment phase can be skipped. E.g. the jar upload only has to be done once, the upload is defined in the "staging" phase and the spark-submit call in the "transform" phase. The parameter "executeTransform" (reachable via the activity tab) can\
be set to false on the second run to avoid re-uploading artifacts.

#### Configuration of the assembly jar

In cluster mode, usually, we run a Spark Job by submitting an assembly jar to the cluster. This can be seen a command line version of Build (DataIntegration) and can also be used manually with 'spark-submit'. In this case the configuration in the environment the jar runs in should look like this (options are set by the spark-submit configuration and parameters):

```conf linenums="1"
spark.interpreter.options = {
  # Specifies deployment mode, requires: local, cluster, client or submit
  deploymentMode = "submit"
}
```

### Execution in local mode

Local mode is mainly for testing, but can be used for deployment on a single server. HDFS and Hive are not required. The following configuration parameters have to be set:

```conf linenums="1"
spark.interpreter.options = {
  # Specifies deployment mode, requires: local, cluster, client or submit
  deploymentMode = "local"
  # URL of the Spark cluster master node, the [*] denotes the number of executors
  sparkMaster = "local[4]"
}
```

In this mode the parameters and Spark settings appended to the 'spark-submit' command will always be used and overwrite configuration settings in other sources.

### Configuration and usage of the SqlEndpoint dataset

#### Server Side Configuration

##### General Settings

The SqlEndpoint dataset is a table or view behaving analog to a table in a relational database like MySQL. When data is written to an SqlEndpoint dataset, a JDBC server is started and can be queried with any JDBC client. In Build (DataIntegration) the SqlEndpoint dataset behaves like any other dataset. It can be used as a target for workflows, be profiled, used as a source for an operation or workflow etc. There are a two of configuration options that are relevant for the JDBC endpoints:

```conf linenums="1"
spark.sql.options = {
  # Specifies if DataIntegration is allowed to start a thrift server for external JDBC access. SqlEndpoint
  # datasets can still be started but can only be accessed internally if set to false.
  startThriftServer = true
  # Enable Hive integration
  # Sets Spark to use an infrastructure for meta data that is compatible with the hive metastore
  enableHiveSupport = true
  ...
}
```

The port on which the JDBC connections will be available is `10005` by default and can be changed in the `hive-site.xml` and `spark-defaults.conf` configuration files.

##### Security Settings

A secure connection can be configured with the authentification settings in the `hive-site.xml` , `spark-defaults.conf` and `dataintegration.conf` files.

If Hive support is disabled ( `enableHiveSupport = false` ) or if the property `hive.server2.authentication` has the value `None` security can be disabled.

There exist a number of option for secure JDBC connections via Thrift and Hive:

- Kerberos
- LDAP
- Custom authentication classes
- User impersonation
- Server and Client Certificates

Eccenca provides a custom Authentification provider which allows to set 1 user/password combination for JDBC connections via:

```code
spark.sql.options = {
  endpointUser = "user"
  endpointPassword = "password"
}
```

The authentication provider class name is `com.eccenca.di.sql.endpoint.security.SqlEndpointAuth` . To use it the following configuration is needed:

```xml
  <configuration>
    <property>
      <name>hive.server2.authentication</name>
      <value>CUSTOM</value>
    </property>
    <property>
      <name>hive.server2.custom.authentication.class</name>
      <value>com.eccenca.di.sql.endpoint.security.SqlEndpointAuth</value>
      <description>
        Custom authentication class. Used when property
        'hive.server2.authentication' is set to 'CUSTOM'. Provided class
        must be a proper implementation of the interface
        org.apache.hive.service.auth.PasswdAuthenticationProvider. HiveServer2
        will call its Authenticate(user, password) method to authenticate requests.
        The implementation may optionally implement Hadoop's
        org.apache.hadoop.conf.Configurable class to grab Hive's Configuration object.
      </description>
    </property>
    ...
  </configuration>

```

Check the Hive documentation for details: [Hive admin manual](https://cwiki.apache.org/confluence/display/Hive/AdminManual+Configuration#AdminManualConfiguration-ConfigurationVariables) or the documentation of a Hadoop Distribution (MapR, Hortenworks or AWS and Azure in he cloud etc.). Hadoop distributions usually provides instructions for configuring secure endpoints.

Integration with various authentication providers can be configured and is mostly set up in `hive-site.xml` .

#### SqlEndpoint Dataset Parameters

The dataset only requires that the `tableNamePrefix` parameters is given. This will be used as the prefix for the names of the generated tables. When a set of Entities is *written* to the endpoint *a view is generated for each entity type* (defined by an `rdf_type` attribute). That means that the mapping or data source that are used as input for the SqlEndpoint need to have a type or require a user defined type mapping.

The operator has a *compatibility mode*. Using it will avoid complex types such as Arrays. When arrays exit in the input they are converted to a String using the given `arraySeperator`.

#### SqlEndpoint Activity

The activity will *start* automatically, when the SqlEndpoint is used as a data sink and Build (DataIntegration) is configured to make the SqlEndpoint accessible remotely.

When the activity is started and *running* it returns the server status and JDBC Url as its value.

*Stopping* the activity will drop all views generated by the activity. It can be *restarted* by rerunning the workflow containing it as a sink.

#### Remote Client Configuration (via JDBC and ODBC)

Within Build (DataIntegration) the SqlEndpoint can be used as a source or sink like any other dataset. If the *startThriftServer* option is set to `true` access via JDBC or ODBC is possible.

[ODBC](https://en.wikipedia.org/wiki/Open_Database_Connectivity) and [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) drivers can be used to connect to relational databases. These drivers are used by clients like, Excel, PowerBI or other BI tools and transform standard SQL-queries to Hive-QL queries and handle the respective query results. Hive-QL support a subset of the SQL-92 standard. Depending on the complexity of the driver it -- in case of a simple driver -- supports the same subset or more modern standards. JDBC drivers are similar to ODBC ones, but serve as connectors for Java applications. When selecting a version of a driver the client operating system and its type (32bit/64 bit) are the most important factors. The version of the client drivers sometimes is the same as the servers. When no version of a driver is given the newest driver of the vendor should work, as it *should* be backwards compatible.

Any JDBC or ODBC client can connect to a JDBC endpoint provided by an SqlEndpoint dataset. SqlEndpoint uses the same query processing as Hive, therefore the requirements for the client are:

- A JDBC driver compatible with *Hive 1.2.1* (platform independent driver org.apache.hive.jdbc.HiveDriver is needed) or
  - Hive 1.2.1 is [ODPi](https://github.com/odpi/specs/blob/master/ODPi-Runtime.md) runtime compliant
- A JDBC driver compatible with *Spark 2.3.3*
- A Hive ODBC driver (ODBC driver for the client architecture and operating system needed)

A detailed instruction to connect to a Hive or SqlEndpoint endpoint with various tools (e.g. SQuirreL, beeline, SQL Developer, ...) can be found at [Apache HiveServer2 Clients](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients).\
The multi platform database client [DBeaver](https://dbeaver.io/) can connect to the SQLEndpoint out of the box.

### Partitioning and merging of data sets

The execution on Spark is possible independent of the used file system as long as it can be referenced/is accessible for all cluster nodes. HDFS is recommended and the default settings are recommended for the best performance on a small cluster. Especially when working in local mode on the local file systems some problems can occur with the parallelism settings of Spark and the resulting partitioned output resources.

Problems can be avoided by changing the following are the default settings:

```conf linenums="1"
spark.interpreter.options = {
  # If true, data will be repartitioned before execution,
  # otherwise the existing partitioning or no partitioning will be used
  partitionOnImport = false
  # Number of partitions for repartitioning on import, default = 16
  partitionNumber = 16
  # Specifies if data is combined before output is written to disk
  combineOutput = false
}
```

When running only locally the configuration should be like the following example (especially `combineOutput` has to be true):

```conf linenums="1"
spark.interpreter.options = {
  # If true, data will be repartitioned before execution,
  # otherwise the existing partitioning or no partitioning will be used
  partitionOnImport = false
  # Number of partitions for repartitioning on import, default = 16
  partitionNumber = 4
  # Specifies if data is combined before output is written to disk
  combineOutput = true
}
```

### Other options specific to Spark

```conf linenums="1"
#################################################
# Spark                                        #
#################################################

spark.interpreter.options = {
  # the default name used when creating a SparkContext (will override spark.app.name in spark-defaults.conf)
  sparkAppName = "eccenca DataIntegration Spark exe

  # Enables more detailed logging, counting of transformed records, etc.
  debugMode = false

  # Enable or disable a spark executor event log for debugging purposes
  eventLog = true

  # Folder for logs that people don't want in the log even though the information is necessary for debugging
  logFolder = ${elds.home}"/var/dataintegration/logs/"

  # Enable or disable an execution time log for benchmarking purposes
  timeLog = true

  # Enable or disable Sparks built-in log for debugging purposes (will override spark.eventLog.enabled in spark-defaults.conf)
  sparkLog = true

  # If true, data will be repartitioned before execution, otherwise the existing partitioning or no partitioning will be used
  partitionOnImport = false

  # Number of partitions for repartitioning on Import
  partitionNumber = 16

  # Specifies number of Spark SQL shuffle partitions (will override spark.sql.shuffle.partitions in spark-defaults.conf)
  shufflePartitions = 32

  # Minimum partition number for Spark execution
  defaultMinPartitions = 4

  # Default parallelism partition number for Spark execution (will override spark.sql.shuffle.partitions in spark-defaults.conf)
  defaultParallelism = 4

  # Specifies if data is combined before output is written to disk. If true the final output will be in a single file on a single partition
  combineOutput = true

  # Specifies if DataIntegration is allowed to start a thrift server for external JDBC access. Views/virtual datasets can still be started but can only be accessed internally if set to false.
  startThriftServer = false

  # Internal data model used in Spark Data Frames: 'sequence' or 'simple'. Sequence behaves like the entities used by the local executor of DataIntegration and is
  # sometimes be needed to work with non relational data (i.e. triple stores, dataplatform). The default value is 'simple' and casts most data objects to Strings
  # which is fast and works in most situations may lead to less clean data.
  columnType = sequence

  # General additional Java options that will be passed to the executors (worker nodes) in the cluster, default is "".
  sparkExecutorJavaOptions = ""

  # General additional Java options that will be passed to the driver application (DataIntegration), default is "".
  sparkDriverJavaOptions = ""

  # Enable or disable the Spark UI. This UI provides an overview of the Spark cluster and running jobs. It will start on port 4040
  # and increase the port number by 1 if the port is already in use. The final port will be shown in the logs. False by default.
  enableSparkUI = true

  # This property decides if Hive integration is enabled orr not.
  # To use hive an external DB (such as MYSQL), the meta store, is needed. Please specify the necessary properties in the hive-site.xml. Note that Hive's default meta store (derby) should not be used in production and may lead to issues.
  enableHiveSupport = false
}
```

## Mapping Creator and LLM Configuration

Enable (or disable) the new visual [Mapping Create UI](../../../build/mapping-creator/index.md) with `com.eccenca.di.mappingCreatorEnabled = true` (or `false` to disable).

```bash linenums="1"
#################################################
### Mapping creator
#################################################

com.eccenca.di.mappingCreatorEnabled = true
```

The [Mapping Creator can optionally use LLM](../../../build/mapping-creator/index.md#smart-suggestions-with-ai-support) to automatically generate class and property mappings.
Use the following configuration section as a blueprint to set up your OpenAI-compatible endpoint, providing:

-   the API key,
-   a model,
-   reasoning level,
-   and (optionally) benchmarking outputs.

```bash linenums="1"
#################################################
### AI assistant
#################################################

# Preliminary LLM config. Will be changed in the future.
com.eccenca.di.assistant = {
  ApiConfig = {
    # API key
    # apiKey = ""

    # Optional organisation id for OpenAI accounts
    # orgId = ""

    # Model to use for mapping suggestions
    model = "gpt-5-mini"

    # URL of OpenAI-compatible endpoint, leave empty for official OpenAI API
    # coreUrl = "https://openrouter.ai/api/v1"

    # Controls how many reasoning tokens the model generates before producing a response.
    # One of "low", "medium, "high". Set to null for default.
    reasoningEffort = "low"

    # Extra parameters to be passed to the API
    # extraParameters = {
    #   provider = {
    #     require_parameters: true
    #   }
    # }

    # Log prompts and responses
    logQueries = false
  }

  BenchmarkConfig = {
    # If set, only this project / transform task / mapping will be benchmarked
    # project = "myProject"
    # transform = "myTransform"
    mapping = "root"

    # Number of runs for each benchmark
    numberOfRuns = 10

    # If true, an HTML report will be generated in addition to the Markdown report
    generateHtml = true

    # Directory where benchmark results are stored
    outputDirectory = "benchmark_results"
  }
}
```
