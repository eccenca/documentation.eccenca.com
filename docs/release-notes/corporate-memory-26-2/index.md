---
status: new
tags:
    - ReleaseNote
---

# Corporate Memory 26.2.0

Corporate Memory 26.2 is the second major release in 2026. It introduces reusable rule blocks and execution variables in Build, a new Manage module and SHACL based resource authoring in Explore, ships eccenca Marketplace as a generally available component, and adds workspace status reporting to cmemc.

<!--
![26.2: Explore - Badges](26-1-explore-badges.png "26.1: Explore - Badges"){ class="bordered" }

![26.2: Explore - Resource Representation](26-1-explore-resources.png "26.1: Explore - Resource Representation"){ class="bordered" }

![26.2: Explore - Resource Table and Filter](26-1-explore-rt-filter.png "26.1: Explore - Resource Table and Filter"){ class="bordered" }

![26.2: Build - Target Schema Extraction](26-1-build-mapping-creator-target-schema.png "26.1: Build - Target Schema Extraction"){ class="bordered" width="80%"}

![26.2: Build - Mapping Creator AI Suggestions](26-1-build-mapping-creator-suggest.png "26.1: Build - Mapping Creator AI Suggestions"){ class="bordered"  width="90%"}
-->

The highlights of this release are:

- Build: **Reusable Rule Blocks, Execution Variables and Jinja for SPARQL**
    - Build introduces reusable transform rule blocks with a dedicated editor, execution variables that parameterize a single task or workflow run, Jinja as the default template engine for SPARQL tasks, and an embedded MCP server that opens the workspace to LLM agents.

- Explore: **Manage Module and Companion Authoring**
    - Explore adds a new Manage module for system state and administration, extends Companion with external MCP server integration and SHACL based resource creation, editing and validation, and refreshes SHACL authoring together with the underlying platform.

- Marketplace: **General Availability**
    - eccenca Marketplace ships as a generally available component for the first time: a package registry with a web application, a REST API for publishing and retrieving versioned packages, and direct installation of packages into a connected Corporate Memory.

- Automate: **Status Reporting and the Move to cmem-client**
    - cmemc adds project-wide and workspace-wide reporting of task loading errors, options to exclude user-identifying metadata from exports, and versioned marketplace package installation. It is now based solely on the cmem-client library.

This release delivers the following component versions:

- eccenca DataIntegration v26.2.0
- eccenca Explore v26.2.0
- eccenca Marketplace v26.2.4
- eccenca Corporate Memory Control (cmemc) v26.2.0
- eccenca Graph Insights v20.0.0

We tested this release with the following dependency components:

- Ontotext GraphDB v11.4.1
- Keycloak v26.6.4

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v26.2.0

We are excited to announce the release of DataIntegration v26.2, which brings reusable rule blocks, execution variables, Jinja templating for SPARQL tasks, an embedded MCP server for LLM agents, and a broad refresh of the platform, its operators and its execution reports.

**v26.2.0 of DataIntegration adds the following new features:**

- **Reusable rule blocks:**
    - Added project-level reusable transform rule block tasks together with a dedicated rule block editor.
    - Added logical input port management, persisted example values, and dedicated rule block evaluation.
    - Added the usage of reusable rule blocks in the transform and linking editors, evaluated as a black box by the outer rule.
    - Added a read-only modal that evaluates the internals of a rule block directly from a transform or linking usage node.
    - Added rule block support to the transform and linking evaluation views, including label lookup via the summary endpoint.
    - Added new API endpoints:
        - `GET /api/workspace/projects/:projectId/ruleBlocks` to fetch lightweight reusable rule block summaries for editor sidebars and labels.
        - `POST /api/workspace/projects/:projectId/tasks/:taskId/evaluateRuleBlock` to evaluate a posted rule block model against explicit example values.
- **Embedded MCP server:**
    - Added an embedded MCP (Model Context Protocol) server at `/mcp`, which exposes workspace inspection, authoring, and execution tools to LLM agents.
    - The server is enabled by default and can be disabled by setting `com.eccenca.di.assistant.McpConfig.enabled = false`; requests then return 404.
    - Only read-only tools are offered unless `com.eccenca.di.assistant.McpConfig.readOnly = false` is set, which also exposes the authoring, deletion, and execution tools.
- **Jinja templating for SPARQL tasks:**
    - Jinja is now the default template engine for SPARQL Update and SPARQL Select tasks and supports filters, conditionals, and iteration over entity value lists.
    - All transformer plugins are automatically available as Jinja filters, for example `{{ value | lowerCase }}`.
    - Global and project variables can be used in templates.
    - Added three new transformer plugins for SPARQL templating, which can also be used as Jinja filters:
        - `validate_uri` validates that the value is a valid absolute IRI and returns it unchanged or raises a validation error.
        - `escape_literal` escapes a value for use inside a SPARQL short-form string literal (backslashes, quotes, `\n`, `\r`, `\t`) without adding the enclosing quotes.
        - `escape_multiline_literal` escapes backslashes and breaks any run of three or more consecutive single or double quotes, so that the value is safe inside a triple-quoted SPARQL literal.
    - The SPARQL Select task supports reading input entities: the query template can reference `input.entity.<property>` and one query is generated per input entity.
    - Added the project-wide default RDF dataset setting `dataset.defaultRdf`. The SPARQL Select task can run against this default dataset without requiring a SPARQL endpoint connected to its input port.
    - The **Simple** and **Velocity Engine** template modes are deprecated in favour of Jinja; existing projects continue to work.
