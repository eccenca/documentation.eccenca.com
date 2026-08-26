---
title: "cmem-client: credentials module"
tags:
  - API
  - Python
  - cmem-client
---

# `credentials` {#cmem_client.models.credentials}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models for the OAuth2 credentials.

These models carry the credentials of an OAuth2 flow as a validated object, instead of
a set of loose strings. The marketplace operations of ``client.marketplace`` take one
of them to authenticate against a marketplace server. The secrets are held as
``SecretStr``, so they are masked when a model is printed or logged.

**Classes:**

- [**BaseCredentials**](#cmem_client.models.credentials.BaseCredentials) – Base class for OAuth2 credential types
- [**ClientCredentials**](#cmem_client.models.credentials.ClientCredentials) – The client credentials class
- [**PasswordCredentials**](#cmem_client.models.credentials.PasswordCredentials) – The password credentials class

## `BaseCredentials` {#cmem_client.models.credentials.BaseCredentials}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Base class for OAuth2 credential types

**Attributes:**

- [**client_id**](#cmem_client.models.credentials.BaseCredentials.client_id) (<code>str</code>) – Keycloak client the credentials authenticate with. The default suits
the password flow; the client credentials flow needs the ID of the service
account instead.

### `client_id` {#cmem_client.models.credentials.BaseCredentials.client_id}

```python
client_id: str = 'cmemc'
```

### `model_config` {#cmem_client.models.credentials.BaseCredentials.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `ClientCredentials` {#cmem_client.models.credentials.ClientCredentials}

Bases: <code>[BaseCredentials](#cmem_client.models.credentials.BaseCredentials)</code>

The client credentials class

**Attributes:**

- [**client_secret**](#cmem_client.models.credentials.ClientCredentials.client_secret) (<code>SecretStr</code>) – Secret of the Keycloak client named by ``client_id``.

### `client_id` {#cmem_client.models.credentials.ClientCredentials.client_id}

```python
client_id: str = 'cmemc'
```

### `client_secret` {#cmem_client.models.credentials.ClientCredentials.client_secret}

```python
client_secret: SecretStr
```

### `model_config` {#cmem_client.models.credentials.ClientCredentials.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `PasswordCredentials` {#cmem_client.models.credentials.PasswordCredentials}

Bases: <code>[BaseCredentials](#cmem_client.models.credentials.BaseCredentials)</code>

The password credentials class

**Attributes:**

- [**username**](#cmem_client.models.credentials.PasswordCredentials.username) (<code>str</code>) – Name of the Keycloak user.
- [**password**](#cmem_client.models.credentials.PasswordCredentials.password) (<code>SecretStr</code>) – Password of the Keycloak user.

### `client_id` {#cmem_client.models.credentials.PasswordCredentials.client_id}

```python
client_id: str = 'cmemc'
```

### `model_config` {#cmem_client.models.credentials.PasswordCredentials.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `password` {#cmem_client.models.credentials.PasswordCredentials.password}

```python
password: SecretStr
```

### `username` {#cmem_client.models.credentials.PasswordCredentials.username}

```python
username: str
```

