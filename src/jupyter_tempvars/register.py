r"""``jupyter_tempvars`` *extension registration function module*.

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


def _jupyter_nbextension_paths():
    """Provide paths for client-side extensions.

    This is where the extension actually gets linked in.

    """
    # TODO: Figure out if 'src' and 'dest' are actually correct here.
    return [
        {
            "section": "notebook",
            "src": "extension",
            "dest": "extension",
        }
    ]
