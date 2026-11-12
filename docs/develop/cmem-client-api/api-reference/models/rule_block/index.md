---
title: "cmem-client: models.rule_block module"
description: "Corporate Memory rule block models for data integration."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.rule_block` {#cmem_client.models.rule_block}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory rule block models for data integration.

A rule block is a reusable transformation unit: a named operator tree with
declared input ports, referenced from transform and linking rules instead of
being copied into them. Rule blocks are project-scoped task items of type
``RuleBlock`` and are available from Corporate Memory 26.2 onwards.

The whole body of a rule block is a single opaque object parameter named
``ruleBlockModel``. Only its ports are modelled explicitly here, because they
are the part callers typically read and report; the operator tree, the input
examples and the editor layout are passed through untouched.

**Classes:**

- [**RuleBlock**](#cmem_client.models.rule_block.RuleBlock) – A rule block description (Build).
- [**RuleBlockData**](#cmem_client.models.rule_block.RuleBlockData) – The data section of a rule block task.
- [**RuleBlockMetadata**](#cmem_client.models.rule_block.RuleBlockMetadata) – Metadata of a rule block.
- [**RuleBlockModel**](#cmem_client.models.rule_block.RuleBlockModel) – The complete rule block model: ports, operator tree, examples and layout.
- [**RuleBlockPort**](#cmem_client.models.rule_block.RuleBlockPort) – A declared input port of a rule block.
- [**RuleBlockSearchResultSet**](#cmem_client.models.rule_block.RuleBlockSearchResultSet) – A rule block search result set.

## `RuleBlock` {#cmem_client.models.rule_block.RuleBlock}

Bases: <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

A rule block description (Build).

**Functions:**

- [**get_id**](#cmem_client.models.rule_block.RuleBlock.get_id) – Get the combined ID of the rule block.

**Attributes:**

- [**data**](#cmem_client.models.rule_block.RuleBlock.data) (<code>[RuleBlockData](#cmem_client.models.rule_block.RuleBlockData)</code>) –
- [**id**](#cmem_client.models.rule_block.RuleBlock.id) (<code>str</code>) –
- [**item_links**](#cmem_client.models.rule_block.RuleBlock.item_links) (<code>list[[ItemLink](../../models/dataset/index.md#cmem_client.models.dataset.ItemLink)]</code>) –
- [**metadata**](#cmem_client.models.rule_block.RuleBlock.metadata) (<code>[RuleBlockMetadata](#cmem_client.models.rule_block.RuleBlockMetadata)</code>) –
- [**model_config**](#cmem_client.models.rule_block.RuleBlock.model_config) –
- [**project_id**](#cmem_client.models.rule_block.RuleBlock.project_id) (<code>str</code>) –
- [**tags**](#cmem_client.models.rule_block.RuleBlock.tags) (<code>list[[Tag](../../models/common/index.md#cmem_client.models.common.Tag)]</code>) –

### `data` {#cmem_client.models.rule_block.RuleBlock.data}

```python
data: RuleBlockData = Field(default_factory=RuleBlockData)
```

### `get_id` {#cmem_client.models.rule_block.RuleBlock.get_id}

```python
get_id()
```

Get the combined ID of the rule block.

### `id` {#cmem_client.models.rule_block.RuleBlock.id}

```python
id: str
```

### `item_links` {#cmem_client.models.rule_block.RuleBlock.item_links}

```python
item_links: list[ItemLink] = Field(default_factory=list, alias='itemLinks')
```

### `metadata` {#cmem_client.models.rule_block.RuleBlock.metadata}

```python
metadata: RuleBlockMetadata = Field(default_factory=RuleBlockMetadata)
```

### `model_config` {#cmem_client.models.rule_block.RuleBlock.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `project_id` {#cmem_client.models.rule_block.RuleBlock.project_id}

```python
project_id: str = Field(alias='project', default='')
```

### `tags` {#cmem_client.models.rule_block.RuleBlock.tags}

```python
tags: list[Tag] = Field(default_factory=list)
```

## `RuleBlockData` {#cmem_client.models.rule_block.RuleBlockData}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The data section of a rule block task.

**Attributes:**

- [**model_config**](#cmem_client.models.rule_block.RuleBlockData.model_config) –
- [**rule_block_model**](#cmem_client.models.rule_block.RuleBlockData.rule_block_model) (<code>[RuleBlockModel](#cmem_client.models.rule_block.RuleBlockModel)</code>) –
- [**task_type**](#cmem_client.models.rule_block.RuleBlockData.task_type) (<code>str</code>) –
- [**type**](#cmem_client.models.rule_block.RuleBlockData.type) (<code>str</code>) –

### `model_config` {#cmem_client.models.rule_block.RuleBlockData.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `rule_block_model` {#cmem_client.models.rule_block.RuleBlockData.rule_block_model}

```python
rule_block_model: RuleBlockModel = Field(alias='ruleBlockModel', default_factory=RuleBlockModel)
```

### `task_type` {#cmem_client.models.rule_block.RuleBlockData.task_type}

```python
task_type: str = Field(alias='taskType', default='RuleBlock')
```

### `type` {#cmem_client.models.rule_block.RuleBlockData.type}

```python
type: str = 'ruleBlock'
```

## `RuleBlockMetadata` {#cmem_client.models.rule_block.RuleBlockMetadata}

Bases: <code>TypedDict</code>

Metadata of a rule block.

**Attributes:**

- [**created**](#cmem_client.models.rule_block.RuleBlockMetadata.created) (<code>str</code>) –
- [**createdByUser**](#cmem_client.models.rule_block.RuleBlockMetadata.createdByUser) (<code>str</code>) –
- [**description**](#cmem_client.models.rule_block.RuleBlockMetadata.description) (<code>str</code>) –
- [**label**](#cmem_client.models.rule_block.RuleBlockMetadata.label) (<code>str</code>) –
- [**lastModifiedByUser**](#cmem_client.models.rule_block.RuleBlockMetadata.lastModifiedByUser) (<code>str</code>) –
- [**modified**](#cmem_client.models.rule_block.RuleBlockMetadata.modified) (<code>str</code>) –

### `created` {#cmem_client.models.rule_block.RuleBlockMetadata.created}

```python
created: str
```

### `createdByUser` {#cmem_client.models.rule_block.RuleBlockMetadata.createdByUser}

```python
createdByUser: str
```

### `description` {#cmem_client.models.rule_block.RuleBlockMetadata.description}

```python
description: str
```

### `label` {#cmem_client.models.rule_block.RuleBlockMetadata.label}

```python
label: str
```

### `lastModifiedByUser` {#cmem_client.models.rule_block.RuleBlockMetadata.lastModifiedByUser}

```python
lastModifiedByUser: str
```

### `modified` {#cmem_client.models.rule_block.RuleBlockMetadata.modified}

```python
modified: str
```

## `RuleBlockModel` {#cmem_client.models.rule_block.RuleBlockModel}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The complete rule block model: ports, operator tree, examples and layout.

The defaults are those of an empty rule block as DataIntegration creates it;
it rejects a model whose layout lacks ``nodePositions``.

**Attributes:**

- [**input_examples**](#cmem_client.models.rule_block.RuleBlockModel.input_examples) (<code>list[Any]</code>) –
- [**layout**](#cmem_client.models.rule_block.RuleBlockModel.layout) (<code>dict[str, Any]</code>) –
- [**model_config**](#cmem_client.models.rule_block.RuleBlockModel.model_config) –
- [**operator_tree**](#cmem_client.models.rule_block.RuleBlockModel.operator_tree) (<code>Any</code>) –
- [**ports**](#cmem_client.models.rule_block.RuleBlockModel.ports) (<code>list[[RuleBlockPort](#cmem_client.models.rule_block.RuleBlockPort)]</code>) –
- [**ui_annotations**](#cmem_client.models.rule_block.RuleBlockModel.ui_annotations) (<code>dict[str, Any]</code>) –

### `input_examples` {#cmem_client.models.rule_block.RuleBlockModel.input_examples}

```python
input_examples: list[Any] = Field(alias='inputExamples', default_factory=list)
```

### `layout` {#cmem_client.models.rule_block.RuleBlockModel.layout}

```python
layout: dict[str, Any] = Field(default_factory=lambda: {'nodePositions': {}})
```

### `model_config` {#cmem_client.models.rule_block.RuleBlockModel.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `operator_tree` {#cmem_client.models.rule_block.RuleBlockModel.operator_tree}

```python
operator_tree: Any = Field(alias='operatorTree', default=None)
```

### `ports` {#cmem_client.models.rule_block.RuleBlockModel.ports}

```python
ports: list[RuleBlockPort] = Field(default_factory=list)
```

### `ui_annotations` {#cmem_client.models.rule_block.RuleBlockModel.ui_annotations}

```python
ui_annotations: dict[str, Any] = Field(alias='uiAnnotations', default_factory=lambda: {'stickyNotes': []})
```

## `RuleBlockPort` {#cmem_client.models.rule_block.RuleBlockPort}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A declared input port of a rule block.

**Attributes:**

- [**deprecated**](#cmem_client.models.rule_block.RuleBlockPort.deprecated) (<code>bool</code>) –
- [**description**](#cmem_client.models.rule_block.RuleBlockPort.description) (<code>str</code>) –
- [**display_order**](#cmem_client.models.rule_block.RuleBlockPort.display_order) (<code>int</code>) –
- [**id**](#cmem_client.models.rule_block.RuleBlockPort.id) (<code>str</code>) –
- [**label**](#cmem_client.models.rule_block.RuleBlockPort.label) (<code>str</code>) –
- [**model_config**](#cmem_client.models.rule_block.RuleBlockPort.model_config) –

### `deprecated` {#cmem_client.models.rule_block.RuleBlockPort.deprecated}

```python
deprecated: bool = False
```

### `description` {#cmem_client.models.rule_block.RuleBlockPort.description}

```python
description: str = ''
```

### `display_order` {#cmem_client.models.rule_block.RuleBlockPort.display_order}

```python
display_order: int = Field(alias='displayOrder', default=0)
```

### `id` {#cmem_client.models.rule_block.RuleBlockPort.id}

```python
id: str = ''
```

### `label` {#cmem_client.models.rule_block.RuleBlockPort.label}

```python
label: str = ''
```

### `model_config` {#cmem_client.models.rule_block.RuleBlockPort.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `RuleBlockSearchResultSet` {#cmem_client.models.rule_block.RuleBlockSearchResultSet}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A rule block search result set.

**Attributes:**

- [**model_config**](#cmem_client.models.rule_block.RuleBlockSearchResultSet.model_config) –
- [**results**](#cmem_client.models.rule_block.RuleBlockSearchResultSet.results) (<code>list[[RuleBlock](#cmem_client.models.rule_block.RuleBlock)]</code>) –

### `model_config` {#cmem_client.models.rule_block.RuleBlockSearchResultSet.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `results` {#cmem_client.models.rule_block.RuleBlockSearchResultSet.results}

```python
results: list[RuleBlock]
```