- **Execution variables:**
    - Added execution variables, which are defined on a task or workflow as defaults and are only available while its execution is running. They are referenced with the `execution.` prefix, e.g. `{{execution.myVariable}}`.
    - Added an **Execution variables** widget to the configuration view of a task or workflow. Their templates may reference global and project variables as well as execution variables defined earlier on the same task. Templates are resolved whenever the variables are saved (through the widget or with the task) and are re-resolved when a referenced project variable changes. The template editor of the widget validates, auto-completes, and previews `execution.` references.
    - Defaults can be overridden when triggering a workflow via the REST API under the `executionVariables` key, given as a name/value map with string values. Requests with any other value shape are rejected.
    - Overrides can alternatively be passed as query parameters with the reserved prefix `variable-`, e.g. `?variable-myVar=value`, which works for every request content type including GET requests.
    - Execution variables are included in the task JSON/XML/RDF serialization (`executionVariables` key / `ExecutionVariables` element). Full task updates (PUT) change them only when the entry is present in the payload: if it is absent, the stored variables stay untouched; if it is present, they are replaced, and an explicit empty list clears them.
    - Added a **Set execution variable** workflow operator and a **Set execution variable** transform operator (in the *Variables* category) that create or update execution variables while a workflow is running.
    - `GET /api/core/variableTemplate/variables` accepts a new `transitive` flag. If the requested task is a workflow, the response lists all variables that have to be set when running the workflow: its own execution variables plus those defined on every task that may take part in the execution, i.e. its operators and datasets, the tasks those tasks reference, and sub-workflows, recursively. If the same variable is defined on multiple levels, the variable of the enclosing workflow is returned, matching the value that applies when the workflow is executed.
- **Workflow operators and execution:**
    - Added a **JSON to File** operator that writes the JSON value held in a field on each entity to a file.
        - Supported output modes are one file per entity, a single ZIP archive, or all values merged into a single JSON array.
        - An optional output property wraps each written value under a key.
        - Invalid or empty input values are skipped and recorded as warnings on the execution report.
    - Extended the **Distinct by** operator:
        - Added strategies to keep the duplicate with the minimum or maximum value of a configurable compare path.
        - Multiple distinct paths can be provided (one per line); entities are deduplicated on the combination of their values.
    - Added a workflow scope option to the in-memory dataset.
        - It holds all data in memory, scoped to a single workflow execution, and stores the data separately for each workflow execution.
        - It can be used to store intermediate results of a workflow, isolated from other concurrent workflow executions.
    - Added a warning when a **Clear dataset** operator has no defined execution order relative to nodes writing to the same dataset, because such a clear may silently run after the writes.
- **Transform and linking rule operators:**
    - Added a **Per-value hash** transformer and renamed **Input hash** to **Combined input hash**.
    - Parameters that only accept a fixed set of values now offer a selection, others suggest known values:
        - **Aggregate numbers** and **Numeric operation** transformers: the operator parameter.
        - **Token-wise distance** and **Geographical distance** measures: the metric and unit parameters.
        - **Format number**, **Extract physical quantity**, and **Normalize physical quantity** transformers: the locale parameter suggests known language tags.
        - **Convert charset** and **Encode URL** transformers: the charset parameters suggest the charsets supported by the system.
        - RDF in-memory dataset: the format parameter offers the supported RDF formats.
- **Datasets:**
    - Neo4j: added a `batchSize` parameter to configure the number of entities that are written in a single Neo4j transaction. Clearing is now done in batches as well.
    - Added support for finding Knowledge Graph datasets in the workspace via absolute graph URI, even when the graph URI has a prefix.
    - S3 resource repositories: added authentication with an assumed IAM role via STS, configured with `targetRoleArn` and an optional `stsEndpointOverride`. If neither access key nor role is configured, the default AWS credentials provider chain is used, so a deployment can rely on a service account instead of access key and secret.
    - S3 resource repositories: added a `skipMetadata` option that skips loading file size and modification time when listing project files, which speeds up opening projects with many files.
- **Execution reports:**
    - Added authentication diagnostics to the workflow execution report.
    - The execution report JSON now carries an `operationType` field (`read`, `write`, or `process`) per report, complementing the free-text `operation` label.
- **User interface:**
    - Extended the task port schema in the workflow editor with a type description and path metadata (i18n label, value type). For paths from a vocabulary graph, a link to Explore is added.
    - Project files widget: added sortable columns for name, last modified, and size.
    - Added copy-to-clipboard support for entity and graph URIs.
    - Related plugins are now shown in the plugin description.
    - Added an AI disclaimer to the Mapping Creator UI.
- **API:**
    - Added a `/api/workspace/status` endpoint that reports the failed task reports of all projects, grouped by project, together with workspace-wide summary counts.
    - Added a `POST /api/workspace/vocabularies/lookup` endpoint for batch lookup of (potential) URIs from the global vocabulary cache.
    - Added a `workspace/projects/:projectId/prefixes/detailed` endpoint that returns project, workspace, and default prefixes separately.
- **Python plugin API:**
    - Python plugins can now be marked as deprecated.
    - Python plugins can now reference related plugins via `relatedPlugins`.

**v26.2.0 of DataIntegration introduces the following changes:**

- **Tasks and datasets:**
    - The input source of transform and linking tasks is now optional: tasks can be created without an input and receive their inputs by connecting them in a workflow. Executing such a task outside of a workflow fails with a clear error message.
    - Knowledge Graph dataset: the graph parameter may now be left empty; in that case, SPARQL queries run against the default graph.
    - JSON dataset: default entity URIs now use source positions in the form `L<line>C<column>`.
    - Excel function operators are now labeled with an **Excel** prefix, e.g. **Excel Int** instead of **Int**.
