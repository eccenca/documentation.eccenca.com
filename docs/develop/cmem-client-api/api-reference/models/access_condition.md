---
title: "cmem-client: access_condition module"
tags:
  - API
  - Python
  - cmem-client
---

# `access_condition` {#cmem_client.models.access_condition}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Access control and authorization models for Corporate Memory.

This module defines models for managing access conditions in Corporate Memory,
which control user and group permissions for graphs, actions, and other resources.
Access conditions form the foundation of Corporate Memory's authorization system.

The AccessCondition model supports both static permissions (defined at creation)
and dynamic permissions (computed via SPARQL queries), providing flexible
access control patterns for different organizational needs.

Access conditions can grant various permissions including graph read/write access,
action execution rights, and management permissions for other access conditions.

**Classes:**

- [**AccessCondition**](#cmem_client.models.access_condition.AccessCondition) – An access condition
- [**AccessConditionResultSet**](#cmem_client.models.access_condition.AccessConditionResultSet) – An access condition result set
- [**AccessConditionReview**](#cmem_client.models.access_condition.AccessConditionReview) – Review of access rights for a given account.
- [**AccessControlConfiguration**](#cmem_client.models.access_condition.AccessControlConfiguration) – An access condition configuration
- [**AclAction**](#cmem_client.models.access_condition.AclAction) – An action that can be granted by an access condition.
- [**MatchingAccessCondition**](#cmem_client.models.access_condition.MatchingAccessCondition) – A single access condition that matched during a review.

**Attributes:**

- [**NS_AC**](#cmem_client.models.access_condition.NS_AC) –
- [**NS_ACTION**](#cmem_client.models.access_condition.NS_ACTION) –

## `AccessCondition` {#cmem_client.models.access_condition.AccessCondition}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

An access condition

A condition names who it applies to (``requires_account``, ``requires_group``) and
what they may then do (the grants below). A condition without a ``requires_*`` field
applies to everyone. The grants of all matching conditions add up, so access is
widened by adding a condition and never narrowed.

**Attributes:**

- [**iri**](#cmem_client.models.access_condition.AccessCondition.iri) (<code>str</code>) – IRI of the access condition, e.g.
``http://eccenca.com/ac/my-condition``. This is the key of the repository,
and it has to start with that namespace.
- [**name**](#cmem_client.models.access_condition.AccessCondition.name) (<code>str</code>) – Short name identifying the condition, e.g. ``My Access Condition``.
- [**comment**](#cmem_client.models.access_condition.AccessCondition.comment) (<code>str | None</code>) – Longer description of what the condition is for.
- [**requires_account**](#cmem_client.models.access_condition.AccessCondition.requires_account) (<code>str | None</code>) – IRI of the single account the condition applies to, e.g.
``http://eccenca.com/admin``.
- [**requires_group**](#cmem_client.models.access_condition.AccessCondition.requires_group) (<code>list[str]</code>) – IRIs of the groups an account has to be a member of for the
condition to apply, e.g. ``http://eccenca.com/elds-admins``.
- [**readable_graphs**](#cmem_client.models.access_condition.AccessCondition.readable_graphs) (<code>list[str]</code>) – IRIs of the graphs this grants read access to. The special
``https://vocab.eccenca.com/auth/AllGraphs`` covers every graph.
- [**writable_graphs**](#cmem_client.models.access_condition.AccessCondition.writable_graphs) (<code>list[str]</code>) – IRIs of the graphs this grants read and write access to.
- [**allowed_actions**](#cmem_client.models.access_condition.AccessCondition.allowed_actions) (<code>list[str]</code>) – IRIs of the actions this grants permission to execute, e.g.
``https://vocab.eccenca.com/auth/Action/Build``. The special
``.../Action/AllActions`` covers every action.
- [**grant_allowed_actions**](#cmem_client.models.access_condition.AccessCondition.grant_allowed_actions) (<code>list[str]</code>) – Patterns of actions whose granting conditions the holder
may manage, e.g. ``https://vocab.eccenca.com/auth/Action/Build*`` or ``*``.
This delegates administration rather than granting the action itself.
- [**grant_read_patterns**](#cmem_client.models.access_condition.AccessCondition.grant_read_patterns) (<code>list[str]</code>) – Patterns of graphs whose read-granting conditions the
holder may manage, e.g. ``https://example.org/*``.
- [**grant_write_patterns**](#cmem_client.models.access_condition.AccessCondition.grant_write_patterns) (<code>list[str]</code>) – Patterns of graphs whose write-granting conditions the
holder may manage.
- [**query**](#cmem_client.models.access_condition.AccessCondition.query) (<code>str | None</code>) – SPARQL SELECT query computing the grants instead of listing them, which
is what makes a condition dynamic. It has to project the variables ``user``,
``group``, ``readGraph`` and ``writeGraph``.
- [**creator**](#cmem_client.models.access_condition.AccessCondition.creator) (<code>str | None</code>) – IRI of the account which created the condition. Read-only, so it is
dropped from a create request.
- [**created**](#cmem_client.models.access_condition.AccessCondition.created) (<code>datetime | None</code>) – When the condition was created. Read-only as well.

**Functions:**

- [**get_create_request**](#cmem_client.models.access_condition.AccessCondition.get_create_request) – Create a CreateAccessConditionRequest dict
- [**get_id**](#cmem_client.models.access_condition.AccessCondition.get_id) – Get the IRI of the access condition
- [**set_iri**](#cmem_client.models.access_condition.AccessCondition.set_iri) – Set the IRI of the access condition based on a new local name

### `allowed_actions` {#cmem_client.models.access_condition.AccessCondition.allowed_actions}

```python
allowed_actions: list[str] = Field(alias='allowedActions', default=[])
```

### `comment` {#cmem_client.models.access_condition.AccessCondition.comment}

```python
comment: str | None = None
```

### `created` {#cmem_client.models.access_condition.AccessCondition.created}

```python
created: datetime | None = None
```

### `creator` {#cmem_client.models.access_condition.AccessCondition.creator}

```python
creator: str | None = None
```

### `get_create_request` {#cmem_client.models.access_condition.AccessCondition.get_create_request}

```python
get_create_request()
```

Create a CreateAccessConditionRequest dict

This object is used to create new access condition.

**Returns:**

- <code>dict</code> – The request payload, with the ``staticId`` derived from the access condition
- <code>dict</code> – IRI and the read-only keys removed.

**Raises:**

- <code>ValueError</code> – If the access condition IRI does not start with the access
condition namespace.

### `get_id` {#cmem_client.models.access_condition.AccessCondition.get_id}

```python
get_id()
```

Get the IRI of the access condition

### `grant_allowed_actions` {#cmem_client.models.access_condition.AccessCondition.grant_allowed_actions}

```python
grant_allowed_actions: list[str] = Field(alias='grantAllowedActions', default=[])
```

### `grant_read_patterns` {#cmem_client.models.access_condition.AccessCondition.grant_read_patterns}

```python
grant_read_patterns: list[str] = Field(alias='grantReadPatterns', default=[])
```

### `grant_write_patterns` {#cmem_client.models.access_condition.AccessCondition.grant_write_patterns}

```python
grant_write_patterns: list[str] = Field(alias='grantWritePatterns', default=[])
```

### `iri` {#cmem_client.models.access_condition.AccessCondition.iri}

```python
iri: str
```

### `model_config` {#cmem_client.models.access_condition.AccessCondition.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.access_condition.AccessCondition.name}

```python
name: str
```

### `query` {#cmem_client.models.access_condition.AccessCondition.query}

```python
query: str | None = Field(alias='dynamicAccessConditionQuery', default=None)
```

### `readable_graphs` {#cmem_client.models.access_condition.AccessCondition.readable_graphs}

```python
readable_graphs: list[str] = Field(alias='readableGraphs', default=[])
```

### `requires_account` {#cmem_client.models.access_condition.AccessCondition.requires_account}

```python
requires_account: str | None = Field(alias='requiresAccount', default=None)
```

### `requires_group` {#cmem_client.models.access_condition.AccessCondition.requires_group}

```python
requires_group: list[str] = Field(alias='requiresGroup', default=[])
```

### `set_iri` {#cmem_client.models.access_condition.AccessCondition.set_iri}

```python
set_iri(local_name)
```

Set the IRI of the access condition based on a new local name

this just adds the namespace prefix

### `writable_graphs` {#cmem_client.models.access_condition.AccessCondition.writable_graphs}

```python
writable_graphs: list[str] = Field(alias='writableGraphs', default=[])
```

## `AccessConditionResultSet` {#cmem_client.models.access_condition.AccessConditionResultSet}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

An access condition result set

**Attributes:**

- [**content**](#cmem_client.models.access_condition.AccessConditionResultSet.content) (<code>list[[AccessCondition](#cmem_client.models.access_condition.AccessCondition)]</code>) – The access conditions on this page.
- [**page**](#cmem_client.models.access_condition.AccessConditionResultSet.page) (<code>[PageDescription](../repositories/base/paged_list.md#cmem_client.repositories.base.paged_list.PageDescription)</code>) – Which page this is and how many there are in total.

### `content` {#cmem_client.models.access_condition.AccessConditionResultSet.content}

```python
content: list[AccessCondition]
```

### `model_config` {#cmem_client.models.access_condition.AccessConditionResultSet.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `page` {#cmem_client.models.access_condition.AccessConditionResultSet.page}

```python
page: PageDescription
```

## `AccessConditionReview` {#cmem_client.models.access_condition.AccessConditionReview}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Review of access rights for a given account.

A review answers what an account may actually do, after every condition which
applies to it has been evaluated and their grants added up.

**Attributes:**

- [**principal_name**](#cmem_client.models.access_condition.AccessConditionReview.principal_name) (<code>str</code>) – Name of the reviewed account.
- [**account_iri**](#cmem_client.models.access_condition.AccessConditionReview.account_iri) (<code>str</code>) – IRI of the reviewed account.
- [**has_root_access**](#cmem_client.models.access_condition.AccessConditionReview.has_root_access) (<code>bool</code>) – Whether the account bypasses access control entirely.
- [**can_read_all**](#cmem_client.models.access_condition.AccessConditionReview.can_read_all) (<code>bool</code>) – Whether the account may read every graph, which makes
``readable_graphs`` beside the point.
- [**can_write_all**](#cmem_client.models.access_condition.AccessConditionReview.can_write_all) (<code>bool</code>) – Whether the account may write every graph.
- [**are_all_actions_allowed**](#cmem_client.models.access_condition.AccessConditionReview.are_all_actions_allowed) (<code>bool</code>) – Whether the account may execute every action.
- [**readable_graphs**](#cmem_client.models.access_condition.AccessConditionReview.readable_graphs) (<code>list[str]</code>) – IRIs of the graphs the account may read.
- [**writable_graphs**](#cmem_client.models.access_condition.AccessConditionReview.writable_graphs) (<code>list[str]</code>) – IRIs of the graphs the account may write.
- [**allowed_actions**](#cmem_client.models.access_condition.AccessConditionReview.allowed_actions) (<code>list[str]</code>) – IRIs of the actions the account may execute.
- [**read_graph_grants**](#cmem_client.models.access_condition.AccessConditionReview.read_graph_grants) (<code>list[str]</code>) – Graph patterns whose read-granting conditions the account
may manage.
- [**write_graph_grants**](#cmem_client.models.access_condition.AccessConditionReview.write_graph_grants) (<code>list[str]</code>) – Graph patterns whose write-granting conditions it may
manage.
- [**matching_access_conditions**](#cmem_client.models.access_condition.AccessConditionReview.matching_access_conditions) (<code>list[[MatchingAccessCondition](#cmem_client.models.access_condition.MatchingAccessCondition)]</code>) – The conditions which produced this result, with the
grants each one contributed. Use it to find out why an account has an
access it should not have.
- [**validity_time_stamp**](#cmem_client.models.access_condition.AccessConditionReview.validity_time_stamp) (<code>datetime</code>) – When the review was computed. A dynamic condition can
change its outcome afterwards.
- [**group_iri**](#cmem_client.models.access_condition.AccessConditionReview.group_iri) (<code>list[str] | None</code>) – IRIs of the groups the account belongs to.

### `account_iri` {#cmem_client.models.access_condition.AccessConditionReview.account_iri}

```python
account_iri: str = Field(alias='accountIri')
```

### `allowed_actions` {#cmem_client.models.access_condition.AccessConditionReview.allowed_actions}

```python
allowed_actions: list[str] = Field(alias='allowedActions', default=[])
```

### `are_all_actions_allowed` {#cmem_client.models.access_condition.AccessConditionReview.are_all_actions_allowed}

```python
are_all_actions_allowed: bool = Field(alias='areAllActionsAllowed')
```

### `can_read_all` {#cmem_client.models.access_condition.AccessConditionReview.can_read_all}

```python
can_read_all: bool = Field(alias='canReadAll')
```

### `can_write_all` {#cmem_client.models.access_condition.AccessConditionReview.can_write_all}

```python
can_write_all: bool = Field(alias='canWriteAll')
```

### `group_iri` {#cmem_client.models.access_condition.AccessConditionReview.group_iri}

```python
group_iri: list[str] | None = Field(alias='groupIri', default=None)
```

### `has_root_access` {#cmem_client.models.access_condition.AccessConditionReview.has_root_access}

```python
has_root_access: bool = Field(alias='hasRootAccess')
```

### `matching_access_conditions` {#cmem_client.models.access_condition.AccessConditionReview.matching_access_conditions}

```python
matching_access_conditions: list[MatchingAccessCondition] = Field(alias='matchingAccessConditions', default=[])
```

### `model_config` {#cmem_client.models.access_condition.AccessConditionReview.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `principal_name` {#cmem_client.models.access_condition.AccessConditionReview.principal_name}

```python
principal_name: str = Field(alias='principalName')
```

### `read_graph_grants` {#cmem_client.models.access_condition.AccessConditionReview.read_graph_grants}

```python
read_graph_grants: list[str] = Field(alias='readGraphGrants', default=[])
```

### `readable_graphs` {#cmem_client.models.access_condition.AccessConditionReview.readable_graphs}

```python
readable_graphs: list[str] = Field(alias='readableGraphs', default=[])
```

### `validity_time_stamp` {#cmem_client.models.access_condition.AccessConditionReview.validity_time_stamp}

```python
validity_time_stamp: datetime = Field(alias='validityTimeStamp')
```

### `writable_graphs` {#cmem_client.models.access_condition.AccessConditionReview.writable_graphs}

```python
writable_graphs: list[str] = Field(alias='writableGraphs', default=[])
```

### `write_graph_grants` {#cmem_client.models.access_condition.AccessConditionReview.write_graph_grants}

```python
write_graph_grants: list[str] = Field(alias='writeGraphGrants', default=[])
```

## `AccessControlConfiguration` {#cmem_client.models.access_condition.AccessControlConfiguration}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

An access condition configuration

**Attributes:**

- [**enabled**](#cmem_client.models.access_condition.AccessControlConfiguration.enabled) (<code>bool</code>) – Whether access control is switched on for the deployment. With it off,
the conditions are kept but not enforced.
- [**admin_action**](#cmem_client.models.access_condition.AccessControlConfiguration.admin_action) (<code>str | None</code>) – IRI of the action which grants administration of access
conditions.

### `admin_action` {#cmem_client.models.access_condition.AccessControlConfiguration.admin_action}

```python
admin_action: str | None = Field(alias='adminAction', default=None)
```

### `enabled` {#cmem_client.models.access_condition.AccessControlConfiguration.enabled}

```python
enabled: bool = Field(default=False)
```

### `model_config` {#cmem_client.models.access_condition.AccessControlConfiguration.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `AclAction` {#cmem_client.models.access_condition.AclAction}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

An action that can be granted by an access condition.

**Attributes:**

- [**iri**](#cmem_client.models.access_condition.AclAction.iri) (<code>str</code>) – IRI of the action, as used in ``AccessCondition.allowed_actions``.
- [**name**](#cmem_client.models.access_condition.AclAction.name) (<code>str</code>) – Short name of the action.

### `iri` {#cmem_client.models.access_condition.AclAction.iri}

```python
iri: str
```

### `model_config` {#cmem_client.models.access_condition.AclAction.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `name` {#cmem_client.models.access_condition.AclAction.name}

```python
name: str
```

## `MatchingAccessCondition` {#cmem_client.models.access_condition.MatchingAccessCondition}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A single access condition that matched during a review.

**Attributes:**

- [**access_condition_iri**](#cmem_client.models.access_condition.MatchingAccessCondition.access_condition_iri) (<code>str</code>) – IRI of the condition which matched.
- [**read_graph_grants**](#cmem_client.models.access_condition.MatchingAccessCondition.read_graph_grants) (<code>list[str]</code>) – Graph IRIs this condition contributed read access to.
- [**write_graph_grants**](#cmem_client.models.access_condition.MatchingAccessCondition.write_graph_grants) (<code>list[str]</code>) – Graph IRIs this condition contributed write access to.

### `access_condition_iri` {#cmem_client.models.access_condition.MatchingAccessCondition.access_condition_iri}

```python
access_condition_iri: str = Field(alias='accessConditionIri')
```

### `model_config` {#cmem_client.models.access_condition.MatchingAccessCondition.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `read_graph_grants` {#cmem_client.models.access_condition.MatchingAccessCondition.read_graph_grants}

```python
read_graph_grants: list[str] = Field(alias='readGraphGrants', default=[])
```

### `write_graph_grants` {#cmem_client.models.access_condition.MatchingAccessCondition.write_graph_grants}

```python
write_graph_grants: list[str] = Field(alias='writeGraphGrants', default=[])
```

## `NS_AC` {#cmem_client.models.access_condition.NS_AC}

```python
NS_AC = 'http://eccenca.com/ac/'
```

## `NS_ACTION` {#cmem_client.models.access_condition.NS_ACTION}

```python
NS_ACTION = 'https://vocab.eccenca.com/auth/Action/'
```

