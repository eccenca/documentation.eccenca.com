# `keycloak_client` {#cmem_client.models.keycloak_client}

Keycloak client models.

An OpenID Connect client is the service account a machine authenticates with. The
clients of the configured realm are the items of ``client.client_accounts``, keyed by
their ``client_id``.

**Classes:**

- [**KeycloakClient**](#cmem_client.models.keycloak_client.KeycloakClient) – A Keycloak OpenID Connect client in the Corporate Memory realm.

## `KeycloakClient` {#cmem_client.models.keycloak_client.KeycloakClient}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A Keycloak OpenID Connect client in the Corporate Memory realm.

**Attributes:**

- [**id**](#cmem_client.models.keycloak_client.KeycloakClient.id) (<code>str</code>) – Internal Keycloak identifier of the client, a UUID. Needed by the Keycloak
admin API, but not the key of the repository.
- [**client_id**](#cmem_client.models.keycloak_client.KeycloakClient.client_id) (<code>str</code>) – Client identifier used when authenticating, e.g.
``cmem-service-account``. This is the key of the repository.
- [**description**](#cmem_client.models.keycloak_client.KeycloakClient.description) (<code>str</code>) – Description of the client as maintained in Keycloak.
- [**protocol**](#cmem_client.models.keycloak_client.KeycloakClient.protocol) (<code>str</code>) – Authentication protocol of the client, e.g. ``openid-connect``.
- [**secret**](#cmem_client.models.keycloak_client.KeycloakClient.secret) (<code>str | None</code>) – Client secret, only present if the deployment returns it and the
requesting account is allowed to read it.

**Functions:**

- [**get_id**](#cmem_client.models.keycloak_client.KeycloakClient.get_id) – Get the clientId as the unique identifier.

### `client_id` {#cmem_client.models.keycloak_client.KeycloakClient.client_id}

```python
client_id: str = Field(alias='clientId')
```

### `description` {#cmem_client.models.keycloak_client.KeycloakClient.description}

```python
description: str = ''
```

### `get_id` {#cmem_client.models.keycloak_client.KeycloakClient.get_id}

```python
get_id()
```

Get the clientId as the unique identifier.

### `id` {#cmem_client.models.keycloak_client.KeycloakClient.id}

```python
id: str
```

### `model_config` {#cmem_client.models.keycloak_client.KeycloakClient.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `protocol` {#cmem_client.models.keycloak_client.KeycloakClient.protocol}

```python
protocol: str = ''
```

### `secret` {#cmem_client.models.keycloak_client.KeycloakClient.secret}

```python
secret: str | None = None
```

