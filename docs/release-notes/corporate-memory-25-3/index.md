---
status: new
tags:
    - ReleaseNote
---
# Corporate Memory 25.3.0

Corporate Memory 25.3 is the third major release in 2025.

<!-- todo:
![25.2: Build - Binary Files and Dataset Workflow Operators](25-2-build-binary-files-dataset.png "25.2: Build - Binary Files and Dataset Workflow Operators"){ class="bordered" }
![25.2: Explore - Dynamic Class and Property Creation](25-2-explore-dynamic-concept-creation.png "25.2: Explore - Dynamic Class and Property Creation"){ class="bordered" }
![25.2: Explore - Multi-Graph Query Management](25-2-explore-multiple-query-catalogs.png "25.2: Explore - Multi-Graph Query Management"){ class="bordered" }
-->

The highlights of this release are:

-   Build: **Enhanced File Management in Workflows**
    -   New binary file dataset and project file operators enable seamless integration of PDFs, images, and other binary files directly into workflows, streamlining document processing pipelines.

-   Explore: **Dynamic Class and Property Creation**
    -   Create classes and properties on-the-fly while defining SHACL shapes, dramatically accelerating ontology development and data modeling workflows without context switching.

-   Explore and Automate: **Multi-Graph Query Management**
    -   The enhanced query catalog now supports multiple query graphs and arbitrary graph selection, enabling better organization and management of SPARQL queries across different knowledge domains.

-   Build: **Mapping Creator** (BETA)
    -   New visual mapping management and GenAI based mapping environment, allowing unparalleled clarity, speed and ease in building and maintaining your mapping rules.

This release delivers the following component versions:

-   eccenca DataIntegration v25.3.0
-   eccenca Explore v25.3.0
-   eccenca Corporate Memory Control (cmemc) v25.5.0

We tested this release with the following dependency components:

-   Ontotext GraphDB v11.1.2
-   Keycloak v26.4.1

More detailed information for this release is provided in the next sections.

## eccenca DataIntegration v25.3.0

We are excited to announce the release of DataIntegration v25.3.0, which introduces …

**v25.3.0 of DataIntegration adds the following new features:**

-   …

**v25.3.0 of DataIntegration introduces the following changes:**

-   …

**v25.3.0 of DataIntegration ships the following fixes:**

-   …

## eccenca Explore v25.3.0

We are pleased to announce Explore v25.3.0, which delivers the new **Companion** LLM data interaction, a whole new way to explore your data relationships in **Graph Insights**, experimental Tentris support, major BKE authoring enhancements and a wide range of usability and stability fixes.

**v25.3.0 of Explore adds the following new features:**

-   **Graph Insights**
    -   New visual graph exploration and visual query UI for easy relation analysis.
-   **Companion:**
    -   LLM based integrated chat to interact with your data, generate or user SPARQL queries, providing a deep integration with Corporate Memory features
    -   MCP Server SSE endpoint to provide the tool powering _Compaion_ to external clients
-   **Backend:**
    -   Added experimental support for the Tentris store backend.
    -   Added support for configuring a fixed authorization bearer token in the HTTP store backend.
-   **BKE authoring enhancements:**
    -   Execute workflows triggered by node shapes directly from BKE.
    -   Simplified connecting nodes from the possible resources menu on the canvas.
    -   Added the missing tooltips for multiple BKE buttons.
-   **SHACL authoring usability:**
    -   Added a tooltip to the LiteralContainer component.

**v25.3.0 of Explore introduces the following changes:**

-   **Thesaurus navigation:**
    -   Navigation tree items are now sorted by their labels for consistent browsing.

**v25.3.0 of Explore ships the following fixes:**

-   **General platform fixes:**
    -   Handle external and internal redirects to preserve unsaved work.
    -   Restored the LinkRules download button.
    -   The SPARQL GSP DELETE request now returns 404 for non-existing graphs consistently across backends.
    -   Explore now relies on GraphDB to manage stopwords, ensuring correct filtering.
    -   Fixed an empty state regression when the graph list query returns no results.
    -   Failures in the shape catalog no longer block other tabs.
    -   Prevented blank pages in the query editor when previous queries were not saved.
    -   SHACL now handles custom value queries without bindings more gracefully.
-   **BKE stability improvements:**
    -   Improved error handling for validation requests in the BKE module.
    -   Fixed the BKE visualization saving issue.
    -   UI query requests for connectable candidates now only run for resources.
    -   The "Open resource details" link can again be opened in a new browser tab.
-   **SHACL editing reliability:**
    -   Added a loading state for SHACL edit controls to provide clearer feedback.

**v25.3.0 of Explore removes the following functionality:**

-   Removed the deprecated LLM assistance feature.

## eccenca Corporate Memory Control (cmemc) v25.5.0

!!! info inline end "Important info"

    This eccenca Corporate Memory release is the first release where we introduced Semantic Versioning for our components.
    This cmemc release notes section reflects this by reporting multiple minor versions in one section.

We are excited to announce cmemc v25.5.0, which introduces new features, improvements and bug fixes.

**v25.5.0 of cmemc adds the following new features:**

-   …

## Migration Notes

!!! info "Backward and Forward Compatibility"

    We do not guarantee forward compatibility for configuration, data or projects.
    I.e. importing a project created with DataIntegration v25.2.0 into DataIntegration v25.1.0 (or older) might not work.

    Backward compatibility will be ensured or migration paths explained.
    I.e. projects created with DataIntegration v24.3.0 can be imported into DataIntegration v25.1.0.

!!! info "Important info"

    Since v24.3.0, the components eccenca DataPlatform and eccenca DataManager are merged
    into a single component eccenca Explore.

### eccenca DataIntegration

-   …

### eccenca Explore

-   With the deprecation of the assistance feature, `assist.*` properties can be removed from your `application.yml`, they are not used any more and have been replaced by `spring.ai` configuration.

### eccenca Corporate Memory Control (cmemc)

-   …
