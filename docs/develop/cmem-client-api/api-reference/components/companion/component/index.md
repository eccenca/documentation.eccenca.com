---
title: "cmem-client: components.companion.component module"
description: "eccenca Corporate Memory Companion component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.companion.component` {#cmem_client.components.companion.component}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

eccenca Corporate Memory Companion component.

The Companion is the conversational assistant of Corporate Memory. Its conversation
history is stored by Explore; this component backs it up to a ZIP archive and restores
it from one.

**Classes:**

- [**Companion**](#cmem_client.components.companion.component.Companion) – High-level interface for the Corporate Memory Companion.

## `Companion` {#cmem_client.components.companion.component.Companion}

```python
Companion(client)
```

High-level interface for the Corporate Memory Companion.

The backup archive holds a `manifest.json` and one NDJSON file per conversation
with the conversation and its messages. The conversations belong to the users who
had them, so treat a backup as personal data.

**Examples:**

```pycon
>>> from pathlib import Path
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.companion.export_to_zip(Path("backup.companion.zip"))
>>> client.companion.import_from_zip(Path("backup.companion.zip"))
```

**Functions:**

- [**export_to_zip**](#cmem_client.components.companion.component.Companion.export_to_zip) – Export the conversation history of all users as a ZIP archive.
- [**import_from_zip**](#cmem_client.components.companion.component.Companion.import_from_zip) – Restore the conversation history from a ZIP archive.

**Attributes:**

- [**logger**](#cmem_client.components.companion.component.Companion.logger) –

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – A configured Corporate Memory client instance with
authentication and endpoint configuration.

### `export_to_zip` {#cmem_client.components.companion.component.Companion.export_to_zip}

```python
export_to_zip(path)
```

Export the conversation history of all users as a ZIP archive.

The archive is streamed to the file, so its size is not limited by memory.

**Parameters:**

- **path** (<code>Path</code>) – The file the ZIP archive is written to. An existing file is overwritten.

**Raises:**

- <code>HTTPStatusError</code> – If Explore rejects the request, for example because the
user is not allowed to do it or Explore does not offer the backup.
- <code>OSError</code> – If the file cannot be written.

### `import_from_zip` {#cmem_client.components.companion.component.Companion.import_from_zip}

```python
import_from_zip(path)
```

Restore the conversation history from a ZIP archive.

The restore adds the conversations of the archive and replaces existing
conversations with the same ID. A replaced conversation is reset to its state in
the archive: messages added after the backup are lost. Explore does not ask
before replacing, so import a backup only to restore the conversation history.
Conversations which are not in the archive are kept.

**Parameters:**

- **path** (<code>Path</code>) – The ZIP archive, as written by `export_to_zip()`.

**Returns:**

- <code>[CompanionRestoreResult](../../../models/companion/index.md#cmem_client.models.companion.CompanionRestoreResult)</code> – The number of restored conversations and messages, as Explore reports it.

**Raises:**

- <code>HTTPStatusError</code> – If Explore rejects the request, for example because the
file is not a Companion backup.
- <code>OSError</code> – If the file cannot be read.

### `logger` {#cmem_client.components.companion.component.Companion.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

