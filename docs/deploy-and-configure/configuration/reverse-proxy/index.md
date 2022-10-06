# Reverse Proxy

A reverse proxy forwards all requests from the users to the called service and returns the result to the users.A reverse proxy forwards all requests from the users to the called service and returns the result to the users. Corporate Memory is tested with an Apache HTTP server as a reverse proxy.

Reverse proxy is a necessary component in the Corporate Memory deployment. It enables you to:

- define routes for all the components within one domain name,
- expose only ports 80 and 443 to the outside network, all other communication would be performed in the internal network, and
- ease configuration and management of the SSL certificates.

This also enables you to activate the [Linked Data delivery mode](#linked-data-delivery-mode) of DataPlatform. The Linked Data delivery mode is able to serve Linked Data that uses the same namespace as the configured domain name as resolvable URIs including content negotiation.

## Example Configuration for Apache HTTP server

apache configuration template

```code
<VirtualHost *:80>
    ServerName corporate-memory.example.com
    Redirect permanent / https://corporate-memory.example.com/
</Virtualhost>
<VirtualHost *:443>

    ServerName corporate-memory.example.com
    ServerAlias www.corporate-memory.example.com
    ProxyPreserveHost On

    ProxyPass /auth https://keycloak.host/auth retry=0
    ProxyPassReverse /auth https://keycloak.host/auth

    ProxyPass /dataplatform https://dataplatform.host/dataplatform retry=0
    ProxyPassReverse /dataplatform https://dataplatform.host/dataplatform

    RewriteEngine  on
    RewriteRule    "^/dataintegration$"  "/dataintegration/" [R]

    RewriteCond %{HTTP:Upgrade} =websocket [NC]
    RewriteRule "/dataintegration/(.*)" wss://dataintegration.host/dataintegration/$1 [P,L]
    RewriteCond %{HTTP:Upgrade} !=websocket [NC]
    RewriteRule "/dataintegration/(.*)" https://dataintegration.host/dataintegration/$1 [P,L]

    ProxyPassReverse /dataintegration https://dataintegration.host/dataintegration

    ProxyPass / https://datamanager.host/ retry=0
    ProxyPassReverse / https://datamanager.host/

    # https://github.com/gitlabhq/gitlabhq/issues/8924
    AllowEncodedSlashes NoDecode

    # Network timeout in seconds for proxied requests (default 300)
    # http://serverfault.com/questions/500467/apache2-proxy-timeout/583266
    ProxyTimeout 1200

    #######################
    # SSL
    #######################
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/ssl-bundle.crt
    SSLCertificateKeyFile /etc/apache2/ssl/cert.key
    SSLCertificateChainFile /etc/apache2/ssl/cert.cabundle
</VirtualHost>
```

Information about the runtime environment, which is used to run DataPlatform, DataIntegration and DataManager, is hidden.

!!! note
    Keep in mind, that you have to adjust the location paths/URLs in the DataManager and DataIntegration configuration files.

## Linked Data delivery mode

The Linked Data delivery mode is able to serve data that uses the same namespace as the configured domain name as resolvable URIs including content negotiation.

Therefore you can use the following template (e.g.: <https://corporate-memory.example.com>):

- <https://dataplatform.corporate-memory.example.com> (DataPlatform)
- <https://dataplatform.corporate-memory.example.com/vocabulary/example/> (a custom vocabulary)
- with HTTPS enforcement (recommended)

apache sample config for linked data delivery

```conf
<VirtualHost *:80>
  ServerName dataplatform.corporate-memory.example.com
  Redirect permanent / https://dataplatform.corporate-memory.example.com/
</Virtualhost>

<VirtualHost *:443>

  ServerName dataplatform.corporate-memory.example.com

  RewriteEngine On
  ProxyPreserveHost On

  Define reverse_url\
  "http://DATAPLATFORM_SERVICE_HOST:8080/proxy/default/graph?owlImportsResolution=false&graph="

  # Return complete graphs for URIs ending with slash
  RewriteCond %{REQUEST_METHOD} ^(.*)
  RewriteRule "^/vocabulary/(.+)/$"\
    "${reverse_url}%{REQUEST_SCHEME}://%{HTTP_HOST}%{REQUEST_URI}"\
    [P]

  # Everything else is just plain proxied
  RewriteRule "^/(.*)$" "http://DATAPLATFORM_SERVICE_HOST:8080/$1" [P]

  # Reverse proxy only needed for login via browser (e.g. with DataManager)
  ProxyPassReverse "/" "http://DATAPLATFORM_SERVICE_HOST:8080/"

  # ssl-config
  SSLEngine on
  SSLCertificateFile /etc/apache2/ssl/ssl-bundle.crt
  SSLCertificateKeyFile /etc/apache2/ssl/cert.key
  SSLCertificateChainFile /etc/apache2/ssl/cert.cabundle
</VirtualHost>
```

!!! note
    Keep in mind, that the vocabulary namespace is using `https` as protocol, too.
