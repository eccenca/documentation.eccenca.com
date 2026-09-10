---
title: "cmem-client: components.graph_store module"
description: "Corporate Memory DataPlatform (explore) graph store management."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.graph_store` {#cmem_client.components.graph_store}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory DataPlatform (explore) graph store management.

This module provides the GraphStore component for managing Corporate Memory's
DataPlatform graph store. The graph store is the primary repository for RDF
data and knowledge graphs, supporting semantic queries and exploration.

The GraphStore component provides high-level administrative operations including
bootstrap data management, full store backup and restoration, and system
information retrieval. These operations are essential for store maintenance,
deployment, and operational monitoring.

**Classes:**

- [**AdminOperationStatus**](#cmem_client.components.graph_store.AdminOperationStatus) – Current administrative operation reported by GET /api/admin/status.
- [**GraphStore**](#cmem_client.components.graph_store.GraphStore) – High-level interface for Corporate Memory DataPlatform graph store operations.
- [**StoreInformation**](#cmem_client.components.graph_store.StoreInformation) – Information about the graph store instance and its capabilities.

**Attributes:**

- [**AUTHORIZATION_GRAPH_URI**](#cmem_client.components.graph_store.AUTHORIZATION_GRAPH_URI) – The URI of the access conditions graph. Deleting or importing this graph requires an authorization refresh.

## `AUTHORIZATION_GRAPH_URI` {#cmem_client.components.graph_store.AUTHORIZATION_GRAPH_URI}

```python
AUTHORIZATION_GRAPH_URI = 'https://ns.eccenca.com/data/ac/'
```

The URI of the access conditions graph. Deleting or importing this graph requires an authorization refresh.

## `AdminOperationStatus` {#cmem_client.components.graph_store.AdminOperationStatus}

Bases: <code>StrEnum</code>

Current administrative operation reported by GET /api/admin/status.

**Attributes:**

- [**BACKUP**](#cmem_client.components.graph_store.AdminOperationStatus.BACKUP) –
- [**BOOTSTRAP**](#cmem_client.components.graph_store.AdminOperationStatus.BOOTSTRAP) –
- [**DROP_ALL_GRAPHS**](#cmem_client.components.graph_store.AdminOperationStatus.DROP_ALL_GRAPHS) –
- [**NONE**](#cmem_client.components.graph_store.AdminOperationStatus.NONE) –
- [**RESTORE**](#cmem_client.components.graph_store.AdminOperationStatus.RESTORE) –
- [**SHOWCASE**](#cmem_client.components.graph_store.AdminOperationStatus.SHOWCASE) –

### `BACKUP` {#cmem_client.components.graph_store.AdminOperationStatus.BACKUP}

```python
BACKUP = 'BACKUP'
```

### `BOOTSTRAP` {#cmem_client.components.graph_store.AdminOperationStatus.BOOTSTRAP}

```python
BOOTSTRAP = 'BOOTSTRAP'
```

### `DROP_ALL_GRAPHS` {#cmem_client.components.graph_store.AdminOperationStatus.DROP_ALL_GRAPHS}

```python
DROP_ALL_GRAPHS = 'DROP_ALL_GRAPHS'
```

### `NONE` {#cmem_client.components.graph_store.AdminOperationStatus.NONE}

```python
NONE = 'NONE'
```

### `RESTORE` {#cmem_client.components.graph_store.AdminOperationStatus.RESTORE}

```python
RESTORE = 'RESTORE'
```

### `SHOWCASE` {#cmem_client.components.graph_store.AdminOperationStatus.SHOWCASE}

```python
SHOWCASE = 'SHOWCASE'
```

## `GraphStore` {#cmem_client.components.graph_store.GraphStore}

```python
GraphStore(client)
```

High-level interface for Corporate Memory DataPlatform graph store operations.

The GraphStore component provides administrative and operational methods for
managing the Corporate Memory DataPlatform graph store. It handles store-level
operations including bootstrap data management, full backup and restoration,
and system information retrieval.

This component abstracts the complexities of the DataPlatform API and provides
a convenient interface for common graph store management tasks. It's designed
for administrative operations rather than individual graph manipulation
(use repositories for graph-level operations).

**Attributes:**

- **_client** (<code>[Client](../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance used for API communication.
- **_sparql_wrapper** (<code>[SPARQLWrapper](../../components/sparql_wrapper/index.md#cmem_client.components.sparql_wrapper.SPARQLWrapper)</code>) – SPARQLWrapper instance for rdflib SPARQL queries.

<details class="administrative-operations" open markdown="1">
<summary>Administrative Operations</summary>

- Full store backup and restoration
- Bootstrap data management (system vocabularies, etc.)

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

For individual graph operations, use the repositories.graphs module
which provides CRUD operations for specific RDF graphs.

</details>

**Functions:**

- [**create_showcase_data**](#cmem_client.components.graph_store.GraphStore.create_showcase_data) – Create showcase data in the graph store.
- [**delete_bootstrap_data**](#cmem_client.components.graph_store.GraphStore.delete_bootstrap_data) – Delete bootstrap data from the graph store.
- [**export_to_zip**](#cmem_client.components.graph_store.GraphStore.export_to_zip) – Export a complete backup of the graph store as a ZIP archive.
- [**import_bootstrap_data**](#cmem_client.components.graph_store.GraphStore.import_bootstrap_data) – Import or update bootstrap data in the graph store.
- [**import_from_zip**](#cmem_client.components.graph_store.GraphStore.import_from_zip) – Import and restore a complete graph store backup from a ZIP archive.

Creates a GraphStore component that uses the provided client for
API communication with the DataPlatform graph store.

**Parameters:**

- **client** (<code>[Client](../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

<details class="note" open markdown="1">
<summary>Note</summary>

This constructor is typically called automatically by the
Client class when accessing the store property. Direct
instantiation is rarely needed in normal usage.

</details>

### `create_showcase_data` {#cmem_client.components.graph_store.GraphStore.create_showcase_data}

```python
create_showcase_data(scale_factor=None)
```

Create showcase data in the graph store.

Inserts a showcase scenario of multiple graphs including integration
graphs, shapes, statement annotations, etc. Useful for demonstration
and testing environments.

**Parameters:**

- **scale_factor** (<code>int | None</code>) – Multiplies the default showcase dataset by this factor.
A value of 10 results in around 40k triples, a value of

50 in around 350k triples. Defaults to the server default when None.

**Raises:**

- <code>HTTPError</code> – If the showcase creation request fails due to network
issues or server errors.

### `delete_bootstrap_data` {#cmem_client.components.graph_store.GraphStore.delete_bootstrap_data}

```python
delete_bootstrap_data()
```

Delete bootstrap data from the graph store.

Warning: This operation removes system vocabularies and foundational
RDF data required for proper Corporate Memory operation. Use with extreme caution.

Removes all bootstrap data including system vocabularies, ontologies,
and other foundational RDF graphs. This is typically used for cleanup
during testing, or system reset.

**Raises:**

- <code>HTTPError</code> – If the bootstrap deletion request fails due to network
issues or server errors.

<details class="caution" open markdown="1">
<summary>Caution</summary>

After deleting bootstrap data, the Corporate Memory system may not
function correctly until new bootstrap data is imported. This
operation should typically be followed by import_bootstrap_data().

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- System reset during testing
- Troubleshooting corrupted system vocabularies
- Development environment reset

</details>

### `export_to_zip` {#cmem_client.components.graph_store.GraphStore.export_to_zip}

```python
export_to_zip(path)
```

Export a complete backup of the graph store as a ZIP archive.

Creates a full backup of the entire Corporate Memory DataPlatform graph store,
including all RDF graphs, system vocabularies, and metadata. The backup is
streamed directly to the specified file path as a compressed ZIP archive.

This operation creates a point-in-time snapshot that can be used for:

- Disaster recovery and backup strategies
- Environment migration and cloning
- System maintenance and testing
- Data archival and compliance requirements

**Parameters:**

- **path** (<code>Path</code>) – The file system path where the ZIP backup archive will be saved.
The path should include the .zip extension and the parent directory

must exist and be writable.

**Raises:**

- <code>HTTPError</code> – If the backup request fails due to network issues, server
errors, or insufficient permissions.
- <code>OSError</code> – If the specified path cannot be written to due to file system
permissions or disk space issues.

<details class="performance-notes" open markdown="1">
<summary>Performance Notes</summary>

- The backup is streamed directly to disk to minimize memory usage
- Large stores may take significant time to back up completely
- Network bandwidth and storage I/O will impact backup duration
- The operation blocks until the entire backup is complete

</details>

<details class="security-considerations" open markdown="1">
<summary>Security Considerations</summary>

- Backup files contain all graph data and should be stored securely
- Consider encryption for sensitive data in backup archives
- Ensure appropriate access controls on backup storage locations
- Backup files may contain authentication tokens or sensitive metadata

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

Use import_from_zip() to restore from backup archives created by this method.

</details>

### `import_bootstrap_data` {#cmem_client.components.graph_store.GraphStore.import_bootstrap_data}

```python
import_bootstrap_data()
```

Import or update bootstrap data in the graph store.

Bootstrap data includes system vocabularies, ontologies, and other
foundational RDF data required for proper Corporate Memory operation.
This operation ensures the store contains all necessary system-level
graphs and vocabularies.

**Raises:**

- <code>HTTPError</code> – If the bootstrap import request fails due to network
issues or server errors.

<details class="note" open markdown="1">
<summary>Note</summary>

This operation may take some time.
It's typically performed during system initialization or when
updating to new Corporate Memory versions that include new
system vocabularies.

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- Initial system setup
- System updates with new vocabularies
- Recovery after bootstrap data corruption

</details>

### `import_from_zip` {#cmem_client.components.graph_store.GraphStore.import_from_zip}

```python
import_from_zip(path)
```

Import and restore a complete graph store backup from a ZIP archive.

Warning: This operation replaces ALL existing data in the graph store.
All current graphs, vocabularies, and metadata will be permanently deleted
and replaced with the contents of the backup archive.

Restores a Corporate Memory DataPlatform graph store from a ZIP backup
archive created by export_to_zip(). The restoration process completely
replaces the current store contents with the archived data, effectively
rolling back the store to the state captured in the backup.

**Parameters:**

- **path** (<code>Path</code>) – The file system path to the ZIP backup archive to import.
The file must be a valid backup archive created by export_to_zip()

or compatible with the Corporate Memory backup format.

**Raises:**

- <code>HTTPError</code> – If the restore request fails due to network issues, server
errors, insufficient permissions, or invalid backup format.
- <code>OSError</code> – If the specified backup file cannot be read due to file system
permissions or if the file does not exist.
- <code>ValidationError</code> – If the backup archive format is invalid or corrupted.

<details class="important-warnings" open markdown="1">
<summary>Important Warnings</summary>

- **Data Loss**: All existing graphs and data will be permanently deleted
- **Downtime**: The store may be unavailable during the restoration process
- **Irreversible**: This operation cannot be undone without another backup
- **Compatibility**: Ensure backup compatibility with current store version

</details>

<details class="performance-notes" open markdown="1">
<summary>Performance Notes</summary>

- Large backup archives may take significant time to restore
- The store will be unavailable during the restoration process
- Network bandwidth and storage I/O will impact restoration duration
- Memory usage is optimized through streaming file upload

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- Disaster recovery from catastrophic data loss
- Environment synchronization and cloning
- Rolling back to known good state after issues
- Migrating data between Corporate Memory instances
- Testing and development environment setup

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

Use export_to_zip() to create backup archives for import with this method.

</details>

### `logger` {#cmem_client.components.graph_store.GraphStore.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `self_information` {#cmem_client.components.graph_store.GraphStore.self_information}

```python
self_information: StoreInformation
```

Get metadata and version information about the graph store instance.

Retrieves information about the Corporate Memory DataPlatform
graph store, including the store implementation type and version.

The information is fetched from the store's actuator endpoint, which
provides real-time metadata about the running graph store instance.

**Returns:**

- **StoreInformation** (<code>[StoreInformation](#cmem_client.components.graph_store.StoreInformation)</code>) – A model containing store type and version information.
The returned object includes the store implementation name

(e.g., "GRAPHDB", "TENTRIS") and its version string.

**Raises:**

- <code>HTTPError</code> – If the information request fails due to network issues,
server errors, or insufficient permissions to access actuator endpoints.
- <code>ValidationError</code> – If the response cannot be parsed as valid store
information due to unexpected response format.

<details class="performance-notes" open markdown="1">
<summary>Performance Notes</summary>

- This property makes a live HTTP request on each access
- Consider caching the result if accessed frequently
- The actuator endpoint is typically lightweight and fast-responding
- Network latency will impact response time for this property

</details>

<details class="security-notes" open markdown="1">
<summary>Security Notes</summary>

- Actuator endpoints may reveal system information
- Ensure appropriate access controls on actuator endpoints
- Store version information should be treated as potentially sensitive

</details>

### `sparql` {#cmem_client.components.graph_store.GraphStore.sparql}

```python
sparql: SPARQLWrapper
```

Get a SPARQLWrapper instance for rdflib-based SPARQL queries.

Returns a SPARQLWrapper component configured with authentication
for executing SPARQL queries using rdflib. The wrapper provides
access to the Corporate Memory SPARQL endpoint with automatic
authentication handling.

**Returns:**

- <code>[SPARQLWrapper](../../components/sparql_wrapper/index.md#cmem_client.components.sparql_wrapper.SPARQLWrapper)</code> – The SPARQLWrapper component instance, created lazily on first access.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> sparql_wrapper = client.store.sparql
```

## `StoreInformation` {#cmem_client.components.graph_store.StoreInformation}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Information about the graph store instance and its capabilities.

This model represents metadata about the DataPlatform graph store,
including the store type and version information. This information
is useful for compatibility checks, monitoring, and debugging.

**Attributes:**

- [**type**](#cmem_client.components.graph_store.StoreInformation.type) (<code>str</code>) – The type of graph store (e.g., "GRAPHDB", "TENTRIS").
- [**version**](#cmem_client.components.graph_store.StoreInformation.version) (<code>str</code>) – The version string of the graph store implementation.

### `model_config` {#cmem_client.components.graph_store.StoreInformation.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `type` {#cmem_client.components.graph_store.StoreInformation.type}

```python
type: str
```

The type/implementation of the graph store (e.g., "GRAPHDB", "TENTRIS").

### `version` {#cmem_client.components.graph_store.StoreInformation.version}

```python
version: str
```

The version string of the graph store implementation.

