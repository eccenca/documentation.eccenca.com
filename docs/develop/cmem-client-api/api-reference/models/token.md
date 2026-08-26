---
title: "cmem-client: token module"
tags:
  - API
  - Python
  - cmem-client
---

# `token` {#cmem_client.models.token}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Authentication token models for OAuth 2.0 flows.

This module provides models for handling OAuth 2.0 tokens, particularly
Keycloak tokens used in Corporate Memory authentication. It includes
automatic JWT parsing and expiration checking functionality.

The KeycloakToken model handles token lifecycle management, including
automatically parsing JWT contents and providing expiration checking
to support token refresh logic in authentication providers.

**Classes:**

- [**KeycloakToken**](#cmem_client.models.token.KeycloakToken) – A Keycloak token

**Functions:**

- [**default_factory_now**](#cmem_client.models.token.default_factory_now) – Get the current UTC datetime

## `KeycloakToken` {#cmem_client.models.token.KeycloakToken}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A Keycloak token

**Attributes:**

- [**access_token**](#cmem_client.models.token.KeycloakToken.access_token) (<code>str</code>) – The encoded bearer token, as sent in the ``Authorization``
header.
- [**expires_in**](#cmem_client.models.token.KeycloakToken.expires_in) (<code>int</code>) – Lifetime of the token in seconds, counted from when Keycloak
issued it.
- [**expires**](#cmem_client.models.token.KeycloakToken.expires) (<code>datetime</code>) – When the token expires. Taken from the ``exp`` claim of the decoded
token on creation, so the default is never what a caller sees.
- [**jwt**](#cmem_client.models.token.KeycloakToken.jwt) (<code>dict</code>) – Claims of the decoded token. The signature is not verified here, because
the token comes straight from the token endpoint over TLS.

**Functions:**

- [**is_expired**](#cmem_client.models.token.KeycloakToken.is_expired) – Check if token is expired
- [**model_post_init**](#cmem_client.models.token.KeycloakToken.model_post_init) – Do the post init

### `access_token` {#cmem_client.models.token.KeycloakToken.access_token}

```python
access_token: str
```

### `expires` {#cmem_client.models.token.KeycloakToken.expires}

```python
expires: datetime = Field(default_factory=default_factory_now)
```

### `expires_in` {#cmem_client.models.token.KeycloakToken.expires_in}

```python
expires_in: int
```

### `is_expired` {#cmem_client.models.token.KeycloakToken.is_expired}

```python
is_expired()
```

Check if token is expired

### `jwt` {#cmem_client.models.token.KeycloakToken.jwt}

```python
jwt: dict = Field(default_factory=dict)
```

### `model_config` {#cmem_client.models.token.KeycloakToken.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `model_post_init` {#cmem_client.models.token.KeycloakToken.model_post_init}

```python
model_post_init(context)
```

Do the post init

## `default_factory_now` {#cmem_client.models.token.default_factory_now}

```python
default_factory_now()
```

Get the current UTC datetime

