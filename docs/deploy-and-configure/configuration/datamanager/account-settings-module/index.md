# Account Settings module

*Configuration property: `modules.accountSettings` | Scope: app-wide and per workspace*

DataManager provides a menu point to edit the account settings. It also need to be enabled in keycloak.

-   js.config.modules.accountSettings
    -   url
    -   enable

| Property | Default | Required | Conflicts with | Valid values |
| -------- | ------- | -------- | -------------- | ------------ |
| js.config.modules.accountSettings.enable | true | no | none | boolean |
| js.config.modules.accountSettings.url | `http://docker.local/auth/realms/cmem/account/?referer={{REFERRER}}&referrer_uri={{REFERRER_URI}}` | yes if enable is true | none | url string with placeholders: {{REFERRER}}, {{`REFERRER_URI}}`  |