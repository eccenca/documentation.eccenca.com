---
title: "Review the changes of an AI agent"
icon: material/source-commit
status: new
tags:
    - AdvancedTutorial
    - Automate
    - Project
---
# Review the changes of an AI agent

## Introduction

An AI agent changes a Build project of eccenca Corporate Memory through the Build MCP server.
This applies to the [Companion](../../explore-and-author/companion/index.md) in Corporate Memory and to an external agent such as Claude Code.
Every change of the agent is recorded in the [change journal](../change-journal/index.md) of the project and awaits review.
A workflow run that the agent requests is held back until these changes are reviewed, because the results of a run cannot be reverted.

This tutorial walks through one review from start to end:

- The agent adds two mapping rules to a transformation and requests a run of the workflow.
- The run is held back as a proposed run.
- One mapping rule is reverted, and the remaining changes are marked as reviewed.
- The next request of the agent runs the workflow.

Where the Companion and an external agent differ, a step shows both in separate tabs.

## Prerequisites

- An agent that works with Corporate Memory, one of the following:
    - The Companion, which the user has access to, see [Access](../../explore-and-author/companion/index.md#access).
    - An external agent that is connected to the Build MCP server, see [MCP](../../automate/agent-integration/index.md#mcp).
- The Build MCP server allows changes (`com.eccenca.di.assistant.McpConfig.readOnly = false`), see [Allow changes through the Build MCP server](../../automate/agent-integration/index.md#allow-changes-through-the-build-mcp-server).
- The review gate is enabled, which is the default (`com.eccenca.di.assistant.McpConfig.reviewGate = true`).
- The project **Product Feed** with a transformation and a workflow that runs it.
    Import the project file [`product-feed.project.zip`](product-feed.project.zip) in one of the following ways:

    - In Build, click **Create new**, select **Project**, click **Add**, then **Import project file**, and select the file.
    - With [cmemc](../../automate/cmemc-command-line-interface/index.md):

        ```shell
        cmemc -c my-cmem project import product-feed.project.zip product-feed
        ```

    Alternatively, create the project with the following contents:

    - The file `products.csv` with the columns `id`, `name`, `price` and `supplier`
    - The CSV dataset **Products (CSV)**, which reads `products.csv`
    - The transformation **Transform products**, which maps the column `name` to `https://schema.org/name`
    - The workflow **Load products**, which runs the transformation and writes the result into the Knowledge Graph dataset **Products (Knowledge Graph)**

    ```text
    id,name,price,supplier
    P-100,Resonator Transformer,0.79,Grant-Nelson
    P-101,Multiplexer Transistor,0.29,Mcpherson Ltd
    P-102,Crystal Oscillator,1.15,Hall-Hodges
    ```

!!! warning "The review covers only changes through the Build MCP server"

    An external agent that can also use cmemc or the Build API changes the project and runs workflows without review, with the permissions of its account.
    Such changes are recorded as changes of a person, and a workflow run starts right away.
    Give the agent access to Corporate Memory only through the Build MCP server, and use an account or client with limited permissions, see [Permissions of the agent](../../automate/agent-integration/index.md#permissions-of-the-agent).

## 1 Let the agent change the project

Give the agent a task that changes the project and runs a workflow:

=== "Companion"

    1. Open the project **Product Feed**.
    2. Click :eccenca-application-ai-suggestion: **Chat with the companion** in the application header.
    3. Select **Ask before writes** in the mode selector above the input field.
        A new chat starts in **Read only**, which does not change anything, see [Modes](../../explore-and-author/companion/chat/index.md#modes).
    4. Enter the task, for example:

        ```text
        In the project Product Feed, map the columns price and supplier of products.csv
        in the transformation Transform products to schema.org properties.
        Then run the workflow Load products.
        ```

    5. Click **Confirm** in the confirmation dialog of each change, see [Confirm a change](../../explore-and-author/companion/chat/index.md#confirm-a-change).

=== "External agent"

    Enter the task in the agent, for example:

    ```text
    In the project Product Feed, map the columns price and supplier of products.csv
    in the transformation Transform products to schema.org properties.
    Then run the workflow Load products.
    ```

The agent adds two mapping rules: `price`, which maps the column `price` to `https://schema.org/price`, and a rule that maps the column `supplier` to a schema.org property.
In this example, the rule for `supplier` is `brand`, which maps it to `https://schema.org/brand`.
The property that an agent selects can differ, for example `manufacturer`.
Then the agent requests the run of **Load products**.

The Build MCP server does not run the workflow.
It records the request as a proposed run and answers that the changes of the agent await review.
The answer contains a link to the **Changes** view of the project and instructs the agent to ask for the review and to request the run again afterwards.
How the agent passes this on depends on the agent.

The Companion links **Review changes** in its answer.
Below the chat, a panel counts the unreviewed changes:

- **Changes from this conversation** — the changes that the Companion made in this chat
- **Other changes awaiting review** — the unreviewed changes of the project from other sources
- A link that lists the unreviewed changes of the project
- A link that lists only the changes of this chat

![The answer of the Companion with the Review changes link and the panel with the unreviewed changes](review-agent-changes-companion.png){ class="bordered" width="70%" }

## 2 Open the review

=== "Companion"

    Click **Review changes** in the answer of the Companion, or a link in the panel below the chat.

=== "External agent"

    1. Open the project **Product Feed**.
        The **Changes** card states how many changes made by an agent await review.

        ![The Changes card of the project with three changes made by an agent awaiting review](review-agent-changes-card.png){ class="bordered" width="50%" }

    2. Click **Review changes**.

The **Changes** view of the project opens.
**Unreviewed changes: 3** above the list counts the changes of the agent: the two mapping rules and the proposed run.
They are highlighted, show an AI icon in the **Source** column and carry the tag **Unreviewed**.
The proposed run carries the tag **Run**.

![The Changes view with the proposed run and the two mapping rules of the agent awaiting review](review-agent-changes-unreviewed.png){ class="bordered" }

The facets on the left of the **Changes** view filter the list.
To list only the changes of the agent, select a checkbox in one of these facets:

=== "Companion"

    Under **CONVERSATION**, select the chat of the Companion, for example **C1**.
    The facet lists each Companion chat that changed the project.

    A change of the Companion also shows its chat as a tag such as **C1** in the **Source** column.
    Click the tag to filter the list by this chat, or click **Open companion conversation** in the row to open the chat in the Companion panel.

    ![The Changes view filtered to the unreviewed changes of one Companion chat](review-agent-changes-companion-journal.png){ class="bordered" }

=== "External agent"

    Under **ORIGIN**, select the client name of the agent, here `mcp:claude-code`.
    The facet lists **Person** for changes made in the user interface or through the API, and the client name of each agent that changed the project through the Build MCP server.

Click :eccenca-application-mapping: in the row of a mapping rule to open the rule in the mapping editor.

## 3 Revert an unwanted change

The column `supplier` holds the company that delivers a part, not its brand or its manufacturer, so the mapping rule for `supplier` is not wanted.

1. Click :eccenca-item-moremenu: in the row of the change that adds this rule, here **Added value mapping 'brand'**.
2. Select **Revert this change**.
3. Click **Revert**.

The mapping rule is removed from **Transform products**.
The revert is recorded as a new change with a tag such as **Reverts #7**, and the reverted change carries a tag such as **Reverted by #9**.
**Unreviewed changes** drops to `2`.

## 4 Mark the remaining changes as reviewed

1. Click **Mark all as reviewed**.
    The dialog lists the changes to mark, here the proposed run and the mapping rule `price`.
2. Click **Confirm**.

Marking the proposed run as reviewed approves it.
To reject a proposed run instead, revert it before marking the remaining changes as reviewed.

## 5 Let the agent run the workflow

Tell the agent that the review is done and ask it to run the workflow again.
In the Companion, click **Confirm** in the confirmation dialog of the run.

The agent requests the run again, and this time the Build MCP server runs **Load products**.
The change journal records the run as **Executed workflow 'Load products'** with a link to its execution report.
The proposed run carries a tag such as **Run as #10**.

![The Changes view after the review with the executed workflow, the revert and the reviewed changes of the agent](review-agent-changes-after-run.png){ class="bordered" }

The Knowledge Graph now contains the name and the price of each product, and no supplier.

## Related

- [Change Journal](../change-journal/index.md) describes the journal, the revert and the review in detail.
- [Companion AI chat](../../explore-and-author/companion/chat/index.md) describes the modes and the confirmation of changes in the Companion.
- [Agent Integration](../../automate/agent-integration/index.md) describes how to connect an external agent and how to limit its permissions.
