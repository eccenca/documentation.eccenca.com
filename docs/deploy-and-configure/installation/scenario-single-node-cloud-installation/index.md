# Scenario: Single Node Cloud Installation

## Introduction

This page describes a docker-compose based orchestration running on a server instance accessible publicly via browser (SSL enabled via letsencrypt).

## Requirements

- ssh access to a server instance (Debian 10) with a public IP address
- A resolvable domain name to this server
- Terminal with ssh client installed locally
- An eccenca partner account for the docker registry as well as the release artifact area

## Server Provisioning

In this step, you install necessary software on the server and execute the following commands as root:

```bash linenums="1"
apt-get update

# install ntp and set timezone
apt-get install -y ntp
timedatectl set-timezone Europe/Berlin

# install needed packages
apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common gnupg lsb-release gettext zip unzip git make vim

# install docker
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo   "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io

# (optional) add a user to docker group
# usermod -a -G docker admin

# install docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

```

## Installation

!!! info
    For username and password in curl command use the credentials to access eccenca Artifactory and docker registry.

Connect to the server and navigate to the directory with the Corporate Memory docker orchestration:

```bash linenums="1"
# login to the eccenca docker registry
docker login docker-registry.eccenca.com

# download the Corporate Memory orchestration distribution
cd /opt
curl -u username https://releases.eccenca.com/docker-orchestration/latest.zip > cmem-orchestration.zip

# unzip the orchestration and move the unzipped directory to /opt/cmem-orchestration
unzip cmem-orchestration.zip
rm cmem-orchestration.zip
mv cmem-orchestration-v* /opt/cmem-orchestration

# configure git in order to commit changes to the orchestration
cd /opt/cmem-orchestration
git config --global user.email "you@example.com" && git init && git add . && git commit -m "stub"

```

The Corporate Memory docker orchestration is configured with environment files.

You will need to create an environment file at `/opt/cmem-orchestration/environments/prod.env` - for now, you can use the provide file `config.ssl-letsencrypt.env` as a template.

???+ warning
    You need to change the lines with DEPLOYHOST and LETSENCRYPT_MAIL to you actual values.

```bash linenums="1"
cd /opt/cmem-orchestration/environments
cp config.ssl-letsencrypt.env prod.env

# change DEPLOYHOST and LETSENCRYPT_MAIL values
vi prod.env
```

In addition that, you need to remove the default config and link it to your prod.env

```bash linenums="1"
cd /opt/cmem-orchestration/environments

rm config.env
ln -s prod.env config.env

```

To see all available configuration options refer to [Docker Orchestration configuration](./../../configuration/docker-orchestration/index.md) page.

Next, request SSL certificates from [letsencrypt](https://letsencrypt.org/) service:

```bash linenums="1"
cd /opt/cmem-orchestration
make letsencrypt-create
```

Change CMEM_BASE_URI according to your DEPLOYHOST.

```bash linenums="1"
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

```bash linenums="1"
make clean-pull-start-bootstrap
make tutorials-import
```

Optional: you can install cmem as a systemd service for this use these commands as root oder sudo:

```bash linenums="1"
cp /opt/cmem-orchestration/conf/systemd/cmem-orchestration.service /etc/systemd/system
systemctl enable cmem-orchestration
systemctl start cmem-orchestration
```

## Validation and Finalisation

Open your browser and navigate to the host you have created in DNS server, e.g. [https://corporate-memory.eccenca.dev](https://corporate-memory.eccenca.dev/)

Click CONTINUE WITH LOGIN and use one of these default accounts:

| account | password | description                                                                                 |
| ------- | -------- | ------------------------------------------------------------------------------------------- |
| `admin` | `admin`  | Is member of the global admin group (can see and do anything)                               |
| `user`  | `user`   | Is member of the local user group (can not change access conditions or see internal graphs) |

![successful-login](../22-1-successful-login.png)

After successful login, you will see Corporate Memory interface. You can now proceed to the :arrow_right:[Getting Started](../../../getting-started/index.md) section.

Do not forget to change the passwords of your deployment, especially if it is available from the public internet. For this, take a look at [Change Passwords and Keys](../../configuration/keycloak/change-passwords-and-keys/index.md).

???+ info "Change the passwords for your needs"
    - To login in to keycloak and change the passwords
    - To change keycloak admin
    - To change cmem admin
    - To change cmem user
    - To change OAUTH_CLIENT_SECRET
