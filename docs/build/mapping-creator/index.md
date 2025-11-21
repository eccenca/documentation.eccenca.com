---
icon: fontawesome/solid/wand-magic-sparkles
subtitle: build mappings visually and AI supported
status: new
tags:
    - Reference
---
# Mapping Creator

??? info "Configuration"

    See [Mapping Creator and LLM Configuration](../../deploy-and-configure/configuration/dataintegration/index.md#mapping-creator-and-llm-configuration) to learn how to enable and configure this feature.

!!! question "Inline help"

    Access inline help and a feature tour via the help menu :eccenca-item-question:.

    ![Inline Help](mapping-creator-help.png){ class="bordered" width="20%" }

Use the Mapping Creator to connect your data to semantic models.
Using visual tools, drag-and-drop, and suggestions, you’ll create mappings between your source data and knowledge graph classes as well as their properties.

![Mapping Creator](mapping-creator.png){ class="bordered" }

The Mapping Creator is split into three parts:

-   The left sidebar shows the source schema
-   The right sidebar shows the target schema
-   Mappings between elements in the source schema and elements in the target schema.

You can move, connect or disconnect, and inspect each element visually.

## Manual creation

Every mapping begins by selecting or creating a target class.
This defines where your data will be be mapped in the knowledge graph.

### Add properties

![Resource edit actions](mapping-creator-edit-actions.png){ class="bordered" width="40%" }

To complete a mapping properties need to be added to complete your desired target schema (i.e. the graph fragment that your transformation shall yield).
The following two options exist to add properties.

#### During class selection

![Properties option in the class selection dialog](mapping-creator-class-selection.png){ class="bordered" width="80%" }

In the _add target class_ dialog you may select different kind of properties:

-   class properties - properties defined in the domain of the selected class or its super-classes
-   default properties - typical well knows like `rdfs:label` or `rdfs:comment`
-   generic properties - properties defined with no explicit domain (or in domain of `owl:Thing`)

The property preview helps to confirm your choice.

#### By adding a property from your vocabularies

![Adding a property from your vocabulary](mapping-creator-property-selection.png){ class="bordered" width="80%" }

The _add property from vocabularies_ dialog allows to search and select a property and to configure it in the desired way:

-   redefine the role of a property, to use a DatatypeProperty in the role of an ObjectProperty, or vice versa
-   define the _direction_ an ObjectProperty should be used in

### Create direct mappings

Drag from a property in your source data to a class or property in the canvas to create your mapping.
This is helpful when smart suggestions are not sufficient.

### Edit saved mapping rule

![Editing a saved rule](mapping-creator-edit-rule.png){ class="bordered" width="60%" }

Click on an already saved target element to show more details.
With the :eccenca-item-edit: Pencil icon you can edit the mapping rule and rename elements, or adjust configurations.
Advanced users can refine transformation logic here.

## Smart suggestions

!!! info
    Note that this feature is only available if a Large Language Model is configured.

Click the :eccenca-application-ai-suggestion: Magic Wand to automatically generate mapping suggestions based on your data and the selected class.
Accept (:octicons-thumbsup-16:) or reject (:octicons-thumbsdown-16:) each suggestion as needed.

### Class Suggestions

![Smart Class Suggestions](mapping-creator-class-suggestion.png){ class="bordered" }

If you haven't selected a target class yet, the AI will suggest classes from the selected vocabularies that best fit your source data.
Alternatively, you can search for classes manually by typing text into the search field.

Hover over the wand icon for each suggestion to understand why this class has been recommended.

### Property Suggestions

Property suggestions are generated that map your source data to elements of the selected target vocabularies.
You can accept (:octicons-thumbsup-16:) or reject (:octicons-thumbsdown-16:) each suggestion.

![Smart Property Suggestions](smart-suggestions.png){ class="bordered" }

Once the smart suggestions have been generated, you need do two steps:

1. For each property, decide whether to accept or reject the AI-generated mapping.
    Click :octicons-thumbsup-16: Confirm to accept or :octicons-thumbsdown-16: Decline to reject.

2. Once you have completed your mapping, click the _Save Mapping_ button to apply and save your changes to the transformation task.
