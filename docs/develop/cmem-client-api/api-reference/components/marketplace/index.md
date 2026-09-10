---
title: "cmem-client: components.marketplace module"
description: "eccenca Marketplace server integration."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.marketplace` {#cmem_client.components.marketplace}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

eccenca Marketplace server integration.

This module provides the Marketplace component for interacting with the eccenca
Marketplace server. The component handles package downloads, uploads and version queries,
abstracting the marketplace REST API into a convenient Python interface.

The eccenca Marketplace is a central repository for distributing Corporate Memory
packages, including vocabularies, ontologies, and Python plugins. This component
enables automated package retrieval for installation and dependency resolution.

**Classes:**

- [**Marketplace**](#cmem_client.components.marketplace.Marketplace) – Interface for eccenca Marketplace server operations.

**Attributes:**

- [**LICENSE_HEADER**](#cmem_client.components.marketplace.LICENSE_HEADER) – Header carrying the encrypted license on outbound marketplace requests.
- [**MARKETPLACE_CACHE_DIR**](#cmem_client.components.marketplace.MARKETPLACE_CACHE_DIR) –

## `LICENSE_HEADER` {#cmem_client.components.marketplace.LICENSE_HEADER}

```python
LICENSE_HEADER = 'x-eccenca-auth'
```

Header carrying the encrypted license on outbound marketplace requests.

## `MARKETPLACE_CACHE_DIR` {#cmem_client.components.marketplace.MARKETPLACE_CACHE_DIR}

```python
MARKETPLACE_CACHE_DIR = xdg_cache_home() / 'eccenca-marketplace'
```

## `Marketplace` {#cmem_client.components.marketplace.Marketplace}

```python
Marketplace(client, marketplace_url='https://eccenca.market', cache_dir=MARKETPLACE_CACHE_DIR, credentials=None, timeout=30, license_issuer_url=None)
```

Interface for eccenca Marketplace server operations.

The Marketplace component provides methods for downloading, uploading and deleting
packages from the eccenca Marketplace server. It handles version resolution, package retrieval,
and writing downloaded content to the filesystem.

**Attributes:**

- **_client** (<code>[Client](../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance used for HTTP communication.
- **_marketplace_url** (<code>[HttpUrl](../../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – Default marketplace server URL for package operations.
- **_cache_dir** (<code>Path | None</code>) – Directory to use for cached downloads.

**Functions:**

- [**delete_package**](#cmem_client.components.marketplace.Marketplace.delete_package) – Delete a package from the marketplace server.
- [**download_package**](#cmem_client.components.marketplace.Marketplace.download_package) – Download a package from the marketplace server to a specified directory.
- [**get_available_packages**](#cmem_client.components.marketplace.Marketplace.get_available_packages) – Get the available packages from the marketplace server.
- [**get_marketplace_keycloak_token**](#cmem_client.components.marketplace.Marketplace.get_marketplace_keycloak_token) – Get the marketplace keycloak token from the marketplace server provided keycloak instance.
- [**get_versions_from_package**](#cmem_client.components.marketplace.Marketplace.get_versions_from_package) – Get the available versions of a package from the marketplace server.
- [**upload_package**](#cmem_client.components.marketplace.Marketplace.upload_package) – Upload a local package to the marketplace server.

**Parameters:**

- **client** (<code>[Client](../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance.
- **marketplace_url** (<code>[HttpUrl](../../models/url/index.md#cmem_client.models.url.HttpUrl) | str</code>) – Default marketplace server URL. Defaults to the public eccenca Marketplace.
- **cache_dir** (<code>Path | None</code>) – Directory to use for cached downloads. If set to None, caching is disabled.
- **credentials** (<code>[BaseCredentials](../../models/credentials/index.md#cmem_client.models.credentials.BaseCredentials) | None</code>) – The credentials used to authenticate with the marketplace server. Setting this attribute
is needed for write operations on the server.
- **timeout** (<code>int</code>) – The timeout to wait for a response from the marketplace server. Defaults to 30 seconds.
- **license_issuer_url** (<code>[HttpUrl](../../models/url/index.md#cmem_client.models.url.HttpUrl) | str | None</code>) – The local marketplace whose ``/api/session`` mints the encrypted license token
attached as ``x-eccenca-auth`` to outbound requests. Defaults to
``client.config.url_marketplace`` (the marketplace bundled beside Corporate Memory).

### `cache_dir` {#cmem_client.components.marketplace.Marketplace.cache_dir}

```python
cache_dir: Path | None
```

Get the cache directory.

### `credentials` {#cmem_client.components.marketplace.Marketplace.credentials}

```python
credentials: BaseCredentials | None
```

Get the marketplace credentials.

### `delete_package` {#cmem_client.components.marketplace.Marketplace.delete_package}

```python
delete_package(package_id)
```

Delete a package from the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier of the package to be deleted.

**Raises:**

- <code>[MarketplaceAuthError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceAuthError)</code> – If the token could not be provided.
- <code>[MarketplaceDeleteError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceDeleteError)</code> – If the deletion was rejected by the marketplace server.
- <code>HTTPError</code> – If the marketplace server request fails.

### `download_package` {#cmem_client.components.marketplace.Marketplace.download_package}

```python
download_package(package_id, path=None, package_version=None, use_cache=True)
```

Download a package from the marketplace server to a specified directory.

Queries the marketplace server for available versions and downloads the
requested package version. If no version is specified, downloads the latest
available version. The package is saved with the naming convention:
{package_id}-v{version}.cpa

If the package already exists in the cache, it will be reused instead of
re-downloading.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier (e.g., "semanticarts-gist-vocab").
- **path** (<code>Path | None</code>) – Target directory where the package will be saved. If None, uses the
cache directory. Must be a directory, not a file path.
- **package_version** (<code>PackageVersionIdentifier | None</code>) – Specific version to download. If None, downloads the latest version.
- **use_cache** (<code>bool</code>) – If True, use cached version if available instead of downloading.

**Returns:**

- <code>Path</code> – The full file path where the package was saved (e.g.,
- <code>Path</code> – /path/to/cache/semanticarts-gist-vocab-v13.0.0.cpa).

**Raises:**

- <code>[MarketplaceReadError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceReadError)</code> – If the marketplace server request fails or the package/version is not found.

### `get_available_packages` {#cmem_client.components.marketplace.Marketplace.get_available_packages}

```python
get_available_packages()
```

Get the available packages from the marketplace server.

### `get_marketplace_keycloak_token` {#cmem_client.components.marketplace.Marketplace.get_marketplace_keycloak_token}

```python
get_marketplace_keycloak_token(credentials=None)
```

Get the marketplace keycloak token from the marketplace server provided keycloak instance.

This method first fetches the keycloak token URL needed from the marketplace server.
After this it fetches a token with the given credentials and provides it for
further authentication of protected routes.

When no credentials parameter is given, it uses the class attribute of the marketplace component.

**Parameters:**

- **credentials** (<code>[BaseCredentials](../../models/credentials/index.md#cmem_client.models.credentials.BaseCredentials) | None</code>) – Marketplace keycloak credentials.

**Returns:**

- <code>str</code> – The marketplace keycloak token.

**Raises:**

- <code>[MarketplaceAuthError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceAuthError)</code> – If no token could be provided.

### `get_versions_from_package` {#cmem_client.components.marketplace.Marketplace.get_versions_from_package}

```python
get_versions_from_package(package_id)
```

Get the available versions of a package from the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier.

**Returns:**

- <code>list[PackageVersionIdentifier]</code> – List of package versions available, newest first.

**Raises:**

- <code>[MarketplaceReadError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceReadError)</code> – If the versions could not be retrieved from the
marketplace server.

### `http` {#cmem_client.components.marketplace.Marketplace.http}

```python
http: httpx.Client
```

Get the HTTP client instance for making API requests.

Returns the configured HTTP client, creating it lazily on first access.
The client is pre-configured with the timeout value. Authentication headers
are added per-request by the individual methods that require them.

**Returns:**

- <code>Client</code> – The httpx.Client instance configured for the marketplace component.

### `license_issuer_url` {#cmem_client.components.marketplace.Marketplace.license_issuer_url}

```python
license_issuer_url: HttpUrl
```

Get the local marketplace URL used as the license-token issuer.

### `logger` {#cmem_client.components.marketplace.Marketplace.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `marketplace_url` {#cmem_client.components.marketplace.Marketplace.marketplace_url}

```python
marketplace_url: HttpUrl
```

Get the marketplace server URL.

### `timeout` {#cmem_client.components.marketplace.Marketplace.timeout}

```python
timeout: int
```

Get the marketplace timeout.

### `upload_package` {#cmem_client.components.marketplace.Marketplace.upload_package}

```python
upload_package(package_id, path)
```

Upload a local package to the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier of the package to be uploaded.
- **path** (<code>Path</code>) – Path of the package to be uploaded. Must be a valid .cpa file.

**Raises:**

- <code>[MarketplaceAuthError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceAuthError)</code> – If the token could not be provided.
- <code>[MarketplaceWriteError](../../exceptions/index.md#cmem_client.exceptions.MarketplaceWriteError)</code> – If the upload was rejected by the marketplace server.
- <code>HTTPError</code> – If the marketplace server request fails.

