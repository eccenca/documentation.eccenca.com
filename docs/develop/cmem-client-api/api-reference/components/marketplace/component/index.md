---
title: "cmem-client: components.marketplace.component module"
description: "eccenca Marketplace server integration."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.marketplace.component` {#cmem_client.components.marketplace.component}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

eccenca Marketplace server integration.

This module provides the Marketplace component for interacting with the eccenca
Marketplace server. The component handles package downloads, uploads and version queries,
abstracting the marketplace REST API into a convenient Python interface.

The eccenca Marketplace is a central repository for distributing Corporate Memory
packages, including vocabularies, ontologies, and Python plugins. This component
enables automated package retrieval for installation and dependency resolution.
Packages and licensing each live in their own module of this package; the `Marketplace`
facade delegates to them.

**Classes:**

- [**Marketplace**](#cmem_client.components.marketplace.component.Marketplace) – Interface for eccenca Marketplace server operations.

**Attributes:**

- [**LICENSE_HEADER**](#cmem_client.components.marketplace.component.LICENSE_HEADER) – Header carrying the encrypted license on outbound marketplace requests.
- [**MARKETPLACE_CACHE_DIR**](#cmem_client.components.marketplace.component.MARKETPLACE_CACHE_DIR) –

## `LICENSE_HEADER` {#cmem_client.components.marketplace.component.LICENSE_HEADER}

```python
LICENSE_HEADER = _LICENSE_HEADER
```

Header carrying the encrypted license on outbound marketplace requests.

## `MARKETPLACE_CACHE_DIR` {#cmem_client.components.marketplace.component.MARKETPLACE_CACHE_DIR}

```python
MARKETPLACE_CACHE_DIR = xdg_cache_home() / 'eccenca-marketplace'
```

## `Marketplace` {#cmem_client.components.marketplace.component.Marketplace}

```python
Marketplace(client, marketplace_url='https://eccenca.market', cache_dir=MARKETPLACE_CACHE_DIR, credentials=None, timeout=30, license_issuer_url=None)
```

Interface for eccenca Marketplace server operations.

The Marketplace component provides methods for downloading, uploading and deleting
packages from the eccenca Marketplace server. It handles version resolution, package retrieval,
and writing downloaded content to the filesystem.

**Attributes:**

- **_client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance used for HTTP communication.
- **_marketplace_url** (<code>[HttpUrl](../../../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – Default marketplace server URL for package operations.
- **_cache_dir** (<code>Path | None</code>) – Directory to use for cached downloads.

**Functions:**

- [**delete_package**](#cmem_client.components.marketplace.component.Marketplace.delete_package) – Delete a package from the marketplace server.
- [**download_package**](#cmem_client.components.marketplace.component.Marketplace.download_package) – Download a package from the marketplace server to a specified directory.
- [**get_available_packages**](#cmem_client.components.marketplace.component.Marketplace.get_available_packages) – Get the available packages from the marketplace server.
- [**get_available_packages_page**](#cmem_client.components.marketplace.component.Marketplace.get_available_packages_page) – Get a filtered, sorted and paginated page of packages from the marketplace server.
- [**get_dependencies_from_package**](#cmem_client.components.marketplace.component.Marketplace.get_dependencies_from_package) – Get the dependencies declared by a package version.
- [**get_health**](#cmem_client.components.marketplace.component.Marketplace.get_health) – Report version and health of the local marketplace, the one beside Corporate Memory.
- [**get_manifest_from_package**](#cmem_client.components.marketplace.component.Marketplace.get_manifest_from_package) – Get the manifest of a package version.
- [**get_marketplace_keycloak_token**](#cmem_client.components.marketplace.component.Marketplace.get_marketplace_keycloak_token) – Get the marketplace keycloak token from the marketplace server provided keycloak instance.
- [**get_package**](#cmem_client.components.marketplace.component.Marketplace.get_package) – Get the metadata of a single package from the marketplace server.
- [**get_versions_from_package**](#cmem_client.components.marketplace.component.Marketplace.get_versions_from_package) – Get the available versions of a package from the marketplace server.
- [**set_license_token**](#cmem_client.components.marketplace.component.Marketplace.set_license_token) – Set the license token (``x-eccenca-auth``) to send to a marketplace target.
- [**upload_package**](#cmem_client.components.marketplace.component.Marketplace.upload_package) – Upload a local package to the marketplace server.

**Parameters:**

- **client** (<code>[Client](../../../client/index.md#cmem_client.client.Client)</code>) – The Corporate Memory client instance.
- **marketplace_url** (<code>[HttpUrl](../../../models/url/index.md#cmem_client.models.url.HttpUrl) | str</code>) – Default marketplace server URL. Defaults to the public eccenca Marketplace.
- **cache_dir** (<code>Path | None</code>) – Directory to use for cached downloads. If set to None, caching is disabled.
- **credentials** (<code>[BaseCredentials](../../../models/credentials/index.md#cmem_client.models.credentials.BaseCredentials) | None</code>) – The credentials used to authenticate with the marketplace server. Setting this attribute
is needed for write operations on the server.
- **timeout** (<code>int</code>) – The timeout to wait for a response from the marketplace server. Defaults to 30 seconds.
- **license_issuer_url** (<code>[HttpUrl](../../../models/url/index.md#cmem_client.models.url.HttpUrl) | str | None</code>) – The local marketplace whose ``/api/session`` mints the encrypted license token
attached as ``x-eccenca-auth`` to outbound requests. Defaults to
``client.config.url_marketplace`` (the marketplace bundled beside Corporate Memory).

### `cache_dir` {#cmem_client.components.marketplace.component.Marketplace.cache_dir}

```python
cache_dir: Path | None
```

Get the cache directory.

### `credentials` {#cmem_client.components.marketplace.component.Marketplace.credentials}

```python
credentials: BaseCredentials | None
```

Get the marketplace credentials.

### `delete_package` {#cmem_client.components.marketplace.component.Marketplace.delete_package}

```python
delete_package(package_id)
```

Delete a package from the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier of the package to be deleted.

**Raises:**

- <code>MarketplaceAuthError</code> – If the token could not be provided.
- <code>MarketplaceDeleteError</code> – If the deletion was rejected by the marketplace server.
- <code>HTTPError</code> – If the marketplace server request fails.

### `download_package` {#cmem_client.components.marketplace.component.Marketplace.download_package}

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

- <code>MarketplaceReadError</code> – If the marketplace server request fails or the package/version is not found.

### `get_available_packages` {#cmem_client.components.marketplace.component.Marketplace.get_available_packages}

```python
get_available_packages()
```

Get the available packages from the marketplace server.

### `get_available_packages_page` {#cmem_client.components.marketplace.component.Marketplace.get_available_packages_page}

```python
get_available_packages_page(package_type=None, search=None, tags=None, sort_by=SortField.package_id, sort_order=SortOrder.asc, offset=0, limit=20, package_license=None, language=None, dependency=None)
```

Get a filtered, sorted and paginated page of packages from the marketplace server.

Marketplace servers older than the paginated route answer 404; for those the plain
package listing is fetched and filtered, sorted and paged here, so callers see the
same result shape regardless of the server version. A server that predates one of the
filters ignores it, so the result is then wider than asked for.

**Parameters:**

- **package_type** (<code>str | None</code>) – Restrict the result to one package type.
- **search** (<code>str | None</code>) – Case-insensitive substring matched against name, description and id.
- **tags** (<code>list[str] | None</code>) – Only packages carrying all of these tags.
- **sort_by** (<code>SortField</code>) – Metadata field to sort by.
- **sort_order** (<code>SortOrder</code>) – Sort direction.
- **offset** (<code>int</code>) – Number of items to skip.
- **limit** (<code>int</code>) – Maximum number of items to return.
- **package_license** (<code>str | None</code>) – Restrict the result to one license identifier.
- **language** (<code>list[str] | None</code>) – Only packages available in all of these languages. An empty list leaves
the language filter unset.
- **dependency** (<code>str | None</code>) – Restrict the result to packages depending on this package id.

**Returns:**

- <code>PackageListResponse</code> – The requested page, including paging position and facet counts.

**Raises:**

- <code>MarketplaceReadError</code> – If the marketplace server request fails.

### `get_dependencies_from_package` {#cmem_client.components.marketplace.component.Marketplace.get_dependencies_from_package}

```python
get_dependencies_from_package(package_id, package_version)
```

Get the dependencies declared by a package version.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier.
- **package_version** (<code>PackageVersionIdentifier</code>) – The version to read the dependencies of.

**Returns:**

- <code>list[ValidDependency]</code> – The marketplace package and python package dependencies of that version.

**Raises:**

- <code>MarketplaceReadError</code> – If the package version is unknown or the request fails.

### `get_health` {#cmem_client.components.marketplace.component.Marketplace.get_health}

```python
get_health()
```

Report version and health of the local marketplace, the one beside Corporate Memory.

Reads `api/info` of the marketplace at `client.config.url_marketplace`, which also
serves as its health probe; the configured `marketplace_url` does not matter here.

**Returns:**

- <code>[MarketplaceStatus](../../../models/status/index.md#cmem_client.models.status.MarketplaceStatus)</code> – The status of the local marketplace: UP with its version, or DOWN with the
- <code>[MarketplaceStatus](../../../models/status/index.md#cmem_client.models.status.MarketplaceStatus)</code> – error of a failing request, instead of raising.

### `get_manifest_from_package` {#cmem_client.components.marketplace.component.Marketplace.get_manifest_from_package}

```python
get_manifest_from_package(package_id, package_version)
```

Get the manifest of a package version.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier.
- **package_version** (<code>PackageVersionIdentifier</code>) – The version to read the manifest of.

**Returns:**

- <code>ValidManifest</code> – The manifest of that version.

**Raises:**

- <code>MarketplaceReadError</code> – If the package version is unknown or the request fails.

### `get_marketplace_keycloak_token` {#cmem_client.components.marketplace.component.Marketplace.get_marketplace_keycloak_token}

```python
get_marketplace_keycloak_token(credentials=None)
```

Get the marketplace keycloak token from the marketplace server provided keycloak instance.

This method first fetches the keycloak token URL needed from the marketplace server.
After this it fetches a token with the given credentials and provides it for
further authentication of protected routes.

When no credentials parameter is given, it uses the class attribute of the marketplace component.

**Parameters:**

- **credentials** (<code>[BaseCredentials](../../../models/credentials/index.md#cmem_client.models.credentials.BaseCredentials) | None</code>) – Marketplace keycloak credentials.

**Returns:**

- <code>str</code> – The marketplace keycloak token.

**Raises:**

- <code>MarketplaceAuthError</code> – If no token could be provided.

### `get_package` {#cmem_client.components.marketplace.component.Marketplace.get_package}

```python
get_package(package_id)
```

Get the metadata of a single package from the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier.

**Returns:**

- <code>PackageMetadata</code> – The package metadata of the latest version.

**Raises:**

- <code>MarketplaceReadError</code> – If the package is unknown or the request fails.

### `get_versions_from_package` {#cmem_client.components.marketplace.component.Marketplace.get_versions_from_package}

```python
get_versions_from_package(package_id)
```

Get the available versions of a package from the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier.

**Returns:**

- <code>list[PackageVersionIdentifier]</code> – List of package versions available, newest first.

**Raises:**

- <code>MarketplaceReadError</code> – If the versions could not be retrieved from the
marketplace server.

### `http` {#cmem_client.components.marketplace.component.Marketplace.http}

```python
http: httpx.Client
```

Get the HTTP client instance for making API requests.

Returns the configured HTTP client, creating it lazily on first access.
The client is pre-configured with the timeout value. Authentication headers
are added per-request by the individual methods that require them.

**Returns:**

- <code>Client</code> – The httpx.Client instance configured for the marketplace component.

### `license_issuer_url` {#cmem_client.components.marketplace.component.Marketplace.license_issuer_url}

```python
license_issuer_url: HttpUrl
```

Get the local marketplace URL used as the license-token issuer.

### `logger` {#cmem_client.components.marketplace.component.Marketplace.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

### `marketplace_url` {#cmem_client.components.marketplace.component.Marketplace.marketplace_url}

```python
marketplace_url: HttpUrl
```

Get the marketplace server URL.

### `set_license_token` {#cmem_client.components.marketplace.component.Marketplace.set_license_token}

```python
set_license_token(token, marketplace_url=None)
```

Set the license token (``x-eccenca-auth``) to send to a marketplace target.

Callers that can produce the encrypted license themselves -- a marketplace server holds
its own license and the target's public key -- use this instead of letting the component
fetch a token from the license issuer's ``/api/session``.

**Parameters:**

- **token** (<code>str | None</code>) – The encrypted license to attach, or None to record that there is none
(which keeps the header off without a lookup attempt).
- **marketplace_url** (<code>[HttpUrl](../../../models/url/index.md#cmem_client.models.url.HttpUrl) | str | None</code>) – The target this token is for. Defaults to the currently
configured marketplace URL.

### `timeout` {#cmem_client.components.marketplace.component.Marketplace.timeout}

```python
timeout: int
```

Get the marketplace timeout.

### `upload_package` {#cmem_client.components.marketplace.component.Marketplace.upload_package}

```python
upload_package(package_id, path)
```

Upload a local package to the marketplace server.

**Parameters:**

- **package_id** (<code>PackageIdentifier</code>) – Marketplace package identifier of the package to be uploaded.
- **path** (<code>Path</code>) – Path of the package to be uploaded. Must be a valid .cpa file.

**Raises:**

- <code>MarketplaceAuthError</code> – If the token could not be provided.
- <code>MarketplaceWriteError</code> – If the upload was rejected by the marketplace server.
- <code>HTTPError</code> – If the marketplace server request fails.

