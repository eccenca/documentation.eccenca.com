---
title: "cmem-client: models.companion module"
description: "Models of the eccenca Corporate Memory Companion component."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.companion` {#cmem_client.models.companion}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models of the eccenca Corporate Memory Companion component.

**Classes:**

- [**CompanionRestoreResult**](#cmem_client.models.companion.CompanionRestoreResult) – The summary Explore returns after restoring a Companion backup.

## `CompanionRestoreResult` {#cmem_client.models.companion.CompanionRestoreResult}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The summary Explore returns after restoring a Companion backup.

**Attributes:**

- [**restored_conversations**](#cmem_client.models.companion.CompanionRestoreResult.restored_conversations) (<code>int</code>) – The number of conversations restored from the backup.
- [**restored_messages**](#cmem_client.models.companion.CompanionRestoreResult.restored_messages) (<code>int</code>) – The number of messages restored from the backup.
- [**not_in_backup**](#cmem_client.models.companion.CompanionRestoreResult.not_in_backup) (<code>list[str]</code>) – The conversation IDs Explore reports as not contained in the backup.

### `model_config` {#cmem_client.models.companion.CompanionRestoreResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `not_in_backup` {#cmem_client.models.companion.CompanionRestoreResult.not_in_backup}

```python
not_in_backup: list[str] = Field(alias='notInBackup', default_factory=list)
```

The conversation IDs Explore reports as not contained in the backup.

### `restored_conversations` {#cmem_client.models.companion.CompanionRestoreResult.restored_conversations}

```python
restored_conversations: int = Field(alias='restoredConversations')
```

The number of conversations restored from the backup.

### `restored_messages` {#cmem_client.models.companion.CompanionRestoreResult.restored_messages}

```python
restored_messages: int = Field(alias='restoredMessages')
```

The number of messages restored from the backup.

