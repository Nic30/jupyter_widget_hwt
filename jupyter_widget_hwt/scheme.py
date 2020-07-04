from traitlets import Unicode, Dict, Int

from hwt.synthesizer.utils import synthesised
from hwtGraph.elk.containers.idStore import ElkIdStore
from hwtGraph.elk.fromHwt.convertor import UnitToLNode
from hwtGraph.elk.fromHwt.defauts import DEFAULT_PLATFORM,\
    DEFAULT_LAYOUT_OPTIMIZATIONS
import ipywidgets as widgets


# See js/lib/scheme.js for the frontend counterpart to this file.
@widgets.register
class HwtSchemeWidget(widgets.DOMWidget):

    # Name of the widget view class in front-end
    _view_name = Unicode('HwtSchemeView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('HwtSchemeModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('jupyter_widget_hwt').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('jupyter_widget_hwt').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.0.1').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.0.1').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is
    # touched.
    value = Dict({}).tag(sync=True)
    width = Unicode("800px").tag(sync=True)
    height = Unicode("250px").tag(sync=True)

    def __init__(self, u, *args, **kwargs):
        try:
            height = kwargs["height"]
            if isinstance(height, int):
                kwargs["height"] = "%dpx" % height
        except KeyError:
            pass

        try:
            width = kwargs["width"]
            if isinstance(width, int):
                kwargs["width"] = "%dpx" % width
        except KeyError:
            pass
        super(HwtSchemeWidget, self).__init__(*args, **kwargs)
        if u is not None:
            synthesised(u, DEFAULT_PLATFORM)
            g = UnitToLNode(u, optimizations=DEFAULT_LAYOUT_OPTIMIZATIONS)
            idStore = ElkIdStore()
            data = g.toElkJson(idStore)
            self.value = data