- **Templating and execution reports:**
    - Jinja templates no longer re-interpret template syntax contained in variable values: a value containing `{{...}}` or `{%...%}` is now rendered literally instead of being evaluated again. Use variable *templates* to compose variables from other variables.
    - Transform execution reports now give better explanations when no URI was generated.
- **Vocabularies and prefixes:**
    - The `updateGlobalVocabularyCache` endpoint now performs a general update of the global vocabulary cache.
        - The `iri` request parameter is now optional; without it, the cache only reconciles newly installed and uninstalled vocabularies.
        - The `iri` parameter accepts either a single IRI or an array of IRIs to additionally force-reload specific vocabularies.
        - Force-reload requests are checked against the list of installed vocabularies first, so requests for non-installed vocabularies no longer create empty cache entries.
    - `userPrefixes` are no longer imported from eccenca DataPlatform, as it does not return them anymore; only `installedPrefixes` are imported now.
    - Prefix management UI: editable project prefixes are now separated from read-only Explore and default prefixes.
- **Reusable rule blocks API:**
    - The transform and linking rule evaluation endpoints support an optional `includeRuleBlockInspection=true` parameter for reusable rule block snapshot metadata. This affects `POST /api/workspace/tasks/:project/:task/rule/:rule/evaluateRule`, `GET /api/workspace/tasks/:project/:task/referenceLinksEvaluated`, `POST /api/workspace/tasks/:project/:linkingTaskId/referenceLinksEvaluated`, and `POST /api/workspace/tasks/:project/:linkingTaskName/evaluateLinkageRule`.
    - When `includeRuleBlockInspection=true` is set, those evaluation responses are extended with reusable rule block snapshot metadata, and the two bare-array endpoints return an object wrapper instead of the legacy top-level array.
    - The default outer transform and linking evaluation of rule block usages stays a black box and no longer returns the internal rule block operator tree inline.
- **User interface:**
    - Dependent parameters in the create/update dialog are no longer cleared automatically, but highlighted instead.
    - The workflow and rule editors still allow undo/redo after saving: the last saved state can be loaded while keeping the undo/redo queues intact where possible.
    - Workflow editor: items in the sidebar are searchable by user-defined tags.
    - Mapping Creator now displays profiling data for RDF data inputs for the root type.
    - Mapping Creator: mapping suggestions are no longer limited to three target vocabularies. Instead, the vocabulary description sent to the model is limited by size, which is configurable via `maxVocabularyChars` (400000 characters by default).
    - The brand color is no longer used for GUI elements in Build and Explore.
- **Platform and dependencies:**
    - Java 25 is now the default Java version.
    - The Docker base image is now built on Red Hat Universal Base Image 10.
    - Upgraded Apache Spark to 4.2.0.
    - Upgraded the AWS S3 SDK to version 2.x and removed the unmaintained awsscala library in favour of the official SDK. See the *Migration Notes*.
        - The `connectionTTL` parameter in the S3 configuration section cannot be `-1` anymore but needs a value in seconds, e.g. `1800`.
        - `tcpKeepAlive` is obsolete for sync transfers; these connections end after the throughput is lower than 1 KB/s for too long.
        - Some S3 settings that are not explicitly overwritten may have new defaults, see the AWS documentation.
    - Files are now organized into separate directories by type (config, data, cache, logs). See the *Migration Notes*.
    - Upgraded React and Redux and removed deprecated dependencies.
    - **Python:**
        - Workflow plugins can now be executed in parallel.
        - The Python version is now 3.13.14.
        - The uv version is now 0.12.1.
        - The cmem-plugin-base version is now 4.20.0.
        - Workflows that are started from within a Python plugin refresh their access token reliably, so long-running workflows no longer fail with an expired token. A failed start reports the response body in addition to the HTTP status code.

**v26.2.0 of DataIntegration removes the following functionality:**

- Removed all legacy UIs that have been replaced.
- Removed the `outputPriority` property of workflow nodes.
    - Use dependency connections between workflow nodes to define an explicit execution order instead.
    - The property could not be set in the workflow editor and was already discarded whenever a workflow was saved there, so saved workflows are not affected.

**v26.2.0 of DataIntegration ships the following fixes:**

- **Transform and linking rule operators:**
    - The **DateTime** comparison metric now computes exact second distances; previously it assumed 30-day months and 365-day years, so different dates around month boundaries could be treated as equal.
    - The **Concatenate multiple values** transformer now removes duplicates when **Remove duplicates** is enabled; previously the option had no effect.
    - The **Substring** transformer no longer fails with an internal error on values shorter than the configured indices. It now reports a clear validation error or, if the indices are not required to be in range, returns an empty string.
    - The **Format number**, **Extract physical quantity**, and **Timestamp to date** plugins are now thread-safe; previously concurrent evaluation could return corrupted values or fail sporadically.
    - The **Token-wise distance** metric now computes stable incremental IDF token weights when executed in parallel; previously the weights could differ between runs.
    - The **Timestamp to date** transformer now renders custom date formats in UTC with a fixed locale; previously the output depended on the server timezone and locale.
    - The **Numeric operation** transformer now returns no value if any input is empty, instead of silently ignoring the empty input.
    - The **Remove stop words** transformers are now considerably faster on large inputs.
    - The **Remove remote stop words** transformer now downloads the stop word list on first use and with a timeout; previously every loading of the transform rule triggered a download that could hang indefinitely.
    - The normalized Levenshtein distance metric now treats two empty strings as equal; previously they were scored as a complete mismatch.
    - The **Geometric mean** aggregator now returns the lowest input score if any score is negative, so a definite mismatch no longer generates a link.
    - The **Euclidian distance** aggregator now treats negative input scores as 0, instead of squaring mismatches into match contributions.
    - The **Cosine** distance metric now treats malformed vector values as not matching, instead of aborting the linking execution.
    - The **Parse integer** transformer:
        - now parses large integers exactly; previously values with more than 16 digits lost precision, e.g. `1234567890123456789` became `1234567890123456768`.
        - now rejects values outside the 64-bit integer range instead of silently corrupting them; type discovery classifies such columns as decimal.
        - now parses independently of the server locale and rejects values with unparsed characters like `12abc`.
        - now rejects misplaced thousands separators like `1,00` instead of mis-parsing them as 100, and accepts an explicit plus sign.
        - now rounds negative half values away from zero, e.g. `-1.5` to -2.
    - Excel function operators no longer output whole number results with a trailing `.0`, e.g. `INT` now returns `2` instead of `2.0`.
