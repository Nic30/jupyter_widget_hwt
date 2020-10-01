#!/usr/bin/python3
# -*- coding: utf-8 -*-
import IPython.core.compilerop
import hashlib
from notebook.notebookapp import main
from pathlib import Path
import re
import sys
import tempfile
import os


# script used to execute jupyter notebook from other IDEs with support for debugger
# [note] if debugger is stoped on some breakpoint the debug console works
#        just the output is redirected to notebook and it can be viewed there
if __name__ == '__main__':
    # in order to have all files in correct paths this script has to be executed in git root
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    # https://gist.github.com/bsdz/349a750eac042301e910bc9cec8cd65c
    ipython_code_cache = Path(tempfile.gettempdir()) / "ipython_cache"
    ipython_code_cache.mkdir(parents=True, exist_ok=True)

    def code_name2(code, number=0):
        hash_digest = hashlib.sha1(code.encode("utf-8")).hexdigest()
        fp = ipython_code_cache / \
            f'ipython-input-{number}-{hash_digest[:12]}.py'
        fp.write_text(code)
        return str(fp)

    IPython.core.compilerop.code_name = code_name2

    # /usr/local/bin/jupyter-notebook
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    #sys.argv.append("notebook")
    sys.exit(main())
