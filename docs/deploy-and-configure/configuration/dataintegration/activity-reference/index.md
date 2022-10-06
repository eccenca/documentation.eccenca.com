---
tags:
    - Reference
---
<!-- Auto-Generated. Do not edit directly! -->

# Activity Reference

## Project Activities

The following activities are available for each project.

#### Dataset matcher

Generates matches between schema paths and datasets based on the schema discovery and profiling information
         of the datasets.
      

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| datasetUri | String | If set, run dataset matching only for this particular dataset. |

The identifier for this plugin is `DatasetMatcher`.

It can be found in the package `com.eccenca.di.datamatching`.



## Task Activities

The following activities are available for different types of tasks.

### Custom

#### Execute REST Task

Executes the REST task.

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteRestTask`.

It can be found in the package `com.eccenca.di.workflow.operators.rest`.



### Dataset

#### Dataset profiler

Generates profiling data of a dataset, e.g. data types, statistics etc.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| datasetUri | String | Optional URI of the dataset resource that should be profiled. If not specified an URI will be generated. |
| uriPrefix | String | Optional URI prefix that is prepended to every generated URI, e.g. property URIs for every schema path.  If not specified an URI prefix will be generated. |
| entitySampleLimit | String | How many entities should be sampled for the profiling. If left blank, all entities will be considered. |
| timeLimit | String | The time in milliseconds that each of the schema extraction step and profiling step should spend on. Leave blank for unlimited time. |
| classProfilingLimit | int | The maximum number of classes that are profiled from the extracted schema. |
| schemaEntityLimit | int | The maximum number of overall schema entities (types, properties/attributes) that will be extracted. |
| executionType | String | The execution type to be used: SPARK, LEGACY. The legacy execution uses large in-memory maps and takes longer! |

The identifier for this plugin is `DatasetProfiler`.

It can be found in the package `com.eccenca.di.profiling`.



#### SQL endpoint status

Shows the SQL endpoint status.

This plugin does not require any parameters.
The identifier for this plugin is `SqlEndpointStatus`.

It can be found in the package `com.eccenca.di.sql.endpoint.activity`.



#### Types cache

Holds the most frequent types in a dataset.

This plugin does not require any parameters.
The identifier for this plugin is `TypesCache`.

It can be found in the package `org.silkframework.workspace.activity.dataset`.



### LinkSpecification

#### Active learning

Executes an active learning iteration.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| fixedRandomSeed | boolean | No description |

The identifier for this plugin is `ActiveLearning`.

It can be found in the package `org.silkframework.learning.active`.



#### Evaluate linking

Evaluates the linking task by generating links.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| includeReferenceLinks | boolean | Do not generate a link for which there is a negative reference link while always generating positive reference links. |
| useFileCache | boolean | Use a file cache. This avoids memory overflows for big files. |
| partitionSize | int | The number of entities in a single partition in the cache. |
| generateLinksWithEntities | boolean | Generate detailed information about the matched entities. If set to false, the generated links won't be shown in the Workbench. |
| writeOutputs | boolean | Write the generated links to the configured output of this task. |
| linkLimit | int | If defined, the execution will stop after the configured number of links is reached.\This is just a hint and the execution may produce slightly fewer or more links. |
| timeout | int | Timeout in seconds after that the matching task of an evaluation should be aborted. Set to 0 or negative to disable the timeout. |

The identifier for this plugin is `EvaluateLinking`.

It can be found in the package `org.silkframework.workspace.activity.linking`.



#### Execute linking

Executes the linking task using the configured execution.

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteLinking`.

It can be found in the package `org.silkframework.workspace.activity.linking`.



#### Linking paths cache

Holds the most frequent paths for the selected entities.

This plugin does not require any parameters.
The identifier for this plugin is `LinkingPathsCache`.

It can be found in the package `org.silkframework.workspace.activity.linking`.



#### Reference entities cache

For each reference link, the reference entities cache holds all values of the linked entities.

This plugin does not require any parameters.
The identifier for this plugin is `ReferenceEntitiesCache`.

It can be found in the package `org.silkframework.workspace.activity.linking`.



#### Supervised learning

Executes the supervised learning.

This plugin does not require any parameters.
The identifier for this plugin is `SupervisedLearning`.

It can be found in the package `org.silkframework.learning.active`.



### Scheduler

#### Activate

Executes the scheduler

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteScheduler`.

It can be found in the package `com.eccenca.di.scheduler`.



### ScriptTask

#### Execute Script

Executes the script.

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteScript`.

It can be found in the package `com.eccenca.di.scripting.scala`.



### TransformSpecification

#### Execute transform

Executes the transformation.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| limit | IntOptionParameter | Limits the maximum number of entities that are transformed. |

The identifier for this plugin is `ExecuteTransform`.

It can be found in the package `org.silkframework.workspace.activity.transform`.



#### Transform paths cache

Holds the most frequent paths for the selected entities.

This plugin does not require any parameters.
The identifier for this plugin is `TransformPathsCache`.

It can be found in the package `org.silkframework.workspace.activity.transform`.



#### Target vocabulary cache

Holds the target vocabularies

This plugin does not require any parameters.
The identifier for this plugin is `VocabularyCache`.

It can be found in the package `org.silkframework.workspace.activity.transform`.



### Workflow

#### Execute locally

Executes the workflow locally.

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteLocalWorkflow`.

It can be found in the package `org.silkframework.workspace.activity.workflow`.



### WorkflowExecution

#### Generate Spark assembly

Generate project and Spark assembly artifacts and deploy them using the specified configuration settings: type, artifact and options like destination in case of a simple copy

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| executeStaging | boolean | Execute loading phase |
| executeTransform | boolean | Execute transform phase |
| executeLoading | boolean | Execute staging phase |

The identifier for this plugin is `DeploySparkWorkflow`.

It can be found in the package `com.eccenca.di.spark`.



#### Default execution

Executes a workflow with the executor defined in the configuration

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteDefaultWorkflow`.

It can be found in the package `com.eccenca.di.spark`.



#### Execute operator

Executes a workflow on with an executor that uses Apache Spark. Depending on the Spark configuration it can still run on a single local machine or on a cluster.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| operator | TaskReference | The workflow to execute. |

The identifier for this plugin is `ExecuteSparkOperator`.

It can be found in the package `com.eccenca.di.spark`.



#### Execute on Spark

Executes a workflow on with an executor that uses Apache Spark. Depending on the Spark configuration it can still run on a single local machine or on a cluster.

This plugin does not require any parameters.
The identifier for this plugin is `ExecuteSparkWorkflow`.

It can be found in the package `com.eccenca.di.spark`.



#### Execute with payload

Executes a workflow with custom payload.

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| configuration | MultilineStringParameter | No description |
| configurationType | String | No description |

The identifier for this plugin is `ExecuteWorkflowWithPayload`.

It can be found in the package `org.silkframework.workbench.workflow`.



#### Generate view

Generate and share a view on a workflow executed by the Spark executor. Executes a workflow on Spark and generates a SparkSQL temporary table instead of serializing the result. The table can be accessed via JDBC

| Parameter | Type | Description | Example |
|  ---------------------- | ------------- | ------------------ | -------------------------- |
| caching | boolean | Optional parameter that enables caching (default=false). |
| userDefinedName | String | Optional View name that is used when a view on a non virtual is generated (default = [TASK-ID]_generated_view). |

The identifier for this plugin is `GenerateSparkView`.

It can be found in the package `com.eccenca.di.sql.virtual`.
