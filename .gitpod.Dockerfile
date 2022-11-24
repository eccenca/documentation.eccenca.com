FROM gitpod/workspace-full

USER gitpod

FROM docker-registry.eccenca.com/eccenca-python:v3.9.14-2

RUN task:check

EXPOSE 8000
