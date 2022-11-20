---
title: "Deployment: Requirements"
icon: material/exclamation-thick
---
# Requirements

This page lists software and hardware requirements for eccenca Corporate Memory deployments.
For a general overview of a deployment setup please refer to the [System Architecture](../system-architecture/index.md).

## Minimal Setup

A minimal single-node deployment for testing/evaluation purposes means:

- no memory consuming linking and transformation workflows,
- nearly no concurrent users.

Depending on how much RAM is dedicated to the triple store, Knowledge Graphs up to several million triples can be built and served.

- Operating System / Hardware
    - Bare metal server or VM with Debian based linux OS (see [Installation](./../installation/index.md) for details)
    - 16 GB RAM
    - 100 GB free disk space (10 GB for docker images + data + logs over time)
    - docker and docker-compose (we deliver an orchestration including all needed components)

For an example of a single-node installation refer to the following scenarios:

- [Scenario: Local Installation](../installation/scenario-local-installation/index.md)
- [Scenario: RedHat Enterprise Linux 7](../installation/scenario-redhat-enterprise-linux-7/index.md)
- [Scenario: Single Node Cloud Installation](../installation/scenario-single-node-cloud-installation/index.md)

## Typical Setup

In a typical deployment all components are installed on separate VMs (nodes).
Therefore, six separate VMs are required.

The following numbers are based on existing customer deployments running Knowledge Graphs up to 300 million triples with 40 concurrent users.

| Component                    | CPU     | Memory |
| ---------------------------: | :------ | :---------- |
| eccenca DataPlatform         | \>= 4 cores[^u] | \>= 8 GB RAM |
| eccenca DataIntegration      | \>= 4 cores[^w] | \>= 8 GB RAM[^w] |
| eccenca DataManager          | 2 cores | \>= 2 GB RAM |
| Triple / Quad Store          | \>= 4 cores[^u] |\>= 8 GB RAM[^t] |
| Keycloak incl. PostgeSQL[^c] | 2 cores | \>= 4 GB RAM |
| Proxy Server[^c]             | \>= 2 cores[^u] | \>= 2 GB RAM |

## Clients

### Browser / Web Client

We support all (LTS/ESR) versions of the below listed browsers that are actively supported be the respective publishers:

- Microsoft Edge > v88.0
- Google Chrome or Chromium > v92.0
- Firefox > v78.0

!!! note

    Internet Explorer 11 as well as Safari Browser are not officially supported. IE11 is reported not to work.

### Command Line Client (cmemc)

For cmemc, currently Python 3.9 is supported, but Python 3.10 is reported to work as well.

There is also a [docker image](../../automate/cmemc-command-line-interface/invocation/docker-image/index.md) available.

[^u]: Needs to be scaled with concurrent users.
[^w]: Depends on the DataIntegration workflows.
[^t]: Needs to be scaled with the amount of triples.
[^c]: In cloud deployments, this could / will be a cloud service.
