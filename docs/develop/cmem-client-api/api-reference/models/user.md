---
title: "user"
tags:
  - API
  - Python
  - cmem-client
---

# `user` {#cmem_client.models.user}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Keycloak user and group models.

Corporate Memory keeps its accounts in Keycloak. The user accounts of the configured
realm are the items of ``client.user_accounts``, keyed by their username, and the
groups a user belongs to decide which access conditions apply to them.

**Classes:**

- [**Group**](#cmem_client.models.user.Group) – A Keycloak group in the Corporate Memory realm.
- [**User**](#cmem_client.models.user.User) – A Keycloak user account in the Corporate Memory realm.

## `Group` {#cmem_client.models.user.Group}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A Keycloak group in the Corporate Memory realm.

**Attributes:**

- [**id**](#cmem_client.models.user.Group.id) (<code>str</code>) – Internal Keycloak identifier of the group, a UUID.
- [**name**](#cmem_client.models.user.Group.name) (<code>str</code>) – Name of the group.
- [**path**](#cmem_client.models.user.Group.path) (<code>str</code>) – Full path of the group, which spells out its parents for a nested group,
e.g. ``/department/team``.

### `id` {#cmem_client.models.user.Group.id}

```python
id: str
```

### `model_config` {#cmem_client.models.user.Group.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.user.Group.name}

```python
name: str
```

### `path` {#cmem_client.models.user.Group.path}

```python
path: str = ''
```

## `User` {#cmem_client.models.user.User}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A Keycloak user account in the Corporate Memory realm.

**Attributes:**

- [**id**](#cmem_client.models.user.User.id) (<code>str</code>) – Internal Keycloak identifier of the account, a UUID. Empty on an account
which was built locally and not yet created.
- [**username**](#cmem_client.models.user.User.username) (<code>str</code>) – Login name of the account. This is the key of the repository.
- [**email**](#cmem_client.models.user.User.email) (<code>str</code>) – Mail address of the account.
- [**first_name**](#cmem_client.models.user.User.first_name) (<code>str</code>) – Given name of the account holder.
- [**last_name**](#cmem_client.models.user.User.last_name) (<code>str</code>) – Family name of the account holder.
- [**enabled**](#cmem_client.models.user.User.enabled) (<code>bool</code>) – Whether the account may log in. A disabled account is kept but
refused.
- [**email_verified**](#cmem_client.models.user.User.email_verified) (<code>bool</code>) – Whether the mail address was confirmed by the account holder.

**Functions:**

- [**get_id**](#cmem_client.models.user.User.get_id) – Get the username as the unique identifier.

### `email` {#cmem_client.models.user.User.email}

```python
email: str = ''
```

### `email_verified` {#cmem_client.models.user.User.email_verified}

```python
email_verified: bool = Field(alias='emailVerified', default=False)
```

### `enabled` {#cmem_client.models.user.User.enabled}

```python
enabled: bool = True
```

### `first_name` {#cmem_client.models.user.User.first_name}

```python
first_name: str = Field(alias='firstName', default='')
```

### `get_id` {#cmem_client.models.user.User.get_id}

```python
get_id()
```

Get the username as the unique identifier.

### `id` {#cmem_client.models.user.User.id}

```python
id: str = ''
```

### `last_name` {#cmem_client.models.user.User.last_name}

```python
last_name: str = Field(alias='lastName', default='')
```

### `model_config` {#cmem_client.models.user.User.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `username` {#cmem_client.models.user.User.username}

```python
username: str
```

