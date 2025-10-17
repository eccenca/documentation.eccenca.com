---
icon: simple/kubernetes
---
# Kubernetes deployment with Helm

## Introduction

This page describes basic principles to install corporate memory in a kubernetes cluster with ```helm``` and ```kubectl```.
It will not explain you basic principles of kubernetes or help in installing the tools.
In the next section you will find useful links for installing the required tools. 

The code examples in this section assumes that you have POSIX-compliant shell (linux, macOS or WSL for Windows), a working ```KUBECONFIG``` and a full provisioned cluster.

## Requirements

-   Access credentials to eccenca Artifactory and eccenca Docker Registry → [contact us to get yours](https://eccenca.com/en/contact)
-   Kubectl from https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
-   Helm from https://helm.sh/docs/intro/install/
-   If deploying on K3D, download a static binary from https://github.com/k3d-io/k3d/releases (or use the script at https://k3d.io/ to do the same).



## Architecture
 ![CMEM Helm Chart Architecture](images/cmem-helm-architecture.svg)



## Installation GraphDB

To install GraphDB, we will use the Ontotext Helm chart.

### 1. Add the Ontotext Helm repository

First, add the Ontotext repository to Helm:

```console
helm repo add ontotext https://maven.ontotext.com/repository/helm-public/
helm repo update

```

### 2. Create a `graphdb-values.yaml` file

Create a file named `graphdb-values.yaml` to configure your GraphDB deployment.
For a basic setup, you can start with an empty file and add configurations as needed.
For production, you should configure persistence, resource limits, and any specific GraphDB settings.
Download a [basic example value file](files/graphdb-values.yaml) (`graphdb-values.yaml`).

Here is an example that disables ingress and sets resources, persistence and security:

```yaml
ingress:
  enabled: false

resources:
  limits:
    memory: 4Gi
    cpu: 2000m
  requests:
    memory: 4Gi
    cpu: 500m

security:
  enabled: true
  provisioningUsername: provisioner
  provisioningPassword: iHaveSuperpowers

persistence:
  enabled: true
  volumeClaimTemplate:
    name: "storage"
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 5Gi
```

### 3. Install the GraphDB chart

Now, install the GraphDB chart using Helm:

```console
helm upgrade -i graphdb ontotext/graphdb \
  --namespace graphdb --create-namespace \
  -f graphdb-values.yaml
```

This will deploy GraphDB into the `graphdb` namespace and it will create the namespace if it not exist.

### 4. Accessing GraphDB

To access the GraphDB UI without exposing it via an Ingress, you can use `kubectl port-forward`. This is useful for initial setup and verification.

First, get the name of the GraphDB service:

```console
kubectl get svc -n graphdb
```

Assuming the service is named `graphdb`, forward a local port to the service port (7200):

```console
kubectl port-forward svc/graphdb 7200:7200 -n graphdb
```

Now you can access the GraphDB workbench in your browser at [http://localhost:7200](http://localhost:7200).


## Installation Keycloak

This guide provides instructions on how to install Keycloak using the provided Helm chart.

### 1. Obtain the Chart

```console
helm repo add --force-update eccenca https://helm.eccenca.com
helm repo update eccenca
helm search repo eccenca
```

You can also download the latest version here:

```console
wget https://helm.eccenca.com/keycloak/latest.tgz
tar -xzf latest.tgz
cd keycloak-helm
```

```console
# this requires gitlab.eccenca.com access
git clone ssh://git@gitlab.eccenca.com:8101/devops/keycloak-helm.git
cd keycloak-helm
```

Assuming you have the chart in a local directory named `keycloak-chart`.

### 2. Create a namespace

We will use the `keycloak` namespace.

```console
kubectl create namespace keycloak
```

### 3. Create a `keycloak-values.yaml` file

Create a file named `keycloak-values.yaml` to configure your Keycloak deployment. At a minimum, you should configure the initial admin credentials and the ingress settings.
You can also [download the minimum file here:](files/keycloak-values.yaml) (`keycloak-values.yaml`).
```yaml
---
postgres:
  internal: true
  provisioning:
    enabled: true
    # If true, this will drop the public schema and re-provision the database on every start.
    force: true

ingress:
  enabled: true
  className: nginx
  annotations:
    cert-manager.io/common-name: "kc.docker.localhost"
  hosts:
    - host: "kc.docker.localhost"
      paths:
        - path: /auth
          pathType: Prefix
          serviceName: keycloak
          servicePort: 8080
  tls:
    - hosts:
         - "kc.docker.localhost"
      secretName:  keycloak-ingress-cert
```

You will also need to configure TLS, for example by using `cert-manager`.
Please se the `README.md` file in the chart repository for explanations.

### 4. Install the chart

Use `helm` to deploy the chart into the `keycloak` namespace.

With local extracted helm chart:
```console
helm upgrade -i keycloak ./keycloak-helm \
  --namespace keycloak --create-namespace\
  -f keycloak-values.yaml
```

Or from helm repository:

```console
helm upgrade -i keycloak eccenca/keycloak-helm \
  --namespace keycloak --create-namespace\
  -f keycloak-values.yaml
```

This command will install the Keycloak chart in the `gemkeycloak` namespace using your custom configuration.
Be aware, that the example tries to restore the database from a dump provided inside the chart. You can disable this, if you like.

### 5. Accessing Keycloak

Once deployed, you can access the Keycloak UI via the hostname you configured in your `keycloak-values.yaml`.

```bash
echo "https://<your-keycloak-hostname>/auth"
```


## Installation Corporate Memory

This guide provides instructions on how to install the chart using `kubectl` and `helm`.
You need to have a keycloak instance and a supported graph database installed.

### 1. Download the chart or use our helm repository or clone the repository

```console
wget https://releases.eccenca.com/cmem-helm/latest.tgz
tar -xzf latest.tgz
cd cmem
```

```console
helm repo add --force-update cmem-helm https://helm.eccenca.com
helm repo update cmem-helm
```

```console
# this requires gitlab.eccenca.com access
git clone https://gitlab.eccenca.com/cmem/cmem-helm.git
cd cmem-helm
```

### 2. Create a namespace

It is recommended to install CMEM in its own namespace.

```console
kubectl create namespace <your-namespace>
```
Replace `<your-namespace>` with the desired namespace (e.g., `cmem`).

### 3. Create Docker registry credentials

To pull the CMEM images, you need to provide credentials to your Docker registry.

```console
kubectl create secret docker-registry eccenca-docker-registry-credentials \
  --docker-server=https://docker-registry.eccenca.com \
  --docker-username=<your-docker-username> \
  --docker-password=<your-docker-password> \
  -n <your-namespace>
```
Replace the placeholders with the provided registry details and credentials.

### 3b. (optional) Create cmem license secret

By default, Corporate Memory is subject to the eccenca free Personal, Evaluation and Development License Agreement (PEDAL), a license intended for non-commercial usage.

If you have a dedicated license file, create a secret with a `license.asc` data entry:

```console
kubectl create secret generic cmem-license \
  --from-file license.asc
  -n <your-namespace>
```

Then, add the secret name to your `values.yaml` file for the key `global.license`.

For more background on license, see also: https://documentation.eccenca.com/latest/deploy-and-configure/configuration/dataplatform/application-full/

### 4. Configure your deployment

Copy the `values.sample.yaml` to a new file, for example `my-values.yaml`.

```console
cp values.sample.yaml my-values.yaml
```

Edit `my-values.yaml` and adjust the configuration to your needs.
At a minimum, you will need to configure the hostname, and connection details for your Ingress or Route, Keycloak and GraphDB.

```yaml
ingress:
  enabled: true
  className: nginx
  annotations:
    cert-manager.io/cluster-issuer: <cluster-issuer-if-present>
  hosts:
    - host: "<your-cmem-hostname>"
      paths:
        - path: /
          pathType: Prefix
          serviceName: explore
          servicePort: 8080
        - path: /dataintegration
          pathType: Prefix
          serviceName: dataintegration
          servicePort: 8080
  tls:
    - hosts:
         - "<your-cmem-hostname>"
      secretName:  cmem-ingress-cert

global:
  protocol: "https"
  cmemClientId: cmem-service-account
  cmemClientSecret: c8c12828-000c-467b-9b6d-2d6b5e16df4a
  hostname: "<your-hostname>"
  keycloakBaseUrl: https://<your-keycloak-hostname>/auth/'
  keycloakIssuerUrl: https://<your-keycloak-hostname>/auth/realms/cmem'

  # If you specified customCACerts, an initContainer is added to DI and EXPLORE to append your custom CA to the system-wide TrustStore.
  # Here you can optionally specify resource requests and limits for that initContainer.
  customCACerts: {}

  # (optional if 3b was created)
  # license: cmem-license

explore:
  store:
    graphdb:
      enabled: true
      repository: cmem
      user: provisioner
      password: "iHaveSuperpowers"
      host: "<your-graphdb-hostname>"
      sslEnabled: false

```

### 5. Install the chart

Use `helm` to deploy the chart.

```console
# In case you have the chart or repostiory locally available
helm upgrade --install <release-name> .
  --namespace <your-namespace> \
  -f my-values.yaml

# or use our helm repository
helm upgrade --install <release-name> cmem-helm/cmem
  --namespace <your-namespace> \
  -f my-values.yaml
```

- `<release-name>`: A name for this release (e.g., `cmem`).
- `<your-namespace>`: The namespace created in step 2.

This command will install the chart in the specified namespace using your custom configuration.

_See [configuration](#configuration) below for more details on available options._

_See [helm install](https://helm.sh/docs/helm/helm_install/) for command documentation._

### 6. Verify the installation

After the installation is complete, you can check the status of the pods:

```console
kubectl get pods -n <your-namespace>
```

You can also check the rollout status of the statefulsets:

```console
kubectl rollout status statefulset/explore -n <your-namespace>
kubectl rollout status statefulset/dataintegration -n <your-namespace>
```
