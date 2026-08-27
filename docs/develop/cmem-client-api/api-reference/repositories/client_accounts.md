---
title: "cmem-client: client_accounts module"
description: "Repository for the Keycloak OpenID Connect client accounts of a deployment."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.client_accounts` {#cmem_client.repositories.client_accounts}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the Keycloak OpenID Connect client accounts of a deployment.

Provides ClientAccountRepository for listing the client accounts (service accounts)
which can authenticate against Corporate Memory, and for reading or rotating their
secret.

**Examples:**

List the client accounts and inspect one:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> list(client.client_accounts)
>>> account = client.client_accounts["cmem-service-account"]
```

Read the current secret of an account:

```pycon
>>> client.client_accounts.get_secret(account.id)
```

``generate_secret()`` rotates it and returns the new one. It is described rather
than shown running, because it invalidates the secret in use: rotating the account
a deployment authenticates with locks out everything configured with the old value,
and unlike the workspace and the store, Keycloak is not restored afterwards.

**Classes:**

- [**ClientAccountRepository**](#cmem_client.repositories.client_accounts.ClientAccountRepository) – Repository for Keycloak OpenID Connect client accounts.

## `ClientAccountRepository` {#cmem_client.repositories.client_accounts.ClientAccountRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>

Repository for Keycloak OpenID Connect client accounts.

Lists clients in the Corporate Memory Keycloak realm that use the
``openid-connect`` protocol and have a client secret configured.
Clients are keyed by their ``clientId``.

**Functions:**

- [**fetch_data**](#cmem_client.repositories.client_accounts.ClientAccountRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**generate_secret**](#cmem_client.repositories.client_accounts.ClientAccountRepository.generate_secret) – Generate and return a new secret for a client.
- [**get_secret**](#cmem_client.repositories.client_accounts.ClientAccountRepository.get_secret) – Get the current secret for a client.
- [**items**](#cmem_client.repositories.client_accounts.ClientAccountRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.client_accounts.ClientAccountRepository.keys) – Get the keys of the repository
- [**values**](#cmem_client.repositories.client_accounts.ClientAccountRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.client_accounts.ClientAccountRepository.logger) (<code>Logger</code>) – Gets the client logger

### `fetch_data` {#cmem_client.repositories.client_accounts.ClientAccountRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `generate_secret` {#cmem_client.repositories.client_accounts.ClientAccountRepository.generate_secret}

```python
generate_secret(client_uuid)
```

Generate and return a new secret for a client.

**Parameters:**

- **client_uuid** (<code>str</code>) – The Keycloak UUID of the client (not the clientId).

**Returns:**

- <code>str</code> – The newly generated client secret value.

### `get_secret` {#cmem_client.repositories.client_accounts.ClientAccountRepository.get_secret}

```python
get_secret(client_uuid)
```

Get the current secret for a client.

**Parameters:**

- **client_uuid** (<code>str</code>) – The Keycloak UUID of the client (not the clientId).

**Returns:**

- <code>str</code> – The current client secret value.

### `items` {#cmem_client.repositories.client_accounts.ClientAccountRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.client_accounts.ClientAccountRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.client_accounts.ClientAccountRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `values` {#cmem_client.repositories.client_accounts.ClientAccountRepository.values}

```python
values()
```

Get the values of the repository

