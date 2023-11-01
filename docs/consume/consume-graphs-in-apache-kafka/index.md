---
icon: material/apache-kafka
status: new
tags:
    - Automate
    - KnowledgeGraph
    - PythonPlugin
---
# Populate Graphs to Apache Kafka

## Introduction

[Apache Kafka](https://kafka.apache.org/) is a distributed event store and stream-processing platform.
Kafka is widely used in enterprises for data pipelines, streaming analytics, data integration and other applications.

By using the [cmem-plugin-kafka](https://pypi.org/project/cmem-plugin-kafka/) [Python Plugin](../../develop/python-plugins/index.md), you can produce and send messages to Apache Kafka from inside of our Corporate Memory Workflows.

## Installation

In order to use the Kafka Producer workflow task, you need to extend your Corporate Memory instance with the `cmem-plugin-kafka` package.
This can be done by using cmemc:

```shell-session title="Installing cmem-plugin-kafka on the instance 'my-cmem'"
$ cmemc -c my-cmem admin workspace python install cmem-plugin-kafka
Install package cmem-plugin-kafka ... done
```

You can validate your installation by listing all installed plugins (from all packages):

```shell-session
$ cmemc -c my-cmem admin workspace python list-plugins
ID                                 Package ID         Type            Label
---------------------------------  -----------------  --------------  ---------------------------------
cmem_plugin_kafka-ReceiveMessages  cmem-plugin-kafka  WorkflowPlugin  Kafka Consumer (Receive Messages)
cmem_plugin_kafka-SendMessages     cmem-plugin-kafka  WorkflowPlugin  Kafka Producer (Send Messages)
```

## Usage

Once you installed the package, you can use the Kafka Producer by simply creating a new task, e.g. search for `kafka` in the **Create new item** screen:

![Create new Item and search for `kafka`](create-new-item-kafka.png "Create new Item and search for `kafka`")

Follow the in-app documentation on how to configure the task (e.g. for providing credentials or preparing data to be sent in messages).

