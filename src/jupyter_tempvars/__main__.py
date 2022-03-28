r"""``jupyter_tempvars`` *package execution module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    25 Mar 2022

**Copyright**
    \(c) Brian Skinn 2022

**Source Repository**
    https://github.com/bskinn/jupyter-tempvars

**Documentation**
    *(pending)*

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import sys

from jupyter_tempvars.cli import main

# Spoof so help usage shows "jupyter-tempvars"
sys.argv[0] = "jupyter-tempvars"
sys.exit(main())
