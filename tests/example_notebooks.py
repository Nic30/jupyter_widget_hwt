import os
import unittest

from nbclient.tests.test_client import run_notebook, assert_notebooks_equal
from nbconvert.exporters.exporter import ResourcesDict


#def run_notebook(fname):
#    with open(fname) as f:
#        input_nb = nbformat.read(f, 4)
#        with pytest.warns(FutureWarning):
#            output_nb = executenb(deepcopy(input_nb))
ROOT = os.path.join(os.path.dirname(__file__), "..")


def notebook_resources():
    """Prepare a notebook resources dictionary for executing test notebooks in the `files` folder."""
    res = ResourcesDict()
    res['metadata'] = ResourcesDict()
    res['metadata']['path'] = os.path.join(ROOT, 'examples')
    return res


class ExampleNotebooksTC(unittest.TestCase):

    def check_notebook(self, name, opts={}):
        input_file = os.path.join(ROOT, 'examples', name)
        input_nb, output_nb = run_notebook(input_file, opts, notebook_resources())
        assert_notebooks_equal(input_nb, output_nb)

    def test_example_scheme_cuckoo_hash(self):
        self.check_notebook('example_scheme_cuckoo_hash.ipynb')

    def test_example_scheme(self):
        self.check_notebook('example_scheme.ipynb')

    def test_example_signal_dump(self):
        self.check_notebook('example_signal_dump.ipynb')

    def test_hwt_tutorial_0_component_export(self):
        self.check_notebook('hwt_tutorial_0_component_export.ipynb')

    def test_hwt_tutorial_1_simulation(self):
        self.check_notebook('hwt_tutorial_1_simulation.ipynb')

    def test_hwt_tutorial_2_custom_interface(self):
        self.check_notebook('hwt_tutorial_2_custom_interface.ipynb')

    def test_hwt_tutorial_3_hdl_syntax(self):
        self.check_notebook('hwt_tutorial_3_hdl_syntax.ipynb')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExampleNotebooksTC))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

