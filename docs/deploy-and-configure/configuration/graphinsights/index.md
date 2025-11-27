---
tags:
    - Configuration
    - Graph-Insights
    - GraphInsights
---
# Graph Insights

## OAuth configuration

Graph Insights requires authentication similar to Explore and Build (DataIntegration).
There is the need for a client to authenticate in a browser and a second client to allow inter-component communication.

For convenience, by default we use the same clients as for the rest of the application:

-   Client for browser: cmem
-   Client for component communication: cmem-service-account

In case you want to have separate clients for production deployments, have a look at the end of this file.

## Resource consideration

Please refer to [Graph Insights Sizing](../../../deploy-and-configure/requirements/graph-insights-sizing.md) for more information.


### Explore configuration

The following two sections are needed for enabling Graph Insights inside Explores configuration.
In the docker orchestration it is enabled through profiles while in helm we just use one profile.
We there use helm templating mechanism to render it into the default profile.

``` yaml
spring.security.oauth2.client.registration.explore-service:
    client-id: cmem-service-account
    client-secret: change-me
    authorization-grant-type: client_credentials
    provider: keycloak
```

``` yaml
semspect:
  enabled: true
  integration:
    url: http://graphinsights:8080/graphinsights
    externalUrl: ${DEPLOY_BASE_URL}/graphinsights
    automaticResyncCronExpression: "0 0/30 8-10 * * *"
    localDatasetStatePath: /graphinsights/infinispan
    ### Configure either fileShareIntegrationSettings or graph-store-integration-settings
    # fileShareIntegrationSettings:
    localGraphStoragePathExplore: /graphinsights
    # localGraphStoragePathSemspect: /explore-share/
    graph-store-integration-settings:
      semspect-dataplatform-url: http://explore/dataplatform
```


#### (a) helm configuration

In helm based deployment you can enable Graph Insights by enable it in your value file.
Preemptive you have to create a secret containing your license file.

``` console
- "kubectl -n cmem create secret generic graphinsights-license --from-file your-graphinsights.lic
```

This enables the plugin.

``` yaml
graphinsights:
  enabled: true
```

All needed configuration can be done in the Corporate Memory helm chart `value.yaml` file.
The configuration mentioned above is rendered with those files, but you usally don't have to touch those:

- `configuration-files/explore-application.yml` for Explore
- `configuration-files/cmem.integration.config.yml` for Graph Insights

For more details please have a look in the helm value file.
Every configuration is documented there.
Please refer to [Kubernetes deployments](../../../deploy-and-configure/installation/scenario-k8s-deployment/index.md) for more information.

#### (b) docker-compose configuration

In our Corporate Memory docker-orchestration all main configurations can be directed by setting environments
variables in `environments/config.env`.
You can find the environments are set as usual in `environments/default.env` and `environments/config.env`.

``` Makefile
###########################
# GRAPH-INSIGHTS SETTINGS #
###########################
GRAPHINSIGHTS_JAVA_TOOL_OPTIONS="-XX:UseSVE=0"

# This is the client the user uses to login to Graph Insights in browser
# for convenience we use the same as CMEM client
# GRAPHINSIGHTS_OAUTH_CLIENT_ID=graph-insights
GRAPHINSIGHTS_OAUTH_CLIENT_ID=${OAUTH_CLIENT_ID}

# This is the client ID for the Graph Insights service account but not used
# due to convienience we use the same as CMEM service account
GRAPHINSIGHTS_OAUTH_SERVICE_CLIENT_ID=graph-insights-service-account
GRAPHINSIGHTS_OAUTH_SERVICE_CLIENT_SECRET=changeme

GRAPHINSIGHTS_SERVER_PORT=8080
GRAPHINSIGHTS_SERVER_SERVLET_CONTEXT_PATH=/graphinsights
# in case of subdomain this have to be adjusted.
GRAPHINSIGHTS_SERVER_FRAME_ANCESTORS=${DEPLOY_BASE_URL}
GRAPHINSIGHTS_LOGGING_LEVEL_ROOT=DEBUG
```

These are used in the configuration files in `conf/explore/application-graphinsights.yml` for Explore settings and
`conf/graphinsights/cmem.integration.config.yml` for Graph Insights settings.

The deployment definition can be found here `extensions/docker-compose.graphinsights.yml`


## Using separate OAuth clients for Graph Insights

TBD
