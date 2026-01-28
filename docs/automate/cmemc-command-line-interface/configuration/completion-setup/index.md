---
title: "cmemc: Command-Line Completion"
icon: material/rocket-launch
tags:
  - cmemc
  - Video
---
# Command-Line Completion

## Introduction

In case you are using bash or zsh as your terminal shell, you should enable [Command-line tab completion](https://en.wikipedia.org/wiki/Command-line_completion) for cmemc.

Tab completion is a powerful feature and will save you a lot of typing work.
Furthermore, it will help you to learn the different commands, parameters and options and will auto-complete parameter values taken live from your Corporate Memory instance (such as graph IRIs, project IDs, etc.).

![cmemc - Create Dataset](22.1-cmemc-create-dataset.gif "cmemc - Create Dataset")

We suggest using [zsh](https://en.wikipedia.org/wiki/Z_shell) so you can take advantage of its advanced menu-completion feature.

## Installation

!!! info

    The installation commands for the completion recently changed.
    Use the following lines for the completion setup of cmemc >= 23.3.
    If using an older version, look at the [old documenation](https://documentation.eccenca.com/23.1/automate/cmemc-command-line-interface/configuration/completion-setup/).


In order to enable tab completion with **zsh** run the following command:

``` shell-session title="completion setup for zsh"
$ eval "$(_CMEMC_COMPLETE=zsh_source cmemc)"
```

!!! note "Windows / msys2"

    When using zsh on Windows with msys2, you need to strip carriage returns to avoid parse errors:

    ``` shell-session title="completion setup for zsh on Windows/msys2"
    $ eval "$(_CMEMC_COMPLETE=zsh_source cmemc | tr -d '\r')"
    ```

To enable the interactive menu as seen above in **zsh** run the following command:

``` shell-session title="interactive menu for zsh"
$ zstyle ':completion:*' menu select
```

In order to enable tab completion with **bash** run the following command:

``` shell-session title="completion setup for bash"
$ eval "$(_CMEMC_COMPLETE=bash_source cmemc)"
```

You may want to add this line to your `.bashrc` or `.zshrc`.


