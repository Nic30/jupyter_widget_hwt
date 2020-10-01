from traitlets import Unicode, Dict, Int

from hwt.synthesizer.utils import synthesised
from hwtGraph.elk.containers.idStore import ElkIdStore
from hwtGraph.elk.fromHwt.convertor import UnitToLNode
from hwtGraph.elk.fromHwt.defauts import DEFAULT_PLATFORM, \
    DEFAULT_LAYOUT_OPTIMIZATIONS
import ipywidgets as widgets
from hwt.synthesizer.rtlLevel.rtlSignal import RtlSignal
from hwt.hdl.operator import Operator
from hwt.synthesizer.unit import Unit
from hwt.hdl.portItem import HdlPortItem
from hwt.synthesizer.interface import Interface


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

        self.u = u
        self.graph = None
        self.json_idStore = None
        self.hwt_obj_to_j_obj_ids = None
        self.id_to_j_obj = None
        if u is not None:
            self._bind_unit(u)

    
    def _bind_unit(self, u: Unit):
        synthesised(u, DEFAULT_PLATFORM)
        self.graph = UnitToLNode(u, optimizations=DEFAULT_LAYOUT_OPTIMIZATIONS)
        self.json_idStore = ElkIdStore()
        self.value = self.graph.toElkJson(self.json_idStore)
    
    def _init_hwt_obj_to_json_mapping_dicts(self):
        # 1:1
        id_to_j_obj = {}

        def walk_json(obj):
            _id = obj.get("id", None)
            if _id is not None:
                id_to_j_obj[_id] = obj

            for prop in ("ports", "children", "edges"):
                obj_list = obj.get(prop, None)
                if obj_list:
                    for o in obj_list:
                        walk_json(o)

        walk_json(self.value)

        # N:M
        hwt_obj_to_j_obj_ids = {}
        for l_obj, j_id in self.json_idStore.items():
            _hwt_obj = l_obj.originObj
            if isinstance(_hwt_obj , (Unit, RtlSignal, Operator)):
                hwt_obj_to_j_obj_ids.setdefault(_hwt_obj, set()).add(j_id)
            elif isinstance(_hwt_obj, HdlPortItem):
                if _hwt_obj.src is not None:
                    hwt_obj_to_j_obj_ids.setdefault(_hwt_obj.src, set()).add(j_id)

                if _hwt_obj.dst is not None:
                    hwt_obj_to_j_obj_ids.setdefault(_hwt_obj.dst, set()).add(j_id)
            else:
                raise NotImplementedError(_hwt_obj)
        self.hwt_obj_to_j_obj_ids = hwt_obj_to_j_obj_ids
        self.id_to_j_obj = id_to_j_obj

    def set_style_for_hwt_obj(self, hwt_obj, style_str:str):
        if self.hwt_obj_to_j_obj_ids is None:
            self._init_hwt_obj_to_json_mapping_dicts()

        if isinstance(hwt_obj, Interface):
            hwt_obj = hwt_obj._sigInside

        j_ids = self.hwt_obj_to_j_obj_ids[hwt_obj]
        for j_id in j_ids:
            j_obj = self.id_to_j_obj[str(j_id)]
            j_obj["hwMeta"]["cssStyle"] = style_str
        
        v = self.value
        #v._notify_trait("value", v, v)
        self.value = {}
        self.value = v

