---
title: "Get ntfy messages"
description: "Read the messages of a topic from an ntfy server."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Get ntfy messages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

## What it does

Reads the messages a topic holds and hands them on as entities, so a workflow
can act on what arrived through ntfy.

## What flows through the ports

The task consumes nothing and reads from the server itself. Its output port
carries one entity per message, with the paths `id`, `time`, `time_iso`,
`topic`, `title`, `message`, `priority`, `tags`, `click`, `icon`, the four
`attachment_*` paths, and `json` holding the message verbatim - so a field this
task does not model can still be read downstream. `tags` is the only path that
may carry several values; every other path carries one or none. A message that
was sent without a priority carries 3, the default ntfy applies to it and
leaves out of its answer.

## Where it sits

It is the reading half of this package. **Get ntfy attachments** fetches the
files of those messages, and **Send ntfy message** sends in the other
direction.

## Caveats

- **A run either returns everything or only what is new.** Returning only new
  ones makes the task write the position it reached into a file in the project
  and continue from it next time. Each task has its own entry there, so two
  tasks reading one topic never take each other's messages - but the file is
  written whole, so two of them finishing in the same moment can lose one of
  the two positions, and that task reads its window again.
- **The position only advances over messages a consumer asked past.** Taking
  an entity is not proof that it was processed, so the position follows the
  last message the rest of the workflow came back from. A run failing halfway
  leaves everything after that to be read again: a message is delivered at
  least once, duplicates are possible, and a lost message is not. A worker
  killed outright writes no position at all.
- **A message published a moment ago may not be there yet.** A busy server
  writes its message cache in batches - ntfy.sh is configured for one second -
  so a workflow that publishes to a topic and reads it back in the same run can
  come away with nothing. Reading what another run published is reliable;
  reading what this run published is not.
- **A message id that the server has forgotten cannot be resumed from.** ntfy
  keeps messages for twelve hours by default, so a task that has not run for
  longer starts from the whole window again - duplicates rather than loss.
- **The preview shows what the starting point names**, not the position a run
  would continue from, because a task action is not told which task it belongs
  to. Resetting the position has the same limitation and clears the position of
  every task reading this topic in this project.
- **An unprotected topic is public, and anybody may write to it.** A topic
  needs no sign-up and carries no password of its own, so on a server without
  access control anybody who guesses the name can read what is on it and
  publish to it - and this task hands a stranger's message to the workflow as
  readily as its own. Give the topic a long random suffix rather than a word
  like `alerts`, and protect it with the server's own
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

The topic whose messages are read. A topic needs no sign-up and has no password of its own, so give it a long random suffix nobody can guess rather than a plain word - see [picking a topic](https://docs.ntfy.sh/publish/#picking-a-topic).

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



### Position file

The project file the read positions are kept in. One file holds the positions of every task in the project and is written whole, so give a task its own file when it may finish at the same moment as another one reading the same project.

- ID: `cursor_file`
- Datatype: `string`
- Default Value: `ntfy-cursors.json`