- **Workflow execution and reports:**
    - Workflow execution report: when a dataset received multiple inputs (e.g. a clear instruction from the **Clear dataset** operator plus queries from the **SPARQL Update query** operator), all inputs were counted in a single report labeled after the last input (e.g. "2 update queries executed" instead of "1 update query executed"). Each write into a dataset now gets its own report entry, and the node in the workflow editor shows the total over all executions of the same kind (e.g. "20 entities written" for two writes of 10 entities each).
    - Workflow execution report: when a hierarchical entity schema (e.g. from a mapping with nested object rules) was read from a dataset, all types were mixed into a single inconsistent report. Each requested type now gets its own report entry that states the type and the requesting task.
    - The execution report of a failed nested workflow no longer loses its detail.
    - Transform execution reports now list a separate error entry for each object mapping's URI rule instead of merging or dropping them.
    - If the configured execution report directory is not accessible, a meaningful error is raised instead of a `NullPointerException`.
    - Stopping a scheduler while other activities were running left it stuck in the "Stopping..." state until all other activities finished.
- **Templating and variables:**
    - **Evaluate template** operator:
        - Variables from a scope (e.g. `{{project.myVar}}`) were required as input attributes, although their values are provided by the variable scope and not by the input.
        - The template editor and all other variable template editors now apply Jinja syntax highlighting.
        - The variables that a template uses are now determined correctly for complex expressions such as method calls or named arguments. Previously, such templates could be rejected as invalid or receive a wrong input schema and fail at execution time.
        - The template editor now reports references to non-existing global or project variables (e.g. `{{project.typo}}`) while typing, and no longer falsely reports variables that are only bound during execution (e.g. `entities` with full evaluation) as missing.
        - Variables from unknown scopes (e.g. the typo `{{projekt.myVar}}`) are now rejected when the operator or transform rule is saved, instead of failing at execution time.
        - Multi-valued variables can now be indexed in templates, e.g. `{{values[0]}}` or `{{values[-1]}}` for the last value.
        - Template parameters in the rule editor now underline syntax errors and references to non-existing variables while typing, like the task dialogs do.
        - With full evaluation enabled, the execution report always showed "0 templates generated" instead of counting the generated template.
    - Project variables that are referenced by an **Evaluate template** operator can no longer be deleted; the delete dialog shows and links the referencing tasks.
    - Template variable evaluation errors, e.g. a template referencing an undefined variable, were reported with status 500 instead of 400.
    - The first variable workflow run after a restart returned an empty output.
- **Datasets and files:**
    - **Neo4j:**
        - When writing entities where an object property had no value, all object properties following it were dropped for that entity.
        - When writing links with an inverse property configured, the inverse relationship was silently ignored; it is now created in addition to the forward relationship.
        - The source ignored the depth and limit parameters when retrieving types and paths; both are now honored.
        - Writing datatype properties whose URI has no matching project prefix failed with a Cypher syntax error.
        - A backtick in the configured node label or in a generated name broke the generated Cypher queries; names are now properly escaped.
    - S3 resource repositories: deleting a folder also deleted sibling resources whose name starts with the folder name, e.g. deleting `assets` also removed `assets2`.
    - Excel dataset: fixed an error when reading a sheet with a missing or empty header row.
    - JSON dataset: numbers are now retrieved in plain notation instead of scientific notation, e.g. `172800000` instead of `1.728E+8`. Scientific notation is only used if the plain notation would be excessively long.
    - The **Download file** task now fails on HTTP errors instead of downloading the error response.
    - Downloading project files whose name contains non-ASCII characters in decomposed unicode form, e.g. umlaut file names uploaded from macOS, no longer produces an invalid response header that made strict HTTP clients such as Python plugins fail.
    - Writing a single zip file to a dataset in a workflow now refreshes the caches of depending tasks.
    - File resource paths that point outside a project's resource directory are now rejected on all operations, including deletion.
    - The **Parse JSON** operator now fails with a clear error when it is connected directly to a dataset, instead of silently writing nothing.
- **Queries and paths:**
    - Path filters using the `>=` or `<=` comparison operators are now parsed correctly.
    - SPARQL Update tasks now execute their queries in the original order instead of reversing each buffered batch.
    - A URI that starts with `<` but is missing the closing `>` is now reported as invalid instead of silently dropping its last character.
    - SPARQL Update queries are now terminated with a semicolon automatically before they are batched; a template without a trailing `;` previously produced an invalid batch that failed with an opaque parse error.
    - SPARQL restrictions that contain semicolons are now parsed correctly.
    - The **SPARQL Update query** operator no longer requires an input port if its template only uses `$outputProperties`; those values come from the connected output task.
