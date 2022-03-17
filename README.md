# jupyter-tempvars
Jupyter extension providing automatic management of per-cell temporary variables

*Project is early-alpha WIP. Notes here are for future cleanup into a proper README.*

Jupyter notebooks are great for exploratory data analysis,
but a big problem with them is the potential for namespace pollution.
Something you define in one cell is accidentally used in another cell...
you make a typo and accidentally refer to something from another cell...
you run cells in a different order, and a "temporary" variable in a cell
causes the calculation in the cell you run to give different results,
or throw an exception.

What would be nice, is to have an easy way of declaring certain variables
to be "cell-local" -- to be temporary variables, not meant to survive
the scope of the cell in which they're used.

This repo is a Jupyter notebook extension providing exactly this functionality.
It's built on the `tempvars` Python package, which provides a context manager
allowing this kind of temporary variable management. This extension wires into
the cell execution machinery to automatically surround every cell with
a `TempVars` context manager, with the variable identification/definition
defined by a line magic:

```
%tempvars start_with t_
```

This line magic will cause all variables whose names start with `t_` to behave
as temporary variables: They will be unset before cell execution, and
any that are created in the course of cell execution will be
deleted after cell execution.

The other way currently to define temp vars is:

```
%tempvars end_with _t
```

