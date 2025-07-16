---
icon: material/debian
---
# Scenario: Single Node Cloud Installation

## Introduction

This page describes a docker-compose based orchestration running on a server instance accessible publicly via browser (SSL enabled via letsencrypt).

## Requirements

-   ssh access to a server instance (Debian 11) with a public IP address
-   A resolvable domain name to this server
-   Terminal with ssh client installed locally
-   An eccenca partner account for the docker registry as well as the release artifact area

## Server Provisioning

In this step, you install necessary software on the server and execute the following commands as root:

```bash
sudo apt-get update

# install ntp and set timezone
sudo apt-get install -y ntp
sudo timedatectl set-timezone Europe/Berlin

# install needed packages
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 \
    software-properties-common gnupg lsb-release gettext zip unzip git \ 
    make vim jq

# install docker and docker-compose
curl -fsSL https://download.docker.com/linux/debian/gpg \
    | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb \
    [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
    https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io \
    docker-compose-plugin

# (optional) add a user to docker group
# may require logout/login to reload group assignments
# sudo usermod -a -G docker admin
```

## Installation

!!! info

    For username and password in curl command use the credentials to access eccenca Artifactory and docker registry.

Connect to the server and navigate to the directory with the Corporate Memory docker orchestration:

```bash
# login to the eccenca docker registry
docker login docker-registry.eccenca.com

# download the Corporate Memory orchestration distribution
cd /opt
curl https://releases.eccenca.com/docker-orchestration/latest.zip \
    > cmem-orchestration.zip

# unzip the orchestration and move the unzipped directory to
# /opt/cmem-orchestration
unzip cmem-orchestration.zip
rm cmem-orchestration.zip
mv cmem-orchestration-v* /opt/cmem-orchestration

# configure git in order to commit changes to the orchestration
cd /opt/cmem-orchestration
git config --global user.email "you@example.com" && git init && git add . \
    && git commit -m "stub"

```

The Corporate Memory docker orchestration is configured with environment files.

You will need to create an environment file at `/opt/cmem-orchestration/environments/prod.env`.
For now, you can use the provided file `config.ssl-letsencrypt.env` as a template.

!!! Info

    You need to change the lines with DEPLOYHOST and LETSENCRYPT_MAIL to your actual values.

```bash
cd /opt/cmem-orchestration/environments
cp config.ssl-letsencrypt.env prod.env

# change DEPLOYHOST and LETSENCRYPT_MAIL values
vi prod.env
```

In addition that, you need to remove the default config and link it to your prod.env

```bash
cd /opt/cmem-orchestration/environments

rm config.env
ln -s prod.env config.env
```

To see all available configuration options refer to [Docker Orchestration configuration](./../../configuration/docker-orchestration/index.md) page.

Next, request SSL certificates from [letsencrypt](https://letsencrypt.org/) service:

```bash
cd /opt/cmem-orchestration
make letsencrypt-create
```

Change `CMEM_BASE_URI` according to your `DEPLOYHOST`.

```bash
# update cmemc configuration
rm conf/cmemc/cmemc.ini
cat <<EOF > conf/cmemc/cmemc.ini
[cmem]
CMEM_BASE_URI=https://corporate-memory.eccenca.dev/
OAUTH_GRANT_TYPE=client_credentials
OAUTH_CLIENT_ID=cmem-service-account
OAUTH_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a
EOF
```

Finally deploy the Corporate Memory instance:

```bash
make clean-pull-start-bootstrap
make tutorials-import
```

Optional: you can install cmem as a systemd service for this use these commands as root or sudo:

```bash
cp /opt/cmem-orchestration/conf/systemd/cmem-orchestration.service \
    /etc/systemd/system
systemctl enable cmem-orchestration
systemctl start cmem-orchestration
```

## Validation and Finalisation

Open your browser and navigate to the host you have created in DNS server, e.g. `https://corporate-memory.eccenca.dev`

Click **CONTINUE WITH LOGIN** and use one of these default accounts:

| account | password | description                                                                                 |
| ------- | -------- | ------------------------------------------------------------------------------------------- |
| `admin` | `admin`  | Is member of the global admin group (can see and do anything)                               |

After successful login, you will see Corporate Memory interface.
You can now proceed to the :material-arrow-right: [Getting Started](../../../getting-started/index.md) section.

Do not forget to change the passwords of your deployment, especially if it is available from the public internet.
For this, take a look at [Change Passwords and Keys](../../configuration/keycloak/change-passwords-and-keys/index.md).


```bash
cp /opt/cmem-orchestration/conf/systemd/cmem-orchestration.service \
    /etc/systemd/system
systemctl enable cmem-orchestration
systemctl start cmem-orchestration
```

### Backup

To create a backup you have to prepare the backup folders. Make sure these folders exists and have write permissions. Run this:

```bash
# assuming you are currently in the the cmem-orchestration folder
mkdir -p data/backups/graphs data/backups/workspace
chmod 777 data/backups/graphs data/backups/workspace

make backup
mkdir -p data/backups/keycloak
Started Keycloak database backup to data/backups/keycloak/keycloak.sql ...
Finished Keycloak database backup.
mv data/backups/keycloak/keycloak.sql data/backups/keycloak/2024-07-26_14-15.sql
ln -sf 2024-07-26_14-15.sql data/backups/keycloak/latest.sql
mkdir -p data/backups/workspace
docker compose run -i --rm --env "OAUTH_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a" --volume /home/ttelleis/cmem-dist/cmem-orchestration/data:/data --volume /home/ttelleis/cmem-dist/cmem-orchestration/conf/cmemc/cmemc.ini:/config/cmemc.ini cmemc -c cmem admin workspace export /data/backups/workspace/2024-07-26_14-15.zip
Export workspace to /data/backups/workspace/2024-07-26_14-15.zip ... done
ln -sf 2024-07-26_14-15.zip data/backups/workspace/latest.zip
mkdir -p data/backups/python-packages
zip -r data/backups/python-packages/2024-07-26_14-15.zip data/python-packages
  adding: data/python-packages/ (stored 0%)
ln -sf 2024-07-26_14-15.zip data/backups/python-packages/latest.zip
mkdir -p data/backups/graphs
docker compose run -i --rm --env "OAUTH_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a" --volume /home/ttelleis/cmem-dist/cmem-orchestration/data:/data --volume /home/ttelleis/cmem-dist/cmem-orchestration/conf/cmemc/cmemc.ini:/config/cmemc.ini cmemc -c cmem admin store export /data/backups/graphs/2024-07-26_14-15.zip
Exporting graphs backup to /data/backups/graphs/2024-07-26_14-15.zip ... done
ln -sf 2024-07-26_14-15.zip data/backups/graphs/latest.zip
zip -r data/backups/2024-07-26_14-15.zip data/backups/keycloak/2024-07-26_14-15.sql data/backups/workspace/2024-07-26_14-15.zip data/backups/graphs/2024-07-26_14-15.zip data/backups/python-packages/2024-07-26_14-15.zip
  adding: data/backups/keycloak/2024-07-26_14-15.sql (deflated 82%)
  adding: data/backups/workspace/2024-07-26_14-15.zip (stored 0%)
  adding: data/backups/graphs/2024-07-26_14-15.zip (stored 0%)
  adding: data/backups/python-packages/2024-07-26_14-15.zip (stored 0%)
ln -sf 2024-07-26_14-15.zip data/backups/latest.zip

```
The full backup is now at `data/backups/latest.zip`.
