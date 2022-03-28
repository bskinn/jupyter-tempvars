r"""``jupyter_tempvars`` *package definition module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    17 Mar 2022

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


from jupyter_tempvars.version import __version__


def _jupyter_nbextension_paths():
    """Provide paths for client-side extensions.

    This is where the extension actually gets linked in.

    """
    return [
        {
            "section": "notebook",
            "src": "extension",
            "dest": "jupyter_tempvars",
        }
    ]
