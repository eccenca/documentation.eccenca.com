---
title: "logging_utils"
tags:
  - API
  - Python
  - cmem-client
---

# `logging_utils` {#cmem_client.logging_utils}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Logging utilities.

Note: This module uses Any for kwargs to match the stdlib logging interface signature.

**Functions:**

- [**install_trace_logger**](#cmem_client.logging_utils.install_trace_logger) – Install TRACE level logging dynamically.
- [**log_method**](#cmem_client.logging_utils.log_method) – Wrapper to log entry and exit of methods using TRACE level.

**Attributes:**

- [**TRACE_LEVEL**](#cmem_client.logging_utils.TRACE_LEVEL) –

## `TRACE_LEVEL` {#cmem_client.logging_utils.TRACE_LEVEL}

```python
TRACE_LEVEL = 5
```

## `install_trace_logger` {#cmem_client.logging_utils.install_trace_logger}

```python
install_trace_logger()
```

Install TRACE level logging dynamically.

## `log_method` {#cmem_client.logging_utils.log_method}

```python
log_method(method, display_name=None)
```

Wrapper to log entry and exit of methods using TRACE level.

Note: Don't use this on methods with sensitive information as they might get logged too

**Returns:**

- **wrapper** (<code>Callable</code>) – The wrapped method, which logs its arguments on entry and its
result on exit.

