jupyter-widget-hwt
===============================

A Jupyter witdgets for visualization of hwt based circuits.

Installation
------------

To install use pip:

    $ pip install jupyter-widget-hwt
    $ jupyter nbextension enable --py --sys-prefix jupyter-widget-hwt

To install for jupyterlab

    $ jupyter labextension install jupyter-widget-hwt

For a development installation (requires npm),
```bash
sudo jupyter labextension install @jupyter-widgets/jupyterlab-manager
sudo pip3 install jupyterlab
git clone https://github.com/Nic30/jupyter-widget-hwt.git
cd jupyter-widget-hwt
sudo pip3 install -e .
sudo jupyter nbextension install --py --symlink --sys-prefix jupyter_widget_hwt
sudo jupyter nbextension enable --py --sys-prefix jupyter_widget_hwt
sudo jupyter labextension install js --minimize=False --debug
```


When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This take a minute or so to get started, but then allows you to hot-reload your javascript extension.
To see a change, save your javascript, watch the terminal for an update.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

Optionally you can manually download a depndencies and libraries with examples add them to a PYTHONPATH
if you do not want to install them.
```
export PYTHONPATH="$PYTHONPATH:$PWD/pyMathBitPrecise:$PWD/pyDigitalWaveTools:$PWD/hdlConvertorAst:\
$PWD/ipCorePackager:$PWD/pycocotb:$PWD/hwt:$PWD/hwtLib:$PWD/hwtGraph"
```
before running jupyter.