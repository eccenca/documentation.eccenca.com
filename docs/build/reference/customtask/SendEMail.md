---
title: "Send email"
description: "Sends an email using an SMTP server."
icon: octicons/cross-reference-24
tags: 
    - WorkflowTask
---
# Send email
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Sends an email using an SMTP server with support for both plain text and HTML formatted messages.

## Features

- Send emails with optional file attachments from workflow datasets
- Support for multiple recipients (To, CC, BCC)
- HTML and plain text message formatting
- SSL/TLS connection support
- Configurable retry mechanism with delays
- Dynamic email configuration via input parameters

## Usage

When connected to a dataset that is based on a file in a workflow, it will send that file as an attachment whenever
the workflow is executed. This allows you to send workflow results via email automatically.

## HTML email example

Enable HTML formatting and use standard HTML markup in your message:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Workflow Results</title>
</head>
<body>

<h1>Workflow Results</h1>

<p>Here are the results of your workflow:</p>
<ul>
  <li><b>Total records processed:</b> 1,234</li>
  <li><b>Status:</b> <span style="color: green;">Success</span></li>
</ul>
<p>Please find the detailed report attached.</p>

<table>
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>Processing Time</td><td>2.5 minutes</td></tr>
  <tr><td>Error Rate</td><td>0%</td></tr>
</table>

</body>
</html>
```

## Parameter

### Host

The SMTP host, e.g, mail.myProvider.com

- ID: `host`
- Datatype: `string`
- Default Value: `None`

### Port

The SMTP port

- ID: `port`
- Datatype: `int`
- Default Value: `587`

### User

Username

- ID: `user`
- Datatype: `string`
- Default Value: `None`

### Password

Password

- ID: `password`
- Datatype: `password`
- Default Value: `None`

### From

The sender email address

- ID: `from`
- Datatype: `string`
- Default Value: `None`

### To

The "To" field is required to have at minimum one email address for the receiver. Multiple email addresses for several receivers are also possible. They need to be separated by commas, as in `info@example.com, john.doe@business.com`. The mailbox may be specified either as a simple address such as `info@example.com`, or in the format 'phrase + route address', as in `"Doe, John" <john.doe@business.com>`. Notice the quotes in the phrase `"Doe, John"`, as well as the `<` and `>` surrounding the address. For further information, see the standard for the format of Internet text messages, [RFC 822](https://datatracker.ietf.org/doc/html/rfc822).

- ID: `receiver`
- Datatype: `string`
- Default Value: `None`

### CC

The "CC" ('carbon copy') field is intended for the secondary recipients of the email. Otherwise, the same comments as in the "To" field, regarding receivers and formatting, are valid here.

- ID: `cc`
- Datatype: `string`
- Default Value: `None`

### BCC

The "BCC" ('blind carbon copy') field is reserved for the anonymous recipients of the email. The recipients contained in this field will not be included in the messages sent to the primary (i.e. "To") and secondary (i.e. "Cc" and the other "Bcc") recipients. Otherwise, the same comments as in the "To" field, regarding receivers and formatting, are valid here.

- ID: `bcc`
- Datatype: `string`
- Default Value: `None`

### Subject

The email subject

- ID: `subject`
- Datatype: `string`
- Default Value: `Dataset`

### Message

The email text message

- ID: `message`
- Datatype: `code-html`
- Default Value: `None`

### With HTML formatting

When enabled, the email text message will be HTML formatted. Otherwise, it's treated as plain text.

- ID: `withHTMLFormatting`
- Datatype: `boolean`
- Default Value: `false`

### With attachment

If enabled a file from the input is attached to the email. A single input to this operator is expected that provides a file, e.g. a file based dataset (XML, JSON etc.).

- ID: `withAttachment`
- Datatype: `boolean`
- Default Value: `false`

### Force SSL

When enabled a SSL/TLS connection will be forced from the start without negotiation with the server. Not to be confused with STARTTLS which upgrades an insecure connection to a SSL/TLS connection, which is done by default.

- ID: `sslConnection`
- Datatype: `boolean`
- Default Value: `false`

### Read email properties from input

When enabled this allows to send multiple emails. All email configurations are input via the first operator input with each entry representing a different email. The optional second input can be a file based dataset for the attachment. Email parameters that can be overwritten are: from, receiver, cc, bcc, subject and message.

- ID: `readParametersFromInput`
- Datatype: `boolean`
- Default Value: `false`

### Delay between emails (ms)

The delay in milliseconds between sending two consecutive emails. This applies to the retry mechanism, but also to sending multiple emails.

- ID: `delayBetweenDeliveriesMS`
- Datatype: `int`
- Default Value: `2`

## Advanced Parameter

### Timeout

Timeout in milliseconds to establish a connection or wait for a server response. Setting it to 0 or negative number will disable the timeout.

- ID: `timeout`
- Datatype: `int`
- Default Value: `10000`

### Number of retries

The number of retries per email when send errors are encountered.

- ID: `nrRetries`
- Datatype: `int`
- Default Value: `2`
