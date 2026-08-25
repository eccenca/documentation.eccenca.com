---
title: "client"
tags:
  - API
  - Python
  - cmem-client
---

# `client` {#cmem_client.client}

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Main API client for eccenca Corporate Memory.

This module provides the primary Client class that serves as the central interface
for interacting with eccenca Corporate Memory instances. The Client orchestrates
authentication, HTTP communication, and provides access to various service components
like workspaces and graph stores.

The Client uses lazy loading for its components and can be configured either manually
or automatically from environment variables, making it flexible for different
deployment scenarios.

**Examples:**

```pycon
>>> from os import environ
>>> from cmem_client.models.url import HttpUrl
>>> from cmem_client.auth_provider.client_credentials import ClientCredentialsFlow
>>> config = Config(url_base=HttpUrl(environ.get("TESTING_BASE_URL")))
>>> client = Client(config=config)
>>> client_id = environ.get("TESTING_CCF_CLIENT_ID")
>>> client_secret = environ.get("TESTING_CCF_CLIENT_SECRET")
>>> client.auth = ClientCredentialsFlow(config=config, client_id=client_id, client_secret=client_secret)
>>> # Client is now configured with oauth provider from environment
```

<details class="logging" open markdown="1">
<summary>Logging</summary>

The client logs through the standard library. Its logger is ``cmem_client.client``
unless another one is passed to the constructor, and every component creates a child
of it, named after its class (``cmem_client.client.GraphsRepository``). Configuring
the client logger therefore configures the whole library.

The quickest way is ``configure_client_logger()``, which sets the level and installs
a handler:

>>> client = Client.from_env()
>>> client.configure_client_logger(level="DEBUG")
>>> client.configure_client_logger(level="INFO", filename="cmem.log")

