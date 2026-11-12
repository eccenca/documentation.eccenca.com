---
title: "cmem-client: components.explore.component module"
description: "Corporate Memory Explore (DataPlatform) component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.explore.component` {#cmem_client.components.explore.component}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory Explore (DataPlatform) component.

The Explore component bundles the operations of the Explore service which are not
collections of items: the SPARQL endpoint, administrative status, bootstrap and showcase
data, full backup and restore, and information about the graph store instance. Each of
these lives in its own module of this package; this class only delegates to them.

**Classes:**

- [**Explore**](#cmem_client.components.explore.component.Explore) – High-level interface for the Corporate Memory Explore (DataPlatform) service.

**Attributes:**

- [**AUTHORIZATION_GRAPH_URI**](#cmem_client.components.explore.component.AUTHORIZATION_GRAPH_URI) – The URI of the access conditions graph. Deleting or importing this graph requires an authorization refresh.

## `AUTHORIZATION_GRAPH_URI` {#cmem_client.components.explore.component.AUTHORIZATION_GRAPH_URI}

```python
AUTHORIZATION_GRAPH_URI = 'https://ns.eccenca.com/data/ac/'
```

The URI of the access conditions graph. Deleting or importing this graph requires an authorization refresh.

## `Explore` {#cmem_client.components.explore.component.Explore}

```python
Explore(client)
```

High-level interface for the Corporate Memory Explore (DataPlatform) service.

The Explore component provides administrative and operational methods for
managing the Corporate Memory DataPlatform graph store. It handles store-level
operations including bootstrap data management, full backup and restoration,
and system information retrieval.

This component abstracts the complexities of the DataPlatform API and provides
a convenient interface for common graph store management tasks. It is designed
for administrative operations rather than individual graph manipulation
(use repositories for graph-level operations).

**Attributes:**

- **_client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance used for API communication.
- **_sparql_wrapper** (<code>[SPARQLWrapper](../../../components/explore/sparql/index.md#cmem_client.components.explore.sparql.SPARQLWrapper)</code>) – SPARQLWrapper instance for rdflib SPARQL queries.

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

- [**create_showcase_data**](#cmem_client.components.explore.component.Explore.create_showcase_data) – Create showcase data in the graph store.
- [**delete_bootstrap_data**](#cmem_client.components.explore.component.Explore.delete_bootstrap_data) – Delete bootstrap data from the graph store.
- [**export_to_zip**](#cmem_client.components.explore.component.Explore.export_to_zip) – Export a complete backup of the graph store as a ZIP archive.
- [**get_health**](#cmem_client.components.explore.component.Explore.get_health) – Report version and health of the Explore (DataPlatform) service.
- [**get_shapes_health**](#cmem_client.components.explore.component.Explore.get_shapes_health) – Report version and health of the shapes catalog served by Explore.
- [**import_bootstrap_data**](#cmem_client.components.explore.component.Explore.import_bootstrap_data) – Import or update bootstrap data in the graph store.
- [**import_from_zip**](#cmem_client.components.explore.component.Explore.import_from_zip) – Import and restore a complete graph store backup from a ZIP archive.
- [**wait_for_admin_idle**](#cmem_client.components.explore.component.Explore.wait_for_admin_idle) – Poll the administrative status until no administrative operation is in progress.

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

<details class="note" open markdown="1">
<summary>Note</summary>

This constructor is typically called automatically by the
Client class when accessing the store property. Direct
instantiation is rarely needed in normal usage.

</details>

### `create_showcase_data` {#cmem_client.components.explore.component.Explore.create_showcase_data}

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

### `delete_bootstrap_data` {#cmem_client.components.explore.component.Explore.delete_bootstrap_data}

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

### `export_to_zip` {#cmem_client.components.explore.component.Explore.export_to_zip}

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

### `get_health` {#cmem_client.components.explore.component.Explore.get_health}

```python
get_health()
```

Report version and health of the Explore (DataPlatform) service.

Reads the service's `/actuator/info` and `/actuator/health`. Both answers are kept
in the result: `info` also carries the store block (type and version of the graph
store), and is only set when both requests succeed.

**Returns:**

- <code>[ExploreStatus](../../../models/status/index.md#cmem_client.models.status.ExploreStatus)</code> – The status of Explore. An unreachable or failing service is reported DOWN with
- <code>[ExploreStatus](../../../models/status/index.md#cmem_client.models.status.ExploreStatus)</code> – the error, instead of raising.

### `get_shapes_health` {#cmem_client.components.explore.component.Explore.get_shapes_health}

```python
get_shapes_health()
```

Report version and health of the shapes catalog served by Explore.

Reads the version the shapes catalog graph declares, with a SPARQL query.

**Returns:**

- <code>[ComponentStatus](../../../models/status/index.md#cmem_client.models.status.ComponentStatus)</code> – The status of the shapes catalog: UP with its version, DOWN without a version
- <code>[ComponentStatus](../../../models/status/index.md#cmem_client.models.status.ComponentStatus)</code> – or with the error of a failing query, instead of raising.

### `import_bootstrap_data` {#cmem_client.components.explore.component.Explore.import_bootstrap_data}

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
It is typically performed during system initialization or when
updating to new Corporate Memory versions that include new
system vocabularies.

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- Initial system setup
- System updates with new vocabularies
- Recovery after bootstrap data corruption

</details>

### `import_from_zip` {#cmem_client.components.explore.component.Explore.import_from_zip}

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

### `logger` {#cmem_client.components.explore.component.Explore.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `logs` {#cmem_client.components.explore.component.Explore.logs}

```python
logs: ExploreLogs = ExploreLogs(client=client)
```

The in-memory log buffer of Explore: the most recent lines and the state of the buffer.

### `self_information` {#cmem_client.components.explore.component.Explore.self_information}

```python
self_information: StoreInformation
```

Get metadata and version information about the graph store instance.

Retrieves information about the Corporate Memory DataPlatform
graph store, including the store implementation type and version.

The information is fetched from the store's actuator endpoint, which
provides real-time metadata about the running graph store instance.

**Returns:**

- **StoreInformation** (<code>[StoreInformation](../../../models/explore/index.md#cmem_client.models.explore.StoreInformation)</code>) – A model containing store type and version information.
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

### `sparql` {#cmem_client.components.explore.component.Explore.sparql}

```python
sparql: SPARQLWrapper
```

Get a SPARQLWrapper instance for rdflib-based SPARQL queries.

Returns a SPARQLWrapper component configured with authentication
for executing SPARQL queries using rdflib. The wrapper provides
access to the Corporate Memory SPARQL endpoint with automatic
authentication handling.

**Returns:**

- <code>[SPARQLWrapper](../../../components/explore/sparql/index.md#cmem_client.components.explore.sparql.SPARQLWrapper)</code> – The SPARQLWrapper component instance, created lazily on first access.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> sparql_wrapper = client.explore.sparql
```

### `titles` {#cmem_client.components.explore.component.Explore.titles}

```python
titles: ExploreTitles = ExploreTitles(client=client)
```

Human-readable titles of IRIs, resolved in batches and cached.

### `wait_for_admin_idle` {#cmem_client.components.explore.component.Explore.wait_for_admin_idle}

```python
wait_for_admin_idle(timeout=60.0, poll_interval=1.0)
```

Poll the administrative status until no administrative operation is in progress.

Administrative operations such as import_bootstrap_data() or create_showcase_data()
are asynchronous on the server: the method call returns as soon as the operation has
been accepted, not once it has finished. Call this method afterward to wait until the
operation has actually completed before relying on its effects, for example before
reading the graphs it wrote.

**Parameters:**

- **timeout** (<code>float</code>) – Maximum seconds to wait before raising TimeoutError.
- **poll_interval** (<code>float</code>) – Seconds to wait between status checks.

**Raises:**

- <code>TimeoutError</code> – If an administrative operation is still in progress after timeout seconds.
- <code>HTTPError</code> – If a status request fails.

