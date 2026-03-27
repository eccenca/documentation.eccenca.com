

# Feature Reference

Documentation for the core components of the Graph Insights interface.

## Workspace

- **[Application and dataset settings](application-settings.md):** Application fine-tuning, dataset selection. 
- **[Exploration canvas](canvas-ui.md):** Layout controls, information density management, and exploration tree exports.
- **[Class tree](category-tree.md):** Starting an exploration, class configuration (captions/visibility).

## Exploration Tree Interaction

- **[Groups](groups.md):** class distribution analysis, expansion controls.
- **[Resources table](objects-table.md):** Group content in table form, data properties-based group filtering.
- **[Resources](objects.md):** Structured list of data properties values, highlighting and flagging options, single resource traversals
- **[Connections](connections.md):** Links visualization, backpropagation (inner join), connection table and filtering.

## Analysis Tools

- **[Histograms](groups.md#histograms):** class distribution analysis and facet-like set operations (union, intersection, difference).
- **[Persistence](persistence.md):** Saved explorations, user-defined classes, and JSON sharing.

---

## Global Keyboard Navigation

Graph Insights supports standard keyboard navigation for accessibility and rapid interaction across all views, including the class tree, data tables, and menus.

- `TAB` / `SHIFT` + `TAB`: Moves focus to the next or previous interactive element.
- Arrow Keys (`UP`, `DOWN`, `LEFT`, `RIGHT`): Navigates within lists, trees, menus, and subpanels.
- `ENTER`: Triggers the focused element (e.g., a button or menu item) or executes the default action.
- `SPACE`: Toggles a checkbox state or triggers the focused element.
- `ESC`: Closes the currently active temporary element (e.g., popup windows, context menus, or dropdowns).
- `SHIFT` + `ENTER`: Inserts a line break within text input fields (e.g., group notes).

### Context Menus

To open a context menu using the keyboard:

- **Windows:** Press `SHIFT` + `F10`.
- **macOS:** Press `CTRL` + `ENTER` *(Note: Supported in Firefox; Chrome behavior may vary)*.