---
title: "cmem-client: access_conditions module"
description: "Repository for the access conditions of Corporate Memory."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.repositories.access_conditions` {#cmem_client.repositories.access_conditions}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Repository for the access conditions of Corporate Memory.

Provides AccessConditionsRepository for creating, updating and deleting access
conditions, and for inspecting the accounts, groups and actions they can refer to.

**Examples:**

Inspect what access conditions can be granted to whom:

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> client.access_conditions.get_users()
>>> client.access_conditions.get_groups()
>>> for action in client.access_conditions.get_actions():
...     print(action.iri)
```

List the configured access conditions:

```pycon
>>> for iri in client.access_conditions:
...     print(iri, client.access_conditions[iri])
```

Reload the access conditions after a change:

```pycon
>>> client.access_conditions.refresh()
```

**Classes:**

- [**AccessConditionsCreateConfig**](#cmem_client.repositories.access_conditions.AccessConditionsCreateConfig) – Access condition creation config.
- [**AccessConditionsDeleteConfig**](#cmem_client.repositories.access_conditions.AccessConditionsDeleteConfig) – Access conditions delete config.
- [**AccessConditionsRepository**](#cmem_client.repositories.access_conditions.AccessConditionsRepository) – Repository for managing authorization access conditions.
- [**AccessConditionsUpdateConfig**](#cmem_client.repositories.access_conditions.AccessConditionsUpdateConfig) – Access condition update config.

## `AccessConditionsCreateConfig` {#cmem_client.repositories.access_conditions.AccessConditionsCreateConfig}

Bases: <code>[CreateConfig](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateConfig)</code>

Access condition creation config.

**Attributes:**

- **model_config** –

## `AccessConditionsDeleteConfig` {#cmem_client.repositories.access_conditions.AccessConditionsDeleteConfig}

Bases: <code>[DeleteConfig](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteConfig)</code>

Access conditions delete config.

**Attributes:**

- **model_config** –

## `AccessConditionsRepository` {#cmem_client.repositories.access_conditions.AccessConditionsRepository}

Bases: <code>[PagedListRepository](../repositories/base/paged_list.md#cmem_client.repositories.base.paged_list.PagedListRepository)</code>, <code>[DeleteItemProtocol](../repositories/protocols/delete_item.md#cmem_client.repositories.protocols.delete_item.DeleteItemProtocol)</code>, <code>[CreateItemProtocol](../repositories/protocols/create_item.md#cmem_client.repositories.protocols.create_item.CreateItemProtocol)</code>, <code>[UpdateItemProtocol](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateItemProtocol)</code>

Repository for managing authorization access conditions.

This repository manages access conditions that control authorization for resources
in Corporate Memory. Access conditions are described with the
[AccessCondition model](../models/access_condition.md#cmem_client.models.access_condition.AccessCondition).

The repository extends PagedListRepository and implements protocols for creating
and deleting access conditions.

**Functions:**

- [**create_item**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.create_item) – Create (add) a new item to the repository
- [**delete_all**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.delete_all) – Delete all items from the repository
- [**delete_item**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.delete_item) – Delete an item from the repository
- [**fetch_data**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.fetch_data) – Fetch a paged list from a JSON endpoint via a type adapter.
- [**get_actions**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_actions) – Return the list of actions that can be granted by access conditions.
- [**get_groups**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_groups) – Return the list of group IRIs known to the authorization system.
- [**get_users**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_users) – Return the list of user IRIs known to the authorization system.
- [**items**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.items) – Get the items of the repository
- [**keys**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.keys) – Get the keys of the repository
- [**raise_modification_error**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.raise_modification_error) – Raise an exception if needed
- [**refresh**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.refresh) – Refresh the DataPlatform access-condition cache.
- [**review**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.review) – Review access rights for a given account and groups.
- [**update_item**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.update_item) – Update an existing item in the repository.
- [**values**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.values) – Get the values of the repository

**Attributes:**

- [**logger**](#cmem_client.repositories.access_conditions.AccessConditionsRepository.logger) (<code>Logger</code>) – Gets the client logger

### `create_item` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.create_item}

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

### `delete_all` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.delete_all}

```python
delete_all()
```

Delete all items from the repository

### `delete_item` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.delete_item}

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

### `fetch_data` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.fetch_data}

```python
fetch_data()
```

Fetch a paged list from a JSON endpoint via a type adapter.

Use this method to fetch data if your result set is a pageable spring endpoint.

### `get_actions` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_actions}

```python
get_actions()
```

Return the list of actions that can be granted by access conditions.

### `get_groups` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_groups}

```python
get_groups()
```

Return the list of group IRIs known to the authorization system.

### `get_users` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.get_users}

```python
get_users()
```

Return the list of user IRIs known to the authorization system.

### `items` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.items}

```python
items()
```

Get the items of the repository

### `keys` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.keys}

```python
keys()
```

Get the keys of the repository

### `logger` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.logger}

```python
logger: logging.Logger
```

Gets the client logger

### `raise_modification_error` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.raise_modification_error}

```python
raise_modification_error(response)
```

Raise an exception if needed

### `refresh` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.refresh}

```python
refresh()
```

Refresh the DataPlatform access-condition cache.

Instructs the DataPlatform to reload its in-memory authorization rules
from the ACL graphs. Must be called after bulk SPARQL changes to ACL
graphs so the DataPlatform picks up the new rules without a restart.

**Raises:**

- <code>HTTPStatusError</code> – If the refresh request fails.

### `review` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.review}

```python
review(account_iri=None, group_iris=None)
```

Review access rights for a given account and groups.

**Parameters:**

- **account_iri** (<code>str | None</code>) – The IRI of the account to review.
- **group_iris** (<code>list[str] | None</code>) – Optional list of group IRIs to include in the review.

**Returns:**

- <code>[AccessConditionReview](../models/access_condition.md#cmem_client.models.access_condition.AccessConditionReview)</code> – An AccessConditionReview model containing the review results.

### `update_item` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.update_item}

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

### `values` {#cmem_client.repositories.access_conditions.AccessConditionsRepository.values}

```python
values()
```

Get the values of the repository

## `AccessConditionsUpdateConfig` {#cmem_client.repositories.access_conditions.AccessConditionsUpdateConfig}

Bases: <code>[UpdateConfig](../repositories/protocols/update_item.md#cmem_client.repositories.protocols.update_item.UpdateConfig)</code>

Access condition update config.

**Attributes:**

- **model_config** –