- **Mapping and rule editors:**
    - Requesting mapping suggestions for a transformation whose input is not a dataset now shows a clear error message instead of a misleading "Task not found" error.
    - Requesting transformation examples for an object mapping rule no longer fails with an internal server error; the generated entity URIs are returned as examples.
    - Target vocabulary selection: installed vocabularies were incorrectly shown with a "not installed" warning after selecting them.
    - Changing only the (already existing) language tag of a value mapping rule is now recognized as a change and can be saved.
    - Angle brackets are now removed from already formatted target properties in the mapping editor.
    - Values in the transform and linking evaluation view can now be selected and copied.
    - Undo/redo via hot keys now works in auto-completion enabled inputs, e.g. template input, rule editor input path operators, and mapping rule path inputs.
- **Workflow editor:**
    - The node execution state is now reset immediately when a workflow is started (again).
    - Workflow nodes created with the "Connect to newly created..." handle menu action now have the complete node menu.
    - Dependency connections can no longer be made via drag and drop to task nodes that do not allow a dependency output.
    - Removing a dataset from the workflow canvas now also removes its **Allow replacement** flag, and workflows no longer keep the flag of removed datasets.
- **Other user interface fixes:**
    - Page numbers and page size are now displayed in the project file list.
    - Renamed the **Create** button in the navigation to **Create new** to improve accessibility.
    - Fixed the display of property value pairs in small containers of project variables.
- **Authentication and configuration:**
    - **OAuth:**
        - The refresh token is now only replaced when the OAuth provider returns a new one.
        - Built CSRF protection into the code flow.
        - The redirect URI is now taken from the session state instead of the callback state.
        - The token type is now checked to be a bearer token, otherwise the request fails with an error message.
        - A warning is logged at application start if insecure, non-TLS URLs are used for any OAuth related service URLs.
        - Deprecated (mis-)using the `state` query parameter for post login redirect URLs. Use `postLoginUrl` instead.
    - Startup now fails if OAuth is enabled (`eccencaDataPlatform.oauth = true`) but `eccencaDataPlatform.url` is not configured, instead of silently disabling authentication.
    - Uploading a file to a graph now fails with an error if the request keeps being unauthorized, instead of reporting success without uploading anything.
    - Deleting a graph that repeatedly fails with a server error now reports the error instead of silently leaving the old data in place.
    - Overriding a setting in `dataintegration.conf` now also updates the settings derived from it, e.g. setting `directories.base` moves the data, cache, and log directories along with it.
    - The `profiling.rdfSerialization.enabled` setting now controls the RDF profiling output; previously it was ignored and the output was controlled by `profiling.cache.enabled` instead.

## eccenca Explore v26.2.0

We are pleased to announce the release of Explore v26.2, which introduces the new Manage module, extends Companion with external MCP servers and SHACL based resource authoring, improves SHACL editing and chart handling, and ships a broad platform refresh.

**v26.2.0 of Explore adds the following new features:**

- **Manage:**
    - Added a new **Manage** module that provides a consolidated view of the current system state together with administration options.
- **Companion:**
    - Added support for integrating external MCP servers.
        - External MCP servers are configured via the Spring AI MCP client configuration.
        - Corporate Memory servers that use the same realm authentication are configured via dedicated properties (`spring.ai.mcp.client.cmem.*`).
    - Added an MCP server metadata provider.
    - Added support for creating and editing resources based on SHACL shapes.
    - Added support for SHACL validation of resources.
- **Charts:**
    - Added support for query placeholders in charts.

**v26.2.0 of Explore introduces the following changes:**

- **Business Knowledge Editor (BKE):**
    - The BKE edge components now use `RdfResource`.
    - Limited the set of connectable nodes.
- **SHACL:**
    - Markdown literals can now be edited in the Markdown editor.
    - The node shape selector now shows the `shacl:name` and falls back to the title.
    - OWL annotation properties can now be selected as path for property shapes.
    - Property shape: selecting **Show more** now shows more items.
    - The SHACL view now provides SPARQL syntax highlighting.
    - Resources added in the simple view now also update their links.
    - Shacline: badges are now placed on top of the group header.
- **Query Catalog:**
    - The query catalog now supports the DataIntegration variable placeholder syntax.
- **Graph Insights:**
    - Updated Graph Insights to v20.0.0.
- **Other:**
    - The graph list now highlights the current graph.
    - Improved data update handling in the UI.
    - Added a setting for the resolution of titles, descriptions, and depictions over all graphs.
    - The Explore backend now builds on Java 25 and Gradle 9.x.
    - Upgraded to Spring Boot 4.1 and Spring AI 2.0.
    - Upgraded Apache Jena to 6.2.0.

**v26.2.0 of Explore ships the following fixes:**

- **SHACL:**
    - The **Open Node Shape** button is now hidden if the default graph is configured, including in the application view.
    - Adjusted the markdown in the tooltip for property shape labels.
    - Values in a select list are now sorted according to the selectable resources query.
    - SPARQL constraints are now evaluated when creating a resource.
- **Charts:**
    - Reading charts in shaped views no longer requires the dedicated chart action.
    - Chart deletion now shows a notification if the deletion fails.
    - Assisted form: added a clearance button to the **Group by** and **Stack** fields.
    - The "Unsaved changes" warning no longer triggers when there are no unsaved changes.
- **Business Knowledge Editor (BKE):**
    - The label of a resource is now shown even if the resource is not in the current graph.
- **Other:**
    - Fixed issues with absolute logout redirect URIs.
    - The initial login into Build now uses the updated `postLoginUrl` parameter.
    - Query resources (`shui:SelectQuery`, `shui:UpdateQuery`) now have a context menu entry for managing them in the query catalog.
    - Badge values are now rendered.
    - Depiction resolving now takes more strategies into account:
        - If a resource is an explicit OWL/RDFS class, the depictions of applicable node shapes are taken into account.
        - If a resource is an implicit OWL/RDFS class and is targeted by a node shape, its depiction is taken into account.
    - Navigation queries now consider complex OWL classes as subclasses. The documentation for using navigation and badge queries has been extended accordingly.
    - Fixed language identification.
    - The health check towards GraphDB is now resilient to dirty disconnects.
    - Project access control: users could see workflows they do not have access to.
    - Fixed parallelism issues in some cases of HTTP store access.
        - Added the new property `store.httpStoreParallelism` to control the number of parallel requests to the HTTP store backend (default: `16`).
    - Long labels are now displayed better in the thesaurus.
    - Refactored queued RTK queries.

