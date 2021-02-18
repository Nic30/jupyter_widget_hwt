jupyter_widget_hwt [![CircleCI](https://circleci.com/gh/Nic30/jupyter_widget_hwt.svg?style=svg)](https://circleci.com/gh/Nic30/jupyter_widget_hwt)
==================================================================================================================================================


A Jupyter witdgets for visualization of hwt based circuits.

Example [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Nic30/jupyter_widget_hwt.git/master?filepath=examples%2Findex.ipynb)


Installation
------------

To install use pip (package not yet in PIP, you have to install manually, see dockerfile):

    $ pip3 install jupyter_widget_hwt
    $ # optionally check
    $ # jupyter nbextension enable --py widgetsnbextension
    $ jupyter nbextension enable --py jupyter_widget_hwt
    $ # optionally you can also enable extension manager
    $ jupyter nbextensions_configurator enable --user

To install for jupyterlab

    $ jupyter labextension install jupyter_widget_hwt

For a development installation (requires npm),
```bash
pip3 install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter contrib nbextension install --user --symlink
git clone https://github.com/Nic30/jupyter_widget_hwt.git
cd jupyter_widget_hwt
# python3 setup.py build
pip3 install --upgrade --force-reinstall --no-cache-dir -e .
# jupyter-nbextension install --py --symlink jupyter_widget_hwt --user
jupyter nbextension enable jupyter_widget_hwt --user --py
# rebuild javascript
jupyter-nbextension install js --minimize=False --debug --user
# initialize this nbextension in the browser every time the notebook (or other app) loads
jupyter-nbextension enable jupyter_widget_hwt --user
```

Uninstall with all dependencies
```bash
pip3 uninstall -y hdlConvertorAst hwt hwtGraph ipCorePackager jupyter-widget-hwt pyDigitalWaveTools pyMathBitPrecise pycocotb
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

Potentially useful commands
----------------------------
```
# complete reinstall of jupyter
rm -r ~/.jupyter
pip3 install --upgrade --force-reinstall --no-cache-dir jupyter ipywidgets
```


This jupyter widget was build using [widget-cookiecutter](https://github.com/jupyter-widgets/widget-cookiecutter)