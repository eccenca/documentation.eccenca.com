---
title: "cmem-client: models.paged_list module"
description: "Models of paged list responses."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.paged_list` {#cmem_client.models.paged_list}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models of paged list responses.

A paged endpoint of Corporate Memory returns its items one page at a time, together with
a PageDescription of the page.

**Classes:**

- [**PageDescription**](#cmem_client.models.paged_list.PageDescription) – A description of a paged list.

## `PageDescription` {#cmem_client.models.paged_list.PageDescription}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A description of a paged list.

**Attributes:**

- [**size**](#cmem_client.models.paged_list.PageDescription.size) (<code>int</code>) – Number of items requested per page. ``fetch_data()`` stops paging as soon as a page
returns fewer items than this.
- [**number**](#cmem_client.models.paged_list.PageDescription.number) (<code>int</code>) – Zero based index of this page.
- [**total_elements**](#cmem_client.models.paged_list.PageDescription.total_elements) (<code>int</code>) – Total number of items across all pages, sent as ``totalElements``.
- [**total_pages**](#cmem_client.models.paged_list.PageDescription.total_pages) (<code>int</code>) – Total number of pages, sent as ``totalPages``.

### `model_config` {#cmem_client.models.paged_list.PageDescription.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `number` {#cmem_client.models.paged_list.PageDescription.number}

```python
number: int
```

### `size` {#cmem_client.models.paged_list.PageDescription.size}

```python
size: int
```

### `total_elements` {#cmem_client.models.paged_list.PageDescription.total_elements}

```python
total_elements: int = Field(alias='totalElements')
```

### `total_pages` {#cmem_client.models.paged_list.PageDescription.total_pages}

```python
total_pages: int = Field(alias='totalPages')
```

