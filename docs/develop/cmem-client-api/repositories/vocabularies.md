# `vocabularies` {#cmem_client.repositories.vocabularies}

Repository for managing vocabularies in Corporate Memory.

Provides VocabulariesRepository class for listing, installing, and uninstalling
vocabularies, and for reading the global vocabulary cache from DataIntegration.

Installed vocabularies (and their labels) are read from the DataPlatform
``/api/vocabs`` endpoint. Installable (not-yet-installed) vocabularies are resolved
from the (optional, legacy) vocabulary catalog graph; on newer backends without a
catalog graph there are none and only installed vocabularies are listed.

Installing and uninstalling are kept for backwards compatibility but are slated to
be superseded by the marketplace package command group. They resolve download URLs
from the (optional) vocabulary catalog graph; when it is absent, there is nothing to
install and callers should use the marketplace package command group instead.

Graph-level operations (upload, delete, reload) are delegated to GraphsRepository
to avoid duplication.

**Examples:**

List the installed vocabularies:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> for vocabulary in client.vocabularies.list_vocabularies(filter_="installed"):
...     print(vocabulary.iri)
```

Install a vocabulary from the (legacy) catalog and drop it again:

```pycon
>>> urls = client.vocabularies.get_catalog_download_urls()
>>> client.vocabularies.install(
...     iri="http://xmlns.com/foaf/0.1/", download_url=urls["http://xmlns.com/foaf/0.1/"]
... )
>>> client.vocabularies.uninstall("http://xmlns.com/foaf/0.1/")
```

Read the global vocabulary cache of DataIntegration:

```pycon
>>> client.vocabularies.get_global_cache()
```

**Classes:**

- [**VocabulariesRepository**](#cmem_client.repositories.vocabularies.VocabulariesRepository) – Repository for Corporate Memory vocabularies.

**Attributes:**

- [**CATALOG_ENTRIES_QUERY**](#cmem_client.repositories.vocabularies.CATALOG_ENTRIES_QUERY) – 
- [**DEFAULT_CATALOG_GRAPH**](#cmem_client.repositories.vocabularies.DEFAULT_CATALOG_GRAPH) – 
- [**REMOVE_CATALOG_ENTRY_IF_NOT_INSTALLABLE**](#cmem_client.repositories.vocabularies.REMOVE_CATALOG_ENTRY_IF_NOT_INSTALLABLE) – 
- [**VocabularyFilter**](#cmem_client.repositories.vocabularies.VocabularyFilter) – 

## `CATALOG_ENTRIES_QUERY` {#cmem_client.repositories.vocabularies.CATALOG_ENTRIES_QUERY}

```python
CATALOG_ENTRIES_QUERY = '\nPREFIX dcat: <http://www.w3.org/ns/dcat#>\nPREFIX voaf: <http://purl.org/vocommons/voaf#>\nPREFIX skos: <http://www.w3.org/2004/02/skos/core#>\nPREFIX vann: <http://purl.org/vocab/vann/>\nSELECT DISTINCT ?iri ?downloadUrl ?label ?prefix\nFROM <{graph}>\nWHERE {{\n    ?iri a voaf:Vocabulary ;\n        dcat:distribution ?distribution .\n    OPTIONAL {{ ?distribution dcat:downloadURL ?url . }}\n    BIND(COALESCE(?url, ?distribution) AS ?downloadUrl)\n    OPTIONAL {{ ?iri skos:prefLabel ?label . }}\n    OPTIONAL {{ ?iri vann:preferredNamespacePrefix ?prefix . }}\n}}\n'
```

## `DEFAULT_CATALOG_GRAPH` {#cmem_client.repositories.vocabularies.DEFAULT_CATALOG_GRAPH}

```python
DEFAULT_CATALOG_GRAPH = 'https://ns.eccenca.com/example/data/vocabs/'
```

## `REMOVE_CATALOG_ENTRY_IF_NOT_INSTALLABLE` {#cmem_client.repositories.vocabularies.REMOVE_CATALOG_ENTRY_IF_NOT_INSTALLABLE}

```python
REMOVE_CATALOG_ENTRY_IF_NOT_INSTALLABLE = '\nPREFIX dcat: <http://www.w3.org/ns/dcat#>\nWITH <{graph}>\nDELETE {{ ?s ?p ?o }}\nWHERE {{\n    ?s ?p ?o .\n    FILTER NOT EXISTS {{ ?s dcat:distribution ?downloadUrl . }}\n    FILTER (STR(?s) = "{vocab}")\n}}\n'
```

## `VocabulariesRepository` {#cmem_client.repositories.vocabularies.VocabulariesRepository}

Bases: <code>[Repository](../repositories/base/abc.md#cmem_client.repositories.base.abc.Repository)[[Vocabulary](../models/vocabulary.md#cmem_client.models.vocabulary.Vocabulary)]</code>

Repository for Corporate Memory vocabularies.

Lists vocabularies as the named graphs that declare an ``owl:Ontology`` resource
and provides install, uninstall, and cache operations. Graph-level operations are
delegated to the GraphsRepository via client.graphs.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.vocabularies.VocabulariesRepository.fetch_data) – Fetch the installed vocabularies from the ``/api/vocabs`` endpoint.
- [**get_catalog_download_urls**](#cmem_client.repositories.vocabularies.VocabulariesRepository.get_catalog_download_urls) – Return all available vocabulary IRIs and their download URLs from the catalog graph.
- [**get_catalog_entries**](#cmem_client.repositories.vocabularies.VocabulariesRepository.get_catalog_entries) – Return installable vocabulary catalog entries keyed by IRI.
- [**get_global_cache**](#cmem_client.repositories.vocabularies.VocabulariesRepository.get_global_cache) – Get the global vocabulary cache from DataIntegration.
- [**install**](#cmem_client.repositories.vocabularies.VocabulariesRepository.install) – Install a vocabulary by downloading it and adding it as an owl:Ontology graph.
- [**items**](#cmem_client.repositories.vocabularies.VocabulariesRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.vocabularies.VocabulariesRepository.keys) – Get the keys of the repository
- [**list_vocabularies**](#cmem_client.repositories.vocabularies.VocabulariesRepository.list_vocabularies) – Return vocabularies filtered by installation status.
- [**reload**](#cmem_client.repositories.vocabularies.VocabulariesRepository.reload) – Reload prefixes and vocabulary cache for the given IRI.
- [**uninstall**](#cmem_client.repositories.vocabularies.VocabulariesRepository.uninstall) – Uninstall (delete) an installed vocabulary.
- [**values**](#cmem_client.repositories.vocabularies.VocabulariesRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.vocabularies.VocabulariesRepository.logger) (<code>Logger</code>) – Gets the client logger

### `fetch_data` {#cmem_client.repositories.vocabularies.VocabulariesRepository.fetch_data}

```python
fetch_data()
```

Fetch the installed vocabularies from the ``/api/vocabs`` endpoint.

The endpoint reports the installed vocabularies together with their installation
status (``installed``) and label. Installable vocabularies are resolved separately
from the vocabulary catalog graph in :meth:`list_vocabularies`.

### `get_catalog_download_urls` {#cmem_client.repositories.vocabularies.VocabulariesRepository.get_catalog_download_urls}

```python
get_catalog_download_urls(catalog_graph=DEFAULT_CATALOG_GRAPH)
```

Return all available vocabulary IRIs and their download URLs from the catalog graph.

Queries the vocabulary catalog graph for entries that provide a download URL.
If the catalog graph does not exist, an empty mapping is returned.

**Parameters:**

- **catalog_graph** (<code>str</code>) – URI of the vocabulary catalog graph to query.

**Returns:**

- <code>dict[str, str]</code> – Mapping of vocabulary IRI to download URL.

### `get_catalog_entries` {#cmem_client.repositories.vocabularies.VocabulariesRepository.get_catalog_entries}

```python
get_catalog_entries(catalog_graph=DEFAULT_CATALOG_GRAPH)
```

Return installable vocabulary catalog entries keyed by IRI.

Queries the vocabulary catalog graph for entries that provide an HTTP download URL
and builds Vocabulary objects carrying the download URL and a human-readable label
(``"<prefix>: <prefLabel>"`` when both are available). If the catalog graph does not
exist, an empty mapping is returned.

**Parameters:**

- **catalog_graph** (<code>str</code>) – URI of the vocabulary catalog graph to query.

**Returns:**

- <code>dict[str, [Vocabulary](../models/vocabulary.md#cmem_client.models.vocabulary.Vocabulary)]</code> – Mapping of vocabulary IRI to Vocabulary catalog entry.

### `get_global_cache` {#cmem_client.repositories.vocabularies.VocabulariesRepository.get_global_cache}

```python
get_global_cache()
```

Get the global vocabulary cache from DataIntegration.

**Returns:**

- <code>[VocabularyCache](../models/vocabulary.md#cmem_client.models.vocabulary.VocabularyCache)</code> – The global vocabulary cache as a VocabularyCache model.

### `install` {#cmem_client.repositories.vocabularies.VocabulariesRepository.install}

```python
install(iri, download_url, on_conflict=ImportConflictPolicy.REPLACE)
```

Install a vocabulary by downloading it and adding it as an owl:Ontology graph.

The vocabulary content is downloaded from the given ``download_url`` (the URL is
supplied by the caller; it is not resolved from any catalog). The graph upload and
vocabulary registration are delegated to GraphsRepository.

**Parameters:**

- **iri** (<code>str</code>) – IRI of the vocabulary to install (used as the graph IRI).
- **download_url** (<code>str</code>) – URL to download the vocabulary RDF file from.
- **on_conflict** (<code>[ImportConflictPolicy](../repositories/protocols/import_item.md#cmem_client.repositories.protocols.import_item.ImportConflictPolicy)</code>) – How to handle a graph that already exists. Defaults to REPLACE.

**Raises:**

- <code>HTTPError</code> – If the download request fails.

### `items` {#cmem_client.repositories.vocabularies.VocabulariesRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.vocabularies.VocabulariesRepository.keys}

```python
keys()
```

Get the keys of the repository

### `list_vocabularies` {#cmem_client.repositories.vocabularies.VocabulariesRepository.list_vocabularies}

```python
list_vocabularies(filter_='all', catalog_graph=DEFAULT_CATALOG_GRAPH)
```

Return vocabularies filtered by installation status.

Installed vocabularies (and their labels) come from the ``/api/vocabs`` endpoint.
Installable vocabularies are the catalog-graph entries that provide a download URL
and are not yet installed; when the catalog graph does not exist there are none.

**Parameters:**

- **filter_** (<code>[VocabularyFilter](#cmem_client.repositories.vocabularies.VocabularyFilter)</code>) – One of "all", "installed", or "installable".
- **catalog_graph** (<code>str</code>) – URI of the vocabulary catalog graph used to resolve installable
vocabularies (ignored for the "installed" filter).

**Returns:**

- <code>list[[Vocabulary](../models/vocabulary.md#cmem_client.models.vocabulary.Vocabulary)]</code> – Filtered list of Vocabulary objects.

### `logger` {#cmem_client.repositories.vocabularies.VocabulariesRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `reload` {#cmem_client.repositories.vocabularies.VocabulariesRepository.reload}

```python
reload(iri)
```

Reload prefixes and vocabulary cache for the given IRI.

Delegates to GraphsRepository._reload_vocabularies which handles
both the DI prefix reload and the global vocabulary cache update.

**Parameters:**

- **iri** (<code>str</code>) – IRI of the vocabulary to reload.

### `uninstall` {#cmem_client.repositories.vocabularies.VocabulariesRepository.uninstall}

```python
uninstall(iri, catalog_graph=DEFAULT_CATALOG_GRAPH)
```

Uninstall (delete) an installed vocabulary.

Delegates the graph deletion (and prefix/cache reload) to GraphsRepository,
then removes the catalog entry if it has no download URL.

**Parameters:**

- **iri** (<code>str</code>) – IRI of the vocabulary to uninstall.
- **catalog_graph** (<code>str</code>) – URI of the vocabulary catalog graph.

**Raises:**

- <code>[VocabularyUninstallError](../exceptions.md#cmem_client.exceptions.VocabularyUninstallError)</code> – If the vocabulary is not installed.

### `values` {#cmem_client.repositories.vocabularies.VocabulariesRepository.values}

```python
values()
```

Get the values of the repository

## `VocabularyFilter` {#cmem_client.repositories.vocabularies.VocabularyFilter}

```python
VocabularyFilter = Literal['all', 'installed', 'installable']
```

