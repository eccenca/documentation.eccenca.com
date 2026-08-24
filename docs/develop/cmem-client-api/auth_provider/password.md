# `password` {#cmem_client.auth_provider.password}

Resource Owner Password OAuth 2.0 flow authentication provider.

This module implements the Resource Owner Password Flow authentication method,
which allows highly-trusted applications to authenticate users by collecting
their username and password credentials directly.

Security Warning: This flow should only be used by absolutely trusted
applications as it requires handling user passwords directly. It's typically
used for legacy applications or first-party applications where other OAuth flows
are not feasible.

This implementation handles token caching and automatic renewal when tokens expire,
similar to the Client Credentials Flow but using username/password credentials.

**Classes:**

- [**PasswordFlow**](#cmem_client.auth_provider.password.PasswordFlow) – Resource Owner Password OAuth 2.0 flow authentication provider.

## `PasswordFlow` {#cmem_client.auth_provider.password.PasswordFlow}

```python
PasswordFlow(config, client_id, username, password)
```

Bases: <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code>

Resource Owner Password OAuth 2.0 flow authentication provider.

Security Warning: This authentication flow should only be used by
absolutely trusted applications as it requires handling user passwords directly.

Implements the Resource Owner Password Flow (RFC 6749, section 4.3) for
authentication with Corporate Memory via Keycloak. This flow exchanges user
credentials (username and password) directly for access tokens, bypassing
the standard OAuth 2.0 authorization code flow.

This provider handles automatic token caching and refresh, ensuring that
get_access_token() always returns a valid token. It's typically used for
legacy applications, first-party applications, or scenarios where the standard
OAuth flows are not feasible.

**Attributes:**

- [**client_id**](#cmem_client.auth_provider.password.PasswordFlow.client_id) (<code>str</code>) – The OAuth 2.0 client identifier for the application.
- [**username**](#cmem_client.auth_provider.password.PasswordFlow.username) (<code>str</code>) – The user's username for authentication.
- [**password**](#cmem_client.auth_provider.password.PasswordFlow.password) (<code>str</code>) – The user's password for authentication.
- [**config**](#cmem_client.auth_provider.password.PasswordFlow.config) (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing endpoint URLs.
- [**httpx**](#cmem_client.auth_provider.password.PasswordFlow.httpx) (<code>Client</code>) – HTTP client for making token requests to the OAuth server.
- [**token**](#cmem_client.auth_provider.password.PasswordFlow.token) (<code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code>) – Currently cached Keycloak token with expiration tracking.

<details class="security-considerations" open markdown="1">
<summary>Security Considerations</summary>

- User credentials are sent directly to the authorization server
- Passwords may be stored in memory for token refresh purposes
- Only use in highly trusted applications with secure credential handling
- Consider using Client Credentials Flow for machine-to-machine auth instead

</details>

<details class="see-also" open markdown="1">
<summary>See Also</summary>

https://auth0.com/docs/get-started/authentication-and-authorization-flow/resource-owner-password-flow
https://tools.ietf.org/html/rfc6749#section-4.3

</details>

**Functions:**

- [**fetch_new_token**](#cmem_client.auth_provider.password.PasswordFlow.fetch_new_token) – Fetch a new access token from the OAuth 2.0 token endpoint.
- [**from_cmempy**](#cmem_client.auth_provider.password.PasswordFlow.from_cmempy) – Create a Password Flow provider from a cmempy environment.
- [**from_context**](#cmem_client.auth_provider.password.PasswordFlow.from_context) – Create an authentication provider from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.auth_provider.password.PasswordFlow.from_dict) – Create a Password Flow provider from a plain dictionary.
- [**from_env**](#cmem_client.auth_provider.password.PasswordFlow.from_env) – Create a Password Flow provider from environment variables.
- [**get_access_token**](#cmem_client.auth_provider.password.PasswordFlow.get_access_token) – Get the access token for Bearer Authorization header.

Security Warning: This constructor stores the user's password in memory
for potential token refresh operations. Only use in absolutely trusted applications.

Creates a new provider instance and immediately fetches an initial access
token. The provider will handle token refresh automatically when needed.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs
and other connection details.
- **client_id** (<code>str</code>) – The OAuth 2.0 client identifier registered with the
authorization server.
- **username** (<code>str</code>) – The user's username or email address for authentication.
- **password** (<code>str</code>) – The user's password for authentication.

**Raises:**

- <code>HTTPError</code> – If the initial token request fails due to network issues
or invalid credentials.
- <code>ValidationError</code> – If the token response cannot be parsed as a valid
Keycloak token.

<details class="security-note" open markdown="1">
<summary>Security Note</summary>

The constructor makes an immediate HTTP request to fetch the initial
token, sending the user's credentials over the network. Ensure secure
network connections (HTTPS) and proper credential handling.

</details>

### `client_id` {#cmem_client.auth_provider.password.PasswordFlow.client_id}

```python
client_id: str = client_id
```

OAuth 2.0 client identifier used to identify the application to the authorization server.

### `config` {#cmem_client.auth_provider.password.PasswordFlow.config}

```python
config: Config = config
```

Corporate Memory configuration containing OAuth token endpoint and other URLs.

### `fetch_new_token` {#cmem_client.auth_provider.password.PasswordFlow.fetch_new_token}

```python
fetch_new_token()
```

Fetch a new access token from the OAuth 2.0 token endpoint.

Security Warning: This method sends user credentials (username and password)
over the network to the authorization server. Ensure secure connections (HTTPS).

Makes an HTTP POST request to the Keycloak token endpoint using the
Resource Owner Password Flow parameters. The response is parsed and returned
as a KeycloakToken object with automatic expiration tracking.

**Returns:**

- <code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code> – A new KeycloakToken instance with the fresh access token and
- <code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code> – expiration information.

**Raises:**

- <code>HTTPError</code> – If the token request fails due to network issues,
invalid credentials, or server errors.
- <code>ValidationError</code> – If the token response cannot be parsed as a
valid Keycloak token format.

<details class="security-considerations" open markdown="1">
<summary>Security Considerations</summary>

- User credentials are sent in plaintext (over HTTPS)
- Consider the security implications of credential reuse for token refresh
- Monitor for credential compromise if tokens are frequently refreshed

</details>

<details class="note" open markdown="1">
<summary>Note</summary>

This method performs a synchronous HTTP request and should not be
called directly in most cases. Use get_access_token() instead,
which handles caching and only calls this method when necessary.

</details>

<details class="implementation-details" open markdown="1">
<summary>Implementation Details</summary>

- Uses the standard OAuth 2.0 Resource Owner Password Flow parameters
- Sends credentials in the request body (not in Authorization header)
- Automatically decodes the JSON response and validates the format
- Extracts JWT claims for expiration tracking

</details>

### `from_cmempy` {#cmem_client.auth_provider.password.PasswordFlow.from_cmempy}

```python
from_cmempy(config)
```

Create a Password Flow provider from a cmempy environment.

### `from_context` {#cmem_client.auth_provider.password.PasswordFlow.from_context}

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

### `from_dict` {#cmem_client.auth_provider.password.PasswordFlow.from_dict}

```python
from_dict(config, d)
```

Create a Password Flow provider from a plain dictionary.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs.
- **d** (<code>dict[str, str]</code>) – Dictionary of configuration values. Expected keys:
``OAUTH_USER`` (required), ``OAUTH_PASSWORD`` (required),
and ``OAUTH_CLIENT_ID`` (optional, defaults to ``"cmem-service-account"``).

**Returns:**

- <code>[PasswordFlow](#cmem_client.auth_provider.password.PasswordFlow)</code> – A configured PasswordFlow instance.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If ``OAUTH_USER`` or ``OAUTH_PASSWORD`` are missing.

### `from_env` {#cmem_client.auth_provider.password.PasswordFlow.from_env}

```python
from_env(config)
```

Create a Password Flow provider from environment variables.

Security Warning: This method reads user credentials from environment
variables, which may be visible in process lists or logs. Use with extreme caution.

This factory method creates a provider instance by reading user credentials
from environment variables. While more secure than hardcoded credentials,
environment variables should be properly protected in production environments.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs.

**Returns:**

- <code>[PasswordFlow](#cmem_client.auth_provider.password.PasswordFlow)</code> – A configured PasswordFlow instance ready for use.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the required OAUTH_USER or OAUTH_PASSWORD
environment variables are not set.

<details class="environment-variables" open markdown="1">
<summary>Environment Variables</summary>

OAUTH_USER (required): The username or email address for authentication.
    Must be a valid user account in the Corporate Memory system.
OAUTH_PASSWORD (required): The user's password for authentication.
    Should be handled securely and not logged.
OAUTH_CLIENT_ID (optional): The OAuth 2.0 client identifier.
    Defaults to "cmem-service-account" if not specified.

</details>

<details class="security-notes" open markdown="1">
<summary>Security Notes</summary>

- Environment variables may be visible in process lists
- Use secure credential management in production environments
- Consider using Client Credentials Flow for service accounts instead
- Ensure proper access controls on systems storing these credentials

</details>

### `get_access_token` {#cmem_client.auth_provider.password.PasswordFlow.get_access_token}

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

### `httpx` {#cmem_client.auth_provider.password.PasswordFlow.httpx}

```python
httpx: httpx.Client = httpx.Client(verify=config.verify, headers=config.extra_headers)
```

HTTP client instance used for making requests to the OAuth token endpoint.

### `logger` {#cmem_client.auth_provider.password.PasswordFlow.logger}

```python
logger: logging.Logger = logging.getLogger(__name__)
```

Logger object used to log messages.

### `password` {#cmem_client.auth_provider.password.PasswordFlow.password}

```python
password: str = password
```

User's password for authentication. ⚠️ Stored in memory for token refresh.

### `preferred_username` {#cmem_client.auth_provider.password.PasswordFlow.preferred_username}

```python
preferred_username: str
```

The preferred username for the authentication provider.

### `token` {#cmem_client.auth_provider.password.PasswordFlow.token}

```python
token: KeycloakToken = self.fetch_new_token()
```

Currently cached access token with automatic expiration tracking and JWT parsing.

### `username` {#cmem_client.auth_provider.password.PasswordFlow.username}

```python
username: str = username
```

User's username/email for authentication with the OAuth server.

