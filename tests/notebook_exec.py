import os
import sys

from nbconvert.preprocessors import ExecutePreprocessor
import nbformat


def run_notebook(notebook_path):
    nb_name, _ = os.path.splitext(os.path.basename(notebook_path))
    dirname = os.path.dirname(notebook_path)

    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    proc = ExecutePreprocessor(
        timeout=5000,
        kernel_name='python%d' % sys.version_info.major)
    proc.allow_errors = True

    test_out_dir = os.path.join(dirname, "test_outputs")
    os.makedirs(test_out_dir, exist_ok=True)

    proc.preprocess(nb, {'metadata': {'path': dirname}})
    output_path = os.path.join(test_out_dir, '{}.ipynb'.format(nb_name))

    with open(output_path, mode='wt') as f:
        nbformat.write(nb, f)

    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)

    return nb, errors
