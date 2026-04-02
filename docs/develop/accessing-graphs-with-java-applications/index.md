---
icon: material/language-java
tags:
    - Java
hide:
    - toc
---
# Accessing Graphs with Java Applications

## Introduction

This short recipe covers how to connect to Corporate Memory using a Java program.
Such program can connect to Corporate Memory at any time autonomously, independently of whether a user is logged in or not.

## Java Example

This example assumes that there is a Corporate Memory instance runnning at `http://docker.localhost`, and the programmer has access to its files.
The process is very simple:

1. Obtain a Bearer token.
      1. Go to the file `cmem-orchestration/environments/config.env`, and get the client secret from variable `CMEM_SERVICE_ACCOUNT_CLIENT_SECRET`.
      1. With the client secret, connect to to the OpenID endpoint to obtain the Bearer token.
1. Use the Bearer token to connect to Corporate Memory, and, for example, execute a query.

The following code provides a simple implementation of the process:

```java title="JavaCMEMHTTPClient.java"
package com.eccenca.cmem.client;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

public class HTTPClient {

  public static void main(String[] args) throws ClientProtocolException, IOException {

    // We assume that the Corporate Memory instance is running at docker.localhost
    String openidConnectEndpoint = "http://docker.localhost/auth/realms/cmem/protocol/openid-connect/token";

    // Get the client secret to obtain the bearer token from file cmem-orchestration/environments/config.env,
    // variable CMEM_SERVICE_ACCOUNT_CLIENT_SECRET
    String clientSecret = "...";

    // Create an HTTP Client
    CloseableHttpClient client = HttpClientBuilder.create().build();

    // POST request to obtain the bearer token for later authorization
    HttpPost httpPostToken = new HttpPost(openidConnectEndpoint);
    httpPostToken.setHeader("Content-type", "application/x-www-form-urlencoded");
    List < NameValuePair > params = new ArrayList < NameValuePair > ();
    params.add(new BasicNameValuePair("grant_type", "client_credentials"));
    params.add(new BasicNameValuePair("client_id", "cmem-service-account"));
    params.add(new BasicNameValuePair("client_secret", clientSecret));
    httpPostToken.setEntity(new UrlEncodedFormEntity(params));

    // Parse the JSON response to obtain the bearer token
    HttpResponse httpResponseToken = client.execute(httpPostToken);
    HttpEntity httpEntity = httpResponseToken.getEntity();
    String responseBody = EntityUtils.toString(httpEntity);
    JSONObject obj = new JSONObject(responseBody);
    String bearerToken = "Bearer " + obj.getString("access_token");

    // POST request to query the default SPARQL endpoint with the bearer token obtained above
    HttpPost httpPostQuery = new HttpPost("http://docker.localhost/dataplatform/proxy/default/sparql");
    httpPostQuery.setHeader("Accept", "application/sparql-results+json");
    httpPostQuery.setHeader("Content-type", "application/x-www-form-urlencoded");
    httpPostQuery.setHeader("Authorization", bearerToken);
    final ArrayList < NameValuePair > postParameters = new ArrayList < NameValuePair > ();
    postParameters.add(new BasicNameValuePair("query", "SELECT * WHERE {?s ?p ?o} LIMIT 10"));
    httpPostQuery.setEntity(new UrlEncodedFormEntity(postParameters));

    // The response (variable responseBodyQuery bellow) should have some bindings:
    //  {
    //     "head": {
    //       "vars": [ "s" , "p" , "o" ]
    //     } ,
    //     "results": {
    //       "bindings": [
    HttpResponse httpResponseQuery = client.execute(httpPostQuery);
    HttpEntity httpEntityQuery = httpResponseQuery.getEntity();
    String responseBodyQuery = EntityUtils.toString(httpEntityQuery);
  }
}
```
