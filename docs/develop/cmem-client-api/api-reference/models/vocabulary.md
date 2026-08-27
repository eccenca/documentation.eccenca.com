---
title: "cmem-client: vocabulary module"
description: "Vocabulary models for Corporate Memory vocabulary catalog."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.vocabulary` {#cmem_client.models.vocabulary}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Vocabulary models for Corporate Memory vocabulary catalog.

Provides Pydantic models for vocabulary catalog entries returned by the
DataPlatform vocabularies API.

The catalog lists both the vocabularies a deployment has installed and those it offers
for installation; they are the items of ``client.vocabularies``, keyed by their IRI.
The cache models describe something else: the classes and properties DataIntegration
extracted from the installed vocabularies, which is what drives autocompletion in the
user interface.

**Classes:**

- [**VocabCacheEntry**](#cmem_client.models.vocabulary.VocabCacheEntry) – Cache data for one vocabulary, containing its classes and properties.
- [**VocabCacheItem**](#cmem_client.models.vocabulary.VocabCacheItem) – A single class or property in the vocabulary cache.
- [**VocabCacheItemInfo**](#cmem_client.models.vocabulary.VocabCacheItemInfo) – Generic info for a vocabulary cache term.
- [**Vocabulary**](#cmem_client.models.vocabulary.Vocabulary) – A vocabulary catalog entry.
- [**VocabularyCache**](#cmem_client.models.vocabulary.VocabularyCache) – Global vocabulary cache response from DataIntegration.
- [**VocabularyLabel**](#cmem_client.models.vocabulary.VocabularyLabel) – Label metadata for a vocabulary.

## `VocabCacheEntry` {#cmem_client.models.vocabulary.VocabCacheEntry}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Cache data for one vocabulary, containing its classes and properties.

**Attributes:**

- [**classes**](#cmem_client.models.vocabulary.VocabCacheEntry.classes) (<code>list[[VocabCacheItem](#cmem_client.models.vocabulary.VocabCacheItem)]</code>) – Classes the vocabulary defines.
- [**properties**](#cmem_client.models.vocabulary.VocabCacheEntry.properties) (<code>list[[VocabCacheItem](#cmem_client.models.vocabulary.VocabCacheItem)]</code>) – Properties the vocabulary defines.

### `classes` {#cmem_client.models.vocabulary.VocabCacheEntry.classes}

```python
classes: list[VocabCacheItem] = Field(default_factory=list)
```

### `model_config` {#cmem_client.models.vocabulary.VocabCacheEntry.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `properties` {#cmem_client.models.vocabulary.VocabCacheEntry.properties}

```python
properties: list[VocabCacheItem] = Field(default_factory=list)
```

## `VocabCacheItem` {#cmem_client.models.vocabulary.VocabCacheItem}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A single class or property in the vocabulary cache.

**Attributes:**

- [**generic_info**](#cmem_client.models.vocabulary.VocabCacheItem.generic_info) (<code>[VocabCacheItemInfo](#cmem_client.models.vocabulary.VocabCacheItemInfo)</code>) – URI and label of the term.

### `generic_info` {#cmem_client.models.vocabulary.VocabCacheItem.generic_info}

```python
generic_info: VocabCacheItemInfo = Field(alias='genericInfo')
```

### `model_config` {#cmem_client.models.vocabulary.VocabCacheItem.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `VocabCacheItemInfo` {#cmem_client.models.vocabulary.VocabCacheItemInfo}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Generic info for a vocabulary cache term.

**Attributes:**

- [**uri**](#cmem_client.models.vocabulary.VocabCacheItemInfo.uri) (<code>str</code>) – URI of the class or property.
- [**label**](#cmem_client.models.vocabulary.VocabCacheItemInfo.label) (<code>str | None</code>) – Human readable name of the term, if the vocabulary defines one.

### `label` {#cmem_client.models.vocabulary.VocabCacheItemInfo.label}

```python
label: str | None = None
```

### `model_config` {#cmem_client.models.vocabulary.VocabCacheItemInfo.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `uri` {#cmem_client.models.vocabulary.VocabCacheItemInfo.uri}

```python
uri: str
```

## `Vocabulary` {#cmem_client.models.vocabulary.Vocabulary}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A vocabulary catalog entry.

**Attributes:**

- [**iri**](#cmem_client.models.vocabulary.Vocabulary.iri) (<code>str</code>) – IRI of the vocabulary. This is the key of the repository.
- [**installed**](#cmem_client.models.vocabulary.Vocabulary.installed) (<code>bool</code>) – Whether the vocabulary is installed in the deployment.
- [**download_url**](#cmem_client.models.vocabulary.Vocabulary.download_url) (<code>str | None</code>) – Where an uninstalled vocabulary can be fetched from, or ``None``
if the catalog offers no source for it.
- [**vocabulary_label**](#cmem_client.models.vocabulary.Vocabulary.vocabulary_label) (<code>str | None</code>) – Name of the vocabulary as given by the catalog.
- [**label**](#cmem_client.models.vocabulary.Vocabulary.label) (<code>[VocabularyLabel](#cmem_client.models.vocabulary.VocabularyLabel) | None</code>) – Label of the graph holding the vocabulary, once it is installed.

**Functions:**

- [**get_id**](#cmem_client.models.vocabulary.Vocabulary.get_id) – Get the IRI of the vocabulary.

### `download_url` {#cmem_client.models.vocabulary.Vocabulary.download_url}

```python
download_url: str | None = Field(default=None, alias='downloadUrl')
```

### `get_id` {#cmem_client.models.vocabulary.Vocabulary.get_id}

```python
get_id()
```

Get the IRI of the vocabulary.

### `installed` {#cmem_client.models.vocabulary.Vocabulary.installed}

```python
installed: bool
```

### `iri` {#cmem_client.models.vocabulary.Vocabulary.iri}

```python
iri: str
```

### `is_installable` {#cmem_client.models.vocabulary.Vocabulary.is_installable}

```python
is_installable: bool
```

Return True if the vocabulary can be installed from catalog.

### `label` {#cmem_client.models.vocabulary.Vocabulary.label}

```python
label: VocabularyLabel | None = None
```

### `model_config` {#cmem_client.models.vocabulary.Vocabulary.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `vocabulary_label` {#cmem_client.models.vocabulary.Vocabulary.vocabulary_label}

```python
vocabulary_label: str | None = Field(default=None, alias='vocabularyLabel')
```

## `VocabularyCache` {#cmem_client.models.vocabulary.VocabularyCache}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Global vocabulary cache response from DataIntegration.

**Attributes:**

- [**vocabularies**](#cmem_client.models.vocabulary.VocabularyCache.vocabularies) (<code>list[[VocabCacheEntry](#cmem_client.models.vocabulary.VocabCacheEntry)]</code>) – Cache entry of each vocabulary DataIntegration knows.

### `model_config` {#cmem_client.models.vocabulary.VocabularyCache.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `vocabularies` {#cmem_client.models.vocabulary.VocabularyCache.vocabularies}

```python
vocabularies: list[VocabCacheEntry] = Field(default_factory=list)
```

## `VocabularyLabel` {#cmem_client.models.vocabulary.VocabularyLabel}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Label metadata for a vocabulary.

**Attributes:**

- [**title**](#cmem_client.models.vocabulary.VocabularyLabel.title) (<code>str</code>) – Text of the label.
- [**lang**](#cmem_client.models.vocabulary.VocabularyLabel.lang) (<code>str | None</code>) – Language tag of the label, e.g. ``en``.

### `lang` {#cmem_client.models.vocabulary.VocabularyLabel.lang}

```python
lang: str | None = None
```

### `model_config` {#cmem_client.models.vocabulary.VocabularyLabel.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `title` {#cmem_client.models.vocabulary.VocabularyLabel.title}

```python
title: str
```

