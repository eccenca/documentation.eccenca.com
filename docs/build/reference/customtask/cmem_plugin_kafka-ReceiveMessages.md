---
title: "Kafka Consumer (Receive Messages)"
description: "Reads messages from a Kafka topic and saves it to a messages dataset (Consumer)."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Kafka Consumer (Receive Messages)
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This workflow operator uses the Kafka Consumer API
to receive messages from an [Apache Kafka](https://kafka.apache.org/) topic.

Messages received from the topic will be generated as entities with the following
flat schema:

- **key** - the optional key of the message,
- **content** - the message itself as plain text (use other operators, such as
  [Parse JSON](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/dataintegration/plugin-reference/#parse-json) or [Parse XML](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/dataintegration/plugin-reference/#parse-xml) to process
  complex message content),
- **offset** - the given offset of the message in the topic,
- **ts-production** - the timestamp when the message was written to the topic,
- **ts-consumption** - the timestamp when the message was consumed from the topic.

In order to process the resulting entities, they have to run through a transformation.

As an alternate working mode, messages can be exported directly to a JSON or XML
dataset if you know that the messages on your topic are valid JSON or XML documents
(see Advanced Options > Messages Dataset).

In this case, a sample response from the consumer will appear as follows:

<details>
  <summary>Sample JSON Response</summary>

```json
[
  {
    "message": {
      "key": "818432-942813-832642-453478",
      "headers": {
        "type": "ADD"
      },
      "content": {
        "location": ["Leipzig"],
        "obstacle": {
          "name": "Iron Bars",
          "order": "1"
        }
      }
    }
  },
  {
    "message": {
      "key": "887428-119918-570674-866526",
      "headers": {
        "type": "REMOVE"
      },
      "content": {
        "comments": "We can pass any json payload here."
      }
    }
  },
  {
    "message": {
      "key": "TestKey",
      "tombstone": true,
      "headers": {
        "h1": "v1",
        "h2": "v2"
      },
      "content": {
        "will_be_ignored": "..."
      }
    }
  }
]
```

</details>
<details>
  <summary>Sample XML Response</summary>

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <KafkaMessages>
        <Message>
        <PurchaseOrder OrderDate="1996-04-06">
            <ShipTo country="string">
            <name>string</name>
            </ShipTo>
        </PurchaseOrder>
        </Message>
        <Message>
        <PurchaseOrder OrderDate="1996-04-06">
            <ShipTo country="string">
            <name>string</name>
            </ShipTo>
        </PurchaseOrder>
        </Message>
        <Message key="TestKey" tombstone="true">will be ignored</Message>
    </KafkaMessages>
```

</details>


## Parameter

### Messages Dataset

Where do you want to save the messages? The dropdown lists usable datasets from the current project only. In case you miss your dataset, check for the correct type (XML/JSON) and build project.

- Datatype: `string`
- Default Value: `None`



### Bootstrap Server

This is URL of one of the Kafka brokers. The task fetches the initial metadata about your Kafka cluster from this URL.

- Datatype: `string`
- Default Value: `None`



### Security Protocol

Which security mechanisms need to be applied to connect? Use PLAINTEXT in case you connect to a plain Kafka, which is available inside your VPN. Use SASL in case you connect to a [confluent.cloud](https://confluent.cloud) cluster (then you also need to specify your SASL credentials in the advanced options section).

- Datatype: `string`
- Default Value: `PLAINTEXT`



### SASL Mechanisms



- Datatype: `string`
- Default Value: `PLAIN`



### SASL Account

The account identifier for the SASL authentication. In case you are using a [confluent.cloud](https://confluent.cloud) cluster, this is the API key.

- Datatype: `string`
- Default Value: `None`



### SASL Password

The credentials for the SASL Account. In case you are using a [confluent.cloud](https://confluent.cloud) cluster, this is the API secret.

- Datatype: `password`
- Default Value: `None`



### Topic

The name of the category/feed where messages were published.

- Datatype: `string`
- Default Value: `None`



### Auto Offset Reset

What to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server (e.g. because that data has been deleted). - `earliest` will fetch the whole topic beginning from the oldest record. - `latest` will receive nothing but will get any new records on the next run.

- Datatype: `string`
- Default Value: `latest`



### Consumer Group Name

When a topic is consumed by consumers in the same group, every record will be delivered to only one consumer of that group. If all the consumers of a topic are labeled the same consumer group, then the records will effectively be load-balanced over these consumers. If all the consumer of a topic are labeled different consumer groups, then each record will be broadcast to all the consumers. When the Group Id field is empty, the plugin defaults to DNS:PROJECT ID:TASK ID.

- Datatype: `string`
- Default Value: `None`



### Client Id

An optional identifier of a Kafka client (producer/consumer) that is passed to a Kafka broker with every request. The sole purpose of this is to be able to track the source of requests beyond just ip and port by allowing a logical application name to be included in Kafka logs and monitoring aggregates. When the Client Id field is empty, the plugin defaults to DNS:PROJECT ID:TASK ID.

- Datatype: `string`
- Default Value: `None`



### Local Consumer Queue Size

Maximum total message size in kilobytes that the consumer can buffer for a specific partition. The consumer will stop fetching from the partition if it hits this limit. This helps prevent consumers from running out of memory.

- Datatype: `Long`
- Default Value: `5000`



### Message Limit

The maximum number of messages to fetch and process in each run. If 0 or less, all messages will be fetched.

- Datatype: `Long`
- Default Value: `100000`



### Disable Commit

Setting this to true will disable committing messages after retrival. This means you will receive the same messages on the next execution (for debugging).

- Datatype: `boolean`
- Default Value: `false`



