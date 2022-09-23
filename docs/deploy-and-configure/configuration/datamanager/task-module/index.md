# Task module

*Configuration property: `modules.task` | Scope: app-wide and per workspace*

The Task module of DataManager is used to offer direct user action interfaces to view or manipulate specific data.

-   js.config.modules.task
    -   [enable](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/task-module#id-.Taskmodulev20.06-js.config.modules.task.enable)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.task.enable | true | no | none | boolean |

Set this property to `true` to enable the Task module of DataManager.

Note: If this property is set to `false`, all other settings of `modules.task` are skipped.

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/task-module#id-.Taskmodulev20.06-Configurationexample)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
js.config.modules:
  task:
    enable: true
```