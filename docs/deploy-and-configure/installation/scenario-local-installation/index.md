---
icon: material/laptop
---
# Introduction

This page describes a `docker compose` based orchestration running on your local machine and accessible via browser.

The code examples in this section assumes that you have POSIX-compliant shell (linux, macOS or WSL for Windows).

## Requirements

-   Access credentials to eccenca Artifactory and eccenca Docker Registry → [contact us to get yours](https://eccenca.com/en/contact)
-   [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/install/) (v2) installed locally
-   [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally
-   [jq](https://jqlang.github.io/jq/download/) installed locally
-   make - build tools (apt-get install make) installed locally
-   At least 4 CPUs and 12GB of RAM (recommended: 16GB) dedicated to docker

## wsl installation and configuration

For all you need to start Powershell started as administrator.
Alternatively you can also install a WSL distribution from Microsoft Store.

Install WSL, then restart your Windows machine.

```shell
wsl --install
```

List available distributions

```shell
wsl --list --online
```

Install a distribution.
Chose from the `Name` column.
Here we use a Debian based distribution like Debian or any Ubuntu.
However other Distributions might work as well.

```shell
wsl --install Debian
```

Check if you use wsl version 2 (this is nessessary to use systemd services)

```shell
wsl -l -v
```

Install version 2 components (this requires a windows restart)

```shell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Enter WSL machine

```shell
wsl -d Debian
```

Enable `generateHosts = false` in your `/etc/hosts` file to make sure that this file won't be overwritten from the host system on every restart.

To be able to use systemd services and commands make sure `/etc/wsl.conf` is available with this content:

```shell
[boot]
systemd=true
```

(Optional) If you need to restart your WSL use in Powershell:

```shell
wsl --shutdown
```

(optional) you can create a `.wslconfig` file under `C:\users\<your username>` to specify some system resources like:

```shell
[wsl2]
memory=16GB # restrict ram wsl can use
processors=4 # restrict cpu-cores
swap=8GB # set swap size
swapFile=C:/Users/<your username>/wsl/Debianswap.vhdx  # location to swap-file
```

## Setup & Check Installation Environment

Open a terminal window, create a directory, copy and extract docker orchestration there.

```shell
# Create eccenca-corporate-memory directory in your ${HOME} and set as a
# working dir.

$ mkdir ${HOME}/eccenca-corporate-memory && cd ${HOME}/eccenca-corporate-memory

# download the Corporate Memory orchestration distribution
$ curl https://releases.eccenca.com/docker-orchestration/latest.zip \
    > cmem-orchestration.zip

# unzip the orchestration and move the unzipped directory
$ unzip cmem-orchestration.zip
$ rm cmem-orchestration.zip
$ mv cmem-orchestration-v* cmem-orchestration
$ cd cmem-orchestration
$ git init && git add . && git commit -m "stub"
```

Check your local environment:

```shell
# Run the following command to check your docker server version.
# To have the current security patches, always update your docker version
# to the latest one.

$ docker version | grep -i version
Docker version: 27.5.1, build 9f9e405

# Check docker compose version, should be at least v2.*.*
# update to the latest version if necessary

$ docker compose version
Docker Compose version v2.32.4

# login into eccenca docker registry

$ docker login docker-registry.eccenca.com
Username: yourusername
Password:
Login Succeeded
```

## Installation

To install Corporate Memory, you need to modify your local hosts file (located in /etc/hosts), minimal configuration is as follows:

```shell
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1 localhost
127.0.0.1 docker.localhost
```

Corporate Memory uses Ontotext GraphDB triple store as default backend.
Graphdb is available as free version and does not requires a license.
If you have a license for Ontotext GraphDB you can copy the file to the `license`folder inside Corporate Memory's root folder.
Then edit the file `compose/docker-compose.store.graphdb.yml` and adjust to fit your filename like this:

```shell
# adapt this line if a license ca be provided
#      - "{DEST}/licenses/graphdb.license:/opt/graphdb/dist/conf/graphdb.license"
```

Run the command to clean workspace, pull the images, start the Corporate Memory instance and load initial data:

```shell
# Pulling the images will take time

$ make clean-pull-start-bootstrap
```

You should see the output as follows:

```shell
make[1]: Entering directory '/home/ttelleis/cmem-dist/cmem-orchestration'
The target cleans up everything and esp. REMOVES ALL YOUR DATA. Do you want to continue?

You can avoid this question / interruption by setting CO_I_KNOW_WHAT_I_DO to true.
Type '1' for Yes or type '2' for No.

1) Yes
2) No
#? 1
make check-env kill stop down rm-log-dir
make[2]: Entering directory '/home/ttelleis/cmem-dist/cmem-orchestration'
/usr/bin/docker compose  kill
no container to kill/usr/bin/docker compose  stop
/usr/bin/docker compose  down --volumes --remove-orphans || exit 0
/usr/bin/docker compose  up -d
[+] Running 12/12
 ✔ Network dockerlocalhost_default              Created                   0.1s
 ✔ Volume "dockerlocalhost_store_volume"        Created                   0.0s
 ✔ Volume "dockerlocalhost_import_volume"       Created                   0.0s
 ✔ Volume "dockerlocalhost_postgres_volume"     Created                   0.0s
 ✔ Container dockerlocalhost-store-1            Started                   1.0s
 ✔ Container dockerlocalhost-apache2-1          Started                   1.3s
 ✔ Container dockerlocalhost-cmemc-1            Started                   1.2s
 ✔ Container dockerlocalhost-datamanager-1      Started                   1.3s
 ✔ Container dockerlocalhost-postgres-1         Healthy                   6.6s
 ✔ Container dockerlocalhost-keycloak-1         Healthy                  47.8s
 ✔ Container dockerlocalhost-dataplatform-1     Started                  48.3s
 ✔ Container dockerlocalhost-dataintegration-1  Started                  48.3s
/home/ttelleis/cmem-dist/cmem-orchestration//scripts/waitForSuccessfulStart.dist.sh
Waiting for healthy orchestration.................. done
Remove existing bootstrap data from triple store and import shipped data from DP
chmod a+r conf/cmemc/cmemc.ini
docker compose run -i --rm --env "OAUTH_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a" --volume /home/ttelleis/cmem-dist/cmem-orchestration/data:/data --volume /home/ttelleis/cmem-dist/cmem-orchestration/conf/cmemc/cmemc.ini:/config/cmemc.ini cmemc -c cmem admin store bootstrap --import
Update or import bootstrap data ... done
make[1]: Leaving directory '/home/ttelleis/cmem-dist/cmem-orchestration'

CMEM-Orchestration successfully started with store graphdb.
Please open http://docker.localhost:80 for validation.
Run make logs to see log output
```

## Initial Login / Test

Open your browser and navigate to <http://docker.localhost>

| account | password | description |
| ------- | -------- | ----------- |
| `admin` | `admin`  | Is member of the global admin group (can see and do anything) |

After successful login, you will see Corporate Memory interface. You can now proceed to the :arrow_right:[Getting Started](../../../getting-started/index.md) section.

### Backup

To create a backup you have to prepare the backup folders. Make sure these folders exists and have write permissions. Run this:

```shell
# assuming you are currently in the the cmem-orchestration folder
$ mkdir -p data/backups/graphs data/backups/workspace
$ chmod 777 data/backups/graphs data/backups/workspace

$ make backup
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

### Caveats

In case you have problems starting and receive error messages like Port 80 already assigned.
Then check if a apache2 service is running and remove it.

```shell
sudo service apache2 status
sudo service stop apache2
```
