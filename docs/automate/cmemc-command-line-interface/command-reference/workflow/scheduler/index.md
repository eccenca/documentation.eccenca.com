---
title: "cmemc: Command Group - workflow scheduler"
description: "List, inspect, enable/disable or open scheduler."
icon: material/calendar
tags:
  - Automate
  - cmemc
---
# workflow scheduler Command Group

List, inspect, enable/disable or open scheduler.

Schedulers execute workflows in specified intervals. They are identified
with a SCHEDULERID. To get a list of existing schedulers, execute the
list command or use tab-completion.

## workflow scheduler open

Open scheduler(s) in the browser.

With this command, you can open a scheduler in the workspace in
your browser to change it.

The command accepts multiple scheduler IDs which results in
opening multiple browser tabs.

```shell-session
$ cmemc workflow scheduler open [OPTIONS] SCHEDULER_IDS...
```

```text
Usage: cmemc workflow scheduler open [OPTIONS] SCHEDULER_IDS...

  Open scheduler(s) in the browser.

  With this command, you can open a scheduler in the workspace in your
  browser to change it.

  The command accepts multiple scheduler IDs which results in opening
  multiple browser tabs.

Options:
  --workflow  Instead of opening the scheduler page, open the page of the
              scheduled workflow.
```
## workflow scheduler list

List available scheduler.

Outputs a table or a list of scheduler IDs which can be used as
reference for the scheduler commands.

```shell-session
$ cmemc workflow scheduler list [OPTIONS]
```

```text
Usage: cmemc workflow scheduler list [OPTIONS]

  List available scheduler.

  Outputs a table or a list of scheduler IDs which can be used as reference
  for the scheduler commands.

Options:
  --raw       Outputs raw JSON.
  --id-only   Lists only task identifier and no labels or other meta data.
              This is useful for piping the IDs into other commands.
```
## workflow scheduler inspect

Display all meta data of a scheduler.

```shell-session
$ cmemc workflow scheduler inspect [OPTIONS] SCHEDULER_ID
```

```text
Usage: cmemc workflow scheduler inspect [OPTIONS] SCHEDULER_ID

  Display all meta data of a scheduler.

Options:
  --raw       Outputs raw JSON.
```
## workflow scheduler disable

Disable scheduler(s).

The command accepts multiple scheduler IDs which results in disabling
them one after the other.

```shell-session
$ cmemc workflow scheduler disable [OPTIONS] [SCHEDULER_IDS]...
```

```text
Usage: cmemc workflow scheduler disable [OPTIONS] [SCHEDULER_IDS]...

  Disable scheduler(s).

  The command accepts multiple scheduler IDs which results in disabling them
  one after the other.

Options:
  -a, --all   Disable all scheduler.
```
## workflow scheduler enable

Enable scheduler(s).

The command accepts multiple scheduler IDs which results in enabling
them one after the other.

```shell-session
$ cmemc workflow scheduler enable [OPTIONS] [SCHEDULER_IDS]...
```

```text
Usage: cmemc workflow scheduler enable [OPTIONS] [SCHEDULER_IDS]...

  Enable scheduler(s).

  The command accepts multiple scheduler IDs which results in enabling them
  one after the other.

Options:
  -a, --all   Enable all scheduler.
```
