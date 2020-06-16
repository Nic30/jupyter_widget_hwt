jupyter_widget_hwt 
===============================
.. image:: https://travis-ci.org/Nic30/jupyter_widget_hwt.svg?branch=master
    :target: https://travis-ci.org/Nic30/jupyter_widget_hwt

A Jupyter witdgets for visualization of hwt based circuits.

Example [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Nic30/jupyter_widget_hwt.git/master?filepath=examples%2Fexample_simple.ipynb)


Installation
------------

To install use pip (package not yet in PIP, you have to install manually, see dockerfile):

    $ pip install jupyter_widget_hwt
    $ jupyter nbextension enable --py --sys-prefix jupyter_widget_hwt

To install for jupyterlab

    $ jupyter labextension install jupyter_widget_hwt

For a development installation (requires npm),
```bash
pip3 install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
git clone https://github.com/Nic30/jupyter_widget_hwt.git
cd jupyter_widget_hwt
sudo pip3 install -e .
# jupyter nbextension install --py --symlink jupyter_widget_hwt
jupyter nbextension enable --py jupyter_widget_hwt
# optionally
# jupyter labextension install js --minimize=False --debug
```


When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This take a minute or so to get started, but then allows you to hot-reload your javascript extension.
To see a change, save your javascript, watch the terminal for an update.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

Optionally you can manually download a depndencies and libraries with examples add them to a PYTHONPATH
if you do not want to install them.
```
export PYTHONPATH="$PYTHONPATH:$PWD/../pyMathBitPrecise:$PWD/../pyDigitalWaveTools:$PWD/../hdlConvertorAst:\
$PWD/../ipCorePackager:$PWD/../pycocotb:$PWD/../hwt:$PWD/../hwtLib:$PWD/../hwtGraph"
```
before running jupyter.


Running in Docker
-----------------

```bash
sudo docker build --tag jupyter_widget_hwt .
# use -p to propagate jupyter ports, -u to run as current user, -v to share exampes, -w to set work dir
sudo docker run -p8888:8888 \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    -v ${PWD}/examples:/opt/jupyter_widget_hwt_examples \
    -w /opt/jupyter_widget_hwt_examples \
    --name jupyter_widget_hwt -it jupyter_widget_hwt\
    jupyter notebook --ip 0.0.0.0 --port 8888

sudo docker rm jupyter_widget_hwt
```