## eccenca Marketplace v26.2.4

We are excited to announce the release of eccenca Marketplace v26.2. The Marketplace is a package registry for Corporate Memory: it stores and serves versioned packages, validates their manifests and archives, and installs them into a connected Corporate Memory instance. Corporate Memory 26.2 is the first platform release that ships this component as generally available.

**v26.2.4 of Marketplace introduces the following changes:**

- `ROOT_PATH` now actually serves the application under the configured prefix.
    - The application mounts itself there, so all routes, the API docs, the static files, and the OIDC endpoints live below the prefix, and requests without it are answered with `404`. `GET /` redirects into the application.
    - The reverse proxy has to forward the prefix intact, i.e. without rewriting it, and the docker entrypoint no longer passes uvicorn's `--root-path`, which would strip the prefix before the mount matches.
    - The OIDC redirect URI moves with the prefix, so `<base-url><root-path>/auth/callback` needs to be registered in Keycloak.
    - The served `openapi.json` declares the prefix in `servers` and keeps its paths prefix-free, so the generated frontend client stays independent of the deployment path.
- `/.well-known/openid-configuration` is served below the prefix as well, e.g. as `/marketplace/.well-known/openid-configuration`.
    It is no longer answered at the bare host root, which on a shared host belongs to Corporate Memory.
- The default `ROOT_PATH` is now `/` (was `/marketplace`), which makes a sub-path deployment opt-in and matches what the docker entrypoint used to default to.
- An empty `ROOT_PATH`, e.g. an unset `${VAR}` in a docker compose file, is now read as `/` instead of failing at startup, while a value that cannot be mounted (query, fragment, whitespace, empty, `.` or `..` segments) is rejected.

**v26.2.4 of Marketplace ships the following fixes:**

- A root deployment no longer emits the protocol-relative `<base href="//">` and no longer builds login redirects with a doubled slash (`//auth/login`), which browsers resolve as a host.
    The post-login `next` target is now confined to the deployment, so a target pointing outside the prefix returns to the application root.
- The frontend no longer concatenates a remote marketplace URL and an API path without a separator, so remote marketplaces served under a sub-path are addressed correctly.

**v26.2.3 of Marketplace adds the following new features:**

- Added support for custom CA certificates.
    - `*.crt` and `*.pem` files mounted at `/custom-cacert` are merged with the certifi bundle when the container starts, so self-signed Keycloak, Corporate Memory, and remote marketplace endpoints work.
    - The result is written to `/tmp/pythoncacerts`, which can be overridden with `CA_BUNDLE_FILE`.
- Added the `ECC_MARKETPLACE_SSL_VERIFY` setting, which is also readable as the unprefixed `SSL_VERIFY`.
    - Set it to `false` to skip TLS certificate verification on all outgoing requests, i.e. the Keycloak well-known, JWKS, and token refresh requests, the OIDC login flow, remote marketplaces, and Corporate Memory.
    - This is meant for development only and defaults to `true`.

**v26.2.3 of Marketplace introduces the following changes:**

- The `https://eccenca.market` deployment now also uses the `LICENSE_TOKEN` mode.
- Updated cmem-client and trivy.

**v26.2.2 of Marketplace adds the following new features:**

- Added the `ECC_MARKETPLACE_LICENSE_TEXT` setting, which configures the license as a string, either as a raw multi-line `.asc` value or base64 encoded, instead of mounting a file via `ECC_MARKETPLACE_LICENSE_FILE`. It takes precedence when both are set.

**v26.2.2 of Marketplace ships the following fixes:**

- The secrets `license_text`, `session_secret`, and `keycloak_client_secret` are now masked in the settings dump that is logged at startup.

**v26.2.1 of Marketplace introduces the following changes:**

- Updated cmem-client to the latest version.

**v26.2.0 of Marketplace is the first generally available release and provides the following capabilities:**

- **Web application:**
    - A single-page web application with package list and package detail views, including filtering and pagination.
    - The application is delivered as static assets by the service itself, so no separate web server is required.
    - It supports internationalization, light and dark theming, and the selection of the marketplace to browse.
    - Serving the web application can be disabled with the `FRONTEND` setting.
- **Package management API:**
    - `GET /api/packages` lists all packages with their metadata, with filtering by `package_type`, `name`, and `tags`.
    - `GET /api/packages/paginated` provides the same list in a paginated form.
    - `GET /api/packages/{package}` retrieves the metadata of a single package, including license, comment, agents, URLs, tags, and languages.
    - `DELETE /api/packages/{package}` deletes a package and all its versions. This requires administrative permissions.
- **Package version management API:**
    - `GET /api/packages/{package}/versions` lists the available versions of a package.
    - `POST /api/packages/{package}/versions` uploads a new package version as a ZIP archive. This requires administrative permissions.
    - `GET /api/packages/{package}/versions/{version}` downloads a package version archive.
    - `DELETE /api/packages/{package}/versions/{version}` deletes a specific version. This requires administrative permissions.
    - Additional endpoints retrieve the full manifest of a version, list its declared files and dependencies, and download a single file either by path or by role (`readme`, `license`, `changelog`, `icon`, `marketplace`).