Deployments which already describe their logging in a file use
``configure_logging_from_dict()`` or ``configure_logging_from_json()`` instead. Both
validate the configuration against
[LoggingConfig](models/logging_config.md#cmem_client.models.logging_config.LoggingConfig) before handing it to
``logging.config.dictConfig()``:

>>> client.configure_logging_from_json(Path("logging.json"))

In addition to the standard levels, the client installs a ``TRACE`` level (5), which
is more verbose than ``DEBUG``. Methods carrying the
[log_method](logging_utils.md#cmem_client.logging_utils.log_method) decorator log their arguments on
entry and their result on exit at that level, which makes it useful when a request
does not do what you expect:

>>> client.configure_client_logger(level="TRACE")
>>> client.configure_client_logger(level="INFO")

Because ``TRACE`` logs arguments and results verbatim, it can write credentials and
payloads into your logs. Keep it out of production.

</details>

**Classes:**

- [**Client**](#cmem_client.client.Client) – API Client for eccenca Corporate Memory.

## `Client` {#cmem_client.client.Client}

```python
Client(config, auth=None, logger=None)
```

API Client for eccenca Corporate Memory.

The Client class provides the main interface for interacting with eccenca
Corporate Memory instances. It manages authentication, HTTP communication,
and provides access to various service components through lazy-loaded properties.

The client follows a lazy initialization pattern where components are only
created when first accessed, improving performance and reducing unnecessary
resource allocation.

**Attributes:**

- [**config**](#cmem_client.client.Client.config) (<code>[Config](config.md#cmem_client.config.Config)</code>) – Configuration object containing URLs and connection settings.
- **_headers** (<code>dict</code>) – Class-level dictionary of HTTP headers shared across instances.
- **_auth** (<code>[AuthProvider](auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code>) – Authentication provider for obtaining access tokens.
- **_http** (<code>Client</code>) – HTTP client instance for making API requests.
- **_workspace** (<code>[BuildWorkspace](components/workspace.md#cmem_client.components.workspace.BuildWorkspace)</code>) – DataIntegration workspace component for build operations.
- **_store** (<code>[GraphStore](components/graph_store.md#cmem_client.components.graph_store.GraphStore)</code>) – DataPlatform graph store component for explore operations.

**Functions:**

- [**configure_client_logger**](#cmem_client.client.Client.configure_client_logger) – Configure logging for the client's loggger and its decendants.
- [**configure_logging_from_dict**](#cmem_client.client.Client.configure_logging_from_dict) – Configure logging for the client.
- [**configure_logging_from_json**](#cmem_client.client.Client.configure_logging_from_json) – Configure logging for the client via a json file.
- [**from_cmempy**](#cmem_client.client.Client.from_cmempy) – Create a client instance configured from a cmempy environment.
- [**from_context**](#cmem_client.client.Client.from_context) – Create a client instance configured from a cmem-plugin-base context object.
- [**from_dict**](#cmem_client.client.Client.from_dict) – Create a client instance from a plain dictionary of configuration values.
- [**from_env**](#cmem_client.client.Client.from_env) – Create a client instance configured from environment variables.
- [**get_new_httpx_client**](#cmem_client.client.Client.get_new_httpx_client) – Create a new HTTP client instance with current configuration.

**Parameters:**

- **config** (<code>[Config](config.md#cmem_client.config.Config)</code>) – Configuration object containing base URLs, SSL settings,
and other connection parameters.
- **auth** (<code>[AuthProvider](auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider) | None</code>) – Optional authentication provider. If given, it is applied
through the ``auth`` setter (which fetches an access token and
prepares the HTTP client). If ``None``, an authentication
provider must be set before making authenticated requests.
- **logger** (<code>Logger | None</code>) – Optional Logger object for configuring logging.

### `access_conditions` {#cmem_client.client.Client.access_conditions}

```python
access_conditions: AccessConditionsRepository
```

Get the access conditions repository for managing DataPlatform authorization.

Returns: The access conditions repository instance, created lazy on first access.

### `auth` {#cmem_client.client.Client.auth}

```python
auth: AuthProvider
```

Get the current authentication provider.

Returns the authentication provider responsible for obtaining and
refreshing access tokens for API requests.

**Returns:**

- <code>[AuthProvider](auth_provider/abc.md#cmem_client.auth_provider.abc.AuthProvider)</code> – The currently configured AuthProvider instance.

**Raises:**

- <code>[ClientNoAuthProviderError](exceptions.md#cmem_client.exceptions.ClientNoAuthProviderError)</code> – If no authentication provider has been
set on this client instance.

<details class="note" open markdown="1">
<summary>Note</summary>

An authentication provider must be set before the client can make
authenticated API requests. Use Client.from_env() for automatic
configuration or set the auth property manually.

</details>

### `client_accounts` {#cmem_client.client.Client.client_accounts}

```python
client_accounts: ClientAccountRepository
```

Get the Keycloak OpenID Connect client accounts repository.

Returns the ClientAccountRepository for managing OpenID Connect client
accounts in the Corporate Memory Keycloak realm.

**Returns:**

- <code>[ClientAccountRepository](repositories/client_accounts.md#cmem_client.repositories.client_accounts.ClientAccountRepository)</code> – The ClientAccountRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> for client_account in client.client_accounts.values():
...     print(client_account.client_id)
```

### `config` {#cmem_client.client.Client.config}

```python
config: Config = config
```

Configuration object containing URLs, timeouts, and SSL settings.

### `configure_client_logger` {#cmem_client.client.Client.configure_client_logger}

```python
configure_client_logger(level='INFO', format_string=None, handlers=None, filename=None)
```

Configure logging for the client's loggger and its decendants.

**Parameters:**

- **level** (<code>str | int</code>) – Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) or int
- **format_string** (<code>str | None</code>) – Custom log format string
- **handlers** (<code>list[Handler] | None</code>) – List of custom handlers (if provided, overrides filename)
- **filename** (<code>str | Path | None</code>) – Path to log file (creates FileHandler if provided)

**Examples:**

```pycon
>>> client = Client.from_env()
>>> client.configure_client_logger(level="DEBUG")
>>> client.configure_client_logger(level="INFO", filename="cmem.log")
```

### `configure_logging_from_dict` {#cmem_client.client.Client.configure_logging_from_dict}

```python
configure_logging_from_dict(config)
```

Configure logging for the client.

**Parameters:**

- **config** (<code>dict[str, Any]</code>) – Dictionary of logging configuration

### `configure_logging_from_json` {#cmem_client.client.Client.configure_logging_from_json}

```python
configure_logging_from_json(json_config)
```

Configure logging for the client via a json file.

**Parameters:**

- **json_config** (<code>Path</code>) – Path to json configuration file

### `datasets` {#cmem_client.client.Client.datasets}

```python
datasets: DatasetsRepository
```

Get the DataIntegration (build) datasets repository.

Returns the DatasetsRepository for managing Corporate Memory datasets
within projects. Provides access to dataset listing, creation, update,
deletion, and file resource upload/download operations.

**Returns:**

- <code>[DatasetsRepository](repositories/datasets.md#cmem_client.repositories.datasets.DatasetsRepository)</code> – The DatasetsRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> client.datasets.fetch_data()
>>> for dataset in client.datasets.values():
...     print(dataset.get_id())
```

### `deployment` {#cmem_client.client.Client.deployment}

```python
deployment: Deployment
```

Get the deployment status component.

Returns the Deployment component for aggregating version and health
information across all Corporate Memory services.

**Returns:**

- <code>[Deployment](components/deployment.md#cmem_client.components.deployment.Deployment)</code> – The Deployment component instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> status = client.deployment.get_status()
>>> print(status.explore.version, status.health)
```

### `files` {#cmem_client.client.Client.files}

```python
files: FilesRepository
```

Get the files repository for managing files

Returns: The files repository instance, created lazy on first access.

### `from_cmempy` {#cmem_client.client.Client.from_cmempy}

```python
from_cmempy(logger=None)
```

Create a client instance configured from a cmempy environment.

### `from_context` {#cmem_client.client.Client.from_context}

```python
from_context(context, logger=None)
```

Create a client instance configured from a cmem-plugin-base context object.

This method is intended for use inside corporate memory python plugins.
It extracts connection URLs from the ``SystemContext`` and uses the token
provided by the ``UserContext`` for authentication, so no environment variables
or credentials need to be supplied manually.

**Parameters:**

- **context** (<code>object</code>) – An ``ExecutionContext`` or ``PluginContext`` instance from
``cmem-plugin-base``. Must expose a ``system`` attribute
(``SystemContext``) for URL discovery and a ``user`` attribute
(``UserContext``) for token retrieval.
- **logger** (<code>Logger | None</code>) – Optional Logger object for configuring logging.

**Returns:**

- <code>[Client](#cmem_client.client.Client)</code> – A fully configured Client instance authenticated via the token
- <code>[Client](#cmem_client.client.Client)</code> – provided by the context's ``UserContext``.

**Raises:**

- <code>ClientEnvConfigError</code> – If the base URL cannot be retrieved from the
context's ``SystemContext``.

**Examples:**

```pycon
>>> def execute(self, inputs, context):
...     client = Client.from_context(context)
...     packages = client.marketplace.get_available_packages()
```

### `from_dict` {#cmem_client.client.Client.from_dict}

```python
from_dict(data, logger=None)
```

Create a client instance from a plain dictionary of configuration values.

This factory method is intended for callers that manage their own
configuration (e.g. a config file with named environments) and want
to pass parsed values directly without relying on environment variables
or the cmempy library.

**Parameters:**

- **data** (<code>dict[str, str]</code>) – A flat dictionary whose keys mirror the environment variable
names used by ``from_env()`` (e.g. ``"CMEM_BASE_URI"``,
``"OAUTH_GRANT_TYPE"``, ``"OAUTH_CLIENT_SECRET"``).
- **logger** (<code>Logger | None</code>) – Optional Logger object for configuring logging.

**Returns:**

- <code>[Client](#cmem_client.client.Client)</code> – A fully configured Client instance with authentication provider
- <code>[Client](#cmem_client.client.Client)</code> – set from the supplied dictionary.

**Raises:**

- <code>ClientEnvConfigError</code> – If required keys are missing from ``data``.

**Examples:**

```pycon
>>> client = Client.from_dict({
...     "CMEM_BASE_URI": "http://docker.localhost",
...     "OAUTH_GRANT_TYPE": "password",
...     "OAUTH_CLIENT_ID": "cmemc",
...     "OAUTH_USER": "admin",
...     "OAUTH_PASSWORD": "admin",
... })
```

### `from_env` {#cmem_client.client.Client.from_env}

```python
from_env(logger=None)
```

Create a client instance configured from environment variables.

This factory method creates a fully configured client by reading
configuration and authentication settings from environment variables.
It's the recommended way to create clients in most applications.

**Parameters:**

- **logger** (<code>Logger | None</code>) – Optional Logger object for configuring logging.

**Returns:**

- <code>[Client](#cmem_client.client.Client)</code> – A fully configured Client instance with authentication provider
- <code>[Client](#cmem_client.client.Client)</code> – automatically set based on environment variables.

**Raises:**

- <code>ClientEnvConfigError</code> – If required environment variables are missing.

**Examples:**

```pycon
>>> my_client = Client.from_env()  # Uses CMEM_BASE_URI, OAUTH_* vars
>>> store_info = my_client.store.self_information
```

### `get_new_httpx_client` {#cmem_client.client.Client.get_new_httpx_client}

```python
get_new_httpx_client()
```

Create a new HTTP client instance with current configuration.

Creates a fresh httpx.Client instance configured with the current
headers, SSL verification settings, and timeout values from the
client configuration.

**Returns:**

- <code>Client</code> – A new httpx.Client instance ready for making HTTP requests.

<details class="note" open markdown="1">
<summary>Note</summary>

This method is called internally when the auth provider changes
or when the HTTP client needs to be refreshed with new headers.

</details>

### `graph_imports` {#cmem_client.client.Client.graph_imports}

```python
graph_imports: GraphImportsRepository
```

Get the graph imports repository for managing graph imports

Returns: The graph imports repository instance, created lazily on first access.

### `graph_insights` {#cmem_client.client.Client.graph_insights}

```python
graph_insights: GraphInsightsRepository
```

Get the Graph Insights repository for managing semspect snapshots.

Returns: The GraphInsightsRepository instance, created lazily on first access.

### `graphs` {#cmem_client.client.Client.graphs}

```python
graphs: GraphsRepository
```

Get the DataPlatform (explore) graph repository component.

Returns the GraphsRepository component for managing Corporate Memory's
DataPlatform graph repository for importing and exporting graph
files and manages their integration with the graph store.

**Returns:**

- <code>[GraphsRepository](repositories/graphs.md#cmem_client.repositories.graphs.GraphsRepository)</code> – The GraphRepository component instance, created lazily on first access.

**Examples:**

```pycon
>>> from pathlib import Path
>>> client = Client.from_env()
>>> graphs = client.graphs
>>> graphs.import_item(Path("backup.ttl"))
```

### `http` {#cmem_client.client.Client.http}

```python
http: httpx.Client
```

Get the HTTP client instance for making API requests.

Returns the configured HTTP client, creating it lazily on first access.
The client is pre-configured with authentication headers, SSL settings,
and timeout values.

**Returns:**

- <code>Client</code> – The httpx.Client instance configured for this client.

<details class="note" open markdown="1">
<summary>Note</summary>

The HTTP client is automatically recreated when the authentication
provider is changed to ensure headers are updated.

</details>

### `logger` {#cmem_client.client.Client.logger}

```python
logger: logging.Logger
```

Return the configured logger.

### `marketplace` {#cmem_client.client.Client.marketplace}

```python
marketplace: Marketplace
```

Get the DataPlatform (explore) marketplace component.

Returns the Marketplace component.

**Returns:**

- <code>[Marketplace](components/marketplace.md#cmem_client.components.marketplace.Marketplace)</code> – The Marketplace component instance, created lazily on first access.

### `marketplace_packages` {#cmem_client.client.Client.marketplace_packages}

```python
marketplace_packages: MarketplacePackagesRepository
```

Get the package repository for managing Corporate Memory's marketplace packages

Returns the package repository for managing Corporate Memory's
marketplace packages. This component handles marketplace packages
in a .zip format.

Returns: The marketplace package repository instance, created lazily on first access.

**Examples:**

```pycon
>>> from pathlib import Path
>>> client = Client.from_env()
>>> packages = client.marketplace_packages
>>> packages.import_item(key="w3c-geo-vocab")
```

### `projects` {#cmem_client.client.Client.projects}

```python
projects: ProjectsRepository
```

Get the DataIntegration (build) project repository component.

Returns the ProjectsRepository component to manage
DataIntegration projects, such as importing and exporting project
files.

**Returns:**

- <code>[ProjectsRepository](repositories/projects.md#cmem_client.repositories.projects.ProjectsRepository)</code> – The ProjectsRepository component instance, created lazily on first access.

**Examples:**

```pycon
>>> from pathlib import Path
>>> client = Client.from_env()
>>> projects = client.projects
>>> projects.import_item(Path("project.zip"))
```

### `python_packages` {#cmem_client.client.Client.python_packages}

```python
python_packages: PythonPackagesRepository
```

Get the package repository for managing python packages

Returns: The python package repository instance, created lazily on first access.

### `queries` {#cmem_client.client.Client.queries}

```python
queries: QueriesRepository
```

Get the DataPlatform (explore) queries repository.

Returns the QueriesRepository for accessing queries stored in the
Corporate Memory query catalog. Queries are fetched from RDF catalog
graphs and described using SHACL UI vocabulary.

**Returns:**

- <code>[QueriesRepository](repositories/queries.md#cmem_client.repositories.queries.QueriesRepository)</code> – The QueriesRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> queries = client.queries
>>> queries.fetch_data()
>>> my_query = queries.get(":myQueryId")
```

### `schedulers` {#cmem_client.client.Client.schedulers}

```python
schedulers: SchedulersRepository
```

Get the workflow schedulers repository.

Returns the SchedulersRepository for accessing workflow schedulers across
all Corporate Memory projects. Schedulers execute workflows at specified
intervals and are identified by a 'project_id:scheduler_id' composite key.

**Returns:**

- <code>[SchedulersRepository](repositories/schedulers.md#cmem_client.repositories.schedulers.SchedulersRepository)</code> – The SchedulersRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> for scheduler in client.schedulers.values():
...     print(scheduler.get_id())
```

### `store` {#cmem_client.client.Client.store}

```python
store: GraphStore
```

Get the DataPlatform (explore) graph store component.

Returns the GraphStore component for managing Corporate Memory's
DataPlatform graph store, including RDF graph operations, bootstrap
data management, and store-level backup/restore functionality.

**Returns:**

- <code>[GraphStore](components/graph_store.md#cmem_client.components.graph_store.GraphStore)</code> – The GraphStore component instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> store_info = client.store.self_information
>>> print(f"Store type: {store_info.type}, version: {store_info.version}")
```

### `user_accounts` {#cmem_client.client.Client.user_accounts}

```python
user_accounts: UserAccountRepository
```

Get the Keycloak user accounts repository.

Returns the UserAccountRepository for managing user accounts in the Corporate
Memory Keycloak realm. Provides CRUD operations on user accounts as well
as group assignment and password management.

**Returns:**

- <code>[UserAccountRepository](repositories/user_accounts.md#cmem_client.repositories.user_accounts.UserAccountRepository)</code> – The UserAccountRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> for user in client.user_accounts.values():
...     print(user.username)
```

### `validations` {#cmem_client.client.Client.validations}

```python
validations: ValidationsRepository
```

Get the repository for managing SHACL batch validation processes.

Returns: The ValidationsRepository instance, created lazily on first access.

### `variables` {#cmem_client.client.Client.variables}

```python
variables: VariablesRepository
```

Get the DataIntegration (build) variables repository.

Returns the VariablesRepository for managing project variables across all
Corporate Memory projects. Variables can hold static values or Jinja2 template
strings referencing other variables.

**Returns:**

- <code>[VariablesRepository](repositories/variables.md#cmem_client.repositories.variables.VariablesRepository)</code> – The VariablesRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> for variable in client.variables.values():
...     print(variable.get_id())
```

### `vocabularies` {#cmem_client.client.Client.vocabularies}

```python
vocabularies: VocabulariesRepository
```

Get the vocabulary catalog repository.

Returns the VocabulariesRepository for listing, installing, uninstalling,
and reading cache data for Corporate Memory vocabularies.

**Returns:**

- <code>[VocabulariesRepository](repositories/vocabularies.md#cmem_client.repositories.vocabularies.VocabulariesRepository)</code> – The VocabulariesRepository instance, created lazily on first access.

**Examples:**

```pycon
>>> client = Client.from_env()
>>> installed = client.vocabularies.list_vocabularies(filter_="installed")
```

### `workflows` {#cmem_client.client.Client.workflows}

```python
workflows: WorkflowsRepository
```

Get the workflows repository for managing workflows

Returns: The workflows repository instance, created lazily on first access.

### `workspace` {#cmem_client.client.Client.workspace}

```python
workspace: BuildWorkspace
```

Get the DataIntegration (build) workspace component.

Returns the BuildWorkspace component for managing Corporate Memory's
DataIntegration workspace, including projects, datasets, transformations,
and workspace-level import/export operations.

**Returns:**

- <code>[BuildWorkspace](components/workspace.md#cmem_client.components.workspace.BuildWorkspace)</code> – The BuildWorkspace component instance, created lazily on first access.

**Examples:**

```pycon
>>> from pathlib import Path
>>> client = Client.from_env()
>>> client.workspace.import_from_zip(Path("backup.zip"))
>>> client.workspace.export_to_zip(Path("new_backup.zip"))
```

### `workspace_configs` {#cmem_client.client.Client.workspace_configs}

```python
workspace_configs: WorkspaceConfigsRepository
```

Get the workspace configs repository for managing explore workspace configurations.

Returns: The workspace configs repository instance, created lazy on first access.

