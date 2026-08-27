---
title: "cmem-client: user_accounts module"
description: "Repository for the Keycloak user accounts of a Corporate Memory deployment."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.user_accounts` {#cmem_client.repositories.user_accounts}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the Keycloak user accounts of a Corporate Memory deployment.

Provides UserAccountRepository for creating, updating and deleting user accounts, for
managing their group membership and for resetting their password. Accounts are keyed by
their username, while the group operations take the internal Keycloak account ID.

**Examples:**

List the accounts and read one of them:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> list(client.user_accounts)
>>> account = client.user_accounts["admin"]
```

Inspect the groups of the deployment and of a single account. Note that the group
operations expect the internal account ID, not the username:

```pycon
>>> [group.name for group in client.user_accounts.list_groups()]
>>> [group.name for group in client.user_accounts.get_user_groups(account.id)]
```

``reset_password()`` sets a new password for an account and
``request_password_change()`` makes the account choose one at its next login. Both
are described rather than shown running, because they change a credential which is
in use, and unlike the workspace and the store, Keycloak is not restored afterwards.

**Classes:**

- [**UserAccountCreateConfig**](#cmem_client.repositories.user_accounts.UserAccountCreateConfig) – User account creation configuration.
- [**UserAccountDeleteConfig**](#cmem_client.repositories.user_accounts.UserAccountDeleteConfig) – User account deletion configuration.
- [**UserAccountRepository**](#cmem_client.repositories.user_accounts.UserAccountRepository) – Repository for Keycloak user accounts.
- [**UserAccountUpdateConfig**](#cmem_client.repositories.user_accounts.UserAccountUpdateConfig) – User account update configuration.

## `UserAccountCreateConfig` {#cmem_client.repositories.user_accounts.UserAccountCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

User account creation configuration.

**Attributes:**

- **model_config** –

## `UserAccountDeleteConfig` {#cmem_client.repositories.user_accounts.UserAccountDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

User account deletion configuration.

**Attributes:**

- **model_config** –

## `UserAccountRepository` {#cmem_client.repositories.user_accounts.UserAccountRepository}

Bases: <code>[PlainListRepository](../repositories/base/plain_list.md#cmem_client.repositories.base.plain_list.PlainListRepository)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for Keycloak user accounts.

Provides access to user accounts in the Corporate Memory Keycloak realm.
Users are identified by their username and stored in a dictionary keyed by
username.

In addition to standard CRUD operations, this repository provides methods
for group assignment, group listing, and password management.

**Functions:**

- [**assign_group**](#cmem_client.repositories.user_accounts.UserAccountRepository.assign_group) – Assign a group to a user.
- [**create_item**](#cmem_client.repositories.user_accounts.UserAccountRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.user_accounts.UserAccountRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.user_accounts.UserAccountRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.user_accounts.UserAccountRepository.fetch_data) – Fetch simple list from a JSON endpoint via a type adapter
- [**get_user_groups**](#cmem_client.repositories.user_accounts.UserAccountRepository.get_user_groups) – Get groups assigned to a user.
- [**items**](#cmem_client.repositories.user_accounts.UserAccountRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.user_accounts.UserAccountRepository.keys) – Get the keys of the repository
- [**list_groups**](#cmem_client.repositories.user_accounts.UserAccountRepository.list_groups) – List all groups in the Keycloak realm.
- [**raise_modification_error**](#cmem_client.repositories.user_accounts.UserAccountRepository.raise_modification_error) – Raise an exception if needed
- [**request_password_change**](#cmem_client.repositories.user_accounts.UserAccountRepository.request_password_change) – Send a password-change request email to a user.
- [**reset_password**](#cmem_client.repositories.user_accounts.UserAccountRepository.reset_password) – Reset the password for a user.
- [**unassign_group**](#cmem_client.repositories.user_accounts.UserAccountRepository.unassign_group) – Remove a group from a user.
- [**update_item**](#cmem_client.repositories.user_accounts.UserAccountRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.user_accounts.UserAccountRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.user_accounts.UserAccountRepository.logger) (<code>Logger</code>) – Gets the client logger

### `assign_group` {#cmem_client.repositories.user_accounts.UserAccountRepository.assign_group}

```python
assign_group(user_id, group_id)
```

Assign a group to a user.

**Parameters:**

- **user_id** (<code>str</code>) – The Keycloak UUID of the user.
- **group_id** (<code>str</code>) – The Keycloak UUID of the group.

### `create_item` {#cmem_client.repositories.user_accounts.UserAccountRepository.create_item}

```python
create_item(item, skip_if_existing=False, configuration=None)
```

Create (add) a new item to the repository

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to add to the repository
- **skip_if_existing** (<code>bool</code>) – If true, creating already existing items will be ignored
- **configuration** (<code>[CreateItemConfig_contra](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemConfig_contra) | None</code>) – Optional configuration

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `delete_all` {#cmem_client.repositories.user_accounts.UserAccountRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.user_accounts.UserAccountRepository.delete_item}

```python
delete_item(key, skip_if_missing=False, configuration=None)
```

Delete an item from the repository

**Parameters:**

- **key** (<code>str</code>) – The key of the item to delete
- **skip_if_missing** (<code>bool</code>) – If True, it is ignored if the deleted item even exists
- **configuration** (<code>DeleteItemConfig</code>) – Optional configuration for deletion

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – if an error occurs while creating the item
- <code>HTTPError</code> – for any other http error

### `fetch_data` {#cmem_client.repositories.user_accounts.UserAccountRepository.fetch_data}

```python
fetch_data()
```

Fetch simple list from a JSON endpoint via a type adapter

Use this method to fetch data when your result set is an array of objects.

### `get_user_groups` {#cmem_client.repositories.user_accounts.UserAccountRepository.get_user_groups}

```python
get_user_groups(user_id)
```

Get groups assigned to a user.

**Parameters:**

- **user_id** (<code>str</code>) – The Keycloak UUID of the user.

**Returns:**

- <code>list[[Group](../models/user.md#cmem_client.models.user.Group)]</code> – List of Group objects currently assigned to the user.

### `items` {#cmem_client.repositories.user_accounts.UserAccountRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.user_accounts.UserAccountRepository.keys}

```python
keys()
```

Get the keys of the repository

### `list_groups` {#cmem_client.repositories.user_accounts.UserAccountRepository.list_groups}

```python
list_groups()
```

List all groups in the Keycloak realm.

**Returns:**

- <code>list[[Group](../models/user.md#cmem_client.models.user.Group)]</code> – List of Group objects available in the realm.

### `logger` {#cmem_client.repositories.user_accounts.UserAccountRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.user_accounts.UserAccountRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `request_password_change` {#cmem_client.repositories.user_accounts.UserAccountRepository.request_password_change}

```python
request_password_change(user_id)
```

Send a password-change request email to a user.

**Parameters:**

- **user_id** (<code>str</code>) – The Keycloak UUID of the user.

### `reset_password` {#cmem_client.repositories.user_accounts.UserAccountRepository.reset_password}

```python
reset_password(user_id, value, temporary=False)
```

Reset the password for a user.

**Parameters:**

- **user_id** (<code>str</code>) – The Keycloak UUID of the user.
- **value** (<code>str</code>) – The new password value.
- **temporary** (<code>bool</code>) – If True, the user must change the password on next login.

### `unassign_group` {#cmem_client.repositories.user_accounts.UserAccountRepository.unassign_group}

```python
unassign_group(user_id, group_id)
```

Remove a group from a user.

**Parameters:**

- **user_id** (<code>str</code>) – The Keycloak UUID of the user.
- **group_id** (<code>str</code>) – The Keycloak UUID of the group.

### `update_item` {#cmem_client.repositories.user_accounts.UserAccountRepository.update_item}

```python
update_item(item, configuration=None)
```

Update an existing item in the repository.

**Parameters:**

- **item** (<code>[ItemType](../repositories/base/abc.md#cmem_client.repositories.base.abc.ItemType)</code>) – The item to update in the repository.
- **configuration** (<code>[UpdateItemConfig_contra](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemConfig_contra) | None</code>) – Optional configuration for the update operation.

**Raises:**

- <code>[RepositoryModificationError](../exceptions.md#cmem_client.exceptions.RepositoryModificationError)</code> – If the item does not exist or an error occurs.
- <code>HTTPError</code> – For any other HTTP error.

### `values` {#cmem_client.repositories.user_accounts.UserAccountRepository.values}

```python
values()
```

Get the values of the repository

## `UserAccountUpdateConfig` {#cmem_client.repositories.user_accounts.UserAccountUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

User account update configuration.

**Attributes:**

- **model_config** –

