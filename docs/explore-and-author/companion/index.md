---
title: "Companion: Foundations"
icon: eccenca/application-ai-suggestion
status: new
tags:
    - Reference
    - Configuration
---
# Companion

!!! info "AI Disclaimer"

    Companion is an AI-based feature.
    AI-generated content may be inaccurate or incomplete.
    Verify important information.

The Companion is the AI assistant of eccenca Corporate Memory.
It answers questions about the data in Corporate Memory and, on request, changes it.
Users talk to it in a chat panel in Explore.
Administrators configure its agents, skills and models in the **Companion Management** module.

<div class="grid cards" markdown>

- :eccenca-application-ai-suggestion: [Companion AI chat](chat/index.md)

    ---

    Ask questions, refer to resources and skills, select a mode and confirm the changes that the Companion proposes.

- :eccenca-application-ai-suggestion: [Companion Management](management/index.md)

    ---

    Inspect the agent network, edit agents, skills and named models, check the available tools and manage the conversations of all users.

- :eccenca-application-ai-suggestion: [Build a Companion catalog](build-a-companion-catalog/index.md)

    ---

    Tutorial: add a catalog with a task agent, an interactive agent and a skill, and ask the Companion about suppliers and prices.

</div>

## How the Companion works

A message travels through several agents before an answer reaches the user.
Each agent has its own instructions, its own tools and a named model that runs it.
All agents, skills and named models are stored in a catalog.

### Agents

Agents answer, route and work.
The kind of an agent decides what it may do, and it cannot be changed after the agent is created:

Routing agents
:   Read the first message of a conversation and hand it to the interactive agent that fits it best.
    Routing agents connect the application views to the Companion and run on a fast model.

Interactive agents
:   Fulfill a role, such as `domain_expert` or `knowledge_graph_expert`, and answer the user.
    An interactive agent may hand the conversation over to another interactive agent and may start task agents.
    Each answer in the chat names the agent that wrote it.

Task agents
:   Do a self-contained piece of work for an interactive agent and return the result.
    Task agents cannot start further agents.

Auxiliary agents
:   Run jobs for the system itself, such as naming a conversation or assessing a change.
    Auxiliary agents take no part in the handovers of a conversation.

### Named models

Agents do not reference a model of a provider directly.
They reference a named model, such as `fast`, `default` or `expert`.
A named model points at a model of a provider and sets the parameters it runs with, for example the reasoning effort.
An installation can therefore exchange a model without changing the agents.

### Skills

A skill is a prompt that a user calls by entering a slash and the name of the skill in the chat, for example `/summarize_graph`.
The text after the name of the skill is passed to the prompt.

### Catalog

A catalog is a graph that holds the agents, skills, named models and catalog properties of the Companion.
The main catalog graph is `https://ns.eccenca.com/data/companion/`.
It can import further catalog graphs with `owl:imports`.
The Companion runs on the effective catalog, which merges the main catalog and its imports.
When an identifier exists in more than one catalog, the entry of the main catalog applies.

Until the catalog is saved for the first time, the Companion uses the catalog shipped with Corporate Memory.

### Application views

The context of a message includes the application view in which the chat is open.
Agents and skills can be restricted to specific application views.
An agent or skill without such a restriction is available in every application view.

### Tools

The Companion uses tools to read and change data in Corporate Memory.
The tools are provided by the Model Context Protocol (MCP) servers of the Corporate Memory components and are named after them:

| Prefix | Tools for |
| --- | --- |
| `cmem_explore-` | Graphs, vocabularies, resources, SHACL shapes and validation, queries and the query catalog |
| `cmem_build-` | Build projects, datasets, transformations, workflows and project resources |
| `cmem_marketplace-` | Marketplace packages and package manifests |

Each tool declares whether it reads or changes data.
A tool that declares nothing counts as changing data.
Each agent uses only the tools that match the tool patterns configured for it.
External MCP servers can be added through the [MCP client configuration](../../deploy-and-configure/configuration/explore/dataplatform/application-full.md#configuration-of-mcp-server).

### Modes

The mode of a chat decides which tool calls run on their own, which need a confirmation and which are declined.
A new chat starts in **Read only**.
See [Modes](chat/index.md#modes) for the available modes.

## Configuration

A specific configuration is required to activate the Companion.
The deployment templates (helm charts and docker-compose configurations) provide tested configuration profiles for different LLM providers.

!!! info "Configuration"

    See [`spring.ai.*` configuration properties in _Configuration of Servlet Container_](../../deploy-and-configure/configuration/explore/dataplatform/application-full.md#configuration-of-servlet-container) to learn how to enable and configure this feature.
    Explore uses _Spring AI_ to connect and configure LLM provider, as such the [Spring AI Chat Model API Configuration Reference](https://docs.spring.io/spring-ai/reference/api/chatmodel.html) applies.

For optimal results, use Anthropic or OpenAI frontier-level models configured through the native Spring AI provider setup.

## Access

Two actions grant access to the Companion:

- `https://vocab.eccenca.com/auth/Action/Explore-Companion-Use` grants access to the chat.
- `https://vocab.eccenca.com/auth/Action/Explore-Companion-Manage` grants access to **Companion Management**.

Assign the actions to a user group in an [access condition](../../deploy-and-configure/configuration/access-conditions/index.md).
