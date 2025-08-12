---
title: "Kafka Producer (Send Messages)"
description: "Reads a messages dataset and sends records to a Kafka topic (Producer)."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
    - PythonPlugin
---
# Kafka Producer (Send Messages)
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This is a [Python Plugin](../../../develop/python-plugins/index.md).
    In order to use it, you need to install it,
    e.g. [with cmemc](../../../automate/cmemc-command-line-interface/command-reference/admin/workspace/python/index.md).

This workflow operator uses the Kafka Producer API to send
messages to a [Apache Kafka](https://kafka.apache.org/).

Accepts entities as input, and, if desired, accepts a pre-constructed XML/JSON dataset,
which is transformed into messages and sent to a designated Kafka topic based
on configuration.

<details>
  <summary>Sample XML format</summary>

  An example XML document is shown below. This document will be sent as two messages
  to the configured topic. Each message is created as a proper XML document.


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

<details>
  <summary>Sample JSON format</summary>

  An example JSON document is shown below. This document will be sent as two messages
  to the configured topic. Each message is created as a proper JSON document.


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



## Parameter

### Messages Dataset

Where do you want to retrieve the messages from? The dropdown lists usable datasets from the current project only. In case you miss your dataset, check for the correct type (XML/JSON) and build project). The messages will be retrieved from the entities if no dataset is provided.

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

The name of the category/feed to which the messages will be published. Note that you may create this topic in advance before publishing messages to it. This is especially true for a kafka cluster hosted at [confluent.cloud](https://confluent.cloud).

- Datatype: `string`
- Default Value: `None`



### Client Id

An optional identifier of a Kafka client (producer/consumer) that is passed to a Kafka broker with every request. The sole purpose of this is to be able to track the source of requests beyond just ip and port by allowing a logical application name to be included in Kafka logs and monitoring aggregates. When the Client Id field is empty, the plugin defaults to DNS:PROJECT ID:TASK ID.

- Datatype: `string`
- Default Value: `None`



### Maximum Message Size

The maximum size of a request message in bytes. This is also effectively a cap on the maximum record size. Note that the server has its own cap on record size which may be different from this.

- Datatype: `Long`
- Default Value: `1048576`



### Compression Type

The compression type for all data generated by the producer. The default is none (i.e. no compression).

- Datatype: `string`
- Default Value: `none`



