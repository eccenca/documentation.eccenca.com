---
title: "cmem-client: models.logs module"
description: "Corporate Memory log buffer models."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.models.logs` {#cmem_client.models.logs}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Corporate Memory log buffer models.

Models for the in-memory log buffer API of a Corporate Memory service
(`GET /api/admin/logs` and `GET /api/admin/logs/status`). Each instance of a
service keeps its own buffer and answers only with its own lines, which is why
the responses carry an instance identifier and a per instance sequence number.

**Classes:**

- [**LogBufferStatus**](#cmem_client.models.logs.LogBufferStatus) – State and configuration of the in-memory log buffer of one instance.
- [**LogLevel**](#cmem_client.models.logs.LogLevel) – Log level a line can be requested at, ordered from least to most severe.
- [**LogLine**](#cmem_client.models.logs.LogLine) – A single buffered log line.
- [**LogTailResponse**](#cmem_client.models.logs.LogTailResponse) – The most recent buffered log lines of one instance, with the state of that read.

## `LogBufferStatus` {#cmem_client.models.logs.LogBufferStatus}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

State and configuration of the in-memory log buffer of one instance.

**Attributes:**

- [**enabled**](#cmem_client.models.logs.LogBufferStatus.enabled) (<code>bool</code>) – Whether the buffer is enabled in this deployment.
- [**attached**](#cmem_client.models.logs.LogBufferStatus.attached) (<code>bool</code>) – Whether the buffer is attached to the logging framework and therefore
actually capturing.
- [**capture_level**](#cmem_client.models.logs.LogBufferStatus.capture_level) (<code>str | None</code>) – The minimum level which is captured, regardless of the configured
logging levels.
- [**capacity**](#cmem_client.models.logs.LogBufferStatus.capacity) (<code>int</code>) – How many lines the buffer holds before the oldest ones are discarded.
- [**max_message_chars**](#cmem_client.models.logs.LogBufferStatus.max_message_chars) (<code>int</code>) – Length a message is truncated to before it is buffered.
- [**size**](#cmem_client.models.logs.LogBufferStatus.size) (<code>int</code>) – How many lines are buffered at the moment.
- [**first_sequence**](#cmem_client.models.logs.LogBufferStatus.first_sequence) (<code>int</code>) – Oldest sequence still buffered.
- [**last_sequence**](#cmem_client.models.logs.LogBufferStatus.last_sequence) (<code>int</code>) – Highest sequence buffered.
- [**instance_id**](#cmem_client.models.logs.LogBufferStatus.instance_id) (<code>str</code>) – The instance this status describes.
- [**excluded_loggers**](#cmem_client.models.logs.LogBufferStatus.excluded_loggers) (<code>list[str]</code>) – Loggers which are never captured, because they carry user data
or credentials.
- [**non_additive_loggers**](#cmem_client.models.logs.LogBufferStatus.non_additive_loggers) (<code>list[str]</code>) – Loggers which do not propagate to the buffer through their
parent.
- [**request_id_mdc_key**](#cmem_client.models.logs.LogBufferStatus.request_id_mdc_key) (<code>str | None</code>) – The mapped diagnostic context key the correlation identifier
is taken from.

### `attached` {#cmem_client.models.logs.LogBufferStatus.attached}

```python
attached: bool
```

### `capacity` {#cmem_client.models.logs.LogBufferStatus.capacity}

```python
capacity: int
```

### `capture_level` {#cmem_client.models.logs.LogBufferStatus.capture_level}

```python
capture_level: str | None = Field(alias='captureLevel', default=None)
```

### `enabled` {#cmem_client.models.logs.LogBufferStatus.enabled}

```python
enabled: bool
```

### `excluded_loggers` {#cmem_client.models.logs.LogBufferStatus.excluded_loggers}

```python
excluded_loggers: list[str] = Field(alias='excludedLoggers', default_factory=list)
```

### `first_sequence` {#cmem_client.models.logs.LogBufferStatus.first_sequence}

```python
first_sequence: int = Field(alias='firstSequence')
```

### `instance_id` {#cmem_client.models.logs.LogBufferStatus.instance_id}

```python
instance_id: str = Field(alias='instanceId')
```

### `last_sequence` {#cmem_client.models.logs.LogBufferStatus.last_sequence}

```python
last_sequence: int = Field(alias='lastSequence')
```

### `max_message_chars` {#cmem_client.models.logs.LogBufferStatus.max_message_chars}

```python
max_message_chars: int = Field(alias='maxMessageChars')
```

### `model_config` {#cmem_client.models.logs.LogBufferStatus.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `non_additive_loggers` {#cmem_client.models.logs.LogBufferStatus.non_additive_loggers}

```python
non_additive_loggers: list[str] = Field(alias='nonAdditiveLoggers', default_factory=list)
```

### `request_id_mdc_key` {#cmem_client.models.logs.LogBufferStatus.request_id_mdc_key}

```python
request_id_mdc_key: str | None = Field(alias='requestIdMdcKey', default=None)
```

### `size` {#cmem_client.models.logs.LogBufferStatus.size}

```python
size: int
```

## `LogLevel` {#cmem_client.models.logs.LogLevel}

Bases: <code>StrEnum</code>

Log level a line can be requested at, ordered from least to most severe.

The level of a request is a minimum: asking for WARN returns the lines logged
at WARN as well as the ones logged at ERROR.

**Attributes:**

- [**DEBUG**](#cmem_client.models.logs.LogLevel.DEBUG) –
- [**ERROR**](#cmem_client.models.logs.LogLevel.ERROR) –
- [**INFO**](#cmem_client.models.logs.LogLevel.INFO) –
- [**TRACE**](#cmem_client.models.logs.LogLevel.TRACE) –
- [**WARN**](#cmem_client.models.logs.LogLevel.WARN) –

### `DEBUG` {#cmem_client.models.logs.LogLevel.DEBUG}

```python
DEBUG = 'DEBUG'
```

### `ERROR` {#cmem_client.models.logs.LogLevel.ERROR}

```python
ERROR = 'ERROR'
```

### `INFO` {#cmem_client.models.logs.LogLevel.INFO}

```python
INFO = 'INFO'
```

### `TRACE` {#cmem_client.models.logs.LogLevel.TRACE}

```python
TRACE = 'TRACE'
```

### `WARN` {#cmem_client.models.logs.LogLevel.WARN}

```python
WARN = 'WARN'
```

## `LogLine` {#cmem_client.models.logs.LogLine}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

A single buffered log line.

**Attributes:**

- [**sequence**](#cmem_client.models.logs.LogLine.sequence) (<code>int</code>) – Position of this line in the log stream of the answering instance.
- [**timestamp**](#cmem_client.models.logs.LogLine.timestamp) (<code>datetime</code>) – When the line was logged.
- [**level**](#cmem_client.models.logs.LogLine.level) (<code>str</code>) – Level the line was logged at. Not restricted to LogLevel, because a
service may log at a level which cannot be requested.
- [**logger**](#cmem_client.models.logs.LogLine.logger) (<code>str</code>) – Name of the logger which produced the line.
- [**thread**](#cmem_client.models.logs.LogLine.thread) (<code>str | None</code>) – Thread the line was logged on, if the service reported one.
- [**message**](#cmem_client.models.logs.LogLine.message) (<code>str</code>) – The log message.
- [**throwable**](#cmem_client.models.logs.LogLine.throwable) (<code>str | None</code>) – The rendered exception, if the line carried one.
- [**request_id**](#cmem_client.models.logs.LogLine.request_id) (<code>str | None</code>) – Correlation identifier of the request which produced this line. The
same value is returned in the X-Request-Id header and, for a failed request,
in its problem detail. Lines logged off the request thread carry none.

### `level` {#cmem_client.models.logs.LogLine.level}

```python
level: str
```

### `logger` {#cmem_client.models.logs.LogLine.logger}

```python
logger: str
```

### `message` {#cmem_client.models.logs.LogLine.message}

```python
message: str
```

### `model_config` {#cmem_client.models.logs.LogLine.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `request_id` {#cmem_client.models.logs.LogLine.request_id}

```python
request_id: str | None = Field(alias='requestId', default=None)
```

### `sequence` {#cmem_client.models.logs.LogLine.sequence}

```python
sequence: int
```

### `thread` {#cmem_client.models.logs.LogLine.thread}

```python
thread: str | None = None
```

### `throwable` {#cmem_client.models.logs.LogLine.throwable}

```python
throwable: str | None = None
```

### `timestamp` {#cmem_client.models.logs.LogLine.timestamp}

```python
timestamp: datetime
```

## `LogTailResponse` {#cmem_client.models.logs.LogTailResponse}

Bases: <code>[Model](../../models/base/index.md#cmem_client.models.base.Model)</code>

The most recent buffered log lines of one instance, with the state of that read.

**Attributes:**

- [**server_time**](#cmem_client.models.logs.LogTailResponse.server_time) (<code>int</code>) – Epoch milliseconds the response was assembled at.
- [**instance_id**](#cmem_client.models.logs.LogTailResponse.instance_id) (<code>str</code>) – The instance which answered. Sequence numbers are only meaningful
together with this value.
- [**first_sequence**](#cmem_client.models.logs.LogTailResponse.first_sequence) (<code>int</code>) – Oldest sequence still buffered.
- [**last_sequence**](#cmem_client.models.logs.LogTailResponse.last_sequence) (<code>int</code>) – Highest sequence examined. Pass it as the `since` of the next
request to receive only what has been logged in between.
- [**truncated**](#cmem_client.models.logs.LogTailResponse.truncated) (<code>bool</code>) – Whether the limit cut the result short.
- [**dropped**](#cmem_client.models.logs.LogTailResponse.dropped) (<code>int</code>) – How many lines were lost between the requested `since` and what the
buffer still holds.
- [**lines**](#cmem_client.models.logs.LogTailResponse.lines) (<code>list[[LogLine](#cmem_client.models.logs.LogLine)]</code>) – The matching lines, oldest first.

### `dropped` {#cmem_client.models.logs.LogTailResponse.dropped}

```python
dropped: int = 0
```

### `first_sequence` {#cmem_client.models.logs.LogTailResponse.first_sequence}

```python
first_sequence: int = Field(alias='firstSequence')
```

### `instance_id` {#cmem_client.models.logs.LogTailResponse.instance_id}

```python
instance_id: str = Field(alias='instanceId')
```

### `last_sequence` {#cmem_client.models.logs.LogTailResponse.last_sequence}

```python
last_sequence: int = Field(alias='lastSequence')
```

### `lines` {#cmem_client.models.logs.LogTailResponse.lines}

```python
lines: list[LogLine] = Field(default_factory=list)
```

### `model_config` {#cmem_client.models.logs.LogTailResponse.model_config}

```python
model_config = ConfigDict(extra='allow', populate_by_name=True)
```

### `server_time` {#cmem_client.models.logs.LogTailResponse.server_time}

```python
server_time: int = Field(alias='serverTime')
```

### `truncated` {#cmem_client.models.logs.LogTailResponse.truncated}

```python
truncated: bool = False
```

