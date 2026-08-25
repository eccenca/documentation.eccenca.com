---
title: "common"
tags:
  - API
  - Python
  - cmem-client
---

# `common` {#cmem_client.models.common}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Shared domain models used across multiple resource types.

Holds the models which are not specific to a single resource. Currently that is the
tag, which DataIntegration attaches to the items of ``client.datasets`` and
``client.workflows`` alike.

**Classes:**

- [**Tag**](#cmem_client.models.common.Tag) – A tag with a label, used across multiple resource types (datasets, workflows, etc.).

## `Tag` {#cmem_client.models.common.Tag}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A tag with a label, used across multiple resource types (datasets, workflows, etc.).

**Attributes:**

- [**label**](#cmem_client.models.common.Tag.label) (<code>str</code>) – Human readable text of the tag.

### `label` {#cmem_client.models.common.Tag.label}

```python
label: str = ''
```

### `model_config` {#cmem_client.models.common.Tag.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

