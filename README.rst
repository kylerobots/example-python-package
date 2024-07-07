Example Python Package
======================

A collection of modern (mostly) best practices implemented in a simple package template. This is designed to allow easy
reference for future projects.

The library itself is just a simple math library with addition, subtraction, multiplication, and division. But it comes
with a number of features.

.. contents:: Table of Contents
    :backlinks: entry
    :local:

The Package Itself
------------------

This package provides a single module, ``example_python_package.simple_math``, with 4 functions: ``add``, ``subtract``,
``multiply``, and ``divide``. Each of these functions takes two arguments and returns
the result of the operation.

There is also a script, ``example_python_package.example.example.py`` that takes two numbers from the command line,
calls all 4 function in turn, and prints the results to the console. This is included to demonstrate the use of the
library.

Included features
-----------------

These are the included features. This README is not an exhaustive guide to each feature. It merely points out which are
in use with some light explanation and often a link to the relevant documentation. Please refer to that documentation
for implementation details.

Code Coverage
^^^^^^^^^^^^^

There is a VS Code task to run and report the code coverage of the unit tests. There is also a job in the
*.github/workflows/pull-request.yml* GitHub workflow that does the same and comments the results on the Pull Request.
This uses `Coverage <https://coverage.readthedocs.io>`_.

Conventional Commit Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^

This package includes a Git pre-commit hook that ensures all commit messages follow the
`Conventional Commits <https://www.conventionalcommits.org>`_ standard. The setup uses
`this repository <https://github.com/compilerla/conventional-pre-commit>`_. After installing the Poetry dev group, just
run ``pre-commit install --hook-type commit-msg``.

.. warning:: This check is not enforced for all developers. Each contributor would need to run this locally to ensure it
    applies.

Additionally, there is an job in the *.github/workflows/pull-request.yml* file that checks all Git commits in a Pull
Request and fails if they do not all follow the convention. This would ensure any developers contributing to the project
adhere to this standard.

Documentation
^^^^^^^^^^^^^

This package includes documentation using `Sphinx <https://www.sphinx-doc.org/en/master/>`_. The documentation can be
built locally with a VS Code task and is automatically built and published to GitHub Pages on each new release.

The documentation contains an API that is automatically generated from the docstrings in the code. It involves running
the *Build API ReStructuredText Files* task in VS Code, then making some light edits to adjust appearance.


Linting
^^^^^^^

This package uses `Ruff <https://docs.astral.sh/ruff/>`_ for linting. Additionally, there are settings for the
`VS Code extension <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>`_ and a job on the Pull
Request workflow that verifies that all checks pass.

The project enables a number of rules, as defined in the *pyproject.toml* file. There are plenty more available, as
documented on Ruff's site. This is just a collection that are plausibly relevant to the purpose of the package here.

Ruff also provides formatting, so it is configured to format the code on save.

Package Publishing
^^^^^^^^^^^^^^^^^^

There is a workflow file called *.github/workflows/release.yml* that will automatically build and push to
`TestPyPi <https://test.pypi.org/>`_ when a new Release is released. It uses Poetry for the build and push. It publishes
to TestPyPi because this isn't a real package that does anything useful, so it is published somewhere that won't
pollute. The process for publishing to PyPi is the same though.

This same workflow will also upload the built files to the Release itself for manual download and installation.

Poetry
^^^^^^

This package uses `Poetry <https://python-poetry.org/>`_ to do all the package management, including dependencies and
installation. The *pyproject.toml* file contains the necessary information. The environment can be set up locally with
``poetry install`` and run with ``poetry run <command>``.

Pyenv Python Versions
^^^^^^^^^^^^^^^^^^^^^

There is a *.python-version* file that specifies which versions of Python `pyenv <https://github.com/pyenv/pyenv>`_ can
support. Just install pyenv per instructions, install the recommended build dependencies, then the desired Python
versions. This will allow you to have multiple different Python versions at once.

Release Drafts
^^^^^^^^^^^^^^

There is a GitHub workflow job that automatically drafts release notes based on Pull Requests. It uses an Action called
`release-drafter <https://github.com/release-drafter/release-drafter>`_. This action is configured to group info based
on the tag type (e.g. *build*, *documentation*, etc.) and can automatically determine the next version using the same
tags.

Unit Testing
^^^^^^^^^^^^

There are several unit tests that check the package. They use `pytest <https://docs.pytest.org/en/8.2.x/index.html>`_.
Additionally, there is a workflow that runs on each Pull Request that runs unit tests over multiple versions of
operating systems and Python versions. This workflow also runs the example script as a form of end-to-end testing.

There is also a file called *noxfile.py* that demonstrates one way to use
`Nox <https://nox.thea.codes/en/stable/index.html>`_ to test multiple versions of Python and multiple dependency
versions. The goal here is not to provide a repeatable CI unit test, but rather to help determine the minimum
supported versions of a dependency to specify in the *pyproject.toml* file.

Acknowledgements
----------------

This guide was partly inspired by
`Claudio Jolowicz's series of blog posts <https://cjolowicz.github.io/posts/hypermodern-python-01-setup/>`_.
