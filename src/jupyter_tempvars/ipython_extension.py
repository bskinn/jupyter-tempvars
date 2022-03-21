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

from jupyter_tempvars.const import MD_IDENTIFIER, MD_UNIVERSAL
from jupyter_tempvars.error import JupyterTempvarsMagicError


def load_ipython_extension(ipython):
    """Register the magics and configure the globals."""
    ns = ipython.user_ns

    ns.update({MD_IDENTIFIER: (metadata := {})})

    @register_line_magic
    def tempvars(line):
        # TODO: Parse these arguments properly (e.g., argparse)
        subcommand, arg = line.strip().split(" ")

        if subcommand == "universal":
            _handle_universal(subcommand, arg, metadata)


def _handle_universal(subcommand, arg, metadata):
    """Apply the indicated value to the 'universal' setting."""
    if arg.isnumeric() and ((val := int(arg)) == 1 or val == 0):
        print(arg, val)
        val = bool(val)
    elif arg.lower() == "true":
        val = True
    elif arg.lower() == "false":
        val = False
    else:
        raise JupyterTempvarsMagicError(
            magic="tempvars", command=subcommand, msg="Must be true/false or 0/1."
        )

    metadata.update({MD_UNIVERSAL: val})
