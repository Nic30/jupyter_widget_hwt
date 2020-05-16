# note that this Dockerfile is meant for notebooks and you can install this package directly
FROM ubuntu:20.04
# https://github.com/binder-examples/minimal-dockerfile
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN apt update &&\
    DEBIAN_FRONTEND="noninteractive" apt install python3 python3-pip npm git -y

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}


# [mybinder specific]
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root

WORKDIR ${HOME}
RUN pip3 install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension
# RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
# RUN pip3 install jupyter_contrib_nbextensions &&\
#    jupyter nbextension install --py jupyter_widget_hwt &&
RUN pip3 install .
#RUN jupyter labextension install js 
#RUN python3 setup.py install &&\
#    jupyter nbextension install --py jupyter_widget_hwt &&\
#    jupyter nbextension enable  --py jupyter_widget_hwt
RUN  pip3 install git+https://github.com/Nic30/hwtLib.git

RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
