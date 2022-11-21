---
status: new
title: cmemc (Overview)
subtitle: Command Line Interface
description: cmemc is the eccenca Corporate Memory command line interface.
icon: octicons/terminal-16
hide:
  - toc
tags:
  - cmemc
  - Automate
---
# cmemc - Command Line Interface

<div class="grid cards" markdown>

-   :octicons-terminal-16: **Command Line** interface for **eccenca Corporate Memory**

    ---

    Developed with **:simple-python: Python** and publicly available as a **pypi.org Package** and a **:simple-docker: Docker Image** under the **:material-license: Apache 2 License**.

    ---

    **Next Steps**: [:material-download-circle-outline:](installation/index.md "Installation")
        :material-plus: [:material-cog-outline:](configuration/file-based-configuration/index.md "Configuration")
        :material-plus: [:material-rocket-launch-outline:](configuration/completion-setup/index.md "Completion Setup")
        :material-equal: :sparkles:{ title="Fun :-)" }

    ---

    [![Python Version](https://img.shields.io/pypi/pyversions/cmem-cmemc.svg "Python Version"){ .off-glb }](https://pypi.org/project/cmem-cmemc/)
    [![pypi package](https://badge.fury.io/py/cmem-cmemc.svg "pypi package"){ .off-glb }](https://pypi.python.org/pypi/cmem-cmemc/)
    [![pypy downloads](https://img.shields.io/pypi/dm/cmem-cmemc.svg "pypy downloads"){ .off-glb }](https://pypi.python.org/pypi/cmem-cmemc/)
    [![Docker Image](https://img.shields.io/badge/docker-image-blue?logo=docker&logoColor=white "Docker Image"){ .off-glb }](./invocation/docker-image/index.md)

-   :octicons-people-24: Intended for **Administrators** and **Linked Data Expert**

    ---

    Battle tested in many projects to **:simple-powerautomate: Automate Activities** and **:material-remote: Remote Control** eccenca Corporate Memory instances.

    ``` shell-session title="Example: List datasets with a specific tag and project."
    $ cmemc -c prod.knowledge.company.org # (1)!
      dataset list \
      --filter project crm-graph \
      --filter tag velocity-daily
    ```

    1.  :person_raising_hand:
        - The option `-c` is short for `--connection` and references to a remote Corporate Memory instance.
        - The `list` command in the `dataset` command group shows all datasets of an instance.
        - In order to manipulate output dataset list, the `--filter` option takes two parameter, a filter type (`tag`, `project`, ...) and a value.


-   :octicons-rocket-16: Fast ad-hoc Execution with **Command Completion**

    ---

    <figure markdown>
      ![cmemc - Create Dataset](configuration/completion-setup/22.1-cmemc-create-dataset.gif "cmemc - Create Dataset")
      <figcaption>Create Build Project and Dataset</figcaption>
    </figure>


-   :material-feature-search-outline: **Main Features**:

    ---

    Manage (`list`, `inspect`, `import`, `export`, ...) and Manipulate (`create`, `delete`, `execute`, ...) Vocabularies, Datasets, :simple-semanticweb: Knowledge Graphs, [:octicons-workflow-24: Workflows](workflow-execution-and-orchestration/index.md), Projects, Queries, Scheduler, Configurations and [much more](command-reference/index.md).

    ``` shell-session title="Example: Backup the query catalog including imports."
    $ cmemc graph export \
      https://ns.eccenca.com/data/queries/ \
      --include-imports --output-dir queries \
      --filename-template "{{date}}-{{iriname}}"
    ```

</div>

