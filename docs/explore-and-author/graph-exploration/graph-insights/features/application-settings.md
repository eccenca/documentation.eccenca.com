

# Application and Dataset Settings

## Application Settings {#settings}

Access global configuration via the top-left dropdown menu.

### General Configuration

- **Technical details:** Toggles visibility of low-level metadata, including **IRIs** and **SPARQL queries**.
- **Tree visibility:** Hides empty or deactivated classes in the class tree.

![Settings Window](../assets/settings.png){ class="bordered" width="60%" }

### Troubleshoot and Reset

1. **Reset local data:** Clears browser-side preferences (e.g., columns visibility, width, and position).
2. **Reset graph data:** Performs a "Factory Reset" of the analysis for the current dataset.

!!! danger "Destructive Action"

    **Reset graph data** permanently deletes all [user-defined classes](persistence.md#custom-categories) and [saved explorations](persistence.md#saved-explorations) associated with the current database. This cannot be undone.




---

## Database Settings



### Database Summary

When no group or connection is selected, the right pane displays the **database summary**.

- **Action:** Click the empty canvas background to deselect items.
- **Outcome:** The database summary is shown in the right `Details` pane.
    - **Classes:** Lists all available classes and their cardinality.
    - **Object Properties:** Lists all object properties with their object property assertions count.

![Database Summary Panel](../assets/database-summary.png){ class="bordered" width="35%" }

#### Search and View Controls

Use the controls at the top of the pane to navigate the summary:

- **Search:** Enter text to filter the summary lists. Use the scope dropdown to restrict the search to `Captions`, `IRIs`, or `All`.
- **View Settings (cogwheel):**
    - **Views:** Switch between `Tree view` and `List view`.
    - **Sorting:** Order lists using `Sort by name` (alphabetical) or `Sort by count` (cardinality) to identify the largest entities.
    - **Hide IRIs:** Toggles the display of the underlying identifiers.
