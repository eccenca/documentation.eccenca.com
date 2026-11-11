---
title: "Send Mattermost messages"
description: "Post messages to Mattermost users and channels through a bot account."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Send Mattermost messages

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.

This task posts messages to Mattermost. Every message is sent by a bot
account, so recipients see it as coming from the bot rather than from the
person who ran the workflow. You need that bot account and a personal access
token for it before the task can do anything - learn more at
[developers.mattermost.com](https://developers.mattermost.com):

- [Using bot accounts](https://developers.mattermost.com/integrate/reference/bot-accounts/)
- [Personal access tokens](https://developers.mattermost.com/integrate/reference/personal-access-token/)

# Ports

One input port accepts entities carrying the paths `user`, `channel` and
`message`. Each entity is sent as one message per recipient it names: a direct
message to the user, a post to the channel, or both.

There is no output port. The task is a terminal step - it hands nothing on to
the rest of the workflow and reports only how many messages went where.

A recipient and a message configured on the task itself are sent once, before
any entity is read. Configuring them while entities also arrive sends both:
that message once, and one message per entity on top of it.

# Caveats

- One field names one recipient, matched exactly. A user is found by username,
  nickname, email address or full name; a channel by its name or its display
  name. A comma separated list is **not** split into several recipients - it is
  looked up as a single name, which fails.
- What an entity carries is not merged with what is configured on the task. An
  entity without a message does not fall back to the configured message; it
  fails.
- The task stops at the first entity it cannot send - one naming no recipient,
  one carrying no message, or one naming a recipient Mattermost does not know.
  Messages sent for earlier entities have already been posted and are not taken
  back.
- Requests to Mattermost time out after two seconds, so an unreachable or slow
  server fails the task rather than delaying it.


## Parameter

### URL

The base URL of your Mattermost deployment. Example: <https://mattermost.example.org>

- ID: `url`
- Datatype: `string`
- Default Value: `None`



### Access Token

The Personal Access Token of the bot account.

- ID: `access_token`
- Datatype: `password`
- Default Value: `None`



### Bot name

The bot account that sends the messages, named by its username, nickname, email address or full name.

- ID: `bot_name`
- Datatype: `string`
- Default Value: `None`



### User

The single user account that receives the message as a direct message, named by username, nickname, email address or full name. Type at least one letter to search for users. Suggestions need the URL and the Access Token to be filled in first.

- ID: `user`
- Datatype: `string`
- Default Value: `None`



### Channel

The single channel that receives the message, named by its name or its display name. Type at least one letter to search for channels. Suggestions need the URL and the Access Token to be filled in first.

- ID: `channel`
- Datatype: `string`
- Default Value: `None`



### Message

The message text, interpreted by Mattermost as Markdown. Its maximum length is a server setting, 16383 characters by default.

- ID: `message`
- Datatype: `multiline string`
- Default Value: `None`

## Advanced Parameter

`None`
