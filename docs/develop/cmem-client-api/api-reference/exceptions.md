---
title: "cmem-client: exceptions module"
description: "Custom exception classes for the cmem_client package."
tags:
  - API
  - Python
  - cmem-client
---

# `exceptions` {#cmem_client.exceptions}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Custom exception classes for the cmem_client package.

This module defines all custom exceptions used throughout the cmem_client library,
providing specific error types for different failure scenarios such as authentication,
configuration, and repository operations.

**Classes:**

- [**BaseError**](#cmem_client.exceptions.BaseError) – Base exception for all cmem_client exceptions.
- [**ClientEnvConfigError**](#cmem_client.exceptions.ClientEnvConfigError) – Exception raised when an environment key is missing.
- [**ClientNoAuthProviderError**](#cmem_client.exceptions.ClientNoAuthProviderError) – Exception raised when no auth provider is given but needed.
- [**FilesDeleteError**](#cmem_client.exceptions.FilesDeleteError) – Exception raised when a file import fails.
- [**FilesExportError**](#cmem_client.exceptions.FilesExportError) – Exception raised when a file export fails.
- [**FilesImportError**](#cmem_client.exceptions.FilesImportError) – Exception raised when a file import fails.
- [**FilesNotFoundError**](#cmem_client.exceptions.FilesNotFoundError) – Exception raised when a file is not found in a project.
- [**FilesReadError**](#cmem_client.exceptions.FilesReadError) – Exception raised when reading the content of a file fails.
- [**GraphExportError**](#cmem_client.exceptions.GraphExportError) – Exception raised when a vocabulary export operation fails.
- [**GraphImportError**](#cmem_client.exceptions.GraphImportError) – Exception raised when a vocabulary import operation fails.
- [**GraphVannMetadataConflictError**](#cmem_client.exceptions.GraphVannMetadataConflictError) – Exception raised when vann namespace metadata in the file conflicts with provided config.
- [**GraphVannMetadataMissingError**](#cmem_client.exceptions.GraphVannMetadataMissingError) – Exception raised when vann namespace metadata is missing from an ontology file.
- [**MarketplaceAuthError**](#cmem_client.exceptions.MarketplaceAuthError) – Exception raised when a marketplace auth operation failed or is invalid.
- [**MarketplaceDeleteError**](#cmem_client.exceptions.MarketplaceDeleteError) – Exception raised when a marketplace delete operation failed or is invalid.
- [**MarketplacePackagesDeleteError**](#cmem_client.exceptions.MarketplacePackagesDeleteError) – Exception raised when a marketplace package deletion fails.
- [**MarketplacePackagesExportError**](#cmem_client.exceptions.MarketplacePackagesExportError) – Exception raised when a marketplace packages export fails.
- [**MarketplacePackagesImportError**](#cmem_client.exceptions.MarketplacePackagesImportError) – Exception raised when a marketplace package installation fails.
- [**MarketplaceReadError**](#cmem_client.exceptions.MarketplaceReadError) – Exception raised when a marketplace read operation failed or is invalid.
- [**MarketplaceWriteError**](#cmem_client.exceptions.MarketplaceWriteError) – Exception raised when a marketplace write operation failed or is invalid.
- [**ProjectExportError**](#cmem_client.exceptions.ProjectExportError) – Exception raised when a project export operation fails.
- [**ProjectImportError**](#cmem_client.exceptions.ProjectImportError) – Exception raised when a project import operation fails.
- [**PythonPackageImportError**](#cmem_client.exceptions.PythonPackageImportError) – Exception raised when a python plugin import fails.
- [**QueryExportError**](#cmem_client.exceptions.QueryExportError) – Exception raised when a query export operation fails.
- [**QueryNotFoundError**](#cmem_client.exceptions.QueryNotFoundError) – Exception raised when a query is not found in the catalog.
- [**QueryUpdateError**](#cmem_client.exceptions.QueryUpdateError) – Exception raised when a query update operation fails.
- [**RepositoryConfigError**](#cmem_client.exceptions.RepositoryConfigError) – Exception raised when a repository configuration is invalid.
- [**RepositoryItemNotFoundError**](#cmem_client.exceptions.RepositoryItemNotFoundError) – Exception raised when a specific item is missing in a repository.
- [**RepositoryModificationError**](#cmem_client.exceptions.RepositoryModificationError) – Exception raised when a repository modification failed or is invalid.
- [**RepositoryReadError**](#cmem_client.exceptions.RepositoryReadError) – Exception raised when a repository read operation failed or is invalid.
- [**VocabularyInstallError**](#cmem_client.exceptions.VocabularyInstallError) – Exception raised when a vocabulary installation fails.
- [**VocabularyUninstallError**](#cmem_client.exceptions.VocabularyUninstallError) – Exception raised when a vocabulary uninstallation fails.
- [**WorkflowExecutionError**](#cmem_client.exceptions.WorkflowExecutionError) – Exception raised when a workflow execution operation failed or is invalid.
- [**WorkflowReadError**](#cmem_client.exceptions.WorkflowReadError) – Exception raised when a workflow read operation failed or is invalid.

## `BaseError` {#cmem_client.exceptions.BaseError}

Bases: <code>Exception</code>

Base exception for all cmem_client exceptions.

## `ClientEnvConfigError` {#cmem_client.exceptions.ClientEnvConfigError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when an environment key is missing.

## `ClientNoAuthProviderError` {#cmem_client.exceptions.ClientNoAuthProviderError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when no auth provider is given but needed.

## `FilesDeleteError` {#cmem_client.exceptions.FilesDeleteError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a file import fails.

## `FilesExportError` {#cmem_client.exceptions.FilesExportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a file export fails.

## `FilesImportError` {#cmem_client.exceptions.FilesImportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a file import fails.

## `FilesNotFoundError` {#cmem_client.exceptions.FilesNotFoundError}

Bases: <code>[RepositoryItemNotFoundError](#cmem_client.exceptions.RepositoryItemNotFoundError)</code>

Exception raised when a file is not found in a project.

## `FilesReadError` {#cmem_client.exceptions.FilesReadError}

Bases: <code>[RepositoryReadError](#cmem_client.exceptions.RepositoryReadError)</code>

Exception raised when reading the content of a file fails.

## `GraphExportError` {#cmem_client.exceptions.GraphExportError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a vocabulary export operation fails.

## `GraphImportError` {#cmem_client.exceptions.GraphImportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a vocabulary import operation fails.

## `GraphVannMetadataConflictError` {#cmem_client.exceptions.GraphVannMetadataConflictError}

Bases: <code>[GraphImportError](#cmem_client.exceptions.GraphImportError)</code>

Exception raised when vann namespace metadata in the file conflicts with provided config.

## `GraphVannMetadataMissingError` {#cmem_client.exceptions.GraphVannMetadataMissingError}

Bases: <code>[GraphImportError](#cmem_client.exceptions.GraphImportError)</code>

Exception raised when vann namespace metadata is missing from an ontology file.

## `MarketplaceAuthError` {#cmem_client.exceptions.MarketplaceAuthError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a marketplace auth operation failed or is invalid.

## `MarketplaceDeleteError` {#cmem_client.exceptions.MarketplaceDeleteError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a marketplace delete operation failed or is invalid.

## `MarketplacePackagesDeleteError` {#cmem_client.exceptions.MarketplacePackagesDeleteError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a marketplace package deletion fails.

## `MarketplacePackagesExportError` {#cmem_client.exceptions.MarketplacePackagesExportError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a marketplace packages export fails.

## `MarketplacePackagesImportError` {#cmem_client.exceptions.MarketplacePackagesImportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a marketplace package installation fails.

## `MarketplaceReadError` {#cmem_client.exceptions.MarketplaceReadError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a marketplace read operation failed or is invalid.

## `MarketplaceWriteError` {#cmem_client.exceptions.MarketplaceWriteError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a marketplace write operation failed or is invalid.

## `ProjectExportError` {#cmem_client.exceptions.ProjectExportError}

Bases: <code>[RepositoryReadError](#cmem_client.exceptions.RepositoryReadError)</code>

Exception raised when a project export operation fails.

## `ProjectImportError` {#cmem_client.exceptions.ProjectImportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a project import operation fails.

## `PythonPackageImportError` {#cmem_client.exceptions.PythonPackageImportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a python plugin import fails.

## `QueryExportError` {#cmem_client.exceptions.QueryExportError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a query export operation fails.

## `QueryNotFoundError` {#cmem_client.exceptions.QueryNotFoundError}

Bases: <code>[RepositoryItemNotFoundError](#cmem_client.exceptions.RepositoryItemNotFoundError)</code>

Exception raised when a query is not found in the catalog.

## `QueryUpdateError` {#cmem_client.exceptions.QueryUpdateError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a query update operation fails.

## `RepositoryConfigError` {#cmem_client.exceptions.RepositoryConfigError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a repository configuration is invalid.

## `RepositoryItemNotFoundError` {#cmem_client.exceptions.RepositoryItemNotFoundError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a specific item is missing in a repository.

## `RepositoryModificationError` {#cmem_client.exceptions.RepositoryModificationError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a repository modification failed or is invalid.

## `RepositoryReadError` {#cmem_client.exceptions.RepositoryReadError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a repository read operation failed or is invalid.

## `VocabularyInstallError` {#cmem_client.exceptions.VocabularyInstallError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a vocabulary installation fails.

## `VocabularyUninstallError` {#cmem_client.exceptions.VocabularyUninstallError}

Bases: <code>[RepositoryModificationError](#cmem_client.exceptions.RepositoryModificationError)</code>

Exception raised when a vocabulary uninstallation fails.

## `WorkflowExecutionError` {#cmem_client.exceptions.WorkflowExecutionError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a workflow execution operation failed or is invalid.

## `WorkflowReadError` {#cmem_client.exceptions.WorkflowReadError}

Bases: <code>[BaseError](#cmem_client.exceptions.BaseError)</code>

Exception raised when a workflow read operation failed or is invalid.

