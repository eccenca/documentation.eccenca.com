---
title: "prefetched_token"
tags:
  - API
  - Python
  - cmem-client
---

# `prefetched_token` {#cmem_client.auth_provider.prefetched_token}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Prefetched token authentication provider.

This module provides an authentication provider for scenarios where access tokens
are obtained through external means rather than through OAuth flows. This is useful
for environments where tokens are managed by external systems, CI/CD pipelines,
or when integrating with existing authentication infrastructure.

The PrefetchedToken provider simply stores and returns a pre-obtained access token
without performing any token refresh or validation. It's the responsibility of the
external system to ensure the token is valid and renewed when necessary.

This approach is often used in containerized environments, serverless functions,
or when tokens are managed by orchestration platforms.

**Classes:**

- [**PrefetchedToken**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken) – Authentication provider for externally managed access tokens.

## `PrefetchedToken` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken}

```python
PrefetchedToken(prefetched_token)
```

Bases: <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code>

Authentication provider for externally managed access tokens.

PrefetchedToken is designed for scenarios where access tokens are obtained
and managed by external systems rather than through standard OAuth 2.0 flows.
This provider simply stores and returns a pre-obtained token without performing
any validation, refresh, or expiration checking.

This approach is commonly used in:

- Containerized environments where tokens are injected at runtime
- CI/CD pipelines with token management systems
- Serverless functions with external authentication services
- Integration with existing authentication infrastructure
- Short-lived execution contexts where token refresh isn't needed

**Attributes:**

- [**prefetched_token**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.prefetched_token) (<code>str</code>) – The pre-obtained access token to be used for authentication.

<details class="important-notes" open markdown="1">
<summary>Important Notes</summary>

- No token validation or expiration checking is performed
- Token refresh is not supported; external systems must handle renewal
- The token is assumed to be valid and properly formatted
- Suitable for short-lived processes or external token management scenarios

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

For automatic token management with refresh capabilities, consider using
ClientCredentialsFlow or PasswordFlow instead.

</details>

**Functions:**

- [**from_cmempy**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_cmempy) – Create a Prefetched Token provider from a cmempy environment.
- [**from_context**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_context) – Create an authentication provider from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_dict) – Create a Prefetched Token provider from a plain dictionary.
- [**from_env**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_env) – Create a Prefetched Token provider from environment variables.
- [**get_access_token**](#cmem_client.auth_provider.prefetched_token.PrefetchedToken.get_access_token) – Get the access token for Bearer Authorization header.

Creates a provider instance that stores the given access token for use
in authentication requests. No validation or processing is performed
on the token; it is stored as-is.

**Parameters:**

- **prefetched_token** (<code>str</code>) – A pre-obtained access token string. The token
should be valid, properly formatted (typically JWT), and
have appropriate permissions for Corporate Memory operations.

<details class="note" open markdown="1">
<summary>Note</summary>

Unlike other authentication providers, this constructor does not
make any network requests or perform token validation. The token
is assumed to be valid and ready for immediate use.

</details>

### `from_cmempy` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_cmempy}

```python
from_cmempy(config)
```

Create a Prefetched Token provider from a cmempy environment.

### `from_context` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_context}

```python
from_context(context)
```

Create an authentication provider from a cmem-plugin-base context object.

Wraps the token callable exposed by the context's ``UserContext`` in a
``ProvidedToken`` provider.

**Parameters:**

- **context** (<code>object</code>) – An ``ExecutionContext`` or ``PluginContext`` instance from
``cmem-plugin-base``. Must expose a ``user`` attribute
(``UserContext``) with a ``token()`` method that returns a
valid bearer token.

**Returns:**

- <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – A ``ProvidedToken`` authentication provider backed by the
- <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – context's ``UserContext.token()`` method.

### `from_dict` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_dict}

```python
from_dict(config, d)
```

Create a Prefetched Token provider from a plain dictionary.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration object. Not used by
PrefetchedToken but required for interface consistency.
- **d** (<code>dict[str, str]</code>) – Dictionary of configuration values. Expected key:
``OAUTH_ACCESS_TOKEN`` (required).

**Returns:**

- <code>[PrefetchedToken](#cmem_client.auth_provider.prefetched_token.PrefetchedToken)</code> – A configured PrefetchedToken instance.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If ``OAUTH_ACCESS_TOKEN`` is missing or empty.

### `from_env` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.from_env}

```python
from_env(config)
```

Create a Prefetched Token provider from environment variables.

This factory method creates a provider instance by reading a pre-obtained
access token from the OAUTH_ACCESS_TOKEN environment variable.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration object. Note that this parameter
is not used by PrefetchedToken but is required to maintain
consistency with other AuthProvider implementations.

**Returns:**

- <code>[PrefetchedToken](#cmem_client.auth_provider.prefetched_token.PrefetchedToken)</code> – A configured PrefetchedToken instance ready for use.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the required OAUTH_ACCESS_TOKEN environment
variable is not set or is empty.

<details class="environment-variables" open markdown="1">
<summary>Environment Variables</summary>

OAUTH_ACCESS_TOKEN (required): The pre-obtained access token.
    Should be a valid JWT or other token format accepted by
    Corporate Memory. The token must have appropriate permissions
    for the intended operations.

</details>

<details class="use-cases" open markdown="1">
<summary>Use Cases</summary>

- Docker containers with token injection
- Kubernetes pods with secret mounting
- CI/CD pipelines with secure token storage
- Serverless functions with environment-based configuration
- Integration with external token management systems

</details>

### `get_access_token` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.get_access_token}

```python
get_access_token()
```

Get the access token for Bearer Authorization header.

Also sets the preferred username for the authentication provider via the extracted token.

**Returns:**

- <code>str</code> – A valid access token string.

**Raises:**

- <code>ValueError</code> – If the provider returned no access token.

<details class="note" open markdown="1">
<summary>Note</summary>

Implementations should handle token refresh logic internally when
tokens expire, ensuring this method always returns a valid token.

</details>

### `logger` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.logger}

```python
logger: logging.Logger = logging.getLogger(__name__)
```

Logger object for logging.

### `preferred_username` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.preferred_username}

```python
preferred_username: str
```

The preferred username for the authentication provider.

### `prefetched_token` {#cmem_client.auth_provider.prefetched_token.PrefetchedToken.prefetched_token}

```python
prefetched_token: str = prefetched_token
```

The pre-obtained access token used for authentication requests.

