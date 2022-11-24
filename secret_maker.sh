#/bin/bash

DOMAIN=$1
USERNAME=$2
TOKEN=$3

STRING=$(echo -n $USERNAME:$TOKEN | base64 -w 0)

echo "Set the following as a project level environment variable to enable using private images from ${DOMAIN}"

echo "GITPOD_IMAGE_AUTH = ${DOMAIN}:${STRING}"
