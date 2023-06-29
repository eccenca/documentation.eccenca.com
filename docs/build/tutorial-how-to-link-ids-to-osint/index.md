---
icon: material/table
subtitle: such as STIX
tags:
  - BeginnersTutorial
  - KnowledgeGraph
  - Security
---

# Tutorial: how to link Intrusion Detection Systems (IDS) to Open-Source INTelligence (OSINT)

## Plan of tutorial

1. Introduction, level, material
2. [Define the need, the expected result and the use case](define-the-need/index.md)
3. [Specify the dashboards before the RDF models](define-the-interfaces/index.md)
4. Build Knowledge Graphs from:
	1. [STIX 2.1 data such as the MITRE ATT&CK® datasets](lift-data-from-STIX-2.1-data-of-mitre-attack/index.md)
	2. [Indicators of compromise rules, like Hayabusa and Sigma rules](lift-data-from-YAML-data-of-hayabusa-sigma/index.md)
5. Link IDS event to a knowledge graph in dashboards via:
	1. [Queries](link-IDS-event-to-KG/index.md)
	2. [Inferences](link-IDS-event-to-KG-via-cmem/index.md) (for the advanced users of Corporate Memory)

## Introduction
“Everything as code” has become the status quo among leading organizations adopting DevSecOps and SRE practices, and yet, monitoring and observability have lagged behind the advancements made in application and infrastructure delivery for the Cyber Investigation Analysts.
“Investigating as code” is not just automated installation and configuration of agents, plugins, and exporters to collect the alerts of Indicator of Compromise (IoC) — it encompasses the conception of a custom dashboard to navigate in gigabytes of event data linked to open data of Open-Source INTelligence (OSINT). 
However, traces and knowledge about attacks are heterogeneous due to fragmented cyber communities. 
This fact prevents rapid development and makes the “investigating as code” a difficult and tedious task, including cybersecurity event browsing.

This tutorial is going to demonstrate solutions that exist to browse the knowledge of an attack like on the Web with Linked Data technology.
It also includes the development of new custom links between events and knowledge, ie. inferences.

This self-service monitoring/alerting and now inferencing allows analysts breaking data silos which enables by continuous improvement the linking of Intrusion Detection Systems (IDS) to Open-Source INTelligence (OSINT).

## Level
This tutorial is also suitable for beginners. 
Simple examples will allow you to discover Linked Data technologies.

## Material
eccenca will offer an online sandbox running an instance of Corporate Memory. You can also install Corporate Memory Console (CMEMC) on your computer to test the example of bash scripts in this tutorial. For the part "Link IDS event to a knowledge graph in dashboards", you need to have a Splunk instance where you can install the Splunk apps of this tutorial.