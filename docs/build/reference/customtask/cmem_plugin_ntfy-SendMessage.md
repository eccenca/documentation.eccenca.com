---
title: "Send ntfy message"
description: "Send a push notification to a topic on an ntfy server."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Send ntfy message

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

## What it does

Sends a push notification through ntfy, so a workflow can tell somebody what
it did without them watching the workspace.

## What flows through the ports

Notifications arrive on one input port as entities carrying the paths `topic`,
`title`, `message`, `priority`, `tags` and `click`, and one notification is
sent per entity - where an entity's `priority` is a number from 1 to 5, one of
ntfy's names from `min` to `max`, or `urgent`, which ntfy reads as `max`. That
port is replaced by the task's own fields when a message is configured on the
task itself, which then sends exactly one notification. There is no output port
either way: the task is a terminal step and hands nothing on.

## Where it sits

It is the sending half of this package. **Get ntfy messages** reads a topic in
the other direction, and **Send ntfy attachment** sends a file produced earlier
in the workflow.

## Caveats

- **The two ways of supplying a notification exclude each other.** Either the
  task sends the one notification configured on it, or it sends one per entity
  that arrives - there is no run in which a constant message goes out a hundred
  times. Markdown, Delay, Icon URL and Email copy are the exception: they are
  never carried by an entity and apply either way.
- **The topic is the one field an entity may leave to the task.** An entity
  that names no topic is sent to the topic configured here, which spares a
  workflow from attaching a constant to every entity.
- **An entity that carries no message fails the run**, because a notification
  without text says nothing. So does a run that has neither: a task with no
  message configured and nothing connected to its port fails rather than
  sending silence.
- **The first rejected request fails the run.** A rate limit is retried up to
  three times first, since the server has said it took nothing. A server error
  is not retried at all: it may have delivered the notification before failing
  to answer, and a duplicate alert is worse than a failed run. Notifications
  already sent are not taken back, and the report says how many went out
  before the failure.
- **A message longer than 4096 bytes is shortened**, marked with an ellipsis,
  rather than refused by the server. The report counts how often that happened.
- **An unprotected topic is public.** A topic needs no sign-up and carries no
  password of its own, so on a server without access control the only thing
  between a notification and anybody who guesses the name is the name itself -
  and then every title and message a workflow sends is readable, along with
  what ran and when. Give the topic a long random suffix rather than a word
  like `alerts`, and protect it with the server's own
  [access control](https://docs.ntfy.sh/config/#access-control) where that is available.
- **A notification cannot be recalled.** The test action below sends a real
  notification to the configured topic.


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

The topic the notification is sent to. An entity that names no topic of its own is sent here. A topic needs no sign-up and has no password of its own, so give it a long random suffix nobody can guess rather than a plain word - see [picking a topic](https://docs.ntfy.sh/publish/#picking-a-topic).

- ID: `topic`
- Datatype: `string`
- Default Value: `None`



### Title

The title of the notification the task sends itself. See [message titles](https://docs.ntfy.sh/publish/#message-title).

- ID: `title`
- Datatype: `string`
- Default Value: `None`



### Message

The text of the notification. Configuring it makes the task send that one notification and removes its input port; left empty, each notification arrives on that port instead.

- ID: `message`
- Datatype: `multiline string`
- Default Value: `None`



### Priority

How urgently the notification is shown, for the one the task sends itself. See [message priority](https://docs.ntfy.sh/publish/#message-priority).

- ID: `priority`
- Datatype: `string`
- Default Value: `default`



### Notification tags

Tags shown with the notification, as a comma separated list. A tag that names an emoji is shown as that emoji. Used for the notification the task sends itself. See [tags and emojis](https://docs.ntfy.sh/publish/#tags-emojis) and the [list of emoji names](https://docs.ntfy.sh/emojis/).

- ID: `notification_tags`
- Datatype: `string`
- Default Value: `None`



### Click URL

The URL opened when the notification is tapped. Used for the notification the task sends itself. See [click action](https://docs.ntfy.sh/publish/#click-action).

- ID: `click`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### Markdown

If enabled, the message is formatted as Markdown. Note that the Android app shows the markup as typed; the web app and the desktop clients render it. See [Markdown formatting](https://docs.ntfy.sh/publish/#markdown-formatting).

- ID: `markdown`
- Datatype: `boolean`
- Default Value: `false`



### Delay

Holds the notification back: a duration such as `30m`, a timestamp, or a time of day such as `9am`, which the server reads in its own time zone. Between ten seconds and three days. See [scheduled delivery](https://docs.ntfy.sh/publish/#scheduled-delivery).

- ID: `delay`
- Datatype: `string`
- Default Value: `None`



### Icon URL

The URL of a PNG or JPEG shown as the notification's icon. See [icons](https://docs.ntfy.sh/publish/#icons).

- ID: `icon`
- Datatype: `string`
- Default Value: `None`



### Email copy

An address the server also sends the notification to as mail. Needs a server configured for mail delivery. See [e-mail notifications](https://docs.ntfy.sh/publish/#e-mail-notifications).

- ID: `email`
- Datatype: `string`
- Default Value: `None`
