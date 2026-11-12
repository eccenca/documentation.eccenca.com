---
title: "cmem-client: components.build.logs module"
description: "The in-memory log buffer of Build (DataIntegration)."
tags:
  - API
  - Python
  - cmem-client
---

# `cmem_client.components.build.logs` {#cmem_client.components.build.logs}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

The in-memory log buffer of Build (DataIntegration).

**Classes:**

- [**BuildLogs**](#cmem_client.components.build.logs.BuildLogs) – Read the in-memory log buffer of Build: the most recent lines, and its state.

## `BuildLogs` {#cmem_client.components.build.logs.BuildLogs}

Bases: <code>_LogBuffer</code>

Read the in-memory log buffer of Build: the most recent lines, and its state.

Build offers the same log API as Explore, with one difference: it does not record
request ids, so its lines cannot be filtered by one. Build would ignore such a filter
and answer with every line it holds, which is why `get_tail()` does not offer it.

**Examples:**

```pycon
>>> from cmem_client.client import Client
>>> client = Client.from_env()
>>> tail = client.build.logs.get_tail(level="WARN", limit=10)
>>> [line.message for line in tail.lines]
```

**Functions:**

- [**get_status**](#cmem_client.components.build.logs.BuildLogs.get_status) – Read the state of the in-memory log buffer of Build.
- [**get_tail**](#cmem_client.components.build.logs.BuildLogs.get_tail) – Read the most recent log lines of Build.

**Attributes:**

- [**logger**](#cmem_client.components.build.logs.BuildLogs.logger) –

### `get_status` {#cmem_client.components.build.logs.BuildLogs.get_status}

```python
get_status()
```

Read the state of the in-memory log buffer of Build.

Reports whether lines are captured at all, at which level, how many are held and
which loggers are excluded. This is the way to find out why a log read returns
fewer lines than expected, or none.

**Returns:**

- <code>[LogBufferStatus](../../../models/logs/index.md#cmem_client.models.logs.LogBufferStatus)</code> – The state and configuration of the buffer of the instance which answered.

**Raises:**

- <code>HTTPStatusError</code> – If the request fails, for example because the deployment
does not know the endpoint or the user is not authorized for it.
- <code>LogsReadError</code> – If the answer is not a log buffer status.

### `get_tail` {#cmem_client.components.build.logs.BuildLogs.get_tail}

```python
get_tail(since=None, limit=None, level=None, logger=None, contains=None)
```

Read the most recent log lines of Build.

The lines are returned oldest first, and every filter is applied by Build before
the limit. Which end the limit cuts depends on `since`: without it Build answers
the newest `limit` matching lines, and with it the oldest `limit` lines after the
cursor, so a follower pages forward instead of skipping ahead.

To follow the log, pass the `last_sequence` of the previous response as `since`
of the next request. A `dropped` above zero in a response means the client fell
behind and those lines are no longer buffered. Sequence numbers belong to the
instance which answered, so a changed `instance_id` invalidates the cursor.

**Parameters:**

- **since** (<code>int | None</code>) – Return only lines with a sequence higher than this one.
- **limit** (<code>int | None</code>) – Maximum number of lines to return. Build clamps this to its own
configured maximum rather than rejecting a larger value. Without a limit
Build answers its own default page, which is smaller than its maximum.
- **level** (<code>[LogLevel](../../../models/logs/index.md#cmem_client.models.logs.LogLevel) | str | None</code>) – Minimum level a line has to be logged at. Asking for WARN returns
WARN and ERROR lines.
- **logger** (<code>list[str] | None</code>) – Return only lines of loggers starting with one of these prefixes.
- **contains** (<code>list[str] | None</code>) – Return only lines containing all of these substrings, ignoring
case.

**Returns:**

- <code>[LogTailResponse](../../../models/logs/index.md#cmem_client.models.logs.LogTailResponse)</code> – The matching lines together with the state of the read.

**Raises:**

- <code>HTTPStatusError</code> – If the request fails, for example because a filter value is
not valid, the buffer is disabled or the user is not authorized.
- <code>LogsReadError</code> – If the answer is not a log buffer response.

### `logger` {#cmem_client.components.build.logs.BuildLogs.logger}

```python
logger = logging.getLogger(f'{self._client.logger.name}.{self.__class__.__name__}')
```

