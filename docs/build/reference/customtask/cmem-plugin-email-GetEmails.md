---
title: "Get emails"
description: "Search IMAP mailbox and get email metadata or file attachments."
icon: octicons/cross-reference-24
tags:
    - WorkflowTask
    - PythonPlugin
---

# Get emails

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

!!! note inline end "Python Plugin"

    This operator is part of a Python Plugin Package.
    In order to use it, you need to install it,
    e.g. with cmemc.


This task connects to an IMAP server, searches a configurable mailbox folder
and returns matching emails as entities.

## How It Works

This workflow task takes no workflow input and produces entities
directly from a mailbox, so it sits at the beginning of a workflow. Each run:

1. **Connects** to the IMAP server over SSL/TLS (default port 993).
2. **Logs in** with the configured username and password.
3. **Opens** the selected mailbox folder. The **Folder** field autocompletes the
   folders available on the connected account.
4. **Searches** that folder with your **Search Term** (IMAP search criteria) and
   collects the matching messages.
5. **Emits entities** according to the **Output Mode** — one entity per email
   or one file entity per attachment.

## Example Search Terms

- `ALL` - all messages in the folder
- `UNSEEN` - only unread messages
- `FROM "someone@example.com"` - messages from a specific sender
- `SUBJECT "invoice"` - messages with a subject containing "invoice"
- `SINCE 01-Jan-2026` - messages received on or after a date
- `BEFORE 01-Feb-2026` - messages received before a date
- `LARGER 1000000` - messages larger than 1 MB (useful for finding emails with attachments)
- `UNSEEN FROM "someone@example.com"` - unread messages from a specific sender
- `UNSEEN SUBJECT "invoice"` - unread messages with a subject containing "invoice"
- `SINCE 01-Jan-2026 BEFORE 01-Feb-2026` - messages received in January 2026
- `UNSEEN FROM "someone@example.com" SINCE 01-Jan-2026` - unread messages from a sender since a date
- `SUBJECT "invoice" SINCE 01-Jan-2026 BEFORE 01-Feb-2026` - invoices received in January 2026

These are common examples. For the complete list of search keys, see
[RFC 3501, §6.4.4](https://datatracker.ietf.org/doc/html/rfc3501#section-6.4.4).

## Output Modes

### Emails

Returns one entity per email with the following fields:

- identity & content: `msg_id`, `subject`, `body` (plain text), `html_body` (raw HTML),

 `snippet` (short preview)

- sender: `sender` (full), `sender_name`, `sender_email`
- recipients (multi-valued): `recipient`, `cc`, `bcc` (full addresses) plus
  `recipient_email`, `cc_email`, `bcc_email`.
  `bcc*` is normally only populated when reading the **Sent** folder, not the Inbox.
- dates: `date` (raw header), `date_sent` (ISO-8601 UTC), `date_sent_local` (ISO-8601,
  original offset)
- threading: `in_reply_to`, `references` (multi-valued)
- attachments: `has_attachments`, `attachment_count`, `attachment_names` (multi-valued)

### File attachments

Returns one file entity per email attachment using the File Entity Schema.
Requires a **Multi CSV ZIP**, **binary** or other dataset sink.


## Parameter

### IMAP Server

Address of the IMAP server (e.g. imap.example.org).

- ID: `imap_server`
- Datatype: `string`
- Default Value: `None`



### Username

Email account username (usually your email address).

- ID: `username`
- Datatype: `string`
- Default Value: `None`



### Password

Password or app-specific password for the email account.

- ID: `password`
- Datatype: `password`
- Default Value: `None`



### Folder

Mailbox folder to search (e.g. INBOX, Sent, Drafts).

- ID: `folder`
- Datatype: `string`
- Default Value: `None`



### Search Term

IMAP search criteria (e.g. ALL, UNSEEN, FROM <someone@example.com>).

- ID: `search_term`
- Datatype: `string`
- Default Value: `ALL`



### Output Mode

Controls what this task returns. `Emails` returns one entity per email with subject, sender, recipients, etc. ,`File attachments` returns one file entity per email attachment, readable by downstream tasks.

- ID: `output_mode`
- Datatype: `string`
- Default Value: `metadata`



### Attachment Regex

Regular expression (Python `re` syntax) matched against each attachment's filename with `re.search` (matches anywhere; case-sensitive — prefix with `(?i)` for case-insensitive). Example: `\.(pdf|xlsx)$` keeps PDF and Excel files. Leave empty to include all attachments. Only applies when Output Mode is set to File attachments.

- ID: `attachment_regex`
- Datatype: `string`
- Default Value: `None`

## Advanced Parameter

### IMAP Port

Port number for the IMAP server (993 for SSL, 143 for plain).

- ID: `imap_port`
- Datatype: `Long`
- Default Value: `993`
