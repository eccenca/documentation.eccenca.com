---
icon: material/redhat
---
# Scenario: RedHat Enterprise Linux 7

## Introduction

This page describes a docker-compose based orchestration running on RedHat Enterprise Linux 7 (RHEL 7) inside a VirtualBox virtual machine.

## Requirements

- [Virtualbox](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html) and [vagrant](https://www.vagrantup.com/downloads.html) installed locally
- Terminal with ssh client installed locally
- POSIX-compatible command line interface (Linux, macOS or WSL for Windows)

## Provisioning

Create a working directory for this scenario and inside the working directory `Vagrantfile` with the following contents:

```bash linenums="1"
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vbguest.auto_update = false
  config.vbguest.no_remote = true

  config.vm.box = "generic/rhel7"
  config.ssh.private_key_path = File.expand_path('~/.vagrant.d/insecure_private_key')
  config.ssh.insert_key = false

  config.vm.define "rhel7" do |rhel7|
    rhel7.vm.network "private_network", ip: "10.10.10.10"
    rhel7.vm.hostname = "rhel7.eccenca.local"

    rhel7.vm.provider "virtualbox" do |dpvm|
      dpvm.memory = 10240
      dpvm.cpus = 4
    end
  end
end
```

Spin up the virtual machine:

```bash linenums="1"
$ vagrant up
Bringing machine 'rhel7' up with 'virtualbox' provider...
==> rhel7: Importing base box 'generic/rhel7'...
==> rhel7: Matching MAC address for NAT networking...
==> rhel7: Checking if box 'generic/rhel7' is up to date...
==> rhel7: A newer version of the box 'generic/rhel7' for provider 'virtualbox' is
==> rhel7: available! You currently have version '1.9.18'. The latest is version
==> rhel7: '2.0.6'. Run `vagrant box update` to update.
==> rhel7: Setting the name of the VM: rhel7_rhel7_1587731923819_11065
==> rhel7: Clearing any previously set network interfaces...
==> rhel7: Preparing network interfaces based on configuration...
    rhel7: Adapter 1: nat
    rhel7: Adapter 2: hostonly
==> rhel7: Forwarding ports...
    rhel7: 22 (guest) => 2222 (host) (adapter 1)
==> rhel7: Running 'pre-boot' VM customizations...
==> rhel7: Booting VM...
==> rhel7: Waiting for machine to boot. This may take a few minutes...
    rhel7: SSH address: 127.0.0.1:2222
    rhel7: SSH username: vagrant
    rhel7: SSH auth method: private key
==> rhel7: Machine booted and ready!
==> rhel7: Checking for guest additions in VM...
    rhel7: The guest additions on this VM do not match the installed version of
    rhel7: VirtualBox! In most cases this is fine, but in rare cases it can
    rhel7: prevent things such as shared folders from working properly. If you see
    rhel7: shared folder errors, please make sure the guest additions within the
    rhel7: virtual machine match the version of VirtualBox you have installed on
    rhel7: your host and reload your VM.
    rhel7:
    rhel7: Guest Additions Version: 5.2.30 r130521
    rhel7: VirtualBox Version: 6.0
==> rhel7: Setting hostname...
==> rhel7: Configuring and enabling network interfaces...
```

Now you can connect to the virtual machine using `~/.vagrant.d/insecure_private_key` ssh key:

```bash linenums="1"
# add vagrant ssh key to your keychain
ssh-add ~/.vagrant.d/insecure_private_key

# connect to the VM
ssh vagrant@10.10.10.10
```

!!! info
    For username:password in curl command use the credentials to access eccenca Artifactory and docker registry.

Install the necessary software Inside the virtual machine and download the Corporate Memory orchestration from [releases.eccenca.com](http://releases.eccenca.com/):

```bash linenums="1"
# switch to superuser
sudo su

# Register your RHEL instance
subscription-manager register
export POOL_ID=$(subscription-manager list --available | grep "Pool ID:" | cut -d':' -f 2 | tr -d '[:space:]')
subscription-manager attach --pool=${POOL_ID}

# enable RHEL repositories
subscription-manager repos --enable=rhel-7-server-rpms
subscription-manager repos --enable=rhel-7-server-extras-rpms
subscription-manager repos --enable=rhel-7-server-optional-rpms

# install and start docker
yum install docker device-mapper-libs device-mapper-event-libs
systemctl start docker.service
systemctl enable docker.service

# install docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /bin/docker-compose
chmod +x /bin/docker-compose

# Install necessary system utilities
yum install unzip git jq

# get corporate memory orchestration package
curl -u username https://releases.eccenca.com/docker-orchestration/cmem-orchestration-v21.11.5.zip > cmem-orchestration.zip
unzip cmem-orchestration.zip
rm cmem-orchestration.zip
mv cmem-orchestration-v* /opt/corporate-memory
cd /opt/corporate-memory
git init && git add README.md && git commit -m "init"

# give docker daemon access to /opt/corporate-memory directory
chcon -Rt svirt_sandbox_file_t /opt/corporate-memory
```

Create `/opt/corporate-memory/environments/prod.env` file with the following contents:

```bash linenums="1"
#!/bin/bash linenums="1"

CMEM_SERVICE_ACCOUNT_CLIENT_SECRET=c8c12828-000c-467b-9b6d-2d6b5e16df4a
STARDOG_PASSWORD=admin
TRUSTSTOREPASS=Aimeik5Ocho5riuC
DEPLOYHOST=corporate.memory

DI_VERSION=v20.03
DP_VERSION=v20.03
DM_VERSION=v20.03
APACHE2_VERSION=v2.6.0
KEYCLOAK_VERSION=v6.0.1-2
POSTGRES_VERSION=11.5-alpine
STARDOG_VERSION=v7.2.0-1

DATAINTEGRATION_JAVA_TOOL_OPTIONS=-Xmx2g
DATAPLATFORM_JAVA_TOOL_OPTIONS=-Xms1g -Xmx2g
STARDOG_SERVER_JAVA_ARGS=-Xms1g -Xmx1g -XX:MaxDirectMemorySize=2g

DEPLOYPROTOCOL=https
PORT=443
APACHE_BASE_FILE=docker-compose.apache2-ssl.yml
DATAINTEGRATION_BASE_FILE=docker-compose.dataintegration-ssl.yml
APACHE_CONFIG=default.ssl.conf
PROXY_ADDRESS_FORWARDING=true
```

Login into eccenca docker registry:

```bash linenums="1"
docker login docker-registry.eccenca.com
```

Provide a stardog license or request a trial license:

```bash linenums="1"
# check validity of your license
$ make stardog-license-check
docker run -it --rm --name stardog-license-check -v data:/data -v /opt/corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license info /data/stardog-license-key.bin
The license is invalid: java.io.EOFException
make: *** [custom.dist.Makefile:5: stardog-license-check] Error 1

# request stardog trial license
$ make stardog-license-request
docker run -it --rm --name stardog-license-check -v data:/data -v /opt/corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license request --force --output /data/stardog-license-key.bin
Thank you for downloading Stardog.
A valid license was not found in /data.
Would you like to download a trial license from Stardog (y/N)? y
Contacting Stardog..............
Please provide a valid email address to start your 60-day trial (we may occasionally contact you with Stardog news):  ivan.ermilov@eccenca.com
Contacting license server...................
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

# check the license again
$ make stardog-license-check
docker run -it --rm --name stardog-license-check -v data:/data -v /opt/corporate-memory//conf/stardog/stardog-license-key.bin:/data/stardog-license-key.bin docker-registry.eccenca.com/complexible-stardog:v7.2.0-1 stardog-admin license info /data/stardog-license-key.bin
Licensee: Stardog Trial User (ivan.ermilov@eccenca.com), Stardog Union
Version: Stardog *
Type:  Trial
Issued:  Mon Mar 30 10:47:17 GMT 2020
Expiration: 59 days
Support: The license does not include maintenance.
Quantity: 3
```

Finally deploy the Corporate Memory instance:

```bash linenums="1"
# create local truststore
CONFIGFILE=environments/prod.env make buildTrustStore

# start and bootstrap Corporate Memory
CONFIGFILE=environments/prod.env make clean-pull-start-bootstrap
```

You have successfully deployed a Corporate Memory instance.

## Access Corporate Memory Instance

On your localhost where you are running VirtualBox, modify /etc/hosts file:

```bash linenums="1"
echo "10.10.10.10 corporate.memory" >> /etc/hosts
```

Open your browser and navigate to [https://corporate.memory]<https://corporate.memory>

| account | password | description                                                                                 |
| ------- | -------- | ------------------------------------------------------------------------------------------- |
| `admin` | `admin`  | Is member of the global admin group (can see and do anything)                               |
| `user`  | `user`   | Is member of the local user group (can not change access conditions or see internal graphs) |

![successful-login](../22-1-successful-login.png)

After successful login, you will see Corporate Memory interface. You can now proceed to the :arrow_right:[Getting Started](../../../getting-started/index.md) section.
