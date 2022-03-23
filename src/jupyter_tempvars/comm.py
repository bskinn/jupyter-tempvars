r"""``jupyter_tempvars`` *message comm definition module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    23 Mar 2022

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

from ipykernel.comm import Comm

from jupyter_tempvars.const import COMM_NAME


def recreate_comm():
    """Generate a new instance of the comm."""
    return Comm(target_name=COMM_NAME)
