---
title: "cmem-client: workspace module"
tags:
  - API
  - Python
  - cmem-client
---

# `workspace` {#cmem_client.components.workspace}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory DataIntegration (build) workspace management.

This module provides the BuildWorkspace component for managing Corporate Memory's
DataIntegration workspace. The workspace contains projects, datasets, transformations,
and other integration artifacts organized in a hierarchical structure.

The BuildWorkspace component provides high-level operations for workspace backup
and restoration, allowing entire workspace snapshots to be exported and imported
as ZIP archives. This is essential for deployment, migration, and disaster recovery
scenarios.

**Classes:**

- [**BuildWorkspace**](#cmem_client.components.workspace.BuildWorkspace) – High-level interface for Corporate Memory DataIntegration workspace operations.

## `BuildWorkspace` {#cmem_client.components.workspace.BuildWorkspace}

```python
BuildWorkspace(client)
```

High-level interface for Corporate Memory DataIntegration workspace operations.

The BuildWorkspace component provides administrative and operational methods for
managing the Corporate Memory DataIntegration (build) workspace. It handles
workspace-level operations including complete backup and restoration of all
workspace contents as ZIP archives.

The workspace contains all DataIntegration artifacts including:

- Projects and their configurations
- Datasets and data sources
- Transformation workflows and mapping rules
- Workflow definitions and scheduling configurations

This component abstracts the complexities of the DataIntegration API and provides
a convenient interface for workspace-wide administrative tasks.

**Attributes:**

- **_client** (<code>[Client](../client.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance used for API communication.

<details class="administrative-operations" open markdown="1">
<summary>Administrative Operations</summary>

- Complete workspace backup and restoration
- Environment synchronization and migration
- Disaster recovery and rollback capabilities
- Deployment automation and CI/CD integration

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

For individual project operations, use the repositories.projects module
which provides CRUD operations for specific DataIntegration projects.

</details>

**Functions:**

- [**export_to_zip**](#cmem_client.components.workspace.BuildWorkspace.export_to_zip) – Export a complete backup of the workspace as a ZIP archive.
- [**get_marshalling_plugins**](#cmem_client.components.workspace.BuildWorkspace.get_marshalling_plugins) – Get the list of marshalling plugins.
- [**get_status**](#cmem_client.components.workspace.BuildWorkspace.get_status) – Get the loading status of the whole workspace.
- [**import_from_zip**](#cmem_client.components.workspace.BuildWorkspace.import_from_zip) – Import and restore a complete workspace backup from a ZIP archive.
- [**reload_workspace**](#cmem_client.components.workspace.BuildWorkspace.reload_workspace) – Reload the workspace.
- [**retrieve_access_control_configuration**](#cmem_client.components.workspace.BuildWorkspace.retrieve_access_control_configuration) – Retrieves the current access control configuration.

Creates a BuildWorkspace component that uses the provided client for
API communication with the DataIntegration workspace endpoints.

**Parameters:**

- **client** (<code>[Client](../client.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

<details class="note" open markdown="1">
<summary>Note</summary>

This constructor is typically called automatically by the
Client class when accessing the workspace property. Direct
instantiation is rarely needed in normal usage.

</details>

### `export_to_zip` {#cmem_client.components.workspace.BuildWorkspace.export_to_zip}

```python
export_to_zip(path, marshalling_plugin='xmlZip', include_access_conditions=False, export_user_data=True)
```

Export a complete backup of the workspace as a ZIP archive.

Creates a comprehensive backup of the entire Corporate Memory DataIntegration
workspace, including all projects, datasets, transformations, vocabularies,
workflows, and configurations. The backup is streamed directly to the
specified file path as a compressed ZIP archive.

This operation creates a point-in-time snapshot of the complete workspace
that can be used for:

- Environment migration and synchronization
- Disaster recovery and backup strategies
- Development and testing environment setup
- Deployment automation and CI/CD pipelines
- Team collaboration and workspace sharing

**Parameters:**

- **path** (<code>Path</code>) – The file system path where the ZIP workspace archive will be saved.
The path should include the .zip extension and the parent directory

must exist and be writable.

- **marshalling_plugin** (<code>str</code>) – The type of marshalling plugin to use.
- **include_access_conditions** (<code>bool</code>) – Whether to include project specific access conditions.
- **export_user_data** (<code>bool</code>) – Whether to include user-identifying metadata (created/modified
timestamps and account names). If False, this data is removed from the archive.

**Raises:**

- <code>HTTPError</code> – If the export request fails due to network issues, server
errors, or insufficient permissions.
- <code>OSError</code> – If the specified path cannot be written to due to file system
permissions or disk space issues.
- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the server reports that the export failed.

<details class="performance-notes" open markdown="1">
<summary>Performance Notes</summary>

- The export is streamed directly to disk to minimize memory usage
- Large workspaces may take significant time to export completely
- Network bandwidth and storage I/O will impact export duration
- The operation blocks until the entire workspace is exported
- Export size depends on workspace complexity and resource files

</details>

<details class="security-considerations" open markdown="1">
<summary>Security Considerations</summary>

- Workspace archives contain all project data and configurations
- May include database connection strings and access credentials
- Should be stored securely with appropriate access controls
- Consider encryption for sensitive workspace data
- Review archive contents before sharing or transferring

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- **Environment Promotion**: Move workspace from dev to production
- **Disaster Recovery**: Regular backups for business continuity
- **Team Onboarding**: Share workspace setups with new team members
- **CI/CD Integration**: Automated workspace deployment pipelines
- **Migration Support**: Transfer workspaces between instances
- **Version Control**: Track workspace state changes over time

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

Use import_from_zip() to restore workspace archives created by this method.

</details>

### `get_marshalling_plugins` {#cmem_client.components.workspace.BuildWorkspace.get_marshalling_plugins}

```python
get_marshalling_plugins()
```

Get the list of marshalling plugins.

### `get_status` {#cmem_client.components.workspace.BuildWorkspace.get_status}

```python
get_status()
```

Get the loading status of the whole workspace.

Reports task loading errors for all projects in a single response.
Only projects with at least one failed task are listed.

**Returns:**

- <code>[WorkspaceStatus](../models/workspace_status.md#cmem_client.models.workspace_status.WorkspaceStatus)</code> – The workspace status, listing the failed tasks per project.

### `import_from_zip` {#cmem_client.components.workspace.BuildWorkspace.import_from_zip}

```python
import_from_zip(path, marshalling_plugin='xmlZip', include_access_conditions=False)
```

Import and restore a complete workspace backup from a ZIP archive.

Warning: This operation overwrites existing workspace content.
All projects, datasets, transformations, and other workspace artifacts will be
replaced or removed during the import process.

Restores a Corporate Memory DataIntegration workspace from a ZIP backup
archive created by export_to_zip(). The import process loads all workspace
artifacts including projects, datasets, transformations, vocabularies,
and configurations from the archive into the current workspace.

**Parameters:**

- **path** (<code>Path</code>) – The file system path to the ZIP backup archive to import.
The file must be a valid workspace backup archive created by

export_to_zip() or compatible with the DataIntegration workspace format.

- **marshalling_plugin** (<code>str</code>) – The type of marshalling plugin to use for import.
- **include_access_conditions** (<code>bool</code>) – Whether to include project specific access conditions.

**Returns:**

- **Response** (<code>Response</code>) – The HTTP response object from the import operation.
Check response.status_code for success (200) and response.json()

for detailed import results and any warnings or errors.

**Raises:**

- <code>HTTPError</code> – If the import request fails due to network issues, server
errors, insufficient permissions, or invalid archive format.
- <code>OSError</code> – If the specified backup file cannot be read due to file system
permissions or if the file does not exist.
- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the server reports that the import failed.

<details class="important-considerations" open markdown="1">
<summary>Important Considerations</summary>

- **Data Validation**: Invalid configurations in the archive may cause failures
- **Dependency Resolution**: Project dependencies must be satisfied after import

</details>

<details class="performance-notes" open markdown="1">
<summary>Performance Notes</summary>

- Large workspace archives may take significant time to import
- The workspace may be partially unavailable during import
- Network bandwidth affects upload speed for large archives
- Import processing time depends on workspace complexity

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- Environment synchronization between development and production
- Workspace migration between Corporate Memory instances
- Disaster recovery from workspace backups
- Deployment automation and CI/CD pipeline integration
- Team collaboration and workspace sharing

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

Use export_to_zip() to create workspace archives for import with this method.

</details>

### `logger` {#cmem_client.components.workspace.BuildWorkspace.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `reload_workspace` {#cmem_client.components.workspace.BuildWorkspace.reload_workspace}

```python
reload_workspace()
```

Reload the workspace.

### `retrieve_access_control_configuration` {#cmem_client.components.workspace.BuildWorkspace.retrieve_access_control_configuration}

```python
retrieve_access_control_configuration()
```

Retrieves the current access control configuration.

