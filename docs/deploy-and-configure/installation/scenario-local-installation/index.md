# Introduction

This page describes a docker-compose based orchestration running on your local machine and accessible via browser.

The code examples in this section assumes that you have POSIX-compliant shell (linux, macOS or WSL for Windows).

## Requirements

- Access credentials to eccenca Artifactory and eccenca Docker Registry → [contact us to get yours](https://eccenca.com/en/contact)
- [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) installed locally
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally
- At least 4 CPUs and 12GB of RAM (recommended: 16GB) dedicated to docker

## Setup & Check Installation Environment

Download the [Corporate Memory docker orchestration](https://releases.eccenca.com/docker-orchestration/) from eccenca Artifactory.

Open a terminal window, create a directory, copy and extract docker orchestration there.

```bash
# create eccenca-corporate-memory directory in your ${HOME} and set as a working dir

$ mkdir ${HOME}/eccenca-corporate-memory && cd ${HOME}/eccenca-corporate-memory

# cp Corporate Memory docker orchestration distribution in the local directory
# Change VERSION to the version you have downloaded e.g. v20.03

$ cp ${HOME}/Downloads/cmem-orchestration-VERSION.zip ./
$ unzip cmem-orchestration-VERSION.zip
$ rm cmem-orchestration-VERSION.zip
$ git init && git add . && git commit -m "stub"
```

Check your local environment:

```bash
# run the following command (without $) to check your docker server version, should be at least 19.03
# to have the current security patches, always update your docker version to the latest one

$ docker info | grep -i version
Server Version: 19.03.8

# check docker-compose version, should be at least 1.25.0
# update to the latest version if necessary

$ docker-compose --version
docker-compose version 1.25.4, build 8d51620a

# login into eccenca docker registry

$ docker login docker-registry.eccenca.com
Username: yourusername
Password:
Login Succeeded
```

## Installation

To install Corporate Memory, you need to modify your local hosts file (located in /etc/hosts), minimal configuration is as follows:

```bash
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1 localhost
127.0.0.1   docker.localhost
127.0.0.1   corporate.memory
```

Corporate Memory uses stardog triple store as a backend. Stardog requires a license:

```bash
# if you have a license copy it to conf/stardog/stardog-license-key.bin
# for example

$ cp ~/Downloads/stardog-Eccenca-Developer-license-key.bin conf/stardog/stardog-license-key.bin
```

Check validity of your stardog license with `make stardog-license-check` command:

```bash
$ make stardog-license-check
docker run -it --rm --name stardog-license-check -v data:/data -v /Users/ivanermilov/eccenca-corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license info /data/stardog-license-key.bin
Licensee: Eccenca User (noreply@stardog.com), Eccenca
Type:  Subscription
Issued:  Mon Jan 20 19:39:39 GMT 2020
Expiration: 286 days
Support: 286 days
Quantity: 1
```

In case you do not have stardog license or your license has expired, request a trial license using `make stardog-license-request` command:

```bash
# if stardog-license-check is failing with invalid or expired license

$ make stardog-license-check
docker run -it --rm --name stardog-license-check -v data:/data -v /Users/ivanermilov/eccenca-corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license info /data/stardog-license-key.bin
The license is invalid: java.io.EOFException
make: *** [stardog-license-check] Error 1

# request stardog trial license

$ make stardog-license-request
docker run -it --rm --name stardog-license-check -v data:/data -v /Users/ivanermilov/eccenca-corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license request --force --output /data/stardog-license-key.bin
Thank you for downloading Stardog.
A valid license was not found in /data.
Would you like to download a trial license from Stardog (y/N)? y
Contacting Stardog...............
Please provide a valid email address to start your 60-day trial (we may occasionally contact you with Stardog news):  you@your-domain.com
Contacting license server.....................
Email validated. You now have a 60-day Stardog trial license. Starting Stardog...
                                                         %▄,
                                                       ░░Γ╬▀▀█▓╣⌐
                                                      ▄▓▌░░░░░░╨▓
                          .⌐⌐.                     .½▓█▌░░░░░░░░░▀▄
                     ⌐Γ░░░░░░░░░░Γ«⌐              ≤░▓███▓▓▌▄░░░░░▓▒█Γ⌐
                .»≥░░░░░░░░░░░░░░░░░░░░░≥▒▒▒▒▒▒▒░░░▓████████░░░░▐█▄╙░░≥░░≥[».
             ┌Γ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░╫█████████▌▒▒▒▒▒█▒▓▓▓▌▌▌▌▓▓█▓⌐
          .≥░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╢▒▒▓▓▒▒▒░░░░╟██████╙ └█b  ████▀▀▒█████▌
 Γ    .∩░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░██████`   ╙   ╟█▓∩  ███▀██▌
├░, .░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░╫██████        ▐█    ██    ╙
├░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▓██████          ,  '  ▄
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░░░░░░░░░░░░▓██████▓░░░░╕    ▐█▄   ██
.░░░░░░░░░░░░░░░░╣▄░░░░░▄╣▓██████▓▄░░░░░░░░░░░░░░░░░╢████████▒██░░╣   ██▄▄╣▒▒▌▄▄
 ░░░░░░░░░░░░░░,  └╙▀▀██████████████▓░░░░░░░░░░░░░░░░██████████▌░░░╦  █▒██████▌
 ╙░░░░░░░░░░░░░░░       ╙▀███████████░░░░░░░░░░░░░░▓░░█████▀▀▀░░░░░╬▒█████████
  '╙░░░░░░░░░▄▄▄`          └▀███████░░░░░░░░░░░░░░║██▓▄░▀▀░░░░░░░░░Γ "╙░░░░▀▀
    ╙░░▄╣▓▓██▀▀               ╙▀███▌░░░░░░░░░░░░░╢█████⌐   ╙░░░░░░░
    └╣███▀▀└                     ╙▀░░░░░░░░░░░░░╣████▀       '""`
                                 .░░░░░░░░░░░░╠▓███▀²
                                «░░░░░░░░░░░░╣███▀
                               ≥░░░░░░░░░░░┴▀▀╙
                            .Γ░░░░░░░░░░∩`
                á▀▀╕▄#▌▀▀░≥░░░░░░░╙∩"
                ░░░░░░░░░░∩`
                 └░░░░╙∩`
Thank you!

# check that you have a valid license now

$ make stardog-license-check
docker run -it --rm --name stardog-license-check -v data:/data -v /Users/ivanermilov/eccenca-corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license info /data/stardog-license-key.bin
Licensee: Stardog Trial User (you@your-domain.com), Stardog Union
Version: Stardog *
Type:  Trial
Issued:  Sun Mar 29 12:03:25 GMT 2020
Expiration: 59 days
Support: The license does not include maintenance.
Quantity: 3
```

Run the command to clean workspace, pull the images, start the Corporate Memory instance and load initial data:

```bash
$ cd ${HOME}/eccenca-corporate-memory

# Pulling the images will take time

$ make clean-pull-start-bootstrap

```

You should see the output as follows:

```bash
/usr/local/bin/docker-compose kill
/usr/local/bin/docker-compose stop
/usr/local/bin/docker-compose down --volumes --remove-orphans
Removing network dockerlocal_default
Removing volume dockerlocal_stardog
/usr/local/bin/docker-compose rm -v --force
No stopped containers
Removing data/dataplatform/shui-vocab/includes/widoco/
Pulling apache2         ... done
Pulling datamanager     ... done
Pulling dataintegration ... done
Pulling stardog         ... done
Pulling dataplatform    ... done
Pulling postgres        ... done
Pulling keycloak        ... done
Creating network "dockerlocal_default" with the default driver
Creating volume "dockerlocal_stardog" with default driver
Creating dockerlocal_apache2_1     ... done
Creating dockerlocal_stardog_1         ... done
Creating dockerlocal_postgres_1        ... done
Creating dockerlocal_datamanager_1     ... done
Creating dockerlocal_dataintegration_1 ... done
Creating dockerlocal_keycloak_1        ... done
Creating dockerlocal_dataplatform_1    ... done
/Users/ivanermilov/eccenca-corporate-memory//scripts/waitForSuccessfulStart.sh
Waiting for healthy orchestration...................... done
CMEM-Orchestration successfully started.
Run make logs to see log output
```

## Initial Login / Test

Open your browser and navigate to <http://docker.localhost>

![cmem-login-page](../22-1-cmem-login-page.png)

Click CONTINUE WITH LOGIN and use one of these default accounts:

| account | password | description                                                                                 |
| ------- | -------- | ------------------------------------------------------------------------------------------- |
| `admin` | `admin`  | Is member of the global admin group (can see and do anything)                               |
| `user`  | `user`   | Is member of the local user group (can not change access conditions or see internal graphs) |

![successful-login](../22-1-successful-login.png)

After successful login, you will see Corporate Memory interface. You can now proceed to the :arrow_right:[Getting Started](../../../getting-started/index.md) section.
