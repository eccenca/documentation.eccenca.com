---
title: "API Reference"
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
    navigation on the left.

| Module | Description |
| :----- | :---------- |
| [abc](auth_provider/abc.md) | Abstract base class and factory for authentication providers. |
| [client_credentials](auth_provider/client_credentials.md) | Client Credentials OAuth 2.0 flow authentication provider. |
| [password](auth_provider/password.md) | Resource Owner Password OAuth 2.0 flow authentication provider. |
| [prefetched_token](auth_provider/prefetched_token.md) | Prefetched token authentication provider. |
| [provided_token](auth_provider/provided_token.md) | Provided token authentication provider. |
| [client](client.md) | Main API client for eccenca Corporate Memory. |
| [deployment](components/deployment.md) | Corporate Memory deployment status component. |
| [graph_store](components/graph_store.md) | Corporate Memory DataPlatform (explore) graph store management. |
| [marketplace](components/marketplace.md) | eccenca Marketplace server integration. |
| [sparql_wrapper](components/sparql_wrapper.md) | SPARQL Wrapper for eccenca Corporate Memory |
| [workspace](components/workspace.md) | Corporate Memory DataIntegration (build) workspace management. |
| [config](config.md) | Configuration management for the Corporate Memory client. |
| [exceptions](exceptions.md) | Custom exception classes for the cmem_client package. |
| [logging_utils](logging_utils.md) | Logging utilities. |
| [access_condition](models/access_condition.md) | Access control and authorization models for Corporate Memory. |
| [base](models/base.md) | Base model classes for all cmem_client data models. |
| [common](models/common.md) | Shared domain models used across multiple resource types. |
| [credentials](models/credentials.md) | Models for the OAuth2 credentials. |
| [dataset](models/dataset.md) | Corporate Memory dataset models for data integration. |
| [error](models/error.md) | Error response models for Corporate Memory API error handling. |
| [graph](models/graph.md) | RDF graph models for Corporate Memory knowledge graphs. |
| [graph_import](models/graph_import.md) | Graph import models for Corporate Memory. |
| [graph_insight](models/graph_insight.md) | Graph Insight models for Corporate Memory. |
| [item](models/item.md) | ImportItem base class and inherited classes |
| [keycloak_client](models/keycloak_client.md) | Keycloak client models. |
| [logging_config](models/logging_config.md) | Models for the configuration of the logging module |
| [marshalling_plugins](models/marshalling_plugins.md) | Marshalling Plugin models |
| [package](models/package.md) | Marketplace package models. |
| [project](models/project.md) | Corporate Memory project models and metadata. |
| [python_install](models/python_install.md) | Result models for Python package installation and plugin management operations. |
| [python_package](models/python_package.md) | Python package models. |
| [query_catalog](models/query_catalog.md) | Models for query catalog operations. |
| [resource](models/resource.md) | A file resource model |
| [scheduler](models/scheduler.md) | Scheduler models |
| [status](models/status.md) | Models for Corporate Memory aggregated status information. |
| [task](models/task.md) | Task models for the DataIntegration task endpoint. |
| [token](models/token.md) | Authentication token models for OAuth 2.0 flows. |
| [url](models/url.md) | HTTP URL validation and manipulation utilities. |
| [user](models/user.md) | Keycloak user and group models. |
| [validation](models/validation.md) | Validation models for SHACL batch validation processes. |
| [variable](models/variable.md) | Corporate Memory project variable models for data integration. |
| [vocabulary](models/vocabulary.md) | Vocabulary models for Corporate Memory vocabulary catalog. |
| [workflow](models/workflow.md) | Workflow models |
| [workspace_config](models/workspace_config.md) | Corporate Memory Explore workspace configuration models. |
| [workspace_plugin](models/workspace_plugin.md) | Workspace plugin model. |
| [workspace_status](models/workspace_status.md) | Corporate Memory DataIntegration workspace status models. |
| [access_conditions](repositories/access_conditions.md) | Repository for the access conditions of Corporate Memory. |
| [abc](repositories/base/abc.md) | Abstract base classes and configuration for CMEM repositories. |
| [paged_list](repositories/base/paged_list.md) | Repository implementation for paginated API endpoints. |
| [plain_list](repositories/base/plain_list.md) | Repository implementation for simple list API endpoints. |
| [task_search](repositories/base/task_search.md) | Repository implementation for Corporate Memory task search endpoints. |
| [client_accounts](repositories/client_accounts.md) | Repository for the Keycloak OpenID Connect client accounts of a deployment. |
| [datasets](repositories/datasets.md) | Repository for managing datasets in Corporate Memory. |
| [files](repositories/files.md) | Repository for the file resources of DataIntegration projects. |
| [graph_imports](repositories/graph_imports.md) | Repository for the `owl:imports` relations between named graphs. |
| [graph_insights](repositories/graph_insights.md) | Repository for the Graph Insights snapshots of Corporate Memory. |
| [graphs](repositories/graphs.md) | Repository for managing named graphs in Corporate Memory. |
| [marketplace_packages](repositories/marketplace_packages.md) | Repository for the marketplace packages installed in Corporate Memory. |
| [projects](repositories/projects.md) | Repository for managing DataIntegration projects. |
| [create_item](repositories/protocols/create_item.md) | Protocol interface for repository item creation operations. |
| [delete_item](repositories/protocols/delete_item.md) | Protocol interface for repository item deletion operations. |
| [export_item](repositories/protocols/export_item.md) | Protocol interface for repository item export operations. |
| [import_item](repositories/protocols/import_item.md) | Protocol interface for repository item import operations. |
| [update_item](repositories/protocols/update_item.md) | Protocol interface for repository item update operations. |
| [python_packages](repositories/python_packages.md) | Repository for the Python packages installed in DataIntegration. |
| [queries](repositories/queries.md) | Repository for managing queries from the Corporate Memory query catalog. |
| [schedulers](repositories/schedulers.md) | Repository for the workflow schedulers of DataIntegration. |
| [user_accounts](repositories/user_accounts.md) | Repository for the Keycloak user accounts of a Corporate Memory deployment. |
| [validations](repositories/validations.md) | Repository for the SHACL validation batches of Corporate Memory. |
| [variables](repositories/variables.md) | Repository for the variables of DataIntegration projects. |
| [vocabularies](repositories/vocabularies.md) | Repository for managing vocabularies in Corporate Memory. |
| [workflows](repositories/workflows.md) | Repository for the workflows of DataIntegration projects. |
| [workspace_configs](repositories/workspace_configs.md) | Repository for the custom workspace configurations of DataIntegration. |
