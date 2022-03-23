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
    SETTINGS_IDENTIFIER,
    SETTINGS_KEY_END_WITH,
    SETTINGS_KEY_START_WITH,
    SETTINGS_KEY_UNIVERSAL,
)

DEFAULT_METADATA = {
    SETTINGS_KEY_UNIVERSAL: False,
    SETTINGS_KEY_START_WITH: [],
    SETTINGS_KEY_END_WITH: [],
}

KEY_SUBCOMMAND = "subcommand"
SUBCOMMAND_UNIVERSAL = "universal"
SUBCOMMAND_START_WITH = "start_with"
SUBCOMMAND_END_WITH = "end_with"


def load_ipython_extension(ipython):
    """Register the magics and configure the globals."""
    ns = ipython.user_ns

    ns.update({SETTINGS_IDENTIFIER: DEFAULT_METADATA})
    settings = ns[SETTINGS_IDENTIFIER]

    prs = _get_parser()

    @register_line_magic
    def tempvars(line):
        try:
            arg_vars = vars(prs.parse_args(shlex.split(line)))
        except ap.ArgumentError as e:
            _handle_invalid_magic(e)
            return

        if arg_vars[KEY_SUBCOMMAND] == SUBCOMMAND_UNIVERSAL:
            _handle_universal(arg_vars[SETTINGS_KEY_UNIVERSAL], settings)

        if arg_vars[KEY_SUBCOMMAND] == SUBCOMMAND_START_WITH:
            _handle_start_with(arg_vars[SETTINGS_KEY_START_WITH], settings)

        if arg_vars[KEY_SUBCOMMAND] == SUBCOMMAND_END_WITH:
            _handle_end_with(arg_vars[SETTINGS_KEY_END_WITH], settings)


def _handle_universal(arg, settings):
    """Apply the indicated value to the 'universal' setting."""
    settings.update({SETTINGS_KEY_UNIVERSAL: arg in ["1", "true", "on"]})


def _handle_start_with(arg, settings):
    """Apply the indicated list of prefixes to the 'start_with' setting."""
    settings.update({SETTINGS_KEY_START_WITH: arg})


def _handle_end_with(arg, settings):
    """Apply the indicated list of suffixes to the 'end_with' setting."""
    settings.update({SETTINGS_KEY_END_WITH: arg})


def _handle_invalid_magic(exc):
    """Process and report any argparse parsing problems."""
    print(f"({exc.argument_name}) {exc.message}")


def _get_parser():
    """Construct the parser for the magic."""
    prs_options = {"exit_on_error": False, "allow_abbrev": False, "add_help": False}

    prs = ap.ArgumentParser(prog="jupyter_tempvars", **prs_options)

    subs = prs.add_subparsers(dest=KEY_SUBCOMMAND, required=True)

    universal = subs.add_parser(SUBCOMMAND_UNIVERSAL, **prs_options)
    universal.add_argument(
        SETTINGS_KEY_UNIVERSAL,
        type=str.lower,
        choices=["0", "1", "true", "false", "on", "off"],
        help="Set the toggle state for universal mode",
    )

    start_with = subs.add_parser(SUBCOMMAND_START_WITH, **prs_options)
    start_with.add_argument(
        SETTINGS_KEY_START_WITH,
        type=str,
        nargs="*",
        help="Set the prefix(es) marking temporary variable names",
    )

    end_with = subs.add_parser(SUBCOMMAND_END_WITH, **prs_options)
    end_with.add_argument(
        SETTINGS_KEY_END_WITH,
        type=str,
        nargs="*",
        help="Set the suffix(es) marking temporary variable names",
    )

    return prs
