---
title: "Excel (OneDrive, Office365)"
description: "Read data from a remote onedrive or Office365 Spreadsheet."
icon: octicons/cross-reference-24
tags: 
    - Dataset
---
# Excel (OneDrive, Office365)
<!-- This file was generated - DO NOT CHANGE IT MANUALLY -->



The dataset needs the URL of a "share via link" sheet on Office 365/OneDrive as input.
It will automatically construct a direct download URL, cache the download file handle it like
an XLSX file in the Excel Dataset.

### Notes

There are 2 types of URLs that can be shared:
Onedrive links look like `https://1drv.ms/x/s!AucULvzmJ-dsdfsfgaIcyWP_XY_G4w?e=yx65uu`

Onedrive (based one sharepoint, for businesses) links look like `https://eccencagmbh-my.sharepoint.com/:x:/g/personal/person_eccenca_com/EdEMTEw1dclHiEZXyvy8P4YBit8wSyGsiwU5Kt__sQOZzw`

The first type should always work is not recommended for this dataset. The second type requires to set up an application in Microsoft EntraID (formerly Azure Active Directory).
EntraID: https://docs.microsoft.com/azure/active-directory/develop/v2-overview
Instructions and examples can be found here:
https://github.com/Azure-Samples/ms-identity-msal-java-samples/tree/main/3-java-servlet-web-app/1-Authentication/sign-in

After following the steps access to sharepoint/onedrive for business can be setup in the application.conf file for eccenca DataIntegration.

Example:

```conf
com.eccenca.di.office365 = {
    authority = "https://login.microsoftonline.com/a0907dd1-f981-4c98-a8b9-1deb27bcf2cc/"
    clientId = "4d14959d-3c62-4f90-a072-a96ca4b3fa9f"
    secret = "Ceb8Q~QkMMV7TBK-ggB3nh22nUnqoDB1KTmkjj"
    scope = "https://graph.microsoft.com/.default"
    tenantId = "a0907dd1-f981-4c98-a8b9-1deb27bcf2cc"
}
```

### Caching

The advanced parameter `invalidateCacheAfter` allows the user to specify a duration of the file cache
after which it is refreshed.
A file based cache is created to avoid CAPTCHAs. During the caching and validation of the URL
access occurs with random wait times between 1 and 5 seconds.
The cache is invalidated after 5 minutes by default.


## Parameter

### URL

Link to the document ('share with anyone having a link' must be enabled).

- Datatype: `string`
- Default Value: `None`



### Streaming

Streaming enables reading and writing large Excels files. Warning: Be careful to disable streaming for large datasets (> 10MB), because of high memory consumption.

- Datatype: `boolean`
- Default Value: `true`



### Invalidate cache after

Duration until file based cache is invalidated.

- Datatype: `duration`
- Default Value: `PT5M`



### Lines to skip

The number of lines to skip in the beginning when reading files.

- Datatype: `int`
- Default Value: `0`



