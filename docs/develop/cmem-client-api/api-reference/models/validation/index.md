---
title: "cmem-client: models.validation module"
description: "Validation models for SHACL batch validation processes."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.validation` {#cmem_client.models.validation}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Validation models for SHACL batch validation processes.

A batch validation checks the resources of a context graph against the shapes of a
shape graph and reports where they violate them. ``client.validations`` starts such a
process and holds the running and finished ones, keyed by their batch ID. The
aggregation is the summary a repository lists, while the result carries every single
violation; note that ``client.validations`` does not fetch on creation, so call
``fetch_data()`` before iterating it.

**Classes:**

- [**ValidationAggregation**](#cmem_client.models.validation.ValidationAggregation) – Summary view of a batch validation process.
- [**ValidationConstraintTemplate**](#cmem_client.models.validation.ValidationConstraintTemplate) – Constraint message template from a validation violation.
- [**ValidationResourceResult**](#cmem_client.models.validation.ValidationResourceResult) – Violations found for a single validated resource.
- [**ValidationResult**](#cmem_client.models.validation.ValidationResult) – Full result of a completed batch validation process.
- [**ValidationViolation**](#cmem_client.models.validation.ValidationViolation) – A single SHACL violation found during validation.
- [**ValidationViolationMessage**](#cmem_client.models.validation.ValidationViolationMessage) – A single message attached to a validation violation.

**Attributes:**

- [**STATUS_CANCELLED**](#cmem_client.models.validation.STATUS_CANCELLED) –
- [**STATUS_ERROR**](#cmem_client.models.validation.STATUS_ERROR) –
- [**STATUS_FINISHED**](#cmem_client.models.validation.STATUS_FINISHED) –
- [**STATUS_RUNNING**](#cmem_client.models.validation.STATUS_RUNNING) –
- [**STATUS_SCHEDULED**](#cmem_client.models.validation.STATUS_SCHEDULED) –

## `STATUS_CANCELLED` {#cmem_client.models.validation.STATUS_CANCELLED}

```python
STATUS_CANCELLED = 'CANCELLED'
```

## `STATUS_ERROR` {#cmem_client.models.validation.STATUS_ERROR}

```python
STATUS_ERROR = 'ERROR'
```

## `STATUS_FINISHED` {#cmem_client.models.validation.STATUS_FINISHED}

```python
STATUS_FINISHED = 'FINISHED'
```

## `STATUS_RUNNING` {#cmem_client.models.validation.STATUS_RUNNING}

```python
STATUS_RUNNING = 'RUNNING'
```

## `STATUS_SCHEDULED` {#cmem_client.models.validation.STATUS_SCHEDULED}

```python
STATUS_SCHEDULED = 'SCHEDULED'
```

## `ValidationAggregation` {#cmem_client.models.validation.ValidationAggregation}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>, <code>[ReadRepositoryItem](../../models/base/index.md#cmem_client.models.base.ReadRepositoryItem)</code>

Summary view of a batch validation process.

**Attributes:**

- [**id**](#cmem_client.models.validation.ValidationAggregation.id) (<code>str</code>) – ID of the batch. This is the key of the repository.
- [**state**](#cmem_client.models.validation.ValidationAggregation.state) (<code>str</code>) – What the batch is doing, one of ``SCHEDULED``, ``RUNNING``,
``FINISHED``, ``CANCELLED`` or ``ERROR``.
- [**context_graph_iri**](#cmem_client.models.validation.ValidationAggregation.context_graph_iri) (<code>str</code>) – IRI of the graph whose resources are validated.
- [**shape_graph_iri**](#cmem_client.models.validation.ValidationAggregation.shape_graph_iri) (<code>str</code>) – IRI of the graph holding the shapes.
- [**execution_started**](#cmem_client.models.validation.ValidationAggregation.execution_started) (<code>int | None</code>) – When the validation started, as a Unix timestamp in
milliseconds, or ``None`` while it is still scheduled.
- [**execution_finished**](#cmem_client.models.validation.ValidationAggregation.execution_finished) (<code>int | None</code>) – When it finished, or ``None`` while it is still running.
- [**resource_count**](#cmem_client.models.validation.ValidationAggregation.resource_count) (<code>int</code>) – How many resources the batch covers.
- [**resource_processed_count**](#cmem_client.models.validation.ValidationAggregation.resource_processed_count) (<code>int</code>) – How many of them are done. Compare with
``resource_count`` to follow the progress of a running batch.
- [**resources_with_violations_count**](#cmem_client.models.validation.ValidationAggregation.resources_with_violations_count) (<code>int</code>) – How many resources violated at least one
shape.
- [**violations_count**](#cmem_client.models.validation.ValidationAggregation.violations_count) (<code>int</code>) – How many violations were found in total.
- [**error**](#cmem_client.models.validation.ValidationAggregation.error) (<code>str | None</code>) – Why the batch failed, set only in state ``ERROR``.

**Functions:**

- [**get_id**](#cmem_client.models.validation.ValidationAggregation.get_id) – Get the batch validation process ID.

### `context_graph_iri` {#cmem_client.models.validation.ValidationAggregation.context_graph_iri}

```python
context_graph_iri: str = Field(alias='contextGraphIri')
```

### `error` {#cmem_client.models.validation.ValidationAggregation.error}

```python
error: str | None = Field(default=None)
```

### `execution_finished` {#cmem_client.models.validation.ValidationAggregation.execution_finished}

```python
execution_finished: int | None = Field(alias='executionFinished', default=None)
```

### `execution_started` {#cmem_client.models.validation.ValidationAggregation.execution_started}

```python
execution_started: int | None = Field(alias='executionStarted', default=None)
```

### `get_id` {#cmem_client.models.validation.ValidationAggregation.get_id}

```python
get_id()
```

Get the batch validation process ID.

### `id` {#cmem_client.models.validation.ValidationAggregation.id}

```python
id: str
```

### `model_config` {#cmem_client.models.validation.ValidationAggregation.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `resource_count` {#cmem_client.models.validation.ValidationAggregation.resource_count}

```python
resource_count: int = Field(alias='resourceCount', default=0)
```

### `resource_processed_count` {#cmem_client.models.validation.ValidationAggregation.resource_processed_count}

```python
resource_processed_count: int = Field(alias='resourceProcessedCount', default=0)
```

### `resources_with_violations_count` {#cmem_client.models.validation.ValidationAggregation.resources_with_violations_count}

```python
resources_with_violations_count: int = Field(alias='resourcesWithViolationsCount', default=0)
```

### `shape_graph_iri` {#cmem_client.models.validation.ValidationAggregation.shape_graph_iri}

```python
shape_graph_iri: str = Field(alias='shapeGraphIri', default='')
```

### `state` {#cmem_client.models.validation.ValidationAggregation.state}

```python
state: str
```

### `violations_count` {#cmem_client.models.validation.ValidationAggregation.violations_count}

```python
violations_count: int = Field(alias='violationsCount', default=0)
```

## `ValidationConstraintTemplate` {#cmem_client.models.validation.ValidationConstraintTemplate}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Constraint message template from a validation violation.

**Attributes:**

- [**constraint_name**](#cmem_client.models.validation.ValidationConstraintTemplate.constraint_name) (<code>str</code>) – Name of the SHACL constraint which was violated, e.g.
``MinCountConstraintComponent``.

### `constraint_name` {#cmem_client.models.validation.ValidationConstraintTemplate.constraint_name}

```python
constraint_name: str = Field(alias='constraintName')
```

### `model_config` {#cmem_client.models.validation.ValidationConstraintTemplate.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

## `ValidationResourceResult` {#cmem_client.models.validation.ValidationResourceResult}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Violations found for a single validated resource.

**Attributes:**

- [**resource_iri**](#cmem_client.models.validation.ValidationResourceResult.resource_iri) (<code>str</code>) – IRI of the validated resource.
- [**node_shapes**](#cmem_client.models.validation.ValidationResourceResult.node_shapes) (<code>list[str]</code>) – IRIs of the node shapes the resource was checked against.
- [**violations**](#cmem_client.models.validation.ValidationResourceResult.violations) (<code>list[[ValidationViolation](#cmem_client.models.validation.ValidationViolation)]</code>) – The violations found on this resource.

### `model_config` {#cmem_client.models.validation.ValidationResourceResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `node_shapes` {#cmem_client.models.validation.ValidationResourceResult.node_shapes}

```python
node_shapes: list[str] = Field(alias='nodeShapes', default_factory=list)
```

### `resource_iri` {#cmem_client.models.validation.ValidationResourceResult.resource_iri}

```python
resource_iri: str = Field(alias='resourceIri')
```

### `violations` {#cmem_client.models.validation.ValidationResourceResult.violations}

```python
violations: list[ValidationViolation] = Field(default_factory=list)
```

## `ValidationResult` {#cmem_client.models.validation.ValidationResult}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

Full result of a completed batch validation process.

**Attributes:**

- [**id**](#cmem_client.models.validation.ValidationResult.id) (<code>str</code>) – ID of the batch this result belongs to.
- [**context_graph_iri**](#cmem_client.models.validation.ValidationResult.context_graph_iri) (<code>str</code>) – IRI of the graph whose resources were validated.
- [**shape_graph_iri**](#cmem_client.models.validation.ValidationResult.shape_graph_iri) (<code>str</code>) – IRI of the graph holding the shapes they were checked against.
- [**execution_started**](#cmem_client.models.validation.ValidationResult.execution_started) (<code>int | None</code>) – When the validation started, as a Unix timestamp in
milliseconds, or ``None`` while it is still scheduled.
- [**execution_finished**](#cmem_client.models.validation.ValidationResult.execution_finished) (<code>int | None</code>) – When it finished, as a Unix timestamp in milliseconds, or
``None`` while it is still running. The endpoint returns a result for a
batch which has not finished yet, and leaves the field out then.
- [**resources**](#cmem_client.models.validation.ValidationResult.resources) (<code>list[str]</code>) – IRIs of every validated resource, including those without a
violation.
- [**results**](#cmem_client.models.validation.ValidationResult.results) (<code>list[[ValidationResourceResult](#cmem_client.models.validation.ValidationResourceResult)]</code>) – The per-resource violations. Resources which passed are not listed.

### `context_graph_iri` {#cmem_client.models.validation.ValidationResult.context_graph_iri}

```python
context_graph_iri: str = Field(alias='contextGraphIri')
```

### `execution_finished` {#cmem_client.models.validation.ValidationResult.execution_finished}

```python
execution_finished: int | None = Field(alias='executionFinished', default=None)
```

### `execution_started` {#cmem_client.models.validation.ValidationResult.execution_started}

```python
execution_started: int | None = Field(alias='executionStarted', default=None)
```

### `id` {#cmem_client.models.validation.ValidationResult.id}

```python
id: str
```

### `model_config` {#cmem_client.models.validation.ValidationResult.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `resources` {#cmem_client.models.validation.ValidationResult.resources}

```python
resources: list[str] = Field(default_factory=list)
```

### `results` {#cmem_client.models.validation.ValidationResult.results}

```python
results: list[ValidationResourceResult] = Field(default_factory=list)
```

### `shape_graph_iri` {#cmem_client.models.validation.ValidationResult.shape_graph_iri}

```python
shape_graph_iri: str = Field(alias='shapeGraphIri')
```

## `ValidationViolation` {#cmem_client.models.validation.ValidationViolation}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A single SHACL violation found during validation.

**Attributes:**

- [**report_entry_constraint_message_template**](#cmem_client.models.validation.ValidationViolation.report_entry_constraint_message_template) (<code>[ValidationConstraintTemplate](#cmem_client.models.validation.ValidationConstraintTemplate)</code>) – The violated constraint.
- [**path**](#cmem_client.models.validation.ValidationViolation.path) (<code>str | None</code>) – IRI of the property the violation was found on, or ``None`` for a
violation which concerns the resource as a whole.
- [**source**](#cmem_client.models.validation.ValidationViolation.source) (<code>str | None</code>) – IRI of the shape which raised the violation.
- [**messages**](#cmem_client.models.validation.ValidationViolation.messages) (<code>list[[ValidationViolationMessage](#cmem_client.models.validation.ValidationViolationMessage)]</code>) – Human readable messages of the violation, one per language.
- [**severity**](#cmem_client.models.validation.ValidationViolation.severity) (<code>str | None</code>) – Severity declared by the shape, e.g. ``Violation`` or ``Warning``.

### `messages` {#cmem_client.models.validation.ValidationViolation.messages}

```python
messages: list[ValidationViolationMessage] = Field(default_factory=list)
```

### `model_config` {#cmem_client.models.validation.ValidationViolation.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `path` {#cmem_client.models.validation.ValidationViolation.path}

```python
path: str | None = None
```

### `report_entry_constraint_message_template` {#cmem_client.models.validation.ValidationViolation.report_entry_constraint_message_template}

```python
report_entry_constraint_message_template: ValidationConstraintTemplate = Field(alias='reportEntryConstraintMessageTemplate')
```

### `severity` {#cmem_client.models.validation.ValidationViolation.severity}

```python
severity: str | None = None
```

### `source` {#cmem_client.models.validation.ValidationViolation.source}

```python
source: str | None = None
```

## `ValidationViolationMessage` {#cmem_client.models.validation.ValidationViolationMessage}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A single message attached to a validation violation.

**Attributes:**

- [**value**](#cmem_client.models.validation.ValidationViolationMessage.value) (<code>str</code>) – Text of the message.
- [**lang**](#cmem_client.models.validation.ValidationViolationMessage.lang) (<code>str</code>) – Language tag of the message, empty if it carries none.

### `lang` {#cmem_client.models.validation.ValidationViolationMessage.lang}

```python
lang: str = ''
```

### `model_config` {#cmem_client.models.validation.ValidationViolationMessage.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `value` {#cmem_client.models.validation.ValidationViolationMessage.value}

```python
value: str
```