- **Validation tools API:**
    - `GET /api/manifest` retrieves the JSON schema of a valid package manifest.
    - `POST /api/manifest` validates a package manifest and `POST /api/archive` validates a full package version ZIP archive. Both require administrative permissions.
    - Manifests support language tags.
- **Corporate Memory integration API:**
    - `GET /api/cmem/packages/list` lists the packages installed in the connected Corporate Memory.
    - `POST /api/cmem/packages/install/from-marketplace` installs a marketplace package version into Corporate Memory. The marketplace to install from is restricted to the configured marketplace URLs and defaults to the first configured marketplace.
    - `POST /api/cmem/packages/install/from-file` installs a package into Corporate Memory from an uploaded archive.
    - `POST /api/cmem/packages/uninstall` uninstalls a package from Corporate Memory.
    - The API group is only registered when the Corporate Memory connection settings are configured, and it forwards the bearer token of the caller to Corporate Memory.
- **Badges:**
    - `GET /api/packages/{package}/badge` and `GET /api/packages/{package}/versions/{version}/badge` render SVG badges for embedding in package READMEs.
    - The `kind` query parameter selects the badge content: `version` (the default), `type` for the package type, and `license` for the SPDX license identifier.
    - Badges carry the eccenca logo and brand colours and are rendered fully offline, so they also work in air-gapped and on-premises setups.
    - The endpoints are public and unauthenticated, consistent with the other metadata endpoints. Unknown or malformed packages and versions render a "not found" badge with HTTP 200 instead of a 404, so an embedded image always renders.
- **Authentication and authorization:**
    - Browser login via Keycloak using the OIDC authorization code flow, so users no longer need to supply a bearer token manually. `GET /auth/login` and `GET /auth/callback` run the code flow and open a signed session cookie, `GET /auth/logout` clears the session.
    - Protected requests authenticate either from a bearer token, for API clients, or from the browser session, with transparent token refresh. Unauthenticated browser requests are redirected to the login.
    - Authorization is group-based: write and delete endpoints are restricted to the configured administrator group.
- **Licensing:**
    - A licenses endpoint at `GET /api/licenses`.
    - The hosted `marketplace.eccenca.dev` deployment runs with license authorization enabled.
- **Deployment and configuration:**
    - A multi-architecture Docker image based on the Red Hat Universal Base Image 10.
    - A file-based package repository with persistent storage.
    - Configuration via environment variables with the `ECC_MARKETPLACE_` prefix, including the Keycloak connection, the session secret, the list of marketplace URLs, and the Corporate Memory endpoints.
    - `ROOT_PATH` supports running the service behind a reverse proxy under a sub-path. The default changed with v26.2.4, see the changes above.
    - The storage and retrieval of packages on the local marketplace can be disabled with the `LOCAL_MARKETPLACE` setting, which also disables the corresponding session capabilities.

## eccenca Corporate Memory Control (cmemc) v26.2.0

We are excited to announce the release of cmemc v26.2, which adds status reporting for task loading errors, privacy-aware exports and versioned package installation, and completes the migration of the command line interface to the cmem-client library.

**v26.2.0 of cmemc adds the following new features:**

- `project status` command
    - Added a command to show the task loading errors of projects.
    - Added the `--all` option to check all projects and the `--exit-1` option to fail on loading errors.
- `admin status` command
    - The command now reports task loading errors across all projects.
    - It uses the bulk `workspace/status` endpoint, i.e. a single request, and prints one summary line per affected project.
    - `project status --all` uses the same bulk endpoint instead of one request per project.
- `project export` and `admin workspace export` commands
    - Added the `--without-userdata` option to exclude user-identifying metadata, i.e. creation and modification timestamps and account names, from the export.
- `package export` command
    - User-identifying metadata is now excluded from the exported project archives.
- `package install` command
    - Added the `--version` option to install a specific version from the marketplace.
    - Shell completion lists the available versions when a package ID is provided.

**v26.2.0 of cmemc introduces the following changes:**

- Migration to cmem-client
    - cmemc is now based solely on cmem-client; the cmem-cmempy dependency was removed.
    - The API client is composed from the resolved connection configuration instead of the environment, so ambient environment variables can no longer leak into the client when a named connection (`-c`) is active. See the migration notes.
    - Migrated all subcommands of the following command groups from cmempy to cmem-client:
        - `admin acl` (`list`, `delete`, `create`, `export`, `import`, `inspect`, `update`, `review`)
        - `admin client` (`list`, `secret`, `open`), including the `client_ids` tab-completion
        - `admin user` (`list`, `create`, `update`, `delete`, `password`, `open`)
        - `admin store` (`bootstrap`, `showcase`, `export`, `import`)
        - `admin workspace python`
        - `graph validation` (`execute`, `list`, `inspect`, `cancel`, `export`)
        - `graph insights` (`list`, `create`, `delete`, `inspect`)
        - `vocabulary` (`list`, `install`, `uninstall`, `open`, `import`, `cache update`, `cache list`), which no longer uses the removed `/api/vocabs` endpoints
        - `workflow` (`list`, `execute`, `io`, `status`, `open`)
    - Migrated the `admin status` and `admin metrics` commands.
    - Migrated the `MigrationRecipe` base class and all migration recipes. Migration recipes now receive the connected client injected from the command.
    - Migrated the shared helpers (`get_graphs`, `get_query_text`, `GraphLink`, `ResourceLink`, `TitleHelper`) and inject the connected client into them. They are used by the `query`, `graph`, `graph imports`, `graph insights`, `admin acl`, and `graph validation` commands.
    - Removed the cmempy dependency from the `WorkflowLink` string processor.
    - `graph delete` and `graph import` refresh access conditions via cmem-client after access condition graph changes.
