---
tags:
    - Configuration
    - Docker
    - Volume
    - Filesystem
    - Load Balancer
---
# Caveats

## Filesystem in Volumes

!!! info

    Please avoid to deploy on NFS (AWS EFS) volumes, use block storage instead (e.g. AWS EBS).

In Kubernetes deployments in AWS we saw issues with volumes based on NFS, such as Amazon EFS (Elastic File System).

For DataIntegration Python Plugins we noticed issues: see [Sharing the `PYTHONPATH` via NFS](../../../develop/python-plugins/installation/index.md#known-issues)

For GraphDB we saw issues when trying to recover from a previous backups.
This is because NFS behaves different why trying to delete files.
In Fact GraphDB requires to store the data on EBS (Elastic Block Storage) volumes.
See [GraphDB technical-requirements](https://graphdb.ontotext.com/documentation/10.7/aws-deployment.html#technical-requirements).

## Load Balancer

Depending on the deployment, load balancers or proxies in between Corporate Memory components (such as DataIntegration - DataPlatform, DataPlatform - Database Triplestore) tend to drop long running TCP connections when they are idle.
As e.g. SPARQL Update requests may be idle for a long time (while the update is performed) the client will not receive the response.
Hence, DI workflow execution will not proceed even though the update went through.

Similar problems can occur between the connection between DataPlatform and GraphDB.

In addition to the hints in the next sections you can always change the TCP keep-alive of the system hosting the containers.
However in cloud environments this often isn't practical. In Debian based Linux distribution you have to edit `/etc/sysctl.conf`.
But be advised, only do this, if you are aware of the risks.

``` unixconfig
net.ipv4.tcp_keepalive_time = 600
net.ipv4.tcp_keepalive_intvl = 60
net.ipv4.tcp_keepalive_probes = 20
```

### Kubernetes Deployments

In Kubernetes deployments services for each deployment usually use load balancers to connect other services.
However we never saw problems as long as inter-component-communication stays at service level.

In detail, DataIntegration can be set like this in the cmem-helm value file: `.Values.dataintegration.config.dataplatformUrl` or let it defaulting to: `http://dataplatform.namespace:8080/dataplatform`.

To connect to Ontotext GraphDB we emphasize to NOT use external load balancers trough an ingress or similar.
Instead use the internal connection like `graphdb-node.graphdb.cluster.local` at the value `.Values.dataplatform.store.graphdb.host`.

### Container Deployments or distributing over multiple VMs

When deploying Corporate Memory in cloud environments such as EC2 where each component runs on a separate VM,
or using Container Services such as ECS (Amazon Elastic Container Service) or ACI (Azure Container Instances) the same rules apply as in Kubernetes deployments.
For networking make sure to create a Private Network (VPC) instead of bridges to bypass load balancers. [VPN](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-services.html)

DataIntegration is configured with the `ENV` variable `DATAPLATFORM_URL` to set up the connection to DataPlatform or in its config file `dataintegration.conf`.

For DataPlatform you have to set this in `application.yaml` or through `ENV` variables, such as: `STORE_GRAPHDB_HOST`, `STORE_GRAPHDB_PORT` and `STORE_GRAPHDB_SSL_ENABLED`.

### Useful Documentation

-   [AWS VPN Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-services.html)
-   [AWS Network load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html)
-   [GraphDB with load balancers](https://graphdb.ontotext.com/documentation/10.7/aws-deployment.html#setting-up-the-load-balancer)
