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

## Docker compose based Orchestration deployment

[Docker Compose](https://docs.docker.com/compose/) is a convenient way to provision several Docker containers locally for development setups or on remote servers for single node setups.

eccenca is heavily using `docker compose` for all kinds of internal and customer deployments. For more details on how to use `docker compose` based orchestration refer to [Scenario: Local Installation](../installation/scenario-local-installation/index.md) and [Scenario: Single Node Cloud Installation](../installation/scenario-single-node-cloud-installation/index.md).

## Explore

### Scaling

Run multiple Explore instances with the same configuration to enable high-availability and/or high-performance setups.

#### Prerequisites <!-- multiple Explore instances the following prerequisites -->

For running multiple Explore instances the following prerequisites apply:

-   The same application configuration properties must be used by all scaled instances.
-   If access control for any SPARQL endpoint is active, a shared Redis cache used by all Explore instances is required.

#### Limitations

When running multiple Explore instances it is not possible to use a shared Virtuoso backend with provisioned access control active.

### Troubleshooting

In case Explore failed to start, check the logs for error messages pointing to faulty parameters in the configuration. Since not every faulty behavior is apparent from reading the logs, the following checks can help you to verify the configuration:

-   Check the `http(s)://<servername:port>/actuator/health/` endpoint to verify if the SPARQL proxy service endpoints are configured properly.

Note: Refer to the [Spring documentation](https://docs.spring.io/spring-boot/docs/2.1.8.RELEASE/reference/htmlsingle/#boot-features-profiles) on how to set active profiles.

### Plugins

In some cases Explore needs to be extended with plugins. Extensions are necessary when drivers cannot be included due to licensing restrictions or when plugins are delivered separately.

In this case, you have to update the .war file of Explore by placing the plugin .jar files in the same directory, or by stating the path via the configuration option.

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
