---
title: "cmemc: Command Group - admin metrics"
description: "List and get metrics."
icon: material/chart-line-variant
tags:
  - cmemc
---
# admin metrics Command Group

List and get metrics.

This command group consists of commands for reading and listing
internal monitoring metrics of eccenca Corporate Memory. A
deployment consists of multiple jobs (e.g. DP, DI), which provide
multiple metric families on an endpoint.

Each metric family can consist of different samples identified by
labels with a name and a value (dimensions). A metric has a specific
type (counter, gauge, summary and histogram) and additional metadata.

Please have a look at https://prometheus.io/docs/concepts/data_model/
for further details.

## admin metrics get

Get sample data of a metric.

A metric of a specific job is identified by a metric ID. Possible
metric IDs of a job can be retrieved with the `metrics list`
command. A metric can contain multiple samples.
These samples are distinguished by labels (name and value).

```shell-session
$ cmemc admin metrics get [OPTIONS] METRIC_ID
```

```text
Usage: cmemc admin metrics get [OPTIONS] METRIC_ID

  Get sample data of a metric.

  A metric of a specific job is identified by a metric ID. Possible metric
  IDs of a job can be retrieved with the `metrics list` command. A metric
  can contain multiple samples. These samples are distinguished by labels
  (name and value).

Options:
  --job [DP]               The job from which the metrics data is fetched.
                           [default: DP]

  --filter <TEXT TEXT>...  A set of label name/value pairs in order to filter
                           the samples of the requested metric family. Each
                           metric has a different set of labels with different
                           values. In order to get a list of possible label
                           names and values, use the command without this
                           option. The label names are then shown as column
                           headers and label values as cell values of this
                           column.

  --enforce-table          A single sample value will be returned as plain
                           text instead of the normal table. This allows for
                           more easy integration with scripts. This flag
                           enforces the use of tabular output, even for single
                           row tables.

  --raw                    Outputs raw prometheus sample classes.
```
## admin metrics inspect

Inspect a metric.

This command outputs the data of a metric.
The first table includes basic meta data about the metric.
The second table includes sample labels and values.

```shell-session
$ cmemc admin metrics inspect [OPTIONS] METRIC_ID
```

```text
Usage: cmemc admin metrics inspect [OPTIONS] METRIC_ID

  Inspect a metric.

  This command outputs the data of a metric. The first table includes basic
  meta data about the metric. The second table includes sample labels and
  values.

Options:
  --job [DP]  The job from which the metrics data is fetched.  [default: DP]
  --raw       Outputs raw JSON of the table data.
```
## admin metrics list

List metrics for a specific job.

For each metric, the output table shows the metric ID,
the type of the metric, a count of how many labels (label names)
are describing the samples (L) and a count of how many samples are
currently available for a metric (S).

```shell-session
$ cmemc admin metrics list [OPTIONS]
```

```text
Usage: cmemc admin metrics list [OPTIONS]

  List metrics for a specific job.

  For each metric, the output table shows the metric ID, the type of the
  metric, a count of how many labels (label names) are describing the
  samples (L) and a count of how many samples are currently available for a
  metric (S).

Options:
  --job [DP]  The job from which the metrics data is fetched.  [default: DP]
  --id-only   Lists metric identifier only. This is useful for piping the IDs
              into other commands.

  --raw       Outputs (sorted) JSON dict, parsed from the metrics API output.
```
