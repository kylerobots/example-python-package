# Example Python Package #

A collection of modern (mostly) best practices implemented in a simple package template. This is designed to allow easy
reference for future projects.

The library itself is just a simple math library with addition, subtraction, multiplication, and division. But it comes
with a number of features.

## Table of Contents ##

1. [The Package Itself](#the-package-itself)
2. [Included Features](#included-features)
    - [Conventional Commit Checks](#conventional-commit-checks)
    - [Package Publishing](#package-publishing)
    - [Poetry](#poetry)
    - [Pyenv Python Versions](#pyenv-python-versions)
    - [Release Drafts](#release-drafts)
    - [Unit Testing](#unit-testing)
3. [Acknowledgements](#acknowledgements)

## The Package Itself ##

This package provides a single module, `simple_math`, with 4 functions: `add`, `subtract`, `multiply`, and `divide`.
They each perform their equivalent math operation.

There is also a script in `example` that takes two numbers from the command line, calls all 4 functions in turn, and
prints the results to the console. This is included to demonstrate the use of the library.

## Included Features ##

These are the included features. This README is not an exhaustive list of all features. It merely points out which are
in use with some light explanation and often a link to the relevant documentation. Please refer to that documentation
for implementation details.

### Conventional Commit Checks ###

This package includes a Git pre-commit hook that ensures all commit messages follow the
[Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) standard. The setup uses
[this repository](https://github.com/compilerla/conventional-pre-commit). After installing the Poetry dev group, just
run `pre-commit install --hook-type commit-msg`. **Note:** this check is not enforced for all developers. Each
contributor would need to run this locally to ensure it applies.

Additionally, there is an Action in the `.github/workflows/conventional-commit.yml` file that checks all Git commits in
a Pull Request and errors if they do not all follow the convention. This would ensure any developers contributing to the
project adhere to this standard.

### Package Publishing ###

There is a workflow file called `python-publish.yml` that will automatically build and push to
[TestPyPi](https://test.pypi.org/) when a new Release is released. It uses Poetry for the build and push. It publishes
to TestPyPi because this isn't a real package that does anything useful, so it is published somewhere "out of the way."

### Poetry ###

This package uses [Poetry](https://python-poetry.org/) to do all the package management, including dependencies and
installation. The `pyproject.toml` file contains the necessary information. The environment can be set up locally with
`poetry install` and run with `poetry run <command>`.

### Pyenv Python Versions ###

There is a `.python-version` file that specifies which versions of Python [pyenv](https://github.com/pyenv/pyenv) can
support. Just install `pyenv` per instructions, install the recommended build dependencies, then the desired Python
versions. This will allow you to have multiple different Python versions at once.

### Release Drafts ###

There is a GitHub workflow that automatically drafts release notes based on pull requests. It uses an Action called
[release-drafter](https://github.com/release-drafter/release-drafter). This action is configured to group info based on
tag type (e.g. `build`, `documentation`, etc.) and can automatically determine the next version use the same tags.

### Unit Testing ###

There are several unit tests that check the package. They use [pytest](https://docs.pytest.org/en/8.2.x/index.html).
Additionally, there is a workflow that runs on each Pull Request that runs unit tests over multiple versions of
operating systems and Python versions, then outputs the results as a comment on the PR. The Action that does the
summarization also includes instructions on how to output a badge on the README, but that is not included here.

There is also a file called `noxfile.py` that demonstrates one way to use
[Nox](https://nox.thea.codes/en/stable/index.html) to test multiple versions of Python and multiple dependency versions.
The goal here is not to provide a consistent CI unit test, but rather to help determine minimum supported versions of a
dependency to specify in the `pyproject.toml` file.

## Acknowledgements ##

This guide was partly inspired by
[Claudio Jolowicz's series of blog posts](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
