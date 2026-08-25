---
title: "status"
tags:
  - API
  - Python
  - cmem-client
---

# `status` {#cmem_client.models.status}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Models for Corporate Memory aggregated status information.

Aggregates version and health metadata across the build (DataIntegration),
explore (DataPlatform), shapes catalog, and graph store components.

**Classes:**

- [**CmemLicense**](#cmem_client.models.status.CmemLicense) – Corporate Memory license metadata from the DataPlatform info payload.
- [**ComponentStatus**](#cmem_client.models.status.ComponentStatus) – Version and health of a single Corporate Memory component.
- [**ExploreStatus**](#cmem_client.models.status.ExploreStatus) – Status of the explore (DataPlatform) component, including raw actuator payload.
- [**HealthState**](#cmem_client.models.status.HealthState) – Health state of a Corporate Memory component.
- [**StatusInfo**](#cmem_client.models.status.StatusInfo) – Aggregated status across all Corporate Memory components.
- [**StoreInfo**](#cmem_client.models.status.StoreInfo) – Graph store metadata embedded in the DataPlatform info payload.
- [**StoreStatus**](#cmem_client.models.status.StoreStatus) – Status of the graph store backing the DataPlatform.
- [**WorkspaceConfiguration**](#cmem_client.models.status.WorkspaceConfiguration) – Workspace configuration metadata from the DataPlatform info payload.

**Attributes:**

- [**SHAPES_CATALOG_VERSION_QUERY**](#cmem_client.models.status.SHAPES_CATALOG_VERSION_QUERY) – SPARQL query used to read the shapes catalog version from the explore store.

## `CmemLicense` {#cmem_client.models.status.CmemLicense}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Corporate Memory license metadata from the DataPlatform info payload.

**Attributes:**

- [**edition**](#cmem_client.models.status.CmemLicense.edition) (<code>str | None</code>) – License edition (e.g. 'PEDAL').
- [**grace_date**](#cmem_client.models.status.CmemLicense.grace_date) (<code>str | None</code>) – Date until which the license keeps working in grace period (ISO date string).
- [**in_grace_period**](#cmem_client.models.status.CmemLicense.in_grace_period) (<code>bool</code>) – Whether the CMEM license is currently within its grace period.
- [**model_config**](#cmem_client.models.status.CmemLicense.model_config) –
- [**valid_date**](#cmem_client.models.status.CmemLicense.valid_date) (<code>str | None</code>) – Date until which the license is valid (ISO date string).

### `edition` {#cmem_client.models.status.CmemLicense.edition}

```python
edition: str | None = None
```

License edition (e.g. 'PEDAL').

### `grace_date` {#cmem_client.models.status.CmemLicense.grace_date}

```python
grace_date: str | None = Field(default=None, alias='graceDate')
```

Date until which the license keeps working in grace period (ISO date string).

### `in_grace_period` {#cmem_client.models.status.CmemLicense.in_grace_period}

```python
in_grace_period: bool = Field(default=False, alias='inGracePeriod')
```

Whether the CMEM license is currently within its grace period.

### `model_config` {#cmem_client.models.status.CmemLicense.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `valid_date` {#cmem_client.models.status.CmemLicense.valid_date}

```python
valid_date: str | None = Field(default=None, alias='validDate')
```

Date until which the license is valid (ISO date string).

## `ComponentStatus` {#cmem_client.models.status.ComponentStatus}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Version and health of a single Corporate Memory component.

**Attributes:**

- [**error**](#cmem_client.models.status.ComponentStatus.error) (<code>str | None</code>) – Captured error message if status retrieval failed; None otherwise.
- [**health**](#cmem_client.models.status.ComponentStatus.health) (<code>[HealthState](#cmem_client.models.status.HealthState)</code>) – Health state of the component.
- [**model_config**](#cmem_client.models.status.ComponentStatus.model_config) –
- [**version**](#cmem_client.models.status.ComponentStatus.version) (<code>str</code>) – Component version string as reported by its version/info endpoint.

### `error` {#cmem_client.models.status.ComponentStatus.error}

```python
error: str | None = None
```

Captured error message if status retrieval failed; None otherwise.

### `health` {#cmem_client.models.status.ComponentStatus.health}

```python
health: HealthState = HealthState.UNKNOWN
```

Health state of the component.

### `model_config` {#cmem_client.models.status.ComponentStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `version` {#cmem_client.models.status.ComponentStatus.version}

```python
version: str = 'UNKNOWN'
```

Component version string as reported by its version/info endpoint.

## `ExploreStatus` {#cmem_client.models.status.ExploreStatus}

Bases: <code>[ComponentStatus](#cmem_client.models.status.ComponentStatus)</code>

Status of the explore (DataPlatform) component, including raw actuator payload.

**Attributes:**

- [**error**](#cmem_client.models.status.ExploreStatus.error) (<code>str | None</code>) – Captured error message if status retrieval failed; None otherwise.
- [**health**](#cmem_client.models.status.ExploreStatus.health) (<code>[HealthState](#cmem_client.models.status.HealthState)</code>) – Health state of the component.
- [**health_details**](#cmem_client.models.status.ExploreStatus.health_details) (<code>dict[str, Any] | None</code>) – Raw payload of the DataPlatform /actuator/health endpoint (component breakdown).
- [**info**](#cmem_client.models.status.ExploreStatus.info) (<code>dict[str, Any] | None</code>) – Raw payload of the DataPlatform /actuator/info endpoint.
- [**license**](#cmem_client.models.status.ExploreStatus.license) (<code>[CmemLicense](#cmem_client.models.status.CmemLicense) | None</code>) – Typed CMEM license info, or None if not reported (DataPlatform < 24.1).
- [**model_config**](#cmem_client.models.status.ExploreStatus.model_config) –
- [**store_info**](#cmem_client.models.status.ExploreStatus.store_info) (<code>[StoreInfo](#cmem_client.models.status.StoreInfo) | None</code>) – Typed graph store info from the actuator payload, or None if absent.
- [**version**](#cmem_client.models.status.ExploreStatus.version) (<code>str</code>) – Component version string as reported by its version/info endpoint.
- [**workspace_configuration**](#cmem_client.models.status.ExploreStatus.workspace_configuration) (<code>[WorkspaceConfiguration](#cmem_client.models.status.WorkspaceConfiguration) | None</code>) – Typed workspace configuration info, or None if absent.
- [**workspaces_to_migrate**](#cmem_client.models.status.ExploreStatus.workspaces_to_migrate) (<code>list[Any]</code>) – Workspace IDs flagged by the DataPlatform as requiring configuration migration.

### `error` {#cmem_client.models.status.ExploreStatus.error}

```python
error: str | None = None
```

Captured error message if status retrieval failed; None otherwise.

### `health` {#cmem_client.models.status.ExploreStatus.health}

```python
health: HealthState = HealthState.UNKNOWN
```

Health state of the component.

### `health_details` {#cmem_client.models.status.ExploreStatus.health_details}

```python
health_details: dict[str, Any] | None = None
```

Raw payload of the DataPlatform /actuator/health endpoint (component breakdown).

### `info` {#cmem_client.models.status.ExploreStatus.info}

```python
info: dict[str, Any] | None = None
```

Raw payload of the DataPlatform /actuator/info endpoint.

### `license` {#cmem_client.models.status.ExploreStatus.license}

```python
license: CmemLicense | None
```

Typed CMEM license info, or None if not reported (DataPlatform < 24.1).

### `model_config` {#cmem_client.models.status.ExploreStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `store_info` {#cmem_client.models.status.ExploreStatus.store_info}

```python
store_info: StoreInfo | None
```

Typed graph store info from the actuator payload, or None if absent.

### `version` {#cmem_client.models.status.ExploreStatus.version}

```python
version: str = 'UNKNOWN'
```

Component version string as reported by its version/info endpoint.

### `workspace_configuration` {#cmem_client.models.status.ExploreStatus.workspace_configuration}

```python
workspace_configuration: WorkspaceConfiguration | None
```

Typed workspace configuration info, or None if absent.

### `workspaces_to_migrate` {#cmem_client.models.status.ExploreStatus.workspaces_to_migrate}

```python
workspaces_to_migrate: list[Any]
```

Workspace IDs flagged by the DataPlatform as requiring configuration migration.

## `HealthState` {#cmem_client.models.status.HealthState}

Bases: <code>StrEnum</code>

Health state of a Corporate Memory component.

**Functions:**

- [**parse**](#cmem_client.models.status.HealthState.parse) – Map a raw health string to a HealthState.

**Attributes:**

- [**DOWN**](#cmem_client.models.status.HealthState.DOWN) –
- [**UNKNOWN**](#cmem_client.models.status.HealthState.UNKNOWN) –
- [**UP**](#cmem_client.models.status.HealthState.UP) –

### `DOWN` {#cmem_client.models.status.HealthState.DOWN}

```python
DOWN = 'DOWN'
```

### `UNKNOWN` {#cmem_client.models.status.HealthState.UNKNOWN}

```python
UNKNOWN = 'UNKNOWN'
```

### `UP` {#cmem_client.models.status.HealthState.UP}

```python
UP = 'UP'
```

### `parse` {#cmem_client.models.status.HealthState.parse}

```python
parse(value)
```

Map a raw health string to a HealthState.

Treats only the literal "UP" as up; any other non-empty value is
considered DOWN. Missing/empty values become UNKNOWN.

**Returns:**

- <code>[HealthState](#cmem_client.models.status.HealthState)</code> – The matching HealthState.

## `SHAPES_CATALOG_VERSION_QUERY` {#cmem_client.models.status.SHAPES_CATALOG_VERSION_QUERY}

```python
SHAPES_CATALOG_VERSION_QUERY = 'PREFIX owl: <http://www.w3.org/2002/07/owl#>\nPREFIX : <https://vocab.eccenca.com/shacl/>\nSELECT ?version\nFROM :\nWHERE {\n  : owl:versionInfo ?version\n}\nORDER BY ASC(?version)\n'
```

SPARQL query used to read the shapes catalog version from the explore store.

## `StatusInfo` {#cmem_client.models.status.StatusInfo}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Aggregated status across all Corporate Memory components.

**Functions:**

- [**to_summary_dict**](#cmem_client.models.status.StatusInfo.to_summary_dict) – Render the documented `admin status` output contract as a plain dict.

**Attributes:**

- [**build**](#cmem_client.models.status.StatusInfo.build) (<code>[ComponentStatus](#cmem_client.models.status.ComponentStatus)</code>) – Status of the build (DataIntegration) component.
- [**explore**](#cmem_client.models.status.StatusInfo.explore) (<code>[ExploreStatus](#cmem_client.models.status.ExploreStatus)</code>) – Status of the explore (DataPlatform) component.
- [**health**](#cmem_client.models.status.StatusInfo.health) (<code>[HealthState](#cmem_client.models.status.HealthState)</code>) – Overall health: UP only if every component is UP, DOWN otherwise.
- [**model_config**](#cmem_client.models.status.StatusInfo.model_config) –
- [**shapes**](#cmem_client.models.status.StatusInfo.shapes) (<code>[ComponentStatus](#cmem_client.models.status.ComponentStatus)</code>) – Status of the shapes catalog (queried from the explore store).
- [**store**](#cmem_client.models.status.StatusInfo.store) (<code>[StoreStatus](#cmem_client.models.status.StoreStatus)</code>) – Status of the graph store backing the DataPlatform.

### `build` {#cmem_client.models.status.StatusInfo.build}

```python
build: ComponentStatus = Field(default_factory=ComponentStatus)
```

Status of the build (DataIntegration) component.

### `explore` {#cmem_client.models.status.StatusInfo.explore}

```python
explore: ExploreStatus = Field(default_factory=ExploreStatus)
```

Status of the explore (DataPlatform) component.

### `health` {#cmem_client.models.status.StatusInfo.health}

```python
health: HealthState
```

Overall health: UP only if every component is UP, DOWN otherwise.

### `model_config` {#cmem_client.models.status.StatusInfo.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `shapes` {#cmem_client.models.status.StatusInfo.shapes}

```python
shapes: ComponentStatus = Field(default_factory=ComponentStatus)
```

Status of the shapes catalog (queried from the explore store).

### `store` {#cmem_client.models.status.StatusInfo.store}

```python
store: StoreStatus = Field(default_factory=StoreStatus)
```

Status of the graph store backing the DataPlatform.

### `to_summary_dict` {#cmem_client.models.status.StatusInfo.to_summary_dict}

```python
to_summary_dict()
```

Render the documented `admin status` output contract as a plain dict.

Reproduces the structure historically consumed by cmemc's `admin status`
command (`--raw`, `--key`, `overall.healthy`) and its shell completion of
status keys, sourced from this typed status model.

**Returns:**

- <code>dict</code> – A dict with a ``build``, ``explore``, ``shapes``, ``store`` and ``overall``
- <code>dict</code> – key, each holding the version and health of that component where available.

## `StoreInfo` {#cmem_client.models.status.StoreInfo}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Graph store metadata embedded in the DataPlatform info payload.

**Attributes:**

- [**license_expiration**](#cmem_client.models.status.StoreInfo.license_expiration) (<code>str | None</code>) – Graph store license expiration date (ISO date string), if reported.
- [**model_config**](#cmem_client.models.status.StoreInfo.model_config) –
- [**type**](#cmem_client.models.status.StoreInfo.type) (<code>str</code>) – Store implementation (e.g. 'GRAPHDB', 'TENTRIS').
- [**version**](#cmem_client.models.status.StoreInfo.version) (<code>str</code>) – Store version string.

### `license_expiration` {#cmem_client.models.status.StoreInfo.license_expiration}

```python
license_expiration: str | None = Field(default=None, alias='licenseExpiration')
```

Graph store license expiration date (ISO date string), if reported.

### `model_config` {#cmem_client.models.status.StoreInfo.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `type` {#cmem_client.models.status.StoreInfo.type}

```python
type: str = 'STORE'
```

Store implementation (e.g. 'GRAPHDB', 'TENTRIS').

### `version` {#cmem_client.models.status.StoreInfo.version}

```python
version: str = 'UNKNOWN'
```

Store version string.

## `StoreStatus` {#cmem_client.models.status.StoreStatus}

Bases: <code>[ComponentStatus](#cmem_client.models.status.ComponentStatus)</code>

Status of the graph store backing the DataPlatform.

**Attributes:**

- [**error**](#cmem_client.models.status.StoreStatus.error) (<code>str | None</code>) – Captured error message if status retrieval failed; None otherwise.
- [**health**](#cmem_client.models.status.StoreStatus.health) (<code>[HealthState](#cmem_client.models.status.HealthState)</code>) – Health state of the component.
- [**model_config**](#cmem_client.models.status.StoreStatus.model_config) –
- [**type**](#cmem_client.models.status.StoreStatus.type) (<code>str</code>) – Store implementation (e.g. 'GRAPHDB', 'TENTRIS').
- [**version**](#cmem_client.models.status.StoreStatus.version) (<code>str</code>) – Component version string as reported by its version/info endpoint.

### `error` {#cmem_client.models.status.StoreStatus.error}

```python
error: str | None = None
```

Captured error message if status retrieval failed; None otherwise.

### `health` {#cmem_client.models.status.StoreStatus.health}

```python
health: HealthState = HealthState.UNKNOWN
```

Health state of the component.

### `model_config` {#cmem_client.models.status.StoreStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `type` {#cmem_client.models.status.StoreStatus.type}

```python
type: str = 'STORE'
```

Store implementation (e.g. 'GRAPHDB', 'TENTRIS').

### `version` {#cmem_client.models.status.StoreStatus.version}

```python
version: str = 'UNKNOWN'
```

Component version string as reported by its version/info endpoint.

## `WorkspaceConfiguration` {#cmem_client.models.status.WorkspaceConfiguration}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Workspace configuration metadata from the DataPlatform info payload.

**Attributes:**

- [**model_config**](#cmem_client.models.status.WorkspaceConfiguration.model_config) –
- [**version**](#cmem_client.models.status.WorkspaceConfiguration.version) (<code>int | None</code>) – Workspace configuration version.
- [**workspaces_to_migrate**](#cmem_client.models.status.WorkspaceConfiguration.workspaces_to_migrate) (<code>list[Any]</code>) – Workspaces flagged as requiring configuration migration.

### `model_config` {#cmem_client.models.status.WorkspaceConfiguration.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `version` {#cmem_client.models.status.WorkspaceConfiguration.version}

```python
version: int | None = None
```

Workspace configuration version.

### `workspaces_to_migrate` {#cmem_client.models.status.WorkspaceConfiguration.workspaces_to_migrate}

```python
workspaces_to_migrate: list[Any] = Field(default_factory=list, alias='workspacesToMigrate')
```

Workspaces flagged as requiring configuration migration.

The DataPlatform reports each entry as an object (e.g. with iri/label/version);
the items are kept untyped because they are only used to detect whether a
migration is pending.

