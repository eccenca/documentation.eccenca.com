# App presentation

*Configuration property: `appPresentation` | Scope: app-wide and per workspace*

DataManager provides the option to customize the visual presentation.

-   js.config.appPresentation
    -   [faviconUrl](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/app-presentation#id-.Apppresentationv20.10-js.config.appPresentation.faviconUrl)
    -   [windowTitle](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/app-presentation#id-.Apppresentationv20.10-js.config.appPresentation.windowTitle)
    -   [logoUrl](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/app-presentation#id-.Apppresentationv20.10-js.config.appPresentation.logoUrl)
    -   [headerName](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/app-presentation#id-.Apppresentationv20.10-js.config.appPresentation.headerName)

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

Configuration example[![Link to Configuration example](https://documentation.eccenca.com/_/0A0A79030170B1271BEB591423192709/1599644127360/images/common/link-solid.svg)](https://documentation.eccenca.com/latest/deploy-and-configure/configuration/datamanager/app-presentation#id-.Apppresentationv20.10-Configurationexample)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

``` yaml
js.config.appPresentation:
  faviconUrl: https://example.com/example/favicon.png
  windowTitle: Datamanager
  logoUrl: https://example.com/example/logo.png
  headerName: Datamanager
```