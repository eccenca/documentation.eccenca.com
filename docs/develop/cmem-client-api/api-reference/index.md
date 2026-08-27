---
title: "API Reference"
description: "This page lists all modules with their short descriptions."
icon: octicons/cross-reference-24
tags:
  - API
  - Python
  - cmem-client
---

# API Reference

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! info

    cmem-client is organized as a package of modules, each documenting one part
    of the Corporate Memory API. Browse them in the table below or in the
    navigation on the left. New to the package? Start with the
    [`client`](client.md) module, the main entry point to the API.

| Module | Description |
| :----- | :---------- |
| [auth_provider.abc](auth_provider/abc/index.md) | Abstract base class and factory for authentication providers. |
| [auth_provider.client_credentials](auth_provider/client_credentials/index.md) | Client Credentials OAuth 2.0 flow authentication provider. |
| [auth_provider.password](auth_provider/password/index.md) | Resource Owner Password OAuth 2.0 flow authentication provider. |
| [auth_provider.prefetched_token](auth_provider/prefetched_token/index.md) | Prefetched token authentication provider. |
| [auth_provider.provided_token](auth_provider/provided_token/index.md) | Provided token authentication provider. |
| [client](client/index.md) | Main API client for eccenca Corporate Memory. |
| [components.deployment](components/deployment/index.md) | Corporate Memory deployment status component. |
| [components.graph_store](components/graph_store/index.md) | Corporate Memory DataPlatform (explore) graph store management. |
| [components.marketplace](components/marketplace/index.md) | eccenca Marketplace server integration. |
| [components.sparql_wrapper](components/sparql_wrapper/index.md) | SPARQL Wrapper for eccenca Corporate Memory |
| [components.workspace](components/workspace/index.md) | Corporate Memory DataIntegration (build) workspace management. |
| [config](config/index.md) | Configuration management for the Corporate Memory client. |
| [exceptions](exceptions/index.md) | Custom exception classes for the cmem_client package. |
| [logging_utils](logging_utils/index.md) | Logging utilities. |
| [models.access_condition](models/access_condition/index.md) | Access control and authorization models for Corporate Memory. |
| [models.base](models/base/index.md) | Base model classes for all cmem_client data models. |
| [models.common](models/common/index.md) | Shared domain models used across multiple resource types. |
| [models.credentials](models/credentials/index.md) | Models for the OAuth2 credentials. |
| [models.dataset](models/dataset/index.md) | Corporate Memory dataset models for data integration. |
| [models.error](models/error/index.md) | Error response models for Corporate Memory API error handling. |
| [models.graph](models/graph/index.md) | RDF graph models for Corporate Memory knowledge graphs. |
| [models.graph_import](models/graph_import/index.md) | Graph import models for Corporate Memory. |
| [models.graph_insight](models/graph_insight/index.md) | Graph Insight models for Corporate Memory. |
| [models.item](models/item/index.md) | ImportItem base class and inherited classes |
| [models.keycloak_client](models/keycloak_client/index.md) | Keycloak client models. |
| [models.logging_config](models/logging_config/index.md) | Models for the configuration of the logging module |
| [models.marshalling_plugins](models/marshalling_plugins/index.md) | Marshalling Plugin models |
| [models.package](models/package/index.md) | Marketplace package models. |
| [models.project](models/project/index.md) | Corporate Memory project models and metadata. |
| [models.python_install](models/python_install/index.md) | Result models for Python package installation and plugin management operations. |
| [models.python_package](models/python_package/index.md) | Python package models. |
| [models.query_catalog](models/query_catalog/index.md) | Models for query catalog operations. |
| [models.resource](models/resource/index.md) | A file resource model |
| [models.scheduler](models/scheduler/index.md) | Scheduler models |
| [models.status](models/status/index.md) | Models for Corporate Memory aggregated status information. |
| [models.task](models/task/index.md) | Task models for the DataIntegration task endpoint. |
| [models.token](models/token/index.md) | Authentication token models for OAuth 2.0 flows. |
| [models.url](models/url/index.md) | HTTP URL validation and manipulation utilities. |
| [models.user](models/user/index.md) | Keycloak user and group models. |
| [models.validation](models/validation/index.md) | Validation models for SHACL batch validation processes. |
| [models.variable](models/variable/index.md) | Corporate Memory project variable models for data integration. |
| [models.vocabulary](models/vocabulary/index.md) | Vocabulary models for Corporate Memory vocabulary catalog. |
| [models.workflow](models/workflow/index.md) | Workflow models |
| [models.workspace_config](models/workspace_config/index.md) | Corporate Memory Explore workspace configuration models. |
| [models.workspace_plugin](models/workspace_plugin/index.md) | Workspace plugin model. |
| [models.workspace_status](models/workspace_status/index.md) | Corporate Memory DataIntegration workspace status models. |
| [repositories.access_conditions](repositories/access_conditions/index.md) | Repository for the access conditions of Corporate Memory. |
| [repositories.base.abc](repositories/base/abc/index.md) | Abstract base classes and configuration for CMEM repositories. |
| [repositories.base.paged_list](repositories/base/paged_list/index.md) | Repository implementation for paginated API endpoints. |
| [repositories.base.plain_list](repositories/base/plain_list/index.md) | Repository implementation for simple list API endpoints. |
| [repositories.base.task_search](repositories/base/task_search/index.md) | Repository implementation for Corporate Memory task search endpoints. |
| [repositories.client_accounts](repositories/client_accounts/index.md) | Repository for the Keycloak OpenID Connect client accounts of a deployment. |
| [repositories.datasets](repositories/datasets/index.md) | Repository for managing datasets in Corporate Memory. |
| [repositories.files](repositories/files/index.md) | Repository for the file resources of DataIntegration projects. |
| [repositories.graph_imports](repositories/graph_imports/index.md) | Repository for the `owl:imports` relations between named graphs. |
| [repositories.graph_insights](repositories/graph_insights/index.md) | Repository for the Graph Insights snapshots of Corporate Memory. |
| [repositories.graphs](repositories/graphs/index.md) | Repository for managing named graphs in Corporate Memory. |
| [repositories.marketplace_packages](repositories/marketplace_packages/index.md) | Repository for the marketplace packages installed in Corporate Memory. |
| [repositories.projects](repositories/projects/index.md) | Repository for managing DataIntegration projects. |
| [repositories.protocols.create_item](repositories/protocols/create_item/index.md) | Protocol interface for repository item creation operations. |
| [repositories.protocols.delete_item](repositories/protocols/delete_item/index.md) | Protocol interface for repository item deletion operations. |
| [repositories.protocols.export_item](repositories/protocols/export_item/index.md) | Protocol interface for repository item export operations. |
| [repositories.protocols.import_item](repositories/protocols/import_item/index.md) | Protocol interface for repository item import operations. |
| [repositories.protocols.update_item](repositories/protocols/update_item/index.md) | Protocol interface for repository item update operations. |
| [repositories.python_packages](repositories/python_packages/index.md) | Repository for the Python packages installed in DataIntegration. |
| [repositories.queries](repositories/queries/index.md) | Repository for managing queries from the Corporate Memory query catalog. |
| [repositories.schedulers](repositories/schedulers/index.md) | Repository for the workflow schedulers of DataIntegration. |
| [repositories.user_accounts](repositories/user_accounts/index.md) | Repository for the Keycloak user accounts of a Corporate Memory deployment. |
| [repositories.validations](repositories/validations/index.md) | Repository for the SHACL validation batches of Corporate Memory. |
| [repositories.variables](repositories/variables/index.md) | Repository for the variables of DataIntegration projects. |
| [repositories.vocabularies](repositories/vocabularies/index.md) | Repository for managing vocabularies in Corporate Memory. |
| [repositories.workflows](repositories/workflows/index.md) | Repository for the workflows of DataIntegration projects. |
| [repositories.workspace_configs](repositories/workspace_configs/index.md) | Repository for the custom workspace configurations of DataIntegration. |
