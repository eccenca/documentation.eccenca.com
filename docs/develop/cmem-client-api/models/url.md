# `url` {#cmem_client.models.url}

HTTP URL validation and manipulation utilities.

This module provides the HttpUrl class, which extends httpx.URL with additional
validation and path manipulation capabilities. It ensures URLs are well-formed
and provides convenient methods for building API endpoints.

The HttpUrl class is used throughout the configuration system to construct
various Corporate Memory API endpoints from base URLs.

**Classes:**

- [**HttpUrl**](#cmem_client.models.url.HttpUrl) – A http(s) URL.

## `HttpUrl` {#cmem_client.models.url.HttpUrl}

```python
HttpUrl(url)
```

Bases: <code>URL</code>

A http(s) URL.

