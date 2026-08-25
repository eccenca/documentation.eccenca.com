# `graphs` {#cmem_client.repositories.graphs}

Repository for managing named graphs in Corporate Memory.

Provides GraphRepository class for managing RDF named graphs with operations for
deletion and import. Supports multiple RDF formats (Turtle, RDF/XML, JSON-LD, N-Triples)
with automatic file type detection.

**Examples:**

List the graphs of a deployment and look one up:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for iri in client.graphs:
...     print(iri, client.graphs[iri].writeable)
```

Import a Turtle file into a graph, export it again and delete it:

```pycon
>>> from pathlib import Path
>>> from cmem_client.repositories.graphs import GraphExportConfig, GraphImportConfig
>>> from cmem_client.repositories.protocols.import_item import ImportConflictPolicy
>>> client.graphs.import_item(
...     path=Path("vocabulary.ttl"),
...     key="https://example.org/vocab/",
...     on_conflict=ImportConflictPolicy.REPLACE,
...     configuration=GraphImportConfig(register_as_vocabulary=True),
... )
>>> client.graphs.export_item(
...     key="https://example.org/vocab/",
...     path=Path("export.ttl"),
...     configuration=GraphExportConfig(resolve_owl_imports=True),
... )
>>> client.graphs.delete_item("https://example.org/vocab/")
```

Detect the serialization of a file before importing it:

```pycon
>>> client.graphs.guess_file_type(path=Path("vocabulary.ttl")).mime_type
```

**Classes:**

- [**GraphDeleteConfig**](#cmem_client.repositories.graphs.GraphDeleteConfig) – Graph Delete Configuration.
- [**GraphExportConfig**](#cmem_client.repositories.graphs.GraphExportConfig) – Graph Export Configuration.
- [**GraphFileSerialization**](#cmem_client.repositories.graphs.GraphFileSerialization) – Supported graph format description
- [**GraphImportConfig**](#cmem_client.repositories.graphs.GraphImportConfig) – Graph Import Configuration.
- [**GraphsRepository**](#cmem_client.repositories.graphs.GraphsRepository) – Repository for graphs.

**Attributes:**

- [**GET_ONTOLOGY_IRI_QUERY**](#cmem_client.repositories.graphs.GET_ONTOLOGY_IRI_QUERY) –
- [**GET_PREFIX_DECLARATION**](#cmem_client.repositories.graphs.GET_PREFIX_DECLARATION) –
- [**INSERT_CATALOG_ENTRY**](#cmem_client.repositories.graphs.INSERT_CATALOG_ENTRY) –
- [**VOCABULARY_CATALOG_GRAPH**](#cmem_client.repositories.graphs.VOCABULARY_CATALOG_GRAPH) – IRI of the (optional, legacy) vocabulary catalog graph.

## `GET_ONTOLOGY_IRI_QUERY` {#cmem_client.repositories.graphs.GET_ONTOLOGY_IRI_QUERY}

```python
GET_ONTOLOGY_IRI_QUERY = '\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT DISTINCT ?iri\nWHERE {\n    ?iri a owl:Ontology;\n}\n'
```

## `GET_PREFIX_DECLARATION` {#cmem_client.repositories.graphs.GET_PREFIX_DECLARATION}

```python
GET_PREFIX_DECLARATION = '\nPREFIX owl: <http://www.w3.org/2002/07/owl#>\nPREFIX vann: <http://purl.org/vocab/vann/>\nSELECT DISTINCT ?prefix ?namespace\nWHERE {{\n    <{ontology_iri}> a owl:Ontology;\n        vann:preferredNamespacePrefix ?prefix;\n        vann:preferredNamespaceUri ?namespace.\n}}\n'
```

## `GraphDeleteConfig` {#cmem_client.repositories.graphs.GraphDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Graph Delete Configuration.

**Attributes:**

- **model_config** –

## `GraphExportConfig` {#cmem_client.repositories.graphs.GraphExportConfig}

Bases: <code>[ExportConfig](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportConfig)</code>

Graph Export Configuration.

**Attributes:**

- [**serialization**](#cmem_client.repositories.graphs.GraphExportConfig.serialization) (<code>[GraphFileSerialization](#cmem_client.repositories.graphs.GraphFileSerialization) | None</code>) – RDF serialization to request for the export. If None, the server default
is used. Export fails if the given format does not support export.
- [**resolve_owl_imports**](#cmem_client.repositories.graphs.GraphExportConfig.resolve_owl_imports) (<code>bool</code>) – If True, resolve ``owl:imports`` and include the imported graphs in
the export. Sent as ``owlImportsResolution``.

### `model_config` {#cmem_client.repositories.graphs.GraphExportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `resolve_owl_imports` {#cmem_client.repositories.graphs.GraphExportConfig.resolve_owl_imports}

```python
resolve_owl_imports: bool = False
```

### `serialization` {#cmem_client.repositories.graphs.GraphExportConfig.serialization}

```python
serialization: GraphFileSerialization | None = None
```

## `GraphFileSerialization` {#cmem_client.repositories.graphs.GraphFileSerialization}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Supported graph format description

**Attributes:**

- [**mime_type**](#cmem_client.repositories.graphs.GraphFileSerialization.mime_type) (<code>str</code>) – MIME type of the serialization, sent as ``Content-Type`` on import and as
``Accept`` on export.
- [**file_extensions**](#cmem_client.repositories.graphs.GraphFileSerialization.file_extensions) (<code>list[str]</code>) – File extensions mapped to this serialization, used by
``guess_file_type()`` to detect the format of a path.
- [**encoding**](#cmem_client.repositories.graphs.GraphFileSerialization.encoding) (<code>str | None</code>) – Content encoding of the file, sent as ``Content-Encoding`` on import when set.
- [**known_not_supporters**](#cmem_client.repositories.graphs.GraphFileSerialization.known_not_supporters) (<code>list[str]</code>) – Store types known not to support this serialization, matched against
the type reported by the graph store. The client does not enforce this; the test suite
uses it to skip combinations a store cannot handle.
- [**export_supported**](#cmem_client.repositories.graphs.GraphFileSerialization.export_supported) (<code>bool</code>) – Whether graphs can be exported in this serialization.
- [**import_supported**](#cmem_client.repositories.graphs.GraphFileSerialization.import_supported) (<code>bool</code>) – Whether graphs can be imported from this serialization.

### `encoding` {#cmem_client.repositories.graphs.GraphFileSerialization.encoding}

```python
encoding: str | None = None
```

### `export_supported` {#cmem_client.repositories.graphs.GraphFileSerialization.export_supported}

```python
export_supported: bool = True
```

### `file_extensions` {#cmem_client.repositories.graphs.GraphFileSerialization.file_extensions}

```python
file_extensions: list[str]
```

### `import_supported` {#cmem_client.repositories.graphs.GraphFileSerialization.import_supported}

```python
import_supported: bool = True
```

### `known_not_supporters` {#cmem_client.repositories.graphs.GraphFileSerialization.known_not_supporters}

```python
known_not_supporters: list[str] = Field(default_factory=list)
```

### `mime_type` {#cmem_client.repositories.graphs.GraphFileSerialization.mime_type}

```python
mime_type: str
```

### `model_config` {#cmem_client.repositories.graphs.GraphFileSerialization.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `GraphImportConfig` {#cmem_client.repositories.graphs.GraphImportConfig}

Bases: <code>[ImportConfig](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportConfig)</code>

Graph Import Configuration.

**Attributes:**

- [**register_as_vocabulary**](#cmem_client.repositories.graphs.GraphImportConfig.register_as_vocabulary) (<code>bool</code>) – If True, register the imported graph as a vocabulary.
- [**serialization**](#cmem_client.repositories.graphs.GraphImportConfig.serialization) (<code>[GraphFileSerialization](#cmem_client.repositories.graphs.GraphFileSerialization) | None</code>) – RDF serialization of the imported file. If None, it is guessed from the
file extension via ``guess_file_type()``.
- [**namespace_prefix**](#cmem_client.repositories.graphs.GraphImportConfig.namespace_prefix) (<code>str | None</code>) – Vocabulary namespace prefix, used as a fallback when the file carries
no vann metadata. Requires ``register_as_vocabulary=True`` and must be set together
with ``namespace_uri``.
- [**namespace_uri**](#cmem_client.repositories.graphs.GraphImportConfig.namespace_uri) (<code>str | None</code>) – Vocabulary namespace URI, used as a fallback when the file carries no vann
metadata. Requires ``register_as_vocabulary=True`` and must be set together with
``namespace_prefix``.

### `model_config` {#cmem_client.repositories.graphs.GraphImportConfig.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `namespace_prefix` {#cmem_client.repositories.graphs.GraphImportConfig.namespace_prefix}

```python
namespace_prefix: str | None = None
```

### `namespace_uri` {#cmem_client.repositories.graphs.GraphImportConfig.namespace_uri}

```python
namespace_uri: str | None = None
```

### `register_as_vocabulary` {#cmem_client.repositories.graphs.GraphImportConfig.register_as_vocabulary}

```python
register_as_vocabulary: bool = False
```

### `serialization` {#cmem_client.repositories.graphs.GraphImportConfig.serialization}

```python
serialization: GraphFileSerialization | None = None
```

### `use_archive_handler` {#cmem_client.repositories.graphs.GraphImportConfig.use_archive_handler}

```python
use_archive_handler: bool = True
```

## `GraphsRepository` {#cmem_client.repositories.graphs.GraphsRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[ImportItemProtocol](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportItemProtocol)</code>, <code>[ExportItemProtocol](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemProtocol)</code>

Repository for graphs.

This repository manages named graphs which are described with the Graph model.
Supports both regular graphs and vocabularies through the register_as_vocabulary flag.

**Attributes:**

- [**formats**](#cmem_client.repositories.graphs.GraphsRepository.formats) (<code>dict[str, [GraphFileSerialization](#cmem_client.repositories.graphs.GraphFileSerialization)]</code>) – Registry of the supported RDF serializations, keyed by format name such as
``turtle`` or ``json-ld``. Read by ``guess_file_type()`` and available to callers
which need to pick a serialization explicitly.

**Functions:**

- [**byte_generator**](#cmem_client.repositories.graphs.GraphsRepository.byte_generator) – Generate bytes from a file in chunks.
- [**delete_all**](#cmem_client.repositories.graphs.GraphsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.graphs.GraphsRepository.delete_item) – Delete an item from the repository
- [**export_item**](#cmem_client.repositories.graphs.GraphsRepository.export_item) – Export an item from the repository to a file path.
- [**export_to_zip**](#cmem_client.repositories.graphs.GraphsRepository.export_to_zip) – Export graph to a ZIP file.
- [**fetch_data**](#cmem_client.repositories.graphs.GraphsRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**guess_file_type**](#cmem_client.repositories.graphs.GraphsRepository.guess_file_type) – Guess the RDF serialization format from a file path for import.
- [**import_item**](#cmem_client.repositories.graphs.GraphsRepository.import_item) – Import an exported file to the repository
- [**items**](#cmem_client.repositories.graphs.GraphsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.graphs.GraphsRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.graphs.GraphsRepository.values) – Get the values of the repository

### `byte_generator` {#cmem_client.repositories.graphs.GraphsRepository.byte_generator}

```python
byte_generator(file_path, chunk_size=1024)
```

Generate bytes from a file in chunks.

**Parameters:**

- **file_path** (<code>Path</code>) – Path to the file to read
- **chunk_size** (<code>int</code>) – Size of each chunk in bytes (default: 1024)

**Yields:**

- **bytes** (<code>Generator[bytes]</code>) – Chunks of data from the file

### `delete_all` {#cmem_client.repositories.graphs.GraphsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.graphs.GraphsRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `export_item` {#cmem_client.repositories.graphs.GraphsRepository.export_item}

```python
export_item(key, path=None, replace=False, configuration=None)
```

Export an item from the repository to a file path.

**Parameters:**

- **key** (<code>str</code>) – The key identifying the item to export.
- **path** (<code>Path | None</code>) – The target file path for export. If None, a path will be generated.
- **replace** (<code>bool</code>) – Whether to replace existing files at the target path.
- **configuration** (<code>[ExportItemConfig_contra](../repositories/protocols/export_item.md#cmem_client.repositories.protocols.export_item.ExportItemConfig_contra) | None</code>) – Optional configuration for export behavior.

**Returns:**

- <code>Path</code> – The actual path where the item was exported.

**Raises:**

- <code>[RepositoryItemNotFoundError](../exceptions.md#cmem_client.exceptions.RepositoryItemNotFoundError)</code> – If the specified item key is not found.
- <code>[RepositoryReadError](../exceptions.md#cmem_client.exceptions.RepositoryReadError)</code> – If there's an error during export or path mismatch.

### `export_to_zip` {#cmem_client.repositories.graphs.GraphsRepository.export_to_zip}

```python
export_to_zip(key, path=None, replace=False)
```

Export graph to a ZIP file.

Exports a single RDF file to a ZIP archive.

**Parameters:**

- **key** (<code>str</code>) – The URI/identifier of the graph to export.
- **path** (<code>Path | None</code>) – Optional target path for the ZIP file. If None, creates a temporary file.
- **replace** (<code>bool</code>) – Whether to overwrite an existing file at the target path.

**Returns:**

- <code>Path</code> – Path to the created ZIP file.

**Raises:**

- <code>[GraphExportError](../exceptions.md#cmem_client.exceptions.GraphExportError)</code> – If the file already exists and replace is False, or if
the exported graph is empty.

### `fetch_data` {#cmem_client.repositories.graphs.GraphsRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `formats` {#cmem_client.repositories.graphs.GraphsRepository.formats}

```python
formats: dict[str, GraphFileSerialization] = {'turtle': GraphFileSerialization(mime_type='text/turtle', file_extensions=['ttl']), 'rdf/xml': GraphFileSerialization(mime_type='application/rdf+xml', file_extensions=['rdf', 'xml']), 'json-ld': GraphFileSerialization(mime_type='application/ld+json', file_extensions=['jsonld'], known_not_supporters=['TENTRIS'], export_supported=False), 'n-triples': GraphFileSerialization(mime_type='application/n-triples', file_extensions=['nt']), 'pretty-turtle': GraphFileSerialization(mime_type='text/turtle+pretty', file_extensions=['ttl'], import_supported=False)}
```

### `guess_file_type` {#cmem_client.repositories.graphs.GraphsRepository.guess_file_type}

```python
guess_file_type(path)
```

Guess the RDF serialization format from a file path for import.

Attempts to determine the appropriate GraphFileSerialization by examining
the file's MIME type and file extension. Supports compressed files (.gz).
Only considers formats where import_supported is True.

**Parameters:**

- **path** (<code>Path</code>) – Path to the RDF file to analyze.

**Returns:**

- **GraphFileSerialization** (<code>[GraphFileSerialization](#cmem_client.repositories.graphs.GraphFileSerialization)</code>) – The detected serialization format with
MIME type, file extensions, and optional encoding information.

**Raises:**

- <code>ValueError</code> – If the file type cannot be determined from the path or
extension.

### `import_item` {#cmem_client.repositories.graphs.GraphsRepository.import_item}

```python
import_item(path=None, key=None, on_conflict=ImportConflictPolicy.FAIL, configuration=None)
```

Import an exported file to the repository

By default, automatically handles zip files, directories, and single files
using ImportItem model. Can be disabled by setting use_archive_handler=False
in the configuration.

**Returns:**

- <code>str</code> – The key of the imported item.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item already exists and the conflict
policy is FAIL, if the import type is not allowed for this repository, if
the import request failed, or if the item is not present afterwards.

### `items` {#cmem_client.repositories.graphs.GraphsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.graphs.GraphsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.graphs.GraphsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.graphs.GraphsRepository.values}

```python
values()
```

Get the values of the repository

## `INSERT_CATALOG_ENTRY` {#cmem_client.repositories.graphs.INSERT_CATALOG_ENTRY}

```python
INSERT_CATALOG_ENTRY = '\nPREFIX voaf: <http://purl.org/vocommons/voaf#>\nPREFIX vann: <http://purl.org/vocab/vann/>\nPREFIX dct: <http://purl.org/dc/terms/>\nPREFIX skos: <http://www.w3.org/2004/02/skos/core#>\nWITH <{graph}>\nINSERT {{\n    <{iri}> a voaf:Vocabulary ;\n        skos:prefLabel "{label}"{language} ;\n        vann:preferredNamespacePrefix "{prefix}" ;\n        vann:preferredNamespaceUri "{namespace}" ;\n        dct:description "vocabulary imported with cmem-client" .\n}}\nWHERE {{}}\n'
```

## `VOCABULARY_CATALOG_GRAPH` {#cmem_client.repositories.graphs.VOCABULARY_CATALOG_GRAPH}

```python
VOCABULARY_CATALOG_GRAPH = 'https://ns.eccenca.com/example/data/vocabs/'
```

IRI of the (optional, legacy) vocabulary catalog graph.

Newer backends do not have this graph. The catalog entry is only written when it
already exists, so importing a vocabulary never (re-)creates it.

