---
title: "cmemc: Command Group - admin logs"
description: "List log lines and get the state of the log buffers."
icon: material/text-box-search-outline
tags:
  - cmemc
  - Logging
  - Debugging
---

# admin logs Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List log lines and get the state of the log buffers.

Each backend of Corporate Memory which keeps its most recent log lines in an in-memory buffer is a job here, under the same job names the `admin metrics` commands use. This command group reads those buffers, which is the fastest way to find out what a failing request did on the server.

!!! note
    SPARQL queries have their own, more specific command: `query status` gives you information about the last executed queries.



## admin logs list

List the most recent log lines of the jobs.

```shell-session title="Usage"
cmemc admin logs list [OPTIONS]
```




Outputs the log lines which the jobs still hold in their in-memory buffer, newest last. Use the ``--filter`` option to narrow the output down; the `level`, `logger` and `contains` filters are applied by the job, so the ``--limit`` counts the lines which match them. A filter which can be given more than once requires all of its values to match.

The TIME column of the table shows your local time and names its offset, while the ``--plain`` and ``--raw`` output use the UTC timestamps the jobs sent. A `(+)` in front of a message marks a line which carries a stack trace; use ``--plain`` or ``--raw`` to read it.

!!! note
    Each instance of a job buffers its own lines, so in a deployment with more than one instance the answer comes from whichever instance was asked, which the output names. Use the `admin logs status` command to see how far back a buffer reaches.


!!! note
    With `--follow` on a terminal, the live table is a viewport rather than a result set: it is filled to the height of your terminal and therefore shows as many lines as fit, which can be more than `--limit`.


!!! note
    To investigate SPARQL queries, the `query status` command is the better tool: it gives you information about the last executed queries, instead of whatever the jobs happened to log about them.




??? info "Options"
    ```text

    --filter <TEXT TEXT>...         Filter log lines by one of the following
                                    filter names and a corresponding value:
                                    level, logger, contains, job, newer-than,
                                    older-than.
    --limit INTEGER RANGE           How many lines to output. The lines of all
                                    jobs are merged and the newest ones are
                                    shown, so this counts across jobs. Use 0 to
                                    get as many lines as the jobs are willing to
                                    return.  [default: 20; x>=0]
    --plain                         Outputs plain log lines instead of a table.
                                    Nothing is shortened, the timestamps are the
                                    UTC ones the jobs sent, and a stack trace is
                                    output as an indented block below its line.
    --raw                           Outputs raw JSON.
    --follow                        Keeps the command running and outputs new
                                    log lines as they arrive. On a terminal, the
                                    table is updated in place and filled to the
                                    height of the terminal, so it can show more
                                    lines than --limit; otherwise, lines are
                                    appended. Can not be combined with the
                                    older-than filter, which looks at the past.
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between two log
                                    reads while following. Applies together with
                                    --follow only, and is ignored when a read
                                    reports that more lines are already waiting.
                                    [default: 1; 0<=x<=60]
    ```

## admin logs status

Get the state of the in-memory log buffers.

```shell-session title="Usage"
cmemc admin logs status [OPTIONS]
```




Outputs whether log lines are captured at all, at which level, how many are held, which time span they cover and which loggers are excluded. Use this command to find out why the `admin logs list` command returns fewer lines than expected, or none.

The buffers of all jobs are shown as one structure, with the job as the first level of every key. Use ``--key` build.capacity` to address a single value of a single job, and ``--key`build` to see one job only.

!!! note
    `firstTimestamp` and `lastTimestamp` are not part of the answer of a job. The status of a buffer names the sequence numbers it spans but no times, so cmemc reads the oldest and the newest buffered line to tell you how far back the buffer reaches. They are shown in your local time, as the TIME column of the `admin logs list` table is, so that the two can be compared; `--raw` keeps the UTC the jobs sent.




??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    --key TEXT  Get a specific key only. If the given value is the prefix of
                more than one key, the table is reduced to these keys. Use `all`
                to output the complete table.
    ```
