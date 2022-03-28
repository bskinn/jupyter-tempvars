r"""``jupyter_tempvars`` *module for CLI helpers*.

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

import argparse as ap
import subprocess as sp


def main():
    """Run the CLI."""
    prs = get_parser()

    params = vars(prs.parse_args())
    prs_command = params["command"]

    if prs_command == "install":
        command = [
            "jupyter",
            "nbextension",
            "install",
            "--user",
            "--py",
            "jupyter_tempvars",
        ]
    elif prs_command == "enable":
        command = [
            "jupyter",
            "nbextension",
            "enable",
            "--user",
            "jupyter_tempvars/jupyter_tempvars",
        ]
    elif prs_command == "disable":
        command = [
            "jupyter",
            "nbextension",
            "disable",
            "--user",
            "jupyter_tempvars/jupyter_tempvars",
        ]

    sp_result = sp.run(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True, timeout=20)

    print(sp_result.stdout)

    return sp_result.returncode


def get_parser():
    """Construct the argument parser."""
    prs = ap.ArgumentParser(
        description="Extension (un)install helper for jupyter-tempvars"
    )

    prs.add_argument("command", choices=["install", "enable", "disable"])

    return prs
