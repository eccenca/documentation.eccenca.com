---
icon: octicons/cross-reference-24
tags:
    - Reference
---
# Mapping Creator

Use the Mapping Creator to connect your data to semantic models. Using visual tools, drag-and-drop, and suggestions, you’ll create mappings between your source data and knowledge graph classes.

![Mapping Creator](mapping-creator.png)

The Mapping Creator is split into three parts:

- The left sidebar shows the source schema
- The right sidebar shows the target schema
- Mappings between elements in the source schema and elements in the target schema.

You can move, connect or disconnect, and inspect each element visually.

## Manual creation

Every mapping begins by selecting or creating a target class. This defines where your data will be be mapped in the knowledge graph.

### Edit saved mapping rule

Click on an already saved target element to show more details. With the Pencil icon you can edit the mapping rule and rename elements, or adjust configurations. Advanced users can refine transformation logic here.

### Create direct mappings

Drag from a property in your source data to a class or property in the canvas to create your mapping. This is helpful when suggestions are not sufficient.

## Smart suggestions

Click the Magic Wand to automatically generate mapping suggestions based on your data and the selected class. Accept or reject each suggestion as needed.

*   **Class Suggestions:** If you haven't selected a target class yet, the AI tries to suggest classes from the selected vocabularies that fits your source data the most. You can also search manually for classes by typing text into the search field.
*   **Property Suggestions:** Property suggestions are generated that map your source data to elements of the selected target vocabularies. You can accept or reject each suggestion.
  
Note that this feature is only available if a Large Language Model is configured.  

![Smart suggestions](smart-suggestions.png)

Once the smart suggestions have been generated, you need do two steps:

1. For each property, decide whether to accept or reject the AI-generated mapping. Use the checkmark to accept or the cross to reject.
2. Once you have completed your mapping, click ‘Update Mapping’ to apply and save your changes to the knowledge graph.