---
title: "cmemc: Command Group - admin migration"
description: "List and apply migration recipes."
icon: material/database-arrow-up-outline
tags:
  - cmemc
---
# admin migration Command Group
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->

List and apply migration recipes.

With this command group, you can check your instance for needed migration activities as well as apply them to your data.

Beside an ID and a description, migration recipes have the following metadata: 'First Version' is the first Corporate Memory version, where this recipe is maybe applicable. The recipe will never be applied to a version below this version. 'Tags' is a classification of the recipe with regard to the target data, it migrates.

The following tags are important: `system` recipes target data structures which are needed to run the most basic functionality properly. These recipes can and should be applied after each version upgrade. `user` recipes can change user and / or customizing data. `acl` recipes migrate access condition data. `shapes` recipes migrate shape data. `config` recipes migrate configuration data.


## admin migration list

List migration recipies.

```shell-session title="Usage"
$ cmemc admin migration list [OPTIONS]
```




This command lists all available migration recipies



??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter migration recipes by one of the following
                             filter names and a corresponding value: id,
                             description, first_version, tag.
    --id-only                Lists only IDs. This is useful for piping the IDs
                             into other commands.
    --raw                    Outputs raw JSON.
    ```

## admin migration execute

Execute needed migration recipes.

```shell-session title="Usage"
$ cmemc admin migration execute [OPTIONS] [MIGRATION_ID]
```




This command executes one or more migration recipes. Each recipe has a check method to determine if a migration is needed. In addition to that, the current component version needs to match the specified first-last-version range of the recipe.

Recipes are executed ordered by first_version.

Here are some argument examples, in order to see how to use this command: execute `--all` `--test-only` will list all needed migrations (but not execute them), execute `--filter` tag system will apply all migrations which target system data, execute bootstrap-data will apply bootstrap-data migration if needed.



??? info "Options"
    ```text

    --filter <TEXT TEXT>...  Filter migration recipes by one of the following
                             filter names and a corresponding value: id,
                             description, first_version, tag.
    -a, --all                Execute all needed migrations.
    --test-only              Only test, do not execute migrations.
    --id-only                Lists only recipe identifier.
    ```

