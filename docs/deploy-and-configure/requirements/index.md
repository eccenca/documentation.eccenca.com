# Requirements

This page lists software and hardware requirements for eccenca Corporate Memory deployments.

For a general overview of a deployment setup please refer to the [System Architecture](https://documentation.eccenca.com/latest/deploy-and-configure/system-architecture).

## Corporate Memory

### Minimal Setup

A minimal single-node deployment for testing/evaluation purposes means:

- no memory consuming linking and transformation workflows,
- nearly no concurrent users (< 5).

Depending on how much RAM is dedicated to the triple store, Knowledge Graphs up to several million triples can be built and served.

- Operating System / Hardware
      - Bare metal server or VM with Ubuntu or RHEL linux OS (see [Installation](https://documentation.eccenca.com/latest/deploy-and-configure/installation) for details)
      - 16 GB RAM
      - 100 GB free disk space (10 GB for docker images + data + logs over time)
      - docker and docker-compose (we deliver an orchestration including all needed components)
- Triple / Quad Store
      - Stardog 7.4.x
      - Ontotext GraphDB
      - OpenLink Virtuoso Open Source
- Identity Management (delivered with orchestration)
      - Keycloak >= v6.0.1
      - PostgreSQL >= v11.5
- Proxy Server (delivered with orchestration)
      - Apache >=2.4 (incl. rewrite and other modules)

For an example of a single-node installation refer to the following scenarios:

- [Scenario: Local Installation](../installation/scenario-local-installation/index.md)
- [Scenario: RedHat Enterprise Linux 7](../installation/scenario-redhat-enterprise-linux-7/index.md)
- [Scenario: Single Node Cloud Installation](../installation/scenario-single-node-cloud-installation/index.md)

### Typical Setup

In a typical deployment all components are installed on separate VMs (nodes). Therefore, six separate VMs are required.

The following numbers are based on existing customer deployments running Knowledge Graphs up to 300 million triples with 40 concurrent users.

- eccenca DataPlatform
      - \>= 4 cores:regional_indicator_u:
      - \>= 8 GB RAM
- eccenca DataIntegration
      - \>= 4 cores:regional_indicator_w:
      - \>= 8 GB RAM:regional_indicator_w:
- eccenca DataManager
      - \>= 2 GB RAM
- Triple / Quad Store
      - \>= 8 GB RAM:regional_indicator_t:
      - \>= 4 cores:regional_indicator_u:
- KeyCloak incl. PostgeSQL:regional_indicator_c:
      - \>= 4 GB RAM
- Proxy Server:regional_indicator_c:
      - \>= 2 cores:regional_indicator_u:
      - \>= 2 GB RAM

!!! info
    - :regional_indicator_u: needs to be scaled with concurrent users
    - :regional_indicator_w: depends on the DataIntegration workflows
    - :regional_indicator_t: needs to be scaled with the amount of triples
    - :regional_indicator_c: in cloud deployments, this could / will be a cloud service

## Clients

### Browser / Web Client

We support all (LTS/ESR) versions of the below listed browsers that are actively supported be the respective publishers

- Microsoft Edge > v88.0
- Google Chrome or Chromium > v92.0
- Firefox > v78.0

???+ info
    Internet Explorer 11 as well as Safari Browser are not officially supported. IE11 is reported not to work.

### Command Line Client (cmemc)

- Python 3.7
- Installation options:
  
  - pip-based installation
  - single binary / executable available for Ubuntu, RHEL and Microsoft Windows
  - docker image based on the official debian slim image
