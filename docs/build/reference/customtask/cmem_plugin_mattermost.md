---
title: "Send Mattermost messages"
description: "Send messages to Mattermost channels and/or users."
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

This task sends messages to Mattermost channels and users.

You need a bot account in order to connect to Mattermost.
Learn more on bot accounts at
[developers.mattermost.com](https://developers.mattermost.com):

- [Using bot accounts](https://developers.mattermost.com/integrate/reference/bot-accounts/)
- [Personal access tokens](https://developers.mattermost.com/integrate/reference/personal-access-token/)

The task has two working modes.

# Single Message

You can send a single static message to a pre-configured channel or user.
Just configure the User and/or Channel and Message parameters to do so.

# Multiple Messages

You can send multiple messages to different channels or users by piping data into
the task. For each entity, a message is send. For dynamic messages the following
input paths are recognized:

- user
- channel
- message

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

The name or display name of the bot you want to use to connect.

- ID: `bot_name`
- Datatype: `string`
- Default Value: `None`

### User

The user account which will receive the message. You can search for users if the connection was successful (Base URl, bot + token).

- ID: `user`
- Datatype: `string`
- Default Value: `None`

### Channel

The channel which will receive the message. You can search for channels if the connection was successful (Base URl, bot + token). If you want to send your message to multiple channels, separate them with a comma.

- ID: `channel`
- Datatype: `string`
- Default Value: `None`

### Message

The message size is limited to a configured maximum (e.g. 16383 characters).

- ID: `message`
- Datatype: `multiline string`
- Default Value: `None`

## Advanced Parameter

`None`
