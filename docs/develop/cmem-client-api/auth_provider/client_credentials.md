# `client_credentials` {#cmem_client.auth_provider.client_credentials}

Client Credentials OAuth 2.0 flow authentication provider.

This module implements the Client Credentials Flow authentication method for
accessing eccenca Corporate Memory via OAuth 2.0. This flow is designed for
machine-to-machine authentication where no user interaction is required.

The Client Credentials Flow exchanges client ID and client secret for an access
token directly with the authorization server. It's ideal for backend services,
APIs, and automated systems that need to authenticate without user involvement.

This implementation handles token caching and automatic renewal when tokens expire.

**Classes:**

- [**ClientCredentialsFlow**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow) – Client Credentials OAuth 2.0 flow authentication provider.

**Attributes:**

- [**DEFAULT_OAUTH_CLIENT_SECRET**](#cmem_client.auth_provider.client_credentials.DEFAULT_OAUTH_CLIENT_SECRET) –

## `ClientCredentialsFlow` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow}

```python
ClientCredentialsFlow(config, client_id, client_secret)
```

Bases: <code>[AuthProvider](../auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code>

Client Credentials OAuth 2.0 flow authentication provider.

Implements the Client Credentials Flow (RFC 6749, section 4.4) for machine-to-machine
authentication with Corporate Memory via Keycloak. This flow exchanges client credentials
(client ID and secret) directly for access tokens without user interaction.

The provider handles automatic token caching and refresh, ensuring that get_access_token()
always returns a valid, non-expired token. It's designed for backend services, CLIs,
daemons, and other automated systems that need to authenticate as an application
rather than on behalf of a user.

**Attributes:**

- [**client_id**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.client_id) (<code>str</code>) – The OAuth 2.0 client identifier for the application.
- [**client_secret**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.client_secret) (<code>str</code>) – The confidential client secret for authentication.
- [**config**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.config) (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing endpoint URLs.
- [**httpx**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.httpx) (<code>Client</code>) – HTTP client for making token requests to the OAuth server.
- [**token**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.token) (<code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code>) – Currently cached Keycloak token with expiration tracking.

<details class="see-also" open markdown="1">
<summary>See Also</summary>

<https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow>
<https://tools.ietf.org/html/rfc6749#section-4.4>

</details>

**Functions:**

- [**fetch_new_token**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.fetch_new_token) – Fetch a new access token from the OAuth 2.0 token endpoint.
- [**from_cmempy**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_cmempy) – Create a Client Credentials Flow provider from a cmempy environment.
- [**from_context**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_context) – Create an authentication provider from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_dict) – Create a Client Credentials Flow provider from a plain dictionary.
- [**from_env**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_env) – Create a Client Credentials Flow provider from environment variables.
- [**get_access_token**](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.get_access_token) – Get the access token for Bearer Authorization header.

Creates a new provider instance and immediately fetches an initial access
token. The provider will handle token refresh automatically when needed.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs
and other connection details.
- **client_id** (<code>str</code>) – The OAuth 2.0 client identifier registered with the
authorization server.
- **client_secret** (<code>str</code>) – The confidential client secret associated with the
client_id for authentication.

**Raises:**

- <code>HTTPError</code> – If the initial token request fails due to network issues
or invalid credentials.
- <code>ValidationError</code> – If the token response cannot be parsed as a valid
Keycloak token.

<details class="note" open markdown="1">
<summary>Note</summary>

The constructor makes an immediate HTTP request to fetch the initial
token, so ensure network connectivity and valid credentials before
instantiation.

</details>

### `client_id` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.client_id}

```python
client_id: str = client_id
```

OAuth 2.0 client identifier used to identify the application to the authorization server.

### `client_secret` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.client_secret}

```python
client_secret: str = client_secret
```

Confidential client secret used to authenticate the application with the OAuth server.

### `config` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.config}

```python
config: Config = config
```

Corporate Memory configuration containing OAuth token endpoint and other URLs.

### `fetch_new_token` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.fetch_new_token}

```python
fetch_new_token()
```

Fetch a new access token from the OAuth 2.0 token endpoint.

Makes an HTTP POST request to the Keycloak token endpoint using the
Client Credentials Flow parameters. The response is parsed and returned
as a KeycloakToken object with automatic expiration tracking.

**Returns:**

- <code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code> – A new KeycloakToken instance with the fresh access token and
- <code>[KeycloakToken](../models/token.md#cmem_client.models.token.KeycloakToken)</code> – expiration information.

**Raises:**

- <code>HTTPError</code> – If the token request fails due to network issues,
invalid credentials, or server errors.
- <code>ValidationError</code> – If the token response cannot be parsed as a
valid Keycloak token format.

<details class="note" open markdown="1">
<summary>Note</summary>

This method performs a synchronous HTTP request and should not be
called directly in most cases. Use get_access_token() instead,
which handles caching and only calls this method when necessary.

</details>

<details class="implementation-details" open markdown="1">
<summary>Implementation Details</summary>

- Uses the standard OAuth 2.0 Client Credentials Flow parameters
- Sends credentials in the request body (not in Authorization header)
- Automatically decodes the JSON response and validates the format
- Extracts JWT claims for expiration tracking

</details>

### `from_cmempy` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_cmempy}

```python
from_cmempy(config)
```

Create a Client Credentials Flow provider from a cmempy environment.

### `from_context` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_context}

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

### `from_dict` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_dict}

```python
from_dict(config, d)
```

Create a Client Credentials Flow provider from a plain dictionary.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs.
- **d** (<code>dict[str, str]</code>) – Dictionary of configuration values. Expected keys:
``OAUTH_CLIENT_ID`` (optional, defaults to ``"cmem-service-account"``)
and ``OAUTH_CLIENT_SECRET`` (required).

**Returns:**

- <code>[ClientCredentialsFlow](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow)</code> – A configured ClientCredentialsFlow instance.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If ``OAUTH_CLIENT_SECRET`` is missing or empty.

### `from_env` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.from_env}

```python
from_env(config)
```

Create a Client Credentials Flow provider from environment variables.

This factory method creates a provider instance by reading OAuth client
credentials from environment variables. It's the recommended way to
create providers in production environments where credentials are
managed externally.

**Parameters:**

- **config** (<code>[Config](../config.md#cmem_client.config.Config)</code>) – Corporate Memory configuration containing OAuth endpoint URLs.

**Returns:**

- <code>[ClientCredentialsFlow](#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow)</code> – A configured ClientCredentialsFlow instance ready for use.

**Raises:**

- <code>[ClientEnvConfigError](../exceptions.md#cmem_client.exceptions.ClientEnvConfigError)</code> – If the required OAUTH_CLIENT_SECRET environment
variable is not set.

<details class="environment-variables" open markdown="1">
<summary>Environment Variables</summary>

OAUTH_CLIENT_ID (optional): The OAuth 2.0 client identifier.
    Defaults to "cmem-service-account" if not specified.
OAUTH_CLIENT_SECRET (required): The confidential client secret
    for authentication. Must be provided.

</details>

<details class="security-note" open markdown="1">
<summary>Security Note</summary>

Client secrets should be stored securely and never committed to
version control. Use environment variables or secure secret
management systems in production.

</details>

### `get_access_token` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.get_access_token}

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

### `httpx` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.httpx}

```python
httpx: httpx.Client = httpx.Client(verify=config.verify, headers=config.extra_headers)
```

HTTP client instance used for making requests to the OAuth token endpoint.

### `logger` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.logger}

```python
logger: logging.Logger = logging.getLogger(__name__)
```

Logger object for logging.

### `preferred_username` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.preferred_username}

```python
preferred_username: str
```

The preferred username for the authentication provider.

### `token` {#cmem_client.auth_provider.client_credentials.ClientCredentialsFlow.token}

```python
token: KeycloakToken = self.fetch_new_token()
```

Currently cached access token with automatic expiration tracking and JWT parsing.

## `DEFAULT_OAUTH_CLIENT_SECRET` {#cmem_client.auth_provider.client_credentials.DEFAULT_OAUTH_CLIENT_SECRET}

```python
DEFAULT_OAUTH_CLIENT_SECRET = 'c8c12828-000c-467b-9b6d-2d6b5e16df4a'
```

