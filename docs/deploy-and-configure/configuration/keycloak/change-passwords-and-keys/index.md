---
tags:
    - Configuration
    - Security
    - Keycloak
---
# Changing Passwords and Keys

This page describes how to change passwords and keys for a new deployment (esp. in the context of a [Single Node Cloud Installation](./../../../installation/scenario-single-node-cloud-installation/index.md)).

Assuming your instance runs at `https://cmem.example.com/` in a default installation Keycloak is deployed at `https://cmem.example.com/auth` (this may vary depending on your setup).

This is your starting page:

![starting-page](22-1-starting-page.png)

## Change credentials of Keycloak admin account

To change the admin user's password go to "Administration Console" and login with username/password admin/admin

In the upper right corner go to "Manage account"

![managing-account](22-1-managing-account.png)

In the "Account Security" field go to "Signing In"

![signing-account](22-1-signing-account.png)

Click on update in "Basic Authentication" to set a new admin password for :

![basic-auth](22-1-basic-auth.png)

Set a new password.

## Change credentials of cmem-service-account

Make sure the realm Cmem is selected, go to Clients in left sidebar and edit cmem-service-account:

![cmem-selection](22-1-cmem-selection.png)

Switch to "Credentials" tab and press "Regenerate Secret" Button.

![credentials-tab](22-1-credentials-tab.png)

## Change credentials of user accounts

In default configuration, there are two users: user and admin. Both are configured with different groups to have different permissions inside Corporate Memory.

To change the default passwords, select the Cmem Realm and open Users in the left sidebar:

![users-lookup](22-1-users-lookup.png)

![user-details](22-1-user-details.png)

Then, select "View all users" and choose an account you want to change the password for (we start with admin)

![view-all-users](22-1-view-all-users.png)

Here you can change the password and unselect Temporary. Then press "Reset Password"

![reset-password](22-1-reset-password.png)

Now proceed with the other account(s).

## Persisting

!!! warning

    This step is applicable only in case your deployment is based on the [Single Node Cloud Installation](./../../../installation/scenario-single-node-cloud-installation/index.md).

In order to persist this setup go back to your terminal inside the installation directory.

The following make targets will create a database dump, store it in `data/backups/keycloak/latest.sql` and replace the initial database dump `conf/postgres/docker-entrypoint-initdb.d/keycloak_db.sql`.

```shell-session
make keycloak-backup keycloak-restore
```

