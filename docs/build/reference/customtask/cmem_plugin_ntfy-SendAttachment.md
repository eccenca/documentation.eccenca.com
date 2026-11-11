---
title: "Send ntfy attachment"
description: "Send a file as an attachment to a topic on an ntfy server."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Send ntfy attachment

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

## What it does

Sends files to an ntfy topic as attachments, so a report a workflow just
produced arrives where somebody will see it.

## What flows through the ports

One input port accepts file entities - from a file dataset, a project resource
or a preceding task that produces files - and every file that arrives is sent
as one notification, byte for byte, under its own name. There is no output
port: the task is a terminal step and hands nothing on.

## Where it sits

It is the file sending counterpart of **Send ntfy message**, which sends text,
and of **Get ntfy attachments**, which fetches files in the other direction.

## Caveats

- **The file is the body of the notification**, so the text fields configured
  here travel beside it and describe it rather than replacing it.
- **An input is required.** With nothing connected the task has no file to
  send and fails instead of notifying anybody.
- **ntfy limits an attachment to 15 MB** by default and keeps it for three
  hours, after which the recipient's link stops working. A file the server
  refuses fails the run, and files already sent are not taken back.
- **The media type a recipient sees comes from the file name.** ntfy reads it
  from the name's extension and ignores what the request declares, so a file
  entity's own media type does not travel with it and a file arriving without
  an extension is offered as a generic download.
- **An upload is never retried, not even when the server asks for a slower
  pace.** A file arrives as a stream that can be read once, so a second attempt
  would upload an empty attachment that ntfy accepts and stores. Failing on the
  rate limit and re-running the workflow is the honest outcome.
- **What is configured applies to every file.** A per-file title or priority
  is not read from the entities, which carry a file and nothing else.
- **An unprotected topic is public.** A topic needs no sign-up and carries no
  password of its own, so on a server without access control anybody who
  guesses the name can download every file this task sends - and a file is
  usually a whole report rather than one line of text. Give the topic a long
  random suffix rather than a word like `reports`, and protect it with the
  server's own [access control](https://docs.ntfy.sh/config/#access-control)
  where that is available.


## Parameter

### Server

The base URL of the ntfy server. The default is the public service; a self-hosted ntfy is named here instead, for example <https://ntfy.example.org> - see [installing ntfy](https://docs.ntfy.sh/install/).

- ID: `server`
- Datatype: `string`
- Default Value: `https://ntfy.sh`



### Access token

The access token to authenticate with. A public topic needs none, so this can be left empty. See [access tokens](https://docs.ntfy.sh/config/#access-tokens).

- ID: `access_token`
- Datatype: `password`
- Default Value: `None`



### Topic

The topic the files are sent to. A topic needs no sign-up and has no password of its own, so give it a long random suffix nobody can guess rather than a plain word - see [picking a topic](https://docs.ntfy.sh/publish/#picking-a-topic).

- ID: `topic`
- Datatype: `string`
- Default Value: `None`



### Title

The title shown with every attachment of this task. It travels as a header, so it is a single line and a line break becomes a space. See [message titles](https://docs.ntfy.sh/publish/#message-title).

- ID: `title`
- Datatype: `string`
- Default Value: `None`



### Message

The text shown with every attachment of this task. Left empty, the recipient sees the file name. Like the title it is a single line, and anything beyond 4096 bytes is shortened.

- ID: `message`
- Datatype: `string`
- Default Value: `None`



### Priority

How urgently every notification of this task is shown. See [message priority](https://docs.ntfy.sh/publish/#message-priority).

- ID: `priority`
- Datatype: `string`
- Default Value: `default`



### Notification tags

Tags shown with the notification, as a comma separated list. A tag that names an emoji is shown as that emoji. See [tags and emojis](https://docs.ntfy.sh/publish/#tags-emojis) and the [list of emoji names](https://docs.ntfy.sh/emojis/).

- ID: `notification_tags`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Click URL

The URL opened when the notification is tapped. See [click action](https://docs.ntfy.sh/publish/#click-action).

- ID: `click`
- Datatype: `string`
- Default Value: `None`
