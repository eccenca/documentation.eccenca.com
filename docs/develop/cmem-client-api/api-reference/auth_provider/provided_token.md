---
title: "cmem-client: provided_token module"
description: "Provided token authentication provider."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.auth_provider.provided_token` {#cmem_client.auth_provider.provided_token}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Provided token authentication provider.

This module provides an authentication provider for scenarios where access tokens
are obtained by calling a method on a user-provided object. This enables integration
with custom authentication systems, third-party libraries, or dynamic token generation
logic that is managed outside the cmem-client library.

The ProvidedToken provider delegates token retrieval to a callable method on an
external object, allowing maximum flexibility for custom authentication workflows
while maintaining compatibility with the Corporate Memory client interface.

**Classes:**

- [**ProvidedToken**](#cmem_client.auth_provider.provided_token.ProvidedToken) – Authentication provider that retrieves tokens by calling a method on a provided object.

## `ProvidedToken` {#cmem_client.auth_provider.provided_token.ProvidedToken}

```python
ProvidedToken(provider_object, method_name)
```

Bases: <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code>

Authentication provider that retrieves tokens by calling a method on a provided object.

This provider enables integration with custom authentication systems by delegating
token retrieval to a callable method on an external object.

**Attributes:**

- [**provider_object**](#cmem_client.auth_provider.provided_token.ProvidedToken.provider_object) (<code>object</code>) – The object containing the token retrieval method.
- [**method_name**](#cmem_client.auth_provider.provided_token.ProvidedToken.method_name) (<code>str</code>) – The name of the method to call for retrieving tokens.
- [**logger**](#cmem_client.auth_provider.provided_token.ProvidedToken.logger) (<code>Logger</code>) – Logger for the authentication provider.

**Functions:**

- [**from_cmempy**](#cmem_client.auth_provider.provided_token.ProvidedToken.from_cmempy) – Create an authentication provider from a cmempy environment.
- [**from_context**](#cmem_client.auth_provider.provided_token.ProvidedToken.from_context) – Create an authentication provider from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.auth_provider.provided_token.ProvidedToken.from_dict) – Create an authentication provider from a plain dictionary.
- [**from_env**](#cmem_client.auth_provider.provided_token.ProvidedToken.from_env) – Create an authentication provider from environment variables.
- [**get_access_token**](#cmem_client.auth_provider.provided_token.ProvidedToken.get_access_token) – Get the access token for Bearer Authorization header.

**Parameters:**

- **provider_object** (<code>object</code>) – Object with a callable method that returns access tokens.
- **method_name** (<code>str</code>) – Name of the method to call on provider_object.

**Raises:**

- <code>AttributeError</code> – If provider_object does not have the specified method.

### `from_cmempy` {#cmem_client.auth_provider.provided_token.ProvidedToken.from_cmempy}

```python
from_cmempy(config)
```

Create an authentication provider from a cmempy environment.

### `from_context` {#cmem_client.auth_provider.provided_token.ProvidedToken.from_context}

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

### `from_dict` {#cmem_client.auth_provider.provided_token.ProvidedToken.from_dict}

```python
from_dict(config, d)
```

Create an authentication provider from a plain dictionary.

Selects and configures the appropriate authentication provider based
on the ``OAUTH_GRANT_TYPE`` key in the dictionary, defaulting to
``"client_credentials"`` when not specified.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Configuration object containing Corporate Memory connection
details and endpoint URLs.
- **d** (<code>dict[str, str]</code>) – Dictionary of configuration values. The ``OAUTH_GRANT_TYPE`` key
controls which provider is created. Remaining keys are forwarded
to the selected provider's ``from_dict`` factory.

**Returns:**

- <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – A configured AuthProvider instance.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If ``OAUTH_GRANT_TYPE`` is not a supported
value or if required keys for the selected provider are missing.

### `from_env` {#cmem_client.auth_provider.provided_token.ProvidedToken.from_env}

```python
from_env(config)
```

Create an authentication provider from environment variables.

This factory method automatically selects and configures the appropriate
authentication provider based on the OAUTH_GRANT_TYPE environment variable.
It supports multiple OAuth 2.0 flows and authentication methods.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Configuration object containing Corporate Memory connection
details and endpoint URLs.

**Returns:**

- <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – A configured AuthProvider instance appropriate for the environment
- <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – configuration.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the OAUTH_GRANT_TYPE is not supported or
if required environment variables for the selected provider
are missing.

<details class="environment-variables" open markdown="1">
<summary>Environment Variables</summary>

OAUTH_GRANT_TYPE (optional): The OAuth flow type. Defaults to
    "client_credentials". Supported values:
    - "client_credentials": Client Credentials Flow for M2M auth
    - "password": Resource Owner Password Flow for trusted apps
    - "prefetched_token": Use externally obtained access token

</details>

### `get_access_token` {#cmem_client.auth_provider.provided_token.ProvidedToken.get_access_token}

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

### `logger` {#cmem_client.auth_provider.provided_token.ProvidedToken.logger}

```python
logger: logging.Logger = logging.getLogger(__name__)
```

### `method_name` {#cmem_client.auth_provider.provided_token.ProvidedToken.method_name}

```python
method_name: str = method_name
```

### `preferred_username` {#cmem_client.auth_provider.provided_token.ProvidedToken.preferred_username}

```python
preferred_username: str
```

The preferred username for the authentication provider.

### `provider_object` {#cmem_client.auth_provider.provided_token.ProvidedToken.provider_object}

```python
provider_object: object = provider_object
```

