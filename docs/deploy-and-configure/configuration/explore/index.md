---
hide:
    - toc
tags:
    - Configuration
---
# Explore (DataManager/DataPlatform)

This page describes how to configure the eccenca Explore component which is done in two parts:

1.  The Explore frontend (DataManager) is configured visually through the :eccenca-module-workspace-configuration: _Workspace configuration_ module.
2.  [The Explore backend (DataPlatform)](dataplatform), all details are described on the respective sub-page

eccenca Explore frontend (DataManager) is a single-page JavaScript application, which means the application consists of a single HTML page which loads all needed web resources in the browser after loading the page itself.

In the context of Explore frontend (DataManager), these web resources are:

-   The application including its configuration (`app*.js`, `config.js`)
-   Styles (`*.css`)
-   Web fonts for typography as well as for icons (`*.woff`, `*.ttf`, `*.eot`)
-   Images (e.g. logos) (`*.png`, `*.svg`)

Explore frontend (DataManager) communicates with different API endpoints in order to retrieve and manipulate data.

The features of Explore frontend (DataManager) include:

-   Dataset Manager to create and update datasets and its meta data
-   Vocabulary Manager to install and remove Vocabulary descriptions
-   Data browser to explore and manage graph-based data
-   Taxonomy Editor to manage and create SKOS based taxonomies
-   Query editor to query graph-based data via SPARQL queries
-   Access control
-   Compliance of W3C standards such as [RDF](https://www.w3.org/standards/techs/rdf#w3c_all), [Linked Data](https://www.w3.org/standards/techs/linkeddata#w3c_all) and [SPARQL](https://www.w3.org/standards/techs/sparql#w3c_all)

