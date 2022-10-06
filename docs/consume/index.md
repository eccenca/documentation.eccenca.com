---
icon: material/star
hide:
  - toc
---

# Consume

This section outlines how to consume data from the Knowledge Graph. While there are several options to retrieve information from the Knowledge Graph, the most direct way is to issue SPARQL queries. SPARQL queries can be managed and executed in the [Query Module UI](../deploy-and-configure/configuration/datamanager/query-module/index.md). External applications may access the query catalog and execute queries through the REST API directly or more conveniently by using the [cmemc - Command Line Interface](../automate/cmemc-command-line-interface/index.md). Since not all applications allow the direct use of SPARQL, this section includes tutorials to access the Knowledge Graph using BI tools (such as Power BI) as well as relational databases.

![The CONSUME functional block in Corporate Memory](22-1-Consume.png){ width="50%" }

- :material-file-document: [Accessing Graphs with Java Applications](../develop/accessing-graphs-with-java-applications/index.md) — This short recipe covers how to connect to Corporate Memory using a Java program.
- :material-file-document: [cmemc - Command Line Interface](../automate/cmemc-command-line-interface/index.md) — cmemc is intended for system administrators and Linked Data Expert, who wants to automate and remote control activities on eccenca Corporate Memory.
- :material-file-document: [Consuming Graphs in Power BI](consuming-graphs-in-power-bi/index.md) — Learn how to consume data from your Corporate Memory Knowledge Graph with our Microsoft Power-BI-Connector.
