---
title: "Send eMail"
description: "Sends an eMail using an SMTP server. If connected to a dataset that is based on a file in a workflow, it will send that file whenever the workflow is executed It can be used to send the result of a workflow via Mail."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Send eMail
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



Sends an eMail using an SMTP server. If connected to a dataset that is based on a file in a workflow, it will send that file whenever the workflow is executed It can be used to send the result of a workflow via Mail.

## Parameter

### Host

The SMTP host, e.g, mail.myProvider.com

- Datatype: `string`
- Default Value: `None`



### Port

The SMTP port

- Datatype: `int`
- Default Value: `587`



### User

Username

- Datatype: `string`
- Default Value: `None`



### Password

Password

- Datatype: `password`
- Default Value: `None`



### From

The sender eMail address

- Datatype: `string`
- Default Value: `None`



### To

The email addresses of the receivers. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com>

- Datatype: `string`
- Default Value: `None`



### CC

The CC-receiver eMail address. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com>

- Datatype: `string`
- Default Value: `None`



### BCC

The BCC-receiver eMail address. Email addresses are comma separated. Names must be quoted when containing commas.Example: john.smith@example.com, "Doe, John" <john.doe@example.com>, needs no quoting <needs.no.quoting@example.com>

- Datatype: `string`
- Default Value: `None`



### Subject

The eMail subject

- Datatype: `string`
- Default Value: `Dataset`



### Message

The eMail text message

- Datatype: `multiline string`
- Default Value: `None`



### With attachment

If enabled a file from the input is attached to the email. A single input to this operator is expected that provides a file, e.g. a file based dataset (XML, JSON etc.).

- Datatype: `boolean`
- Default Value: `true`



### Force SSL

When enabled a SSL/TLS connection will be forced from the start without negotiation with the server. Not to be confused with STARTTLS which upgrades an insecure connection to a SSL/TLS connection, which is done by default.

- Datatype: `boolean`
- Default Value: `false`



### Timeout

Timeout in milliseconds to establish a connection or wait for a server response. Setting it to 0 or negative number will disable the timeout.

- Datatype: `int`
- Default Value: `10000`



### Read e-mail properties from input

When enabled this allows to send multiple e-mails. All e-mail configurations are input via the first operator input with each entry representing a different e-mail. The optional second input can be a file based dataset for the attachment. E-mail parameters that can be overwritten are: from, receiver, cc, bcc, subject and message.

- Datatype: `boolean`
- Default Value: `false`



### Nr. of retries

The number of retries per email when send errors are encountered.

- Datatype: `int`
- Default Value: `2`



### Delay between e-mails (ms)

The delay in milliseconds between sending two consecutive e-mails. This applies to the retry mechanism, but also to sending multiple e-mails.

- Datatype: `int`
- Default Value: `2`



