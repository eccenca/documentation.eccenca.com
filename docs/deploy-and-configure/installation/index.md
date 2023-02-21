---
icon: material/download-circle-outline
---
# Installation

This page describes proven deployment scenarios for eccenca Corporate Memory.

All Corporate Memory components are distributed as Docker images and can be obtained from eccenca's Artifactory service. To run them you need a Docker enabled Linux server. In addition to that, eccenca provides distribution archives for all components which contain configuration examples (YAML) as well as JAR/WAR artifacts.

## Operating Systems (OS)

Corporate Memory is tested on Ubuntu 18.04 (backward compatible with 16.04 and 14.04) and RHEL 7.7.

Special note on RHEL SELinux Support: there is no limitation for RedHat SELinux. We recommend to keep the SELinux in *enforced* mode. You can keep the default setting of the `/etc/selinux/config` file.

???+ example "sample config"

    ```bash title="/etc/selinux/config" linenums="1"
    # This file controls the state of SELinux on the system.
    # SELINUX= can take one of these three values:
    #     enforcing - SELinux security policy is enforced.
    #     permissive - SELinux prints warnings instead of enforcing.
    #     disabled - No SELinux policy is loaded.
    SELINUX=enforcing
    # SELINUXTYPE= can take one of three values:
    #     targeted - Targeted processes are protected,
    #     minimum - Modification of targeted policy. Only selected processes are protected.
    #     mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ```

## Docker-compose based Orchestration deployment

[Docker Compose](https://docs.docker.com/compose/) is a convenient way to provision several Docker containers locally for development setups or on remote servers for single node setups.

eccenca is heavily using Docker Compose for all kinds of internal and customer deployments. For more details on how to use docker-compose based orchestration refer to [Scenario: Local Installation](../installation/scenario-local-installation/index.md) and [Scenario: Single Node Cloud Installation](../installation/scenario-single-node-cloud-installation/index.md).

## DataIntegration

### Running on a Spark Cluster

eccenca DataIntegration supports the execution of DataIntegration workflows in a cluster environment with Apache Spark.

#### Prerequisites

For the execution of DataIntegration in a Spark cluster the following software components from the Hadoop eco-system are recommended:

- Scala 2.11 or 2.10
- Apache Spark 2.1.2 (compiled for Scala 2.11)
- Apache Hadoop 2.7 (HDFS)
- Apache Hive 1.2, with a relational database as metastore (e.g. Derby)

Recent versions of the following Hadoop distributions are generally supported as well:

- Hortonworks (HDP 2.5)
- Cloudera (CDH 5.8)
- Oracle Big Data Lite (4.6)
- Microsoft HDInsight (based on HDP)

#### Installation <!-- Different Modes of Installation-->

A Spark application can run in three different modes:

- local mode
- client mode
- cluster mode

The local mode is for running Spark applications on one local machine. In the client mode the DataIntegration application will run outside of the cluster and create Spark Jobs to be executed in the cluster at run time. The cluster mode requires that the application using Spark completely runs in the cluster and is managed by the software running on the cluster (e.g. Spark, Apache Yarn, Mesos). DataIntegration supports local mode (for testing), client mode (for production, only with clusters managed by Spark) or cluster mode on Yarn (for production, integrates best with other distributed applications).

When running DataIntegration in a cluster, the same installation procedure and prerequisites apply as for the local installation. The application can be installed outside the cluster or on any cluster node. A number of configuration options have to be set to be able to connect to and use a Spark cluster. The necessary configuration options are described in [DataIntegration](./../configuration/dataintegration/index.md).

## DataPlatform

### Scaling

Run multiple DataPlatform instances with the same configuration to enable high-availability and/or high-performance setups.

#### Prerequisites <!-- multiple DataPlatform instances the following prerequisites -->

For running multiple DataPlatform instances the following prerequisites apply:

- The same application configuration properties must be used by all scaled instances.
- If access control for any SPARQL endpoint is active, a shared Redis cache used by all DataPlatform instances is required.

#### Limitations

When running multiple DataPlatform instances it is not possible to use a shared Virtuoso backend with active provisioned access control.

### Troubleshooting

In case DataPlatform fails to start, check the logs for error messages pointing to faulty parameters in the configuration. Since not every faulty behavior is apparent from reading the logs, the following checks can help you to verify the configuration:

- Check the `http(s)://<servername:port>/actuator/health/` endpoint to verify if the SPARQL proxy service endpoints are configured properly.

Note: Refer to the [Spring documentation](https://docs.spring.io/spring-boot/docs/2.1.8.RELEASE/reference/htmlsingle/#boot-features-profiles) on how to set active profiles.

### Plugins

In some cases DataPlatform needs to be extended with plugins. Extensions are necessary when drivers cannot be included due to licensing restrictions or when plugins are delivered separately.

In this case, you have to update the .war file of DataPlatform by placing the plugin .jar files in the same directory, or by stating the path via the configuration option.

To include plugins that are located in the same directory as the `eccenca-DataPlatform.war` file, execute the .war file with the option `-u` or `--update-war`:

```bash linenums="1"
# with plugins located in the same folder as the WAR file
java -jar ${JAVA_TOOL_OPTIONS} eccenca-DataPlatform.war --update-war
```

If the plugins to be included are not located in the same folder as the .war file, you can specify a directory containing the plugins as the argument of the `-u` or `--update-war` option.

```bash linenums="1"
java -jar ${JAVA_TOOL_OPTIONS} eccenca-DataPlatform.war -u /data/plugins
```

The last command repackages the `eccenca-DataPlatform.war` by including all plugins (.jar) located in the specified directory.

Note: Make sure that only the `eccenca-DataPlatform.war` file is in the directory since multiple .war files can cause problems.

Note: During the update procedure, the directory `WEB-INF` is created. Due to security concerns the update mechanism does not delete this directory. You can delete it after the update process is finished.
