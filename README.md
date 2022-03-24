# jupyter-tempvars: Convenient temporary variable management in Jupyter Notebook

**Do you work in Jupyter Notebook a lot?**

**Are your notebooks flaky sometimes, due to leftover temporary variables?**

`jupyter-tempvars` can help!

Namespace pollution with leftover/temporary variables is a well known
and widespread challenge with using Jupyter notebooks. It's a downside
of the huge power of the shared global notebook namespace for things
like exploratory data analysis.

Singular annoyance of having a notebook not work right, and then
suddenly work right when you restart. OR, having a notebook working,
and then it *stops* working once you restart. Or, you pass the notebook
on to someone else, and they can't reproduce your results.

`jupyter-tempvars` is a Jupyter nbextension built on the
[`tempvars` Python package](https://github.com/bskinn/tempvars)
that helps minimize these kinds of problems. Simply decorate code
cells with tags indicating
the name structure that marks temporary variables, and those variables
will be automatically removed from the namespace both before and after
that cell is executed. No more carrying in existing variables from
the global namespace, and no more leaking variables back out!

To note, `jupyter-tempvars` (i) only exposes a subset of the functionality
provided by `tempvars`, and (ii) requires the full Jupyter notebook
Javascript frontend to function. If you need a more powerful temporary variable
management tool, or if you want to manage temporary variables
when using, e.g., [`nbmake`](https://github.com/treebeardtech/nbmake),
take a look at [the capabilities of `tempvars`](https://tempvars.readthedocs.io/en/latest/usage.html).

## Installation

- `jupyter`
  - `pip`
  - Anaconda
  - others?
- `jupyter-contrib-nbextensions`
  - Mainly for the configurator
- `jupyter-tempvars`
  - `pip`
  - `jupyter nbextension install --user --py jupyter_tempvars`
  - If no configurator: `jupyter nbextension enable jupyter_tempvars --user --py`
- Run Jupyter
- Turn on 'Temporary Variables' in the `Nbextensions` tab

## Usage

*Right now, just cell tag metadata and starts/ends.*


----

Available (soon) on [PyPI](https://pypi.org/project/jupyter-tempvars).

Source on [GitHub](https://github.com/bskinn/jupyter-tempvars).
Bug reports and feature requests are welcomed at the
[Issues](https://github.com/bskinn/jupyter-tempvars/issues) page there.

Copyright (c) Brian Skinn 2022

License: The MIT License. See
[LICENSE.txt](https://github.com/bskinn/sphobjinv/blob/main/LICENSE.txt)
for full license terms.
