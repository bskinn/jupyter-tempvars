r"""``jupyter_tempvars`` *error hierarcy definition module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    20 Mar 2022

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


class JupyterTempvarsError(Exception):
    """Parent class for all jupyter_tempvars errors."""


class JupyterTempvarsMagicError(JupyterTempvarsError):
    """Error in IPython magic usage."""

    def __init__(self, *, magic: str, command: str, msg: str) -> None:
        """Initialize the exception instance."""
        self.magic = magic
        self.command = command
        self.msg = msg

    def __str__(self):
        """Return str error representation."""
        return f"Command '{self.command}' invalid for %{self.magic}: {self.msg}"
