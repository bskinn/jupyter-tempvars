r"""``jupyter_tempvars`` *IPython extension registration function module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    18 Mar 2022

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

from IPython.core.magic import register_line_magic
from IPython.display import display, Javascript


def load_ipython_extension(ipython):
    """Register the magics and configure the globals."""

    @register_line_magic
    def tempvars(line):
        subcommand, arg = line.strip().split(" ")

        if subcommand == "universal":
            # TODO: Error if not a boolean word
            display(
                Javascript(
                    "Jupyter.notebook.metadata['tempvars']['universal'] "
                    f"= {arg.lower()};"
                )
            )
