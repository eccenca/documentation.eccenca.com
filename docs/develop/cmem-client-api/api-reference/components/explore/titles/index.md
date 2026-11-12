---
title: "cmem-client: components.explore.titles module"
description: "Titles of resources, resolved by the Corporate Memory Explore title service."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.explore.titles` {#cmem_client.components.explore.titles}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Titles of resources, resolved by the Corporate Memory Explore title service.

**Classes:**

- [**ExploreTitles**](#cmem_client.components.explore.titles.ExploreTitles) – Resolve IRIs to human-readable titles, with one request per batch and a cache.

## `ExploreTitles` {#cmem_client.components.explore.titles.ExploreTitles}

```python
ExploreTitles(client)
```

Resolve IRIs to human-readable titles, with one request per batch and a cache.

Explore resolves a title from the label of a resource, in the language it prefers, and
derives one from the IRI when there is no label. Every answer is cached per IRI and
context graph for as long as the client lives, so a title is requested only once.
There is no endpoint listing all titles, so this is a feature of the Explore component
rather than a repository.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> titles = client.explore.titles.get_many(["https://vocab.eccenca.com/shacl/", "urn:x:a"])
>>> client.explore.titles.get("https://vocab.eccenca.com/shacl/").title
```

**Functions:**

- [**get**](#cmem_client.components.explore.titles.ExploreTitles.get) – Get the title of one IRI.
- [**get_many**](#cmem_client.components.explore.titles.ExploreTitles.get_many) – Get the titles of several IRIs, with one request for all which are not cached yet.

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance.

### `get` {#cmem_client.components.explore.titles.ExploreTitles.get}

```python
get(iri, context_graph=None, refresh=False)
```

Get the title of one IRI.

**Parameters:**

- **iri** (<code>str</code>) – The IRI to resolve.
- **context_graph** (<code>str | None</code>) – The graph to read the label from, if not all graphs.
- **refresh** (<code>bool</code>) – Ask the service again instead of using a cached title.

**Returns:**

- <code>[Title](../../../models/explore/index.md#cmem_client.models.explore.Title)</code> – The title of the IRI. An IRI the service does not answer for gets itself as title.

**Raises:**

- <code>HTTPStatusError</code> – If the title service rejects the request.

### `get_many` {#cmem_client.components.explore.titles.ExploreTitles.get_many}

```python
get_many(iris, context_graph=None, refresh=False)
```

Get the titles of several IRIs, with one request for all which are not cached yet.

**Parameters:**

- **iris** (<code>Iterable[str]</code>) – The IRIs to resolve. Duplicates are resolved once.
- **context_graph** (<code>str | None</code>) – The graph to read the labels from, if not all graphs.
- **refresh** (<code>bool</code>) – Ask the service again for all of them instead of using cached titles.

**Returns:**

- <code>dict[str, [Title](../../../models/explore/index.md#cmem_client.models.explore.Title)]</code> – The title of every IRI, by IRI and in the order given. An IRI the service does
- <code>dict[str, [Title](../../../models/explore/index.md#cmem_client.models.explore.Title)]</code> – not answer for gets itself as title, and is asked for again next time.

**Raises:**

- <code>HTTPStatusError</code> – If the title service rejects the request.

