---
title: "cmemc: Command Group - project rule-block"
description: "List, inspect, create, delete, import or export project rule blocks."
icon: material/function-variant
tags:
  - Transform
  - cmemc
---

# project rule-block Command Group

<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List, inspect, create, delete, import or export project rule blocks.

A rule block is a named, reusable operator tree with declared input ports, comparable to a function in a programming language. Transform and linking rules reference a rule block instead of repeating its operators, so a correction made in the rule block reaches every rule that uses it.

Rule blocks are identified by a `RULE_BLOCK_ID`, which is a concatenation of a `PROJECT_ID` and the ID of the rule block, such as `my-project:normalize-name`.

!!! note
    To get a list of existing rule blocks, execute the `list` command or use tab-completion. Rule blocks need Corporate Memory 26.2 or newer.



## project rule-block list

List available rule blocks.

```shell-session title="Usage"
cmemc project rule-block list [OPTIONS]
```




Output and filter a list of available rule blocks. Each rule block is listed with its ID, its number of input ports and its label.

Filters are applied in the order they are given on the command line. The `usage` filter resolves the dependents of each remaining rule block, so putting a cheaper filter such as `project` in front of it reduces the number of requests it has to make.



??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter rule blocks by one of the following filter
                             names and a corresponding value: project, regex,
                             tag, usage, deprecated.
    --raw                    Outputs raw JSON objects of the rule blocks.
    --id-only                Lists only rule block IDs and no labels or other
                             metadata. This is useful for piping the IDs into
                             other cmemc commands.
    ```

## project rule-block inspect

Display all metadata of a rule block.

```shell-session title="Usage"
cmemc project rule-block inspect [OPTIONS] RULE_BLOCK_ID
```




The complete rule block is shown as a flat key and value table: its metadata, each declared input port with its label, display order and deprecation state, and the operator tree.

For accessing nested values, use the following notation: `ruleBlockModel.ports[0].label`

!!! note
    Some shell environments require quotes around expressions with square brackets.


```shell-session title="Example"
cmemc project rule-block inspect my-project:normalize-name
```


```shell-session title="Example"
cmemc project rule-block inspect my-project:normalize-name --key "ruleBlockModel.ports[0].label"
```





??? info "Options"
    ```text

    --key TEXT  Get a specific key only. If the given value is the prefix of
                more than one key, the table is reduced to these keys. Use `all`
                to output the complete table.
    --raw       Outputs raw JSON.
    ```

## project rule-block open

Open rule blocks in the browser.

```shell-session title="Usage"
cmemc project rule-block open RULE_BLOCK_IDS...
```




With this command, you can open a rule block in the Rule Block Editor in your browser.

The command accepts multiple rule block IDs which results in opening multiple browser tabs.



## project rule-block usage

Display all tasks which use a rule block.

```shell-session title="Usage"
cmemc project rule-block usage [OPTIONS] RULE_BLOCK_ID
```




Tasks which reference the rule block directly, such as a transformation with a rule block operator, are listed as direct users. Tasks which reference one of those in turn, such as a workflow containing that transformation, are listed as indirect users. Deleting the rule block together with its dependent tasks deletes all of them.



??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```

## project rule-block create

Create an empty rule block.

```shell-session title="Usage"
cmemc project rule-block create [OPTIONS] RULE_BLOCK_ID
```




The new rule block has no input ports and no operator tree yet. Open it with the `open` command to build it in the Rule Block Editor, or fill it with the `import` command from an exported file.

```shell-session title="Example"
cmemc project rule-block create normalize-name --project my-project --label "Normalize Name"
```




??? info "Options"
    ```text

    --project TEXT      The project, where the rule block will be created. If
                        there is only one project in the workspace, this option
                        can be omitted.
    --label TEXT        The label of the new rule block.
    --description TEXT  The description of the new rule block.
    ```

## project rule-block update

Update a key of an existing rule block.

```shell-session title="Usage"
cmemc project rule-block update [OPTIONS] RULE_BLOCK_ID
```




Any key shown by the `inspect` command can be updated, including nested keys such as the label or the deprecation state of an input port. All other values are preserved.

!!! note
    A new input port cannot be added this way, because a list index that does not exist yet cannot be addressed. Add input ports in the Rule Block Editor, or use `export`, edit the file, and `import --replace`.


```shell-session title="Example"
cmemc project rule-block update my-project:normalize-name --key label --value "Normalize Person Name"
```


```shell-session title="Example"
cmemc project rule-block update my-project:normalize-name --key "ruleBlockModel.ports[1].deprecated" --value true
```




??? info "Options"
    ```text

    --key TEXT    The key to update. Supports nested keys using 'a.b[i].c'
                  notation, e.g. ruleBlockModel.ports[0].deprecated.  [required]
    --value TEXT  The new value. Parsed as JSON when possible (e.g. true, false,
                  1), otherwise used as a plain string.  [required]
    ```

