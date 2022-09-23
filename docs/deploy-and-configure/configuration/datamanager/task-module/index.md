# Task module

*Configuration property: `modules.task` | Scope: app-wide and per workspace*

The Task module of DataManager is used to offer direct user action interfaces to view or manipulate specific data.

-   js.config.modules.task
    -   [enable](#task-module)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.task.enable | true | no | none | boolean |

Set this property to `true` to enable the Task module of DataManager.

Note: If this property is set to `false`, all other settings of `modules.task` are skipped.

## Configuration example

```
js.config.modules:
  task:
    enable: true
```