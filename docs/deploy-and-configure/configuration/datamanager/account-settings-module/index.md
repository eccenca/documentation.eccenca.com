# Account Settings module

*Configuration property: `modules.accountSettings` | Scope: app-wide and per workspace*

DataManager provides a menu item for editing the account settings, which needs to be enabled in keycloak.

-   js.config.modules.accountSettings
    -   url
    -   enable

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.accountSettings.enable | true | no | none | boolean |
| js.config.modules.accountSettings.url | `http://docker.local/auth/realms/cmem/account/?referer={{REFERRER}}&referrer_uri={{REFERRER_URI}}` | yes if enable is true | none | url string with placeholders: {{REFERRER}}, {{`REFERRER_URI}}`  |
