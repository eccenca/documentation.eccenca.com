---
icon: material/download-circle-outline
---
# Installation

This page describes proven deployment scenarios for eccenca Corporate Memory.

All Corporate Memory components are distributed as Docker images and can be obtained from eccenca's container repository service.
To run them you need a Docker enabled Linux server.

Corporate Memory uses Ontotext GraphDB triple store as default backend.
Graphdb is available as free version and does not requires a license.
You need to copy your license for Ontotext GraphDB to the `license` folder inside Corporate Memory's root folder.

``` shell
# create the License folder within ${HOME}/cmem-orchestration
mkdir -p licenses
#copy YOUR-LICENSE-FILE
cp YOUR_SE_LICENSE_FILE \
  ${HOME}/cmem-orchestration-VERSION/licenses/graphdb-se.license
# or
cp YOUR_EE_LICENSE_FILE \
  ${HOME}/cmem-orchestration-VERSION/licenses/graphdb-ee.license
```

## Operating Systems (OS)

Corporate Memory is tested on Ubuntu 24.04 (backward compatible with LTS versions older than that) as Debian 11, 12 and 13.

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

[Docker Compose](https://docs.docker.com/compose/) is a convenient way to provision several Docker containers locally for development
setups or on remote servers for single node setups.

eccenca is heavily using `docker compose` for all kinds of internal and customer deployments.
For more details on how to use `docker compose` based orchestration refer
to [Scenario: Local Installation](../installation/scenario-local-installation/index.md) and [Scenario: Single Node Cloud Installation](../installation/scenario-single-node-cloud-installation/index.md).

## Helm based Kubernetes deployment

Most production deployments are Kubernetes based.
We have deployments in AWS (EKS), Azure (AKS), Red Hat Openshift and self-hosted clusters.
We provide Charts for Corporate Memory and Keycloak at our [Helm Repository](https://helm.eccenca.com).
For more details on how to use `helm` based deployments refer
to [Scenario: Kubernetes Deployment](../installation/scenario-k8s-deployment/index.md).
