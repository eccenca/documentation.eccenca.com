# `logging_config` {#cmem_client.models.logging_config}

Models for the configuration of the logging module

``Client.configure_logging_from_dict()`` and ``configure_logging_from_json()`` validate
their input against these models before handing it to ``logging.config.dictConfig()``,
so a malformed logging configuration is rejected with a readable error instead of
failing inside the standard library. The models mirror the dictConfig schema and allow
extra keys, so anything dictConfig understands stays usable.

**Classes:**

- [**FormatterConfig**](#cmem_client.models.logging_config.FormatterConfig) – Formatter configuration.
- [**HandlerConfig**](#cmem_client.models.logging_config.HandlerConfig) – Handler configuration.
- [**LoggerConfig**](#cmem_client.models.logging_config.LoggerConfig) – Logger configuration.
- [**LoggingConfig**](#cmem_client.models.logging_config.LoggingConfig) – Logging configuration. Allows for extra fields but validates the most common fields.

**Attributes:**

- [**LogLevel**](#cmem_client.models.logging_config.LogLevel) – Levels accepted in a logging configuration, including the client's own ``TRACE``.

## `FormatterConfig` {#cmem_client.models.logging_config.FormatterConfig}

Bases: <code>BaseModel</code>

Formatter configuration.

**Attributes:**

- [**format**](#cmem_client.models.logging_config.FormatterConfig.format) (<code>str</code>) – Format string of the log records, e.g.
``"%(asctime)s - %(name)s - %(levelname)s - %(message)s"``.
- [**datefmt**](#cmem_client.models.logging_config.FormatterConfig.datefmt) (<code>str | None</code>) – Format string for the timestamp, or ``None`` for the default.

### `datefmt` {#cmem_client.models.logging_config.FormatterConfig.datefmt}

```python
datefmt: str | None = None
```

### `format` {#cmem_client.models.logging_config.FormatterConfig.format}

```python
format: str
```

## `HandlerConfig` {#cmem_client.models.logging_config.HandlerConfig}

Bases: <code>BaseModel</code>

Handler configuration.

**Attributes:**

- [**class_**](#cmem_client.models.logging_config.HandlerConfig.class_) (<code>str</code>) – Dotted path of the handler class, e.g. ``logging.StreamHandler``.
Written as ``class`` in the configuration itself.
- [**level**](#cmem_client.models.logging_config.HandlerConfig.level) (<code>[LogLevel](#cmem_client.models.logging_config.LogLevel) | None</code>) – Lowest level this handler emits, or ``None`` to inherit from the logger.
- [**formatter**](#cmem_client.models.logging_config.HandlerConfig.formatter) (<code>str | None</code>) – Name of the formatter to use, referring to a key of ``formatters``.
- [**filename**](#cmem_client.models.logging_config.HandlerConfig.filename) (<code>str | None</code>) – File the handler writes to, for the file based handlers.

### `class_` {#cmem_client.models.logging_config.HandlerConfig.class_}

```python
class_: str = Field(..., alias='class')
```

### `filename` {#cmem_client.models.logging_config.HandlerConfig.filename}

```python
filename: str | None
```

### `formatter` {#cmem_client.models.logging_config.HandlerConfig.formatter}

```python
formatter: str | None
```

### `level` {#cmem_client.models.logging_config.HandlerConfig.level}

```python
level: LogLevel | None
```

## `LogLevel` {#cmem_client.models.logging_config.LogLevel}

```python
LogLevel = Literal['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
```

Levels accepted in a logging configuration, including the client's own ``TRACE``.

## `LoggerConfig` {#cmem_client.models.logging_config.LoggerConfig}

Bases: <code>BaseModel</code>

Logger configuration.

**Attributes:**

- [**level**](#cmem_client.models.logging_config.LoggerConfig.level) (<code>[LogLevel](#cmem_client.models.logging_config.LogLevel) | None</code>) – Lowest level this logger passes on, e.g. ``DEBUG``.
- [**handlers**](#cmem_client.models.logging_config.LoggerConfig.handlers) (<code>list[str] | None</code>) – Names of the handlers to attach, referring to keys of ``handlers``.

### `handlers` {#cmem_client.models.logging_config.LoggerConfig.handlers}

```python
handlers: list[str] | None
```

### `level` {#cmem_client.models.logging_config.LoggerConfig.level}

```python
level: LogLevel | None
```

## `LoggingConfig` {#cmem_client.models.logging_config.LoggingConfig}

Bases: <code>BaseModel</code>

Logging configuration. Allows for extra fields but validates the most common fields.

**Attributes:**

- [**version**](#cmem_client.models.logging_config.LoggingConfig.version) (<code>int</code>) – Schema version of the configuration. dictConfig only knows ``1``, and
anything else is rejected.
- [**disable_existing_loggers**](#cmem_client.models.logging_config.LoggingConfig.disable_existing_loggers) (<code>bool</code>) – Whether loggers which already exist are switched off.
Setting this silences libraries that configured logging before the client.
- [**formatters**](#cmem_client.models.logging_config.LoggingConfig.formatters) (<code>dict[str, [FormatterConfig](#cmem_client.models.logging_config.FormatterConfig)] | None</code>) – Formatters of the configuration, keyed by name.
- [**handlers**](#cmem_client.models.logging_config.LoggingConfig.handlers) (<code>dict[str, [HandlerConfig](#cmem_client.models.logging_config.HandlerConfig)] | None</code>) – Handlers of the configuration, keyed by name.
- [**loggers**](#cmem_client.models.logging_config.LoggingConfig.loggers) (<code>dict[str, [LoggerConfig](#cmem_client.models.logging_config.LoggerConfig)] | None</code>) – Loggers of the configuration, keyed by logger name. Configure
``cmem_client.client`` to cover the whole library at once.
- [**root**](#cmem_client.models.logging_config.LoggingConfig.root) (<code>[LoggerConfig](#cmem_client.models.logging_config.LoggerConfig) | None</code>) – Configuration of the root logger.

**Functions:**

- [**check_version**](#cmem_client.models.logging_config.LoggingConfig.check_version) – Ensure version is always 1.

### `check_version` {#cmem_client.models.logging_config.LoggingConfig.check_version}

```python
check_version(v)
```

Ensure version is always 1.

### `disable_existing_loggers` {#cmem_client.models.logging_config.LoggingConfig.disable_existing_loggers}

```python
disable_existing_loggers: bool
```

### `formatters` {#cmem_client.models.logging_config.LoggingConfig.formatters}

```python
formatters: dict[str, FormatterConfig] | None
```

### `handlers` {#cmem_client.models.logging_config.LoggingConfig.handlers}

```python
handlers: dict[str, HandlerConfig] | None
```

### `loggers` {#cmem_client.models.logging_config.LoggingConfig.loggers}

```python
loggers: dict[str, LoggerConfig] | None
```

### `model_config` {#cmem_client.models.logging_config.LoggingConfig.model_config}

```python
model_config = {'extra': 'allow'}
```

### `root` {#cmem_client.models.logging_config.LoggingConfig.root}

```python
root: LoggerConfig | None
```

### `version` {#cmem_client.models.logging_config.LoggingConfig.version}

```python
version: int = 1
```

