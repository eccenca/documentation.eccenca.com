---
title: "cmemc: Command Group - graph validation"
description: "Validate resources in a graph."
icon: octicons/verified-16
tags:
  - KnowledgeGraph
  - Validation
  - cmemc
---

# graph validation Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

Validate resources in a graph.

This command group is dedicated to the management of resource validation processes. A validation process verifies, that resources in a specific graph are valid according to the node shapes in a shape catalog graph.

!!! note
    Validation processes are identified with a random ID and can be listed with the `graph validation list` command. To start or cancel validation processes, use the `graph validation execute` and `graph validation cancel` command. To inspect the found violations of a validation process, use the `graph validation inspect` command.

## graph validation execute

Start a new validation process.

```shell-session title="Usage"
cmemc graph validation execute [OPTIONS] IRI
```

Validation is performed on all typed resources of the data / context graph (and its sub-graphs). Each resource is validated against all applicable node shapes from the shape catalog.

??? info "Options"
    ```text

    --wait                          Wait until the process is finished. When
                                    using this option without the `--id-only`
                                    flag, it will enable a progress bar and a
                                    summary view.
    --shape-graph TEXT              The shape catalog used for validation.
                                    [default: https://vocab.eccenca.com/shacl/]
    --query TEXT                    SPARQL query to select the resources which
                                    you want to validate from the data graph.
                                    Can be provided as a local file or as a
                                    query catalog IRI. [default: all typed
                                    resources]
    --result-graph TEXT             (Optionally) write the validation results to
                                    a Knowledge Graph. [default: None]
    --replace                       Replace the result graph instead of just
                                    adding the new results. This is a dangerous
                                    option, so use it with care!
    --ignore-graph TEXT             A set of data graph IRIs which are not
                                    queried in the resource selection. This
                                    option is useful for validating only parts
                                    of an integration graph which imports other
                                    graphs.
    --id-only                       Return the validation process identifier
                                    only. This is useful for piping the ID into
                                    other commands.
    --inspect                       Return the list of violations instead of the
                                    summary (includes --wait).
    --polling-interval INTEGER RANGE
                                    How many seconds to wait between status
                                    polls. Status polls are cheap, so a higher
                                    polling interval is most likely not needed.
                                    [default: 1; x>=1]
    ```

## graph validation list

List running and finished validation processes.

```shell-session title="Usage"
cmemc graph validation list [OPTIONS]
```

This command provides a filterable table or identifier list of validation processes. The command operates on the process summary and provides some statistics.

!!! note
    Detailed information on the found violations can be listed with the `graph validation inspect` command.

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter validation processes by one of the following
                             filter names and a corresponding value: status,
                             context-graph, shape-graph, more-resources-than,
                             more-violations-than, more-violated-resources-than.
    --id-only                List validation process identifier only. This is
                             useful for piping the IDs into other commands.
    --raw                    Outputs raw JSON of the validation list.
    ```

## graph validation inspect

List and inspect errors found with a validation process.

```shell-session title="Usage"
cmemc graph validation inspect [OPTIONS] PROCESS_ID
```

This command provides detailed information on the found violations of a validation process.

Use the ``--filter`` option to limit the output based on different criteria such as constraint name (`constraint`), origin node shape of the rule (`node-shape`), or the validated resource (`resource`).

!!! note
    Validation processes IDs can be listed with the `graph validation list` command, or by utilizing the tab completion of this command.

??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter violations by one of the following filter
                             names and a corresponding value: constraint,
                             severity, resource, node-shape, source.
    --id-only                Return violated resource identifier only. This is
                             useful for piping the ID into other commands.
    --summary                Outputs the summary of the graph validation instead
                             of the violations list (not filterable).
    --raw                    Outputs raw JSON of the validation result.
    ```

## graph validation cancel

Cancel a running validation process.

```shell-session title="Usage"
cmemc graph validation cancel PROCESS_ID
```

!!! note
    In order to get the process IDs of all currently running validation processes, use the `graph validation list` command with the option `--filter status running`, or utilize the tab completion of this command.

## graph validation export

Export a report of finished validations.

```shell-session title="Usage"
cmemc graph validation export [OPTIONS] [PROCESS_IDS]...
```

This command exports a jUnit XML or JSON report in order to process them somewhere else (e.g. a CI pipeline).

You can export a single report of multiple validation processes.

For jUnit XML: Each validation process result will be transformed to a single test suite. All violations of one resource in a result will be collected and attached to a single test case in that test suite.

!!! note
    Validation processes IDs can be listed with the `graph validation list` command, or by utilizing the tab completion of this command.

??? info "Options"
    ```text

    --output-file FILE      Export the report to this file. Existing files will
                            be overwritten.  [default: report.xml]
    --exit-1 [never|error]  Specify, when this command returns with exit code 1.
                            Available options are 'never' (exit 0, even if there
                            are violations in the reports), 'error' (exit 1 if
                            there is at least one violation in a report).),
                            [default: error]
    --format [JSON|XML]     Export either the plain JSON report or a distilled
                            jUnit XML report.  [default: XML]
    ```
