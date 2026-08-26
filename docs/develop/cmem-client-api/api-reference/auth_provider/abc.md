---
title: "cmem-client: abc module"
tags:
  - API
  - Python
  - cmem-client
---

# `abc` {#cmem_client.auth_provider.abc}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Abstract base class and factory for authentication providers.

This module defines the AuthProvider abstract base class that establishes the
interface all authentication providers must implement. It also provides a
factory method that automatically selects the appropriate authentication
provider based on environment variables.

The factory method supports automatic configuration from environment variables,
making it easy to switch between different authentication methods without
code changes by simply setting the OAUTH_GRANT_TYPE environment variable.

**Classes:**

- [**AuthProvider**](#cmem_client.auth_provider.abc.AuthProvider) – Abstract base class for authentication providers.

**Attributes:**

- [**DEFAULT_OAUTH_CLIENT_ID**](#cmem_client.auth_provider.abc.DEFAULT_OAUTH_CLIENT_ID) –

## `AuthProvider` {#cmem_client.auth_provider.abc.AuthProvider}

Bases: <code>ABC</code>

Abstract base class for authentication providers.

AuthProvider defines the common interface that all authentication providers
must implement to work with the Corporate Memory client. It provides the
contract for obtaining access tokens and includes a factory method for
creating appropriate provider instances based on environment configuration.

All concrete authentication provider implementations must inherit from this
class and implement the get_access_token method. The class also provides
automatic provider selection through environment variables.

**Functions:**

- [**from_cmempy**](#cmem_client.auth_provider.abc.AuthProvider.from_cmempy) – Create an authentication provider from a cmempy environment.
- [**from_context**](#cmem_client.auth_provider.abc.AuthProvider.from_context) – Create an authentication provider from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.auth_provider.abc.AuthProvider.from_dict) – Create an authentication provider from a plain dictionary.
- [**from_env**](#cmem_client.auth_provider.abc.AuthProvider.from_env) – Create an authentication provider from environment variables.
- [**get_access_token**](#cmem_client.auth_provider.abc.AuthProvider.get_access_token) – Get the access token for Bearer Authorization header.

**Attributes:**

- [**logger**](#cmem_client.auth_provider.abc.AuthProvider.logger) (<code>Logger</code>) – The logger for the auth provider.
- [**preferred_username**](#cmem_client.auth_provider.abc.AuthProvider.preferred_username) (<code>str</code>) – The preferred username for the authentication provider.

### `from_cmempy` {#cmem_client.auth_provider.abc.AuthProvider.from_cmempy}

```python
from_cmempy(config)
```

Create an authentication provider from a cmempy environment.

### `from_context` {#cmem_client.auth_provider.abc.AuthProvider.from_context}

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

- <code>[AuthProvider](#cmem_client.auth_provider.abc.AuthProvider)</code> – A ``ProvidedToken`` authentication provider backed by the
- <code>[AuthProvider](#cmem_client.auth_provider.abc.AuthProvider)</code> – context's ``UserContext.token()`` method.

### `from_dict` {#cmem_client.auth_provider.abc.AuthProvider.from_dict}

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

- <code>[AuthProvider](#cmem_client.auth_provider.abc.AuthProvider)</code> – A configured AuthProvider instance.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If ``OAUTH_GRANT_TYPE`` is not a supported
value or if required keys for the selected provider are missing.

### `from_env` {#cmem_client.auth_provider.abc.AuthProvider.from_env}

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

- <code>[AuthProvider](#cmem_client.auth_provider.abc.AuthProvider)</code> – A configured AuthProvider instance appropriate for the environment
- <code>[AuthProvider](#cmem_client.auth_provider.abc.AuthProvider)</code> – configuration.

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

### `get_access_token` {#cmem_client.auth_provider.abc.AuthProvider.get_access_token}

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

### `logger` {#cmem_client.auth_provider.abc.AuthProvider.logger}

```python
logger: logging.Logger
```

The logger for the auth provider.

### `preferred_username` {#cmem_client.auth_provider.abc.AuthProvider.preferred_username}

```python
preferred_username: str
```

The preferred username for the authentication provider.

## `DEFAULT_OAUTH_CLIENT_ID` {#cmem_client.auth_provider.abc.DEFAULT_OAUTH_CLIENT_ID}

```python
DEFAULT_OAUTH_CLIENT_ID = 'cmem-service-account'
```

