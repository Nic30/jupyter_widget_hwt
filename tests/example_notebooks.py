import os
import unittest

from nbclient.tests.test_client import run_notebook, normalize_output
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
        self.assert_notebooks_equal(input_nb, output_nb)

    def assert_notebooks_equal(self, expected, actual):
        # based on nbclient.tests.test_client.assert_notebooks_equal
        expected_cells = expected['cells']
        actual_cells = actual['cells']
        self.assertEqual(len(expected_cells), len(actual_cells))
    
        for expected_cell, actual_cell in zip(expected_cells, actual_cells):
            # Uncomment these to help debug test failures better
            expected_outputs = expected_cell.get('outputs', [])
            actual_outputs = actual_cell.get('outputs', [])
            normalized_expected_outputs = list(map(normalize_output, expected_outputs))
            normalized_actual_outputs = list(map(normalize_output, actual_outputs))
            self.assertListEqual(normalized_expected_outputs, normalized_actual_outputs)
    
            expected_execution_count = expected_cell.get('execution_count', None)
            actual_execution_count = actual_cell.get('execution_count', None)
            self.assertEqual(expected_execution_count, actual_execution_count)

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

