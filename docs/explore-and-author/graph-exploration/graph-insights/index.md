---
status: new
icon: eccenca/graph-insights
tags:
    - KnowledgeGraph
---
# Graph Insights

![Explore - Graph Insights](explore-graph-insights.png "Explore - Graph Insights"){ class="bordered" }

## Introduction

Graph Insights allows you to explore your knowledge graph through grouped nodes and aggregated relations to keep the view readable.
Expansions are data-guided to avoid dead ends, while on-demand details give you context without clutter.
Interactive filters help you shape the exploration, building query paths with class, attribute, and relation filters along the way.
Each exploration can be converted to SPARQL, effectively serving as a no-code query builder. This also provides table-like views for users less familiar with graphs.

## Configuration Info

A specific configuration is required to activate this feature.

!!! info "Configuration"

    See [Graph Insights Configuration](../../../deploy-and-configure/configuration/graphinsights/index.md) to learn how to enable and configure this feature.

<!--
## Usage

...
-->

## Management

In order to manage Graph Insights snapshots, you can use the
[`graph insights`](../../../automate/cmemc-command-line-interface/command-reference/graph/insights/index.md)
command group of cmemc.
With this command group, you can list, create, delete, and inspect graph insight snapshots.

## Automation

To automate re-creation of Graph Insights snapshots, you can use the
[Update Snapshots](../../../build/reference/customtask/cmem_plugin_graph_insights-Update.md)
task in your workflows.
This task allows for updating snapshots based on the specification of an affected graph.