## project rule-block export

Export rule blocks to JSON files.

```shell-session title="Usage"
$ cmemc project rule-block export [OPTIONS] [RULE_BLOCK_IDS]...
```




The exported file holds the rule block as a task structure without its project, so it can be imported into any project with the `import` command.

!!! note
    The exported rule block is not necessarily self-contained. Its operator parameters can reference project variables and custom transformer plugins, and neither of those travels with the file, so an import into a different project can succeed and still leave a rule block which does not work.


```shell-session title="Example"
$ cmemc project rule-block export my-project:normalize-name --output-file normalize-name.json
```


```shell-session title="Example"
$ cmemc project rule-block export --filter project my-project --output-dir backup -t "{{project}}/{{id}}"
```




??? info "Options"
    ```text

    -a, --all                     Export all rule blocks.
    --filter <TEXT TEXT>...       Filter rule blocks by one of the following
                                  filter names and a corresponding value:
                                  project, regex, tag, usage, deprecated.
    --output-file FILE            Export to this file. Use '-' for stdout. Only
                                  allowed with a single rule block. If
                                  specified, overrides --output-dir and
                                  --filename-template.
    --output-dir DIRECTORY        The base directory where the export files will
                                  be created. Ignored if --output-file is
                                  specified.  [default: .]
    -t, --filename-template TEXT  Template for the export file name(s). Possible
                                  placeholders are (Jinja2): {{id}} (the rule
                                  block ID), {{project}} (the project ID),
                                  {{connection}} (from the --connection option)
                                  and {{date}} (the current date as YYYY-MM-DD).
                                  The file suffix will be appended. Needed
                                  directories will be created.  [default: {{date
                                  }}-{{connection}}-{{project}}-{{id}}.rule-
                                  block]
    --replace                     Replace existing export files. This is a
                                  dangerous option, so use it with care.
    --without-userdata            Exclude user-identifying metadata (creation
                                  and modification timestamps and account names)
                                  from the exported files.
    ```

## project rule-block import

Import rule blocks from JSON files.

```shell-session title="Usage"
cmemc project rule-block import [OPTIONS] INPUT_FILES...
```




This command imports rule blocks from JSON files created with the `export` command. A file does not record its source project, so the same file can be imported into any project.

!!! note
    The imported rule block is not necessarily self-contained. Its operator parameters can reference project variables and custom transformer plugins, and neither of those travels with the file.


```shell-session title="Example"
cmemc project rule-block import normalize-name.json --project my-other-project
```




??? info "Options"
    ```text

    --project TEXT  The project, where the rule blocks will be imported. If
                    there is only one project in the workspace, this option can
                    be omitted.
    --replace       Replace existing rule blocks. By default, import will skip
                    rule blocks that already exist.
    --id TEXT       Import the rule block under this ID instead of the one
                    stored in the file.
    ```

## project rule-block delete

Delete rule blocks.

```shell-session title="Usage"
cmemc project rule-block delete [OPTIONS] [RULE_BLOCK_IDS]...
```




Deleting a rule block which other tasks reference is refused, because DataIntegration would leave those tasks pointing at something that no longer exists and would report the breakage nowhere. Use the ``--with-dependent-tasks`` option to delete the rule block together with every task which references it, directly or indirectly. Use the `usage` command to see who those are beforehand.

When several rule blocks are selected, all of them are checked first, and nothing is deleted if one of them is used.

```shell-session title="Example"
cmemc project rule-block delete my-project:normalize-name
```


```shell-session title="Example"
cmemc project rule-block delete --filter usage unused
```




??? info "Options"
    ```text

    -a, --all                Delete all rule blocks. This is a dangerous option,
                             so use it with care.
    --filter <TEXT TEXT>...  Filter rule blocks by one of the following filter
                             names and a corresponding value: project, regex,
                             tag, usage, deprecated.
    --with-dependent-tasks   Also delete every task which directly or indirectly
                             references the rule block. This is a dangerous
                             option, so use it with care.
    ```

## project rule-block eval

Evaluate a rule block against its stored input examples.

```shell-session title="Usage"
cmemc project rule-block eval [OPTIONS] RULE_BLOCK_ID
```




The input examples are the ones stored with the rule block in the Rule Block Editor. Each example is listed with the values it feeds into the input ports and the values the rule block produces from them. An example which fails to evaluate shows the failing operator and its error message instead of a result.

Use ``--raw`` to get the complete evaluation tree, which also carries the intermediate values of every operator and the stack trace of a failure.

!!! note
    A rule block can only be evaluated as part of a project. There is no way to evaluate an exported file without importing it first.


```shell-session title="Example"
cmemc project rule-block eval my-project:normalize-name
```




??? info "Options"
    ```text

    --raw       Outputs raw JSON.
    ```
