# App presentation

*Configuration property: `appPresentation` | Scope: app-wide and per workspace*

DataManager provides the option to customize the visual presentation.

-   js.config.appPresentation
    -   [faviconUrl](../app-presentation)
    -   [windowTitle](../app-presentation)
    -   [logoUrl](../app-presentation)
    -   [headerName](../app-presentation)

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.appPresentation.faviconUrl | none | no | none | string (URL) |

Use this property to define a custom favicon that is displayed in browser tab. Pictures can be an URL or a [Data URL](https://dopiaza.org/tools/datauri/index.php).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.appPresentation.windowTitle | 'eccenca DataManager' | no | none | string |

Use this property to define a custom browser tab name.

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.appPresentation.logoUrl | none | no | none | string (URL) |

Use this property to define a custom logo that is shown in the Module bar. Pictures can be a an URL or a [Data URL](https://dopiaza.org/tools/datauri/index.php).

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.appPresentation.headerName |  |  |  |  |

Use this property to define a custom name that is shown in the Module bar.

# Configuration example

``` yaml
js.config.appPresentation:
  faviconUrl: https://example.com/example/favicon.png
  windowTitle: Datamanager
  logoUrl: https://example.com/example/logo.png
  headerName: Datamanager
```