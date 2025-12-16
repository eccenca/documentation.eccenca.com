---
title: "cmemc: Command Group - workflow scheduler"
description: "List, inspect, enable/disable or open scheduler."
icon: material/calendar
tags:
  - Automate
  - cmemc
---
# workflow scheduler Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, inspect, enable/disable or open scheduler.

Schedulers execute workflows in specified intervals. They are identified with a `SCHEDULER_ID`. To get a list of existing schedulers, execute the list command or use tab-completion.

## workflow scheduler open

Open scheduler(s) in the browser.

```shell-session title="Usage"
cmemc workflow scheduler open [OPTIONS] SCHEDULER_IDS...
```

With this command, you can open a scheduler in the workspace in your browser to change it.

The command accepts multiple scheduler IDs which results in opening multiple browser tabs.

??? info "Options"
    ```text

    --workflow  Instead of opening the scheduler page, open the page of the
                scheduled workflow.
    ```

## workflow scheduler list

List available scheduler.

```shell-session title="Usage"
cmemc workflow scheduler list [OPTIONS]
```

Outputs a table or a list of scheduler IDs which can be used as reference for the scheduler commands.

??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    --id-only   Lists only task identifier and no labels or other metadata. This
                is useful for piping the IDs into other commands.
    ```

## workflow scheduler inspect

Display all metadata of a scheduler.

```shell-session title="Usage"
cmemc workflow scheduler inspect [OPTIONS] SCHEDULER_ID
```

??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## workflow scheduler disable

Disable scheduler(s).

```shell-session title="Usage"
cmemc workflow scheduler disable [OPTIONS] [SCHEDULER_IDS]...
```

The command accepts multiple scheduler IDs which results in disabling them one after the other.

??? info "Options"
    ```text

    -a, --all   Disable all scheduler.
    ```

## workflow scheduler enable

Enable scheduler(s).

```shell-session title="Usage"
cmemc workflow scheduler enable [OPTIONS] [SCHEDULER_IDS]...
```

The command accepts multiple scheduler IDs which results in enabling them one after the other.

??? info "Options"
    ```text

    -a, --all   Enable all scheduler.
    ```
