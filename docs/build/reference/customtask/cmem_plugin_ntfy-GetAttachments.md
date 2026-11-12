---
title: "Get ntfy attachments"
description: "Download the attachments of a topic's messages from an ntfy server."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Get ntfy attachments

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

## What it does

Downloads the files attached to the messages of a topic, so a workflow can
process what somebody sent to it.

## What flows through the ports

The task consumes nothing and reads from the server itself. Its output port
carries one file entity per downloaded attachment, with the media type the
message declared and the name it gave, reduced to a plain file name. A file
dataset or a file consuming task can be connected to it.

## Where it sits

It reads the same topic as **Get ntfy messages** and keeps its own position, so
the two can run side by side without taking each other's messages. They share
one position file by default, which is worth separating if they are scheduled
to finish at the same moment. Use that task instead when the text of the
messages is what matters.

## Caveats

- **A message without an attachment is passed over**, and so is an attachment
  that is not where the message said - ntfy drops an uploaded file after three
  hours. Neither fails the run, and the report counts them apart, because the
  second one is also what a wrong address looks like from here.
- **A run either reads everything or only what is new**, as with the messages
  task, and the position advances over passed-over messages as well, so they
  are not offered again.
- **A message published a moment ago may not be there yet.** A busy server
  writes its message cache in batches - ntfy.sh is configured for one second -
  so a workflow that publishes to a topic and reads it back in the same run can
  come away with nothing. Reading what another run published is reliable;
  reading what this run published is not.
- **An attachment is fetched from wherever the message points.** A publisher
  may attach a file that is hosted elsewhere, and ntfy hands such a URL on
  unchanged, so the download goes to that host rather than to the configured
  server. The access token is sent to the configured server only.
- **ntfy writes those addresses from its own base URL**, not from the address
  it was reached on, so a server behind a container host name, a proxy or a
  tunnel hands out links that point somewhere this task cannot reach - and that
  it does not recognise as the configured server either, which withholds the
  token as well. The task can be told to fetch ntfy's own file path from the
  configured server instead, which leaves an attachment hosted elsewhere alone.
- **Files are downloaded to the worker's temporary directory** and are not
  cleaned up by the task, because the rest of the workflow still has to read
  them.
- **An attachment may be large, and only this task limits it.** ntfy allows
  15 MB per file by default, but an attachment hosted elsewhere is not bound by
  that, so anything over the size limit configured here is passed over and
  counted rather than written to the worker's disk.
- **An unprotected topic is public, and anybody may write to it.** A topic
  needs no sign-up and carries no password of its own, so on a server without
  access control anybody who guesses the name can publish to it - which,
  together with the point above, means choosing what this task downloads and
  from where. Give the topic a long random suffix rather than a word like
  `reports`, and protect it with the server's own
  [access control](https://docs.ntfy.sh/config/#access-control) where that is available.


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

The topic whose attachments are downloaded. A topic needs no sign-up and has no password of its own, so give it a long random suffix nobody can guess rather than a plain word - see [picking a topic](https://docs.ntfy.sh/publish/#picking-a-topic).

- ID: `topic`
- Datatype: `string`
- Default Value: `None`



### Messages to return

Which of a topic's messages a run returns.

- ID: `read_mode`
- Datatype: `string`
- Default Value: `stateless`



### Starting point

How far back a run reaches: a duration such as `10m`, a Unix timestamp, a message id, or `all` for everything the server still holds. A task set to return only new messages reads this on its first run only, and continues from its remembered position afterwards. See [fetching cached messages](https://docs.ntfy.sh/subscribe/api/#fetch-cached-messages).

- ID: `since`
- Datatype: `string`
- Default Value: `all`

## Advanced Parameter

### Priority filter

Return only messages of these priorities, as a comma separated list - each one a number from 1 to 5 or one of ntfy's names, from `min` to `max`. A message matching any of them is returned. Empty returns every priority. See [filtering messages](https://docs.ntfy.sh/subscribe/api/#filter-messages).

- ID: `priority_filter`
- Datatype: `string`
- Default Value: `None`



### Tag filter

Return only messages carrying these tags, as a comma separated list. A message must carry all of them. Empty returns every message. See [filtering messages](https://docs.ntfy.sh/subscribe/api/#filter-messages).

- ID: `tags_filter`
- Datatype: `string`
- Default Value: `None`



### Maximum attachment size

How many megabytes an attachment may weigh before it is passed over rather than downloaded. An attachment URL is whatever the publisher of the message put there, and ntfy forwards an external one unchanged, so the server's own limit of 15 MB does not bind it. 0 downloads whatever arrives.

- ID: `maximum_size`
- Datatype: `Long`
- Default Value: `100`



### Fetch attachments from this server

If enabled, an attachment is fetched from the server configured above rather than from the address the message carries. ntfy builds that address from its own base URL, so a server reached under another name - a container host name, a proxy, a tunnel - hands out links that point somewhere unreachable and that the task does not recognise as its own, which also withholds the access token. Only ntfy's own file path is redirected; an attachment the publisher hosted elsewhere is always fetched from where it says.

- ID: `from_own_server`
- Datatype: `boolean`
- Default Value: `false`



### Position file

The project file the read positions are kept in. One file holds the positions of every task in the project and is written whole, so give a task its own file when it may finish at the same moment as another one reading the same project.

- ID: `cursor_file`
- Datatype: `string`
- Default Value: `ntfy-cursors.json`
