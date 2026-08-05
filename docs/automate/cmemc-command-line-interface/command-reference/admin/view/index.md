---
title: "cmemc: Command Group - admin view"
description: "List and update explore application view configurations."
icon: octicons/cross-reference-24
tags:
  - cmemc
---
# admin view Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List and update explore application view configurations.

This command group manages Explore (DataPlatform) application view configurations. Application view configurations control the behavior of specific Explore view profiles including companion services and other settings.


## admin view list

List explore application view configurations.

```shell-session title="Usage"
$ cmemc admin view list [OPTIONS]
```




Outputs a list of application view configurations from the Explore component. The default application view (id: 'default') is always listed first, followed by any custom application view configurations.

Profile IDs can be used as a reference for the other commands of the `admin view` command group.



??? info "Options"
    ```text

    --raw                    Outputs raw JSON.
    --id-only                Lists only profile IDs. This is useful for piping
                             the IDs into other commands.
    --filter <TEXT TEXT>...  Filter application view configurations by one of
                             the following filter names and a corresponding
                             value: id, label.
    ```

## admin view export

Export application view configurations to a JSON file.

```shell-session title="Usage"
$ cmemc admin view export [OPTIONS] [PROFILE_IDS]...
```




Application view configurations can be exported based on profile IDs, filters, or all at once. The exported JSON can be imported back using the `admin view import` command.

```shell-session title="Example"
$ cmemc admin view export --all
```


```shell-session title="Example"
$ cmemc admin view export --all --output-file configs.json
```


```shell-session title="Example"
$ cmemc admin view export --filter id my-view
```


```shell-session title="Example"
$ cmemc admin view export my-view
```




??? info "Options"
    ```text

    -a, --all                     Export all application view configurations.
    --filter <TEXT TEXT>...       Filter application view configurations by one
                                  of the following filter names and a
                                  corresponding value: id, label.
    --output-file FILE            Export to this file. Use '-' for stdout. If
                                  specified, overrides --output-dir and
                                  --filename-template.
    --output-dir DIRECTORY        The base directory where the export file will
                                  be created. Ignored if --output-file is
                                  specified.  [default: .]
    -t, --filename-template TEXT  Template for the export file name. Possible
                                  placeholders are (Jinja2): {{connection}}
                                  (from the --connection option) and {{date}}
                                  (the current date as YYYY-MM-DD). Ignored if
                                  --output-file is specified.  [default:
                                  {{date}}-{{connection}}.view-configs.json]
    --replace                     Replace an existing export file. This is a
                                  dangerous option, so use it with care.
    ```

## admin view import

Import application view configurations from a JSON file.

```shell-session title="Usage"
$ cmemc admin view import [OPTIONS] INPUT_FILE
```




This command imports application view configurations from a JSON file that was created using the `admin view export` command.

If `--replace` is specified, existing configurations with the same profile ID will be updated. Otherwise, existing configurations will be skipped.

!!! note
    Importing the default application view configuration updates the project-level overrides stored in /api/conf/workspaces/projectDefault.


```shell-session title="Example"
$ cmemc admin view import configs.json
```


```shell-session title="Example"
$ cmemc admin view import --replace configs.json
```




??? info "Options"
    ```text

    --replace   Replace existing application view configurations. By default,
                import will skip configurations that already exist.
    --id TEXT   Import the configuration under this profile ID instead of the
                one stored in the file.
    ```

## admin view delete

Delete custom application view configurations.

```shell-session title="Usage"
$ cmemc admin view delete [OPTIONS] [PROFILE_IDS]...
```




!!! warning
    Application view configurations will be deleted without prompting.


!!! note
    The default application view configuration cannot be deleted. Use the `admin view list` command to list available application view configurations.




??? info "Options"
    ```text

    -a, --all                Delete all custom application view configurations.
                             This is a dangerous option, so use it with care.
    --filter <TEXT TEXT>...  Filter application view configurations by one of
                             the following filter names and a corresponding
                             value: id, label.
    ```

## admin view create

Create a new explore application view configuration.

```shell-session title="Usage"
$ cmemc admin view create [OPTIONS] PROFILE_ID
```




The new profile is created with its ID and label only. Use the `admin view update` command to set configuration values such as enableCompanion or module toggles.

!!! note
    Application view configurations can be listed with the `admin view list` command.




??? info "Options"
    ```text

    --label TEXT  Label for the application view configuration. Defaults to the
                  profile ID.
    ```

## admin view update

Update a key in an existing explore application view configuration.

```shell-session title="Usage"
$ cmemc admin view update [OPTIONS] PROFILE_ID
```




Any configuration key can be updated, including nested module keys. All other fields are preserved.

```shell-session title="Example"
$ cmemc admin view update my-profile --key enableCompanion --value true
```


```shell-session title="Example"
$ cmemc admin view update my-profile --key modules.marketplaceModuleConfiguration.enabled --value false
```




??? info "Options"
    ```text

    --key TEXT    The configuration key to update. Supports nested keys using
                  'a.b[i].c' notation, e.g.
                  modules.marketplaceModuleConfiguration.enabled.  [required]
    --value TEXT  The new value. Parsed as JSON when possible (e.g. true, false,
                  1), otherwise used as a plain string.  [required]
    ```

## admin view inspect

Inspect the configuration of an application view profile.

```shell-session title="Usage"
$ cmemc admin view inspect [OPTIONS] PROFILE_ID
```




For accessing nested configuration values, use the following notation: exploreGraphLists[4].comments[0]

!!! note
    Some shell environments require quotes around expressions with square brackets.


Examples: cmemc admin view inspect my-profile

cmemc admin view inspect my-profile `--key` enable

cmemc admin view inspect my-profile `--key` "exploreGraphLists[4].comments[0]"




??? info "Options"
    ```text

    --key TEXT  Get a specific key only from the configuration.
    --raw       Outputs raw JSON.
    ```