- `graph export` command
    - `--include-imports` now resolves `owl:imports` in the graph store when exporting to a file or to stdout.
        - This needs one request per selected graph instead of one request per graph in the import closure.
        - Exporting to `--output-dir` is unchanged and still resolves the import closure client side, as each graph needs its own `.ttl`/`.graph` pair.
- `vocabulary` command group
    - `vocabulary import` now validates `vann:preferredNamespacePrefix` and `vann:preferredNamespaceUri` in the imported file.
    - `vocabulary import`: re-importing an existing vocabulary without `--replace` now correctly exits with an error.
    - `vocabulary install` and `vocabulary uninstall` show a deprecation note, as the vocabulary catalog is removed from Corporate Memory 26.2 onwards. `vocabulary install` throws an error if no vocabulary catalog is available.
- `workflow list` command
    - The `--raw` output now includes the additional fields `variableInputs`, `variableOutputs`, `tags`, `warnings`, and `projectLabel`, sourced from the task search API.
- Docker image
    - Switched to the ubi10/ubi-minimal base image.

**v26.2.0 of cmemc deprecates the following functionality:**

- `vocabulary` command group
    - `vocabulary install` is deprecated, as the vocabulary catalog is not part of Corporate Memory 26.2 and higher.
    - `vocabulary uninstall` is deprecated, as the vocabulary catalog is not part of Corporate Memory 26.2 and higher.

**v26.2.0 of cmemc ships the following fixes:**

- `package install` and `package uninstall` commands
    - `--ignore-lock` now releases the package lock file when the top-level operation finishes, so a stale lock left behind by an interrupted run no longer blocks subsequent commands.
- `admin metrics` command
    - Fixed the tab completion: the `--id` and `--filter` completers no longer fail silently when `ctx.obj` is unset.
- Fixed the `eccenca-marketplace-client` imports, as they are now part of cmem-client.

## Migration Notes

!!! info "Backward and Forward Compatibility"

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v26.2.0 into DataIntegration v26.1.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v26.1.0 can be imported into DataIntegration v26.2.0.

### eccenca DataIntegration

- **Directory layout:** Files are now organized into separate directories by type below a common base directory.
    - `config` for configuration files
    - `data` for project data
    - `cache` for cache files
    - `logs` for log files
    - If you run the application with custom directory settings, you may need to move existing files into the new layout or adjust the `directories` configuration accordingly.
    - For local installations, the `MigrateDirectories` script (in `app/scripts`) can move files from the old `elds.home` based layout to the new directories. Run it with `--dry-run` first to preview the changes.
    - If you use the provided Docker orchestration or the HELM charts, no action is required: they have already been updated to the new directory layout.

    This change was pre-announced with the v26.1 release notes.

- **Internal datasets:** The internal datasets have been deprecated. Use either the new in-workflow dataset or the in-memory dataset instead.
    - The default for the new `workflowScoped` parameter of the in-memory dataset is `true`. Existing in-memory datasets created before this change have this parameter unset and will therefore pick up the new default after upgrading.
    - To preserve the previous application-scoped behaviour, i.e. data shared across workflow executions and persisting for the lifetime of the process, set `workflowScoped = false` on those datasets after migration.
- **S3 configuration:** The `connectionTTL` parameter no longer accepts `-1` and needs a value in seconds, e.g. `1800`.
    See the AWS S3 SDK entry in the changes section above for further behaviour changes.
- **Templating:** The `Simple` and `Velocity Engine` template modes of SPARQL tasks are deprecated in favour of Jinja, which is now the default template engine. Existing projects continue to work.
- **Workflow nodes:** The `outputPriority` property of workflow nodes has been removed.
    Use dependency connections between workflow nodes to define an explicit execution order instead.

### eccenca Explore

- The default configuration of the graph tabs changed: the **Vocabularies** tab now excludes vocabularies marked with `shui:isSystemResource`.

### eccenca Marketplace

- eccenca Marketplace is shipped as a generally available component for the first time with this release, so there is no migration path from an earlier Corporate Memory version.
- Access to the hosted marketplaces requires license authorization.
    Provide the license either as a file via `ECC_MARKETPLACE_LICENSE_FILE` or as a string via `ECC_MARKETPLACE_LICENSE_TEXT`, which takes precedence when both are set.
- The `ECC_MARKETPLACE_CMEM_INSTALLATION_GROUP` setting has been removed and will be replaced by actions.
- **Sub-path deployments:** With v26.2.4 the application mounts itself below `ROOT_PATH` instead of only being aware of the prefix.
    The default is now `/` (was `/marketplace`), so a deployment that relied on the previous default has to set `ROOT_PATH=/marketplace` explicitly.
    Upgrading a sub-path deployment, e.g. `ROOT_PATH=/marketplace`, requires three changes:

    - The reverse proxy has to forward the prefix intact, i.e. without stripping or rewriting it.
    - uvicorn must not be given `--root-path`, since it would strip the prefix before the mount matches. The shipped docker entrypoint already dropped it.
    - `<base-url>/marketplace/auth/callback` has to be re-registered as a valid redirect URI in Keycloak.

### cmemc

**v26.2.0 of cmemc changes the following behaviour:**

- The vocabulary catalog is not part of Corporate Memory 26.2 and higher.
    The `vocabulary install` and `vocabulary uninstall` commands are deprecated and show a deprecation note.
    `vocabulary install` fails with an error if no vocabulary catalog is available.
- cmemc is now based solely on cmem-client.
    The API client is composed from the resolved connection configuration instead of the environment, so ambient environment variables no longer leak into the client while a named connection (`-c`) is active.
    Scripts that mix a named connection with environment variable overrides need to be adjusted.
