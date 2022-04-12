## CHANGELOG: jupyter-tempvars -- Convenient temporary variable management in Jupyter Notebook

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project strives to adhere to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html).


### [0.1.post1] - 2022-04-11

#### Administrative

- Fix semantic error in README.md regarding variable restoration behavior
  after code cell execution (variables *are* restored by default)


### [0.1] - 2022-04-06

#### Features

- Per-cell temporary variable filtering based on starts-with and ends-with
  filters.
- `pip`-installable packaging for PyPI upload using the recent
  PEP621 `pyproject.toml` project config for `setuptools`.
- Includes a helper script to simplify installation/upgrade of the
  extension files to the user-space Jupyter extension location.
