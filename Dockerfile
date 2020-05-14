# note that this Dockerfile is meant for notebooks and you can install this package directly
FROM ubuntu:20.04
# https://github.com/binder-examples/minimal-dockerfile
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN apt update && apt upgrade -yq &&\
    apt install python3

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}


# [mybinder specific]
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root

WORKDIR ${HOME}
RUN python3 setup.py install

RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
