---
title: "cmemc: Configuration"
icon: material/cog-outline
tags:
  - cmemc
hide:
  - toc
---
# Configuration

In order to work with cmemc, you have to configure it according to your needs.

<div class="grid cards" markdown>

- :material-file-cog-outline: File-based Configuration

    ---

    The most common way to configure cmemc is with a central [configuration file](file-based-configuration/index.md).

- :material-cog-outline: Environment-based Configuration

    ---

    In addition to configuration files, cmemc can be widely configured and parameterized with [environment variables](environment-based-configuration/index.md).

- :material-rocket-launch: Completion Setup

    ---

    Setting up [command completion](completion-setup/index.md) is optional but highly recommended and will greatly speed up your cmemc terminal sessions.

- :material-key-link: Security Considerations

    ---

    cmemc can be configured to fetch your [credentials from external processes](getting-credentials-from-external-processes/index.md), such as password stores.
    In addition to that, cmemc can work with [custom certificates](certificate-handling-and-ssl-verification/index.md).

</div>

## Configuration value resolution order

When the same key is defined in multiple places, cmemc resolves values in the following order:

1. **Named connection section** — When you run cmemc with a specific connection (e.g. `-c my-connection`),
all keys from the corresponding `[my-connection]` section are used. This takes full precedence,
including over OS environment variables, so you can define self-contained, reproducible
connection profiles that are not affected by your shell environment.

2. **Environment variables** — If a key is set as an environment variable and no named connection
section is active, the environment variable value is used.

3. **`[DEFAULT]` section** — The `[DEFAULT]` section in [`cmemc.ini`](file-based-configuration/index.md) acts as a fallback
for all connections. Its values are ignored if the same key is already set as an environment variable.
Keys present in the `[DEFAULT]` section but absent from the named connection section still apply as a fallback.
