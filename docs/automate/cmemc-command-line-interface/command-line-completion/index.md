---
tags:
  - cmemc
---
# cmemc Command-Line Completion

## Introduction

In case you are using bash or zsh as your terminal shell, you should enable [Command-line tab completion](https://en.wikipedia.org/wiki/Command-line_completion) for cmemc.

Tab completion is a powerful feature and will save you a lot of typing work.
Furthermore, it will help you to learn the different commands, parameters and options and will auto-complete parameter values taken live from your Corporate Memory instance (such as graph IRIs, project IDs, ...).

![cmemc - Create Dataset](22.1-cmemc-create-dataset.gif "cmemc - Create Dataset")

We suggest to use [zsh](https://en.wikipedia.org/wiki/Z_shell) so you can take advantage of the advanced menu-completion feature of zsh.

## Installation

In order to enable tab completion with **zsh** run the following command:

``` shell-session title="completion setup for zsh"
$ eval "$(_CMEMC_COMPLETE=source_zsh cmemc)"
```

In order to enable tab completion with **bash** run the following command:

``` shell-session title="completion setup for bash"
$ eval "$(_CMEMC_COMPLETE=source cmemc)"
```

You may want to add this line to your `.bashrc` or `.zshrc`.


