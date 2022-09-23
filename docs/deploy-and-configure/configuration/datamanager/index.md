# DataManager

This page describes how to configure eccenca DataManager.

It is intended for system administrators, who are responsible for installing, configuring, maintaining and supporting the deployment of DataManager.

eccenca DataManager is a single-page JavaScript application, which means the application consists of a single HTML page which loads all needed web resources in the browser after loading the page itself.

In the context of DataManager, these web resources are:

-   The application including its configuration (app*.js, config.js)
-   Styles (*.css)
-   Web fonts for typography as well as for icons (*.woff, *.ttf, *.eot)
-   Images (e.g. logos) (*.png, *.svg)

DataManager communicates with different API endpoints in order to retrieve and manipulate data.

The features of DataManager include:

-   Dataset Manager to create and update datasets and its meta data
-   Vocabulary Manager to install and remove Vocabulary descriptions
-   Data browser to explore and manage graph-based data
-   Taxonomy Editor to manage and create SKOS based taxonomies
-   Query editor to query graph-based data via SPARQL queries
-   Access control
-   Compliance of W3C standards such as [RDF](https://www.w3.org/standards/techs/rdf#w3c_all), [Linked Data](https://www.w3.org/standards/techs/linkeddata#w3c_all) and [SPARQL](https://www.w3.org/standards/techs/sparql#w3c_all)