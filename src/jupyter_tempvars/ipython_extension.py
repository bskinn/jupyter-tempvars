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

import argparse as ap
import shlex

from IPython.core.magic import register_line_magic

from jupyter_tempvars.const import (
    METADATA_IDENTIFIER,
    METADATA_KEY_END,
    METADATA_KEY_START,
    METADATA_KEY_UNIVERSAL,
)

DEFAULT_METADATA = {
    METADATA_KEY_UNIVERSAL: False,
    METADATA_KEY_START: [],
    METADATA_KEY_END: [],
}

KEY_SUBCOMMAND = "subcommand"
SUBCOMMAND_UNIVERSAL = "universal"


def load_ipython_extension(ipython):
    """Register the magics and configure the globals."""
    ns = ipython.user_ns

    ns.update({METADATA_IDENTIFIER: (metadata := DEFAULT_METADATA)})

    @register_line_magic
    def tempvars(line):
        # TODO: Expand this arg parse with user-friendly error
        # explaining. Prob expand to new function.
        arg_vars = vars(_get_parser().parse_args(shlex.split(line)))

        if arg_vars[KEY_SUBCOMMAND] == SUBCOMMAND_UNIVERSAL:
            _handle_universal(arg_vars[METADATA_KEY_UNIVERSAL], metadata)


def _handle_universal(arg, metadata):
    """Apply the indicated value to the 'universal' setting."""
    metadata.update({METADATA_KEY_UNIVERSAL: arg in ["1", "true", "on"]})


def _get_parser():
    """Construct the parser for the magic."""
    prs = ap.ArgumentParser(exit_on_error=False, allow_abbrev=False)

    subs = prs.add_subparsers(dest=KEY_SUBCOMMAND, required=True)

    universal = subs.add_parser(SUBCOMMAND_UNIVERSAL)
    universal.add_argument(
        METADATA_KEY_UNIVERSAL,
        type=str.lower,
        choices=["0", "1", "true", "false", "on", "off"],
        help="Set the toggle state for universal mode",
    )

    return prs
