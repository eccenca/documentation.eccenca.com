# `dataset` {#cmem_client.models.dataset}

Corporate Memory dataset models for data integration.

This module defines models for representing datasets within Corporate Memory
projects. Datasets are data sources or sinks used in data integration workflows,
connecting to various external systems through plugins.

The Dataset model represents the configuration and metadata of datasets within
the DataIntegration environment, including their association with projects
and the plugins that handle their data access.

**Classes:**

- [**Dataset**](#cmem_client.models.dataset.Dataset) – A Dataset Description (Build)
- [**DatasetData**](#cmem_client.models.dataset.DatasetData) – Plugin configuration as returned by the full dataset details endpoint.
- [**DatasetMetadata**](#cmem_client.models.dataset.DatasetMetadata) – Metadata for a dataset with optional label and description.
- [**DatasetPlugin**](#cmem_client.models.dataset.DatasetPlugin) – A dataset plugin description as returned by the task plugins endpoint.
- [**DatasetPluginSchema**](#cmem_client.models.dataset.DatasetPluginSchema) – Schema description of a dataset plugin as returned by the plugin schema endpoint.
- [**DatasetSearchResultSet**](#cmem_client.models.dataset.DatasetSearchResultSet) – A dataset search result set
- [**ItemLink**](#cmem_client.models.dataset.ItemLink) – An item link pointing to a workspace resource.
- [**PluginProperty**](#cmem_client.models.dataset.PluginProperty) – A single configuration property of a dataset plugin.

## `Dataset` {#cmem_client.models.dataset.Dataset}

Bases: <code>[ReadRepositoryItem](../models/base.md#cmem_client.models.base.ReadRepositoryItem)</code>

A Dataset Description (Build)

**Attributes:**

- [**id**](#cmem_client.models.dataset.Dataset.id) (<code>str</code>) – ID of the dataset, unique within its project.
- [**project_id**](#cmem_client.models.dataset.Dataset.project_id) (<code>str</code>) – ID of the project holding the dataset. Together with ``id`` it
forms the ``{project_id}:{id}`` key of the repository.
- [**tags**](#cmem_client.models.dataset.Dataset.tags) (<code>list[[Tag](../models/common.md#cmem_client.models.common.Tag)]</code>) – Tags attached to the dataset.
- [**item_links**](#cmem_client.models.dataset.Dataset.item_links) (<code>list[[ItemLink](#cmem_client.models.dataset.ItemLink)]</code>) – Links into the user interface for this dataset.
- [**data**](#cmem_client.models.dataset.Dataset.data) (<code>[DatasetData](#cmem_client.models.dataset.DatasetData)</code>) – Plugin type and parameters, which is what actually connects the dataset
to its data.
- [**metadata**](#cmem_client.models.dataset.Dataset.metadata) (<code>[DatasetMetadata](#cmem_client.models.dataset.DatasetMetadata)</code>) – Label and description of the dataset.

**Functions:**

- [**get_id**](#cmem_client.models.dataset.Dataset.get_id) – Get the ID of the dataset

### `data` {#cmem_client.models.dataset.Dataset.data}

```python
data: DatasetData = Field(default_factory=DatasetData)
```

### `get_id` {#cmem_client.models.dataset.Dataset.get_id}

```python
get_id()
```

Get the ID of the dataset

### `id` {#cmem_client.models.dataset.Dataset.id}

```python
id: str
```

### `item_links` {#cmem_client.models.dataset.Dataset.item_links}

```python
item_links: list[ItemLink] = Field(default_factory=list, alias='itemLinks')
```

### `metadata` {#cmem_client.models.dataset.Dataset.metadata}

```python
metadata: DatasetMetadata = Field(default_factory=DatasetMetadata)
```

### `model_config` {#cmem_client.models.dataset.Dataset.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_id` {#cmem_client.models.dataset.Dataset.project_id}

```python
project_id: str = Field(alias='project', default='')
```

### `tags` {#cmem_client.models.dataset.Dataset.tags}

```python
tags: list[Tag] = Field(default_factory=list)
```

## `DatasetData` {#cmem_client.models.dataset.DatasetData}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Plugin configuration as returned by the full dataset details endpoint.

**Attributes:**

- [**type**](#cmem_client.models.dataset.DatasetData.type) (<code>str</code>) – ID of the dataset plugin, e.g. ``csv`` or ``eccencaDataPlatform``. Use
``DatasetsRepository.get_dataset_plugins()`` to see which ones a deployment
offers.
- [**parameters**](#cmem_client.models.dataset.DatasetData.parameters) (<code>dict[str, Any]</code>) – Parameters of that plugin, keyed by parameter name. Which ones
apply is described by ``DatasetsRepository.get_plugin_schema()``.
- [**read_only**](#cmem_client.models.dataset.DatasetData.read_only) (<code>bool</code>) – Whether the dataset may only be read.
- [**uri_property**](#cmem_client.models.dataset.DatasetData.uri_property) (<code>str</code>) – Property holding the URI of an entity, for the dataset types
which need one.

### `model_config` {#cmem_client.models.dataset.DatasetData.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `parameters` {#cmem_client.models.dataset.DatasetData.parameters}

```python
parameters: dict[str, Any] = Field(default_factory=dict)
```

### `read_only` {#cmem_client.models.dataset.DatasetData.read_only}

```python
read_only: bool = Field(alias='readOnly', default=False)
```

### `type` {#cmem_client.models.dataset.DatasetData.type}

```python
type: str = ''
```

### `uri_property` {#cmem_client.models.dataset.DatasetData.uri_property}

```python
uri_property: str = Field(alias='uriProperty', default='')
```

## `DatasetMetadata` {#cmem_client.models.dataset.DatasetMetadata}

Bases: <code>TypedDict</code>

Metadata for a dataset with optional label and description.

**Attributes:**

- [**label**](#cmem_client.models.dataset.DatasetMetadata.label) (<code>str</code>) – Human readable name of the dataset.
- [**description**](#cmem_client.models.dataset.DatasetMetadata.description) (<code>str</code>) – Description of the dataset.

### `description` {#cmem_client.models.dataset.DatasetMetadata.description}

```python
description: str
```

### `label` {#cmem_client.models.dataset.DatasetMetadata.label}

```python
label: str
```

## `DatasetPlugin` {#cmem_client.models.dataset.DatasetPlugin}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A dataset plugin description as returned by the task plugins endpoint.

**Attributes:**

- [**title**](#cmem_client.models.dataset.DatasetPlugin.title) (<code>str</code>) – Human readable name of the plugin.
- [**description**](#cmem_client.models.dataset.DatasetPlugin.description) (<code>str</code>) – What the plugin connects to.
- [**task_type**](#cmem_client.models.dataset.DatasetPlugin.task_type) (<code>str</code>) – Kind of task the plugin builds, ``Dataset`` for these.

### `description` {#cmem_client.models.dataset.DatasetPlugin.description}

```python
description: str = ''
```

### `model_config` {#cmem_client.models.dataset.DatasetPlugin.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `task_type` {#cmem_client.models.dataset.DatasetPlugin.task_type}

```python
task_type: str = Field(alias='taskType', default='')
```

### `title` {#cmem_client.models.dataset.DatasetPlugin.title}

```python
title: str = ''
```

## `DatasetPluginSchema` {#cmem_client.models.dataset.DatasetPluginSchema}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

Schema description of a dataset plugin as returned by the plugin schema endpoint.

**Attributes:**

- [**title**](#cmem_client.models.dataset.DatasetPluginSchema.title) (<code>str</code>) – Human readable name of the plugin.
- [**description**](#cmem_client.models.dataset.DatasetPluginSchema.description) (<code>str</code>) – What the plugin connects to.
- [**properties**](#cmem_client.models.dataset.DatasetPluginSchema.properties) (<code>dict[str, [PluginProperty](#cmem_client.models.dataset.PluginProperty)]</code>) – Parameters the plugin accepts, keyed by parameter name. These are
the keys of ``DatasetData.parameters``.
- [**required**](#cmem_client.models.dataset.DatasetPluginSchema.required) (<code>list[str]</code>) – Names of the parameters which must be given.

### `description` {#cmem_client.models.dataset.DatasetPluginSchema.description}

```python
description: str = ''
```

### `model_config` {#cmem_client.models.dataset.DatasetPluginSchema.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `properties` {#cmem_client.models.dataset.DatasetPluginSchema.properties}

```python
properties: dict[str, PluginProperty] = Field(default_factory=dict)
```

### `required` {#cmem_client.models.dataset.DatasetPluginSchema.required}

```python
required: list[str] = Field(default_factory=list)
```

### `title` {#cmem_client.models.dataset.DatasetPluginSchema.title}

```python
title: str = ''
```

## `DatasetSearchResultSet` {#cmem_client.models.dataset.DatasetSearchResultSet}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A dataset search result set

**Attributes:**

- [**results**](#cmem_client.models.dataset.DatasetSearchResultSet.results) (<code>list[[Dataset](#cmem_client.models.dataset.Dataset)]</code>) – The datasets the search returned.

### `model_config` {#cmem_client.models.dataset.DatasetSearchResultSet.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `results` {#cmem_client.models.dataset.DatasetSearchResultSet.results}

```python
results: list[Dataset]
```

## `ItemLink` {#cmem_client.models.dataset.ItemLink}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

An item link pointing to a workspace resource.

**Attributes:**

- [**path**](#cmem_client.models.dataset.ItemLink.path) (<code>str</code>) – Path the link points at, relative to the DataIntegration user interface.
- [**type**](#cmem_client.models.dataset.ItemLink.type) (<code>str</code>) – Kind of view the link opens, e.g. the dataset preview.

### `model_config` {#cmem_client.models.dataset.ItemLink.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `path` {#cmem_client.models.dataset.ItemLink.path}

```python
path: str = ''
```

### `type` {#cmem_client.models.dataset.ItemLink.type}

```python
type: str = ''
```

## `PluginProperty` {#cmem_client.models.dataset.PluginProperty}

Bases: <code>[Model](../models/base.md#cmem_client.models.base.Model)</code>

A single configuration property of a dataset plugin.

**Attributes:**

- [**title**](#cmem_client.models.dataset.PluginProperty.title) (<code>str</code>) – Human readable name of the property.
- [**description**](#cmem_client.models.dataset.PluginProperty.description) (<code>str</code>) – What the property configures.

### `description` {#cmem_client.models.dataset.PluginProperty.description}

```python
description: str = ''
```

### `model_config` {#cmem_client.models.dataset.PluginProperty.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `title` {#cmem_client.models.dataset.PluginProperty.title}

```python
title: str = ''
```

