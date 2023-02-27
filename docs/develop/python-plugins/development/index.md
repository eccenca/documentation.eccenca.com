---
title: "Python Plugins: Development"
icon: material/code-json
tags:
    - Python
---
# Python Plugin Development

## Introduction

Python plugins are small software projects which extend the functionality of eccenca Corporate Memory.
They have its own release cycle and are not included in the main software.
Python plugins can can be installed and uninstalled during runtime.

In order to support the development of python plugins, we published a [base package](https://github.com/eccenca/cmem-plugin-base) as well as a [project template](https://github.com/eccenca/cmem-plugin-template).
Please have a look at these projects to get started.

This page gives an overview of the concepts you need to understand in order to develop plugins.

## Plugin Types

The following plugin types are defined.

### Workflow Plugins

A workflow plugin implements a new operator (task) that can be used within a workflow.
A workflow plugin may accept an arbitrary list of inputs and optionally returns a single output.

The lifecycle of a workflow plugin is as follows:

-   The plugin will be instantiated once the workflow execution reaches the respective plugin.
-   The `execute` function is called and gets the results of the ingoing operators as input.
-   The output is forwarded to the next operator.

The following depiction shows a task of the plugin **My Workflow Plugin**.
The task has two connected incoming tasks and one connected outgoing task.

![workflow-plugins](22-2-my-workflow-plugin.png)

The corresponding source code of the plugin is listed below.

```py title="workflow.py"
from typing import Sequence
from cmem_plugin_base.dataintegration.context import ExecutionContext
from cmem_plugin_base.dataintegration.description import PluginParameter, Plugin
from cmem_plugin_base.dataintegration.entity import Entities
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin

@Plugin(label="My Workflow Plugin")
class MyWorkflowPlugin(WorkflowPlugin):
    """My Workflow Plugin"""

    def execute(
        self, inputs: Sequence[Entities], context: ExecutionContext
    ) -> Entities:
        return inputs[0]
```

### Transform Plugins

A transform plugin can be used in transform and linking rules.
It accepts an arbitrary number of inputs and returns an output.
Each input as well as the output consists of a sequence of values.

The image below shows a value transformation that uses the **My Transform Plugin** plugin.
The plugin splits the input string into a list of words and forwards only the last one.

![transform-plugins](22-1-my-transform-plugin.png)

The corresponding source code of the plugin is listed below.

```py title="transform.py"
from typing import Sequence
from cmem_plugin_base.dataintegration.description import PluginParameter, Plugin
from cmem_plugin_base.dataintegration.plugins import TransformPlugin


@Plugin(label="My Transform Plugin")
class MyTransformPlugin(TransformPlugin):
    """My Transform Plugin"""

    def transform(self, inputs: Sequence[Sequence[str]]) -> Sequence[str]:
        for item in inputs:
            return item[0].split(" ")[-1]
```

## Context Objects

The [cmem-plugin-base](https://github.com/eccenca/cmem-plugin-base/) package describes [context objects](https://github.com/eccenca/cmem-plugin-base/blob/main/cmem_plugin_base/dataintegration/context.py), which are passed to the plugin depending on the executed method.

| Class              | Description                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SystemContext`    | Passed into methods to request general system information.                                                                                          |
| `UserContext`      | Passed into methods that are triggered by a user interaction.                                                                                       |
| `TaskContext`      | Passed into objects that are part of a DataIntegration task/project.                                                                                |
| `ExecutionReport`  | Workflow operators may generate execution reports. An execution report holds basic information and various statistics about the operator execution. |
| `ReportContext`    | Passed into workflow plugins that may generate a report during execution.                                                                           |
| `PluginContext`    | Combines context objects that are available during plugin creation or update.                                                                       |
| `ExecutionContext` | Combines context objects that are available during plugin execution.                                                                                |

## Entities

An `entity` is a structure to describe data objects which are passed around in workflows from one task to another task.
An entity is identified by a `uri` and holds `values`, i.e., a sequence of string sequences (= a list of multi-value fields).

Multiple entities are handled as `entities` objects, which have an attached `schema` to it.

A `schema` contains of `path` descriptions and is identified by a `type_uri`.

The following image shows these terms and their relationships. (1)
{ .annotate }

1. The concrete implementation details of entities can be found in the [entity module](https://github.com/eccenca/cmem-plugin-base/blob/main/cmem_plugin_base/dataintegration/entity.py) of the cmem-plugin-base package.

![entities-flow-diagram](22-2-entities-flow-diagram.png)

| Class          | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| `Entities`     | Holds a collection of entities and their schema                    |
| `Entity`       | An Entity can represent an instance of any given concept.          |
| `EntitySchema` | An entity schema that represents the type of uri and list of paths |
| `EntityPath`   | A path in a schema                                                 |

### Producing Entities

The following section shows the source code of a **Produce Entities** plugin, which is commented below.

```py title="entities-producer.py" linenums="1"
"""Entities Producer"""
import uuid
from secrets import token_urlsafe
from typing import Sequence

from cmem_plugin_base.dataintegration.context import ExecutionContext, ExecutionReport
from cmem_plugin_base.dataintegration.description import Plugin, PluginParameter
from cmem_plugin_base.dataintegration.entity import (
    Entities,
    Entity,
    EntitySchema,
    EntityPath,
)
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin


@Plugin(
    label="Produce Entities",
    description="Generates random values of X rows a Y values.",
    documentation="""
This example workflow operator generates random values as Entities.

The values are generated in X rows a Y values. Both parameter can be specified:

- 'number_of_entities': How many rows do you need.
- 'number_of_values': How many values per row do you need.
""",
    parameters=[
        PluginParameter(
            name="number_of_entities",
            label="Entities (Rows)",
            description="How many rows will be created per run.",
            default_value="10",
        ),
        PluginParameter(
            name="number_of_values",
            label="Values (Columns)",
            description="How many values are created per entity / row.",
            default_value="5",
        ),
    ],
)
class EntitiesProducer(WorkflowPlugin):
    """Entities Producer Plugin"""

    def __init__(self, number_of_entities: int = 2, number_of_values: int = 2) -> None:
        if number_of_entities < 1:
            raise ValueError("Entities (Rows) needs to be a positive integer.")

        if number_of_values < 1:
            raise ValueError("Values (Columns) needs to be a positive integer.")

        self.number_of_entities = number_of_entities
        self.number_of_values = number_of_values

    def execute(
        self, inputs: Sequence[Entities], context: ExecutionContext
    ) -> Entities:
        self.log.info("Start creating random values.")
        self.log.info(f"Config length: {len(self.config.get())}")
        entities_counter = 0
        value_counter = 0
        entities = []
        for _ in range(self.number_of_entities):
            entity_uri = f"urn:uuid:{str(uuid.uuid4())}"
            entities_counter += 1
            values = []
            for _ in range(self.number_of_values):
                values.append([token_urlsafe(16)])
                value_counter += 1
                context.report.update(
                    ExecutionReport(
                        entity_count=entities_counter,
                        operation="wait",
                        operation_desc="entities generated",
                    )
                )
            entities.append(Entity(uri=entity_uri, values=values))
        paths = []
        for path_no in range(self.number_of_values):
            path_uri = f"https://entities.org/vocab/RandomValuePath/{path_no}"
            paths.append(EntityPath(path=path_uri))
        schema = EntitySchema(
            type_uri="https://entities.org/vocab/RandomValueRow",
            paths=paths,
        )
        self.log.info(
            f"Happy to serve {entities_counter} entities with {value_counter} values."
        )
        context.report.update(
            ExecutionReport(
                entity_count=entities_counter,
                operation="wait",
                operation_desc="entities generated",
                summary=[
                    ("No. of entities", f"{entities_counter}"),
                    ("No. of values", f"{value_counter}"),
                ],
            )
        )
        return Entities(entities=entities, schema=schema)
```

Code explanation:

1. Provide a label, description and short documentation for the plugin. [(#17-27)](#__codelineno-10-17)
2. Define the parameters of the plugin. Here, two parameters are defined, where one specifies the number of `rows` and the other acthe number of `columns`. [(#24-41)](#__codelineno-10-24)
3. Intialise the parameters of the plugin. Additionally, you can validate and raise exceptions from `init()`. [(#46-54)](#__codelineno-10-46)
4. To return Entities we have to create a list of `entities` and its `schema`. As a first step, declare entities as an empty list. [(#62)](#__codelineno-10-62)
5. As previously mentioned, each `Entity` should have a `URI` and it can have sequence of `values`. Here, a list of entities is created with random UUIDs based on rows and values are created based on columns. After each entity is created it is appended to the entities list. [(#64-78)](#__codelineno-10-64)
6. To generate a `schema` (which is of type `EntitySchema`), which should have a `type_uri` and a sequence of `paths`, define an empty list of paths. [(#79)]((#__codelineno-10-79))
7. Based on the columns, each unique path is appended to the paths list. Once all paths are added, the schema is updated with `type_uri` and `paths` respectively. [(#80-86)]((#__codelineno-10-80))
8. Once the entities and the schema are generated you can return them. [(#101)](#__codelineno-10-101)
9. Update plugin logs using `PluginLogger` which is available as a default logger. [(#87-91)](#__codelineno-10-87)
10. To make your plugin more user-friendly you can use the Context API `report.update()` to update the workflow report. [(#91-100)](#__codelineno-10-86)

### Consuming Entities

Consuming entities in a workflow plugin means that you process at least one `entities` object from the `inputs` list.

The following code shows a plugin which loops through all inputs and counts all entities and its values.

```py title="entities-consumer.py" linenums="1"
"""Consume Entities"""
from typing import Sequence
from cmem_plugin_base.dataintegration.context import ExecutionContext, ExecutionReport
from cmem_plugin_base.dataintegration.description import Plugin
from cmem_plugin_base.dataintegration.entity import Entities
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin


@Plugin(
    label="Consume Entities",
    description="Reads random values of X rows a Y values.",
    documentation="""
This example workflow operator reads random values.
""",
)
class EntitiesConsumer(WorkflowPlugin):
    """Entities Consumer"""

    def execute(self, inputs: Sequence[Entities], context: ExecutionContext):
        entities_counter = 0
        value_counter = 0
        for item in inputs:
            for entity in item.entities:
                entities_counter += 1
                for _ in entity.values:
                    value_counter += 1
        context.report.update(
            ExecutionReport(
                entity_count=entities_counter,
                operation="wait",
                operation_desc="entities received",
                summary=[
                    ("No. of entities", f"{entities_counter}"),
                    ("No. of values", f"{value_counter}"),
                ],
            )
        )
```

Code explanation:

1. `inputs` from the workflow is a sequence of `Entities` with each item from the input having a list of entities and each entity having values. The entities and values are seperately counted. (#22-26)
2. Once the counting is done, the workflow report is updated with the total number of entities and values as the summary. (#27-37)

## Configuration

Plugins can have an application-wide configuration which cannot be changed on runtime and applies to all instances of this plugin.

This plugin configuration is provided in the `self.config` [PluginConfig](https://github.com/eccenca/cmem-plugin-base/blob/main/cmem_plugin_base/dataintegration/plugins.py#L32) object of the plugin.
The `get` method of this object returns a JSON string of the configuration.

Plugin configurations use the `plugin_id` as a config path in `dataintegration.conf`.

```hocon title="Example plugin configuration"
plugins.python.<plugin_id> = {
    key1 = "value1"
    key2 = "value2"
}
```

## Logging

Logging should be done with the [PluginLogger](https://github.com/eccenca/cmem-plugin-base/blob/main/cmem_plugin_base/dataintegration/plugins.py#L10), which is available as `self.log` in all plugins.

```py
self.log.info("Successfully executed Workflow Plugin")
```

On runtime, this logger will be replaced with a JVM based logging function feeding the plugin logs to the normal DataIntegration log stream.
This JVM-based logger will prefix all plugin logs with `plugins.python.<plugin id>`.

