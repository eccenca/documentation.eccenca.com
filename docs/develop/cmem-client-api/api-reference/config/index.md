---
title: "cmem-client: config module"
description: "Configuration management for the Corporate Memory client."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.config` {#cmem_client.config}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Configuration management for the Corporate Memory client.

This module provides the Config class that handles all configuration aspects
of the Corporate Memory client, including URL construction, SSL verification,
authentication endpoints, and environment variable parsing.

The Config class automatically constructs various API endpoints based on a base URL
and provides flexible configuration through both programmatic setup and environment
variables, making it suitable for different deployment environments.

**Classes:**

- [**Config**](#cmem_client.config.Config) – Corporate Memory Client configuration.

**Attributes:**

- [**DEFAULT_CMEM_BASE_URI**](#cmem_client.config.DEFAULT_CMEM_BASE_URI) –

## `Config` {#cmem_client.config.Config}

```python
Config(url_base, realm_id='cmem')
```

Corporate Memory Client configuration.

The Config class manages all configuration aspects for connecting to Corporate
Memory instances, including URL construction, SSL verification, timeout settings,
and authentication endpoints. It provides both programmatic configuration and
automatic configuration from environment variables.

The class automatically constructs various API endpoints based on a base URL
and realm configuration, with support for customizing individual endpoints
when needed for complex deployment scenarios.

**Attributes:**

- **_realm_id** (<code>str</code>) – The Keycloak realm identifier for authentication.
- **_verify** (<code>bool | str</code>) – SSL/TLS certificate verification flag.
- **_url_base** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – Base URL of the Corporate Memory instance.
- **_url_keycloak** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – Base URL of the Keycloak authentication server.
- **_url_keycloak_issuer** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – Keycloak realm issuer URL for token validation.
- **_url_build_api** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – DataIntegration (build) API endpoint URL.
- **_url_explore_api** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – DataPlatform (explore) API endpoint URL.
- **_url_oauth_token** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code>) – OAuth token endpoint URL for authentication.
- [**timeout**](#cmem_client.config.Config.timeout) (<code>int | None</code>) – HTTP request timeout in seconds.

**Functions:**

- [**from_cmempy**](#cmem_client.config.Config.from_cmempy) – Create a Config instance from a cmempy environment.
- [**from_context**](#cmem_client.config.Config.from_context) – Create a Config instance from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.config.Config.from_dict) – Create a Config instance from a plain dictionary of configuration values.
- [**from_env**](#cmem_client.config.Config.from_env) – Create a Config instance from environment variables.

**Parameters:**

- **url_base** (<code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl) | str</code>) – The base URL of the Corporate Memory instance. Can be
provided as either an HttpUrl object or a string that will
be converted to HttpUrl.
- **realm_id** (<code>str</code>) – The Keycloak realm identifier for authentication.
Defaults to "cmem" for standard Corporate Memory deployments.

### `extra_headers` {#cmem_client.config.Config.extra_headers}

```python
extra_headers: dict[str, str] = {}
```

Extra HTTP headers to include with every request, e.g. from CMEMC_CUSTOM_HEADER_* vars.

### `from_cmempy` {#cmem_client.config.Config.from_cmempy}

```python
from_cmempy()
```

Create a Config instance from a cmempy environment.

### `from_context` {#cmem_client.config.Config.from_context}

```python
from_context(context)
```

Create a Config instance from a cmem-plugin-base context object.

Reads connection URLs directly from the context's ``SystemContext``,
making manual environment variable configuration unnecessary inside
Corporate Memory Python plugins.

**Parameters:**

- **context** (<code>object</code>) – An ``ExecutionContext`` or ``PluginContext`` instance from
``cmem-plugin-base``. Must expose a ``system`` attribute
(``SystemContext``) providing ``cmem_base_uri()``,
``di_api_endpoint()``, and ``dp_api_endpoint()``.

**Returns:**

- <code>[Config](#cmem_client.config.Config)</code> – A Config instance populated with URLs from the context's
- <code>[Config](#cmem_client.config.Config)</code> – ``SystemContext``.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions/index.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the base URL returned by the context's
``SystemContext`` is empty or missing.

### `from_dict` {#cmem_client.config.Config.from_dict}

```python
from_dict(d)
```

Create a Config instance from a plain dictionary of configuration values.

This factory method creates a configuration by reading values from a
plain dictionary. The expected keys mirror the environment variable names
used by ``from_env()``, making it easy to pass config-file sections or
test fixtures without mutating ``os.environ``.

**Parameters:**

- **d** (<code>dict[str, str]</code>) – A mapping of configuration keys to string values. Keys follow
the same naming convention as environment variables (e.g.
``"CMEM_BASE_URI"``, ``"SSL_VERIFY"``).

**Returns:**

- <code>[Config](#cmem_client.config.Config)</code> – A Config instance configured with values from the dictionary.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions/index.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the required ``CMEM_BASE_URI`` key is
missing or empty.

<details class="keys" open markdown="1">
<summary>Keys</summary>

CMEM_BASE_URI (required): Base URL of the Corporate Memory instance.
DI_API_ENDPOINT (optional): DataIntegration API endpoint override.
DP_API_ENDPOINT (optional): DataPlatform API endpoint override.
KEYCLOAK_BASE_URI (optional): Keycloak server URL override.
KEYCLOAK_REALM_ID (optional): Keycloak realm identifier override.
OAUTH_TOKEN_URI (optional): OAuth token endpoint override.
MARKETPLACE_BASE_URI (optional): Local marketplace (license issuer) override.
SSL_VERIFY (optional): Set to ``"false"`` to disable SSL verification.
REQUESTS_CA_BUNDLE (optional): Path to a custom CA bundle file.

</details>

### `from_env` {#cmem_client.config.Config.from_env}

```python
from_env()
```

Create a Config instance from environment variables.

This factory method creates a configuration by reading various environment
variables that specify Corporate Memory connection details. It provides
a convenient way to configure the client in containerized or cloud
environments where configuration is managed through environment variables.

**Returns:**

- <code>[Config](#cmem_client.config.Config)</code> – A Config instance configured with values from environment variables.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions/index.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the required CMEM_BASE_URI environment
variable is not set.

<details class="environment-variables" open markdown="1">
<summary>Environment Variables</summary>

CMEM_BASE_URI (required): Base URL of the Corporate Memory instance.
DI_API_ENDPOINT (optional): DataIntegration API endpoint override.
DP_API_ENDPOINT (optional): DataPlatform API endpoint override.
KEYCLOAK_BASE_URI (optional): Keycloak server URL override.
KEYCLOAK_REALM_ID (optional): Keycloak realm identifier override.
OAUTH_TOKEN_URI (optional): OAuth token endpoint override.
MARKETPLACE_BASE_URI (optional): Local marketplace (license issuer) override.
SSL_VERIFY (optional): SSL certificate verification flag.
REQUESTS_CA_BUNDLE (optional): Path to a custom CA bundle file.

</details>

### `realm_id` {#cmem_client.config.Config.realm_id}

```python
realm_id = realm_id
```

### `timeout` {#cmem_client.config.Config.timeout}

```python
timeout: int | None = None
```

HTTP request timeout in seconds, defaults to no timeout (None)

### `url_base` {#cmem_client.config.Config.url_base}

```python
url_base: HttpUrl
```

Get the base URL of the Corporate Memory instance.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The base URL from which all other API endpoints are derived.
- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – This is the root URL of the Corporate Memory deployment.

### `url_build_api` {#cmem_client.config.Config.url_build_api}

```python
url_build_api: HttpUrl
```

Get the DataIntegration (build) API endpoint URL.

Returns the URL for the DataIntegration API, which handles projects,
datasets, transformations, and data integration workflows. If not
explicitly set, it defaults to the base URL with '/dataintegration/' appended.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The DataIntegration API endpoint URL.

### `url_explore_api` {#cmem_client.config.Config.url_explore_api}

```python
url_explore_api: HttpUrl
```

Get the DataPlatform (explore) API endpoint URL.

Returns the URL for the DataPlatform API, which handles graph storage,
SPARQL queries, and semantic data exploration. If not explicitly set,
it defaults to the base URL with '/dataplatform/' appended.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The DataPlatform API endpoint URL.

### `url_keycloak` {#cmem_client.config.Config.url_keycloak}

```python
url_keycloak: HttpUrl
```

Get the Keycloak authentication server base URL.

Returns the URL of the Keycloak server used for authentication and
authorization. If not explicitly set, it defaults to the base URL
with '/auth/' appended.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The Keycloak server base URL.

### `url_keycloak_issuer` {#cmem_client.config.Config.url_keycloak_issuer}

```python
url_keycloak_issuer: HttpUrl
```

Get the Keycloak realm issuer URL.

Returns the issuer URL for the specific Keycloak realm, which is used
for token validation and OpenID Connect flows. This URL is constructed
from the Keycloak base URL and the realm identifier.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The Keycloak realm issuer URL.

<details class="note" open markdown="1">
<summary>Note</summary>

This property cannot be set directly. It is automatically constructed
based on the Keycloak URL and realm ID. To customize it, set the
url_keycloak property and realm_id attribute instead.

</details>

### `url_marketplace` {#cmem_client.config.Config.url_marketplace}

```python
url_marketplace: HttpUrl
```

Get the local marketplace URL used as the license-token issuer.

Returns the URL of the marketplace bundled beside this Corporate Memory
instance. Its ``/api/session`` endpoint mints the encrypted license token
(``x-eccenca-auth``) attached to outbound marketplace requests. If not
explicitly set, it defaults to the base URL with '/marketplace/' appended.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The local marketplace URL.

### `url_oauth_token` {#cmem_client.config.Config.url_oauth_token}

```python
url_oauth_token: HttpUrl
```

Get the OAuth 2.0 token endpoint URL.

Returns the URL for the OAuth 2.0 token endpoint, which is used by
authentication providers to obtain access tokens. If not explicitly
set, it defaults to the standard OpenID Connect token endpoint path
within the Keycloak realm.

**Returns:**

- <code>[HttpUrl](../models/url/index.md#cmem_client.models.url.HttpUrl)</code> – The OAuth 2.0 token endpoint URL.

### `verify` {#cmem_client.config.Config.verify}

```python
verify: bool | str
```

Get the SSL/TLS certificate verification flag or CA bundle path.

**Returns:**

- <code>bool | str</code> – True if SSL/TLS certificates should be verified using the default
- <code>bool | str</code> – CA bundle, False to disable verification, or a string path to a
- <code>bool | str</code> – custom CA bundle file.
- <code>bool | str</code> – Defaults to True for security reasons.

<details class="note" open markdown="1">
<summary>Note</summary>

Disabling SSL verification should only be done in development
environments. Production deployments should always verify certificates.

</details>

## `DEFAULT_CMEM_BASE_URI` {#cmem_client.config.DEFAULT_CMEM_BASE_URI}

```python
DEFAULT_CMEM_BASE_URI = 'http://docker.localhost'
```

