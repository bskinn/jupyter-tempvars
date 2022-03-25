# jupyter-tempvars: Convenient temporary variable management in Jupyter Notebook

**Do you work in Jupyter Notebook?**

**Are your notebooks flaky sometimes, due to leftover/temporary variables?**

`jupyter-tempvars` can help!

Namespace pollution with leftover/temporary variables is a
common challenge of using Jupyter notebooks. It's a downside
of the power provided by the shared global notebook namespace,
for things like exploratory data analysis.

And, it can be a pretty big downside. It's quite annoying
to work for hours to try to figure out what's wrong with a notebook,
only to have it suddenly work properly when you restart Jupyter.
It's also quite annoying to have a workbook that you *thought*
was working correctly, suddely *stop* working once you restart.
It can cause even bigger problems if you pass a notebook
on to someone else, and then it doesn't work right for them even
though it was working fine for you.

`jupyter-tempvars` is a Jupyter nbextension built on the
[`tempvars` Python package](https://github.com/bskinn/tempvars)
that helps minimize these kinds of problems. Simply decorate code
cells with metadata tags matching a defined template, and then variables
that fit the rules you define will be automatically treated
as temporary variables. This means that:

 1. Matching variables will be removed from the global namespace before
    each tagged cell is executed, ensuring that cell isn't contaminated
    by "dragged-in" variables, ***and***

 2. Matching variables will be removed from the global namespace after the cell has
    finished executing, ensuring that other code cells aren't contaminated by
    this cell, either.


## Prerequisites

### Python

I've been developing `jupyter-tempvars` using Python 3.9, but I believe any
version of Python 3 that works with the underlying `tempvars` library
(and that should be all actively maintained versions, 3.7+!) should work fine.

### Jupyter

`jupyter-tempvars` requires a full instance of [Jupyter Notebook](https://jupyter.org/),
including the Javascript frontend. So far, I've only tested it with vanilla Jupyter,
but in theory I think it should work with JupyterHub, Jupyter in Anaconda, etc.
I would be grateful for feedback from anyone who tries to use it in
other contexts. I believe it should work with `notebook` versions 4.x and above.
Note that `jupyter-tempvars` will **NOT** work with JupyterLab!

To get a basic Jupyter install just `pip install jupyter`.

### `jupyter-contrib-nbextensions`

The community-developed
[`jupyter-contrib-nbextensions` package](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)
is not strictly required in order to use `jupyter-tempvars`, but it's highly recommended.
If nothing else, the configurator plugin that adds a `Nbextensions` tab to the
main Jupyter interface is really handy. See the install instructions
[here](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html).


## Installation


- `jupyter-tempvars`
  - `pip`
  - `jupyter nbextension install --user --py jupyter_tempvars`
  - If no configurator: `jupyter nbextension enable jupyter_tempvars --user --py`
- Run Jupyter
- Turn on 'Temporary Variables' in the `Nbextensions` tab

## Usage

*Right now, just cell tag metadata and starts/ends.*


## Advanced Variable Management via `tempvars`

`jupyter-tempvars` only exposes a subset of the functionality
provided by the underlying `tempvars` Python package. If you need
a more powerful temporary variable
management tool, take a look at the
[full capabilities](https://tempvars.readthedocs.io/en/latest/usage.html) of `tempvars`.

`jupyter-tempvars` also requires the full Jupyter notebook frontend to function.
If you want to manage temporary variables when using, e.g.,
[`nbclient`](https://github.com/jupyter/nbclient) or
[`nbmake`](https://github.com/treebeardtech/nbmake),
you should look into using `tempvars` directly in your code,
instead of `jupyter-tempvars`.

----

Available (soon) on [PyPI](https://pypi.org/project/jupyter-tempvars).

Source on [GitHub](https://github.com/bskinn/jupyter-tempvars).
Bug reports and feature requests are welcomed at the
[Issues](https://github.com/bskinn/jupyter-tempvars/issues) page there.

Copyright (c) Brian Skinn 2022

License: The MIT License. See
[LICENSE.txt](https://github.com/bskinn/sphobjinv/blob/main/LICENSE.txt)
for full license terms.
