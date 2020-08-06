from io import StringIO
from sys import stderr
import unittest

from traitlets import Unicode, Dict

from hwt.simulator.rtlSimulatorJson import BasicRtlSimulatorJson
import ipywidgets as widgets


# See js/lib/scheme.js for the frontend counterpart to this file.
@widgets.register
class HwtSignalDumpWidget(widgets.DOMWidget):

    # Name of the widget view class in front-end
    _view_name = Unicode('HwtSignalDumpView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('HwtSignalDumpModel').tag(sync=True)

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
    width = Unicode("800").tag(sync=True)
    height = Unicode("250").tag(sync=True)

    def __init__(self, unittest_test, *args, **kwargs):
        """
        :param unittest_test: UnittestTestCaseCls('test_name')
        """
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

        super(HwtSignalDumpWidget, self).__init__(*args, **kwargs)
        orig_runSim = unittest_test.runSim
        orig_sim = unittest_test.DEFAULT_SIMULATOR
        signal_data = {}

        def runSim(*args, **kwargs):
            # run sim which overrides the log file with a json container for data
            unittest_test.DEFAULT_LOG_DIR = None
            unittest_test.rtl_simulator.set_trace_file(signal_data, -1)
            orig_runSim(*args, **kwargs)

        suite = unittest.TestSuite()
        try:
            unittest_test.runSim = runSim
            unittest_test.__class__.DEFAULT_SIMULATOR = BasicRtlSimulatorJson

            suite.addTest(unittest_test)
            out_log = StringIO()
            runner = unittest.TextTestRunner(stream=out_log, verbosity=0)
            res = runner.run(suite)
            if res.errors or res.failures:
                stderr.write(str(res))
                stderr.write(out_log.getvalue())
        except Exception:
            # we are printing the error message but we still want to see the simulation output
            pass
        finally:
            unittest_test.__class__.DEFAULT_SIMULATOR = orig_sim
            unittest_test.runSim = orig_runSim
        self.value = signal_data